---
type: "bai-doc"
title: "Request Body với Pydantic"
session: 4
lesson: 3
tags:
  - "type/bai-doc"
  - "session/04"
concepts:
  - "[[Pydantic BaseModel]]"
  - "[[Request Body]]"
  - "[[Khai báo schema]]"
  - "[[Tự động validate JSON]]"
  - "[[response_model]]"
  - "[[Định dạng JSON]]"
deliverable_filename: "BÀI ĐỌC_ REQUEST BODY VỚI PYDANTIC_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Request Body - Nhận Và Kiểm Chứng Dữ Liệu JSON Bằng Pydantic Model

Khi client muốn tạo mới hoặc cập nhật một tài nguyên lớn (ví dụ: đăng ký tài khoản sinh viên mới gồm họ tên, email, ngày sinh, mật khẩu), việc gửi dữ liệu qua URL là không an toàn và bị giới hạn độ dài. Thay vào đó, dữ liệu được đóng gói trong phần thân của yêu cầu (Request Body) dưới định dạng JSON. Trong FastAPI, chúng ta sử dụng Pydantic để định nghĩa cấu trúc dữ liệu mong muốn (Schema) và tự động xác thực toàn bộ dữ liệu JSON này.

## 1. Khái niệm Request Body và vai trò của Pydantic BaseModel

Request Body là phần thân chứa dữ liệu của HTTP request (thường đi với POST, PUT, PATCH). Để nhận diện và kiểm chứng cấu trúc của dữ liệu JSON gửi lên từ client, FastAPI tích hợp chặt chẽ với Pydantic - một thư viện xác thực dữ liệu hàng đầu trong Python.

Pydantic giúp chúng ta định nghĩa một class kế thừa từ `BaseModel`. Mỗi thuộc tính khai báo trong class này đại diện cho một trường thông tin mà chúng ta yêu cầu client phải gửi lên, kèm theo kiểu dữ liệu mong muốn của trường đó.

## 2. Triển khai Request Body với Pydantic trong FastAPI

Để nhận request body, đầu tiên ta định nghĩa lớp kế thừa `BaseModel`. Sau đó khai báo tham số hàm route có kiểu dữ liệu là lớp vừa định nghĩa.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Định nghĩa Schema (cấu trúc dữ liệu mong muốn)
class StudentCreate(BaseModel):
    name: str
    email: str
    age: int
    is_enrolled: bool = True # Trường tùy chọn có giá trị mặc định

# 2. Áp dụng schema vào route xử lý POST
@app.post("/students")
def create_student(student: StudentCreate): 
    # FastAPI tự động đọc JSON từ Request Body, validate cấu trúc,
    # và chuyển đổi thành một đối tượng student kiểu StudentCreate.
    student_dict = student.dict()
    # Thao tác xử lý dữ liệu (ví dụ lưu vào DB)
    student_dict["id"] = 101 
    return {
        "message": "Tạo sinh viên thành công",
        "student": student_dict
    }
```

Khi client gửi một POST request đến `/students` với body JSON:
`{"name": "Nguyen Van An", "email": "an.nv@gmail.com", "age": 20}`
FastAPI sẽ kiểm tra tính hợp lệ và truyền đối tượng `student` đã được xác thực vào hàm. Chúng ta có thể truy cập thuộc tính bằng cú pháp hướng đối tượng `student.name` hoặc chuyển thành dict bằng `student.dict()`.

## 3. Tự động kiểm chứng JSON và xử lý lỗi 422

Nếu client gửi một JSON không đúng cấu trúc đã định nghĩa, ví dụ: thiếu trường `name` bắt buộc, hoặc truyền trường `age` dưới dạng chuỗi chữ không thể ép kiểu (ví dụ `"twenty"`), FastAPI sẽ tự động chặn request lại và trả về lỗi 422 Unprocessable Entity kèm theo thông tin chi tiết chính xác lỗi xảy ra ở đâu, thuộc loại nào.

Nhờ đó, lập trình viên không phải viết hàng chục dòng code `if/else` để kiểm tra sự tồn tại và tính hợp lệ của từng trường dữ liệu, giúp code backend ngắn gọn, sạch sẽ và an toàn hơn.

## 4. Lợi ích của response_model và Pydantic lồng nhau

Pydantic còn hỗ trợ mô tả các cấu trúc dữ liệu phức tạp (lồng nhau) và kiểm soát dữ liệu trả về thông qua `response_model`:

- **Pydantic model lồng nhau:** Một thuộc tính trong model có thể có kiểu dữ liệu là một model khác (ví dụ: trường `address` có kiểu dữ liệu là model `AddressSchema` gồm tỉnh/thành phố, quận/huyện).
- **response_model:** Khai báo trong decorator (ví dụ `@app.post('/students', response_model=StudentOut)`), giúp lọc bớt dữ liệu nhạy cảm trước khi trả về cho client (ví dụ ẩn mật khẩu sinh viên hoặc ngày tạo) và đảm bảo cấu trúc response trả về chuẩn hóa.

## Tổng Kết

- Request body dùng để truyền tải dữ liệu có cấu trúc lớn và phức tạp dưới dạng JSON trong thân HTTP request.
- FastAPI sử dụng Pydantic BaseModel để định nghĩa cấu trúc (schema) dữ liệu.
- FastAPI tự động validate toàn bộ dữ liệu body JSON gửi lên và trả về lỗi 422 nếu dữ liệu không khớp với schema.
- Pydantic hỗ trợ các cấu trúc dữ liệu lồng nhau và giúp chuẩn hóa đầu ra của API qua tham số response_model.

## Tài Liệu Tham Khảo

- FastAPI Official Documentation - Request Body: https://fastapi.tiangolo.com/tutorial/body/
- Pydantic Official Documentation: https://docs.pydantic.dev/

## Khái niệm liên quan

- [[Pydantic BaseModel]]
- [[Request Body]]
- [[Khai báo schema]]
- [[Tự động validate JSON]]
- [[response_model]]
- [[Định dạng JSON]]

— Thuộc [[Session 04 — MOC]]
