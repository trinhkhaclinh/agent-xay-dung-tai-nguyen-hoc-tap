---
name: soan-bai-doc
description: Soạn Bài đọc chuyên sâu (reading_*.json) cho từng chủ đề/Lesson của session, theo mạch khái niệm → ví dụ mẫu → vận dụng. Dùng khi cần tạo tài liệu đọc/giáo trình cho session, hoặc khi orchestrator yêu cầu sinh bài đọc.
---

# Soạn Bài đọc → reading_<NN>.json

Đầu vào: `session_content_spec.json`. Đầu ra: `_spec/reading_<NN>.json` (1 file/chủ đề lớn; Session 02 có 5).

## Đọc trước
- `_spec/session_content_spec.json` (nguồn nội dung).
- `knowledge/format-specs/01-bai-doc.md` (cấu trúc + schema + checklist).
- `knowledge/pedagogy/principles.md` mục 4 (worked examples / explicit instruction).
- `knowledge/style-guide.md` (giọng học thuật "chúng ta", domain thực tế).

## Cách làm
Mỗi bài đọc bám 1 Lesson (hoặc gộp chủ đề liên quan). Dựng `blocks` theo đúng cấu trúc:
`h1` (tiêu đề "Bài Đọc Chuyên Sâu: ...") → các `h2` đánh số → `p`/`h3`/`code`/`bullets` →
`h2 "Tổng Kết"` → `h2 "Tài Liệu Tham Khảo"`.

- Triển khai mạch: **khái niệm (vì sao) → ví dụ mẫu chi tiết (code từng bước, có comment) → mở rộng/vận dụng**.
- **Trích lại nguyên văn** `scenario` và `code_examples` từ SSOT (giữ tên file `main.py`/`gateway.py`, giữ
  nội dung code); KHÔNG tự bịa ví dụ mới hay đổi tên file — để bài đọc↔slide↔video cùng Lesson khớp 100%.
- Code: đặt tên file thực tế (vd `gateway.py`), docstring tiếng Việt, đánh số bước bằng comment `#`.
- Độ dài tham chiếu 45–85 đoạn.

## Đặt tên file
`filename` viết HOA kiểu mẫu: `"BÀI ĐỌC_ <TÊN CHỦ ĐỀ VIẾT HOA>_"`, `subdir`: `"Bài đọc"`.

## Tự kiểm trước khi ghi
Theo checklist QA trong `01-bai-doc.md`: đúng 1 h1; ≥3 h2 đánh số; có Tổng Kết + Tài Liệu Tham Khảo;
≥1 code; không placeholder.
