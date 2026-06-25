---
type: "kich-ban-video"
title: "Lesson 01 - API Create - Tạo dữ liệu với phương thức POST"
session: 5
lesson: 1
tags:
  - "type/kich-ban-video"
  - "session/05"
concepts:
  - "[[POST method]]"
  - "[[HTTP 201 Created]]"
  - "[[In-memory database]]"
  - "[[Dữ liệu trùng lặp]]"
deliverable_filename: "Lesson 01 - API Create - Tạo dữ liệu với phương thức POST"
status: "done"
---

## Giới thiệu về API Create và phương thức POST

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về thao tác đầu tiên trong chu trình CRUD - đó chính là API Create, hay tạo mới dữ liệu sử dụng phương thức HTTP POST.

Để thực hiện việc này, chúng ta cần gửi dữ liệu lên server thông qua Request Body. Sau khi server ghi nhận thành công, mã phản hồi trả về cần là 201 Created.

**[Chuyển tiếp slide]**

## Cú pháp khai báo POST API trong FastAPI

Hãy cùng mở mã nguồn lên để xem cách khai báo trong FastAPI. Để quy định mã trả về thành công là 201, chúng ta truyền tham số status_code vào decorator route.

**[mở trình duyệt hiển thị code API POST sinh viên]**

Như các em thấy trong code, trước khi thêm sinh viên mới vào danh sách, thầy tiến hành kiểm tra xem email của sinh viên này đã tồn tại trong danh sách hay chưa. Nếu đã tồn tại, thầy ném ra lỗi HTTP 400 Bad Request. Nếu không, thầy tạo đối tượng mới với ID tự động tăng và thêm vào danh sách.

**[mở công cụ Postman thực hiện gọi POST /students thành công và thất bại]**

Khi thầy gửi request POST qua Postman với email trùng, hệ thống trả ngay mã lỗi 400. Còn khi gửi email mới, kết quả trả về là 201 Created cùng thông tin đối tượng.

## Tổng kết bài giảng

Như vậy, chúng ta đã hoàn thành bài học về API Create với phương thức POST và mã trạng thái 201 Created. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở bài học đọc dữ liệu tiếp theo!

## Khái niệm liên quan

- [[POST method]]
- [[HTTP 201 Created]]
- [[In-memory database]]
- [[Dữ liệu trùng lặp]]

— Thuộc [[Session 05 — MOC]]
