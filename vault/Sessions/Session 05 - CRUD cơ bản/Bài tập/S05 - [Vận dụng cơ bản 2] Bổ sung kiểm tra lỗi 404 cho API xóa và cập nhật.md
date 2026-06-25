---
type: "bai-tap"
title: "[Vận dụng cơ bản 2] Bổ sung kiểm tra lỗi 404 cho API xóa và cập nhật"
session: 5
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex02"
tags:
  - "type/bai-tap"
  - "session/05"
deliverable_filename: "[Vận dụng cơ bản 2] Bổ sung kiểm tra lỗi 404 cho API xóa và cập nhật"
status: "done"
---

# Xử lý lỗi 404 Not Found khi xóa và sửa đổi tài nguyên

## 1. Bối cảnh nghiệp vụ

Trong ứng dụng quản lý, khi client gửi request yêu cầu cập nhật hoặc xóa một học viên theo ID, hệ thống phải kiểm tra xem học viên đó có tồn tại hay không. Nếu không, hệ thống cần phản hồi lỗi 404 Not Found thay vì chạy tiếp dẫn đến lỗi runtime hoặc trả về kết quả thành công giả.

## 2. Mã nguồn hiện tại (Legacy Code)

```python
from fastapi import FastAPI

app = FastAPI()
students_db = [{"id": 1, "name": "Nguyen Van An", "email": "an@gmail.com"}]

# Chưa kiểm tra ID tồn tại trước khi xóa
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    global students_db
    students_db = [s for s in students_db if s["id"] != student_id]
    return {"message": "Xóa thành công"}
```

## 3. Yêu cầu đầu ra

### Nhiệm vụ 1: Triển khai mã nguồn mới

- Sửa đổi API DELETE để kiểm tra xem `student_id` có tồn tại trong `students_db` hay không.
- Nếu không tồn tại, ném lỗi 404 Not Found.
- Nếu tồn tại, thực hiện xóa và trả về mã trạng thái HTTP 204 No Content.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session05_Ex02
```

```
HNKS25CNTT1_FastAPI_Session05_Ex02
```

— Thuộc [[Session 05 — MOC]]
