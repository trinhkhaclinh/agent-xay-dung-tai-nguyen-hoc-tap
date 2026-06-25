---
type: "bai-giang-outline"
title: "Giới thiệu và Cài đặt FastAPI"
session: 2
slide_count: 27
tags:
  - "type/bai-giang"
  - "session/02"
deliverable_filename: "Session 02 - Giới thiệu và Cài đặt FastAPI"
status: "done"
---

# Giới thiệu và Cài đặt FastAPI — Outline bài giảng

## Slide 1 — [title] Giới thiệu và Cài đặt FastAPI
- Session 02
- Module: Training Program Preparation
- Phiên bản: 1.0

## Slide 2 — [agenda] Nội dung
*Phần: NỘI DUNG*
- 1. Tổng quan kiến trúc web và FastAPI
- 2. Thiết lập môi trường và Virtual Environment
- 3. Khởi tạo ứng dụng FastAPI
- 4. API endpoint và routing
- 5. Tài liệu API với OpenAPI và Swagger UI

## Slide 3 — [section-title] 1. Tổng quan kiến trúc web và FastAPI - 1
*Phần: 1. Tổng quan kiến trúc web và FastAPI*
- Mô hình Client-Server và vòng đời Request-Response
- SSR vs API-first, kiến trúc Decoupled
- FastAPI, WSGI vs ASGI, Uvicorn
**Speaker notes:** Khớp Kịch bản video Lesson 01 phần Mở đầu: đặt vấn đề vì sao cần hiểu kiến trúc web trước khi viết API; nêu 3 trọng tâm của Lesson.

## Slide 4 — [bullets] 1. Mô hình Client-Server & vòng đời Request-Response - 2
*Phần: 1. Tổng quan kiến trúc web và FastAPI*
- Client gửi Request → Server xử lý → trả Response
- HTTP/HTTPS là nền tảng mọi ứng dụng web hiện đại
- JSON: định dạng trao đổi dữ liệu nhẹ giữa FE và BE
- Chuỗi bọc nháy kép; số/bool không cần nháy
**Sơ đồ:** Sơ đồ Client ↔ Internet (HTTP/HTTPS) ↔ Server, mũi tên Request đi và Response về
**Speaker notes:** Khớp Kịch bản video Lesson 01 phần Request-Response: mở DevTools tab Network minh hoạ một cuộc gọi HTTP và xem JSON trả về.

## Slide 5 — [comparison-table] 1. Web truyền thống (SSR) vs Web Service/API - 3
*Phần: 1. Tổng quan kiến trúc web và FastAPI*
- SSR: server dựng và trả toàn bộ HTML cho trình duyệt
- Decoupled/API-first: server chỉ trả dữ liệu thuần JSON
- Một API phục vụ được Web, Mobile và bên thứ ba
**Sơ đồ:** Bảng 2 cột so sánh: Web truyền thống (SSR) | Web Service (Decoupled/API)
**Speaker notes:** Khớp Kịch bản video Lesson 01 phần So sánh SSR và API: đối chiếu trải nghiệm tải trang website tin tức SSR với SPA tiêu thụ API.

## Slide 6 — [comparison-table] 1. WSGI vs ASGI và vai trò Uvicorn - 4
*Phần: 1. Tổng quan kiến trúc web và FastAPI*
- WSGI (Django/Flask): đồng bộ, mỗi request một thread
- ASGI: bất đồng bộ (async/await), chịu tải cao hơn
- Uvicorn là ASGI server siêu nhanh cho FastAPI
- Hiệu năng FastAPI tiệm cận NodeJS/Go
**Sơ đồ:** Bảng 2 cột so sánh WSGI (đồng bộ) | ASGI (bất đồng bộ)
**Speaker notes:** Khớp Kịch bản video Lesson 01 phần Hiệu năng: giải thích vì sao async giúp FastAPI chịu tải cao, dẫn vào vai trò của Uvicorn.

## Slide 7 — [3-card] 1. FastAPI = Starlette + Pydantic - 5
*Phần: 1. Tổng quan kiến trúc web và FastAPI*
- Starlette: web toolkit (routing, middleware)
- Pydantic: data validation bằng type hints
- Sơ đồ luồng: Client → API (FastAPI) → Database
**Sơ đồ:** 3 card: Starlette | Pydantic | Sơ đồ Client → API → Database
**Speaker notes:** Khớp Kịch bản video Lesson 01 phần Kết: chốt FastAPI đứng trên Starlette + Pydantic; yêu cầu học viên vẽ được sơ đồ Client → API → Database (sản phẩm đầu ra).

## Slide 8 — [section-title] 2. Thiết lập môi trường và Virtual Environment - 1
*Phần: 2. Thiết lập môi trường và Virtual Environment*
- Vì sao cần môi trường ảo
- Tạo và kích hoạt venv đa nền tảng
- Quản lý thư viện với pip và requirements.txt
**Speaker notes:** Khớp Kịch bản video Lesson 02 phần Mở đầu: nêu tình huống hai dự án cần hai phiên bản thư viện khác nhau, dẫn vào nhu cầu cô lập môi trường.

## Slide 9 — [bullets] 2. Vấn đề xung đột phiên bản - 2
*Phần: 2. Thiết lập môi trường và Virtual Environment*
- Cài thư viện vào Python hệ thống → dễ xung đột
- Project A cần Lib X v1.0, Project B cần v2.0
- Giải pháp: cô lập mỗi dự án bằng môi trường ảo
**Sơ đồ:** Sơ đồ hai dự án dùng chung Python hệ thống bị xung đột vs mỗi dự án có venv riêng
**Speaker notes:** Khớp Kịch bản video Lesson 02 phần Vấn đề: minh hoạ xung đột phiên bản qua tình huống Project A/B, nhấn mạnh đây là lý do tồn tại của venv.

## Slide 10 — [3-card] 2. Vòng đời môi trường ảo (venv) - 3
*Phần: 2. Thiết lập môi trường và Virtual Environment*
- Tạo: python -m venv venv (có trình thông dịch + pip riêng)
- Kích hoạt: Windows .\venv\Scripts\activate; macOS/Linux source venv/bin/activate
- Hủy kích hoạt: deactivate; dấu hiệu là tiền tố (venv)
**Sơ đồ:** 3 card quy trình: Tạo → Kích hoạt → Hủy kích hoạt môi trường ảo
**Speaker notes:** Khớp Kịch bản video Lesson 02 phần Thực hành venv: demo tạo, kích hoạt trên Windows và nhận biết tiền tố (venv) trên terminal.

## Slide 11 — [code] 2. Đóng gói và tái tạo môi trường - 4
*Phần: 2. Thiết lập môi trường và Virtual Environment*
- python -m venv venv
- .\venv\Scripts\activate
- pip install fastapi uvicorn
- pip freeze > requirements.txt
**Sơ đồ:** Khối code bash 4 dòng kèm chú thích từng bước
**Speaker notes:** Khớp Kịch bản video Lesson 02 phần Đóng gói: giải thích pip freeze > requirements.txt để khoá phiên bản và pip install -r requirements.txt để đồng đội tái tạo; nhắc thêm venv/ vào .gitignore. Sản phẩm đầu ra: môi trường Python + FastAPI hoạt động.

## Slide 12 — [section-title] 3. Khởi tạo ứng dụng FastAPI - 1
*Phần: 3. Khởi tạo ứng dụng FastAPI*
- Viết ứng dụng FastAPI tối thiểu trong main.py
- Chạy server bằng Uvicorn
- Cơ chế Hot Reload với --reload
**Speaker notes:** Khớp Kịch bản video Lesson 03 phần Mở đầu: dẫn dắt từ môi trường đã sẵn sàng sang viết và chạy ứng dụng FastAPI đầu tiên.

## Slide 13 — [3-card] 3. Quy trình 3 bước thiết lập code - 2
*Phần: 3. Khởi tạo ứng dụng FastAPI*
- Bước 1: nạp lớp FastAPI
- Bước 2: tạo thực thể app = FastAPI()
- Bước 3: định nghĩa route và hàm xử lý (@app.get)
**Sơ đồ:** 3 card đánh số: Nạp lớp → Tạo app → Định nghĩa route
**Speaker notes:** Khớp Kịch bản video Lesson 03 phần Worked example: trình bày quy trình 3 bước rõ ràng để giảm tải nhận thức trước khi xem code.

## Slide 14 — [code] 3. Ứng dụng FastAPI tối thiểu (main.py) - 3
*Phần: 3. Khởi tạo ứng dụng FastAPI*
- from fastapi import FastAPI
- app = FastAPI()
- @app.get("/")
- def read_root(): return {"message": "Chào mừng đến FastAPI!"}
- Hàm trả Dictionary → FastAPI tự chuyển thành JSON
**Sơ đồ:** Khối code Python main.py kèm chú thích 3 bước
**Speaker notes:** Khớp Kịch bản video Lesson 03 phần Code mẫu: gõ từng dòng main.py, nhấn mạnh hàm xử lý trả Dictionary được tự động chuyển thành JSON.

## Slide 15 — [code] 3. Chạy server bằng Uvicorn & Hot Reload - 4
*Phần: 3. Khởi tạo ứng dụng FastAPI*
- uvicorn main:app --reload
- main = tên file, app = biến instance, --reload = tự restart
- FastAPI không tự lắng nghe cổng → cần Uvicorn
- Mặc định http://127.0.0.1:8000; log 200 OK xác nhận chạy
**Sơ đồ:** Sơ đồ trình duyệt gọi 127.0.0.1:8000 → Uvicorn → app FastAPI
**Speaker notes:** Khớp Kịch bản video Lesson 03 phần Chạy server: phân tích lệnh uvicorn main:app --reload, mở localhost:8000, sửa code để minh hoạ Hot Reload. Sản phẩm đầu ra: project FastAPI đầu tiên chạy bằng Uvicorn.

## Slide 16 — [code] 3. Ví dụ domain: cổng điều phối Logistics (gateway.py) - 5
*Phần: 3. Khởi tạo ứng dụng FastAPI*
- @app.get("/") trả JSON tình trạng vận hành kho
- gateway_status, workload_ratio, active_nodes, system_message
- Bật --reload để cập nhật tức thì khi sửa code
**Sơ đồ:** Khối code Python gateway.py trả về JSON trạng thái nhiều trường
**Speaker notes:** Khớp Kịch bản video Lesson 03 phần Vận dụng domain: áp ngay kiến thức vào API giám sát cổng điều phối Logistics (domain xuyên suốt của môn học).

## Slide 17 — [section-title] 4. API endpoint và routing - 1
*Phần: 4. API endpoint và routing*
- Cấu trúc HTTP Request/Response
- Các HTTP method cốt lõi và ánh xạ CRUD
- Quy chuẩn đặt tên endpoint RESTful & Routing Engine
**Speaker notes:** Khớp Kịch bản video Lesson 04 phần Mở đầu: chuyển từ một endpoint đơn lẻ sang thiết kế hệ endpoint chuẩn RESTful.

## Slide 18 — [comparison-table] 4. Cấu trúc HTTP Request và Response - 2
*Phần: 4. API endpoint và routing*
- Request: Method, URL, Headers, Body
- Response: Status Code, Headers, Body
- Mỗi hội thoại HTTP gồm một Request và một Response
- HTTP là nền tảng của mọi RESTful API
**Sơ đồ:** Bảng 2 cột: thành phần HTTP Request | thành phần HTTP Response
**Speaker notes:** Khớp Kịch bản video Lesson 04 phần HTTP: bóc tách các thành phần Request/Response bằng DevTools hoặc Postman.

## Slide 19 — [table] 4. Ánh xạ CRUD ↔ HTTP Method - 3
*Phần: 4. API endpoint và routing*
- GET = Read (đọc)
- POST = Create (tạo)
- PUT = Update toàn bộ
- PATCH = Update một phần
- DELETE = Delete (xoá)
**Sơ đồ:** Bảng 2 cột: HTTP Method | Hành động CRUD tương ứng
**Speaker notes:** Khớp Kịch bản video Lesson 04 phần CRUD: nhấn mạnh hành động được xác định bởi HTTP Method chứ không phải bởi URL.

## Slide 20 — [bullets] 4. Quy chuẩn đặt tên RESTful & Routing Engine - 4
*Phần: 4. API endpoint và routing*
- Đặt tên bằng danh từ số nhiều: /students, /courses
- Không nhúng động từ (sai: /getStudents, /createCourse)
- Endpoint định danh tài nguyên, không mô tả hành động
- Routing Engine dò URL path + HTTP method → đúng hàm xử lý
**Sơ đồ:** Sơ đồ Routing Engine: (URL path + Method) → ánh xạ tới hàm Python
**Speaker notes:** Khớp Kịch bản video Lesson 04 phần RESTful naming: đối chiếu cách đặt tên đúng/sai, giải thích cơ chế Routing Engine của FastAPI.

## Slide 21 — [code] 4. Endpoint /hello và hệ endpoint tài nguyên - 5
*Phần: 4. API endpoint và routing*
- @app.get("/hello") def say_hello()
- @app.get("/students") liệt kê sinh viên
- @app.post("/students") tạo sinh viên mới
- Cùng URL /students, hành động khác nhau theo Method
**Sơ đồ:** Khối code Python: decorator @app.get và @app.post trên cùng path /students
**Speaker notes:** Khớp Kịch bản video Lesson 04 phần Code mẫu: triển khai /hello rồi mở rộng sang /students với GET và POST. Sản phẩm đầu ra: endpoint /hello hoạt động.

## Slide 22 — [section-title] 5. Tài liệu API với OpenAPI và Swagger UI - 1
*Phần: 5. Tài liệu API với OpenAPI và Swagger UI*
- Chuẩn OpenAPI và Zero Configuration
- Swagger UI tại /docs để đọc và kiểm thử
- Phân biệt Swagger UI và ReDoc
**Speaker notes:** Khớp Kịch bản video Lesson 05 phần Mở đầu: nêu giá trị của tài liệu API tự động đối với cộng tác nhóm và bên thứ ba.

## Slide 23 — [bullets] 5. OpenAPI & Zero Configuration - 2
*Phần: 5. Tài liệu API với OpenAPI và Swagger UI*
- OpenAPI: tiêu chuẩn quốc tế mô tả REST API
- FastAPI tuân thủ hoàn toàn chuẩn OpenAPI
- Tự đọc cấu trúc hàm và kiểu dữ liệu để sinh tài liệu
- Không cần cấu hình thêm (Zero Configuration)
**Sơ đồ:** Sơ đồ: code + type hints → FastAPI tự sinh tài liệu OpenAPI
**Speaker notes:** Khớp Kịch bản video Lesson 05 phần OpenAPI: giải thích vì sao tài liệu tự sinh mà không cần viết thủ công nhờ type hints.

## Slide 24 — [comparison-table] 5. Swagger UI vs ReDoc - 3
*Phần: 5. Tài liệu API với OpenAPI và Swagger UI*
- Swagger UI tại /docs: tài liệu + kiểm thử tương tác
- Try it out / Execute: gọi API không cần Postman
- ReDoc tại /redoc: giao diện ba cột tối giản, tối ưu tra cứu
**Sơ đồ:** Bảng 2 cột so sánh Swagger UI (/docs) | ReDoc (/redoc)
**Speaker notes:** Khớp Kịch bản video Lesson 05 phần Demo: mở /docs dùng Try it out gọi thử endpoint, rồi mở /redoc để so sánh giao diện đọc tài liệu.

## Slide 25 — [code] 5. Tùy biến metadata & tags cho Swagger - 4
*Phần: 5. Tài liệu API với OpenAPI và Swagger UI*
- FastAPI(title=..., description=..., version=...)
- @app.get("/courses", tags=["courses"])
- Dùng tags metadata để phân nhóm endpoint gọn gàng
**Sơ đồ:** Khối code Python khai báo metadata FastAPI và tags trên endpoint
**Speaker notes:** Khớp Kịch bản video Lesson 05 phần Tùy biến: thêm title/description/version và tags để Swagger UI hiển thị đẹp, có phân nhóm. Sản phẩm đầu ra: Swagger hiển thị và test được API.

## Slide 26 — [summary] Tổng kết
*Phần: TỔNG KẾT*
- 1. Kiến trúc Client-Server, SSR vs API-first, FastAPI trên ASGI/Uvicorn
- 2. Cô lập dự án bằng venv, quản lý thư viện với pip và requirements.txt
- 3. Viết app FastAPI tối thiểu và chạy bằng uvicorn main:app --reload
- 4. Thiết kế endpoint RESTful, ánh xạ CRUD qua HTTP method
- 5. Khai thác tài liệu tự động OpenAPI qua Swagger UI (/docs) và ReDoc (/redoc)
**Speaker notes:** Khớp Kịch bản video phần Tổng kết Session: điểm lại 5 Lesson, nối tới sản phẩm đầu ra và chuẩn bị cho session tiếp theo.

## Slide 27 — [closing] KẾT THÚC
- HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN

## Khái niệm liên quan

- [[Mô hình Client-Server]]
- [[Request-Response & HTTP-HTTPS|Request/Response & HTTP/HTTPS]]
- [[Định dạng JSON]]
- [[Kiến trúc Decoupled (Frontend-Backend tách biệt)|Kiến trúc Decoupled (Frontend/Backend tách biệt)]]
- [[SSR vs SPA vs API-first]]
- [[FastAPI = Starlette + Pydantic]]
- [[WSGI vs ASGI]]
- [[Uvicorn (ASGI server)]]
- [[Xung đột phiên bản (version conflict)]]
- [[Virtual Environment (venv)]]
- [[Kích hoạt-Hủy kích hoạt môi trường|Kích hoạt/Hủy kích hoạt môi trường]]
- [[pip]]
- [[requirements.txt]]
- [[gitignore|.gitignore]]
- [[Đối tượng FastAPI app]]
- [[Decorator @app.get]]
- [[Hàm xử lý trả Dictionary → JSON]]
- [[Lệnh uvicorn main -app --reload|Lệnh uvicorn main:app --reload]]
- [[Hot Reload]]
- [[127.0.0.1 -8000|127.0.0.1:8000]]
- [[HTTP Request (Method-URL-Headers-Body)|HTTP Request (Method/URL/Headers/Body)]]
- [[HTTP Response (Status Code-Headers-Body)|HTTP Response (Status Code/Headers/Body)]]
- [[Ánh xạ CRUD ↔ HTTP Method]]
- [[Endpoint định danh tài nguyên]]
- [[RESTful naming]]
- [[Decorator routing (@app.get-post-put-delete)|Decorator routing (@app.get/post/put/delete)]]
- [[Routing Engine]]
- [[Chuẩn OpenAPI]]
- [[Zero Configuration]]
- [[Swagger UI (-docs)|Swagger UI (/docs)]]
- [[ReDoc (-redoc)|ReDoc (/redoc)]]
- [[Try it out - Execute|Try it out / Execute]]
- [[Tags metadata phân nhóm API]]

— Thuộc [[Session 02 — MOC]]
