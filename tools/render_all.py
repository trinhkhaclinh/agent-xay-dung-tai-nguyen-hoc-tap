# -*- coding: utf-8 -*-
"""Render toàn bộ artifact của một session từ thư mục _spec/.

Quy ước tên file JSON trong <session_dir>/_spec/:
  session_content_spec.json   -> SSOT (không render, chỉ tham chiếu)
  reading_*.json              -> Bài đọc
  video_*.json                -> Kịch bản quay video
  exercise_*.json             -> Bài tập
  quiz_*.json                 -> Quiz (đặt tên file đầu ra qua trường "filename")
  slide_outline.json          -> Outline bài giảng
  mindmap.json                -> Mindmap

Chạy:  PYTHONIOENCODING=utf-8 python tools/render_all.py "output/Session 02 - ..."
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.io_utils import load_json
import render_reading
import render_video_script
import render_exercise
import render_quiz
import render_mindmap
import render_slide_outline


def render_all(session_dir):
    spec_dir = os.path.join(session_dir, "_spec")
    if not os.path.isdir(spec_dir):
        raise SystemExit("Không thấy thư mục _spec/ trong %s" % session_dir)
    done = []

    def run(pattern, fn):
        for p in sorted(glob.glob(os.path.join(spec_dir, pattern))):
            spec = load_json(p)
            out = fn(spec, session_dir)
            done.append(out)
            print("  [OK]", os.path.relpath(out, session_dir))

    run("reading_*.json", render_reading.render)
    run("video_*.json", render_video_script.render)
    run("exercise_*.json", render_exercise.render)
    run("quiz_*.json", render_quiz.render)
    run("slide_outline*.json", render_slide_outline.render)
    run("mindmap*.json", render_mindmap.render)

    print("Đã render %d artifact vào %s" % (len(done), session_dir))
    return done


def main():
    if len(sys.argv) < 2:
        print('Cách dùng: python tools/render_all.py "<session_dir>"')
        sys.exit(1)
    render_all(sys.argv[1])


if __name__ == "__main__":
    main()
