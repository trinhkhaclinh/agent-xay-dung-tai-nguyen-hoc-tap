---
type: "bai-tap"
title: "[Phân tích] Phân tích API tìm kiếm khóa học với FastAPI"
session: 2
level: "Phân tích"
bloom: "Phân tích"
ex_code: "Ex04"
tags:
  - "type/bai-tap"
  - "session/02"
deliverable_filename: "[Phân tích] Phân tích API tìm kiếm khóa học với FastAPI"
status: "done"
---

# Phân tích API tìm kiếm khóa học với FastAPI

## 1. Bối cảnh nghiệp vụ

Hệ thống Quản lý khóa học của trung tâm cần một chức năng tìm kiếm: học viên muốn lọc các khóa học theo từ khóa tên khóa, theo lĩnh vực (category) và theo mức học phí tối đa. Đội kỹ thuật còn tranh luận chưa thống nhất nên thiết kế endpoint tìm kiếm theo kiểu nào cho đúng chuẩn RESTful và dễ mở rộng.

Nhiệm vụ của bạn là phân tích các phương án thiết kế endpoint, lập bảng so sánh theo tiêu chí, chọn ra phương án phù hợp nhất rồi triển khai.

## 2. Yêu cầu bài toán

- Tìm kiếm khóa học theo nhiều điều kiện kết hợp: keyword (từ khóa tên khóa), category (lĩnh vực), max_fee (học phí tối đa).
- Các điều kiện đều là tùy chọn (optional): có thể truyền một, nhiều hoặc không truyền điều kiện nào (khi không truyền thì trả về toàn bộ).
- Endpoint chỉ đọc dữ liệu, không làm thay đổi tài nguyên, nên phải dùng đúng HTTP method tương ứng.

## 3. Ràng buộc & Bẫy dữ liệu

- Bẫy động từ trong URL: cám dỗ đặt tên kiểu /searchCourses — vi phạm quy chuẩn RESTful (không nhúng động từ vào URL).
- Bẫy số lượng tham số: khi có nhiều bộ lọc tùy chọn, nhồi tất cả vào path parameter sẽ làm URL cứng nhắc và khó bỏ trống từng điều kiện.
- Bẫy HTTP method: tìm kiếm là thao tác đọc (Read) nên không nên dùng POST chỉ để truyền điều kiện qua request body, trừ khi có lý do đặc biệt.
- Bẫy kiểu dữ liệu: max_fee là số; nếu không khai báo kiểu, dữ liệu nhận từ URL sẽ là chuỗi và so sánh sai.

## 4. Yêu cầu

### Phần 1 — Phân tích (đề xuất ≥ 2 thiết kế)

Mô tả ít nhất ba cách thiết kế endpoint tìm kiếm khóa học và nêu rõ cách truyền điều kiện của mỗi cách:

- Phương án A — Path parameter: nhúng điều kiện vào đường dẫn, ví dụ GET /courses/category/python.
- Phương án B — Query parameter: truyền điều kiện qua chuỗi truy vấn trên cùng tài nguyên, ví dụ GET /courses?keyword=fastapi&category=web&max_fee=2000000.
- Phương án C — Request body với POST: gửi điều kiện tìm kiếm trong body, ví dụ POST /courses/search với body JSON chứa các bộ lọc.

### Phần 2 — So sánh & Lựa chọn

Hoàn thành bảng so sánh dưới đây (điền Cao/Trung bình/Thấp hoặc nhận xét ngắn cho từng ô), sau đó kết luận chọn phương án nào và biện luận vì sao.

| Tiêu chí | A. Path parameter | B. Query parameter | C. Request body (POST) |
| --- | --- | --- | --- |
| Tuân thủ chuẩn RESTful cho thao tác đọc |  |  |  |
| Hỗ trợ nhiều bộ lọc tùy chọn (optional) |  |  |  |
| Độ rõ ràng & dễ đọc của URL |  |  |  |
| Khả năng bookmark / chia sẻ link kết quả |  |  |  |
| Dễ mở rộng thêm điều kiện mới |  |  |  |
| Tự sinh tài liệu đẹp trên Swagger UI |  |  |  |

Kết luận: chọn phương án phù hợp nhất cho bài toán tìm kiếm nhiều điều kiện tùy chọn và giải thích lý do dựa trên bảng so sánh.

### Phần 3 — Triển khai

- Hiện thực hóa phương án đã chọn thành endpoint hoàn chỉnh trên FastAPI, dùng query parameter tùy chọn cho keyword, category và max_fee.
- Khai báo kiểu dữ liệu cho từng tham số (ví dụ max_fee: int | None = None) để FastAPI tự validate và hiển thị đúng trên Swagger UI.
- Lọc danh sách khóa học theo các điều kiện được truyền; nếu không truyền điều kiện nào thì trả về toàn bộ danh sách.
- Kiểm thử nhiều tổ hợp điều kiện trên /docs và xác nhận kết quả lọc đúng.

Dữ liệu mẫu gợi ý để triển khai và kiểm thử:

```python
courses_db = [
    {"id": 1, "name": "Web API with FastAPI", "category": "web", "fee": 1800000},
    {"id": 2, "name": "Python co ban", "category": "python", "fee": 1200000},
    {"id": 3, "name": "Data Science nhap mon", "category": "data", "fee": 2500000}
]
```

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session02_Ex04
```

```
HNKS25CNTT1_FastAPI_Session02_Ex04
```

— Thuộc [[Session 02 — MOC]]
