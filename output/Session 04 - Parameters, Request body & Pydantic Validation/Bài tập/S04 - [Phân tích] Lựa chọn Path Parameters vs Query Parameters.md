---
type: "bai-tap"
title: "[Phân tích] Lựa chọn Path Parameters vs Query Parameters"
session: 4
level: "Phân tích"
bloom: "Phân tích"
ex_code: "Ex04"
tags:
  - "type/bai-tap"
  - "session/04"
deliverable_filename: "[Phân tích] Lựa chọn Path Parameters vs Query Parameters"
status: "done"
---

# Phân tích so sánh Path Parameters và Query Parameters

## 1. Bối cảnh nghiệp vụ

Một công ty công nghệ giáo dục đang tái thiết kế hệ thống API của mình. Có hai nghiệp vụ cần thiết kế:
Nghiệp vụ A: Xem danh sách bài học của một khóa học cụ thể.
Nghiệp vụ B: Tìm kiếm khóa học theo từ khóa và sắp xếp theo giá tiền.

## 2. Yêu cầu phân tích

Sinh viên cần lập bảng phân tích so sánh và chọn giải pháp thiết kế URL tối ưu cho hai nghiệp vụ trên.

## 3. Yêu cầu đầu ra

### (1) Lập bảng so sánh

| Tiêu chí | Path Parameters | Query Parameters |
| --- | --- | --- |
| Mục đích sử dụng chính |  |  |
| Tính bắt buộc |  |  |
| Ảnh hưởng cấu trúc URL |  |  |
| Khả năng caching ở phía Client |  |  |

### (2) Thiết kế API thực tế

- Đề xuất URL và viết code triển khai API cho cả Nghiệp vụ A và Nghiệp vụ B trong FastAPI.
- Giải thích lý do lựa chọn của mình dựa trên quy chuẩn RESTful API.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session04_Ex04
```

```
HNKS25CNTT1_FastAPI_Session04_Ex04
```

— Thuộc [[Session 04 — MOC]]
