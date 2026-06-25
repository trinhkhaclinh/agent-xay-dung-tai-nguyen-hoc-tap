# -*- coding: utf-8 -*-
"""Script to copy Session 04 deliverables from vault to a separate directory.
"""
import os
import shutil

ROOT = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap"
SRC = os.path.join(ROOT, "vault", "Sessions", "Session 04 - Parameters, Request body & Pydantic Validation")
DST = os.path.join(ROOT, "Session_04_Results")

import stat

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def copy_results():
    import sys
    # Force UTF-8 encoding for stdout
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if os.path.exists(DST):
        shutil.rmtree(DST, onerror=remove_readonly)
    os.makedirs(DST, exist_ok=True)
    
    for item in os.listdir(SRC):
        src_item = os.path.join(SRC, item)
        dst_item = os.path.join(DST, item)
        if os.path.isdir(src_item):
            shutil.copytree(src_item, dst_item)
            print(f"Copied directory: {item}")
        else:
            shutil.copy2(src_item, dst_item)
            print(f"Copied file: {item}")
            
    print("Session 04 results copied successfully to Session_04_Results!")

if __name__ == "__main__":
    copy_results()
