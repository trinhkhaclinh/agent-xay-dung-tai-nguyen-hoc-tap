---
type: "bai-tap"
title: "[BTTH] Phát triển ứng dụng quản lý sách thư viện hoàn chỉnh"
session: 5
level: "Tổng hợp"
bloom: "Tổng hợp"
ex_code: "Ex06"
tags:
  - "type/bai-tap"
  - "session/05"
deliverable_filename: "[BTTH] Phát triển ứng dụng quản lý sách thư viện hoàn chỉnh"
status: "done"
---

# Bài tập thực hành tổng hợp: CRUD Thư viện Sách

## 1. Bối cảnh nghiệp vụ

Học viên cần xây dựng một ứng dụng nhỏ quản lý sách trong thư viện trường học in-memory đầy đủ 4 thao tác tạo mới, lấy danh sách, sửa đổi và xóa sách.

## 2. Yêu cầu kỹ thuật

- POST `/books`: Thêm sách mới gồm `title` (str, >=2 ký tự), `author` (str), `isbn` (str, phải duy nhất). Trả về 201 Created.
- GET `/books`: Trả về danh sách sách, hỗ trợ lọc theo query `author` (tùy chọn).
- GET `/books/{book_id}`: Trả về chi tiết sách theo ID, lỗi 404 nếu không tìm thấy.
- PUT `/books/{book_id}`: Ghi đè cập nhật sách, lỗi 404 nếu không thấy.
- DELETE `/books/{book_id}`: Xóa sách, trả về 204 No Content, lỗi 404 nếu không thấy.

## 3. Yêu cầu đầu ra

- Viết file `main.py` hoàn chỉnh, cấu hình đầy đủ Pydantic Schemas và chạy được bằng Uvicorn.
- Thực hiện demo đầy đủ cả 5 API trên Swagger UI.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session05_Ex06
```

```
HNKS25CNTT1_FastAPI_Session05_Ex06
```

— Thuộc [[Session 05 — MOC]]
