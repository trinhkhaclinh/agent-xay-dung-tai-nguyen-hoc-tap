---
type: "bai-tap"
title: "[Vận dụng cơ bản 1] Sửa lỗi trùng lặp dữ liệu và mã trạng thái trong API POST"
session: 5
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex01"
tags:
  - "type/bai-tap"
  - "session/05"
deliverable_filename: "[Vận dụng cơ bản 1] Sửa lỗi trùng lặp dữ liệu và mã trạng thái trong API POST"
status: "done"
---

# Kiểm soát trùng lặp và mã phản hồi chuẩn cho API POST

## 1. Bối cảnh nghiệp vụ

Một lập trình viên backend đã viết một API POST để thêm học viên mới vào danh sách. Tuy nhiên, API này đang gặp hai vấn đề nghiêm trọng: một là cho phép thêm các học viên trùng lặp email, hai là trả về mã trạng thái mặc định 200 OK thay vì mã chuẩn 201 Created.

## 2. Vấn đề hiện tại

Học viên cần xác định lỗi logic trong code, sửa lại để chặn trùng lặp email và cấu hình đúng mã phản hồi HTTP 201.

## 3. Mã nguồn hiện tại (Legacy Code)

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students_db = []

class StudentCreate(BaseModel):
    name: str
    email: str

# Đang sử dụng mã mặc định 200 và chưa kiểm tra email trùng
@app.post("/students")
def add_student(student: StudentCreate):
    new_student = {"id": len(students_db) + 1, "name": student.name, "email": student.email}
    students_db.append(new_student)
    return new_student
```

## 4. Yêu cầu đầu ra

### Nhiệm vụ 1: Phân tích lỗi

- Giải thích vì sao mã 201 Created phù hợp hơn mã 200 OK cho thao tác tạo mới dữ liệu.
- Chỉ ra rủi ro khi hệ thống để lọt email trùng lặp.

### Nhiệm vụ 2: Viết mã nguồn sửa đổi

- Chỉnh sửa route decorator để thiết lập `status_code=201`.
- Dùng vòng lặp kiểm tra trùng lặp email, nếu trùng ném ra lỗi `HTTPException` với mã lỗi `400 Bad Request`.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session05_Ex01
```

```
HNKS25CNTT1_FastAPI_Session05_Ex01
```

— Thuộc [[Session 05 — MOC]]
