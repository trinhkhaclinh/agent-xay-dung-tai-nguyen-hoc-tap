# -*- coding: utf-8 -*-
"""Cổng validate SSOT (session_content_spec.json) — gate "shift-left" sau Bước 1.

Vì sao cần: SSOT là hợp đồng cho cả 6 nhóm artifact. Một lỗi ở SSOT lan ra 6 đầu ra và
tốn 6× công sửa ở vòng lặp QA cuối. Kiểm SSOT NGAY trước khi fan-out là rẻ nhất.

Kiểm gì:
  - Cấu trúc: đủ khóa cấp session + cấp lesson (BLOCKER nếu thiếu/empty).
  - Sư phạm: mỗi objective có nhãn bậc Bloom; cả session trải ≥3 bậc; đủ key_concepts/facts.
  - prior_session.review_topics (phục vụ quiz Đầu giờ phần BÀI CŨ).
  - Cú pháp code_examples (tái dùng verify_code).

Chạy:
  PYTHONIOENCODING=utf-8 python tools/qa_spec.py "output/<folder>/_spec/session_content_spec.json"
  (truyền thư mục _spec cũng được — tự tìm session_content_spec.json)
Thoát != 0 nếu có BLOCKER.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from verify_code import iter_snippets, PY_LANGS  # noqa: E402

BLOOM = ["Nhớ", "Hiểu", "Vận dụng", "Phân tích", "Đánh giá", "Sáng tạo"]
TOP_REQUIRED = ["session_no", "session_id", "title", "module", "hinh_thuc_hoc", "summary", "lessons"]
LESSON_REQUIRED = ["no", "title", "objectives", "key_concepts", "scenario", "facts",
                   "code_examples", "san_pham_dau_ra"]


def bloom_level(objective):
    for b in BLOOM:
        if "(%s)" % b in objective:
            return b
    return None


def validate(ssot):
    errors, warns = [], []
    for k in TOP_REQUIRED:
        if ssot.get(k) in (None, "", []):
            errors.append("Thiếu/empty khóa SSOT cấp session: '%s'" % k)

    lessons = ssot.get("lessons") or []
    if not lessons:
        errors.append("SSOT không có lesson nào.")

    levels = set()
    for i, l in enumerate(lessons, 1):
        tag = "Lesson %s" % l.get("no", i)
        for k in LESSON_REQUIRED:
            if l.get(k) in (None, "", []):
                errors.append("%s: thiếu/empty '%s'" % (tag, k))
        objs = l.get("objectives") or []
        if len(objs) < 2:
            warns.append("%s: nên có ≥2 objective (hiện %d)" % (tag, len(objs)))
        for o in objs:
            lv = bloom_level(o)
            if lv:
                levels.add(lv)
            else:
                warns.append("%s: objective thiếu nhãn bậc Bloom '(Hiểu/Vận dụng/...)': \"%s…\"" % (tag, o[:55]))
        if len(l.get("key_concepts") or []) < 3:
            warns.append("%s: nên có ≥3 key_concepts" % tag)
        if len(l.get("facts") or []) < 3:
            warns.append("%s: nên có ≥3 facts (tái dùng cho quiz/mindmap)" % tag)
        if not (l.get("code_examples") or []):
            warns.append("%s: chưa có code_examples — artifact dẫn xuất sẽ thiếu code chuẩn để trích lại" % tag)

    if len(levels) < 3:
        warns.append("Cả session chỉ trải %d bậc Bloom (%s) — nên ≥3 (Hiểu→Vận dụng→Phân tích/Sáng tạo)."
                     % (len(levels), ", ".join(sorted(levels)) or "—"))

    ps = ssot.get("prior_session") or {}
    rt = ps.get("review_topics") or []
    if not rt:
        warns.append("prior_session.review_topics trống — quiz Đầu giờ (BÀI CŨ) sẽ thiếu nội dung ôn.")
    elif len(rt) < 3:
        warns.append("prior_session.review_topics < 3 mục (%d)." % len(rt))

    for lang, code, where in iter_snippets(ssot):
        if lang in PY_LANGS:
            try:
                compile(code, "<SSOT:%s>" % where, "exec")
            except SyntaxError as e:
                errors.append("SSOT %s: lỗi cú pháp Python — %s (dòng %s)" % (where, e.msg, e.lineno))

    return errors, warns, levels, len(lessons)


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python tools/qa_spec.py <session_content_spec.json | thư mục _spec>")
        sys.exit(2)
    fp = sys.argv[1]
    if os.path.isdir(fp):
        fp = os.path.join(fp, "session_content_spec.json")
    try:
        ssot = json.load(open(fp, encoding="utf-8-sig"))
    except Exception as e:
        print("[X] Không đọc được SSOT (%s): %s" % (fp, e))
        sys.exit(1)

    errors, warns, levels, n = validate(ssot)
    print("=== QA SPEC (SSOT): %s ===" % os.path.basename(fp))
    print("Lessons: %d | bậc Bloom phủ: %s" % (n, ", ".join(sorted(levels)) or "—"))
    if warns:
        print("\nNÊN SỬA (%d):" % len(warns))
        for w in warns[:50]:
            print("  [!]", w)
    if errors:
        print("\nBLOCKER (%d):" % len(errors))
        for e in errors[:50]:
            print("  [X]", e)
        print("\n=> FAIL (%d BLOCKER)" % len(errors))
        sys.exit(1)
    print("\n=> PASS (0 BLOCKER%s)" % ("" if not warns else "; %d cảnh báo" % len(warns)))
    sys.exit(0)


if __name__ == "__main__":
    main()
