---
type: "bai-tap"
title: "[Vận dụng chuyên sâu] Triển khai API PATCH cập nhật từng phần"
session: 5
level: "Vận dụng chuyên sâu"
bloom: "Vận dụng"
ex_code: "Ex03"
tags:
  - "type/bai-tap"
  - "session/05"
deliverable_filename: "[Vận dụng chuyên sâu] Triển khai API PATCH cập nhật từng phần"
status: "done"
---

# Phát triển tính năng cập nhật từng phần với PATCH

## 1. Bối cảnh nghiệp vụ

Mặc dù phương thức PUT rất phổ biến, nhưng đôi khi người dùng chỉ muốn sửa đổi một thuộc tính duy nhất (ví dụ: chỉ sửa đổi email của học viên mà giữ nguyên họ tên). Nếu dùng PUT, người dùng buộc phải gửi lại cả họ tên cũ. Giải pháp thay thế tối ưu là sử dụng phương thức PATCH.

## 2. Quy tắc nghiệp vụ

- Sử dụng decorator `@app.patch`.
- Schema nhận vào phải cho phép các trường có giá trị tùy chọn (tất cả các trường đều có mặc định là None).
- Chỉ cập nhật những thuộc tính được client gửi lên thực sự trong request body.

## 3. Yêu cầu đầu ra

### (1) Thiết kế Pydantic Schema cho PATCH

- Tạo `StudentPatchSchema` với các trường `name: str | None = None` và `email: str | None = None`.

### (2) Viết logic cập nhật động

- Duyệt danh sách tìm kiếm học viên theo ID.
- Sử dụng hàm `.dict(exclude_unset=True)` của Pydantic để chỉ lấy ra các trường được truyền lên và cập nhật vào đối tượng gốc.
- Trả lỗi 404 nếu không tìm thấy.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session05_Ex03
```

```
HNKS25CNTT1_FastAPI_Session05_Ex03
```

— Thuộc [[Session 05 — MOC]]
