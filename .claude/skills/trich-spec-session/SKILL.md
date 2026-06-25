---
name: trich-spec-session
description: Dựng session_content_spec.json (nguồn sự thật duy nhất) cho một Session từ khung chương trình, theo backwards design. Dùng khi cần lập đặc tả nội dung/mục tiêu học tập cho session trước khi sinh học liệu, hoặc khi orchestrator yêu cầu bước 1.
---

# Dựng SSOT — session_content_spec.json

Đầu vào: số session. Đầu ra: `output/<thư mục session>/_spec/session_content_spec.json`.

## Đọc trước
- `knowledge/framework.json` (lấy session theo `session_no`).
- `knowledge/format-specs/00-tong-quan-va-block-model.md` (schema SSOT).
- `knowledge/pedagogy/principles.md` (Backwards Design) + `bloom-verbs-vi.md`.
- `knowledge/style-guide.md` (mục 3: domain nghiệp vụ thực tế).

## Các bước (Backwards Design)
1. Lấy module, session_id, title, hinh_thuc_hoc, danh sách `lessons` (title, noi_dung_chi_tiet, san_pham_dau_ra).
2. Với MỖI Lesson, viết:
   - `objectives`: 2–4 mục tiêu, mỗi mục bắt đầu bằng **động từ Bloom** (xem bloom-verbs-vi.md), bám
     sát "noi_dung_chi_tiet" và "san_pham_dau_ra". Trải ≥3 bậc Bloom cho cả session.
   - `key_concepts`: 3–6 khái niệm cốt lõi (cụm danh từ).
   - `scenario`: 1 kịch bản nghiệp vụ thực tế dùng xuyên suốt Lesson (Quản lý sinh viên / Khóa học /
     Logistics / E-commerce — chọn nhất quán trong session).
   - `facts`: 3–6 định nghĩa/sự thật chính xác (tái dùng cho quiz & mindmap).
   - `code_examples`: 1–3 ví dụ code **chạy được**, đặt tên file thực tế, comment tiếng Việt.
   - `san_pham_dau_ra`: copy từ framework.
3. `prior_session`: tìm session trước (session_no-1); liệt kê 3–6 `review_topics` (kiến thức cần ôn
   để vào bài mới) cho quiz Đầu giờ.
4. Viết `summary` 2–3 câu cho cả session.

## Chất lượng
- Nội dung kỹ thuật phải ĐÚNG (FastAPI/Python). Khi nghi ngờ, đối chiếu tài liệu chính thống.
- Mọi `code_examples` phải tự chạy được và minh họa đúng `key_concepts`. Đây là **code chuẩn tắc**:
  các artifact sau (bài đọc/video/slide) sẽ TRÍCH LẠI nguyên văn, nên đặt tên file thực tế (`main.py`,
  `gateway.py`) và viết hoàn chỉnh để chạy được, không để mảnh vụn.
- Đây là hợp đồng cho mọi artifact sau — viết kỹ, đầy đủ, chính xác.

Ghi file bằng JSON UTF-8 (ensure_ascii=false), đúng schema trong `00-...md`.

## Cổng kiểm (BẮT BUỘC trước khi bàn giao SSOT cho fan-out)
```
PYTHONIOENCODING=utf-8 python tools/qa_spec.py "output/<folder>/_spec/session_content_spec.json"
PYTHONIOENCODING=utf-8 python tools/verify_code.py "output/<folder>/_spec/session_content_spec.json" --run
```
Sửa tới khi cả hai exit 0 (hết BLOCKER). Cảnh báo NÊN SỬA (thiếu nhãn Bloom, <3 bậc Bloom, thiếu facts…)
nên xử lý luôn vì sẽ ảnh hưởng toàn bộ artifact dẫn xuất.
