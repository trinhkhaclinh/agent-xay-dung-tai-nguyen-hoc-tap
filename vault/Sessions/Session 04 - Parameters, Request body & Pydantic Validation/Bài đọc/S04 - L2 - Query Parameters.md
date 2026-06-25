---
type: "bai-doc"
title: "Query Parameters"
session: 4
lesson: 2
tags:
  - "type/bai-doc"
  - "session/04"
concepts:
  - "[[Query Parameter]]"
  - "[[Tham số mặc định (optional)]]"
  - "[[Tham số bắt buộc (required)]]"
  - "[[Optional - None|Optional / None]]"
  - "[[Kết hợp Path + Query]]"
deliverable_filename: "BÀI ĐỌC_ QUERY PARAMETERS TRONG FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Query Parameters - Lọc, Tìm Kiếm Và Quản Lý Tham Số Tùy Chọn

Khi thiết kế API, không phải lúc nào chúng ta cũng chỉ lấy một tài nguyên cụ thể qua ID. Thông thường, client cần tìm kiếm, lọc danh sách, hoặc phân trang dữ liệu (ví dụ: lấy danh sách khóa học có từ khóa 'Python', thuộc cấp độ 'beginner'). Để thực hiện việc này mà không làm thay đổi cấu trúc URL chính, chúng ta sử dụng Query Parameters. Bài đọc này giúp chúng ta làm chủ cách nhận diện, khai báo các tham số bắt buộc và tùy chọn trong FastAPI.

## 1. Khái niệm Query Parameters và điểm khác biệt với Path Parameters

Query parameters (tham số truy vấn) là các cặp khóa - giá trị nằm ở sau dấu hỏi chấm `?` trên đường dẫn URL, và nối với nhau bằng dấu và `&`. Ví dụ: `/courses?keyword=python&level=beginner`.

Điểm khác biệt cốt lõi: Path parameter dùng để định vị một tài nguyên cụ thể, mang tính bắt buộc. Trong khi đó, Query parameter dùng để thay đổi cách hiển thị tài nguyên (lọc, sắp xếp, tìm kiếm, phân trang) và thường mang tính tùy chọn.

## 2. Khai báo Query Parameters trong FastAPI

Trong FastAPI, bất kỳ tham số nào của hàm xử lý route mà **KHÔNG** nằm trong khai báo đường dẫn của route decorator sẽ tự động được hiểu là một Query Parameter.

```python
from fastapi import FastAPI

app = FastAPI()

courses_db = [
    {"id": 1, "name": "Lập trình Python cơ bản", "level": "beginner", "price": 1200000},
    {"id": 2, "name": "Xây dựng Web API với FastAPI", "level": "intermediate", "price": 2000000},
    {"id": 3, "name": "Lập trình Python nâng cao", "level": "advanced", "price": 3000000},
]

# Tham số 'keyword' và 'level' không nằm trong đường dẫn '/courses'
@app.get("/courses")
def filter_courses(keyword: str = "", level: str | None = None):
    results = courses_db
    if keyword:
        results = [c for c in results if keyword.lower() in c["name"].lower()]
    if level:
        results = [c for c in results if c["level"] == level]
    return results
```

Khi client gọi URL `/courses?keyword=python&level=beginner`, FastAPI sẽ trích xuất `keyword='python'` và `level='beginner'` để truyền vào hàm `filter_courses`.

## 3. Tham số Bắt buộc (Required) vs Tùy chọn (Optional)

Trong FastAPI, tính chất bắt buộc hay tùy chọn của một query parameter được quyết định bởi việc tham số đó có **giá trị mặc định** hay không:

- **Tham số tùy chọn (Optional):** Có giá trị mặc định (ví dụ: `keyword: str = ""` hoặc `level: str | None = None`). Nếu client không truyền tham số này trên URL, hàm vẫn chạy và nhận giá trị mặc định.
- **Tham số bắt buộc (Required):** Không khai báo giá trị mặc định (ví dụ: `api_key: str`). Nếu client không truyền tham số này trên URL (ví dụ gọi trơn `/courses`), FastAPI sẽ lập tức chặn lại và trả về lỗi 422 kèm thông báo thiếu tham số bắt buộc.

```python
# Định nghĩa kết hợp tham số bắt buộc và tùy chọn
@app.get("/services")
def get_services(
    service_type: str,            # Bắt buộc (không có giá trị mặc định)
    limit: int = 10,              # Tùy chọn (mặc định là 10)
    keyword: str | None = None    # Tùy chọn (mặc định là None)
):
    return {"type": service_type, "limit": limit, "keyword": keyword}
```

## 4. Ép kiểu dữ liệu thông minh với kiểu Boolean

FastAPI hỗ trợ ép kiểu dữ liệu thông minh cho các query parameter kiểu logic (`bool`). Khi khai báo một query parameter có kiểu `bool`, FastAPI nhận diện rất nhiều giá trị chuỗi khác nhau từ URL và tự động chuyển về đúng giá trị logic của Python:

- Giá trị là `true`, `1`, `yes`, `on` hoặc `True` -> chuyển thành `True` trong Python.
- Giá trị là `false`, `0`, `no`, `off` hoặc `False` -> chuyển thành `False` trong Python.

```python
@app.get("/items")
def read_items(is_active: bool = True):
    # Truy cập /items?is_active=false -> is_active = False
    # Truy cập /items?is_active=1 -> is_active = True
    return {"is_active": is_active}
```

## Tổng Kết

- Query parameters là các tham số nằm sau dấu '?' trên URL dùng để lọc, tìm kiếm hoặc phân trang dữ liệu.
- Tham số không nằm trong route path thì tự động được xem là query parameter.
- Query parameter có giá trị mặc định là tùy chọn; không có giá trị mặc định là bắt buộc.
- FastAPI hỗ trợ ép kiểu tự động cho kiểu dữ liệu số, chuỗi, và đặc biệt là cơ chế phân giải kiểu bool linh hoạt từ URL.

## Tài Liệu Tham Khảo

- FastAPI Official Documentation - Query Parameters: https://fastapi.tiangolo.com/tutorial/query-params/

## Khái niệm liên quan

- [[Query Parameter]]
- [[Tham số mặc định (optional)]]
- [[Tham số bắt buộc (required)]]
- [[Optional - None|Optional / None]]
- [[Kết hợp Path + Query]]

— Thuộc [[Session 04 — MOC]]
