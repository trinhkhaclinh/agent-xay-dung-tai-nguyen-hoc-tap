# -*- coding: utf-8 -*-
"""QA cho Obsidian vault: frontmatter hợp lệ, wikilink không gãy, concept đủ, Session MOC đủ.

Chạy:  PYTHONIOENCODING=utf-8 python tools/qa_vault.py [vault_root]
Thoát != 0 nếu có BLOCKER.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED = {
    "bai-doc": ["session", "lesson", "deliverable_filename"],
    "kich-ban-video": ["session", "lesson", "deliverable_filename"],
    "bai-tap": ["session", "level", "deliverable_filename"],
    "quiz": ["session", "quiz_type", "deliverable_filename"],
    "bai-giang-outline": ["session", "deliverable_filename"],
    "mindmap": ["session", "deliverable_filename"],
    "session-moc": ["session"],
    "module-moc": ["module"],
    "khai-niem": [],
}
PLACEHOLDERS = ["lorem ipsum", "[điền", "placeholder", "tbd"]

errors, warns = [], []
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
FM = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_fm(text):
    m = FM.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z0-9_]+):(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm


def link_target(raw):
    raw = raw.replace("\\|", "|")
    return raw.split("|")[0].split("#")[0].strip()


def main():
    vault = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "vault")
    md_files = [p for p in glob.glob(os.path.join(vault, "**", "*.md"), recursive=True)
                if os.sep + "_templates" + os.sep not in p]
    basenames = set(os.path.splitext(os.path.basename(p))[0] for p in md_files)

    for p in md_files:
        rel = os.path.relpath(p, vault)
        text = open(p, encoding="utf-8").read()
        fm = parse_fm(text)
        if fm is None:
            errors.append("%s: thiếu frontmatter" % rel)
            continue
        typ = fm.get("type", "").strip('"')
        if not typ:
            errors.append("%s: frontmatter thiếu 'type'" % rel)
        elif typ in REQUIRED:
            for key in REQUIRED[typ]:
                if key not in fm:
                    warns.append("%s: thiếu khóa '%s' (type=%s)" % (rel, key, typ))
        # wikilink gãy
        for raw in WIKILINK.findall(text):
            tgt = link_target(raw)
            if tgt and tgt not in basenames:
                errors.append("%s: wikilink gãy [[%s]]" % (rel, tgt))
        low = text.lower()
        for ph in PLACEHOLDERS:
            if ph in low:
                warns.append("%s: placeholder nghi vấn '%s'" % (rel, ph))

    # Concept đủ cho mỗi SSOT + Session MOC tồn tại
    for spec in glob.glob(os.path.join(ROOT, "output", "*", "_spec", "session_content_spec.json")) \
            + glob.glob(os.path.join(vault, "Sessions", "*", "_spec", "session_content_spec.json")):
        ssot = json.load(open(spec, encoding="utf-8"))
        nn = ssot.get("session_no")
        moc = "Session %02d — MOC" % nn
        if moc not in basenames:
            errors.append("Thiếu Session MOC: %s" % moc)
        concepts = set()
        for l in ssot.get("lessons", []):
            concepts.update(l.get("key_concepts", []))
        from sys import path as _p
        _p.insert(0, os.path.join(ROOT, "tools"))
        from lib.md_helpers import safe_name
        for c in concepts:
            if safe_name(c) not in basenames:
                warns.append("Thiếu concept note cho '%s' (session %s)" % (c, nn))

    print("=== QA VAULT: %s ===" % vault)
    print("Note .md: %d | basenames duy nhất: %d" % (len(md_files), len(basenames)))
    if errors:
        print("\nBLOCKER (%d):" % len(errors))
        for e in errors[:50]:
            print("  [X]", e)
    if warns:
        print("\nNÊN SỬA (%d):" % len(warns))
        for w in warns[:50]:
            print("  [!]", w)
    if not errors and not warns:
        print("PASS toàn bộ — không phát hiện vấn đề.")
    elif not errors:
        print("\n=> PASS (0 BLOCKER; %d cảnh báo)" % len(warns))
    else:
        print("\n=> FAIL (%d BLOCKER)" % len(errors))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
