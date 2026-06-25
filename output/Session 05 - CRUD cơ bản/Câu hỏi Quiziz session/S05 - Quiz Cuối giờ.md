---
type: "quiz"
title: "Session 05 — Quiz Cuối giờ"
session: 5
quiz_type: "cuoigio"
sheet_name: "Quiz_CuoiGio_FastAPI_05"
tags:
  - "type/quiz"
  - "session/05"
deliverable_filename: ""
status: "done"
---

# Session 05 — Quiz Cuối giờ

> 15 câu · lược đồ 12 cột (stage-2 ánh xạ sang .xlsx Quizizz).

| question_content | answer_1 | explanation_answer_1 | answer_2 | explanation_answer_2 | answer_3 | explanation_answer_3 | answer_4 | explanation_answer_4 | isCorrect | difficulty | category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Để khai báo mã trạng thái HTTP trả về mặc định khi gọi API thành công trong route decorator, ta dùng đối số nào? | code | Không đúng. | status | Không đúng. | status_code | Chính xác, ví dụ: @app.post('/...', status_code=201). | response_status | Không đúng. | 3 | 5 | DECORATOR |
| Khi thực hiện API POST tạo mới đối tượng, nếu phát hiện email gửi lên đã tồn tại trong danh sách, lập trình viên nên xử lý như thế nào? | Vẫn cho ghi đè đè lên đối tượng cũ | Gây mất dữ liệu người dùng cũ. | Ném ra lỗi HTTPException với mã lỗi 400 Bad Request để thông báo email đã tồn tại | Chính xác, đây là cách validate logic nghiệp vụ cơ bản. | Trả về thông tin đối tượng cũ với mã 201 Created | Sai logic nghiệp vụ và mã phản hồi. | Crash server bằng lệnh exit | Không được phép làm sập ứng dụng. | 2 | 6 | VALIDATION |
| Vì sao phương thức HTTP GET được coi là an toàn (safe)? | Vì dữ liệu truyền lên luôn được mã hóa | Không đúng. | Vì nó chỉ thực hiện đọc dữ liệu và không làm thay đổi trạng thái tài nguyên trên máy chủ | Chính xác, GET không làm ghi nhận mới, sửa đổi hay xóa dữ liệu. | Vì nó không cho phép truyền bất kỳ tham số nào | GET cho phép truyền query và path parameters. | Vì nó bắt buộc phải chạy qua giao thức HTTPS | GET chạy được cả trên HTTP. | 2 | 6 | SAFE_METHOD |
| Thao tác cập nhật in-memory list bằng PUT yêu cầu logic xử lý nào sau khi tìm thấy ID khớp? | Xóa phần tử cũ đi và dùng append() thêm phần tử mới | Không cần thiết và thay đổi thứ tự phần tử. | Ghi đè giá trị mới lên các thuộc tính tương ứng của phần tử cũ | Chính xác, ghi đè giá trị giúp giữ nguyên tham chiếu đối tượng trong danh sách. | Chuyển đổi cờ is_deleted sang True | Đây là thao tác xóa mềm. | Trả về lỗi 400 Bad Request | Thao tác thành công nên không trả lỗi 400. | 2 | 6 | UPDATE |
| Khi xóa thành công một đối tượng và trả về mã trạng thái HTTP 204 No Content, body của HTTP response sẽ chứa thông tin gì? | Chuỗi JSON {'message': 'Success'} | Mã 204 yêu cầu body phải trống. | Hoàn toàn trống rỗng (không chứa dữ liệu) | Chính xác, No Content nghĩa là không có nội dung body. | Mã ID của đối tượng vừa bị xóa | Không đúng. | Thông tin chi tiết đối tượng bị xóa để đối chiếu | Không đúng. | 2 | 7 | DELETE |
| Trong thực tế, khi triển khai API DELETE, phương thức nào dưới đây an toàn hơn để bảo toàn lịch sử dữ liệu? | Xóa vật lý (Hard Delete) | Mất dữ liệu vĩnh viễn và có thể gây lỗi khóa ngoại. | Xóa mềm (Soft Delete) | Chính xác, chỉ cập nhật cờ ẩn dữ liệu giúp khôi phục dễ dàng. | Reset lại toàn bộ máy chủ | Gây gián đoạn dịch vụ toàn bộ hệ thống. | Tự động sao lưu dữ liệu sang ổ đĩa khác rồi xóa vật lý | Tốn kém tài nguyên và phức tạp. | 2 | 5 | SOFT_DELETE |
| Khi client gọi API GET /students/100 (trong đó ID 100 không tồn tại), mã trạng thái HTTP nào là chuẩn nhất để trả về? | 200 OK | Không đúng, API thất bại. | 400 Bad Request | Lỗi cú pháp request, còn ở đây request đúng cú pháp nhưng không có dữ liệu. | 404 Not Found | Chính xác, 404 Not Found biểu thị tài nguyên không tồn tại. | 500 Internal Server Error | Lỗi hệ thống phía server. | 3 | 5 | READ |
| Đối với API GET danh sách sinh viên, việc truyền thêm tham số keyword: str = '' đóng vai trò gì? | Là path parameter bắt buộc để định vị sinh viên | Không đúng. | Là query parameter tùy chọn dùng để lọc kết quả theo tên sinh viên | Chính xác, mặc định chuỗi rỗng để trả về toàn bộ nếu không truyền keyword. | Là request body nhận dữ liệu JSON | Không đúng. | Là cấu hình bảo mật bắt buộc | Không liên quan. | 2 | 5 | READ |
| Thao tác cập nhật từng phần (PATCH) trong Pydantic được thực hiện thuận tiện nhờ phương thức chuyển đổi dữ liệu nào? | student.dict(exclude_unset=True) | Chính xác, exclude_unset=True giúp loại bỏ các trường client không truyền lên (giữ lại None mặc định). | student.dict() | Phương thức này sẽ lấy toàn bộ các trường kể cả các trường mặc định None. | student.json() | Trả về chuỗi JSON. | str(student) | Trả về chuỗi biểu diễn đối tượng. | 1 | 8 | PATCH |
| Khi thiết kế RESTful API, Endpoint dùng để xóa sinh viên có ID là 5 nên đặt đường dẫn và phương thức nào? | GET /students/delete/5 | Sai phương thức và vi phạm RESTful naming. | DELETE /students/5 | Chính xác, dùng đúng phương thức DELETE và path parameter định danh tài nguyên. | POST /students/5/delete | Sai phương thức. | PUT /students/5 | PUT dùng cho cập nhật ghi đè. | 2 | 6 | REST_DESIGN |
| Phương thức HTTP POST có tính chất Idempotent hay không? | Có, luôn trả về cùng kết quả | Không đúng. | Không, mỗi lần gọi POST thành công thường tạo thêm một tài nguyên mới trong hệ thống | Chính xác, gọi nhiều lần sinh ra nhiều tài nguyên khác nhau. | Có, chỉ khi chạy trên máy chủ Uvicorn | Không liên quan tới máy chủ. | Không, nhưng có tính chất Safe | POST không an toàn vì làm thay đổi trạng thái máy chủ. | 2 | 6 | POST |
| Khi viết hàm delete_student(student_id: int) thao tác trên list in-memory của Python, từ khóa nào cần dùng để thay đổi danh sách bên ngoài phạm vi hàm? | local | Không đúng. | nonlocal | Dùng cho hàm lồng nhau. | global | Chính xác, sử dụng global students_db để khai báo biến danh sách toàn cục. | import | Dùng để import thư viện. | 3 | 6 | PYTHON |
| Tại sao không nên dùng phương thức HTTP GET cho hành động xóa dữ liệu? | Vì GET không hỗ trợ truyền tham số | GET hỗ trợ truyền tham số trên URL. | Vì các công cụ tìm kiếm (crawler) hoặc trình duyệt có thể tự động gọi trước (prefetch) các link GET, dẫn tới vô tình xóa sạch dữ liệu hệ thống | Chính xác, đây là lỗ hổng bảo mật nghiêm trọng nếu dùng GET để thay đổi trạng thái hệ thống. | Vì GET chạy chậm hơn các phương thức khác | Tốc độ tương đương. | Vì dữ liệu xóa bằng GET sẽ bị lỗi hiển thị | Không liên quan. | 2 | 7 | REST_DESIGN |
| Nếu client gửi request PUT đến /students/5 mà thiếu trường email bắt buộc trong schema, FastAPI phản hồi lỗi gì? | 400 Bad Request | Không đúng. | 404 Not Found | Không đúng. | 422 Unprocessable Entity | Chính xác, do dữ liệu không vượt qua bước validate cấu trúc Pydantic của request body. | 500 Internal Server Error | Không đúng. | 3 | 5 | VALIDATION |
| Khi thực hiện xóa mềm (Soft Delete), API GET lấy danh sách thông thường cần bổ sung logic gì? | Không cần bổ sung gì | Sẽ hiển thị cả đối tượng đã bị xóa mềm. | Chỉ lấy các phần tử có cờ trạng thái is_deleted == False | Chính xác, lọc bỏ các đối tượng đã bị đánh dấu xóa mềm để ẩn chúng khỏi danh sách hiển thị thông thường. | Xóa sạch bộ nhớ cache | Không liên quan. | Tự động phục hồi các bản ghi đã xóa | Không đúng. | 2 | 6 | SOFT_DELETE |

— Thuộc [[Session 05 — MOC]]
