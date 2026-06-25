---
type: "bai-tap"
title: "[Sáng tạo] Thiết kế API cổng điều phối Logistics"
session: 2
level: "Sáng tạo"
bloom: "Sáng tạo"
ex_code: "Ex05"
tags:
  - "type/bai-tap"
  - "session/02"
deliverable_filename: "[Sáng tạo] Thiết kế API cổng điều phối Logistics"
status: "done"
---

# Thiết kế API cổng điều phối Logistics

## 1. Bối cảnh nghiệp vụ

Một doanh nghiệp kho vận vận hành nhiều nhà kho ở các tỉnh thành. Ban điều hành muốn xây dựng một cổng điều phối Logistics (Logistics Dispatcher) dưới dạng API để các hệ thống khác (web quản trị, ứng dụng tài xế, đối tác bên thứ ba) cùng truy cập. Đây là kiến trúc Decoupled: server chỉ trả dữ liệu JSON, một API phục vụ được nhiều loại client.

Đây là bài tập mở. Bạn đóng vai kiến trúc sư API: tự đề xuất tập tính năng và thiết kế hệ endpoint cho cổng điều phối, sau đó triển khai bằng FastAPI ở mức tối thiểu chạy được.

## 2. Yêu cầu bài toán

Tự chọn và thiết kế tối thiểu một miền tài nguyên (resource) của hệ thống Logistics. Một vài gợi ý để khơi ý tưởng (không bắt buộc làm hết):

- warehouses — nhà kho: trạng thái vận hành, tỷ lệ tải (workload), danh sách node đang hoạt động.
- shipments — đơn vận: tạo đơn, tra cứu trạng thái, cập nhật tiến trình giao hàng.
- vehicles — phương tiện: danh sách xe, tình trạng sẵn sàng, phân công tuyến.
- dispatch — điều phối: gán đơn vận cho phương tiện/kho phù hợp.

Endpoint giám sát trạng thái hệ thống dưới đây là điểm khởi đầu có sẵn; bạn mở rộng từ đây.

```python
# gateway.py - điểm khởi đầu cổng điều phối Logistics
from fastapi import FastAPI

app = FastAPI(title="Logistics Dispatcher API")

@app.get("/")
def get_system_status():
    """Tra ve tinh trang van hanh tuc thoi cua nha kho trung tam."""
    return {
        "gateway_status": "operational",
        "workload_ratio": 0.72,
        "active_nodes": ["VN-SGN-01", "VN-DAD-02"],
        "system_message": "Logistics Dispatcher running smoothly."
    }
```

## 3. Ràng buộc thiết kế

- Mọi endpoint phải tuân thủ quy chuẩn RESTful: đặt tên tài nguyên bằng danh từ số nhiều, không nhúng động từ vào URL, hành động xác định bằng HTTP method (GET/POST/PUT/PATCH/DELETE).
- Có ít nhất một endpoint GET (đọc) và một endpoint POST (tạo) để minh họa ánh xạ CRUD.
- Dữ liệu trao đổi ở định dạng JSON; có thể lưu tạm trong bộ nhớ (in-memory) cho phạm vi bài tập.
- Ứng dụng chạy được bằng Uvicorn và xem được tài liệu tự sinh trên Swagger UI.

## 4. Yêu cầu

### Phần 1 — Thiết kế (đặc tả)

- Mô tả tính năng bạn chọn xây dựng và liệt kê bảng các endpoint dự kiến (đường dẫn, HTTP method, mục đích).
- Giải thích mỗi endpoint ánh xạ với thao tác CRUD nào và vì sao chọn HTTP method đó.
- Nêu ngắn gọn cấu trúc dữ liệu JSON của tài nguyên chính.

| Đường dẫn (endpoint) | HTTP method | Mục đích nghiệp vụ |
| --- | --- | --- |
| /shipments | GET |  |
| /shipments | POST |  |
|  |  |  |

### Phần 2 — Triển khai

- Hiện thực hóa các endpoint đã thiết kế bằng FastAPI trong file gateway.py.
- Trả về dữ liệu JSON đúng cấu trúc đã đặc tả; khai báo kiểu dữ liệu cho path/query parameter khi cần.
- Đặt title/description cho app để Swagger UI hiển thị rõ ràng.

### Phần 3 — Kiểm thử & thuyết minh

1. Chạy server bằng uvicorn gateway:app --reload và truy cập http://127.0.0.1:8000/docs.
2. Dùng Try it out để gọi thử từng endpoint và chụp lại kết quả phản hồi JSON.
3. Viết một đoạn ngắn (5–7 dòng) thuyết minh vì sao thiết kế của bạn tuân thủ RESTful và dễ mở rộng cho các client khác nhau.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session02_Ex05
```

```
HNKS25CNTT1_FastAPI_Session02_Ex05
```

— Thuộc [[Session 02 — MOC]]
