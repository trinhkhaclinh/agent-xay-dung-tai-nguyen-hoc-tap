---
type: "kich-ban-video"
title: "Lesson 03 - API Update - Cập nhật dữ liệu với PUT"
session: 5
lesson: 3
tags:
  - "type/kich-ban-video"
  - "session/05"
concepts:
  - "[[PUT method]]"
  - "[[Idempotent update]]"
  - "[[Ghi đè thuộc tính]]"
  - "[[Cập nhật từng phần (PATCH)]]"
deliverable_filename: "Lesson 03 - API Update - Cập nhật dữ liệu với PUT"
status: "done"
---

## Tìm hiểu về API Update và phương thức PUT

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Bài học hôm nay của chúng ta sẽ tập trung vào thao tác Update sử dụng phương thức HTTP PUT.

Khi sử dụng PUT, mục đích của chúng ta là thay thế hoặc ghi đè toàn bộ dữ liệu của một tài nguyên đang có bằng một bộ dữ liệu mới gửi lên từ client.

**[Chuyển tiếp slide]**

## Khai báo API PUT và phân biệt với PATCH

Bây giờ, chúng ta sẽ xem cách viết code API PUT trong FastAPI. Chúng ta cần nhận cả ID của sinh viên qua path parameter và thông tin cập nhật mới qua request body.

**[mở trình duyệt hiển thị code API PUT]**

Khi tìm thấy sinh viên khớp ID, thầy thực hiện ghi đè toàn bộ trường name và email. Nếu không tìm thấy, hệ thống trả lỗi 404. Các em cũng lưu ý sự khác biệt: PUT dùng để ghi đè toàn bộ, trong khi phương thức PATCH được dùng khi chúng ta chỉ muốn cập nhật một hoặc vài thuộc tính riêng lẻ của đối tượng.

**[mở Postman thực hiện demo API PUT]**

Thầy gửi yêu cầu PUT thành công, dữ liệu sinh viên đã thay đổi ngay lập tức trên danh sách in-memory của server.

## Tổng kết bài giảng

Như vậy, thầy đã hướng dẫn các em nắm bắt phương thức PUT để cập nhật dữ liệu và cách phân biệt với PATCH. Cảm ơn các em và hẹn gặp lại các em ở bài học xóa dữ liệu tiếp theo!

## Khái niệm liên quan

- [[PUT method]]
- [[Idempotent update]]
- [[Ghi đè thuộc tính]]
- [[Cập nhật từng phần (PATCH)]]

— Thuộc [[Session 05 — MOC]]
