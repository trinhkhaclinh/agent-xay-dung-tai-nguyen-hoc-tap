# -*- coding: utf-8 -*-
"""Script to convert Session 02 output files from .docx/.xlsx/.xmind to .md from vault.
"""
import os
import shutil
import stat

ROOT = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap"
SRC = os.path.join(ROOT, "vault", "Sessions", "Session 02 - Giới thiệu & Cài đặt FastAPI")
DST = os.path.join(ROOT, "output", "Session 02 - Giới thiệu & Cài đặt FastAPI")

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def convert_to_md():
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(SRC):
        print(f"Vault source directory {SRC} does not exist!")
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

    # Delete existing non-spec subdirectories in output to clear old binary/office files
    for key, output_dir_name in mapping.items():
        dst_dir = os.path.join(DST, output_dir_name)
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir, onerror=remove_readonly)
            print(f"Cleared old directory: {output_dir_name}")

    # Copy new markdown versions from vault
    for src_name, dst_name in mapping.items():
        src_path = os.path.join(SRC, src_name)
        dst_path = os.path.join(DST, dst_name)
        
        if os.path.exists(src_path):
            shutil.copytree(src_path, dst_path)
            print(f"Copied .md files: {src_name} -> {dst_name}")

    print("Session 02 outputs converted to .md format successfully!")

if __name__ == "__main__":
    convert_to_md()
