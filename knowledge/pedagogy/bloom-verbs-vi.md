# Bảng động từ Bloom (tiếng Việt) — tham chiếu khi viết mục tiêu & đề bài

Dùng khi viết `objectives` trong `session_content_spec` và khi đặt yêu cầu bài tập/quiz.
6 bậc (Anderson & Krathwohl, 2001), từ thấp đến cao:

| Bậc | Tên | Động từ gợi ý (VI) | Áp dụng vào |
|-----|-----|--------------------|-------------|
| 1 | **Nhớ** (Remember) | liệt kê, nêu, định nghĩa, gọi tên, nhận biết | Quiz `difficulty` 4 (BÀI CŨ) |
| 2 | **Hiểu** (Understand) | giải thích, mô tả, phân biệt, tóm tắt, cho ví dụ | Quiz, bài đọc |
| 3 | **Vận dụng** (Apply) | viết, triển khai, cấu hình, sửa lỗi, sử dụng, chạy | Bài tập "Vận dụng cơ bản/chuyên sâu", quiz `difficulty` 8 |
| 4 | **Phân tích** (Analyze) | so sánh, phân tích, trace luồng, chỉ ra lỗi, đối chiếu | Bài tập "Phân tích" (bảng so sánh thiết kế) |
| 5 | **Đánh giá** (Evaluate) | lựa chọn, đề xuất, biện luận, đánh giá ưu/nhược | Bài tập "Phân tích" phần "So sánh & Lựa chọn" |
| 6 | **Sáng tạo** (Create) | thiết kế, xây dựng, kết hợp, sáng tạo, mở rộng | Bài tập "Sáng tạo", "BTTH" tổng hợp |

## Quy tắc nhanh
- Mỗi `objective` = **1 động từ Bloom + nội dung + (điều kiện/chuẩn)**.
  VD: "Triển khai (Vận dụng) được endpoint GET `/students` trả về JSON đúng chuẩn RESTful."
- Một session Lý thuyết nên có objective trải ≥3 bậc (Hiểu → Vận dụng → Phân tích/Sáng tạo).
- Tầng bài tập map trực tiếp từ bậc Bloom cao nhất mà Lesson hướng tới.
