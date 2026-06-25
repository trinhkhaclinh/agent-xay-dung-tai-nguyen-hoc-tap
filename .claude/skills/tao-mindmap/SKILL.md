---
name: tao-mindmap
description: Tạo Mindmap (mindmap.json -> .xmind) tổng hợp toàn session theo cây Lesson → khái niệm. Dùng khi cần sơ đồ tư duy/mindmap ôn tập cho session, hoặc khi orchestrator yêu cầu sinh mindmap.
---

# Tạo Mindmap → mindmap.json

Đầu vào: `session_content_spec.json`. Đầu ra: `_spec/mindmap.json` (1 file/session).

> md-first: `render_vault.py` chuyển cây này thành **danh sách lồng nhau** trong note Mindmap của vault
> (stage-1, Obsidian hiển thị dạng outline/graph). Việc xuất `.xmind` là stage-2 (đợt sau).

## Đọc trước
- `_spec/session_content_spec.json`.
- `knowledge/format-specs/06-mindmap-va-cau-truc-thu-muc.md` (định dạng + schema).

## Cách làm
Cây nội dung:
- `root` = tên session (không kèm "Session NN").
- `children` cấp 1 = các Lesson, đánh số ("1. <Tên Lesson>", "2. ...").
- Cấp 2–3 = `key_concepts` + `facts` của từng Lesson, nhóm hợp lý, diễn đạt ngắn gọn (cụm từ, không câu dài).

Mindmap phải phản ánh đúng nội dung SSOT (nhất quán với bài đọc/slide/video). Ưu tiên các điểm "phải nhớ".

## Đặt tên file
`filename`: `"Session NN - <Tên>"`. `subdir`: `"Mindmap"`. Renderer sẽ đóng gói .xmind.

## Tự kiểm
File .xmind mở được; root khớp tên session; mỗi Lesson có 1 nhánh cấp 1 với các nhánh con khái niệm.
