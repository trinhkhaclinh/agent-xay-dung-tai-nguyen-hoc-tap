---
type: "bai-giang-outline"
title: "CRUD cơ bản"
session: 5
slide_count: 16
tags:
  - "type/bai-giang"
  - "session/05"
deliverable_filename: "Session 05 - CRUD co ban"
status: "done"
---

# CRUD cơ bản — Outline bài giảng

## Slide 1 — [title] CRUD cơ bản
- Session 05
- [MODULE IT-215] - Phát triển dịch vụ web với FastAPI
- Phiên bản: 1.0

## Slide 2 — [agenda] Nội dung bài học
*Phần: NỘI DUNG*
- 1. API Create: Tạo dữ liệu (POST)
- 2. API Read: Đọc dữ liệu (GET)
- 3. API Update: Cập nhật dữ liệu (PUT)
- 4. API Delete: Xóa dữ liệu (DELETE)

## Slide 3 — [section-title] Phần 1: API Create - Tạo mới dữ liệu
*Phần: 1. API Create*
- Phương thức HTTP POST
- Mã phản hồi 201 Created
- Kiểm tra trùng lặp in-memory

## Slide 4 — [bullets] Thao tác Create với POST
*Phần: 1. API Create*
- Dùng để gửi dữ liệu từ Request Body lên server nhằm tạo tài nguyên mới.
- Không mang tính chất idempotent: mỗi lần gọi POST thành công sinh ra 1 tài nguyên mới.
- Phản hồi thành công: HTTP 201 Created kèm đối tượng vừa tạo.

## Slide 5 — [code] Triển khai POST API trong FastAPI
*Phần: 1. API Create*
- @app.post("/students", status_code=201)
def create(student: StudentCreate):
    # logic validate email trùng lặp
    # append vào list in-memory
    return new_student
**Speaker notes:** Hướng dẫn cấu hình status_code=201 trong decorator và xử lý trùng lặp email.

## Slide 6 — [section-title] Phần 2: API Read - Truy xuất dữ liệu
*Phần: 2. API Read*
- Phương thức HTTP GET
- Lọc danh sách theo keyword
- Xử lý chi tiết và lỗi 404 Not Found

## Slide 7 — [bullets] Thao tác Read với GET
*Phần: 2. API Read*
- Đọc dữ liệu từ server, mang tính chất an toàn (Safe) và đồng nhất (Idempotent).
- GET /students: Lấy danh sách toàn bộ, kết hợp query parameter để tìm kiếm.
- GET /students/{id}: Lấy chi tiết. Trả về 404 Not Found nếu ID không tồn tại.

## Slide 8 — [code] Triển khai GET API trong FastAPI
*Phần: 2. API Read*
- @app.get("/students/{student_id}")
def detail(student_id: int):
    # tìm sinh viên khớp ID
    # không thấy -> raise HTTPException(status_code=404)
    return student
**Speaker notes:** Giải thích mã lỗi 404 Not Found và cách ném lỗi với HTTPException.

## Slide 9 — [section-title] Phần 3: API Update - Cập nhật dữ liệu
*Phần: 3. API Update*
- Phương thức HTTP PUT
- Tính chất ghi đè toàn bộ
- Phân biệt PUT và PATCH

## Slide 10 — [bullets] Thao tác Update với PUT
*Phần: 3. API Update*
- PUT dùng để ghi đè/thay thế hoàn toàn tài nguyên đang tồn tại.
- Client phải gửi lên toàn bộ các trường của schema.
- Khác biệt với PATCH: PATCH chỉ cập nhật một vài trường được chỉ định (cập nhật từng phần).

## Slide 11 — [code] Triển khai PUT API trong FastAPI
*Phần: 3. API Update*
- @app.put("/students/{student_id}")
def update(student_id: int, data: StudentUpdate):
    # tìm ID -> ghi đè name, email
    # không thấy -> raise 404 Not Found
    return updated_student
**Speaker notes:** Hướng dẫn cách viết logic ghi đè thuộc tính in-memory.

## Slide 12 — [section-title] Phần 4: API Delete - Xóa dữ liệu
*Phần: 4. API Delete*
- Phương thức HTTP DELETE
- Mã trạng thái 204 No Content
- Xóa vật lý vs Xóa mềm (Soft Delete)

## Slide 13 — [bullets] Thao tác Delete với DELETE
*Phần: 4. API Delete*
- DELETE dùng để loại bỏ tài nguyên ra khỏi hệ thống.
- Xóa thành công thường trả về mã 204 No Content (body trống) hoặc 200 OK.
- Phân loại: Xóa vật lý (xóa vĩnh viễn) và Xóa mềm (chỉ đổi cờ trạng thái is_deleted = True).

## Slide 14 — [code] Triển khai DELETE API trong FastAPI
*Phần: 4. API Delete*
- @app.delete("/students/{student_id}", status_code=204)
def delete(student_id: int):
    # tìm ID -> pop khỏi list
    # không thấy -> raise 404
    return # 204 trả về body rỗng
**Speaker notes:** Giải thích mã 204 No Content và cách trả về body trống khi xóa thành công.

## Slide 15 — [summary] Tổng kết bài học
*Phần: TỔNG KẾT*
- Create: HTTP POST, trả về 201 Created.
- Read: HTTP GET, an toàn/idempotent, trả lỗi 404 Not Found.
- Update: HTTP PUT, ghi đè toàn bộ, phân biệt với PATCH cập nhật từng phần.
- Delete: HTTP DELETE, xóa vật lý hoặc xóa mềm, trả về 204 No Content.

## Slide 16 — [closing] KẾT THÚC
- HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN

## Khái niệm liên quan

- [[POST method]]
- [[HTTP 201 Created]]
- [[In-memory database]]
- [[Dữ liệu trùng lặp]]
- [[GET method]]
- [[HTTP 200 OK]]
- [[HTTP 404 Not Found]]
- [[Lọc danh sách]]
- [[PUT method]]
- [[Idempotent update]]
- [[Ghi đè thuộc tính]]
- [[Cập nhật từng phần (PATCH)]]
- [[DELETE method]]
- [[HTTP 204 No Content]]
- [[Xóa vật lý]]
- [[Xóa mềm (Soft Delete)]]

— Thuộc [[Session 05 — MOC]]
