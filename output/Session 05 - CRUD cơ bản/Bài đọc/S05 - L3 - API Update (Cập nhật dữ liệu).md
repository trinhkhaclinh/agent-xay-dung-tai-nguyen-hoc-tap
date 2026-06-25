---
type: "bai-doc"
title: "API Update (Cập nhật dữ liệu)"
session: 5
lesson: 3
tags:
  - "type/bai-doc"
  - "session/05"
concepts:
  - "[[PUT method]]"
  - "[[Idempotent update]]"
  - "[[Ghi đè thuộc tính]]"
  - "[[Cập nhật từng phần (PATCH)]]"
deliverable_filename: "BÀI ĐỌC_ API UPDATE TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: API Update - Phương Thức PUT, Ghi Đè Dữ Liệu Và Phân Biệt Với PATCH

Thao tác thứ ba trong CRUD là Update (Cập nhật dữ liệu). Trong thiết kế API chuẩn RESTful, thao tác cập nhật toàn bộ thuộc tính của tài nguyên thường sử dụng phương thức HTTP PUT. Bài đọc này giúp học viên triển khai thành công API PUT cập nhật thông tin sinh viên in-memory và phân tích so sánh chi tiết với phương thức PATCH.

## 1. Phương thức PUT và tính chất ghi đè toàn bộ

Phương thức PUT đại diện cho hành động thay thế/ghi đè hoàn toàn tài nguyên hiện tại bằng dữ liệu mới gửi lên từ client. Khi gọi PUT, client bắt buộc phải truyền đầy đủ các thuộc tính của đối tượng. Nếu thiếu một trường nào đó, trường đó có thể bị xóa hoặc đặt về giá trị mặc định tùy thiết kế hệ thống.

## 2. Triển khai API PUT cập nhật thông tin trong FastAPI

Khi nhận request PUT, đầu tiên ta dùng ID sinh viên để tìm kiếm sinh viên đó. Nếu tìm thấy, thực hiện ghi đè dữ liệu. Nếu không tìm thấy, trả về lỗi 404 Not Found.

```python
class StudentUpdateSchema(BaseModel):
    name: str
    email: str

@app.put("/students/{student_id}")
def update_student_info(student_id: int, student_data: StudentUpdateSchema):
    for s in students_db:
        if s["id"] == student_id:
            s["name"] = student_data.name
            s["email"] = student_data.email
            return {"message": "Cập nhật thành công", "data": s}
    raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên để cập nhật")
```

## 3. Phân biệt PUT và PATCH

Trong thiết kế API nâng cao, có hai phương thức cập nhật:

- **PUT (Replace):** Thay thế toàn bộ đối tượng. Phải truyền tất cả các trường. Mang tính chất idempotent.
- **PATCH (Modify):** Cập nhật từng phần (chỉ sửa các trường gửi lên). Client chỉ gửi các trường cần thay đổi (ví dụ: chỉ đổi mỗi email). Cần xử lý logic kiểm tra các trường truyền lên linh hoạt hơn.

## Tổng Kết

- PUT dùng để ghi đè toàn bộ tài nguyên hiện có và mang tính chất idempotent.
- Nếu ID tài nguyên không tồn tại, API PUT phải phản hồi lỗi 404 Not Found.
- Phân biệt rõ PUT (ghi đè toàn phần) và PATCH (cập nhật từng phần) khi thiết kế API hệ thống.

## Tài Liệu Tham Khảo

- MDN Web Docs - PUT: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT

## Khái niệm liên quan

- [[PUT method]]
- [[Idempotent update]]
- [[Ghi đè thuộc tính]]
- [[Cập nhật từng phần (PATCH)]]

— Thuộc [[Session 05 — MOC]]
