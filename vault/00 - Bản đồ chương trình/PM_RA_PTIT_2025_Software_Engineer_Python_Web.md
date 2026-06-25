---
type: "course-curriculum"
title: "PM_RA_PTIT_2025_Software_Engineer_Python_Web"
module: "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI"
tags:
  - "type/curriculum"
  - "module/IT-215"
status: "done"
---

# [MODULE IT-215] - Phát triển dịch vụ web với FastAPI

> Đặc tả chi tiết khung chương trình được trích xuất từ `PM_RA_PTIT_2025_Software_Engineer_Python_Web.xlsx`.
> Các session được gắn liên kết trực tiếp tới các Session MOC tương ứng trong hệ thống Obsidian Vault.

## [[Session 01 — MOC|Session 01 — Định hướng học tập, demo sản phẩm cuối môn]]
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Video sản phẩm cuối môn |  |  |

## [[Session 02 — MOC|Session 02 — Giới thiệu & Cài đặt FastAPI cơ bản]]
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Tổng quan kiến trúc web và FastAPI | Tổng quan kiến trúc web và FastAPI | Vẽ được sơ đồ Client → API → Database |
| Lesson 02: Thiết lập môi trường và Virtual Environment | Thiết lập môi trường và Virtual Environment | Môi trường Python + FastAPI hoạt động |
| Lesson 03: Khởi tạo ứng dụng FastAPI | Khởi tạo ứng dụng FastAPI đầu tiên, chạy server với Uvicorn | Project FastAPI đầu tiên chạy bằng Uvicorn |
| Lesson 04: API endpoint và routing | Cấu hình routing cho API endpoint | Endpoint /hello hoạt động |
| Lesson 05: Swagger UI | Cài đặt và cấu hình Swagger UI, giới thiệu ReDoc và OpenAPI specs | Swagger hiển thị và test được API |

## Session 03 — Thực hành viết API endpoint và Swagger UI
- **Hình thức học:** `Thực hành`
- *Không có danh sách bài học con.*

## [[Session 04 — MOC|Session 04 — Parameters, Request body & Pydantic Validation]]
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Path Parameters | Lấy dữ liệu từ URL | API /users/{id} |
| Lesson 02: Query Parameters | Nhận tham số tìm kiếm | API /products?name=laptop |
| Lesson 03: Request Body với Pydantic | Nhận dữ liệu JSON | API Create User |
| Lesson 04: Type Hints trong FastAPI | Validate dữ liệu | API tự động validate dữ liệu |

## [[Session 05 — MOC|Session 05 — CRUD cơ bản]]
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: API create | Tạo dữ liệu | API POST |
| Lesson 02: API read | Đọc dữ liệu | API GET |
| Lesson 03: API update | Cập nhật dữ liệu | API PUT |
| Lesson 04: API delete | Xóa dữ liệu | API DELETE |

## Session 06 — Thực hành CRUD
- **Hình thức học:** `Thực hành`
- *Không có danh sách bài học con.*

## Session 07 — API Response & Handling Errors
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Response Model | Chuẩn hóa phản hồi | API có response_model |
| Lesson 02: HTTP Status Codes | Quản lý và áp dụng các mã trạng thái HTTP chuẩn RESTful (200, 201, 400, 404, 500) | API trả về đúng status code |
| Lesson 03: Cơ chế bắt ngoại lệ | Sử dụng HTTPException để dừng luồng xử lý và trả về lỗi phù hợp | API xử lý lỗi 404 |
| Lesson 04: Custom Exception Handlers | Tùy biến thông báo lỗi trả về cho client ở mức toàn cục (Global Exception Handler) | Global Exception Handler |

## Session 08 — Thực hành Chuẩn hóa phản hồi & Xử lý lỗi
- **Hình thức học:** `Thực hành`
- *Không có danh sách bài học con.*

## Session 09 — Mini Project 1
- **Hình thức học:** `Mini Project`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Thiết kế Endpoint | Phân tích yêu cầu | Danh sách API Endpoint |
| CRUD | Xây dựng chức năng | Contact Management API |
| Kiểm thử | Test toàn bộ API | Bộ API hoạt động hoàn chỉnh |

## Session 10 — Kết nối Cơ sở dữ liệu với SQLAlchemy ORM
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Tổng quan ORM | Giới thiệu mô hình ORM và thư viện SQLAlchemy trong hệ sinh thái Python | Hiểu mapping Table ↔ Object |
| Lesson 02: Kết nối CSDL và Database Session | Cấu hình chuỗi kết nối (Connection String) kết nối tới MySQL | Kết nối thành công tới DB |
| Lesson 03: SQLAlchemy Models | Định nghĩa các bảng dữ liệu bằng cú pháp khai báo SQLAlchemy | Model User |
| Lesson 04: Hàm Service Select/Insert | Viết các hàm Service độc lập để truy vấn (Select) và thêm mới (Insert) bản ghi | Service thêm và lấy dữ liệu |

## Session 11 — Khởi tạo CSDL và các thao tác CRUD
- **Hình thức học:** `Thực hành`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Thực hành kết nối CSDL và API CRUD | Tích hợp hàm CRUD thêm mới và lấy danh sách bản ghi từ MySQL vào API Endpoint |  |

## Session 12 — Hàm CRUD nâng cao, Mapping Schema & Dependency Injection
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Hàm Service Update/Delete | Viết các hàm Service cập nhật (Update) và xóa (Delete) bản ghi khỏi CSDL | Service Update/Delete |
| Lesson 02: Mapping Models & Schemas | Kỹ thuật chuyển đổi qua lại giữa Pydantic Schemas và SQLAlchemy Models | Model + Schema hoàn chỉnh |
| Lesson 03: Khái niệm DI | Khái niệm Dependency Injection và lợi ích của việc tách biệt tài nguyên trong hệ thống | Dependency tái sử dụng |
| Lesson 04: Hệ thống Depends | Cách sử dụng cú pháp Depends của FastAPI để nhúng phụ thuộc vào endpoint | Endpoint sử dụng Depends |
| Lesson 05: Quản lý DB Session | Viết hàm Dependency tạo và tự động đóng Database Session sử dụng từ khóa yield | Session đóng mở tự động |

## Session 13 — Thực hành Tích hợp Database vào Endpoint API
- **Hình thức học:** `Thực hành`
- *Không có danh sách bài học con.*

## Session 14 — Project Structure
- **Hình thức học:** `Lý Thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Vai trò Project Structure | Vai trò Project Structure | Hiểu kiến trúc dự án |
| Lesson 02: routers | Quản lý endpoint |  |
| Lesson 03: schemas | Validation |  |
| Lesson 04: models | ORM Model |  |
| Lesson 05: services | Business Logic |  |
| Lesson 06: database | Database Connection |  |

## Session 15 — Thiết kế & Xây dựng RESTful API tổng hợp
- **Hình thức học:** `Hackathon`
- *Không có danh sách bài học con.*

## Session 16 — Quan hệ giữa các bảng (Relationships) trong CSDL
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Quan hệ giữa các bảng | Tổng quan | ERD đơn giản |
| Lesson 02: Quan hệ 1-N | Thiết lập mối quan hệ Một - Nhiều (One-to-Many) giữa các bảng trong SQLAlchemy | Quan hệ 1-N |
| Lesson 03: Quan hệ N-N | Thiết lập mối quan hệ Nhiều - Nhiều (Many-to-Many) qua bảng trung gian | Quan hệ N-N |
| Lesson 04: Cơ chế Loading dữ liệu | Tìm hiểu và cấu hình kỹ thuật tải dữ liệu liên quan (Lazy Loading vs Joined Loading) | Truy vấn tối ưu |
| Lesson 05: Thiết kế API cho dữ liệu quan hệ | Nested Response | API dữ liệu quan hệ |

## Session 17 — Thực hành
- **Hình thức học:** `Thực hành`
- *Không có danh sách bài học con.*

## Session 18 — Security - Authentication & JWT (JSON Web Tokens)
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Nguyên tắc bảo mật | Giới thiệu giao thức OAuth2, cơ chế Authentication trong ứng dụng web hiện đại | Hiểu luồng Login |
| Lesson 02: Cấu trúc JWT | Tìm hiểu thành phần của chuỗi JWT (Header, Payload, Signature) và cơ chế sinh token | JWT Token |
| Lesson 03: Mã hóa mật khẩu | Cơ chế băm mật khẩu một chiều (Password Hashing) sử dụng thư viện passlib và bcrypt | Password Hash Service |

## Session 19 — Thực hành Triển khai Đăng ký & Đăng nhập (Authentication)
- **Hình thức học:** `Thực hành`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Thực hành API Đăng ký | Viết API Register nhận thông tin user, thực hiện hash mật khẩu và lưu vào bảng Users | API Register |
| Lesson 02: Thực hành API Đăng nhập | Viết API Login/Token xác thực mật khẩu, tạo chuỗi Access Token JWT gửi về client | API Login + JWT |

## Session 20 — Mini Project 2
- **Hình thức học:** `Mini Project`
- *Không có danh sách bài học con.*

## Session 21 — Authorization, Middleware & CORS
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Authorization | Kỹ thuật giải mã (Decode) JWT và phân quyền người dùng từ Token | Current User Dependency |
| Lesson 02: Phân quyền theo vai trò | Thiết lập phân quyền Role-based Access Control (Admin, User) bảo vệ endpoint nhạy cảm | API phân quyền |
| Lesson 03: Middleware | Khái niệm Middleware | Middleware cơ bản |
| Lesson 04: CORS | Cách cấu hình CORS để cho phép Frontend kết nối | CORS Middleware |

## Session 22 — Thực hành Phân quyền bảo mật & Cấu hình CORS
- **Hình thức học:** `Thực hành`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Thực hành Security Dependency | Viết Security Dependency bắt buộc Client đính kèm JWT Token hợp lệ khi gọi API |  |
| Lesson 02: Thực hành Tích hợp CORS | Cấu hình và thử nghiệm chặn/cho phép các domain ngoại lai gửi request tới API |  |

## Session 23 — Form Data, Upload File, File Storage
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: Form Data | Nhận dữ liệu Form | API Form |
| Lesson 02: Upload File | Upload ảnh/tài liệu | API Upload |
| Lesson 03: File Storage | Lưu file server | Thư mục uploads |

## Session 24 — Upload Avatar, Upload Document
- **Hình thức học:** `Thực hành`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
|  |  | Avatar Upload API<br><br>Document Upload API<br><br>File Storage System |

## Session 25 — TESTING API
- **Hình thức học:** `Lý thuyết`

| Bài học (Lesson) | Nội dung chi tiết | Sản phẩm đầu ra |
| --- | --- | --- |
| Lesson 01: API Testing cơ bản | Kiểm thử API | Test Project |
| Lesson 02: Test GET | API Read | Test Case GET |
| Lesson 03: Test POST | API Create | Test Case POST |
| Lesson 04: Test JWT | Endpoint bảo mật | Test Authentication |

## 26-30 — 
- **Hình thức học:** `Làm dự án cuối môn`
- *Không có danh sách bài học con.*

