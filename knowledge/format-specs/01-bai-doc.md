# Hợp đồng định dạng — Bài đọc (Bài đọc/*.docx)

Mục tiêu: tài liệu đọc chuyên sâu cho từng chủ đề/Lesson, kết hợp **khái niệm → ví dụ mẫu (worked
example) → vận dụng**. Mỗi session thường có **1 bài đọc / chủ đề lớn** (Session 02 có 5 bài đọc).

Renderer: `tools/render_reading.py`  ·  Input JSON: `reading.json` (dùng Block Model).

## Cấu trúc bắt buộc (theo mẫu Session 02)
1. **`h1`** — Tiêu đề, mở đầu "Bài Đọc Chuyên Sâu: ..." (Title Case tiếng Việt).
2. Các **`h2`** đánh số: `1.`, `2.`, `3.`, ... cho từng mục lớn.
3. **`h3`** cho các bước con (vd "Phân phối các bước thực hiện:").
4. Nội dung: `p` (giải thích), `bullets`, `code` (theo từng bước, có chú thích `#`).
5. Mục áp chót **`h2` "Tổng Kết"** — tóm tắt kỹ thuật đã nắm (3-5 `bullets` hoặc `p`).
6. Mục cuối **`h2` "Tài Liệu Tham Khảo"** — danh sách nguồn chính thống.

## Nguyên tắc nội dung
- **Kịch bản nghiệp vụ thực tế**, KHÔNG ví dụ đồ chơi. Mẫu Session 02 dùng "API giám sát cổng điều phối
  Logistics" thay vì `hello world` trần. Lấy `scenario` từ SSOT.
- Code đặt tên file thực tế (vd `gateway.py`), có docstring tiếng Việt, comment đánh số bước.
- Giọng học thuật, ngôi "chúng ta"; giải thích "vì sao" không chỉ "làm gì".
- Độ dài tham chiếu: 45–85 đoạn (xem mẫu).

## Schema `reading.json`
```jsonc
{
  "filename": "BÀI ĐỌC_ TỔNG QUAN KIẾN TRÚC WEB ...",   // KHÔNG đuôi; renderer thêm .docx
  "subdir": "Bài đọc",
  "blocks": [
    { "type": "h1", "text": "Bài Đọc Chuyên Sâu: ..." },
    { "type": "h2", "text": "1. Kiến Trúc Bộ Đôi Công Cụ: FastAPI & Uvicorn" },
    { "type": "p",  "text": "..." },
    { "type": "h3", "text": "Phân phối các bước thực hiện:" },
    { "type": "code", "lang": "bash", "text": "python -m venv venv" },
    { "type": "bullets", "items": ["...", "..."] },
    { "type": "h2", "text": "Tổng Kết" },
    { "type": "bullets", "items": ["..."] },
    { "type": "h2", "text": "Tài Liệu Tham Khảo" },
    { "type": "bullets", "items": ["FastAPI Official Documentation - ...", "..."] }
  ]
}
```

## Checklist QA (qa_check.py)
- [ ] Có đúng 1 `h1`; tiêu đề chứa "Bài Đọc".
- [ ] ≥ 3 mục `h2` đánh số.
- [ ] Có mục "Tổng Kết" và "Tài Liệu Tham Khảo".
- [ ] Có ≥ 1 khối `code`.
- [ ] Không còn placeholder `[...]` / `TODO`.
