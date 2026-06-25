---
type: "bai-tap"
title: "[Sáng tạo] Xây dựng API Quản lý sản phẩm với validation động"
session: 4
level: "Sáng tạo"
bloom: "Sáng tạo"
ex_code: "Ex05"
tags:
  - "type/bai-tap"
  - "session/04"
deliverable_filename: "[Sáng tạo] Xây dựng API Quản lý sản phẩm với validation động"
status: "done"
---

# Xây dựng Hệ thống Validation động cho sản phẩm

## 1. Bối cảnh nghiệp vụ

Nhà trường muốn các học viên tự thiết kế một hệ thống kiểm chứng sản phẩm cho trang thương mại điện tử. Yêu cầu sản phẩm phải chứa mã vạch (phải bắt đầu bằng chữ 'PROD-' và theo sau bởi 5 chữ số), giá tiền phải lớn hơn 1000 VNĐ, và danh sách thẻ phân loại (tags) của sản phẩm không được rỗng.

## 2. Thử thách Sáng tạo

Hãy tự đề xuất cấu trúc Pydantic Model đầy đủ và viết API POST `/products` nhận sản phẩm đó. Đồng thời viết thêm một route GET `/products/search` sử dụng Query parameter với ràng buộc tùy chọn lọc theo khoảng giá từ `min_price` đến `max_price` (phải đảm bảo min_price <= max_price thông qua hàm tự viết validate).

## 3. Yêu cầu đầu ra

- Viết code đầy đủ chứa các model Pydantic nâng cao.
- Viết hàm kiểm chứng tùy biến (custom validator) sử dụng `@validator` hoặc `@model_validator` của Pydantic để đảm bảo logic min_price <= max_price.
- Hướng dẫn chi tiết cách chạy và kiểm tra lỗi 422 trên Swagger UI.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session04_Ex05
```

```
HNKS25CNTT1_FastAPI_Session04_Ex05
```

— Thuộc [[Session 04 — MOC]]
