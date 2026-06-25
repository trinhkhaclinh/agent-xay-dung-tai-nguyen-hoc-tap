---
type: "mindmap"
title: "Giới thiệu và Cài đặt FastAPI"
session: 2
tags:
  - "type/mindmap"
  - "session/02"
deliverable_filename: "Session 02 - Giới thiệu và Cài đặt FastAPI"
status: "done"
---

# Giới thiệu và Cài đặt FastAPI — Mindmap

- **Giới thiệu và Cài đặt FastAPI**
  - 1. Tổng quan kiến trúc web và FastAPI
    - Mô hình Client - Server
      - Client gửi Request
      - Server xử lý, trả Response
      - Client <-> Internet (HTTP/HTTPS) <-> Server
      - HTTP/HTTPS: nền tảng web hiện đại
    - Định dạng JSON
      - Định dạng trao đổi dữ liệu nhẹ
      - Key & chuỗi: nháy kép
      - Số/bool: không cần nháy
    - Kiến trúc Decoupled (FE/BE tách biệt)
      - Server chỉ trả dữ liệu thuần (JSON)
      - 1 API phục vụ Web + Mobile + bên thứ ba
      - SSR vs SPA vs API-first
    - FastAPI = Starlette + Pydantic
      - Starlette: routing, middleware
      - Pydantic: validation bằng type hints
    - WSGI vs ASGI
      - WSGI (Django/Flask): đồng bộ, 1 thread/request
      - ASGI (FastAPI): bất đồng bộ (async/await), tải cao
      - Uvicorn: ASGI server siêu nhanh
      - Hiệu năng tiệm cận NodeJS/Go
  - 2. Virtual environment
    - Vì sao cần venv
      - Cài vào Python hệ thống dễ xung đột phiên bản
      - Cô lập thư viện theo từng dự án
    - Tạo & kích hoạt
      - python -m venv venv
      - venv/ chứa interpreter & pip riêng
      - Windows: .\venv\Scripts\activate
      - macOS/Linux: source venv/bin/activate
      - Dấu hiệu: tiền tố (venv)
      - Hủy: deactivate
    - pip & requirements.txt
      - pip freeze > requirements.txt (đóng gói)
      - pip install -r requirements.txt (tái tạo)
      - Thêm venv/ vào .gitignore
  - 3. Khởi tạo ứng dụng FastAPI
    - Quy trình 3 bước
      - Nạp lớp FastAPI
      - Tạo thực thể app = FastAPI()
      - Định nghĩa route + hàm xử lý
    - Decorator & hàm xử lý
      - @app.get("/")
      - Trả Dictionary -> tự chuyển thành JSON
    - Chạy bằng Uvicorn
      - FastAPI không tự lắng nghe cổng mạng
      - uvicorn main:app --reload
      - main = tên file, app = biến instance
      - --reload: Hot Reload, tự restart khi sửa
    - Truy cập server
      - Mặc định http://127.0.0.1:8000
      - Log 200 OK xác nhận hoạt động
  - 4. API endpoint và Routing
    - Cấu trúc HTTP
      - Request: Method / URL / Headers / Body
      - Response: Status Code / Headers / Body
      - HTTP: nền tảng mọi RESTful API
    - HTTP Methods (CRUD)
      - GET = Read
      - POST = Create
      - PUT = Update toàn bộ
      - PATCH = Update một phần
      - DELETE = Delete
    - RESTful naming
      - Danh từ số nhiều (/students)
      - Không nhúng động từ (sai: /getStudents)
      - Hành động xác định bởi Method, không phải URL
    - Routing Engine
      - Decorator routing (@app.get/post/put/delete)
      - Dò URL path + HTTP method -> hàm xử lý
  - 5. Swagger UI
    - Chuẩn OpenAPI
      - Tiêu chuẩn quốc tế mô tả REST API
      - FastAPI tuân thủ hoàn toàn
    - Zero Configuration
      - Tự đọc hàm & kiểu dữ liệu sinh tài liệu
      - Không cần cấu hình thêm
    - Swagger UI (/docs)
      - http://localhost:8000/docs
      - Vừa tài liệu, vừa kiểm thử tương tác
      - Try it out / Execute
    - ReDoc (/redoc)
      - http://localhost:8000/redoc
      - Giao diện ba cột, tối ưu đọc/tra cứu
    - Tags metadata
      - Phân nhóm endpoint cho gọn gàng

— Thuộc [[Session 02 — MOC]]
