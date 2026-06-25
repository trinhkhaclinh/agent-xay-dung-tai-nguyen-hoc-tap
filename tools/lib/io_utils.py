# -*- coding: utf-8 -*-
"""Tiện ích I/O dùng chung cho các renderer."""
import json
import os


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def out_path(session_dir, subdir, filename, ext):
    """Tạo đường dẫn đầu ra <session_dir>/<subdir>/<filename><ext> và đảm bảo thư mục tồn tại."""
    d = os.path.join(session_dir, subdir)
    os.makedirs(d, exist_ok=True)
    if not ext.startswith("."):
        ext = "." + ext
    return os.path.join(d, filename + ext)
