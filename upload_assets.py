import os
import sys
import subprocess
import time

DIST_DIR = "/Applications/Wanting.Wings.v2.0/dist"
LOG_FILE = "/Applications/Wanting.Wings.v2.0/upload_log.txt"

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, "a") as f:
        f.write(formatted + "\n")

def run_cmd(cmd):
    log(f"Executing: {' '.join(cmd)}")
    res = subprocess.run(cmd, text=True, capture_output=True)
    if res.returncode != 0:
        log(f"[ERROR] Code {res.returncode}")
        log(f"Stdout: {res.stdout.strip()}")
        log(f"Stderr: {res.stderr.strip()}")
        return False
    log(f"[SUCCESS] {res.stdout.strip()}")
    return True

def main():
    log("=== GitHub Release Asset Upload Started ===")
    
    # 检查 dist 目录下有哪些合法的包
    assets = []
    for f in os.listdir(DIST_DIR):
        path = os.path.join(DIST_DIR, f)
        if os.path.isfile(path) and (f.endswith(".zip") or f.endswith(".apk") or f.endswith(".bz2")):
            assets.append(path)
            
    assets.sort(key=lambda x: os.path.getsize(x)) # 从小到大排序，先上传小的，后上传大的
    
    log(f"Found {len(assets)} files to upload:")
    for a in assets:
        size_mb = os.path.getsize(a) / (1024 * 1024)
        log(f" - {os.path.basename(a)} ({size_mb:.2f} MB)")
        
    for i, a in enumerate(assets):
        filename = os.path.basename(a)
        log(f"\n[{i+1}/{len(assets)}] Uploading {filename}...")
        
        # 尝试最多 3 次
        success = False
        for attempt in range(1, 4):
            log(f"Attempt {attempt} for {filename}...")
            # 使用 gh release upload --clobber 覆盖同名文件
            cmd = ["gh", "release", "upload", "v2.0", a, "--clobber"]
            if run_cmd(cmd):
                success = True
                log(f"Successfully uploaded {filename}!")
                break
            else:
                log(f"Failed attempt {attempt} for {filename}. Waiting 10s before retry...")
                time.sleep(10)
                
        if not success:
            log(f"[FATAL] Failed to upload {filename} after 3 attempts.")
            sys.exit(1)
            
    log("\n=== ALL 11 ASSETS SUCCESSFULLY UPLOADED TO GITHUB RELEASE v2.0! ===")

if __name__ == "__main__":
    main()
