---
type: "bai-doc"
title: "API Read (Đọc dữ liệu)"
session: 5
lesson: 2
tags:
  - "type/bai-doc"
  - "session/05"
concepts:
  - "[[GET method]]"
  - "[[HTTP 200 OK]]"
  - "[[HTTP 404 Not Found]]"
  - "[[Lọc danh sách]]"
deliverable_filename: "BÀI ĐỌC_ API READ TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: API Read - Phương Thức GET, Tìm Kiếm Danh Sách Và Lỗi 404 Not Found

Thao tác thứ hai trong chu trình CRUD là Read (Đọc dữ liệu). Trong kiến trúc RESTful API, việc truy xuất thông tin danh sách hoặc lấy chi tiết dữ liệu luôn sử dụng phương thức HTTP GET. Bài đọc này hướng dẫn chi tiết cách viết Endpoint GET lấy danh sách có lọc theo từ khóa và lấy chi tiết tài nguyên kèm xử lý ngoại lệ 404 Not Found.

## 1. Phương thức GET và tính chất Safe / Idempotent

GET là phương thức 'an toàn' (safe) vì nó chỉ đọc dữ liệu và không làm thay đổi trạng thái của máy chủ. Nó cũng mang tính 'idempotent' (đồng nhất): việc gọi GET 1 lần hay 100 lần liên tiếp cùng một URL luôn trả về cùng một kết quả dữ liệu (nếu dữ liệu gốc chưa bị tác động bởi thao tác khác).

## 2. Triển khai API GET lấy danh sách và tìm kiếm

Thông thường, API lấy danh sách sẽ hỗ trợ thêm các Query Parameter để lọc kết quả theo từ khóa.

```python
@app.get("/students")
def list_students(keyword: str = ""):
    if keyword:
        return [s for s in students_db if keyword.lower() in s["name"].lower()]
    return students_db
```

## 3. Triển khai API GET lấy chi tiết và lỗi 404 Not Found

Khi client muốn xem chi tiết một sinh viên cụ thể thông qua ID (Path Parameter), chúng ta phải tìm kiếm trong danh sách. Nếu tìm thấy, trả về thông tin đối tượng kèm mã 200 OK. Nếu duyệt hết danh sách mà không tìm thấy sinh viên nào khớp ID, bắt buộc phải trả về lỗi HTTP 404 Not Found kèm thông điệp báo lỗi rõ ràng.

```python
@app.get("/students/{student_id}")
def read_student_detail(student_id: int):
    for s in students_db:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên yêu cầu")
```

## Tổng Kết

- HTTP GET dùng để đọc dữ liệu, có tính chất an toàn (safe) và đồng nhất (idempotent).
- API danh sách thường kết hợp query parameter để thực hiện lọc và tìm kiếm.
- Khi tìm kiếm theo ID không tồn tại, luôn trả về mã lỗi HTTP 404 Not Found để thông báo chính xác trạng thái.

## Tài Liệu Tham Khảo

- MDN Web Docs - GET: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET

## Khái niệm liên quan

- [[GET method]]
- [[HTTP 200 OK]]
- [[HTTP 404 Not Found]]
- [[Lọc danh sách]]

— Thuộc [[Session 05 — MOC]]
