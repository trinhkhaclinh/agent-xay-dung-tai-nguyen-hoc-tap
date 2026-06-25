# -*- coding: utf-8 -*-
"""Render Kịch bản quay video: video_script.json -> Kịch bản quay video/<filename>.docx"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.docx_helpers import new_doc, add_blocks
from lib.io_utils import load_json, out_path


def render(spec, session_dir):
    doc = new_doc()
    add_blocks(doc, spec.get("blocks", []))
    path = out_path(session_dir, spec.get("subdir", "Kịch bản quay video"), spec["filename"], ".docx")
    doc.save(path)
    return path


def main():
    if len(sys.argv) < 3:
        print("Cách dùng: python tools/render_video_script.py <spec.json> <session_dir>")
        sys.exit(1)
    spec = load_json(sys.argv[1])
    print("=>", render(spec, sys.argv[2]))


if __name__ == "__main__":
    main()
