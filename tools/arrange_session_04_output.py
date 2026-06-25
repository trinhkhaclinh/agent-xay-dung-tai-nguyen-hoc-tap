# -*- coding: utf-8 -*-
"""Script to move and rearrange Session 04 results into the output directory.
"""
import os
import shutil
import stat

ROOT = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap"
SRC = os.path.join(ROOT, "Session_04_Results")
DST = os.path.join(ROOT, "output", "Session 04 - Parameters, Request body & Pydantic Validation")

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def arrange_output():
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(SRC):
        print(f"Source directory {SRC} does not exist!")
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

    # Move folders and files
    for src_name, dst_name in mapping.items():
        src_path = os.path.join(SRC, src_name)
        dst_path = os.path.join(DST, dst_name)
        
        if os.path.exists(src_path):
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path, onerror=remove_readonly)
            shutil.move(src_path, dst_path)
            print(f"Moved {src_name} -> {dst_name}")

    # Handle Session 04 — MOC.md if it exists (Session MOC is usually only in vault, but we can move it to the root of output or remove it)
    moc_src = os.path.join(SRC, "Session 04 — MOC.md")
    if os.path.exists(moc_src):
        # We can just remove it or put it in DST root
        # Let's delete it so the output folder matches Session 02 exactly (which has no MOC file)
        os.remove(moc_src)
        print("Removed Session 04 — MOC.md from output target (not needed in output folder)")

    # Clean up the original Session_04_Results folder
    if os.path.exists(SRC):
        shutil.rmtree(SRC, onerror=remove_readonly)
        print("Cleaned up Session_04_Results directory.")

    print("Rearrangement complete successfully!")

if __name__ == "__main__":
    arrange_output()
