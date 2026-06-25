---
type: "bai-tap"
title: "[BTTH] Xây dựng API quản lý sinh viên cơ bản"
session: 2
level: "BTTH"
bloom: "BTTH"
ex_code: "Ex06"
tags:
  - "type/bai-tap"
  - "session/02"
deliverable_filename: "[BTTH] Xây dựng API quản lý sinh viên cơ bản"
status: "done"
---

# Xây dựng API quản lý sinh viên cơ bản

## 1. Bối cảnh nghiệp vụ

Đây là bài thực hành tổng hợp cuối Session 02. Bạn sẽ tự tay dựng một dự án FastAPI hoàn chỉnh từ đầu cho hệ thống Quản lý sinh viên: thiết lập môi trường ảo, khởi tạo ứng dụng, thiết kế hệ endpoint theo chuẩn RESTful và khai thác tài liệu tự sinh trên Swagger UI.

Mục tiêu là gộp tất cả kiến thức đã học trong session thành một sản phẩm chạy được, sẵn sàng cho các session sau (validate dữ liệu, kết nối database).

## 2. Quy tắc nghiệp vụ

- Tài nguyên quản lý là students; mỗi sinh viên gồm: id (tự sinh), name, email, class_name.
- Hệ thống cần hỗ trợ các thao tác CRUD cơ bản: liệt kê, xem chi tiết theo ID, tạo mới, cập nhật, xóa.
- Mỗi thao tác phải dùng đúng HTTP method theo ánh xạ CRUD: GET (đọc), POST (tạo), PUT (cập nhật), DELETE (xóa).
- Endpoint đặt tên theo chuẩn RESTful (danh từ số nhiều /students, path parameter /students/{student_id}, không nhúng động từ).
- Dữ liệu lưu tạm trong bộ nhớ (in-memory) cho phạm vi bài tập; trao đổi ở định dạng JSON.

## 3. Mã nguồn hiện tại (Legacy Code)

Khung dự án khởi điểm dưới đây mới có danh sách tạm và một endpoint liệt kê. Bạn phát triển tiếp thành API CRUD hoàn chỉnh.

```python
# main.py - khung khoi diem cho BTTH
from fastapi import FastAPI

app = FastAPI(
    title="Student Management API",
    description="API quan ly sinh vien co ban - Session 02",
    version="1.0.0"
)

students_db = [
    {"id": 1, "name": "Nguyen Van An", "email": "an@ptit.edu.vn", "class_name": "CNTT1"}
]

@app.get("/students", tags=["students"])
def list_students():
    return students_db

# TODO: bo sung cac endpoint con lai cua CRUD
```

## 4. Yêu cầu

### Phần 1 — Thiết lập môi trường

1. Tạo và kích hoạt môi trường ảo: python -m venv venv rồi .\venv\Scripts\activate (Windows).
2. Cài thư viện: pip install fastapi uvicorn.
3. Đóng gói môi trường: pip freeze > requirements.txt và thêm venv/ vào .gitignore.

### Phần 2 — Triển khai hệ endpoint CRUD

Hoàn thiện đầy đủ các endpoint sau cho tài nguyên students:

| Đường dẫn | HTTP method | Chức năng | CRUD |
| --- | --- | --- | --- |
| /students | GET | Lấy danh sách toàn bộ sinh viên | Read |
| /students/{student_id} | GET | Lấy chi tiết 1 sinh viên theo ID | Read |
| /students | POST | Đăng ký (tạo mới) sinh viên, id tự sinh | Create |
| /students/{student_id} | PUT | Cập nhật thông tin sinh viên theo ID | Update |
| /students/{student_id} | DELETE | Xóa sinh viên theo ID | Delete |

- Khai báo kiểu dữ liệu cho path parameter (student_id: int) để FastAPI tự validate.
- Endpoint tạo mới phải tự sinh id tăng dần và trả về hồ sơ vừa tạo.
- Các endpoint thao tác theo ID phải xử lý trường hợp không tìm thấy sinh viên (trả về thông báo lỗi rõ ràng).

### Phần 3 — Chạy & kiểm thử trên Swagger UI

1. Chạy server bằng uvicorn main:app --reload và truy cập http://127.0.0.1:8000.
2. Mở Swagger UI tại http://127.0.0.1:8000/docs, dùng Try it out để kiểm thử lần lượt cả 5 endpoint.
3. Thực hiện một kịch bản đầy đủ: tạo mới một sinh viên → liệt kê → xem chi tiết → cập nhật → xóa → liệt kê lại để xác nhận.
4. Đối chiếu giao diện tài liệu tại /docs (Swagger UI) và /redoc (ReDoc).

### Sản phẩm nộp

- Mã nguồn dự án (main.py) và file requirements.txt.
- Ảnh chụp màn hình Swagger UI thể hiện cả 5 endpoint chạy thành công.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session02_Ex06
```

```
HNKS25CNTT1_FastAPI_Session02_Ex06
```

— Thuộc [[Session 02 — MOC]]
