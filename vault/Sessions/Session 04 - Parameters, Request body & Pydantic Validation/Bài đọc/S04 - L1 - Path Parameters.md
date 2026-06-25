---
type: "bai-doc"
title: "Path Parameters"
session: 4
lesson: 1
tags:
  - "type/bai-doc"
  - "session/04"
concepts:
  - "[[Path Parameter]]"
  - "[[Ép kiểu theo type hint (int-str)|Ép kiểu theo type hint (int/str)]]"
  - "[[Tự động validate 422]]"
  - "[[Thứ tự khai báo route]]"
  - "[[Enum cho giá trị định sẵn]]"
  - "[[RESTful naming]]"
deliverable_filename: "BÀI ĐỌC_ PATH PARAMETERS TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Path Parameters - Định Danh Và Lấy Dữ Liệu Từ URL

Trong kiến trúc RESTful API, tài nguyên hệ thống được định danh thông qua đường dẫn URL. Khi chúng ta muốn thao tác trên một tài nguyên cụ thể (ví dụ: lấy thông tin của sinh viên có mã số 123), chúng ta cần truyền định danh đó vào URL. Trong FastAPI, cơ chế giúp chúng ta lấy phần biến động này từ URL được gọi là Path Parameters. Bài đọc này sẽ hướng dẫn chi tiết cách khai báo, ép kiểu dữ liệu và xử lý xung đột đường dẫn khi làm việc với Path Parameters.

## 1. Khái niệm và Cách hoạt động của Path Parameters

Path parameters (tham số đường dẫn) là các phần biến động nằm trực tiếp trong URL, được dùng để xác định tài nguyên cụ thể mà client muốn truy cập. Khác với query parameters (dùng cho tìm kiếm/lọc), path parameter đóng vai trò định vị tài nguyên độc bản.

Hãy tưởng tượng một tòa nhà ký túc xá. Địa chỉ chung là 'Ký túc xá A'. Nếu muốn tìm đúng phòng của một sinh viên, chúng ta cần số phòng cụ thể: 'Ký túc xá A / Phòng 402'. Ở đây, '402' chính là tham số đường dẫn để chỉ định căn phòng duy nhất. Tương tự, trong ứng dụng quản lý đào tạo, URL '/students/123' cho biết chúng ta đang muốn tương tác với sinh viên có mã số là 123.

## 2. Khai báo Path Parameters trong FastAPI

Để khai báo một path parameter trong FastAPI, chúng ta sử dụng dấu ngoặc nhọn `{}` trong đường dẫn của route decorator. Đồng thời, hàm xử lý bên dưới phải nhận một tham số có tên trùng khớp chính xác với tên tham số nằm trong dấu ngoặc nhọn.

```python
from fastapi import FastAPI

app = FastAPI()

# 1. Khai báo path parameter '{student_id}' trong route
@app.get("/students/{student_id}")
def get_student_detail(student_id: int): # 2. Khai báo tham số hàm trùng tên và có type hint
    # student_id đã được FastAPI tự động ép sang kiểu dữ liệu int
    return {
        "student_id": student_id,
        "name": "Nguyen Van An",
        "email": "an.nv@gmail.com",
        "status": "Active"
    }
```

Trong ví dụ trên, khi client gửi yêu cầu đến GET `/students/123`, FastAPI sẽ trích xuất giá trị '123' từ URL, tự động chuyển đổi nó sang kiểu số nguyên `int` và truyền vào hàm `get_student_detail` dưới dạng tham số `student_id`.

## 3. Ép kiểu và Tự động Validate dữ liệu (Lỗi 422)

Một thế mạnh cực lớn của FastAPI là khả năng tự động kiểm tra (validate) kiểu dữ liệu dựa trên Type Hints của Python. Khi chúng ta khai báo `student_id: int`, FastAPI hiểu rằng tham số này bắt buộc phải là số nguyên.

Nếu client gửi request hợp lệ như GET `/students/123`, hệ thống trả về kết quả 200 OK. Tuy nhiên, nếu client gửi request sai kiểu như GET `/students/abc` (trong đó 'abc' không thể chuyển đổi sang số nguyên), FastAPI sẽ ngay lập tức chặn lại và trả về mã trạng thái HTTP 422 (Unprocessable Entity) kèm thông báo lỗi chi tiết dạng JSON mà chúng ta không cần viết thêm bất kỳ dòng code kiểm tra nào.

```json
{
  "detail": [
    {
      "loc": ["path", "student_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

Cơ chế này giúp loại bỏ hoàn toàn các lỗi runtime do sai kiểu dữ liệu bên trong logic xử lý của ứng dụng, làm cho backend của chúng ta cực kỳ an toàn và ổn định.

## 4. Thứ tự khai báo Route và tránh xung đột

Khi khai báo nhiều route có cấu trúc đường dẫn tương tự nhau, thứ tự khai báo trong code là cực kỳ quan trọng. FastAPI phân giải các route theo thứ tự từ trên xuống dưới.

Giả sử chúng ta muốn có một route tĩnh là `/students/me` để lấy thông tin của chính sinh viên đang đăng nhập, và một route động `/students/{student_id}` để lấy thông tin sinh viên bất kỳ. Nếu chúng ta đặt route động `/students/{student_id}` phía TRƯỚC route tĩnh, khi client gọi GET `/students/me`, FastAPI sẽ khớp chuỗi 'me' vào tham số động `{student_id}`, cố gắng ép kiểu 'me' sang `int` và trả về lỗi 422.

Do đó, quy tắc vàng là: **Luôn đặt các route tĩnh (cụ thể) lên TRƯỚC các route động (chứa tham số).**

```python
# ĐÚNG: Route tĩnh đặt trước
@app.get("/students/me")
def get_my_profile():
    return {"student_id": 999, "name": "Sinh viên hiện tại (Tôi)"}

# Route động đặt sau
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    return {"student_id": student_id, "message": f"Thông tin chi tiết sinh viên {student_id}"}
```

## Tổng Kết

- Path parameters là các tham số biến động nằm trong URL dùng để định danh duy nhất một tài nguyên.
- FastAPI sử dụng Type Hints để tự động ép kiểu và validate dữ liệu của path parameter.
- Nếu truyền sai kiểu dữ liệu yêu cầu, FastAPI tự động trả về lỗi HTTP 422 Unprocessable Entity kèm mô tả chi tiết vị trí lỗi.
- Thứ tự khai báo route trong FastAPI rất quan trọng: Luôn đặt các route cụ thể (tĩnh) lên phía trước các route động chứa tham số để tránh xung đột đường dẫn.

## Tài Liệu Tham Khảo

- FastAPI Official Documentation - Path Parameters: https://fastapi.tiangolo.com/tutorial/path-params/
- Python Type Hints Tutorial: https://docs.python.org/3/library/typing.html

## Khái niệm liên quan

- [[Path Parameter]]
- [[Ép kiểu theo type hint (int-str)|Ép kiểu theo type hint (int/str)]]
- [[Tự động validate 422]]
- [[Thứ tự khai báo route]]
- [[Enum cho giá trị định sẵn]]
- [[RESTful naming]]

— Thuộc [[Session 04 — MOC]]
