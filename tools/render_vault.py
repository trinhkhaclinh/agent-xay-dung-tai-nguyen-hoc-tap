# -*- coding: utf-8 -*-
"""Render JSON (_spec/*.json) -> note Markdown trong Obsidian vault, kèm Session MOC + concept notes.

Chạy:  PYTHONIOENCODING=utf-8 python tools/render_vault.py "<session_dir hoặc _spec>" "vault"
- <session_dir>: thư mục session đã có _spec/ (vd "output/Session 02 - ...") HOẶC chính thư mục _spec.
- vault: thư mục gốc vault (mặc định ./vault).
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.io_utils import load_json
from lib import md_helpers as M
from concept_linker import link_concepts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def _concepts_section(concepts):
    if not concepts:
        return ""
    lines = ["## Khái niệm liên quan", ""]
    for c in concepts:
        lines.append("- " + M.wikilink(c))
    return "\n".join(lines)


def _definitions_from_facts(ssot):
    """Map khái niệm -> 1 fact mô tả (best-effort), để concept note có nội dung thật."""
    facts = []
    for l in ssot.get("lessons", []):
        facts += l.get("facts", [])
    defs = {}
    for l in ssot.get("lessons", []):
        for c in l.get("key_concepts", []):
            if c in defs:
                continue
            tokens = [t for t in re.split(r"[^0-9A-Za-zÀ-ỹ]+", c) if len(t) >= 3]
            for f in facts:
                fl = f.lower()
                if any(t.lower() in fl for t in tokens):
                    defs[c] = f
                    break
    return defs


def _lesson_by_no(ssot, no):
    for l in ssot.get("lessons", []):
        if l.get("no") == no:
            return l
    return {}


def _spec_num(path):
    m = re.search(r"_(\d+)\.json$", os.path.basename(path))
    return int(m.group(1)) if m else 0


def render_session(input_dir, vault_root):
    spec_dir = input_dir if os.path.basename(input_dir.rstrip("/\\")) == "_spec" \
        else os.path.join(input_dir, "_spec")
    ssot = load_json(os.path.join(spec_dir, "session_content_spec.json"))
    nn = ssot["session_no"]
    folder = ssot.get("folder_name", "Session %02d" % nn)
    sdir = os.path.join(vault_root, "Sessions", folder)
    created = []  # (group, note_name, subdir)

    def note(subdir, basename, meta, body):
        meta = dict(meta)
        meta.setdefault("status", "done")
        text = M.dump_frontmatter(meta) + "\n\n" + body
        _write(os.path.join(sdir, subdir, basename + ".md"), text)
        return basename

    # ----- Bài đọc -----
    for p in sorted(glob.glob(os.path.join(spec_dir, "reading_*.json")), key=_spec_num):
        spec = load_json(p)
        lesson_no = _spec_num(p)
        lesson = _lesson_by_no(ssot, lesson_no)
        title = lesson.get("title") or spec.get("filename", "")
        concepts = lesson.get("key_concepts", [])
        basename = M.name_reading(nn, lesson_no, title)
        meta = {"type": "bai-doc", "title": title, "session": nn, "lesson": lesson_no,
                "tags": ["type/bai-doc", "session/%02d" % nn],
                "concepts": [M.wikilink(c) for c in concepts],
                "deliverable_filename": spec.get("filename", "")}
        body = M.blocks_to_md(spec.get("blocks", [])) + "\n\n" + _concepts_section(concepts) \
            + "\n\n— Thuộc [[%s]]" % M.name_session_moc(nn)
        created.append(("Bài đọc", note("Bài đọc", basename, meta, body), "Bài đọc"))

    # ----- Kịch bản video -----
    for p in sorted(glob.glob(os.path.join(spec_dir, "video_*.json")), key=_spec_num):
        spec = load_json(p)
        lesson_no = spec.get("lesson_no")
        lesson = _lesson_by_no(ssot, lesson_no)
        concepts = lesson.get("key_concepts", [])
        basename = M.name_video(nn, spec.get("filename", "video"))
        meta = {"type": "kich-ban-video", "title": spec.get("filename", ""), "session": nn,
                "lesson": lesson_no, "tags": ["type/kich-ban-video", "session/%02d" % nn],
                "concepts": [M.wikilink(c) for c in concepts],
                "deliverable_filename": spec.get("filename", "")}
        body = M.blocks_to_md(spec.get("blocks", [])) + "\n\n" + _concepts_section(concepts) \
            + "\n\n— Thuộc [[%s]]" % M.name_session_moc(nn)
        created.append(("Kịch bản video", note("Kịch bản video", basename, meta, body), "Kịch bản video"))

    # ----- Bài tập -----
    for p in sorted(glob.glob(os.path.join(spec_dir, "exercise_*.json")), key=_spec_num):
        spec = load_json(p)
        level = spec.get("level", "")
        bloom = next((b for b in ["Vận dụng", "Phân tích", "Đánh giá", "Sáng tạo"] if b in level), level)
        sub = spec.get("submission", {})
        basename = M.name_exercise(nn, spec.get("filename", "exercise"))
        body = M.blocks_to_md(spec.get("blocks", []))
        if sub:
            fmt = "%s_%s_%s_%s" % (sub.get("lop", "[Tên Lớp]"), sub.get("mon", "FastAPI"),
                                   sub.get("session", "Session"), sub.get("ex", "Ex01"))
            example = sub.get("example", "")
            body += ("\n\n## 5. Quy định nộp bài\n\n- Nộp code đã sửa + phần phân tích lỗi\n"
                     "- Đưa lên GitHub theo format:\n\n```\n%s\n```\n\n```\n%s\n```" % (fmt, example))
        body += "\n\n— Thuộc [[%s]]" % M.name_session_moc(nn)
        meta = {"type": "bai-tap", "title": spec.get("filename", ""), "session": nn,
                "level": level, "bloom": bloom, "ex_code": sub.get("ex", ""),
                "tags": ["type/bai-tap", "session/%02d" % nn],
                "deliverable_filename": spec.get("filename", "")}
        created.append(("Bài tập", note("Bài tập", basename, meta, body), "Bài tập"))

    # ----- Quiz -----
    for p in sorted(glob.glob(os.path.join(spec_dir, "quiz_*.json"))):
        spec = load_json(p)
        qtype = "daugio" if "daugio" in os.path.basename(p).lower() else "cuoigio"
        basename = M.name_quiz(nn, qtype)
        headers = ["question_content", "answer_1", "explanation_answer_1", "answer_2",
                   "explanation_answer_2", "answer_3", "explanation_answer_3", "answer_4",
                   "explanation_answer_4", "isCorrect", "difficulty", "category"]
        rows = []
        for q in spec.get("questions", []):
            a = q.get("answers", ["", "", "", ""])
            e = q.get("explanations", ["", "", "", ""])
            rows.append([q.get("q", ""), a[0], e[0], a[1], e[1], a[2], e[2], a[3], e[3],
                         q.get("correct", ""), q.get("difficulty", ""), q.get("category", "")])
        label = "Quiz Đầu giờ" if qtype == "daugio" else "Quiz Cuối giờ"
        body = ("# Session %02d — %s\n\n> %d câu · lược đồ 12 cột (stage-2 ánh xạ sang .xlsx Quizizz).\n\n%s"
                % (nn, label, len(rows), M.md_table(headers, rows)))
        body += "\n\n— Thuộc [[%s]]" % M.name_session_moc(nn)
        meta = {"type": "quiz", "title": "Session %02d — %s" % (nn, label), "session": nn,
                "quiz_type": qtype, "sheet_name": spec.get("sheet_name", ""),
                "tags": ["type/quiz", "session/%02d" % nn],
                "deliverable_filename": spec.get("filename", "")}
        created.append(("Quiz", note("Quiz", basename, meta, body), "Quiz"))

    # ----- Bài giảng (Outline) -----
    all_concepts = []
    for l in ssot.get("lessons", []):
        all_concepts += l.get("key_concepts", [])
    seen = set(); all_concepts = [c for c in all_concepts if not (c in seen or seen.add(c))]
    for p in sorted(glob.glob(os.path.join(spec_dir, "slide_outline*.json"))):
        spec = load_json(p)
        basename = M.name_outline(nn)
        lines = ["# %s — Outline bài giảng" % spec.get("title", ""), ""]
        for i, sld in enumerate(spec.get("slides", []), 1):
            lines.append("## Slide %d — [%s] %s" % (i, sld.get("layout", "bullets"), sld.get("title", "")))
            if sld.get("section"):
                lines.append("*Phần: %s*" % sld["section"])
            for c in sld.get("content", []):
                lines.append("- %s" % c)
            if sld.get("diagram_hint"):
                lines.append("**Sơ đồ:** %s" % sld["diagram_hint"])
            if sld.get("speaker_notes"):
                lines.append("**Speaker notes:** %s" % sld["speaker_notes"])
            lines.append("")
        body = "\n".join(lines) + "\n" + _concepts_section(all_concepts) \
            + "\n\n— Thuộc [[%s]]" % M.name_session_moc(nn)
        meta = {"type": "bai-giang-outline", "title": spec.get("title", ""), "session": nn,
                "slide_count": len(spec.get("slides", [])),
                "tags": ["type/bai-giang", "session/%02d" % nn],
                "deliverable_filename": spec.get("filename", "")}
        created.append(("Bài giảng (outline)", note("Bài giảng (outline)", basename, meta, body),
                        "Bài giảng (outline)"))

    # ----- Mindmap -----
    for p in sorted(glob.glob(os.path.join(spec_dir, "mindmap*.json"))):
        spec = load_json(p)
        basename = M.name_mindmap(nn)
        root_node = {"title": spec.get("root", ""), "children": spec.get("children", [])}
        body = "# %s — Mindmap\n\n%s" % (spec.get("root", ""), M.mindmap_to_md(root_node)) \
            + "\n\n— Thuộc [[%s]]" % M.name_session_moc(nn)
        meta = {"type": "mindmap", "title": spec.get("root", ""), "session": nn,
                "tags": ["type/mindmap", "session/%02d" % nn],
                "deliverable_filename": spec.get("filename", "")}
        created.append(("Mindmap", note("Mindmap", basename, meta, body), "Mindmap"))

    # ----- Concept notes (chất keo liên kết) -----
    defs = _definitions_from_facts(ssot)
    cres = link_concepts(vault_root, all_concepts, nn, role="giới thiệu", definitions=defs)

    # ----- Session MOC -----
    moc = _build_session_moc(ssot, nn, folder, created, all_concepts)
    _write(os.path.join(sdir, M.name_session_moc(nn) + ".md"), moc)

    return created, cres


def _build_session_moc(ssot, nn, folder, created, all_concepts):
    meta = {"type": "session-moc", "title": M.name_session_moc(nn), "session": nn,
            "hinh_thuc_hoc": ssot.get("hinh_thuc_hoc", ""), "lessons": len(ssot.get("lessons", [])),
            "tags": ["type/moc", "session/%02d" % nn], "status": "done"}
    out = [M.dump_frontmatter(meta), "", "# Session %02d — %s" % (nn, ssot.get("title", "")), ""]
    out.append("> Thuộc [[%s]]" % M.MODULE_MOC_NAME)
    if ssot.get("summary"):
        out += ["", ssot["summary"]]
    out += ["", "## Mục tiêu học tập"]
    for l in ssot.get("lessons", []):
        out.append("- **Lesson %s — %s**" % (l.get("no"), l.get("title", "")))
        for o in l.get("objectives", []):
            out.append("    - %s" % o)
    # nhóm artifact
    groups = {}
    for grp, name, _sub in created:
        groups.setdefault(grp, []).append(name)
    out += ["", "## Tài nguyên"]
    for grp in ["Bài đọc", "Kịch bản video", "Bài tập", "Quiz", "Bài giảng (outline)", "Mindmap"]:
        if grp in groups:
            out.append("### %s" % grp)
            for name in groups[grp]:
                out.append("- [[%s]]" % name)
    out += ["", "## Khái niệm cốt lõi"]
    out.append(" · ".join(M.wikilink(c) for c in all_concepts))
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print('Cách dùng: python tools/render_vault.py "<session_dir|_spec>" [vault_root]')
        sys.exit(1)
    input_dir = sys.argv[1]
    vault_root = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "vault")
    created, cres = render_session(input_dir, vault_root)
    for grp, name, _sub in created:
        print("  [%s] %s" % (grp, name))
    nc = sum(1 for r in cres.values() if r in ("created", "updated"))
    print("Đã tạo %d note artifact + Session MOC; concept notes: %d mới/cập nhật (tổng %d)."
          % (len(created), nc, len(cres)))


if __name__ == "__main__":
    main()
