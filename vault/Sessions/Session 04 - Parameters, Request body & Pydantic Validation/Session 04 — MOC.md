---
type: "session-moc"
title: "Session 04 — MOC"
session: 4
hinh_thuc_hoc: "Lý thuyết"
lessons: 4
tags:
  - "type/moc"
  - "session/04"
status: "done"
---

# Session 04 — Parameters, Request body & Pydantic Validation

> Thuộc [[IT-215 FastAPI — MOC]]

Học cách nhận và kiểm chứng dữ liệu đầu vào của API: Path Parameters (lấy dữ liệu từ URL), Query Parameters (tham số tìm kiếm/lọc), Request Body với Pydantic (nhận JSON có cấu trúc), và Type Hints kết hợp Query/Path/Field để tự động validate dữ liệu và trả về lỗi 422 chuẩn.

## Mục tiêu học tập
- **Lesson 1 — Path Parameters**
    - Giải thích (Hiểu) Path Parameter và cách lấy dữ liệu định danh tài nguyên từ URL
    - Triển khai (Vận dụng) endpoint /students/{student_id} với type hint để FastAPI tự ép kiểu
    - Giải thích (Hiểu) cơ chế tự động validate và lỗi 422 khi sai kiểu path parameter
    - Phân tích (Phân tích) thứ tự khai báo route để tránh xung đột giữa route tĩnh và route động
- **Lesson 2 — Query Parameters**
    - Giải thích (Hiểu) Query Parameter và phân biệt với Path Parameter
    - Triển khai (Vận dụng) API tìm kiếm/lọc /courses?keyword=...&level=... với nhiều query
    - Phân biệt (Hiểu) tham số bắt buộc và tùy chọn qua giá trị mặc định
    - Vận dụng (Vận dụng) kết hợp Path + Query trong cùng một endpoint
- **Lesson 3 — Request Body với Pydantic**
    - Giải thích (Hiểu) Pydantic BaseModel và vai trò khai báo cấu trúc dữ liệu (schema)
    - Triển khai (Vận dụng) endpoint POST nhận Request Body JSON nhờ tham số kiểu model
    - Giải thích (Hiểu) cơ chế tự động validate JSON và lỗi 422 khi thiếu/sai trường
    - Vận dụng (Vận dụng) response_model và model lồng nhau cho dữ liệu phức tạp
- **Lesson 4 — Type Hints trong FastAPI**
    - Giải thích (Hiểu) vai trò của Type Hints làm nền tảng cho validate tự động trong FastAPI
    - Vận dụng (Vận dụng) Query() và Path() để đặt ràng buộc (min_length, ge, le, gt)
    - Vận dụng (Vận dụng) Field() trong Pydantic model để ràng buộc và mô tả dữ liệu
    - Giải thích (Hiểu) cấu trúc thông báo lỗi 422 (loc / msg / type) để gỡ lỗi

## Tài nguyên
### Bài đọc
- [[S04 - L1 - Path Parameters]]
- [[S04 - L2 - Query Parameters]]
- [[S04 - L3 - Request Body với Pydantic]]
- [[S04 - L4 - Type Hints trong FastAPI]]
### Kịch bản video
- [[S04 - Lesson 01 - Path Parameters - Lấy dữ liệu từ URL]]
- [[S04 - Lesson 02 - Query Parameters - Nhận tham số tìm kiếm]]
- [[S04 - Lesson 03 - Request Body với Pydantic - Nhận dữ liệu JSON]]
- [[S04 - Lesson 04 - Type Hints trong FastAPI - Ràng buộc dữ liệu]]
### Bài tập
- [[S04 - [Vận dụng cơ bản 1] Sửa lỗi xung đột thứ tự Route trong API Sinh viên]]
- [[S04 - [Vận dụng cơ bản 2] Ràng buộc dữ liệu số học với Path Parameters]]
- [[S04 - [Vận dụng chuyên sâu] Thiết kế và validate API Đăng ký môn học]]
- [[S04 - [Phân tích] Lựa chọn Path Parameters vs Query Parameters]]
- [[S04 - [Sáng tạo] Xây dựng API Quản lý sản phẩm với validation động]]
- [[S04 - [BTTH] Phát triển bộ API quản lý điểm sinh viên hoàn chỉnh]]
### Quiz
- [[S04 - Quiz Cuối giờ]]
- [[S04 - Quiz Đầu giờ]]
### Bài giảng (outline)
- [[S04 - Bài giảng (Outline)]]
### Mindmap
- [[S04 - Mindmap]]

## Khái niệm cốt lõi
[[Path Parameter]] · [[Ép kiểu theo type hint (int-str)|Ép kiểu theo type hint (int/str)]] · [[Tự động validate 422]] · [[Thứ tự khai báo route]] · [[Enum cho giá trị định sẵn]] · [[RESTful naming]] · [[Query Parameter]] · [[Tham số mặc định (optional)]] · [[Tham số bắt buộc (required)]] · [[Optional - None|Optional / None]] · [[Kết hợp Path + Query]] · [[Pydantic BaseModel]] · [[Request Body]] · [[Khai báo schema]] · [[Tự động validate JSON]] · [[response_model]] · [[Định dạng JSON]] · [[Type Hints]] · [[Query() validation]] · [[Path() validation]] · [[Field() constraints]] · [[422 Unprocessable Entity]] · [[Swagger UI (-docs)|Swagger UI (/docs)]]
