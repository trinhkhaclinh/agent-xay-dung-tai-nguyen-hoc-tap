---
type: "bai-doc"
title: "API Create (Tạo dữ liệu)"
session: 5
lesson: 1
tags:
  - "type/bai-doc"
  - "session/05"
concepts:
  - "[[POST method]]"
  - "[[HTTP 201 Created]]"
  - "[[In-memory database]]"
  - "[[Dữ liệu trùng lặp]]"
deliverable_filename: "BÀI ĐỌC_ API CREATE TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: API Create - Phương Thức POST Và Trạng Thái 201 Created

Thao tác đầu tiên trong chu trình CRUD là Create (Tạo mới). Trong thiết kế hệ thống phần mềm web RESTful API, việc tạo mới một thực thể tài nguyên (như tạo mới một hồ sơ sinh viên hoặc thêm một lớp học mới) luôn được ánh xạ tới phương thức HTTP POST. Bài đọc này giúp chúng ta làm chủ kỹ năng thiết kế Endpoint POST, xử lý mã trạng thái phản hồi chuẩn 201 Created và kiểm tra logic trùng lặp dữ liệu.

## 1. Phương thức POST và kiến trúc RESTful

Khác với GET dùng để truy xuất, POST là phương thức dùng để gửi dữ liệu lên server nhằm tạo ra một tài nguyên mới. POST không mang tính chất idempotent (không đồng nhất): nếu client gửi hai request POST giống hệt nhau liên tiếp, server thông thường sẽ tạo ra hai tài nguyên mới có ID khác nhau.

## 2. Trạng thái HTTP 201 Created

Khi một tài nguyên được tạo thành công ở phía Backend, mã trạng thái HTTP chuẩn xác cần trả về là 201 Created. Điều này thông báo cho phía Client (Frontend) biết rằng dữ liệu đã được ghi nhận bền vững và hệ thống đã cấp phát định danh (ID) mới cho tài nguyên đó.

## 3. Triển khai API POST và Kiểm tra Trùng lặp

Khi viết code tạo mới, chúng ta cần thực hiện các bước: nhận dữ liệu từ request body, kiểm tra logic nghiệp vụ (email không được trùng, mã số học viên phải duy nhất), thêm dữ liệu vào kho lưu trữ (in-memory list hoặc cơ sở dữ liệu), và trả về thông tin đối tượng kèm mã 201 Created.

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()
students_db = []

class StudentCreate(BaseModel):
    name: str
    email: str

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    # 1. Kiểm tra trùng lặp email
    for s in students_db:
        if s["email"] == student.email:
            raise HTTPException(status_code=400, detail="Email đã được sử dụng")
            
    # 2. Tạo đối tượng mới kèm cấp ID tự động
    new_id = len(students_db) + 1
    new_student = {"id": new_id, "name": student.name, "email": student.email}
    
    # 3. Thêm vào database in-memory
    students_db.append(new_student)
    return new_student
```

## Tổng Kết

- Phương thức POST dùng để tạo tài nguyên mới và không mang tính chất idempotent.
- HTTP 201 Created là mã phản hồi chuẩn sau khi tạo tài nguyên thành công.
- Cần kiểm tra các ràng buộc nghiệp vụ (trùng lặp dữ liệu độc bản) trước khi thêm mới.

## Tài Liệu Tham Khảo

- MDN Web Docs - POST: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST
- FastAPI Status Codes: https://fastapi.tiangolo.com/tutorial/response-status-code/

## Khái niệm liên quan

- [[POST method]]
- [[HTTP 201 Created]]
- [[In-memory database]]
- [[Dữ liệu trùng lặp]]

— Thuộc [[Session 05 — MOC]]
