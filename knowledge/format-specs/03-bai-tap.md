# Hợp đồng định dạng — Bài tập (Bài tập/*.docx)

Mục tiêu: bộ bài tập **phân tầng theo thang Bloom**, mỗi file một bài, đặt tên có tiền tố cấp độ.
Renderer: `tools/render_exercise.py`  ·  Input JSON: `exercise.json` (Block Model + `table`).

## Bộ cấp độ chuẩn (theo mẫu Session 02) — đặt tên file dạng `[Cấp độ] Tiêu đề.docx`
| Tiền tố file              | Bloom            | Dạng đề |
|---------------------------|------------------|---------|
| `[Vận dụng cơ bản 1]`     | Apply (sửa lỗi)  | Cho code legacy lỗi → trace + sửa |
| `[Vận dụng cơ bản 2]`     | Apply (sửa lỗi)  | Tình huống lỗi khác, cùng dạng |
| `[Vận dụng chuyên sâu]`   | Apply nâng cao   | Đề bài nghiệp vụ phức tạp hơn |
| `[Phân tích]`             | Analyze          | Đề xuất ≥2 thiết kế, bảng so sánh, chọn + triển khai |
| `[Sáng tạo]`              | Create           | Mở, sinh viên tự thiết kế giải pháp/tính năng |
| `[BTTH]`                  | Tổng hợp         | Bài tập thực hành tổng hợp cuối session |

Tối thiểu nên có: 2 × Vận dụng cơ bản, 1 × Phân tích, 1 × Vận dụng chuyên sâu, 1 × Sáng tạo, 1 × BTTH.

## Cấu trúc mục bắt buộc (mỗi bài)
1. `h1` tiêu đề bài.
2. `h2` **"1. Bối cảnh nghiệp vụ"** — tình huống thực tế.
3. `h2` **"2. Vấn đề hiện tại"** (bài sửa lỗi) hoặc **"2. Quy tắc nghiệp vụ"** / **"Yêu cầu bài toán"**.
4. (Bài sửa lỗi) `h2` **"3. Mã nguồn hiện tại (Legacy Code)"** + block `code`.
   (Bài phân tích) `h2` **"3. Ràng buộc & Bẫy dữ liệu"** — liệt kê edge cases.
5. `h2` **"4. Yêu cầu"** / **"Yêu cầu đầu ra"** — chia `h3` Phần 1/2/3 (Phân tích → So sánh → Triển khai).
   Dùng block `table` cho bảng tiêu chí so sánh khi cần.
6. `h2` **"5. Quy định nộp bài"** — chuẩn nộp GitHub:
   - "Nộp code đã sửa + phần phân tích lỗi"
   - "Đưa lên GitHub theo format:"
   - `[Tên Lớp]_[Môn Học]_[Session01]_Ex01`
   - ví dụ: `HNKS25CNTT1_FastAPI_Session01_Ex01`

## Schema `exercise.json`
```jsonc
{
  "filename": "[Vận dụng cơ bản 1] Sai sót trong API lấy danh sách sinh viên",
  "subdir": "Bài tập",
  "level": "Vận dụng cơ bản",
  "blocks": [
    { "type": "h1", "text": "Sai sót trong API lấy danh sách sinh viên" },
    { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
    { "type": "p", "text": "..." },
    { "type": "h2", "text": "3. Mã nguồn hiện tại (Legacy Code)" },
    { "type": "code", "lang": "python", "text": "..." },
    { "type": "h2", "text": "4. Yêu cầu" },
    { "type": "h3", "text": "(1) Phân tích lỗi" },
    { "type": "bullets", "items": ["..."] },
    { "type": "table", "headers": ["Tiêu chí","Giải pháp 1","Giải pháp 2"],
      "rows": [["Độ rõ ràng","",""],["Dễ mở rộng","",""]] }
  ],
  "submission": {
    "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session02", "ex": "Ex01",
    "example": "HNKS25CNTT1_FastAPI_Session02_Ex01"
  }
}
```
Nếu có `submission`, renderer tự thêm mục "5. Quy định nộp bài" chuẩn (không cần liệt kê trong blocks).

## Checklist QA
- [ ] Đủ bộ cấp độ tối thiểu (≥6 bài, đủ các tiền tố trên).
- [ ] Mỗi bài có "Bối cảnh nghiệp vụ" và "Quy định nộp bài".
- [ ] Bài sửa lỗi có block `code` legacy; bài phân tích có ≥2 phương án + bảng so sánh.
- [ ] Mục nộp bài có format GitHub đúng mẫu.
