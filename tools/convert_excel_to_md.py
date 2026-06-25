# -*- coding: utf-8 -*-
"""Script to convert PM_RA_PTIT_2025_Software_Engineer_Python_Web.xlsx to a rich linked Markdown file in the vault.
"""
import os
import json
import sys

ROOT = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap"
JSON_PATH = os.path.join(ROOT, "knowledge", "framework.json")
MD_PATH = os.path.join(ROOT, "vault", "00 - Bản đồ chương trình", "PM_RA_PTIT_2025_Software_Engineer_Python_Web.md")

def convert():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(JSON_PATH):
        print(f"Parsed framework.json not found at {JSON_PATH}. Please run tools/extract_framework.py first.")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    out = []
    
    # Write frontmatter
    out.append("---")
    out.append('type: "course-curriculum"')
    out.append('title: "PM_RA_PTIT_2025_Software_Engineer_Python_Web"')
    out.append('module: "%s"' % data.get("module", "IT-215 FastAPI"))
    out.append('tags:')
    out.append('  - "type/curriculum"')
    out.append('  - "module/IT-215"')
    out.append('status: "done"')
    out.append("---")
    out.append("")
    out.append(f"# {data.get('module', 'IT-215 FastAPI')}")
    out.append("")
    out.append(f"> Đặc tả chi tiết khung chương trình được trích xuất từ `{data.get('source_file', 'Excel')}`.")
    out.append("> Các session được gắn liên kết trực tiếp tới các Session MOC tương ứng trong hệ thống Obsidian Vault.")
    out.append("")

    # Loop through each session
    sessions_dir = os.path.join(ROOT, "vault", "Sessions")
    
    def session_moc_exists(no):
        if no is None:
            return False
        moc_filename = f"Session {no:02d} — MOC.md"
        if not os.path.isdir(sessions_dir):
            return False
        for d in os.listdir(sessions_dir):
            if os.path.exists(os.path.join(sessions_dir, d, moc_filename)):
                return True
        return False

    for s in data["sessions"]:
        no = s.get("session_no")
        title = s.get("title", "")
        sid = s.get("session_id", "")
        form = s.get("hinh_thuc_hoc", "Chưa xác định")
        
        # Heading with wikilink if exists, else plain text
        if no and session_moc_exists(no):
            moc_name = f"Session {no:02d} — MOC"
            out.append(f"## [[{moc_name}|{sid} — {title}]]")
        else:
            out.append(f"## {sid} — {title}")
            
        out.append(f"- **Hình thức học:** `{form}`")
        
        lessons = s.get("lessons", [])
        if not lessons:
            out.append("- *Không có danh sách bài học con.*")
            out.append("")
            continue
            
        # Draw table of lessons
        out.append("")
        out.append("| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |")
        out.append("| --- | --- | --- |")
        for l in lessons:
            lno = l.get("no")
            ltitle = l.get("title", "")
            detail = l.get("noi_dung_chi_tiet", "").replace("\n", "<br>")
            output = l.get("san_pham_dau_ra", "").replace("\n", "<br>")
            
            l_label = f"Lesson {lno:02d}: {ltitle}" if lno else ltitle
            out.append(f"| {l_label} | {detail} | {output} |")
            
        out.append("")

    # Write to target Markdown file
    os.makedirs(os.path.dirname(MD_PATH), exist_ok=True)
    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
        
    print(f"Successfully converted and saved to: {MD_PATH}")

if __name__ == "__main__":
    convert()
