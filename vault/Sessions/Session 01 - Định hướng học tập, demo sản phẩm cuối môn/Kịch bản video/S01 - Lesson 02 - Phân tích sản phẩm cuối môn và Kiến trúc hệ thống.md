---
type: "kich-ban-video"
title: "Lesson 02 - Phân tích sản phẩm cuối môn và Kiến trúc hệ thống"
session: 1
lesson: 2
tags:
  - "type/kich-ban-video"
  - "session/01"
concepts:
  - "[[Sản phẩm cuối môn]]"
  - "[[Kiến trúc hệ thống]]"
  - "[[Đặc tả yêu cầu (SRS)]]"
  - "[[API Endpoint]]"
  - "[[Swagger UI]]"
deliverable_filename: "Lesson 02 - Phân tích sản phẩm cuối môn và Kiến trúc hệ thống"
status: "done"
---

## Giới thiệu sản phẩm cuối môn

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học này, thầy và các em sẽ cùng nhau phân tích chi tiết sản phẩm cuối khóa mà các em sẽ tự tay xây dựng.

Đích đến kỹ thuật của môn học là một hệ thống Web API hoàn chỉnh. Để hiểu rõ sản phẩm hoạt động thế nào, hãy cùng nhìn vào sơ đồ kiến trúc 3 tầng Client-API-Database trên màn hình.

**[Chuyển tiếp slide]**

## Phân tích kiến trúc 3 tầng và API

Trong kiến trúc này, phía giao diện người dùng gửi các HTTP Request chứa dữ liệu đến Backend FastAPI. Backend của chúng ta tiếp nhận, thực thi nghiệp vụ và tương tác với cơ sở dữ liệu MySQL thông qua SQLAlchemy ORM để truy xuất hoặc lưu trữ thông tin, sau đó trả dữ liệu JSON về cho Client.

**[mở tài liệu Swagger UI của sản phẩm mẫu]**

Như các em thấy trên màn hình là tài liệu Swagger UI của sản phẩm mẫu. Chúng ta có các API đăng ký, đăng nhập bảo mật, các API quản lý lớp học, sinh viên với đầy đủ chức năng tạo mới, hiển thị, cập nhật và xóa. Đây chính là cấu trúc giao diện mà các em sẽ hoàn thiện.

## Cấu trúc thư mục dự án tiêu chuẩn

Để dự án không bị rối, các em cần tuân thủ cấu trúc chia thư mục rõ ràng. Chúng ta chia nhỏ code thành models chứa cấu trúc bảng CSDL, schemas chứa lớp validate Pydantic, services xử lý nghiệp vụ và routers quản lý đường dẫn API.

## Tổng kết bài giảng

Tóm lại, trong bài học này các em đã hiểu rõ mục tiêu sản phẩm cuối khóa cũng như cấu trúc dự án mẫu cần hướng tới. Hãy chuẩn bị tinh thần học tập thật tốt. Cảm ơn các em và chúc các em học tập hiệu quả!

## Khái niệm liên quan

- [[Sản phẩm cuối môn]]
- [[Kiến trúc hệ thống]]
- [[Đặc tả yêu cầu (SRS)]]
- [[API Endpoint]]
- [[Swagger UI]]

— Thuộc [[Session 01 — MOC]]
