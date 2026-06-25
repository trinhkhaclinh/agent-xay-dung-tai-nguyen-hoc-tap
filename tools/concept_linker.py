# -*- coding: utf-8 -*-
"""Tạo/cập nhật atomic concept notes trong vault/Khái niệm/ (idempotent).

Mỗi khái niệm 1 note; mục "## Xuất hiện ở" tích lũy các session dùng nó ⇒ graph Obsidian thể hiện
mạng tri thức + thứ tự tiên quyết xuyên chương trình.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.md_helpers import safe_name, dump_frontmatter, name_session_moc, wikilink

CONCEPT_DIR = "Khái niệm"


def concept_path(vault_root, concept):
    return os.path.join(vault_root, CONCEPT_DIR, safe_name(concept) + ".md")


def _new_concept_md(concept, session_no, definition):
    meta = {
        "type": "khai-niem",
        "title": concept,
        "aliases": [],
        "tags": ["concept"],
        "introduced_in": "[[%s]]" % name_session_moc(session_no),
        "related": [],
        "status": "draft",
    }
    body = [dump_frontmatter(meta), ""]
    body.append("# %s" % concept)
    body.append("")
    if definition:
        body.append("> %s" % definition)
    else:
        body.append("> Khái niệm trong [[%s]]." % name_session_moc(session_no))
    body.append("")
    body.append("## Liên quan")
    body.append("")
    body.append("## Xuất hiện ở")
    return "\n".join(body) + "\n"


def ensure_concept(vault_root, concept, session_no, role="giới thiệu", definition=None):
    """Tạo note nếu thiếu; thêm 1 dòng backref session vào mục 'Xuất hiện ở' nếu chưa có."""
    path = concept_path(vault_root, concept)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    backref = "- [[%s]] — %s" % (name_session_moc(session_no), role)

    if not os.path.exists(path):
        content = _new_concept_md(concept, session_no, definition)
        content = content.rstrip() + "\n" + backref + "\n"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return "created"

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    moc_link = "[[%s]]" % name_session_moc(session_no)
    if moc_link in content:
        return "exists"  # đã có backref session này
    if "## Xuất hiện ở" not in content:
        content = content.rstrip() + "\n\n## Xuất hiện ở\n"
    content = content.rstrip() + "\n" + backref + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "updated"


def link_concepts(vault_root, concepts, session_no, role="giới thiệu", definitions=None):
    definitions = definitions or {}
    results = {}
    seen = set()
    for c in concepts:
        key = safe_name(c)
        if key in seen:
            continue
        seen.add(key)
        results[c] = ensure_concept(vault_root, c, session_no, role, definitions.get(c))
    return results


def main():
    if len(sys.argv) < 4:
        print('Cách dùng: python tools/concept_linker.py <vault_root> <session_no> "<KN1>" "<KN2>" ...')
        sys.exit(1)
    vault, no = sys.argv[1], int(sys.argv[2])
    res = link_concepts(vault, sys.argv[3:], no)
    for c, r in res.items():
        print("  [%s] %s" % (r, c))


if __name__ == "__main__":
    main()
