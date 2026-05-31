#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SDK_DIR = "/Applications/renpy-8.5.3-sdk"
LAUNCHER = os.path.join(SDK_DIR, "renpy.sh")
DIST_DIR = os.path.join(PROJECT_DIR, "dist")

def run(cmd):
    print(f"\n[EXEC] {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def main():
    print("=" * 60)
    print("   WANTING WINGS V2.0 — CLEAN ANDROID BUILDER")
    print("=" * 60)
    
    os.makedirs(DIST_DIR, exist_ok=True)
    
    print("\n=== [1] Compiling scripts to bytecode ===")
    run([LAUNCHER, PROJECT_DIR, "compile"])
    
    print("\n=== [2] Building Android PATCHED APK ===")
    # Uses 'android-patched' file list which includes dpatch files
    run([LAUNCHER, os.path.join(SDK_DIR, "launcher"), "android_build", PROJECT_DIR, "--destination", DIST_DIR, "--package", "android-patched"])
    
    # Rename it
    for f in os.listdir(DIST_DIR):
        if f.startswith("com.yorkyang2333.wantingwings") and f.endswith(".apk"):
            src = os.path.join(DIST_DIR, f)
            dst = os.path.join(DIST_DIR, "WantingWings-2.0-android-patched.apk")
            if os.path.exists(dst): os.remove(dst)
            shutil.move(src, dst)
            print(f"-> Renamed to {dst}")
            break
            
    print("\n=== [3] Building Android STANDARD APK ===")
    # Uses 'android' default file list which automatically excludes dpatch files
    run([LAUNCHER, os.path.join(SDK_DIR, "launcher"), "android_build", PROJECT_DIR, "--destination", DIST_DIR, "--package", "android"])
    
    # Rename it
    for f in os.listdir(DIST_DIR):
        if f.startswith("com.yorkyang2333.wantingwings") and f.endswith(".apk"):
            src = os.path.join(DIST_DIR, f)
            dst = os.path.join(DIST_DIR, "WantingWings-2.0-android.apk")
            if os.path.exists(dst): os.remove(dst)
            shutil.move(src, dst)
            print(f"-> Renamed to {dst}")
            break
            
    print("\n" + "=" * 60)
    print("   ANDROID BUILD COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[FATAL ERROR] Build command failed with exit code {e.returncode}")
        sys.exit(1)
