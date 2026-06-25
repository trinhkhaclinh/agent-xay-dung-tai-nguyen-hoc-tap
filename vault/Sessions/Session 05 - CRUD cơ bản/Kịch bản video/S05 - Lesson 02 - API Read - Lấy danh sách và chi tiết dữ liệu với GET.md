---
type: "kich-ban-video"
title: "Lesson 02 - API Read - Lấy danh sách và chi tiết dữ liệu với GET"
session: 5
lesson: 2
tags:
  - "type/kich-ban-video"
  - "session/05"
concepts:
  - "[[GET method]]"
  - "[[HTTP 200 OK]]"
  - "[[HTTP 404 Not Found]]"
  - "[[Lọc danh sách]]"
deliverable_filename: "Lesson 02 - API Read - Lấy danh sách và chi tiết dữ liệu với GET"
status: "done"
---

## Phương thức GET và API đọc dữ liệu

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Hôm nay, thầy và các em sẽ đi tiếp thao tác thứ hai trong chu trình CRUD - đó là thao tác Read, sử dụng phương thức HTTP GET.

GET là phương thức an toàn và đồng nhất, có nhiệm vụ trả dữ liệu về mà không thay đổi bất kỳ trạng thái nào trên server.

**[Chuyển tiếp slide]**

## API lấy danh sách và tìm kiếm chi tiết

Hãy cùng nhìn vào mã nguồn khai báo GET API. Để hỗ trợ tìm kiếm, chúng ta kết hợp thêm query parameter keyword trong hàm xử lý danh sách.

**[mở trình duyệt hiển thị code API GET list và GET detail]**

Còn đối với API lấy chi tiết một sinh viên cụ thể theo ID, chúng ta khai báo ID dưới dạng path parameter. Thầy dùng vòng lặp để duyệt và tìm kiếm sinh viên. Nếu tìm thấy, chúng ta trả về dữ liệu. Nếu không tìm thấy, chúng ta ném ra lỗi HTTPException với mã lỗi 404 Not Found.

**[mở Postman gọi GET /students/999 để minh họa lỗi 404]**

Khi thầy truyền ID sinh viên là 999 không tồn tại, Postman sẽ nhận ngay phản hồi lỗi 404 Not Found. Đây là cách xử lý lỗi cực kỳ chuẩn mực trong thiết kế API.

## Tổng kết bài giảng

Tóm lại, trong bài học này các em đã biết cách lấy danh sách và thông tin chi tiết của đối tượng sử dụng GET và xử lý lỗi 404 Not Found. Cảm ơn các em đã theo dõi. Hẹn gặp lại các em ở bài học cập nhật dữ liệu!

## Khái niệm liên quan

- [[GET method]]
- [[HTTP 200 OK]]
- [[HTTP 404 Not Found]]
- [[Lọc danh sách]]

— Thuộc [[Session 05 — MOC]]
