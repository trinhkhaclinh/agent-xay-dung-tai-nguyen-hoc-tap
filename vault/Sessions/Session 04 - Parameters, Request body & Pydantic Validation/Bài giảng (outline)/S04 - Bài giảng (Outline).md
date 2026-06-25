---
type: "bai-giang-outline"
title: "Parameters, Request body & Pydantic Validation"
session: 4
slide_count: 18
tags:
  - "type/bai-giang"
  - "session/04"
deliverable_filename: "Session 04 - Parameters, Request body và Pydantic Validation"
status: "done"
---

# Parameters, Request body & Pydantic Validation — Outline bài giảng

## Slide 1 — [title] Parameters, Request body & Pydantic Validation
- Session 04
- [MODULE IT-215] - Phát triển dịch vụ web với FastAPI
- Phiên bản: 1.0

## Slide 2 — [agenda] Nội dung bài học
*Phần: NỘI DUNG*
- 1. Path Parameters: Định danh & Lấy dữ liệu từ URL
- 2. Query Parameters: Tìm kiếm & Lọc dữ liệu
- 3. Request Body với Pydantic: Đọc & Validate JSON
- 4. Type Hints: Ràng buộc dữ liệu nâng cao với Query, Path, Field

## Slide 3 — [section-title] Phần 1: Path Parameters - Lấy dữ liệu từ URL
*Phần: 1. Path Parameters*
- Định danh tài nguyên RESTful
- Cú pháp khai báo trong FastAPI
- Ép kiểu dữ liệu tự động

## Slide 4 — [bullets] Khái niệm Path Parameters
*Phần: 1. Path Parameters*
- Là phần thay đổi trực tiếp nằm trên URL nhằm xác định tài nguyên cụ thể.
- Ví dụ: Trong đường dẫn /students/123, '123' là mã số của sinh viên cần lấy.
- Sử dụng cho các trường hợp lấy chi tiết, cập nhật hoặc xóa một tài nguyên cụ thể.
**Sơ đồ:** Hình minh họa URL /students/{student_id} với mũi tên chỉ vào {student_id} chú thích 'Path Parameter'

## Slide 5 — [code] Khai báo Path Parameter trong code
*Phần: 1. Path Parameters*
- from fastapi import FastAPI
app = FastAPI()

@app.get("/students/{student_id}")
def read_student(student_id: int):
    return {"student_id": student_id}
**Speaker notes:** Giải thích cách bọc ngoặc nhọn ở route và khai báo kiểu int ở hàm.

## Slide 6 — [bullets] Quy tắc thứ tự khai báo Route
*Phần: 1. Path Parameters*
- FastAPI phân giải các route từ trên xuống dưới.
- Nếu route động đặt trước route tĩnh, route tĩnh sẽ bị nuốt chửng và lỗi validate 422.
- Giải pháp: Đặt route tĩnh (ví dụ /students/me) trước route động (ví dụ /students/{student_id}).
**Speaker notes:** Nhấn mạnh lỗi thường gặp của học viên khi làm API thông tin cá nhân.

## Slide 7 — [section-title] Phần 2: Query Parameters - Tìm kiếm và Lọc
*Phần: 2. Query Parameters*
- Khái niệm tham số truy vấn
- Khai báo tham số tùy chọn
- Ép kiểu logic Boolean

## Slide 8 — [bullets] Khái niệm Query Parameters
*Phần: 2. Query Parameters*
- Là các cặp key-value xuất hiện sau dấu '?' trên URL.
- Ví dụ: /courses?keyword=python&level=beginner.
- Dùng để lọc dữ liệu, phân trang hoặc tìm kiếm. Không trực tiếp làm thay đổi định danh đường dẫn chính.

## Slide 9 — [code] Khai báo Query Parameter
*Phần: 2. Query Parameters*
- @app.get("/courses")
def get_courses(keyword: str = "", level: str | None = None):
    # keyword và level là các query parameter tùy chọn vì có giá trị mặc định
    return {"keyword": keyword, "level": level}
**Speaker notes:** So sánh: tham số không khai báo ở route decorator chính là query parameter.

## Slide 10 — [section-title] Phần 3: Request Body - Đọc & Validate JSON
*Phần: 3. Request Body với Pydantic*
- Giới thiệu Request Body
- Kế thừa Pydantic BaseModel
- Cơ chế validate tự động

## Slide 11 — [bullets] Vì sao cần Request Body?
*Phần: 3. Request Body với Pydantic*
- Khi cần gửi dữ liệu lớn, có cấu trúc và cần bảo mật (như đăng ký sinh viên mới).
- Dữ liệu được gửi ẩn trong thân HTTP request dưới định dạng JSON.
- FastAPI kết hợp với Pydantic để tự động hóa việc đọc và kiểm tra cấu trúc dữ liệu này.

## Slide 12 — [code] Sử dụng Pydantic BaseModel
*Phần: 3. Request Body với Pydantic*
- from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/students")
def create(student: StudentCreate):
    return student
**Speaker notes:** Hướng dẫn cách viết BaseModel và tích hợp vào hàm POST.

## Slide 13 — [section-title] Phần 4: Ràng buộc dữ liệu nâng cao
*Phần: 4. Type Hints*
- Sử dụng Query() và Path() của FastAPI
- Sử dụng Field() của Pydantic
- Phân tích cấu trúc lỗi 422

## Slide 14 — [code] Validate với Query() và Path()
*Phần: 4. Type Hints*
- from fastapi import Query, Path

@app.get("/items/{id}")
def read(
    id: int = Path(..., ge=1),
    keyword: str = Query(None, min_length=2)
):
    return {"id": id, "keyword": keyword}
**Speaker notes:** Giải thích ge=1 là lớn hơn hoặc bằng 1, và min_length=2 là độ dài chuỗi tối thiểu.

## Slide 15 — [code] Validate thuộc tính với Field()
*Phần: 4. Type Hints*
- from pydantic import Field, BaseModel

class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
**Speaker notes:** Giải thích cách dùng Field() trong BaseModel để kiểm soát chặt chẽ giá trị thuộc tính.

## Slide 16 — [bullets] Cơ chế báo lỗi HTTP 422
*Phần: 4. Type Hints*
- Khi dữ liệu gửi lên vi phạm bất kỳ ràng buộc nào, FastAPI lập tức chặn lại.
- Phản hồi mã trạng thái 422 Unprocessable Entity.
- JSON trả về chứa loc (vị trí xảy ra lỗi), msg (thông điệp chi tiết) và type (mã lỗi).
**Sơ đồ:** Sơ đồ JSON lỗi 422 chỉ ra ba thành phần loc, msg, type

## Slide 17 — [summary] Tổng kết bài học
*Phần: TỔNG KẾT*
- Path Parameter: Dùng ngoặc nhọn {}, định danh duy nhất tài nguyên.
- Query Parameter: Lọc & tìm kiếm, mặc định khi không khai báo ở route.
- Request Body: Đọc dữ liệu JSON phức tạp qua Pydantic BaseModel.
- Query(), Path(), Field(): Đặt ràng buộc dữ liệu trực quan trên Type Hints.
- Lỗi 422: Tự động trả về khi validate thất bại, chứa chi tiết vị trí lỗi.

## Slide 18 — [closing] KẾT THÚC
- HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN

## Khái niệm liên quan

- [[Path Parameter]]
- [[Ép kiểu theo type hint (int-str)|Ép kiểu theo type hint (int/str)]]
- [[Tự động validate 422]]
- [[Thứ tự khai báo route]]
- [[Enum cho giá trị định sẵn]]
- [[RESTful naming]]
- [[Query Parameter]]
- [[Tham số mặc định (optional)]]
- [[Tham số bắt buộc (required)]]
- [[Optional - None|Optional / None]]
- [[Kết hợp Path + Query]]
- [[Pydantic BaseModel]]
- [[Request Body]]
- [[Khai báo schema]]
- [[Tự động validate JSON]]
- [[response_model]]
- [[Định dạng JSON]]
- [[Type Hints]]
- [[Query() validation]]
- [[Path() validation]]
- [[Field() constraints]]
- [[422 Unprocessable Entity]]
- [[Swagger UI (-docs)|Swagger UI (/docs)]]

— Thuộc [[Session 04 — MOC]]
