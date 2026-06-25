---
type: "bai-tap"
title: "[Vận dụng cơ bản 2] Sai sót khi lấy thông tin sinh viên theo ID"
session: 2
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex02"
tags:
  - "type/bai-tap"
  - "session/02"
deliverable_filename: "[Vận dụng cơ bản 2] Sai sót khi lấy thông tin sinh viên theo ID"
status: "done"
---

# Sai sót khi lấy thông tin sinh viên theo ID

## 1. Bối cảnh nghiệp vụ

Tiếp nối hệ thống Quản lý sinh viên, đội phát triển cần một endpoint trả về thông tin chi tiết của một sinh viên dựa trên mã định danh (ID). Màn hình hồ sơ sinh viên sẽ gọi endpoint này mỗi khi người dùng bấm vào một dòng trong danh sách.

Một bạn trong nhóm đã viết endpoint nhưng khi truy cập http://127.0.0.1:8000/students/2 thì server báo lỗi 404 Not Found, còn ID trong phản hồi thì luôn sai. Bạn được nhờ tìm nguyên nhân và sửa lại cho đúng.

## 2. Vấn đề hiện tại

- Đường dẫn khai báo trong decorator là /student (số ít) và không có tham số đường dẫn (path parameter), nên Routing Engine của FastAPI không khớp được URL /students/2 → trả về 404.
- Hàm xử lý không nhận tham số id từ URL mà lại gán cứng một giá trị, khiến mọi lời gọi đều trả về cùng một sinh viên — ID phản hồi luôn sai so với ID yêu cầu.
- Endpoint chưa khai báo kiểu dữ liệu cho path parameter nên không tận dụng được khả năng validate tự động của FastAPI.

## 3. Mã nguồn hiện tại (Legacy Code)

```python
# main.py - phiên bản lỗi cần sửa
from fastapi import FastAPI

app = FastAPI()

STUDENTS = [
    {"id": 1, "name": "Nguyen Van An", "class": "CNTT1"},
    {"id": 2, "name": "Tran Thi Binh", "class": "CNTT2"},
    {"id": 3, "name": "Le Van Cuong", "class": "CNTT1"}
]

# Endpoint lấy 1 sinh viên theo ID (đang bị lỗi)
@app.get("/student")
def get_student():
    student_id = 1  # Lỗi: gán cứng ID, không lấy từ URL
    for s in STUDENTS:
        if s["id"] == student_id:
            return s
    return {"error": "not found"}
```

## 4. Yêu cầu

### Phần 1 — Phân tích lỗi (trace)

1. Truy vết vì sao gọi GET /students/2 lại trả về 404: so sánh URL được khai báo trong decorator với URL mà Client thực sự gọi.
2. Giải thích vì sao phản hồi luôn trả về sinh viên có id = 1 dù Client yêu cầu id khác.
3. Nêu khái niệm path parameter và cách FastAPI ánh xạ {student_id} trên URL vào tham số của hàm xử lý.

### Phần 2 — Sửa lỗi (triển khai)

- Đổi đường dẫn thành dạng tài nguyên có path parameter: GET /students/{student_id}.
- Khai báo tham số student_id: int trong hàm xử lý để FastAPI tự lấy giá trị từ URL và validate kiểu dữ liệu.
- Dùng student_id nhận được để tìm đúng sinh viên trong danh sách thay vì gán cứng.
- Chạy lại bằng uvicorn main:app --reload và kiểm thử GET /students/2 trên Swagger UI tại /docs.

### Phần 3 — Kết quả mong đợi

Khi gọi GET /students/2, API trả về đúng sinh viên có id = 2:

```json
{
  "id": 2,
  "name": "Tran Thi Binh",
  "class": "CNTT2"
}
```

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session02_Ex02
```

```
HNKS25CNTT1_FastAPI_Session02_Ex02
```

— Thuộc [[Session 02 — MOC]]
