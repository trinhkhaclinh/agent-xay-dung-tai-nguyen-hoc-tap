---
type: "quiz"
title: "Session 05 — Quiz Đầu giờ"
session: 5
quiz_type: "daugio"
sheet_name: "Quiz_DauGio_FastAPI_05"
tags:
  - "type/quiz"
  - "session/05"
deliverable_filename: ""
status: "done"
---

# Session 05 — Quiz Đầu giờ

> 20 câu · lược đồ 12 cột (stage-2 ánh xạ sang .xlsx Quizizz).

| question_content | answer_1 | explanation_answer_1 | answer_2 | explanation_answer_2 | answer_3 | explanation_answer_3 | answer_4 | explanation_answer_4 | isCorrect | difficulty | category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nếu route khai báo là /users/{id} và ta muốn id chỉ nhận giá trị lớn hơn hoặc bằng 1, ta cấu hình như thế nào? | id: int = Path(..., gt=1) | gt là lớn hơn hẳn (Greater Than). | id: int = Path(..., ge=1) | Chính xác, ge là lớn hơn hoặc bằng (Greater than or Equal) và sử dụng Path() cho path parameter. | id: int = Query(..., ge=1) | Query() dùng cho query parameter. | id: int = Field(..., ge=1) | Field() dùng cho thuộc tính trong BaseModel. | 2 | 4 | BÀI CŨ |
| Tham số nào của hàm được xem là Query Parameter mặc định trong FastAPI? | Tham số nằm trong ngoặc nhọn {} ở route decorator | Đó là Path Parameter. | Tham số kế thừa từ BaseModel của Pydantic | Đó là Request Body. | Tham số không nằm trong route path và có kiểu dữ liệu nguyên thủy (số, chuỗi, boolean) | Chính xác, FastAPI tự động phân giải các tham số này từ query string trên URL. | Tham số được khai báo trong Request Body | Không đúng. | 3 | 4 | BÀI CŨ |
| Khi validate dữ liệu thất bại, FastAPI mặc định trả về mã lỗi HTTP nào? | 400 Bad Request | Lỗi request không hợp lệ nói chung. | 404 Not Found | Lỗi không tìm thấy tài nguyên. | 500 Internal Server Error | Lỗi hệ thống phía server. | 422 Unprocessable Entity | Chính xác, mã 422 được tự động sinh kèm thông tin chi tiết lỗi. | 4 | 4 | BÀI CŨ |
| Từ khóa nào đại diện cho giá trị bắt buộc truyền khi sử dụng Path() hoặc Query()? | None | None biểu thị tham số tùy chọn. | Required | Không phải cú pháp Python. | ... (Ellipsis) | Chính xác, dấu ba chấm biểu thị giá trị bắt buộc phải có. | True | Không đúng. | 3 | 4 | BÀI CŨ |
| Trường 'loc' trong JSON lỗi 422 của FastAPI dùng để chỉ ra điều gì? | Thời gian xảy ra lỗi | Không đúng. | Vị trí của tham số gây lỗi trong request | Chính xác, loc viết tắt của Location (ví dụ: ['body', 'email'] chỉ ra email trong request body bị lỗi). | Mô tả thông điệp lỗi bằng tiếng Anh | Đó là trường msg. | Loại lỗi lập trình | Đó là trường type. | 2 | 4 | BÀI CŨ |
| Hàm Field() dùng để đặt ràng buộc dữ liệu được import từ thư viện nào? | fastapi | FastAPI cung cấp Query và Path. | starlette | Không cung cấp Field. | pydantic | Chính xác, Field() được cung cấp bởi pydantic. | typing | Cung cấp các type hint. | 3 | 4 | BÀI CŨ |
| Đâu là quy tắc vàng để tránh xung đột đường dẫn route trong FastAPI? | Khai báo route động trước, route tĩnh sau | Gây xung đột lỗi 422. | Đặt tên các route hoàn toàn giống nhau | Gây lỗi đè route. | Luôn khai báo route tĩnh lên trước các route động | Chính xác, đặt route cụ thể lên trước giúp FastAPI định tuyến chính xác. | Không được dùng quá 2 route trong ứng dụng | Không đúng. | 3 | 4 | BÀI CŨ |
| Pydantic BaseModel chủ yếu được dùng để làm gì khi khai báo ở tham số hàm POST? | Đọc dữ liệu từ Path Parameter | Không đúng. | Định nghĩa cấu trúc (schema) và đại diện cho dữ liệu nhận từ Request Body | Chính xác, giúp nhận và kiểm chứng dữ liệu JSON gửi lên từ client. | Tự động kết nối tới cơ sở dữ liệu MySQL | Đó là ORM model. | Render giao diện trang web | Không đúng. | 2 | 4 | BÀI CŨ |
| Để kiểm tra định dạng email bằng regex trong Field() của Pydantic v2, ta dùng tham số nào? | regex | Đã bị bỏ ở bản cũ. | pattern | Chính xác, pattern nhận biểu thức chính quy để kiểm tra định dạng chuỗi. | format | Không đúng. | match | Không đúng. | 2 | 4 | BÀI CŨ |
| Ý nghĩa của tham số response_model trong route decorator là gì? | Tăng tốc độ xử lý của API | Không ảnh hưởng tốc độ. | Chuẩn hóa dữ liệu đầu ra và tự động lọc bỏ các trường thông tin nhạy cảm trước khi trả về client | Chính xác, ví dụ dùng để ẩn mật khẩu người dùng trước khi phản hồi. | Tự động kết nối với MySQL | Không đúng. | Quy định kiểu dữ liệu của request body | Đó là Pydantic model trong tham số hàm. | 2 | 4 | BÀI CŨ |
| Trong Python, làm thế nào để khai báo một trường tùy chọn kiểu chuỗi có mặc định là None? | email: str | Đây là trường bắt buộc. | email: str \| None = None | Chính xác, cú pháp Union type hoặc Optional giúp biểu thị trường tùy chọn. | email: Optional | Không đúng cú pháp gán mặc định. | email: None = str | Sai cú pháp. | 2 | 4 | BÀI CŨ |
| Khi validate thành công, đối tượng Pydantic có thể chuyển đổi thành kiểu Dictionary của Python bằng phương thức nào? | to_dict() | Không đúng. | dict() | Chính xác, student.dict() (hoặc model_dump() trong Pydantic v2). | json() | Chuyển thành chuỗi JSON. | convert() | Không đúng. | 2 | 4 | BÀI CŨ |
| Trong chu trình CRUD, thao tác 'Create' thường ánh xạ tới phương thức HTTP nào? | GET | GET dùng cho Read. | POST | Chính xác, POST dùng cho Create. | PUT | PUT dùng cho Update. | DELETE | DELETE dùng cho Delete. | 2 | 8 | BÀI MỚI |
| Mã trạng thái HTTP chuẩn nhất biểu thị việc tạo mới tài nguyên thành công là gì? | 200 OK | Dùng cho các thao tác thành công chung. | 201 Created | Chính xác, 201 Created. | 204 No Content | Dùng khi thành công nhưng không có nội dung trả về. | 400 Bad Request | Dùng khi request bị lỗi cú pháp. | 2 | 8 | BÀI MỚI |
| Phương thức HTTP nào được thiết kế để ghi đè toàn bộ thông tin của tài nguyên đang tồn tại? | POST | Dùng để tạo mới. | PATCH | Dùng để cập nhật từng phần. | PUT | Chính xác, PUT ghi đè toàn bộ tài nguyên. | GET | Dùng để đọc. | 3 | 8 | BÀI MỚI |
| Nếu xóa tài nguyên thành công và server không muốn gửi lại bất kỳ dữ liệu nào trong body, mã HTTP phản hồi là gì? | 200 OK | Trả về dữ liệu kèm body. | 201 Created | Dùng cho tạo mới. | 204 No Content | Chính xác, 204 No Content biểu thị thành công và body trống. | 404 Not Found | Không tìm thấy tài nguyên. | 3 | 8 | BÀI MỚI |
| Tính chất 'Idempotent' của một phương thức HTTP có nghĩa là gì? | Phương thức đó chạy rất nhanh | Không đúng. | Thực hiện gọi API nhiều lần liên tiếp với cùng dữ liệu luôn cho kết quả trạng thái hệ thống giống nhau | Chính xác, ví dụ gọi PUT sửa thông tin hoặc DELETE xóa đối tượng nhiều lần thì kết quả cuối cùng đối tượng vẫn chỉ bị sửa/xóa như vậy. | Yêu cầu phải có mật khẩu xác thực | Không đúng. | Không cho phép truyền tham số | Không đúng. | 2 | 8 | BÀI MỚI |
| Cơ chế 'Soft Delete' (Xóa mềm) hoạt động như thế nào trong thực tế? | Xóa hoàn toàn dữ liệu khỏi RAM | Đó là xóa vật lý. | Chỉ xóa dữ liệu khi máy tính tắt | Không đúng. | Thay đổi trạng thái của cờ đánh dấu (ví dụ is_deleted = True) thay vì xóa vật lý khỏi database | Chính xác, giúp bảo toàn tính toàn vẹn dữ liệu và lưu lịch sử. | Tự động gửi email thông báo cho người dùng khi xóa | Không đúng. | 3 | 8 | BÀI MỚI |
| Để ném ra lỗi không tìm thấy tài nguyên khi client gọi GET hoặc DELETE sai ID, ta dùng cú pháp nào? | raise HTTPException(status_code=400, detail='...') | 400 là Bad Request. | raise HTTPException(status_code=404, detail='...') | Chính xác, mã 404 biểu thị Not Found. | return {'error': 'Not Found'} | Chỉ trả về dict thường, mã HTTP phản hồi vẫn là 200 OK. | sys.exit(1) | Dừng ứng dụng server lập tức, gây crash. | 2 | 8 | BÀI MỚI |
| Sự khác biệt lớn nhất giữa PUT và PATCH là gì? | PUT chạy nhanh hơn PATCH | Hiệu năng tương đương. | PUT ghi đè toàn bộ thuộc tính; PATCH chỉ cập nhật các thuộc tính được truyền lên (cập nhật từng phần) | Chính xác, đây là quy chuẩn thiết kế RESTful. | PATCH là phương thức an toàn (safe), PUT thì không | Cả hai đều là update không safe. | FastAPI không hỗ trợ PATCH, chỉ hỗ trợ PUT | FastAPI hỗ trợ đầy đủ các phương thức. | 2 | 8 | BÀI MỚI |

— Thuộc [[Session 05 — MOC]]
