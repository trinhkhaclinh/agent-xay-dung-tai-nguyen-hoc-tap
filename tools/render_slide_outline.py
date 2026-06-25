# -*- coding: utf-8 -*-
"""Render Outline bài giảng: slide_outline.json -> Bài giảng/<filename>.md (+ .docx)

KHÔNG render .pptx (theo quyết định dự án). Outline đủ chi tiết để map 1:1 lên template PowerPoint.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.docx_helpers import new_doc, add_blocks
from lib.io_utils import load_json, out_path


def _md(spec):
    lines = []
    lines.append("# %s — Outline bài giảng" % spec.get("title", ""))
    meta = " · ".join(filter(None, [
        spec.get("module", ""),
        ("Phiên bản %s" % spec["version"]) if spec.get("version") else "",
        "%d slide" % len(spec.get("slides", [])),
    ]))
    if meta:
        lines.append("> " + meta)
    lines.append("")
    for i, s in enumerate(spec.get("slides", []), 1):
        head = "## Slide %d — [%s] %s" % (i, s.get("layout", "bullets"), s.get("title", ""))
        lines.append(head)
        if s.get("section"):
            lines.append("*Phần: %s*" % s["section"])
        for c in s.get("content", []):
            lines.append("- %s" % c)
        if s.get("diagram_hint"):
            lines.append("**Sơ đồ:** %s" % s["diagram_hint"])
        if s.get("speaker_notes"):
            lines.append("**Speaker notes:** %s" % s["speaker_notes"])
        lines.append("")
    return "\n".join(lines)


def _docx_blocks(spec):
    blocks = [{"type": "h1", "text": "%s — Outline bài giảng" % spec.get("title", "")}]
    sub = " · ".join(filter(None, [spec.get("module", ""),
                                   ("Phiên bản %s" % spec["version"]) if spec.get("version") else ""]))
    if sub:
        blocks.append({"type": "quote", "text": sub})
    for i, s in enumerate(spec.get("slides", []), 1):
        blocks.append({"type": "h2", "text": "Slide %d — [%s] %s" % (
            i, s.get("layout", "bullets"), s.get("title", ""))})
        if s.get("section"):
            blocks.append({"type": "quote", "text": "Phần: %s" % s["section"]})
        if s.get("content"):
            blocks.append({"type": "bullets", "items": s["content"]})
        if s.get("diagram_hint"):
            blocks.append({"type": "p", "text": "Sơ đồ: %s" % s["diagram_hint"]})
        if s.get("speaker_notes"):
            blocks.append({"type": "p", "text": "Speaker notes: %s" % s["speaker_notes"]})
    return blocks


def render(spec, session_dir):
    md_path = out_path(session_dir, spec.get("subdir", "Bài giảng"), spec["filename"], ".md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(_md(spec))
    doc = new_doc()
    add_blocks(doc, _docx_blocks(spec))
    docx_path = out_path(session_dir, spec.get("subdir", "Bài giảng"), spec["filename"], ".docx")
    doc.save(docx_path)
    return md_path


def main():
    if len(sys.argv) < 3:
        print("Cách dùng: python tools/render_slide_outline.py <spec.json> <session_dir>")
        sys.exit(1)
    spec = load_json(sys.argv[1])
    print("=>", render(spec, sys.argv[2]))


if __name__ == "__main__":
    main()
