# -*- coding: utf-8 -*-
"""Sinh Module MOC (bản đồ chương trình) từ knowledge/framework.json.

Liệt kê toàn bộ session, link [[Session NN — MOC]] (stub nếu chưa sinh), nhóm theo hình thức học.
Chạy:  PYTHONIOENCODING=utf-8 python tools/build_moc.py [vault_root]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.md_helpers import dump_frontmatter, name_session_moc, MODULE_MOC_NAME

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build_module_moc(vault_root, framework_path=None):
    framework_path = framework_path or os.path.join(ROOT, "knowledge", "framework.json")
    data = json.load(open(framework_path, encoding="utf-8"))
    sessions_dir = os.path.join(vault_root, "Sessions")

    def session_exists(no):
        if no is None:
            return False
        moc = name_session_moc(no) + ".md"
        # tìm trong mọi thư mục session
        if not os.path.isdir(sessions_dir):
            return False
        for d in os.listdir(sessions_dir):
            if os.path.exists(os.path.join(sessions_dir, d, moc)):
                return True
        return False

    meta = {"type": "module-moc", "title": MODULE_MOC_NAME,
            "module": data.get("module", ""), "tags": ["type/moc", "module/IT-215"], "status": "done"}
    out = [dump_frontmatter(meta), "", "# %s" % data.get("module", "IT-215 FastAPI"), ""]
    out.append("> Bản đồ chương trình — %d session. Link tới MOC từng session (✅ đã sinh / ⬜ chưa)."
               % data.get("session_count", len(data["sessions"])))
    out.append("")
    out.append("| # | Hình thức | Session | Trạng thái |")
    out.append("| --- | --- | --- | --- |")
    for sdata in data["sessions"]:
        no = sdata.get("session_no")
        title = sdata.get("title", "")
        form = sdata.get("hinh_thuc_hoc", "")
        if session_exists(no):
            link = "[[%s\\|%s]]" % (name_session_moc(no), title)  # escape | trong bảng
            mark = "✅"
        else:
            link = title
            mark = "⬜"
        sid = sdata.get("session_id", "")
        out.append("| %s | %s | %s — %s | %s |" % (no if no else "", form, sid, link, mark))
    out.append("")

    moc_dir = os.path.join(vault_root, "00 - Bản đồ chương trình")
    os.makedirs(moc_dir, exist_ok=True)
    path = os.path.join(moc_dir, MODULE_MOC_NAME + ".md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    return path


def main():
    vault = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "vault")
    p = build_module_moc(vault)
    print("=> Module MOC:", p)


if __name__ == "__main__":
    main()
