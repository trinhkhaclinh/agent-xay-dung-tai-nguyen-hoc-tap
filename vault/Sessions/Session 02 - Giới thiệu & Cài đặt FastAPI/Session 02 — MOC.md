---
type: "session-moc"
title: "Session 02 — MOC"
session: 2
hinh_thuc_hoc: "Lý thuyết"
lessons: 5
tags:
  - "type/moc"
  - "session/02"
status: "done"
---

# Session 02 — Giới thiệu & Cài đặt FastAPI cơ bản

> Thuộc [[IT-215 FastAPI — MOC]]

Session nền tảng: hiểu kiến trúc web Client-Server và vị thế của FastAPI, thiết lập môi trường ảo, khởi tạo ứng dụng FastAPI chạy bằng Uvicorn, thiết kế API endpoint theo chuẩn RESTful, và khai thác tài liệu API tự động với Swagger UI/OpenAPI.

## Mục tiêu học tập
- **Lesson 1 — Tổng quan kiến trúc web và FastAPI**
    - Giải thích (Hiểu) mô hình Client-Server và vòng đời Request-Response qua giao thức HTTP/HTTPS
    - Phân biệt (Phân tích) Web truyền thống (SSR) với Web Service/API (Decoupled) và kiến trúc API-first
    - Giải thích (Hiểu) vì sao FastAPI đạt hiệu năng cao nhờ chuẩn ASGI + Uvicorn so với WSGI
    - Vẽ (Vận dụng) được sơ đồ Client → API → Database
- **Lesson 2 — Thiết lập môi trường và Virtual Environment**
    - Giải thích (Hiểu) vì sao cần môi trường ảo để tránh xung đột phiên bản thư viện giữa các dự án
    - Tạo và kích hoạt (Vận dụng) môi trường ảo venv trên Windows/macOS/Linux
    - Quản lý (Vận dụng) thư viện bằng pip và requirements.txt để tái tạo môi trường đồng bộ
- **Lesson 3 — Khởi tạo ứng dụng FastAPI**
    - Triển khai (Vận dụng) ứng dụng FastAPI tối thiểu trong file main.py
    - Chạy (Vận dụng) server bằng Uvicorn và truy cập localhost:8000
    - Giải thích (Hiểu) cơ chế Hot Reload với cờ --reload trong phát triển
- **Lesson 4 — API endpoint và routing**
    - Giải thích (Hiểu) cấu trúc HTTP Request/Response và các phương thức HTTP cốt lõi (GET/POST/PUT/PATCH/DELETE)
    - Áp dụng (Vận dụng) quy chuẩn đặt tên endpoint RESTful (danh từ số nhiều, không nhúng động từ)
    - Triển khai (Vận dụng) endpoint /hello với decorator và hiểu cơ chế Routing Engine của FastAPI
- **Lesson 5 — Tài liệu API với OpenAPI và Swagger UI**
    - Giải thích (Hiểu) chuẩn OpenAPI và cách FastAPI tự sinh tài liệu (Zero Configuration)
    - Sử dụng (Vận dụng) Swagger UI tại /docs để đọc tài liệu và kiểm thử API tương tác
    - Phân biệt (Hiểu) Swagger UI và ReDoc

## Tài nguyên
### Bài đọc
- [[S02 - L1 - Tổng quan kiến trúc web và FastAPI]]
- [[S02 - L2 - Thiết lập môi trường và Virtual Environment]]
- [[S02 - L3 - Khởi tạo ứng dụng FastAPI]]
- [[S02 - L4 - API endpoint và routing]]
- [[S02 - L5 - Tài liệu API với OpenAPI và Swagger UI]]
### Kịch bản video
- [[S02 - Lesson 01 - Tổng quan mô hình client server]]
- [[S02 - Lesson 02 - Kiến trúc và hiệu năng của FastAPI]]
- [[S02 - Lesson 03 - Thiết lập môi trường]]
- [[S02 - Lesson 04 - Ứng dụng FastAPI đầu tiên]]
- [[S02 - Lesson 05 - HTTP method]]
- [[S02 - Lesson 06 - Tài liệu API tự động]]
### Bài tập
- [[S02 - [Vận dụng cơ bản 1] Sai sót trong API lấy danh sách sinh viên]]
- [[S02 - [Vận dụng cơ bản 2] Sai sót khi lấy thông tin sinh viên theo ID]]
- [[S02 - [Vận dụng chuyên sâu] API đăng ký sinh viên]]
- [[S02 - [Phân tích] Phân tích API tìm kiếm khóa học với FastAPI]]
- [[S02 - [Sáng tạo] Thiết kế API cổng điều phối Logistics]]
- [[S02 - [BTTH] Xây dựng API quản lý sinh viên cơ bản]]
### Quiz
- [[S02 - Quiz Cuối giờ]]
- [[S02 - Quiz Đầu giờ]]
### Bài giảng (outline)
- [[S02 - Bài giảng (Outline)]]
### Mindmap
- [[S02 - Mindmap]]

## Khái niệm cốt lõi
[[Mô hình Client-Server]] · [[Request-Response & HTTP-HTTPS|Request/Response & HTTP/HTTPS]] · [[Định dạng JSON]] · [[Kiến trúc Decoupled (Frontend-Backend tách biệt)|Kiến trúc Decoupled (Frontend/Backend tách biệt)]] · [[SSR vs SPA vs API-first]] · [[FastAPI = Starlette + Pydantic]] · [[WSGI vs ASGI]] · [[Uvicorn (ASGI server)]] · [[Xung đột phiên bản (version conflict)]] · [[Virtual Environment (venv)]] · [[Kích hoạt-Hủy kích hoạt môi trường|Kích hoạt/Hủy kích hoạt môi trường]] · [[pip]] · [[requirements.txt]] · [[gitignore|.gitignore]] · [[Đối tượng FastAPI app]] · [[Decorator @app.get]] · [[Hàm xử lý trả Dictionary → JSON]] · [[Lệnh uvicorn main -app --reload|Lệnh uvicorn main:app --reload]] · [[Hot Reload]] · [[127.0.0.1 -8000|127.0.0.1:8000]] · [[HTTP Request (Method-URL-Headers-Body)|HTTP Request (Method/URL/Headers/Body)]] · [[HTTP Response (Status Code-Headers-Body)|HTTP Response (Status Code/Headers/Body)]] · [[Ánh xạ CRUD ↔ HTTP Method]] · [[Endpoint định danh tài nguyên]] · [[RESTful naming]] · [[Decorator routing (@app.get-post-put-delete)|Decorator routing (@app.get/post/put/delete)]] · [[Routing Engine]] · [[Chuẩn OpenAPI]] · [[Zero Configuration]] · [[Swagger UI (-docs)|Swagger UI (/docs)]] · [[ReDoc (-redoc)|ReDoc (/redoc)]] · [[Try it out - Execute|Try it out / Execute]] · [[Tags metadata phân nhóm API]]
