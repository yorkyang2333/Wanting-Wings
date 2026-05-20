#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess

PROJECT_DIR = "/Applications/Wanting.Wings.v2.0"
SDK_DIR = "/Applications/renpy-8.5.2-sdk"
LAUNCHER_SH = os.path.join(SDK_DIR, "renpy.sh")
DIST_DIR = os.path.join(PROJECT_DIR, "dist")
GAME_DIR = os.path.join(PROJECT_DIR, "game")


def run_cmd(cmd, cwd=PROJECT_DIR, shell=False):
    print(f"\n[EXEC] {cmd}")
    res = subprocess.run(cmd, shell=shell, cwd=cwd, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"[ERROR] Exit code {res.returncode}")
        print(f"Stdout:\n{res.stdout}")
        print(f"Stderr:\n{res.stderr}")
        raise RuntimeError(f"Command failed: {cmd}")
    return res.stdout


def check_icons():
    print("\n=== [0] Checking Android icon files ===")
    fg = os.path.join(PROJECT_DIR, "android-icon_foreground.png")
    bg = os.path.join(PROJECT_DIR, "android-icon_background.png")
    missing = []
    if not os.path.exists(fg):
        missing.append("android-icon_foreground.png")
    if not os.path.exists(bg):
        missing.append("android-icon_background.png")
    if missing:
        print(f"[WARNING] Missing icon files: {', '.join(missing)}")
        print("  rapt requires 432x432 PNG files:")
        print("    android-icon_foreground.png  (your logo on transparent background)")
        print("    android-icon_background.png  (solid color or pattern)")
        print("  APK will use default Ren'Py icon as fallback.")
    else:
        print("-> Icon files found.")


def compile_bytecode():
    print("\n=== [1] Compiling scripts to bytecode ===")
    run_cmd([LAUNCHER_SH, PROJECT_DIR, "compile"])
    print("-> Compilation complete.")


def build_android_apk(label, exclude_dpatch=False):
    print(f"\n=== Building Android APK: {label} ===")

    dpatch_backup_dir = os.path.join(PROJECT_DIR, "_temp_dpatch_backup")
    dpatch_files = []

    if exclude_dpatch:
        os.makedirs(dpatch_backup_dir, exist_ok=True)
        for f in os.listdir(GAME_DIR):
            if f.endswith("_d.rpy") or f.endswith("_d.rpyc") or "dpatch" in f:
                dpatch_files.append(f)
                shutil.move(os.path.join(GAME_DIR, f), os.path.join(dpatch_backup_dir, f))
        print(f"-> Temporarily removed {len(dpatch_files)} dpatch files.")

    try:
        os.makedirs(DIST_DIR, exist_ok=True)
        run_cmd([
            LAUNCHER_SH,
            os.path.join(SDK_DIR, "launcher"),
            "android_build", PROJECT_DIR,
            "--destination", DIST_DIR
        ])
    finally:
        if exclude_dpatch and dpatch_files:
            for f in dpatch_files:
                src = os.path.join(dpatch_backup_dir, f)
                if os.path.exists(src):
                    shutil.move(src, os.path.join(GAME_DIR, f))
            shutil.rmtree(dpatch_backup_dir, ignore_errors=True)
            print(f"-> Restored {len(dpatch_files)} dpatch files.")

    return find_built_apk(label)


def find_built_apk(label):
    pattern = "com.wantingwings.game"
    for f in os.listdir(DIST_DIR):
        if f.startswith(pattern) and f.endswith(".apk"):
            src = os.path.join(DIST_DIR, f)
            dst = os.path.join(DIST_DIR, f"WantingWings-2.0-{label}.apk")
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
            print(f"-> Built: {dst}")
            return dst
    raise FileNotFoundError(f"No APK found in {DIST_DIR} for '{label}'")


def upload_to_github(apk_paths):
    print("\n=== [3] Uploading APKs to GitHub Release v2.0 ===")
    run_cmd(["gh", "auth", "status"])
    for apk in apk_paths:
        print(f"-> Uploading {os.path.basename(apk)}")
        run_cmd(["gh", "release", "upload", "v2.0", apk, "--clobber"])
    print("-> Upload complete.")


def main():
    print("=" * 60)
    print("   WANTING WINGS V2.0 — ANDROID BUILD PIPELINE")
    print("=" * 60)

    try:
        check_icons()
        compile_bytecode()

        print("\n=== [2] Building Android APKs ===")
        patched = build_android_apk("android-patched", exclude_dpatch=False)
        standard = build_android_apk("android-release", exclude_dpatch=True)

        upload_to_github([patched, standard])

        print("\n" + "=" * 60)
        print("   BUILD COMPLETE")
        print("=" * 60)

    except Exception as e:
        print(f"\n[FATAL] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
