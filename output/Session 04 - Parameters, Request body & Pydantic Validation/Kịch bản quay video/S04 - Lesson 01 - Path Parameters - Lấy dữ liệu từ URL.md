---
type: "kich-ban-video"
title: "Lesson 01 - Path Parameters - Lấy dữ liệu từ URL"
session: 4
lesson: 1
tags:
  - "type/kich-ban-video"
  - "session/04"
concepts:
  - "[[Path Parameter]]"
  - "[[Ép kiểu theo type hint (int-str)|Ép kiểu theo type hint (int/str)]]"
  - "[[Tự động validate 422]]"
  - "[[Thứ tự khai báo route]]"
  - "[[Enum cho giá trị định sẵn]]"
  - "[[RESTful naming]]"
deliverable_filename: "Lesson 01 - Path Parameters - Lấy dữ liệu từ URL"
status: "done"
---

## Giới thiệu về Path Parameters

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về một khái niệm rất quan trọng trong thiết kế và xây dựng API - đó chính là Path Parameters, hay còn gọi là tham số đường dẫn.

Hãy cùng nhìn lên sơ đồ kiến trúc URL trên màn hình. Mỗi tài nguyên trong hệ thống đều cần một định danh duy nhất. Khi các em muốn truy xuất thông tin cụ thể của một sinh viên nào đó, các em không thể gọi chung chung là đường dẫn học sinh được. Chúng ta cần một mã số định danh cụ thể, ví dụ như mã số 123. Phần thay đổi này nằm trực tiếp trong đường dẫn và đó chính là Path Parameter.

**[Chuyển tiếp slide]**

## Cách khai báo Path Parameter trong FastAPI

Bây giờ, chúng ta sẽ mở công cụ soạn thảo mã nguồn VS Code lên để xem cách khai báo trong code FastAPI nhé. Trong FastAPI, các em chỉ cần bọc tên biến trong cặp dấu ngoặc nhọn ở đường dẫn của route decorator. Đồng thời, các em khai báo tên tham số đó trong hàm xử lý bên dưới.

**[mở trình duyệt và hiển thị code FastAPI]**

Như các em thấy trên màn hình, khi chúng ta đặt student_id có kiểu dữ liệu là int, FastAPI sẽ thực hiện hai việc. Một là ép kiểu chuỗi nhận từ URL sang kiểu int. Hai là tự động kiểm chứng dữ liệu. Nếu người dùng truyền vào chữ thay vì số, FastAPI sẽ trả về lỗi HTTP 422.

**[mở công cụ Postman và thực hiện demo gọi API /students/abc]**

Khi thầy gửi request với tham số abc, các em sẽ thấy ngay mã lỗi 422 Unprocessable Entity hiển thị dưới dạng JSON. Đây chính là tính năng tự động validate cực kỳ mạnh mẽ của FastAPI.

## Thứ tự khai báo route để tránh xung đột

Một lưu ý cực kỳ quan trọng mà các em cần nhớ: đó là thứ tự khai báo route. Vì FastAPI phân giải đường dẫn từ trên xuống dưới, các em luôn phải đặt route tĩnh ví dụ như /students/me lên trước route động là /students/student_id. Nếu không, route tĩnh sẽ bị nhận nhầm là một giá trị của route động.

## Tổng kết bài giảng

Như vậy là trong bài học này, thầy đã hướng dẫn các em hiểu rõ cách hoạt động của Path Parameter, cách khai báo và thứ tự sắp xếp route để tránh xung đột đường dẫn. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em trong bài học tiếp theo nhé!

## Khái niệm liên quan

- [[Path Parameter]]
- [[Ép kiểu theo type hint (int-str)|Ép kiểu theo type hint (int/str)]]
- [[Tự động validate 422]]
- [[Thứ tự khai báo route]]
- [[Enum cho giá trị định sẵn]]
- [[RESTful naming]]

— Thuộc [[Session 04 — MOC]]
