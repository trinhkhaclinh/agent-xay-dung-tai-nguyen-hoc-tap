---
type: "bai-doc"
title: "Type Hints trong FastAPI"
session: 4
lesson: 4
tags:
  - "type/bai-doc"
  - "session/04"
concepts:
  - "[[Type Hints]]"
  - "[[Query() validation]]"
  - "[[Path() validation]]"
  - "[[Field() constraints]]"
  - "[[422 Unprocessable Entity]]"
  - "[[Swagger UI (-docs)|Swagger UI (/docs)]]"
deliverable_filename: "BÀI ĐỌC_ TYPE HINTS TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Ràng Buộc Dữ Liệu Nâng Cao Bằng Type Hints Và Thư Viện FastAPI

Xác định kiểu dữ liệu (như số hay chuỗi) là chưa đủ đối với một hệ thống thực tế. Chúng ta cần những ràng buộc chặt chẽ hơn: từ khóa tìm kiếm phải có độ dài từ 2 đến 50 ký tự; số trang phải lớn hơn hoặc bằng 1; giá sản phẩm phải lớn hơn 0; hay mã số sinh viên phải tuân theo một định dạng nhất định. FastAPI cung cấp các công cụ đắc lực như `Path()`, `Query()`, và `Field()` tích hợp trực tiếp vào hệ thống Type Hints để khai báo các ràng buộc dữ liệu này một cách trực quan nhất. Bài đọc này giúp chúng ta làm chủ kỹ năng này.

## 1. Vai trò của Type Hints làm nền tảng cho validation tự động

Type hints trong Python ban đầu sinh ra chỉ để phục vụ cho việc nhắc mã nguồn và kiểm tra tĩnh. Tuy nhiên, FastAPI và Pydantic đã tận dụng tối đa sức mạnh của nó để thực hiện kiểm chứng dữ liệu động khi runtime. Không có type hints, FastAPI không thể biết cách ép kiểu và validate dữ liệu.

## 2. Sử dụng Query() để validate Query Parameters

Để thêm các ràng buộc validation (độ dài chuỗi, biểu thức chính quy, mô tả hiển thị trên Swagger) cho query parameter, chúng ta sử dụng hàm `Query()` từ thư viện `fastapi` làm giá trị mặc định của tham số.

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/products")
def search_products(
    keyword: str = Query(
        None, 
        min_length=2, 
        max_length=50, 
        description="Từ khóa tìm kiếm sản phẩm"
    ),
    page: int = Query(1, ge=1, description="Số trang, tối thiểu là 1")
):
    return {"keyword": keyword, "page": page}
```

Trong đoạn code trên:
- `min_length=2`: từ khóa tìm kiếm phải có ít nhất 2 ký tự.
- `max_length=50`: tối đa 50 ký tự.
- `ge=1` (Greater than or Equal): số trang phải lớn hơn hoặc bằng 1. Nếu client vi phạm, FastAPI lập tức trả lỗi 422.

## 3. Sử dụng Path() để validate Path Parameters

Tương tự như `Query()`, chúng ta sử dụng `Path()` để đặt các ràng buộc cho path parameter. Tuy nhiên, vì path parameter luôn luôn là bắt buộc, đối số đầu tiên truyền vào `Path()` phải là dấu ba chấm `...` (biểu thị required).

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/students/{student_id}")
def get_student(
    student_id: int = Path(..., ge=1, le=1000, description="Mã ID sinh viên, từ 1 đến 1000")
):
    return {"student_id": student_id}
```

Nếu client gọi `/students/0` hoặc `/students/1500`, yêu cầu sẽ bị chặn lại ngay lập tức do vi phạm ràng buộc số học `ge=1` và `le=1000`.

## 4. Sử dụng Field() để validate thuộc tính Pydantic Model

Để áp dụng validation bên trong Pydantic model (request body), chúng ta dùng hàm `Field()` từ thư viện `pydantic`. Các đối số ràng buộc của `Field()` hoàn toàn tương đồng với `Query()` và `Path()`.

```python
from pydantic import BaseModel, Field

class StudentCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Họ và tên sinh viên")
    email: str = Field(..., pattern=r"^\S+@\S+\.\S+$", description="Email đúng định dạng")
    age: int = Field(..., gt=18, lt=100, description="Tuổi phải từ 19 đến 99")
    gpa: float = Field(0.0, ge=0.0, le=4.0, description="GPA hệ 4, từ 0 đến 4.0")
```

Lưu ý:
- Đối số đầu tiên `...` chỉ ra rằng thuộc tính đó là bắt buộc phải truyền.
- `pattern`: Sử dụng regex (biểu thức chính quy) để kiểm tra định dạng email.
- `gt=18` (Greater Than): lớn hơn 18 tuổi.
- `lt=100` (Less Than): nhỏ hơn 100 tuổi.

## 5. Phân tích cấu trúc lỗi 422 (Unprocessable Entity)

Khi một ràng buộc bị vi phạm, FastAPI trả về mã lỗi 422 kèm cấu trúc JSON lỗi chuẩn hóa. Dưới đây là phân tích chi tiết cấu trúc này:

- `loc` (Location): Vị trí xảy ra lỗi, ví dụ `["body", "age"]` chỉ ra lỗi nằm trong request body ở trường age; hoặc `["query", "keyword"]` chỉ ra lỗi nằm ở query parameter keyword trên URL.
- `msg` (Message): Mô tả chi tiết về lỗi xảy ra (ví dụ: 'ensure this value is greater than 18').
- `type` (Type): Mã loại lỗi để lập trình viên frontend có thể bắt lỗi tự động (ví dụ `value_error.number.not_gt`).

Hiểu rõ cấu trúc này giúp các nhà phát triển frontend dễ dàng bắt lỗi và hiển thị cảnh báo đỏ trên giao diện người dùng một cách chính xác nhất.

## Tổng Kết

- FastAPI tích hợp Type Hints để khai báo validation cực kỳ tường minh.
- Dùng Query() để validate query parameter, Path() để validate path parameter và Field() để validate Pydantic model.
- Các ràng buộc bao gồm: độ dài chuỗi (min_length, max_length), khoảng số học (ge, le, gt, lt), regex pattern.
- Lỗi 422 chứa thông tin chi tiết về vị trí (loc), thông điệp (msg), và loại lỗi (type), giúp lập trình viên dễ dàng debug.

## Tài Liệu Tham Khảo

- FastAPI Query Parameters and String Validations: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
- FastAPI Path Parameters and Numeric Validations: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/

## Khái niệm liên quan

- [[Type Hints]]
- [[Query() validation]]
- [[Path() validation]]
- [[Field() constraints]]
- [[422 Unprocessable Entity]]
- [[Swagger UI (-docs)|Swagger UI (/docs)]]

— Thuộc [[Session 04 — MOC]]
