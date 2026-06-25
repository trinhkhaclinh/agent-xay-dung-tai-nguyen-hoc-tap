---
type: "bai-tap"
title: "[Vận dụng cơ bản 1] Sai sót trong API lấy danh sách sinh viên"
session: 2
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex01"
tags:
  - "type/bai-tap"
  - "session/02"
deliverable_filename: "[Vận dụng cơ bản 1] Sai sót trong API lấy danh sách sinh viên"
status: "done"
---

# Sai sót trong API lấy danh sách sinh viên

## 1. Bối cảnh nghiệp vụ

Phòng Đào tạo của một trung tâm đang xây dựng hệ thống Quản lý sinh viên. Một lập trình viên mới được giao nhiệm vụ viết endpoint trả về danh sách toàn bộ sinh viên để màn hình Frontend hiển thị. Tuy nhiên khi đội Frontend gọi thử, dữ liệu nhận về không thể parse thành JSON và đường dẫn cũng không đúng quy ước RESTful mà cả nhóm đã thống nhất.

Bạn được phân công review (rà soát) đoạn code này, chỉ ra lỗi và bàn giao lại bản đã sửa chạy đúng trên Uvicorn.

## 2. Vấn đề hiện tại

- Endpoint được đặt tên là /getStudents — nhúng động từ get vào URL, vi phạm quy chuẩn đặt tên RESTful (danh từ số nhiều, không nhúng động từ).
- Hàm xử lý trả về một chuỗi (string) đã tự ghép tay thay vì trả về cấu trúc dữ liệu Python (list/dict). Vì vậy Frontend nhận về text thô, không phải JSON hợp lệ và không thể parse.
- Do trả về string nên Swagger UI tại /docs cũng hiển thị kiểu dữ liệu phản hồi sai, gây khó kiểm thử.

## 3. Mã nguồn hiện tại (Legacy Code)

```python
# main.py - phiên bản lỗi cần sửa
from fastapi import FastAPI

app = FastAPI()

# Endpoint lấy danh sách sinh viên (đang bị lỗi)
@app.get("/getStudents")
def get_students():
    students = [
        {"id": 1, "name": "Nguyen Van An"},
        {"id": 2, "name": "Tran Thi Binh"},
        {"id": 3, "name": "Le Van Cuong"}
    ]
    # Lỗi: tự ghép chuỗi thay vì trả về cấu trúc dữ liệu cho FastAPI tự chuyển thành JSON
    result = ""
    for s in students:
        result = result + str(s["id"]) + ": " + s["name"] + "; "
    return result
```

## 4. Yêu cầu

### Phần 1 — Phân tích lỗi (trace)

1. Truy vết: khi Client gọi GET /getStudents, hàm get_students trả về kiểu dữ liệu gì? Vì sao Frontend không parse được thành JSON?
2. Chỉ ra điểm sai trong cách đặt tên endpoint và giải thích quy chuẩn RESTful tương ứng (danh từ số nhiều, hành động do HTTP method quyết định).
3. Giải thích cơ chế: nếu hàm trả về list/dict thì FastAPI sẽ tự động làm gì với dữ liệu đó.

### Phần 2 — Sửa lỗi (triển khai)

- Đổi tên endpoint về đúng chuẩn RESTful: GET /students.
- Sửa hàm xử lý để trả về danh sách dict (list of dict) để FastAPI tự động serialize thành JSON.
- Chạy lại server bằng lệnh uvicorn main:app --reload và xác nhận log 200 OK.
- Mở Swagger UI tại http://127.0.0.1:8000/docs, dùng Try it out để kiểm thử endpoint và xác nhận phản hồi là JSON hợp lệ.

### Phần 3 — Kết quả mong đợi

Khi gọi GET /students, API trả về JSON dạng mảng các đối tượng sinh viên như bên dưới:

```json
[
  {"id": 1, "name": "Nguyen Van An"},
  {"id": 2, "name": "Tran Thi Binh"},
  {"id": 3, "name": "Le Van Cuong"}
]
```

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session02_Ex01
```

```
HNKS25CNTT1_FastAPI_Session02_Ex01
```

— Thuộc [[Session 02 — MOC]]
