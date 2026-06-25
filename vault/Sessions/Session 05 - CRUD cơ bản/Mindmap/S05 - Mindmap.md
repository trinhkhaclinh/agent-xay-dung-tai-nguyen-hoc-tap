---
type: "mindmap"
title: "Thao tác CRUD cơ bản in-memory"
session: 5
tags:
  - "type/mindmap"
  - "session/05"
deliverable_filename: "Session 05 - CRUD co ban"
status: "done"
---

# Thao tác CRUD cơ bản in-memory — Mindmap

- **Thao tác CRUD cơ bản in-memory**
  - 1. Create (Tạo dữ liệu)
    - HTTP Method: POST
    - HTTP Status Code: 201 Created
    - Logic nghiệp vụ: Kiểm tra trùng lặp email/ID trước khi lưu
  - 2. Read (Đọc dữ liệu)
    - HTTP Method: GET
    - HTTP Status Code: 200 OK
    - GET list: Lọc danh sách theo Query Parameter keyword
    - GET detail: Lấy theo ID, trả lỗi 404 Not Found nếu không tồn tại
  - 3. Update (Cập nhật)
    - HTTP Method: PUT (Ghi đè toàn bộ tài nguyên)
    - HTTP Method: PATCH (Cập nhật từng phần linh hoạt)
    - Tính chất: Idempotent (cập nhật nhiều lần cùng kết quả)
    - Xử lý lỗi: Trả 404 Not Found nếu ID không hợp lệ
  - 4. Delete (Xóa dữ liệu)
    - HTTP Method: DELETE
    - HTTP Status Code: 204 No Content (thành công, body trống)
    - Hard Delete (Xóa vật lý): Xóa vĩnh viễn bằng pop() hoặc DELETE FROM
    - Soft Delete (Xóa mềm): Đổi cờ trạng thái is_deleted = True để bảo toàn dữ liệu

— Thuộc [[Session 05 — MOC]]
