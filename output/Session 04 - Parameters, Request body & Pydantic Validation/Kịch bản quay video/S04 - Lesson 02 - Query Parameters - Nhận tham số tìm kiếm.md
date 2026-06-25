---
type: "kich-ban-video"
title: "Lesson 02 - Query Parameters - Nhận tham số tìm kiếm"
session: 4
lesson: 2
tags:
  - "type/kich-ban-video"
  - "session/04"
concepts:
  - "[[Query Parameter]]"
  - "[[Tham số mặc định (optional)]]"
  - "[[Tham số bắt buộc (required)]]"
  - "[[Optional - None|Optional / None]]"
  - "[[Kết hợp Path + Query]]"
deliverable_filename: "Lesson 02 - Query Parameters - Nhận tham số tìm kiếm"
status: "done"
---

## Tìm hiểu về Query Parameters

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học này, thầy và các em sẽ cùng nhau nghiên cứu về Query Parameters - tham số truy vấn.

Khác với Path Parameter dùng để định vị một đối tượng cụ thể, Query Parameter dùng để lọc, sắp xếp, tìm kiếm hoặc phân trang dữ liệu. Chúng xuất hiện sau dấu hỏi chấm trên URL và được phân tách bởi dấu và.

**[Chuyển tiếp slide]**

## Khai báo Query Parameter trong FastAPI

Bây giờ, chúng ta hãy xem cách khai báo trong FastAPI. Các em hãy chú ý: bất kỳ tham số nào của hàm xử lý route mà KHÔNG nằm trong route decorator sẽ mặc định được FastAPI hiểu là Query Parameter.

**[mở trình duyệt và hiển thị code API tìm kiếm khóa học]**

Ở đây, thầy khai báo keyword kiểu str với giá trị mặc định là chuỗi rỗng và level kiểu str hoặc None với mặc định là None. Do có giá trị mặc định, các tham số này trở thành tham số tùy chọn. Nếu client không truyền, ứng dụng vẫn chạy bình thường. Còn nếu các em bỏ giá trị mặc định đi, tham số đó sẽ trở thành bắt buộc.

**[mở công cụ Postman gửi request /courses?keyword=python]**

Khi thầy gửi request này, các em thấy server trả về đúng các khóa học có chứa chữ python trong tên. Và đặc biệt, FastAPI còn tự động ép kiểu boolean cực kỳ thông minh khi các em truyền true, false, 1, 0 từ URL.

## Tổng kết bài giảng

Qua bài học hôm nay, các em đã nắm vững cách khai báo và sử dụng Query Parameter để lọc dữ liệu, cũng như phân biệt được tham số bắt buộc và tùy chọn. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở bài học tiếp theo!

## Khái niệm liên quan

- [[Query Parameter]]
- [[Tham số mặc định (optional)]]
- [[Tham số bắt buộc (required)]]
- [[Optional - None|Optional / None]]
- [[Kết hợp Path + Query]]

— Thuộc [[Session 04 — MOC]]
