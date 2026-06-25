---
type: "bai-tap"
title: "[Vận dụng cơ bản 1] Thiết lập Git và thực hiện Commit đầu tiên"
session: 1
level: "Vận dụng cơ bản"
bloom: "Vận dụng"
ex_code: "Ex01"
tags:
  - "type/bai-tap"
  - "session/01"
deliverable_filename: "[Vận dụng cơ bản 1] Thiết lập Git và thực hiện Commit đầu tiên"
status: "done"
---

# Thiết lập Git quản lý mã nguồn dự án

## 1. Bối cảnh nghiệp vụ

Học viên chuẩn bị bắt đầu dự án môn học IT-215. Để nộp bài tập và quản lý các phiên bản code, việc cài đặt và làm quen với Git là yêu cầu bắt buộc ngay từ buổi học đầu tiên.

## 2. Yêu cầu bài toán

Hãy khởi tạo một kho lưu trữ Git cục bộ trong thư mục dự án mẫu, cấu hình thông tin cá nhân và tạo commit đầu tiên chứa file README.md.

## 3. Mã nguồn hiện tại (Legacy Code)

```bash
# Thực hiện chạy các lệnh trong terminal
# Bước 1: Khởi tạo git
git init

# Bước 2: Cấu hình thông tin cá nhân
git config --global user.name "Tên của bạn"
git config --global user.email "email@gmail.com"
```

## 4. Yêu cầu đầu ra

- Tạo file README.md mô tả dự án học tập cá nhân.
- Thêm file vào khu vực theo dõi (staging area) bằng lệnh `git add`.
- Tạo commit đầu tiên bằng `git commit -m 'Initial commit'`.
- Chụp màn hình log lịch sử commit (`git log`).

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session01_Ex01
```

```
HNKS25CNTT1_FastAPI_Session01_Ex01
```

— Thuộc [[Session 01 — MOC]]
