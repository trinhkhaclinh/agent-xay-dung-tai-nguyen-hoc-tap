# -*- coding: utf-8 -*-
"""Render Mindmap: mindmap.json -> Mindmap/<filename>.xmind (định dạng XMind Zen).

File .xmind là zip gồm content.json + metadata.json + manifest.json.
ID sinh xác định (hash từ đường dẫn tiêu đề) để tái lập được, không random.
"""
import hashlib
import json
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.io_utils import load_json, out_path


def _tid(path):
    return hashlib.md5(("xmind::" + path).encode("utf-8")).hexdigest()[:16]


def _build_topic(node, path):
    title = node.get("title", "")
    here = path + "/" + title
    topic = {"id": _tid(here), "class": "topic", "title": title}
    kids = node.get("children", [])
    if kids:
        topic["children"] = {
            "attached": [_build_topic(k, here) for k in kids]
        }
    return topic


def build_content(spec):
    root_title = spec.get("root", spec.get("filename", "Mind Map"))
    root_node = {"title": root_title, "children": spec.get("children", [])}
    root_topic = _build_topic(root_node, "")
    return [{
        "id": _tid("sheet::" + root_title),
        "class": "sheet",
        "title": "Mind Map",
        "rootTopic": root_topic,
    }]


def render(spec, session_dir):
    content = build_content(spec)
    metadata = {"creator": {"name": "PTIT-Rikkei Resource Agent", "version": "1.0"}}
    manifest = {"file-entries": {"content.json": {}, "metadata.json": {}}}
    path = out_path(session_dir, spec.get("subdir", "Mindmap"), spec["filename"], ".xmind")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("content.json", json.dumps(content, ensure_ascii=False))
        z.writestr("metadata.json", json.dumps(metadata, ensure_ascii=False))
        z.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False))
    return path


def main():
    if len(sys.argv) < 3:
        print("Cách dùng: python tools/render_mindmap.py <spec.json> <session_dir>")
        sys.exit(1)
    spec = load_json(sys.argv[1])
    print("=>", render(spec, sys.argv[2]))


if __name__ == "__main__":
    main()
