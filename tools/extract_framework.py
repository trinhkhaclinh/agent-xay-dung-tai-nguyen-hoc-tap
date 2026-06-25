# -*- coding: utf-8 -*-
"""Parse khung chương trình (.xlsx) -> knowledge/framework.json.

Khung chương trình có các cột (sau hàng tiêu đề):
  A=STT, B=Hình thức học, C=Session, D=Nội dung (tên session),
  E=Lesson, F=Nội dung chi tiết, G=Sản phẩm đầu ra

Các cột cấp-session (B, C, D) bị merge dọc xuống nhiều hàng Lesson, nên ta
"carry-forward" giá trị gần nhất. Mỗi hàng có Lesson/Nội dung chi tiết riêng.

Chạy:  PYTHONIOENCODING=utf-8 python tools/extract_framework.py
"""
import json
import os
import re
import sys

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_XLSX = os.path.join(ROOT, "PM_RA_PTIT_2025_Software_Engineer_Python_Web.xlsx")
OUT_PATH = os.path.join(ROOT, "knowledge", "framework.json")

LESSON_RE = re.compile(r"^\s*Lesson\s*0*(\d+)\s*[:.\-]\s*(.+)$", re.IGNORECASE)
SESSION_RE = re.compile(r"Session\s*0*(\d+)", re.IGNORECASE)


def _clean(v):
    if v is None:
        return ""
    return str(v).strip()


def parse(xlsx_path):
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))

    module_title = ""
    header_idx = None
    for i, r in enumerate(rows):
        cells = [_clean(c) for c in r]
        line = " ".join(c for c in cells if c)
        if not module_title and "MODULE" in line.upper():
            module_title = line
        if "STT" in cells and any("Session" in c for c in cells) and any(
            "Lesson" in c for c in cells
        ):
            header_idx = i
            break
    if header_idx is None:
        raise RuntimeError("Không tìm thấy hàng tiêu đề (STT/Session/Lesson)")

    sessions = []
    cur = None
    last_form = ""  # Hình thức học carry-forward

    for r in rows[header_idx + 1:]:
        cells = list(r) + [None] * (7 - len(r))
        stt = _clean(cells[0])
        form = _clean(cells[1])
        session = _clean(cells[2])
        topic = _clean(cells[3])
        lesson = _clean(cells[4])
        detail = _clean(cells[5])
        output = _clean(cells[6])

        if not any([stt, form, session, topic, lesson, detail, output]):
            continue
        if form:
            last_form = form

        # Bắt đầu một session mới khi cột Session có giá trị
        if session:
            m = SESSION_RE.search(session)
            session_no = int(m.group(1)) if m else None
            cur = {
                "stt": stt,
                "hinh_thuc_hoc": last_form,
                "session_id": session,
                "session_no": session_no,
                "title": topic,
                "lessons": [],
            }
            sessions.append(cur)

        if cur is None:
            continue

        # Bổ sung tên session nếu hàng đầu thiếu (hiếm)
        if topic and not cur["title"]:
            cur["title"] = topic

        # Một dòng lesson/nội dung
        if lesson or detail or output:
            lm = LESSON_RE.match(lesson)
            if lm:
                lno = int(lm.group(1))
                ltitle = lm.group(2).strip()
            else:
                lno = None
                ltitle = lesson
            cur["lessons"].append(
                {
                    "no": lno,
                    "title": ltitle,
                    "noi_dung_chi_tiet": detail,
                    "san_pham_dau_ra": output,
                }
            )

    return {"module": module_title, "source_file": os.path.basename(xlsx_path),
            "session_count": len(sessions), "sessions": sessions}


def main():
    xlsx = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_XLSX
    data = parse(xlsx)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Module:", data["module"])
    print("Sessions:", data["session_count"])
    for s in data["sessions"]:
        print("  - %s [%s] %s (%d lessons)" % (
            s["session_id"], s["hinh_thuc_hoc"], s["title"], len(s["lessons"])))
    print("=> Wrote", OUT_PATH)


if __name__ == "__main__":
    main()
