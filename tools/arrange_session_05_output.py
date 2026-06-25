# -*- coding: utf-8 -*-
"""Script to copy and rearrange Session 05 results into the output directory.
"""
import os
import shutil
import stat

ROOT = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap"
SRC = os.path.join(ROOT, "vault", "Sessions", "Session 05 - CRUD cơ bản")
DST = os.path.join(ROOT, "output", "Session 05 - CRUD cơ bản")

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def arrange_output():
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(SRC):
        print(f"Source directory {SRC} does not exist in vault!")
        return

    os.makedirs(DST, exist_ok=True)

    mapping = {
        "Bài giảng (outline)": "Bài giảng",
        "Bài tập": "Bài tập",
        "Bài đọc": "Bài đọc",
        "Quiz": "Câu hỏi Quiziz session",
        "Kịch bản video": "Kịch bản quay video",
        "Mindmap": "Mindmap"
    }

    # Clean existing directories in output
    for key, output_dir_name in mapping.items():
        dst_dir = os.path.join(DST, output_dir_name)
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir, onerror=remove_readonly)
            print(f"Cleared old output directory: {output_dir_name}")

    # Copy folders from vault
    for src_name, dst_name in mapping.items():
        src_path = os.path.join(SRC, src_name)
        dst_path = os.path.join(DST, dst_name)
        
        if os.path.exists(src_path):
            shutil.copytree(src_path, dst_path)
            print(f"Copied {src_name} -> {dst_name}")

    print("Session 05 rearrangement in output complete successfully!")

if __name__ == "__main__":
    arrange_output()
