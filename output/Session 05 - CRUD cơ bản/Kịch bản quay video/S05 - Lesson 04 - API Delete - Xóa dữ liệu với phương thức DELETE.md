---
type: "kich-ban-video"
title: "Lesson 04 - API Delete - Xóa dữ liệu với phương thức DELETE"
session: 5
lesson: 4
tags:
  - "type/kich-ban-video"
  - "session/05"
concepts:
  - "[[DELETE method]]"
  - "[[HTTP 204 No Content]]"
  - "[[Xóa vật lý]]"
  - "[[Xóa mềm (Soft Delete)]]"
deliverable_filename: "Lesson 04 - API Delete - Xóa dữ liệu với phương thức DELETE"
status: "done"
---

## Thao tác DELETE trong CRUD

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Chúng ta sẽ cùng nhau tìm hiểu thao tác cuối cùng trong chuỗi CRUD - đó là API Delete, sử dụng phương thức HTTP DELETE.

Thao tác xóa giúp chúng ta loại bỏ một tài nguyên ra khỏi hệ thống. Khi thực hiện thành công, mã trạng thái phản hồi chuẩn nhất thường là 204 No Content.

**[Chuyển tiếp slide]**

## Triển khai API DELETE trong FastAPI

Hãy cùng quan sát đoạn code trên màn hình. Để thiết lập mã trả về là 204, chúng ta truyền status.HTTP_204_NO_CONTENT vào decorator route.

**[mở trình duyệt hiển thị code API DELETE]**

Trong hàm, nếu tìm thấy ID, thầy dùng hàm pop() để loại bỏ sinh viên khỏi danh sách và kết thúc hàm bằng lệnh return trống. Khi đó, FastAPI tự hiểu và trả về mã 204 mà không có nội dung body. Còn nếu không tìm thấy, hệ thống vẫn ném ra lỗi 404 như thường lệ.

**[mở Postman gửi request DELETE /students/1]**

Các em thấy trên Postman, response trả về hoàn toàn trống rỗng nhưng mã trạng thái hiển thị rõ là 204 No Content. Đây là kết quả xóa vật lý thành công.

## Xóa mềm - Giải pháp thực tế doanh nghiệp

Thầy cũng muốn mở rộng thêm về khái niệm Xóa mềm. Trong các dự án thực tế, người ta rất hạn chế xóa vĩnh viễn dữ liệu. Thay vào đó, chúng ta chỉ thay đổi một cờ trạng thái, ví dụ chuyển is_deleted thành True để ẩn tài nguyên đi.

## Tổng kết bài giảng

Như vậy, thầy và các em đã đi qua đầy đủ 4 thao tác CRUD in-memory. Cảm ơn các em đã đồng hành cùng thầy và chúc các em thực hành tốt!

## Khái niệm liên quan

- [[DELETE method]]
- [[HTTP 204 No Content]]
- [[Xóa vật lý]]
- [[Xóa mềm (Soft Delete)]]

— Thuộc [[Session 05 — MOC]]
