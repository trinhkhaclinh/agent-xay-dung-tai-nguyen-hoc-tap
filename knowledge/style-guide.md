# Style Guide — Giọng văn & quy ước biên soạn (PTIT × Rikkei)

Áp dụng cho mọi tài nguyên do agent sinh ra. Rút từ phân tích bộ mẫu Session 02.

## 1. Ngôn ngữ & chính tả
- **Tiếng Việt có dấu, chuẩn UTF-8**. Không viết tắt tùy tiện.
- Thuật ngữ kỹ thuật giữ **nguyên tiếng Anh** khi đã phổ biến: `endpoint`, `request`, `response`,
  `routing`, `middleware`, `query parameter`, `request body`, `JWT`, `CRUD`, `ORM`, `dependency injection`.
  Lần đầu xuất hiện nên kèm giải thích tiếng Việt ngắn trong ngoặc.
- Tên lệnh/code/đường dẫn để **nguyên dạng** (`uvicorn main:app --reload`, `/students`, `requirements.txt`).
- Viết hoa tên riêng công nghệ: FastAPI, Uvicorn, Pydantic, Starlette, Swagger UI, OpenAPI, Postman, MySQL.

## 2. Giọng văn theo loại tài liệu
| Tài liệu        | Ngôi xưng              | Giọng |
|-----------------|------------------------|-------|
| Bài đọc         | "chúng ta"             | Học thuật, mạch lạc, giải thích "vì sao" |
| Kịch bản video  | "thầy" – "các em"      | Văn nói, dẫn dắt, thân thiện, có mô tả màn hình |
| Bài tập         | "sinh viên" / mệnh lệnh| Rõ ràng, đề bài nghiệp vụ, yêu cầu cụ thể |
| Slide outline   | cụm từ ngắn            | Súc tích, từ khóa, không câu dài |
| Quiz            | trung tính             | Câu hỏi gọn; giải thích đáp án ngắn, chính xác |

- Kịch bản video luôn **mở** bằng: "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei
  Education..." và **chốt** bằng: "Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em...".
- Slide kết thúc deck: "HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN".

## 3. Nguyên tắc ví dụ & code (RẤT QUAN TRỌNG)
- **Dùng kịch bản nghiệp vụ thực tế, tránh ví dụ đồ chơi.** Mẫu Session 02 dùng: cổng giám sát Logistics
  (`gateway.py`), quản lý sinh viên (`/students`), quản lý khóa học (`/courses`). Tái dùng các domain này
  để xuyên suốt: Quản lý sinh viên, Khóa học/Đào tạo, Logistics/Kho vận, Thương mại điện tử.
- Code phải **chạy được**, đặt tên file thực tế, có docstring/được comment tiếng Việt theo bước.
- Endpoint tuân thủ RESTful: danh từ số nhiều (`/students`), không nhúng động từ (`❌ /getStudents`).
- Số liệu/định nghĩa phải **nhất quán** giữa các artifact (cùng port 8000, cùng ví dụ, cùng thuật ngữ).

## 4. Định dạng nộp bài (bài tập)
GitHub: `[Tên Lớp]_[Môn Học]_[Session]_Ex##` — ví dụ `HNKS25CNTT1_FastAPI_Session02_Ex01`.
Môn học mặc định cho module này: `FastAPI`.

## 5. Tính nhất quán cấp session
- Bài đọc, slide, kịch bản video, mindmap của cùng một Lesson phải nói **cùng một nội dung** (cùng khái niệm,
  cùng ví dụ, cùng kết luận) — chỉ khác hình thức trình bày. Đây là lý do mọi thứ dẫn xuất từ `session_content_spec`.
- Quiz Cuối giờ chỉ hỏi nội dung đã dạy trong session; Quiz Đầu giờ ôn lại session trước + xem trước session này.

## 6. Tránh
- ❌ Placeholder còn sót (`[điền sau]`, `TODO`, `Lorem ipsum`).
- ❌ Ví dụ `foo/bar`, `hello world` trần không gắn nghiệp vụ.
- ❌ Trộn tiếng Anh/Việt lủng củng trong cùng câu khi đã có thuật ngữ Việt phổ biến.
- ❌ Sai lệch nội dung giữa các artifact của cùng session.
