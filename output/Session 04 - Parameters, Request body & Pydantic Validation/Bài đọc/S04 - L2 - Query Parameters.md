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

### Ví dụ cơ bản: API Chào hỏi (Greeting API)

Hãy xem ví dụ đơn giản nhất dưới đây:

```python
from fastapi import FastAPI

app = FastAPI()

# Tham số `name` không nằm trong đường dẫn "/greet"
@app.get("/greet")
def greet_user(name: str):
    return {"message": f"Xin chào {name}!"}
```

**Cách hoạt động:**
- Đường dẫn chỉ là `/greet`, không chứa `{name}`.
- Hàm `greet_user` có tham số đầu vào `name: str`.
- FastAPI nhận diện `name` là một Query Parameter.
- Khi người dùng truy cập URL: `http://127.0.0.1:8000/greet?name=Linh`
  - FastAPI tự động trích xuất giá trị `Linh` từ phần `?name=Linh` trên URL.
  - Truyền giá trị này vào biến `name` trong hàm và trả về: `{"message": "Xin chào Linh!"}`.

### Ví dụ thực tế: Lọc danh sách dữ liệu (Filter API)

Trong thực tế, Query Parameters thường dùng để lọc dữ liệu từ danh sách:

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

Trong FastAPI, việc một Query Parameter là **bắt buộc (Required)** hay **tùy chọn (Optional)** được xác định dựa trên việc bạn có **khai báo giá trị mặc định** cho tham số đó trong hàm xử lý hay không.

### 3.1. Tham số không có giá trị mặc định (Bắt buộc - Required)
Khi một tham số của hàm không được gán giá trị mặc định (ví dụ: `service_type: str`), FastAPI hiểu rằng đây là một tham số bắt buộc.

*   **Cơ chế:** Client **bắt buộc** phải truyền tham số này kèm theo giá trị của nó trên URL dưới dạng `?param=value`.
*   **Nếu thiếu:** FastAPI sẽ tự động chặn request lại ngay lập tức (không thực thi code bên trong hàm) và trả về mã lỗi **422 Unprocessable Entity** kèm thông tin chi tiết lỗi dưới dạng JSON.

**Ví dụ:**
```python
@app.get("/services")
def get_services(service_type: str):
    return {"type": service_type}
```
*   **Gọi đúng:** `/services?service_type=design` $\rightarrow$ Trả về `{"type": "design"}`
*   **Gọi sai (thiếu tham số):** `/services` $\rightarrow$ Trả về lỗi 422:
    ```json
    {
      "detail": [
        {
          "type": "missing",
          "loc": ["query", "service_type"],
          "msg": "Field required",
          "input": null
        }
      ]
    }
    ```

---

### 3.2. Tham số có giá trị mặc định (Tùy chọn - Optional)
Khi bạn gán một giá trị mặc định cho tham số (ví dụ: `limit: int = 10` hoặc `keyword: str | None = None`), FastAPI sẽ hiểu đây là tham số tùy chọn.

*   **Cơ chế:** Nếu client không truyền tham số này trên URL, FastAPI sẽ tự động lấy giá trị mặc định đã khai báo để truyền vào hàm.
*   **Có hai kiểu khai báo tham số tùy chọn phổ biến:**
    1.  **Gán giá trị mặc định cụ thể:** `limit: int = 10`. Nếu không truyền `limit`, hệ thống sẽ tự động dùng giá trị `10`.
    2.  **Gán giá trị mặc định là `None` (hoặc `str | None = None`):** Thường dùng khi tham số không bắt buộc và cũng không có giá trị mặc định cố định nào hợp lý. Khi nhận giá trị `None`, bạn có thể dùng điều kiện `if keyword:` hoặc `if keyword is not None:` để xử lý logic tương ứng.

**Ví dụ:**
```python
@app.get("/items")
def get_items(limit: int = 10, search: str | None = None):
    return {"limit": limit, "search": search}
```
*   **Gọi không truyền tham số:** `/items` $\rightarrow$ Trả về `{"limit": 10, "search": null}`
*   **Gọi truyền một phần:** `/items?limit=5` $\rightarrow$ Trả về `{"limit": 5, "search": null}`
*   **Gọi truyền đầy đủ:** `/items?limit=5&search=laptop` $\rightarrow$ Trả về `{"limit": 5, "search": "laptop"}`

---

### 3.3. Quy tắc thứ tự khai báo tham số trong Python
Theo quy định cú pháp của Python, các tham số **không có giá trị mặc định (bắt buộc)** phải được khai báo trước các tham số **có giá trị mặc định (tùy chọn)** trong khai báo hàm.

```python
# HỢP LỆ (Bắt buộc đứng trước, Tùy chọn đứng sau)
@app.get("/test")
def test_api(required_param: str, optional_param: int = 10):
    return {"required": required_param, "optional": optional_param}

# KHÔNG HỢP LỆ (Sẽ gây lỗi SyntaxError của Python ngay khi khởi động)
@app.get("/test")
def test_api(optional_param: int = 10, required_param: str):
    ...
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
