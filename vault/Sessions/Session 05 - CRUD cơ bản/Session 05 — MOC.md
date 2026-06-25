---
type: "session-moc"
title: "Session 05 — MOC"
session: 5
hinh_thuc_hoc: "Lý thuyết"
lessons: 4
tags:
  - "type/moc"
  - "session/05"
status: "done"
---

# Session 05 — CRUD cơ bản

> Thuộc [[IT-215 FastAPI — MOC]]

Học cách thiết kế và triển khai 4 thao tác quản lý dữ liệu cơ bản (CRUD) in-memory bằng FastAPI: API Create (POST), API Read (GET), API Update (PUT), và API Delete (DELETE) kết hợp xử lý các mã trạng thái HTTP thích hợp và kiểm chứng dữ liệu bằng Pydantic.

## Mục tiêu học tập
- **Lesson 1 — API Create (Tạo dữ liệu)**
    - Triển khai (Vận dụng) Endpoint POST để nhận dữ liệu và thêm mới sinh viên/khóa học
    - Giải thích (Hiểu) mã trạng thái HTTP 201 Created và cách phản hồi dữ liệu sau khi tạo thành công
- **Lesson 2 — API Read (Đọc dữ liệu)**
    - Triển khai (Vận dụng) API GET lấy danh sách toàn bộ hoặc lọc theo từ khóa
    - Triển khai (Vận dụng) API GET lấy chi tiết một sinh viên theo ID và trả về lỗi 404 nếu không tìm thấy
- **Lesson 3 — API Update (Cập nhật dữ liệu)**
    - Triển khai (Vận dụng) API PUT để ghi đè cập nhật thông tin tài nguyên
    - Phân tích (Phân tích) sự khác biệt giữa ghi đè toàn bộ (PUT) và cập nhật từng phần (PATCH)
- **Lesson 4 — API Delete (Xóa dữ liệu)**
    - Triển khai (Vận dụng) API DELETE để xóa bỏ tài nguyên
    - Giải thích (Hiểu) các mã trạng thái HTTP phản hồi khi xóa thành công (204 No Content hoặc 200 OK)

## Tài nguyên
### Bài đọc
- [[S05 - L1 - API Create (Tạo dữ liệu)]]
- [[S05 - L2 - API Read (Đọc dữ liệu)]]
- [[S05 - L3 - API Update (Cập nhật dữ liệu)]]
- [[S05 - L4 - API Delete (Xóa dữ liệu)]]
### Kịch bản video
- [[S05 - Lesson 01 - API Create - Tạo dữ liệu với phương thức POST]]
- [[S05 - Lesson 02 - API Read - Lấy danh sách và chi tiết dữ liệu với GET]]
- [[S05 - Lesson 03 - API Update - Cập nhật dữ liệu với PUT]]
- [[S05 - Lesson 04 - API Delete - Xóa dữ liệu với phương thức DELETE]]
### Bài tập
- [[S05 - [Vận dụng cơ bản 1] Sửa lỗi trùng lặp dữ liệu và mã trạng thái trong API POST]]
- [[S05 - [Vận dụng cơ bản 2] Bổ sung kiểm tra lỗi 404 cho API xóa và cập nhật]]
- [[S05 - [Vận dụng chuyên sâu] Triển khai API PATCH cập nhật từng phần]]
- [[S05 - [Phân tích] Phân tích tính Idempotent của các phương thức HTTP]]
- [[S05 - [Sáng tạo] Thiết kế cơ chế Xóa mềm (Soft Delete) trong FastAPI]]
- [[S05 - [BTTH] Phát triển ứng dụng quản lý sách thư viện hoàn chỉnh]]
### Quiz
- [[S05 - Quiz Cuối giờ]]
- [[S05 - Quiz Đầu giờ]]
### Bài giảng (outline)
- [[S05 - Bài giảng (Outline)]]
### Mindmap
- [[S05 - Mindmap]]

## Khái niệm cốt lõi
[[POST method]] · [[HTTP 201 Created]] · [[In-memory database]] · [[Dữ liệu trùng lặp]] · [[GET method]] · [[HTTP 200 OK]] · [[HTTP 404 Not Found]] · [[Lọc danh sách]] · [[PUT method]] · [[Idempotent update]] · [[Ghi đè thuộc tính]] · [[Cập nhật từng phần (PATCH)]] · [[DELETE method]] · [[HTTP 204 No Content]] · [[Xóa vật lý]] · [[Xóa mềm (Soft Delete)]]
