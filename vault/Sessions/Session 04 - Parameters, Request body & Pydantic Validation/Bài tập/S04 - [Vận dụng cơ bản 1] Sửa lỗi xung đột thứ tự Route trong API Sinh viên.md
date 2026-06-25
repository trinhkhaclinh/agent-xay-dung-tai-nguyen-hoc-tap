---
type: "bai-tap"
title: "[Vận dụng cơ bản 1] Sửa lỗi xung đột thứ tự Route trong API Sinh viên"
session: 4
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex01"
tags:
  - "type/bai-tap"
  - "session/04"
deliverable_filename: "[Vận dụng cơ bản 1] Sửa lỗi xung đột thứ tự Route trong API Sinh viên"
status: "done"
---

# Sửa lỗi xung đột thứ tự Route trong API Sinh viên

## 1. Bối cảnh nghiệp vụ

Một hệ thống quản lý học tập đang phát triển các endpoint để quản lý thông tin sinh viên. Nhà phát triển đã viết mã để hỗ trợ hai tính năng: một route lấy hồ sơ cá nhân của sinh viên hiện tại đăng nhập qua đường dẫn '/students/me' và một route lấy thông tin sinh viên bất kỳ qua ID học sinh '/students/{student_id}'.

## 2. Vấn đề hiện tại

Tuy nhiên, khi gọi API `/students/me`, hệ thống liên tục trả về lỗi mã trạng thái 422 Unprocessable Entity với thông điệp báo rằng 'me' không phải số nguyên hợp lệ. Sinh viên cần xác định nguyên nhân và sửa lại mã nguồn.

## 3. Mã nguồn hiện tại (Legacy Code)

```python
from fastapi import FastAPI

app = FastAPI()

# Lấy chi tiết sinh viên bất kỳ theo ID
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    return {"student_id": student_id, "name": "Nguyen Van An", "role": "student"}

# Lấy thông tin sinh viên hiện tại
@app.get("/students/me")
def get_my_profile():
    return {"student_id": 999, "name": "Sinh viên hiện tại (Tôi)", "role": "admin"}
```

## 4. Yêu cầu đầu ra

### Nhiệm vụ 1: Phân tích nguyên nhân lỗi

- Hãy giải thích chi tiết cơ chế phân giải đường dẫn của FastAPI và tại sao lỗi này xảy ra khi gọi GET `/students/me`.
- Chỉ ra dòng code gây ra xung đột.

### Nhiệm vụ 2: Sửa lỗi mã nguồn

- Sắp xếp lại các route để sửa dứt điểm lỗi xung đột.
- Viết code hoàn thiện và chạy thử nghiệm trên Uvicorn.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session04_Ex01
```

```
HNKS25CNTT1_FastAPI_Session04_Ex01
```

— Thuộc [[Session 04 — MOC]]
