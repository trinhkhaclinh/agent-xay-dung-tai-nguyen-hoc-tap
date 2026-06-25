---
name: tao-quiz
description: Tạo 2 bộ Quiz Quizizz (quiz_daugio.json + quiz_cuoigio.json) cho session — Đầu giờ ôn bài cũ + xem trước bài mới, Cuối giờ củng cố. Đúng lược đồ 12 cột để import Quizizz. Dùng khi cần ngân hàng câu hỏi trắc nghiệm/quiz cho session, hoặc khi orchestrator yêu cầu sinh quiz.
---

# Tạo Quiz → quiz_daugio.json + quiz_cuoigio.json

Đầu vào: `session_content_spec.json`. Đầu ra: `_spec/quiz_daugio.json`, `_spec/quiz_cuoigio.json`.

> md-first: `render_vault.py` chuyển JSON này thành **bảng Markdown 12 cột** trong note Quiz của vault
> (stage-1). Việc xuất `.xlsx` Quizizz là stage-2 (đợt sau). Schema JSON giữ nguyên như dưới.

## Đọc trước
- `_spec/session_content_spec.json` (đặc biệt `facts`, `key_concepts`, `prior_session.review_topics`).
- `knowledge/format-specs/04-quiz.md` (lược đồ cột + phân bổ + schema + checklist).
- `knowledge/pedagogy/principles.md` mục 3 & 5 (retrieval/spacing/interleaving, distractor design).

## Quiz Đầu giờ (`quiz_daugio.json`)
- Trộn ~60% `BÀI CŨ` (từ `prior_session.review_topics`, `difficulty` 4) + ~40% `BÀI MỚI`
  (xem trước `key_concepts`/`facts` session này, `difficulty` 8). Tổng ≥ 20 câu.
- `sheet_name` đặt theo chủ đề bài cũ (vd `Quiz_DauGio_OOP`).
- `filename`: `"Import_Quiz_DauGio_<chủ đề>"`, `subdir`: `"Câu hỏi Quiziz session"`.

## Quiz Cuối giờ (`quiz_cuoigio.json`)
- 100% nội dung session vừa học, phủ đều các Lesson; gồm câu Hiểu + câu Vận dụng. Tổng ≥ 15 câu.
- `category` theo Lesson/chủ đề; `difficulty` 4–8 tùy bậc Bloom.
- `sheet_name` vd `Quiz_CuoiGio_FastAPI`; `filename`: `"Import_Quiz_CuoiGio_<chủ đề>"`.

## Mỗi câu hỏi
4 đáp án + **4 giải thích** (vì sao đúng/sai), `correct` ∈ {1,2,3,4}, `difficulty` số, `category` chuỗi.
- Distractor là **hiểu lầm phổ biến** (vd nhầm cú pháp ngôn ngữ khác, sai chuẩn REST), không phi lý lộ liễu.
- Câu hỏi & đáp án chính xác kỹ thuật; bám `facts` của SSOT để nhất quán với các artifact khác.

## Tự kiểm
Theo checklist `04-quiz.md`: mỗi câu đủ 4 đáp án + 4 giải thích; `isCorrect`∈{1..4}; Đầu giờ có cả BÀI CŨ & BÀI MỚI.
(Renderer `render_quiz.py` cũng validate và sẽ báo lỗi nếu thiếu.)
