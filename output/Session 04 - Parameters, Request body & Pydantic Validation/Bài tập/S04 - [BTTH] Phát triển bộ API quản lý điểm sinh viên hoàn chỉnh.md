---
type: "bai-tap"
title: "[BTTH] Phát triển bộ API quản lý điểm sinh viên hoàn chỉnh"
session: 4
level: "Tổng hợp"
bloom: "Tổng hợp"
ex_code: "Ex06"
tags:
  - "type/bai-tap"
  - "session/04"
deliverable_filename: "[BTTH] Phát triển bộ API quản lý điểm sinh viên hoàn chỉnh"
status: "done"
---

# Bài tập thực hành tổng hợp: Quản lý điểm thi

## 1. Bối cảnh nghiệp vụ

Học viên cần xây dựng một ứng dụng nhỏ quản lý điểm thi của lớp học. Ứng dụng cần hỗ trợ các chức năng: xem danh sách điểm thi (có lọc theo tên môn và lọc sinh viên đỗ/trượt), xem điểm của một sinh viên cụ thể theo ID, và nhập điểm thi mới cho sinh viên.

## 2. Yêu cầu kỹ thuật

- GET `/grades`: Lọc theo query `subject` (tùy chọn) và `passed` (bool, mặc định True để lấy danh sách đỗ - điểm >= 5).
- GET `/grades/{student_id}`: Path parameter student_id phải >= 1.
- POST `/grades`: Request body nhận JSON gồm `student_id` (int, >=1), `subject` (str, 2-50 ký tự), và `score` (float, từ 0.0 đến 10.0).

## 3. Yêu cầu đầu ra

- Viết file `main.py` hoàn chỉnh chạy được.
- Tạo dữ liệu giả lập (mock database) dưới dạng List các dict trong Python.
- Thực hiện demo đầy đủ 3 API trên Swagger UI.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session04_Ex06
```

```
HNKS25CNTT1_FastAPI_Session04_Ex06
```

— Thuộc [[Session 04 — MOC]]
