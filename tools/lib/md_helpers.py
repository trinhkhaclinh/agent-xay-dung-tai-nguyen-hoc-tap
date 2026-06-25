# -*- coding: utf-8 -*-
"""Tiện ích Markdown + Obsidian: frontmatter, Block Model -> Markdown, đặt tên note, wikilink.

Dùng chung cho render_vault.py, concept_linker.py, build_moc.py để tên note & link luôn khớp.
"""
import re

# Ký tự không hợp lệ trong tên file Windows: \ / : * ? " < > |
_ILLEGAL = {"/": "-", "\\": "-", ":": " -", "*": "", "?": "", '"': "'", "<": "(", ">": ")", "|": "-"}


def safe_name(s):
    """Chuẩn hóa chuỗi thành basename note hợp lệ, duy nhất, giữ tiếng Việt có dấu."""
    s = (s or "").strip()
    for k, v in _ILLEGAL.items():
        s = s.replace(k, v)
    s = re.sub(r"\s+", " ", s).strip()
    # tránh tên note bắt đầu bằng dấu chấm (file ẩn, vô hình với glob/Obsidian)
    s = s.lstrip(". ").strip()
    return s


def wikilink(target, display=None):
    """[[target]] hoặc [[safe|display]] nếu cần chuẩn hóa target."""
    safe = safe_name(target)
    disp = display if display is not None else target
    if safe == disp:
        return "[[%s]]" % safe
    return "[[%s|%s]]" % (safe, disp)


# ---------- Frontmatter ----------

def _yaml_scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    # luôn bọc nháy kép cho chuỗi (an toàn với : # [ ] {{ }} và [[..]])
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def dump_frontmatter(meta):
    """meta: dict gồm scalar | list[str]. Trả về khối ---\n...\n--- (YAML block style)."""
    lines = ["---"]
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, (list, tuple)):
            if not v:
                lines.append("%s: []" % k)
            else:
                lines.append("%s:" % k)
                for it in v:
                    lines.append("  - %s" % _yaml_scalar(it))
        else:
            lines.append("%s: %s" % (k, _yaml_scalar(v)))
    lines.append("---")
    return "\n".join(lines)


# ---------- Block Model -> Markdown ----------

def md_table(headers, rows):
    out = ["| " + " | ".join(str(h) for h in headers) + " |"]
    out.append("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        cells = [str(row[j]).replace("\n", "<br>").replace("|", "\\|") if j < len(row) else ""
                 for j in range(len(headers))]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def blocks_to_md(blocks):
    out = []
    for b in blocks:
        t = b.get("type", "p")
        if t == "h1":
            out.append("# " + b.get("text", ""))
        elif t == "h2":
            txt = b.get("text", "")
            # kịch bản video đã có sẵn tiền tố '## '
            out.append(txt if txt.startswith("#") else "## " + txt)
        elif t == "h3":
            out.append("### " + b.get("text", ""))
        elif t in ("p", "narration"):
            out.append(b.get("text", ""))
        elif t == "quote":
            out.append("> " + b.get("text", ""))
        elif t == "marker":
            txt = b.get("text", "").strip()
            if not (txt.startswith("[") and txt.endswith("]")):
                txt = "[" + txt.strip("[]") + "]"
            out.append("**%s**" % txt)
        elif t == "bullets":
            out.append("\n".join("- " + str(it) for it in b.get("items", [])))
        elif t == "numbers":
            out.append("\n".join("%d. %s" % (i, it) for i, it in enumerate(b.get("items", []), 1)))
        elif t == "code":
            lang = b.get("lang", "")
            out.append("```%s\n%s\n```" % (lang, b.get("text", "")))
        elif t == "table":
            out.append(md_table(b.get("headers", []), b.get("rows", [])))
        else:
            out.append(b.get("text", ""))
    return "\n\n".join(x for x in out if x is not None)


def mindmap_to_md(node, depth=0):
    """node: {title, children[]} -> danh sách lồng nhau (2 space/cấp)."""
    lines = []
    title = node.get("title", "")
    if depth == 0:
        lines.append("- **%s**" % title)
        child_depth = 1
    else:
        lines.append("  " * depth + "- " + title)
        child_depth = depth + 1
    for c in node.get("children", []):
        lines.append(mindmap_to_md(c, child_depth))
    return "\n".join(lines)


# ---------- Đặt tên note (DUY NHẤT toàn vault) ----------

def s(nn):
    return "S%02d" % int(nn)


def name_reading(nn, lesson, title):
    return safe_name("%s - L%s - %s" % (s(nn), lesson, title))


def name_video(nn, video_filename):
    return safe_name("%s - %s" % (s(nn), video_filename))


def name_exercise(nn, ex_filename):
    return safe_name("%s - %s" % (s(nn), ex_filename))


def name_quiz(nn, quiz_type):
    label = "Quiz Đầu giờ" if quiz_type == "daugio" else "Quiz Cuối giờ"
    return safe_name("%s - %s" % (s(nn), label))


def name_outline(nn):
    return safe_name("%s - Bài giảng (Outline)" % s(nn))


def name_mindmap(nn):
    return safe_name("%s - Mindmap" % s(nn))


def name_session_moc(nn):
    return safe_name("Session %02d — MOC" % int(nn))


MODULE_MOC_NAME = "IT-215 FastAPI — MOC"
