---
type: "bai-tap"
title: "[Sáng tạo] Thiết kế cơ chế Xóa mềm (Soft Delete) trong FastAPI"
session: 5
level: "Sáng tạo"
bloom: "Sáng tạo"
ex_code: "Ex05"
tags:
  - "type/bai-tap"
  - "session/05"
deliverable_filename: "[Sáng tạo] Thiết kế cơ chế Xóa mềm (Soft Delete) trong FastAPI"
status: "done"
---

# Xây dựng cơ chế ẩn dữ liệu (Soft Delete)

## 1. Bối cảnh nghiệp vụ

Để bảo toàn lịch sử hoạt động và tránh lỗi liên kết dữ liệu trong các dự án thực tế, người ta thường dùng Xóa mềm (Soft Delete) thay vì xóa vật lý khỏi bộ nhớ.

## 2. Thử thách Sáng tạo

Hãy tự thiết kế và cài đặt một hệ thống API quản lý sinh viên có hỗ trợ Xóa mềm. Mỗi sinh viên ban đầu có thuộc tính `is_deleted = False`.

## 3. Yêu cầu đầu ra

- Viết API DELETE `/students/{student_id}` thực hiện chuyển đổi `is_deleted = True` thay vì dùng pop().
- Chỉnh sửa API GET `/students` để mặc định chỉ trả về các học viên chưa bị xóa (is_deleted == False).
- Viết thêm một API đặc biệt dành cho Admin: GET `/students/trash` để hiển thị danh sách các học viên đã bị xóa mềm, hỗ trợ khôi phục dữ liệu.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session05_Ex05
```

```
HNKS25CNTT1_FastAPI_Session05_Ex05
```

— Thuộc [[Session 05 — MOC]]
