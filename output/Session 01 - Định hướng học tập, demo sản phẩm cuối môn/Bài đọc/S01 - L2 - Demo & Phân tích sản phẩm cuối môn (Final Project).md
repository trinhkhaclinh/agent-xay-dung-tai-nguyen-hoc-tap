---
type: "bai-doc"
title: "Demo & Phân tích sản phẩm cuối môn (Final Project)"
session: 1
lesson: 2
tags:
  - "type/bai-doc"
  - "session/01"
concepts:
  - "[[Sản phẩm cuối môn]]"
  - "[[Kiến trúc hệ thống]]"
  - "[[Đặc tả yêu cầu (SRS)]]"
  - "[[API Endpoint]]"
  - "[[Swagger UI]]"
deliverable_filename: "BÀI ĐỌC_ PHÂN TÍCH SẢN PHẨM CUỐI MÔN_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Demo & Phân Tích Kiến Trúc Sản Phẩm Cuối Môn

Đích đến của môn học IT-215 là xây dựng một hệ thống Web API chất lượng cao cho một dự án thực tế (ví dụ: Hệ thống quản lý trung tâm đào tạo hoặc Hệ thống bán hàng). Để hình dung rõ sản phẩm này, chúng ta cần phân tích kiến trúc hệ thống Client-Server-Database và tìm hiểu các tính năng nghiệp vụ bắt buộc phải có.

## 1. Tổng quan Kiến trúc Client-API-Database

Một ứng dụng web hiện đại thường tuân theo kiến trúc 3 tầng tách biệt giúp nâng cao khả năng mở rộng:

- **Client (Giao diện):** Nơi người dùng tương tác trực tiếp (giao diện Web React/Vue hoặc ứng dụng di động Mobile App).
- **API Server (Backend):** Máy chủ viết bằng FastAPI tiếp nhận request, kiểm tra nghiệp vụ, tương tác với database và trả dữ liệu JSON.
- **Database (Cơ sở dữ liệu):** MySQL lưu trữ các bảng thông tin một cách bền vững.

API đóng vai trò là chiếc cầu nối duy nhất truyền tải thông tin an toàn giữa giao diện người dùng và cơ sở dữ liệu.

## 2. Cấu trúc Thư mục Dự án FastAPI mẫu

Để dự án lớn không bị rối và dễ bảo trì, chúng ta tổ chức code theo cấu trúc phân lớp chức năng tiêu chuẩn:

```text
my_project/
├── app/                         # Thư mục chính chứa mã nguồn
│   ├── main.py                  # Điểm chạy khởi tạo ứng dụng
│   ├── database.py              # Cấu hình kết nối MySQL
│   ├── models.py                # Định nghĩa các bảng cơ sở dữ liệu (ORM)
│   ├── schemas.py               # Định nghĩa schema validate dữ liệu (Pydantic)
│   ├── services.py              # Xử lý logic nghiệp vụ chính
│   └── routers/                 # Quản lý định tuyến chia nhỏ API
│       ├── users.py             # Các API liên quan đến người dùng
│       └── courses.py           # Các API liên quan đến môn học
├── requirements.txt             # Danh sách thư viện cần cài đặt
└── README.md                    # Hướng dẫn chạy dự án
```

## 3. Các Tính năng Cốt lõi của Sản phẩm Cuối khóa

Dự án cuối khóa của học viên bắt buộc phải có tối thiểu các nhóm chức năng sau:

1. Quản lý CRUD: Cho phép tạo mới, hiển thị chi tiết, cập nhật và xóa tài nguyên.
2. Tìm kiếm & Phân trang: Lọc danh sách theo từ khóa, giới hạn số bản ghi trả về.
3. Xác thực & Phân quyền: Đăng ký, đăng nhập nhận token JWT; phân chia quyền Admin và User.
4. Tài liệu API Swagger UI: Mọi API phải được mô tả đầy đủ tham số và phản hồi lỗi chuẩn xác.

## Tổng Kết

- Sản phẩm cuối môn là một Web API hoàn chỉnh viết bằng FastAPI kết nối MySQL.
- Mô hình kiến trúc Client-API-Database giúp phân tách giao diện và xử lý dữ liệu độc lập.
- Cấu trúc dự án phân lớp rõ ràng (models, schemas, services, routers) là yêu cầu kỹ thuật bắt buộc.

## Tài Liệu Tham Khảo

- FastAPI Project Structure Best Practices: https://fastapi.tiangolo.com/tutorial/bigger-applications/

## Khái niệm liên quan

- [[Sản phẩm cuối môn]]
- [[Kiến trúc hệ thống]]
- [[Đặc tả yêu cầu (SRS)]]
- [[API Endpoint]]
- [[Swagger UI]]

— Thuộc [[Session 01 — MOC]]
