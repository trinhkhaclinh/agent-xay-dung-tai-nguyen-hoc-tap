---
type: "kich-ban-video"
title: "Lesson 03 - Request Body với Pydantic - Nhận dữ liệu JSON"
session: 4
lesson: 3
tags:
  - "type/kich-ban-video"
  - "session/04"
concepts:
  - "[[Pydantic BaseModel]]"
  - "[[Request Body]]"
  - "[[Khai báo schema]]"
  - "[[Tự động validate JSON]]"
  - "[[response_model]]"
  - "[[Định dạng JSON]]"
deliverable_filename: "Lesson 03 - Request Body với Pydantic - Nhận dữ liệu JSON"
status: "done"
---

## Giới thiệu về Request Body và Pydantic

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Hôm nay, thầy và các em sẽ cùng tìm hiểu về cách truyền dữ liệu lớn và phức tạp vào server bằng Request Body sử dụng thư viện Pydantic.

Khi các em muốn đăng ký một sinh viên mới hay thêm một khóa học mới, thông tin gửi lên rất nhiều. Việc truyền qua URL là không khả thi. Chúng ta sẽ đóng gói dữ liệu dưới dạng JSON và đặt trong Request Body.

**[Chuyển tiếp slide]**

## Tạo Pydantic BaseModel để kiểm chứng dữ liệu

Để FastAPI hiểu được cấu trúc JSON gửi lên, chúng ta sẽ định nghĩa một lớp kế thừa từ Pydantic BaseModel. Hãy cùng nhìn lên màn hình.

**[mở trình duyệt hiển thị code định nghĩa class StudentCreate]**

Chúng ta khai báo các thuộc tính name, email kiểu str và age kiểu int. Khi áp dụng class này làm kiểu dữ liệu cho tham số của route xử lý POST, FastAPI sẽ tự động phân giải JSON từ request body và validate. Nếu dữ liệu gửi lên bị thiếu trường bắt buộc hoặc sai kiểu dữ liệu, FastAPI lập tức trả lỗi 422 mà các em không cần tự viết code validation.

**[mở Postman thực hiện demo POST /students với body JSON hợp lệ và không hợp lệ]**

Như các em thấy, khi thầy truyền thiếu trường name, API lập tức phản hồi mã trạng thái 422 kèm mô tả rõ ràng lỗi thiếu trường name. Điều này giúp code backend của chúng ta cực kỳ an toàn.

## Tổng kết bài giảng

Tóm lại, trong bài học này các em đã biết cách sử dụng Pydantic BaseModel để định nghĩa schema và tự động validate dữ liệu gửi lên trong Request Body. Cảm ơn các em đã chú ý lắng nghe. Hẹn gặp lại các em trong các bài học sau!

## Khái niệm liên quan

- [[Pydantic BaseModel]]
- [[Request Body]]
- [[Khai báo schema]]
- [[Tự động validate JSON]]
- [[response_model]]
- [[Định dạng JSON]]

— Thuộc [[Session 04 — MOC]]
