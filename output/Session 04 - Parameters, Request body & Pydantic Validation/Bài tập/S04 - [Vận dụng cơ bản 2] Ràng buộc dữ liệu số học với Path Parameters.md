---
type: "bai-tap"
title: "[Vận dụng cơ bản 2] Ràng buộc dữ liệu số học với Path Parameters"
session: 4
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex02"
tags:
  - "type/bai-tap"
  - "session/04"
deliverable_filename: "[Vận dụng cơ bản 2] Ràng buộc dữ liệu số học với Path Parameters"
status: "done"
---

# Thiết lập ràng buộc số học cho Path Parameters

## 1. Bối cảnh nghiệp vụ

Hệ thống quản lý đào tạo yêu cầu mã ID của sinh viên phải luôn là số nguyên dương lớn hơn hoặc bằng 1 và không vượt quá 99999. Nếu client gửi yêu cầu với ID bằng 0 hoặc số âm, hệ thống cần phát hiện lỗi ngay từ tầng API validation để tránh truy vấn vô ích vào cơ sở dữ liệu.

## 2. Yêu cầu bài toán

Hãy chỉnh sửa API endpoint nhận ID sinh viên để áp dụng các ràng buộc số học nêu trên sử dụng Path() của FastAPI. Đảm bảo các ràng buộc được mô tả rõ ràng để tự động sinh Swagger document.

## 3. Mã nguồn hiện tại (Legacy Code)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/students/{student_id}")
def get_student_detail(student_id: int):
    # Hiện tại chưa có ràng buộc giá trị min/max cho student_id
    return {"student_id": student_id, "message": "Thành công"}
```

## 4. Yêu cầu đầu ra

### Nhiệm vụ 1: Triển khai mã nguồn mới

- Nhúng Path() của fastapi vào tham số student_id.
- Áp dụng ràng buộc lớn hơn hoặc bằng 1 (ge=1) và nhỏ hơn hoặc bằng 99999 (le=99999).
- Thêm mô tả 'ID định danh của sinh viên' vào tài liệu.

### Nhiệm vụ 2: Kiểm thử

- Demo cấu trúc lỗi JSON trả về khi gọi API với ID bằng 0.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session04_Ex02
```

```
HNKS25CNTT1_FastAPI_Session04_Ex02
```

— Thuộc [[Session 04 — MOC]]
