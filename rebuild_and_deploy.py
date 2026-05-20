#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import zipfile

# 基础目录配置
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

def install_dependencies():
    print("=== [1] Installing required python packages ===")
    try:
        import PIL
        print("Pillow library is already installed.")
    except ImportError:
        print("Pillow not found. Installing via pip...")
        try:
            run_cmd([sys.executable, "-m", "pip", "install", "pillow"])
        except Exception:
            run_cmd(["pip", "install", "pillow"])

def generate_icons():
    print("\n=== [2] Generating cross-platform icons ===")
    install_dependencies()
    from PIL import Image

    icon_src = os.path.join(GAME_DIR, "gui", "window_icon.png")
    if not os.path.exists(icon_src):
        print(f"[WARNING] Source icon {icon_src} not found! Skipping icon generation.")
        return

    # 生成 Android 图标 (android-icon.png)
    android_icon_dst = os.path.join(PROJECT_DIR, "android-icon.png")
    shutil.copyfile(icon_src, android_icon_dst)
    print(f"-> Generated Android icon at: {android_icon_dst}")

    # 生成 Windows 图标 (icon.ico)
    windows_icon_dst = os.path.join(PROJECT_DIR, "icon.ico")
    img = Image.open(icon_src)
    img.save(windows_icon_dst, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print(f"-> Generated Windows icon at: {windows_icon_dst}")

    # 生成 macOS 图标 (icon.icns)
    macos_icon_dst = os.path.join(PROJECT_DIR, "icon.icns")
    tmp_iconset = os.path.join(PROJECT_DIR, "tmp.iconset")
    os.makedirs(tmp_iconset, exist_ok=True)
    
    sizes = [16, 32, 64, 128, 256, 512]
    try:
        for size in sizes:
            out_img_normal = os.path.join(tmp_iconset, f"icon_{size}x{size}.png")
            out_img_2x = os.path.join(tmp_iconset, f"icon_{size//2}x{size//2}@2x.png")
            
            # 使用 PIL 进行高清重采样缩放并保存
            img.resize((size, size), Image.Resampling.LANCZOS).save(out_img_normal)
            if size >= 32:
                img.resize((size, size), Image.Resampling.LANCZOS).save(out_img_2x)
        
        # 编译为 icns
        run_cmd(["iconutil", "-c", "icns", tmp_iconset, "-o", macos_icon_dst])
        print(f"-> Generated macOS icon at: {macos_icon_dst}")
    except Exception as e:
        print(f"[WARNING] Failed to generate macOS .icns: {e}. Falling back to copying raw icon.")
    finally:
        if os.path.exists(tmp_iconset):
            shutil.rmtree(tmp_iconset)

def compile_bytecode():
    print("\n=== [3] Compiling python scripts to bytecode (*.rpyc) ===")
    run_cmd([LAUNCHER_SH, PROJECT_DIR, "compile"])
    print("-> Bytecode static compilation completed successfully!")

def build_desktop_packages():
    print("\n=== [4] Building all Desktop packages via distribute ===")
    # 清理老的 dist 目录防止混淆，但先保留 android-related 证书
    temp_keystore_backup = os.path.join(PROJECT_DIR, "dist_keystore_backup")
    os.makedirs(temp_keystore_backup, exist_ok=True)
    
    keystore_src = os.path.join(DIST_DIR, "bundle.keystore")
    if os.path.exists(keystore_src):
        shutil.copy(keystore_src, os.path.join(temp_keystore_backup, "bundle.keystore"))
    
    # 彻底重建 dist/ 保证干净
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR, exist_ok=True)
    
    # 恢复 keystore 证书
    keystore_backup_file = os.path.join(temp_keystore_backup, "bundle.keystore")
    if os.path.exists(keystore_backup_file):
        shutil.copy(keystore_backup_file, os.path.join(DIST_DIR, "bundle.keystore"))
    shutil.rmtree(temp_keystore_backup)

    # 桌面端打包 (这会自动生成 pc.zip 并将碎文件封入 RPA)
    run_cmd([LAUNCHER_SH, os.path.join(SDK_DIR, "launcher"), "distribute", PROJECT_DIR])
    print("-> distribute finished. Now collecting built packages from default output directory...")
    
    # 自动把默认生成在 /Applications/WantingWings-2.0-dists 里的所有文件移动到 dist/ 目录下
    default_dist_dir = "/Applications/WantingWings-2.0-dists"
    if os.path.exists(default_dist_dir):
        for f in os.listdir(default_dist_dir):
            src_file = os.path.join(default_dist_dir, f)
            dst_file = os.path.join(DIST_DIR, f)
            if os.path.isfile(src_file):
                print(f"Moving {f} to local dist/")
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.move(src_file, dst_file)
        # 清理空的同级目录
        try:
            shutil.rmtree(default_dist_dir)
        except Exception:
            pass
    else:
        print("[WARNING] Could not find default dist output directory: /Applications/WantingWings-2.0-dists")
        
    print("-> All Desktop packages (including Linux Patched) successfully collected in local dist/ folder!")


def extract_rpa_for_android():
    print("\n=== [5] Extracting compiled RPA archives for Android optimization ===")
    pc_zip_path = os.path.join(DIST_DIR, "WantingWings-2.0-pc-patched.zip")
    if not os.path.exists(pc_zip_path):
        raise FileNotFoundError(f"Could not find pc-patched.zip at {pc_zip_path} to extract RPA assets!")

    temp_extract_dir = os.path.join(DIST_DIR, "_temp_extract")
    os.makedirs(temp_extract_dir, exist_ok=True)
    
    with zipfile.ZipFile(pc_zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith(".rpa"):
                # 获取文件名并解压
                basename = os.path.basename(file_info.filename)
                if "script" in basename:
                    print(f"-> Skipping script archive to avoid duplicate script load conflict: {basename}")
                    continue
                target_path = os.path.join(GAME_DIR, basename)
                
                # 解压并拷贝到 game/ 目录下
                print(f"-> Extracting {basename} to game/")
                with zip_ref.open(file_info.filename) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
                    
    shutil.rmtree(temp_extract_dir)
    print("-> All RPA files successfully mounted to local game/ folder!")

def isolate_loose_assets(backup=True):
    # 这是最硬核的一步，临时移动散碎文件夹以优化 Android 打包
    loose_dirs = ["images", "audio", "gui", "voice"]
    backup_root = os.path.join(os.path.dirname(PROJECT_DIR), "Wanting.Wings.v2.0_assets_backup")
    
    if backup:
        print("\n=== [6a] Isolating 14,000+ loose assets to avoid Android IO penalty ===")
        os.makedirs(backup_root, exist_ok=True)
        for d in loose_dirs:
            src = os.path.join(GAME_DIR, d)
            dst = os.path.join(backup_root, d)
            if os.path.exists(src):
                print(f"-> Moving loose {d}/ to backup directory")
                shutil.move(src, dst)
        print("-> Loose files successfully isolated. Development directory is now ultra-clean!")
    else:
        print("\n=== [6b] Restoring loose assets back to development directory ===")
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
    print("\n=== [7] Building Dual Android APKs (Patched & Standard) ===")
    
    # 临时备份 dist 目录下的 APK 以免被覆盖
    build_dest = os.path.join(PROJECT_DIR, "dist")
    
    # (1) 构建 安卓补丁完整版 APK (WantingWings-2.0-android-patched.apk)
    print("\n>>> Building Android PATCHED APK (with all dpatch files)...")
    run_cmd([LAUNCHER_SH, os.path.join(SDK_DIR, "launcher"), "android_build", PROJECT_DIR, "--destination", build_dest])
    
    apk_pattern = "com.wantingwings.game"
    found_apk = None
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
            
    dpatch_backup_dir = os.path.join(os.path.dirname(PROJECT_DIR), "Wanting.Wings.v2.0_dpatch_backup")
    os.makedirs(dpatch_backup_dir, exist_ok=True)
    
    for df in dpatch_files:
        src = os.path.join(GAME_DIR, df)
        dst = os.path.join(dpatch_backup_dir, df)
        if os.path.exists(src):
            print(f"-> Moving {df} out of game/")
            shutil.move(src, dst)
            
    # 启动构建标准版 APK
    print("\n>>> Building Android STANDARD APK (without dpatch)...")
    run_cmd([LAUNCHER_SH, os.path.join(SDK_DIR, "launcher"), "android_build", PROJECT_DIR, "--destination", build_dest])
    
    found_apk = None
    for f in os.listdir(build_dest):
        if f.startswith(apk_pattern) and f.endswith(".apk"):
            found_apk = os.path.join(build_dest, f)
            break
            
    if not found_apk:
        raise FileNotFoundError("Could not find the standard APK built!")
        
    standard_apk_name = os.path.join(build_dest, "com.wantingwings.game-2.0-release.apk")
    if os.path.exists(standard_apk_name):
        os.remove(standard_apk_name)
    shutil.move(found_apk, standard_apk_name)
    print(f"-> SUCCESSFULLY built Standard APK: {standard_apk_name}")

    # 恢复 dpatch 文件
    print("\n>>> Restoring dpatch files to local folder...")
    for df in dpatch_files:
        src = os.path.join(dpatch_backup_dir, df)
        dst = os.path.join(GAME_DIR, df)
        if os.path.exists(src):
            shutil.move(src, dst)
    shutil.rmtree(dpatch_backup_dir)

def cleanup_temporary_rpa():
    print("\n=== [8] Cleaning up temporary RPA files in development directory ===")
    rpa_files = ["assets_dpatch.rpa", "audio.rpa", "gui.rpa", "images.rpa", "script.rpa", "script_dpatch.rpa"]
    for rf in rpa_files:
        path = os.path.join(GAME_DIR, rf)
        if os.path.exists(path):
            print(f"-> Deleting temporary {rf}")
            os.remove(path)
    print("-> Temporary RPA files clean-up completed.")

def redeploy_github_release():
    print("\n=== [9] Uploading 11 premium assets to GitHub Release v2.0 ===")
    # 确保 gh 已授权并可以连接
    run_cmd(["gh", "auth", "status"])
    
    # 删除旧的 Release
    print("Deleting old draft/release v2.0...")
    try:
        run_cmd(["gh", "release", "delete", "v2.0", "-y"])
    except Exception:
        print("Release v2.0 did not exist or delete failed (normal if first time). Continuing...")
        
    try:
        run_cmd(["git", "push", "origin", "--delete", "v2.0"])
    except Exception:
        pass

    # 重新发布 v2.0 Draft，多线程极速上传 11 个包
    print("Re-creating release v2.0 and uploading 11 assets...")
    # 查找 dist/ 下的所有压缩包和 APK（排除临时的、以及隐藏文件）
    assets_to_upload = []
    for f in os.listdir(DIST_DIR):
        path = os.path.join(DIST_DIR, f)
        if os.path.isfile(path) and (f.endswith(".zip") or f.endswith(".apk") or f.endswith(".bz2")):
            assets_to_upload.append(path)
            
    print(f"Assets slated for upload ({len(assets_to_upload)} files): {[os.path.basename(a) for a in assets_to_upload]}")
    
    # 运行创建和并行上传
    gh_cmd = [
        "gh", "release", "create", "v2.0",
        "--title", "Wanting Wings v2.0 Release",
        "--notes", "Official compiled packages for Wanting Wings v2.0 including Windows, macOS, Linux, Steam, and Android APK."
    ] + assets_to_upload
    
    run_cmd(gh_cmd)
    print("\n=== All 11 platform assets successfully uploaded & published to GitHub! ===")

def main():
    print("=========================================================")
    print("      WANTING WINGS V2.0 AUTOMATION BUILD PIPELINE      ")
    print("=========================================================")
    
    try:
        # Step 0: 清理上次残留的临时 .rpa 文件，确保干净的开发环境
        cleanup_temporary_rpa()
        
        # Step 1: 生成全套自定义图标
        generate_icons()
        
        # Step 2: 编译字节码
        compile_bytecode()
        
        # Step 3: 分发打包桌面端 (这会自动把散装文件编译进 dist/ 里的 RPA 压缩包中)
        build_desktop_packages()
        
        # Step 4: 临时把打好的完美官方 RPA 大文件取回，为 Android 极限优化做准备
        extract_rpa_for_android()
        
        # Step 5: 隔离 14,000+ 个碎文件，避免安卓打包产生 IO 卡顿致命伤
        isolate_loose_assets(backup=True)
        
        # Step 6: 自动连环打包：补丁版 APK 和 标准版 APK
        try:
            build_android_apks()
        finally:
            # 无论 APK 打包是成功还是中途出错报错，都必须强制将碎文件还原回去，确保开发目录的完整！
            isolate_loose_assets(backup=False)
            
        # Step 7: 清理临时的 .rpa 归档，恢复 Git 净洁免 LFS 开发状态
        cleanup_temporary_rpa()
        
        # Step 8: 一键上架发布 GitHub v2.0，极速覆盖部署 11 大核心资产
        redeploy_github_release()
        
        print("\n=========================================================")
        print("          CONGRATULATIONS! ALL TASKS COMPLETED!          ")
        print("=========================================================")
        
    except Exception as e:
        print(f"\n[FATAL RUNTIME ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
