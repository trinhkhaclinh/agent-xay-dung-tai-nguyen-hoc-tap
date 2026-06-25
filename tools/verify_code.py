# -*- coding: utf-8 -*-
"""Cổng kiểm CODE trong các _spec/*.json của một session (gate kỹ thuật #1).

Vì sao cần: qa_vault.py chỉ kiểm cấu trúc/wikilink, KHÔNG kiểm code chạy được.
Với môn FastAPI, code sai là lỗi tệ nhất — tool này biến "hy vọng code đúng" thành cổng chặn.

Kiểm gì:
  - snippet lang=python  -> compile() kiểm cú pháp (SyntaxError = BLOCKER).
  - snippet lang=json    -> json.loads (parse lỗi = NÊN SỬA, không chặn vì JSON minh hoạ hay rút gọn).
  - bash/text/sql/...     -> bỏ qua (đếm vào 'skipped').
  - Cờ --run: với snippet python là "ứng dụng FastAPI hoàn chỉnh" nằm trong file CANONICAL
    (không phải exercise_/quiz_, vốn cố tình chứa code lỗi để học viên sửa), chạy thử
    import + TestClient GET "/" trong tiến trình con có timeout:
      lỗi thực thi = BLOCKER · thiếu thư viện / có uvicorn.run top-level = SKIP.

Chạy:
  PYTHONIOENCODING=utf-8 python tools/verify_code.py "output/<folder>/_spec"
  PYTHONIOENCODING=utf-8 python tools/verify_code.py "output/<folder>/_spec" --run
Thoát != 0 nếu có BLOCKER.
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RUNNER = os.path.join(HERE, "lib", "run_snippet.py")

PY_LANGS = {"python", "py", "python3"}
JSON_LANGS = {"json"}

FULL_APP = re.compile(r"FastAPI\s*\(")
HAS_APP = re.compile(r"(?m)^\s*app\s*=")
TOPLEVEL_RUN = re.compile(r"(?m)^\s{0,3}uvicorn\.run\s*\(")
RUN_TIMEOUT_S = 20


def norm_lang(lang):
    return (lang or "").strip().lower()


def iter_snippets(obj, path="$"):
    """Đệ quy toàn bộ JSON, yield (lang, code, where) cho mọi khối code.

    Nhận diện 2 dạng:
      - block model:        {"type": "code", "lang": ..., "text": ...}
      - code_examples item: {"caption": ..., "lang": ..., "code": ...}
    """
    if isinstance(obj, dict):
        if obj.get("type") == "code" and isinstance(obj.get("text"), str):
            yield norm_lang(obj.get("lang")), obj["text"], path
        elif isinstance(obj.get("code"), str):
            cap = obj.get("caption") or obj.get("filename") or ""
            yield norm_lang(obj.get("lang")), obj["code"], path + ((" [%s]" % cap) if cap else "")
        for k, v in obj.items():
            yield from iter_snippets(v, "%s.%s" % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_snippets(v, "%s[%d]" % (path, i))


def _indent(text, prefix="      | "):
    return "\n".join(prefix + ln for ln in (text or "").splitlines())


def _run_snippet(code):
    """Chạy snippet trong tiến trình con. Trả (rc, output). rc: 0 OK · 2 BLOCKER · 3 SKIP."""
    fd, tmp = tempfile.mkstemp(suffix=".py")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(code)
        try:
            p = subprocess.run([sys.executable, RUNNER, tmp],
                               capture_output=True, text=True, timeout=RUN_TIMEOUT_S)
        except subprocess.TimeoutExpired:
            return 2, "Timeout (>%ds) — snippet có thể gọi server chặn luồng." % RUN_TIMEOUT_S
        return p.returncode, (p.stdout + p.stderr).strip()
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass


def verify_file(fp, run=False):
    stats = {"python": 0, "json": 0, "skipped": 0, "ran": 0, "run_skipped": 0}
    errors, warns = [], []
    rel = os.path.basename(fp)
    buggy = rel.startswith("exercise_") or rel.startswith("quiz_")
    try:
        data = json.load(open(fp, encoding="utf-8-sig"))
    except Exception as e:
        return ["%s: JSON hỏng — %s" % (rel, e)], [], stats

    for lang, code, where in iter_snippets(data):
        if lang in PY_LANGS:
            stats["python"] += 1
            try:
                compile(code, "<%s:%s>" % (rel, where), "exec")
            except SyntaxError as e:
                errors.append("%s %s: lỗi cú pháp Python — %s (dòng %s)" % (rel, where, e.msg, e.lineno))
                continue
            if run and not buggy and FULL_APP.search(code) and HAS_APP.search(code):
                if TOPLEVEL_RUN.search(code):
                    stats["run_skipped"] += 1
                    continue
                rc, out = _run_snippet(code)
                if rc == 2:
                    errors.append("%s %s: lỗi khi chạy thử ứng dụng FastAPI\n%s" % (rel, where, _indent(out)))
                elif rc == 3:
                    stats["run_skipped"] += 1
                else:
                    stats["ran"] += 1
        elif lang in JSON_LANGS:
            stats["json"] += 1
            try:
                json.loads(code)
            except Exception as e:
                warns.append("%s %s: JSON ví dụ không parse được — %s" % (rel, where, e))
        else:
            stats["skipped"] += 1
    return errors, warns, stats


def verify_paths(paths, run=False):
    targets = []
    for a in paths:
        if os.path.isdir(a):
            targets += sorted(glob.glob(os.path.join(a, "*.json")))
        elif a.endswith(".json"):
            targets.append(a)
    all_err, all_warn = [], []
    tot = {"python": 0, "json": 0, "skipped": 0, "ran": 0, "run_skipped": 0}
    for fp in targets:
        e, w, s = verify_file(fp, run=run)
        all_err += e
        all_warn += w
        for k in tot:
            tot[k] += s.get(k, 0)
    return targets, all_err, all_warn, tot


def main():
    run = "--run" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not paths:
        print("Cách dùng: python tools/verify_code.py <_spec dir|file.json> [--run]")
        sys.exit(2)
    targets, errors, warns, tot = verify_paths(paths, run=run)
    if not targets:
        print("Không tìm thấy _spec/*.json để kiểm.")
        sys.exit(2)

    print("=== VERIFY CODE: %d file%s ===" % (len(targets), " (--run)" if run else ""))
    print("Snippet Python: %d | chạy thật (smoke): %d | bỏ chạy: %d | JSON: %d | bỏ qua (bash/text): %d"
          % (tot["python"], tot["ran"], tot["run_skipped"], tot["json"], tot["skipped"]))
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
    print("\n=> PASS — không lỗi cú pháp/thực thi.")
    sys.exit(0)


if __name__ == "__main__":
    main()
