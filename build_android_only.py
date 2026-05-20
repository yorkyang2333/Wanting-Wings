#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import zipfile

PROJECT_DIR = "/Applications/Wanting.Wings.v2.0"
SDK_DIR = "/Applications/renpy-8.5.2-sdk"
LAUNCHER_SH = os.path.join(SDK_DIR, "renpy.sh")
DIST_DIR = os.path.join(PROJECT_DIR, "dist")
GAME_DIR = os.path.join(PROJECT_DIR, "game")

def run_cmd(cmd, cwd=PROJECT_DIR, shell=False):
    print(f"\n[EXEC] Running: {cmd} in {cwd}")
    res = subprocess.run(cmd, shell=shell, cwd=cwd, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"[ERROR] Command failed with code {res.returncode}")
        print(f"Stdout:\n{res.stdout}")
        print(f"Stderr:\n{res.stderr}")
        raise RuntimeError(f"Command execution failed: {cmd}")
    return res.stdout

def compile_bytecode():
    print("\n=== [1] Compiling python scripts to bytecode (*.rpyc) ===")
    run_cmd([LAUNCHER_SH, PROJECT_DIR, "compile"])
    print("-> Bytecode static compilation completed successfully!")

def extract_rpa_for_android():
    print("\n=== [2] Extracting compiled RPA archives for Android optimization ===")
    pc_zip_path = os.path.join(DIST_DIR, "WantingWings-2.0-pc-patched.zip")
    if not os.path.exists(pc_zip_path):
        raise FileNotFoundError(f"Could not find pc-patched.zip at {pc_zip_path} to extract RPA assets!")

    with zipfile.ZipFile(pc_zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith(".rpa"):
                basename = os.path.basename(file_info.filename)
                if "script" in basename:
                    print(f"-> Skipping script archive to avoid duplicate script load conflict: {basename}")
                    continue
                target_path = os.path.join(GAME_DIR, basename)
                
                print(f"-> Extracting {basename} to game/")
                with zip_ref.open(file_info.filename) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
    print("-> All RPA files successfully mounted to local game/ folder!")

def isolate_loose_assets(backup=True):
    loose_dirs = ["images", "audio", "gui", "voice"]
    backup_root = os.path.join(PROJECT_DIR, "_temp_assets_backup")
    
    if backup:
        print("\n=== [3a] Isolating 14,000+ loose assets to avoid Android IO penalty ===")
        os.makedirs(backup_root, exist_ok=True)
        for d in loose_dirs:
            src = os.path.join(GAME_DIR, d)
            dst = os.path.join(backup_root, d)
            if os.path.exists(src):
                print(f"-> Moving loose {d}/ to backup directory")
                shutil.move(src, dst)
        print("-> Loose files successfully isolated!")
    else:
        print("\n=== [3b] Restoring loose assets back to development directory ===")
        for d in loose_dirs:
            src = os.path.join(backup_root, d)
            dst = os.path.join(GAME_DIR, d)
            if os.path.exists(src):
                print(f"-> Moving back {d}/ to game/")
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.move(src, dst)
        if os.path.exists(backup_root):
            shutil.rmtree(backup_root)
        print("-> Development directory fully restored!")

def build_android_apks():
    print("\n=== [4] Building Dual Android APKs (Patched & Standard) ===")
    
    # 临时备份 dist 目录下的 APK 以免被覆盖
    build_dest = os.path.join(PROJECT_DIR, "dist")
    
    # (1) 构建 安卓补丁完整版 APK (WantingWings-2.0-android-patched.apk)
    print("\n>>> Building Android PATCHED APK (with all dpatch files)...")
    run_cmd([LAUNCHER_SH, os.path.join(SDK_DIR, "launcher"), "android_build", PROJECT_DIR, "--destination", build_dest])
    
    apk_pattern = "com.wantingwings.game"
    found_apk = None
    for f in os.listdir(build_dest):
        if f.startswith(apk_pattern) and f.endswith(".apk") and not f.endswith("-patched.apk") and not f.endswith("-release.apk"):
            found_apk = os.path.join(build_dest, f)
            break
            
    if not found_apk:
        # Fallback to look for any fresh apk that isn't renamed yet
        for f in os.listdir(build_dest):
            if f.startswith(apk_pattern) and f.endswith(".apk"):
                found_apk = os.path.join(build_dest, f)
                break
                
    if not found_apk:
        raise FileNotFoundError("Could not find the built APK to rename!")
        
    patched_apk_name = os.path.join(build_dest, "WantingWings-2.0-android-patched.apk")
    if os.path.exists(patched_apk_name):
        os.remove(patched_apk_name)
    shutil.move(found_apk, patched_apk_name)
    print(f"-> SUCCESSFULLY built Patched APK: {patched_apk_name}")

    # (2) 构建 安卓标准版 APK (com.wantingwings.game-2.0-release.apk)
    print("\n>>> Preparing environment for Android STANDARD APK...")
    # 动态查找并临时移除所有 dpatch 和 _d.rpy/rpyc 文件以构建标准版
    dpatch_files = []
    for f in os.listdir(GAME_DIR):
        if f.endswith("_d.rpy") or f.endswith("_d.rpyc") or "dpatch" in f:
            dpatch_files.append(f)
            
    dpatch_backup_dir = os.path.join(PROJECT_DIR, "_temp_dpatch_backup")
    os.makedirs(dpatch_backup_dir, exist_ok=True)
    
    for df in dpatch_files:
        src = os.path.join(GAME_DIR, df)
        dst = os.path.join(dpatch_backup_dir, df)
        if os.path.exists(src):
            print(f"-> Moving {df} out of game/")
            shutil.move(src, dst)
            
    # 启动构建标准版 APK
    try:
        print("\n>>> Building Android STANDARD APK (without dpatch)...")
        run_cmd([LAUNCHER_SH, os.path.join(SDK_DIR, "launcher"), "android_build", PROJECT_DIR, "--destination", build_dest])
        
        found_apk = None
        for f in os.listdir(build_dest):
            if f.startswith(apk_pattern) and f.endswith(".apk") and not f.endswith("-patched.apk") and not f.endswith("-release.apk"):
                found_apk = os.path.join(build_dest, f)
                break
                
        if not found_apk:
            # Fallback
            for f in os.listdir(build_dest):
                if f.startswith(apk_pattern) and f.endswith(".apk") and f != "WantingWings-2.0-android-patched.apk":
                    found_apk = os.path.join(build_dest, f)
                    break
                    
        if not found_apk:
            raise FileNotFoundError("Could not find the standard APK built!")
            
        standard_apk_name = os.path.join(build_dest, "com.wantingwings.game-2.0-release.apk")
        if os.path.exists(standard_apk_name):
            os.remove(standard_apk_name)
        shutil.move(found_apk, standard_apk_name)
        print(f"-> SUCCESSFULLY built Standard APK: {standard_apk_name}")
    finally:
        # 恢复 dpatch 文件
        print("\n>>> Restoring dpatch files to local folder...")
        for df in dpatch_files:
            src = os.path.join(dpatch_backup_dir, df)
            dst = os.path.join(GAME_DIR, df)
            if os.path.exists(src):
                shutil.move(src, dst)
        shutil.rmtree(dpatch_backup_dir)

def cleanup_temporary_rpa():
    print("\n=== [5] Cleaning up temporary RPA files in development directory ===")
    rpa_files = ["assets_dpatch.rpa", "audio.rpa", "gui.rpa", "images.rpa", "script.rpa", "script_dpatch.rpa"]
    for rf in rpa_files:
        path = os.path.join(GAME_DIR, rf)
        if os.path.exists(path):
            print(f"-> Deleting temporary {rf}")
            os.remove(path)
    print("-> Temporary RPA files clean-up completed.")

def upload_to_github():
    print("\n=== [6] Uploading optimized APKs to GitHub Release v2.0 ===")
    run_cmd(["gh", "auth", "status"])
    
    patched_apk = os.path.join(DIST_DIR, "WantingWings-2.0-android-patched.apk")
    standard_apk = os.path.join(DIST_DIR, "com.wantingwings.game-2.0-release.apk")
    
    print(f"Uploading Patched APK: {patched_apk}")
    run_cmd(["gh", "release", "upload", "v2.0", patched_apk, "--clobber"])
    
    print(f"Uploading Standard APK: {standard_apk}")
    run_cmd(["gh", "release", "upload", "v2.0", standard_apk, "--clobber"])
    print("\n=== Android APKs successfully uploaded & published to GitHub! ===")

def main():
    print("=========================================================")
    print("      WANTING WINGS V2.0 ANDROID ONLY BUILD PIPELINE      ")
    print("=========================================================")
    
    try:
        # Step 0: 清理上次残留的临时 .rpa 文件，确保干净的开发环境
        cleanup_temporary_rpa()
        
        # Step 1: 编译字节码
        compile_bytecode()
        
        # Step 2: 提取 RPA
        extract_rpa_for_android()
        
        # Step 3: 隔离 14,000+ 个碎文件，避免安卓打包产生 IO 卡顿致命伤
        isolate_loose_assets(backup=True)
        
        # Step 4: 自动打包 Android 两个 APK
        try:
            build_android_apks()
        finally:
            # 还原碎文件
            isolate_loose_assets(backup=False)
            
        # Step 5: 清理临时的 .rpa 归档，恢复 Git 净洁免 LFS 开发状态
        cleanup_temporary_rpa()
        
        # Step 6: 覆盖上传至 GitHub Release
        upload_to_github()
        
        print("\n=========================================================")
        print("          CONGRATULATIONS! ALL TASKS COMPLETED!          ")
        print("=========================================================")
        
    except Exception as e:
        print(f"\n[FATAL RUNTIME ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
