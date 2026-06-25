---
type: "mindmap"
title: "Parameters, Request body & Pydantic Validation"
session: 4
tags:
  - "type/mindmap"
  - "session/04"
deliverable_filename: "Session 04 - Parameters, Request body và Pydantic Validation"
status: "done"
---

# Parameters, Request body & Pydantic Validation — Mindmap

- **Parameters, Request body & Pydantic Validation**
  - 1. Path Parameters (Định danh tài nguyên)
    - Khai báo: dùng cặp ngoặc nhọn trong URL, ví dụ /students/{student_id}
    - Tự động ép kiểu & validate theo Type Hints của Python
    - Tránh xung đột route: Luôn đặt route tĩnh trước route động
  - 2. Query Parameters (Lọc & Tìm kiếm)
    - Khai báo: các tham số hàm không có trong route path
    - Phân loại: Bắt buộc (không mặc định) vs Tùy chọn (có mặc định)
    - Ép kiểu Boolean linh hoạt từ URL: true/false, 1/0, yes/no
  - 3. Request Body với Pydantic (Dữ liệu phức tạp)
    - Pydantic BaseModel: Định nghĩa cấu trúc dữ liệu JSON (Schema)
    - Tự động validate đầu vào & Trả lỗi 422 Unprocessable Entity
    -  response_model: Lọc dữ liệu đầu ra và bảo mật thông tin nhạy cảm
  - 4. Type Hints & Validation nâng cao
    - Ràng buộc Query Parameter: Dùng Query(min_length, max_length, ge, le)
    - Ràng buộc Path Parameter: Dùng Path(..., ge, le, description)
    - Ràng buộc thuộc tính Model: Dùng Field(..., gt, pattern)
    - Cấu trúc lỗi 422: Gồm loc (vị trí lỗi), msg (thông báo), type (loại lỗi)

— Thuộc [[Session 04 — MOC]]
