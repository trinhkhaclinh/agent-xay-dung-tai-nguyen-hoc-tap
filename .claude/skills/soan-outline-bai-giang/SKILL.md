---
name: soan-outline-bai-giang
description: Soạn Outline bài giảng (slide_outline.json) cho session — nội dung từng slide, gợi ý layout/sơ đồ và speaker notes, để dựng .pptx trên template Rikkei. Dùng khi cần outline slide/khung bài giảng, hoặc khi orchestrator yêu cầu sinh bài giảng. Lưu ý: chỉ sinh outline, KHÔNG render .pptx.
---

# Soạn Outline bài giảng → slide_outline.json

Đầu vào: `session_content_spec.json`. Đầu ra: `_spec/slide_outline.json` (1 file/session).

## Đọc trước
- `_spec/session_content_spec.json`.
- `knowledge/format-specs/05-bai-giang-outline.md` (cấu trúc deck + layout + schema + checklist).
- `knowledge/pedagogy/principles.md` mục 4 (mỗi slide một ý) & mục 6 (dual coding → diagram_hint).

## Cách làm
Dựng deck ~20–28 slide cho 4–6 Lesson:
1. Slide `title` (tên session, module, version 1.0).
2. Slide `agenda` (NỘI DUNG = liệt kê các Lesson).
3. Mỗi Lesson: 1 slide `section-title` ("N. <Tên Lesson> - 1") + các slide nội dung ("N. ... - 2/3/...").
4. Slide `summary` (TỔNG KẾT mỗi Lesson 1 dòng).
5. Slide `closing` ("KẾT THÚC" + "HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN").

Mỗi slide nội dung cần: `layout` (title/agenda/section-title/bullets/3-card/comparison-table/code/quadrant/table/summary/closing),
`content` (ý ngắn gọn — KHÔNG văn xuôi dài), `diagram_hint` khi cần hình, và **`speaker_notes`** liên kết với
kịch bản video Lesson tương ứng.

- Chọn `layout` đúng bản chất nội dung: so sánh → `comparison-table`; quy trình/đặc tính → `3-card`;
  ví dụ code → `code`; tiến hóa/định vị 2 trục → `quadrant`.
- Nội dung khớp với bài đọc & kịch bản video cùng Lesson. Slide `code` phải **trích từ `code_examples`
  của SSOT** (giữ nguyên tên file & nội dung), không tự chế ví dụ khác.

## Đặt tên file
`filename`: `"Session NN - <Tên>"`. `subdir`: `"Bài giảng"`.

## Tự kiểm
Theo checklist `05-bai-giang-outline.md`: có title/agenda/TỔNG KẾT/KẾT THÚC; mỗi Lesson có section + slide nội dung;
mỗi slide nội dung có speaker_notes.
