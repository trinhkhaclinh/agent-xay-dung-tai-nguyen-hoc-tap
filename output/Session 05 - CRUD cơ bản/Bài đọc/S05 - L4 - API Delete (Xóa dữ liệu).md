---
type: "bai-doc"
title: "API Delete (Xóa dữ liệu)"
session: 5
lesson: 4
tags:
  - "type/bai-doc"
  - "session/05"
concepts:
  - "[[DELETE method]]"
  - "[[HTTP 204 No Content]]"
  - "[[Xóa vật lý]]"
  - "[[Xóa mềm (Soft Delete)]]"
deliverable_filename: "BÀI ĐỌC_ API DELETE TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: API Delete - Phương Thức DELETE, Trạng Thái 204 No Content Và Xóa Mềm

Thao tác cuối cùng trong CRUD là Delete (Xóa dữ liệu). Trong thiết kế API chuẩn RESTful, việc loại bỏ một tài nguyên khỏi hệ thống sử dụng phương thức HTTP DELETE. Bài đọc này hướng dẫn chi tiết cách triển khai API DELETE xóa sinh viên theo ID, làm quen với mã phản hồi 204 No Content và tìm hiểu về khái niệm Xóa mềm (Soft Delete) trong thiết kế database.

## 1. Phương thức DELETE và tính chất Idempotent

Phương thức DELETE dùng để xóa tài nguyên được chỉ định. Đây cũng là một phương thức idempotent: xóa lần đầu thành công trả về 200/204; các lần sau tài nguyên đã biến mất nên hệ thống có thể trả lỗi 404, nhưng trạng thái thực tế của máy chủ không thay đổi thêm (tài nguyên vẫn ở trạng thái đã bị xóa).

## 2. Triển khai API DELETE với trạng thái 204 No Content

Khi xóa thành công, nếu server không có dữ liệu nào cần gửi lại cho client ngoài thông điệp thành công, mã trạng thái HTTP chuẩn xác nhất cần phản hồi là 204 No Content.

```python
@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_student(student_id: int):
    global students_db
    for idx, s in enumerate(students_db):
        if s["id"] == student_id:
            students_db.pop(idx)
            return # Kết thúc hàm, trả về 204 No Content không kèm body
    raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên để xóa")
```

## 3. Xóa vật lý (Hard Delete) và Xóa mềm (Soft Delete)

Trong thực tế dự án doanh nghiệp, việc xóa bỏ hoàn toàn dữ liệu khỏi cơ sở dữ liệu (Hard Delete) là hành động mạo hiểm và có thể gây mất tính toàn vẹn dữ liệu liên kết. Thay vào đó, người ta thường dùng Xóa mềm (Soft Delete):

- **Xóa vật lý (Hard Delete):** Dùng lệnh `pop()` hoặc `DELETE FROM` để xóa hoàn toàn bản ghi khỏi bộ nhớ.
- **Xóa mềm (Soft Delete):** Thêm một trường trạng thái (ví dụ `is_deleted: bool = False` hoặc `deleted_at: datetime = None`). Khi gọi DELETE, API chỉ chuyển đổi `is_deleted = True`. Các API GET danh sách sau đó sẽ lọc bỏ các sinh viên có `is_deleted == True`.

## Tổng Kết

- Phương thức DELETE dùng để loại bỏ tài nguyên và mang tính chất idempotent.
- Mã HTTP 204 No Content được sử dụng để phản hồi khi xóa thành công và không cần trả về nội dung body.
- Xóa mềm (Soft Delete) là giải pháp tối ưu trong các dự án thực tế để bảo toàn dữ liệu lịch sử.

## Tài Liệu Tham Khảo

- MDN Web Docs - DELETE: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE

## Khái niệm liên quan

- [[DELETE method]]
- [[HTTP 204 No Content]]
- [[Xóa vật lý]]
- [[Xóa mềm (Soft Delete)]]

— Thuộc [[Session 05 — MOC]]
