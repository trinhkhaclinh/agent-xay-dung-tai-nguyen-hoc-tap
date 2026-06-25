# -*- coding: utf-8 -*-
"""Render Bài tập: exercise.json -> Bài tập/<filename>.docx

Nếu spec có khóa `submission`, tự thêm mục "5. Quy định nộp bài" theo chuẩn GitHub của Rikkei.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.docx_helpers import new_doc, add_blocks
from lib.io_utils import load_json, out_path


def _submission_blocks(sub):
    lop = sub.get("lop", "[Tên Lớp]")
    mon = sub.get("mon", "FastAPI")
    session = sub.get("session", "Session")
    ex = sub.get("ex", "Ex01")
    example = sub.get("example", "HNKS25CNTT1_%s_%s_%s" % (mon, session, ex))
    fmt = "%s_%s_%s_%s" % (lop, mon, session, ex)
    return [
        {"type": "h2", "text": "5. Quy định nộp bài"},
        {"type": "bullets", "items": [
            "Nộp code đã sửa + phần phân tích lỗi",
            "Đưa lên GitHub theo format:",
        ]},
        {"type": "code", "text": fmt},
        {"type": "code", "text": example},
    ]


def render(spec, session_dir):
    doc = new_doc()
    blocks = list(spec.get("blocks", []))
    if spec.get("submission"):
        # chỉ thêm nếu blocks chưa có mục nộp bài
        has = any(b.get("type", "").startswith("h") and "nộp bài" in b.get("text", "").lower()
                  for b in blocks)
        if not has:
            blocks += _submission_blocks(spec["submission"])
    add_blocks(doc, blocks)
    path = out_path(session_dir, spec.get("subdir", "Bài tập"), spec["filename"], ".docx")
    doc.save(path)
    return path


def main():
    if len(sys.argv) < 3:
        print("Cách dùng: python tools/render_exercise.py <spec.json> <session_dir>")
        sys.exit(1)
    spec = load_json(sys.argv[1])
    print("=>", render(spec, sys.argv[2]))


if __name__ == "__main__":
    main()
