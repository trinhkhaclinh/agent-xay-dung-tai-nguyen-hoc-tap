---
name: thiet-ke-bai-tap
description: Thiết kế bộ Bài tập (exercise_*.json) phân tầng theo thang Bloom cho session — sửa lỗi, phân tích, vận dụng chuyên sâu, sáng tạo, BTTH tổng hợp. Dùng khi cần ra đề/bài tập thực hành cho session, hoặc khi orchestrator yêu cầu sinh bài tập.
---

# Thiết kế Bài tập → exercise_<NN>.json (≥6 bài)

Đầu vào: `session_content_spec.json`. Đầu ra: nhiều `_spec/exercise_<NN>.json`.

## Đọc trước
- `_spec/session_content_spec.json`.
- `knowledge/format-specs/03-bai-tap.md` (bộ cấp độ + cấu trúc mục + schema + checklist).
- `knowledge/pedagogy/principles.md` mục 2 & 5 (Bloom, rubric) + `bloom-verbs-vi.md`.
- `knowledge/style-guide.md` mục 3 & 4 (domain thực tế, format nộp bài).

## Bộ cấp độ tối thiểu (mỗi bài 1 file)
- `[Vận dụng cơ bản 1]`, `[Vận dụng cơ bản 2]` — cho code legacy lỗi → trace + sửa.
- `[Vận dụng chuyên sâu]` — bài nghiệp vụ phức tạp hơn.
- `[Phân tích]` — đề xuất ≥2 thiết kế, **bảng so sánh** (block `table`), chọn + triển khai.
- `[Sáng tạo]` — mở, sinh viên tự thiết kế tính năng/giải pháp.
- `[BTTH]` — bài tập thực hành tổng hợp cuối session.

## Cấu trúc mỗi bài (blocks)
`h1` tiêu đề → `h2 "1. Bối cảnh nghiệp vụ"` → `h2 "2. Vấn đề hiện tại"`/`"Quy tắc nghiệp vụ"` →
(sửa lỗi) `h2 "3. Mã nguồn hiện tại (Legacy Code)"` + `code`; (phân tích) `h2 "3. Ràng buộc & Bẫy dữ liệu"` →
`h2 "4. Yêu cầu"` (chia `h3` Phần 1/2/3) → (renderer tự thêm) `"5. Quy định nộp bài"`.

Đặt `submission`: `{lop:"[Tên Lớp]", mon:"FastAPI", session:"SessionNN", ex:"ExKK", example:"HNKS25CNTT1_FastAPI_SessionNN_ExKK"}`
→ renderer tự sinh mục nộp bài chuẩn GitHub.

- Bài tập bám `key_concepts`/`scenario` của SSOT; bẫy dữ liệu phản ánh lỗi hay gặp thực tế.
- Code legacy phải có lỗi rõ ràng để sửa (vd trả string thay vì JSON, đặt tên endpoint sai chuẩn REST).

## Tự kiểm
Theo checklist `03-bai-tap.md`: đủ bộ cấp độ; mỗi bài có Bối cảnh + Quy định nộp bài; bài phân tích có ≥2 phương án + bảng.
