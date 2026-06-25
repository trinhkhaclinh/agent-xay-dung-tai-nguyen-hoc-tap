---
type: "bai-tap"
title: "[Phân tích] Phân tích tính Idempotent của các phương thức HTTP"
session: 5
level: "Phân tích"
bloom: "Phân tích"
ex_code: "Ex04"
tags:
  - "type/bai-tap"
  - "session/05"
deliverable_filename: "[Phân tích] Phân tích tính Idempotent của các phương thức HTTP"
status: "done"
---

# Phân tích so sánh tính Idempotent của các HTTP Methods

## 1. Bối cảnh nghiệp vụ

Khi thiết kế hệ thống API chịu tải lớn và có khả năng xảy ra mất kết nối giữa chừng, tính chất Idempotent (đồng nhất kết quả khi gọi nhiều lần) của các phương thức HTTP đóng vai trò quyết định thiết kế an toàn hệ thống.

## 2. Yêu cầu phân tích

Sinh viên cần lập bảng phân tích so sánh tính chất an toàn (Safe) và tính chất đồng nhất (Idempotent) của 4 phương thức HTTP GET, POST, PUT, DELETE.

## 3. Yêu cầu đầu ra

### (1) Lập bảng so sánh

| Phương thức HTTP | Safe (An toàn) | Idempotent (Đồng nhất) | Mô tả hành vi khi gọi liên tiếp |
| --- | --- | --- | --- |
| GET |  |  |  |
| POST |  |  |  |
| PUT |  |  |  |
| DELETE |  |  |  |

### (2) Giải thích ứng dụng thực tế

- Giải thích vì sao DELETE được coi là idempotent mặc dù lần gọi thứ 2 có thể trả về lỗi 404 thay vì 204.
- Vì sao không được dùng GET để thực hiện hành động xóa hoặc thay đổi dữ liệu.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session05_Ex04
```

```
HNKS25CNTT1_FastAPI_Session05_Ex04
```

— Thuộc [[Session 05 — MOC]]
