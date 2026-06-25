---
type: "bai-tap"
title: "[Vận dụng chuyên sâu] API đăng ký sinh viên"
session: 2
level: "Vận dụng chuyên sâu"
bloom: "Vận dụng"
ex_code: "Ex03"
tags:
  - "type/bai-tap"
  - "session/02"
deliverable_filename: "[Vận dụng chuyên sâu] API đăng ký sinh viên"
status: "done"
---

# API đăng ký sinh viên

## 1. Bối cảnh nghiệp vụ

Trung tâm đào tạo mở cổng đăng ký sinh viên mới đầu khóa. Bộ phận tuyển sinh cần một API cho phép Frontend gửi thông tin của một sinh viên lên hệ thống để tạo hồ sơ. Đây là thao tác tạo mới tài nguyên, vì vậy phải dùng đúng HTTP method theo ánh xạ CRUD đã học (POST = Create).

Hệ thống hiện chỉ mới có endpoint GET /students để liệt kê. Bạn cần bổ sung luồng đăng ký hoàn chỉnh cho danh sách lưu tạm trong bộ nhớ (in-memory) ở phạm vi của session này.

## 2. Quy tắc nghiệp vụ

- Mỗi sinh viên gồm các trường: name (họ tên), email, class_name (lớp). ID do hệ thống tự sinh, Client không gửi lên.
- Khi đăng ký thành công, hệ thống cấp một id tăng dần (auto-increment) và trả về toàn bộ hồ sơ vừa tạo.
- Không cho phép đăng ký trùng email: nếu email đã tồn tại trong danh sách, API phải báo lỗi rõ ràng.
- Endpoint tuân thủ RESTful: tạo mới tài nguyên students bằng POST /students (không dùng /createStudent hay /addStudent).

## 3. Mã nguồn hiện tại (Legacy Code)

Đoạn code khởi điểm dưới đây mới chỉ có danh sách tạm và endpoint liệt kê. Bạn cần bổ sung endpoint đăng ký.

```python
# main.py - điểm khởi đầu, cần bổ sung endpoint đăng ký
from fastapi import FastAPI

app = FastAPI(title="Student Registration API")

# Danh sách lưu tạm trong bộ nhớ
students_db = [
    {"id": 1, "name": "Nguyen Van An", "email": "an@ptit.edu.vn", "class_name": "CNTT1"}
]

@app.get("/students")
def list_students():
    return students_db

# TODO: bổ sung endpoint đăng ký sinh viên mới (POST /students)
```

## 4. Yêu cầu

### Phần 1 — Triển khai endpoint đăng ký

- Viết endpoint POST /students nhận vào name, email, class_name của sinh viên cần đăng ký.
- Tự sinh id mới bằng cách lấy id lớn nhất hiện có cộng thêm 1 (hoặc dùng độ dài danh sách + 1).
- Thêm hồ sơ mới vào students_db và trả về hồ sơ vừa tạo (gồm cả id) cho Client.

### Phần 2 — Xử lý quy tắc nghiệp vụ

- Trước khi tạo mới, kiểm tra email gửi lên đã tồn tại trong students_db hay chưa.
- Nếu email đã tồn tại, trả về thông báo lỗi rõ ràng (ví dụ trường error mô tả email bị trùng) thay vì tạo bản ghi trùng.
- Đảm bảo dùng đúng HTTP method POST cho thao tác tạo mới và giữ tên endpoint là /students.

### Phần 3 — Kiểm thử trên Swagger UI

1. Chạy server bằng uvicorn main:app --reload.
2. Mở Swagger UI tại http://127.0.0.1:8000/docs, dùng Try it out gửi một sinh viên mới và xác nhận phản hồi có id tự sinh.
3. Gửi lại đúng email vừa tạo và xác nhận hệ thống báo lỗi trùng email.
4. Gọi GET /students để xác nhận sinh viên mới đã nằm trong danh sách.

Ví dụ phản hồi khi đăng ký thành công:

```json
{
  "id": 2,
  "name": "Tran Thi Binh",
  "email": "binh@ptit.edu.vn",
  "class_name": "CNTT2"
}
```

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session02_Ex03
```

```
HNKS25CNTT1_FastAPI_Session02_Ex03
```

— Thuộc [[Session 02 — MOC]]
