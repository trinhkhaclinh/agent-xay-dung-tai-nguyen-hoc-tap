---
type: "bai-tap"
title: "[Vận dụng chuyên sâu] Thiết kế và validate API Đăng ký môn học"
session: 4
level: "Vận dụng chuyên sâu"
bloom: "Vận dụng"
ex_code: "Ex03"
tags:
  - "type/bai-tap"
  - "session/04"
deliverable_filename: "[Vận dụng chuyên sâu] Thiết kế và validate API Đăng ký môn học"
status: "done"
---

# Đăng ký khóa học với Request Body lồng nhau

## 1. Bối cảnh nghiệp vụ

Hệ thống đăng ký học tập cần một API nhận thông tin đăng ký của sinh viên. Mỗi bản đăng ký gồm: mã số sinh viên, danh sách mã các môn học muốn đăng ký (tối thiểu đăng ký 1 môn, tối đa 5 môn), và thông tin người bảo trợ liên hệ khẩn cấp (gồm tên và số điện thoại).

## 2. Quy tắc nghiệp vụ

- Mã số sinh viên phải lớn hơn 0.
- Danh sách môn học phải chứa các chuỗi ký tự mã môn (ví dụ 'IT215'), độ dài danh sách từ 1 đến 5.
- Thông tin liên hệ khẩn cấp là bắt buộc, số điện thoại phải có định dạng số điện thoại Việt Nam (10 chữ số).

## 3. Yêu cầu đầu ra

### (1) Thiết kế Pydantic Schemas

- Định nghĩa `EmergencyContactSchema` chứa name và phone.
- Định nghĩa `CourseRegistrationSchema` chứa student_id, course_codes (kiểu list[str]) và contact (kiểu EmergencyContactSchema).

### (2) Viết API Endpoint và chạy thử

- Viết endpoint POST `/registrations` nhận body JSON tương ứng.
- Kiểm tra validation khi gửi dữ liệu sai quy tắc.

## 5. Quy định nộp bài

- Nộp code đã sửa + phần phân tích lỗi
- Đưa lên GitHub theo format:

```
[Tên Lớp]_FastAPI_Session04_Ex03
```

```
HNKS25CNTT1_FastAPI_Session04_Ex03
```

— Thuộc [[Session 04 — MOC]]
