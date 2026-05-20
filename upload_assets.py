import os
import sys
import subprocess
import time
import json

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

def get_uploaded_assets():
    cmd = ["gh", "release", "view", "v2.0", "--json", "assets"]
    res = subprocess.run(cmd, text=True, capture_output=True)
    if res.returncode != 0:
        log("[WARNING] Failed to fetch uploaded assets list from GitHub.")
        return set()
    try:
        data = json.loads(res.stdout)
        uploaded = set()
        for asset in data.get("assets", []):
            if asset.get("state") == "uploaded":
                uploaded.add(asset.get("name"))
        return uploaded
    except Exception as e:
        log(f"[WARNING] Failed to parse JSON of uploaded assets: {e}")
        return set()

def main():
    log("=== GitHub Release Asset Upload Started (With Skip Checking) ===")
    
    # Check what packages are available in dist directory
    assets = []
    for f in os.listdir(DIST_DIR):
        path = os.path.join(DIST_DIR, f)
        if os.path.isfile(path) and (f.endswith(".zip") or f.endswith(".apk") or f.endswith(".bz2")):
            assets.append(path)
            
    assets.sort(key=lambda x: os.path.getsize(x)) # Sort by size (ascending)
    
    log(f"Found {len(assets)} local files in dist:")
    for a in assets:
        size_mb = os.path.getsize(a) / (1024 * 1024)
        log(f" - {os.path.basename(a)} ({size_mb:.2f} MB)")
        
    uploaded_assets = get_uploaded_assets()
    log(f"Already uploaded assets on GitHub: {list(uploaded_assets)}")
    
    for i, a in enumerate(assets):
        filename = os.path.basename(a)
        
        if filename in uploaded_assets:
            log(f"\n[{i+1}/{len(assets)}] Skipping {filename} (Already uploaded and verified on GitHub Release).")
            continue
            
        log(f"\n[{i+1}/{len(assets)}] Uploading {filename}...")
        
        # Try up to 3 times
        success = False
        for attempt in range(1, 4):
            log(f"Attempt {attempt} for {filename}...")
            cmd = ["gh", "release", "upload", "v2.0", a, "--clobber"]
            if run_cmd(cmd):
                success = True
                log(f"Successfully uploaded {filename}!")
                break
            else:
                log(f"Failed attempt {attempt} for {filename}. Waiting 15s before retry...")
                time.sleep(15)
                
        if not success:
            log(f"[FATAL] Failed to upload {filename} after 3 attempts.")
            sys.exit(1)
            
    log("\n=== ALL 11 ASSETS SUCCESSFULLY UPLOADED TO GITHUB RELEASE v2.0! ===")

if __name__ == "__main__":
    main()
