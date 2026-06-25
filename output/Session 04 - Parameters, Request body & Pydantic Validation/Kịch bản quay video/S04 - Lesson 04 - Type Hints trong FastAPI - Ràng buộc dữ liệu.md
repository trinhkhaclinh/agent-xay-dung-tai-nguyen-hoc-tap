---
type: "kich-ban-video"
title: "Lesson 04 - Type Hints trong FastAPI - Ràng buộc dữ liệu"
session: 4
lesson: 4
tags:
  - "type/kich-ban-video"
  - "session/04"
concepts:
  - "[[Type Hints]]"
  - "[[Query() validation]]"
  - "[[Path() validation]]"
  - "[[Field() constraints]]"
  - "[[422 Unprocessable Entity]]"
  - "[[Swagger UI (-docs)|Swagger UI (/docs)]]"
deliverable_filename: "Lesson 04 - Type Hints trong FastAPI - Ràng buộc dữ liệu"
status: "done"
---

## Đặt các ràng buộc dữ liệu nâng cao

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu cách thiết lập các ràng buộc nâng cao cho dữ liệu bằng cách sử dụng Query, Path, và Field.

Trong thực tế, chỉ định nghĩa kiểu dữ liệu là số hay chuỗi chưa đủ. Chúng ta cần những ràng buộc chi tiết hơn như: tuổi phải lớn hơn 18, từ khóa tìm kiếm phải dài ít nhất 2 ký tự, hay email phải đúng định dạng.

**[Chuyển tiếp slide]**

## Sử dụng Query, Path, và Field

Hãy cùng theo dõi ví dụ trên màn hình. Để ràng buộc query parameter, chúng ta dùng Query(). Để ràng buộc path parameter, chúng ta dùng Path() và để đặt ràng buộc cho thuộc tính của Pydantic model, chúng ta dùng Field().

**[mở trình duyệt hiển thị code ví dụ kết hợp Query, Path và Field]**

Các em có thể dùng tham số min_length, max_length cho chuỗi; ge, le, gt, lt cho số và pattern để dùng biểu thức chính quy kiểm tra email. Tất cả các ràng buộc này không chỉ tự động kiểm chứng khi chạy mà còn hiển thị rất rõ ràng trên tài liệu Swagger UI tự động.

**[mở tài liệu Swagger UI tại đường dẫn /docs và demo kiểm thử]**

Khi thầy nhập thử tuổi là 15 vào API tạo sản phẩm, Swagger UI sẽ hiển thị ngay lỗi 422. Cấu trúc lỗi này gồm loc chỉ ra vị trí lỗi, msg mô tả lỗi và type phân loại lỗi, giúp lập trình viên frontend dễ dàng lập trình hiển thị thông báo lỗi lên giao diện.

## Tổng kết bài giảng

Như vậy là chúng ta đã cùng nhau làm chủ kỹ thuật validate dữ liệu nâng cao với Query, Path, Field và hiểu sâu cấu trúc lỗi 422. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở session học tiếp theo nhé!

## Khái niệm liên quan

- [[Type Hints]]
- [[Query() validation]]
- [[Path() validation]]
- [[Field() constraints]]
- [[422 Unprocessable Entity]]
- [[Swagger UI (-docs)|Swagger UI (/docs)]]

— Thuộc [[Session 04 — MOC]]
