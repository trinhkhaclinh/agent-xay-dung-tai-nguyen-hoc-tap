---
type: "quiz"
title: "Session 04 — Quiz Đầu giờ"
session: 4
quiz_type: "daugio"
sheet_name: "Quiz_DauGio_FastAPI_04"
tags:
  - "type/quiz"
  - "session/04"
deliverable_filename: ""
status: "done"
---

# Session 04 — Quiz Đầu giờ

> 20 câu · lược đồ 12 cột (stage-2 ánh xạ sang .xlsx Quizizz).

| question_content | answer_1 | explanation_answer_1 | answer_2 | explanation_answer_2 | answer_3 | explanation_answer_3 | answer_4 | explanation_answer_4 | isCorrect | difficulty | category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FastAPI được xây dựng dựa trên hai thư viện chính nào? | Flask và Django | Không đúng, Flask và Django là các framework độc lập. | Tornado và Twisted | Không đúng, Tornado và Twisted là các thư viện mạng cũ. | Starlette và Pydantic | Chính xác, FastAPI là sự kết hợp của Starlette (cho web) và Pydantic (cho validate dữ liệu). | Pyramid và Bottle | Không đúng, đây là các micro-framework khác. | 3 | 4 | BÀI CŨ |
| Lệnh nào dùng để khởi động server Uvicorn cho file main.py có khai báo app = FastAPI()? | python main.py | Chỉ chạy file script Python thường, không khởi chạy uvicorn trừ khi viết code khởi động bên trong. | fastapi run main.py | Không phải lệnh chuẩn của FastAPI đời đầu. | uvicorn main:app --reload | Chính xác, uvicorn <tên_file>:<tên_biến_app> --reload để tự động tải lại code. | run uvicorn mainapp | Sai cú pháp lệnh. | 3 | 4 | BÀI CŨ |
| Để truy cập tài liệu Swagger UI tự sinh của ứng dụng FastAPI, ta dùng đường dẫn nào? | /swagger | Không đúng. | /api/docs | Không đúng. | /docs | Chính xác, FastAPI mặc định cấu hình Swagger UI tại đường dẫn /docs. | /redoc/ui | Không đúng. | 3 | 4 | BÀI CŨ |
| Kiểu kiến trúc nào phân tách hoàn toàn mã nguồn giao diện (Frontend) và xử lý dữ liệu (Backend)? | Server-Side Rendering (SSR) | SSR trộn cả giao diện và dữ liệu tại server. | Monolithic Architecture | Monolithic gộp chung toàn bộ hệ thống làm một. | Decoupled Architecture (API-first) | Chính xác, kiến trúc tách rời (decoupled) sử dụng API làm trung tâm giao tiếp. | MVC Pattern | MVC là mẫu thiết kế phần mềm, không phải kiến trúc hệ thống decoupled. | 3 | 4 | BÀI CŨ |
| Thư viện nào trong FastAPI chịu trách nhiệm kiểm tra tính hợp lệ của dữ liệu đầu vào? | Starlette | Starlette lo phần routing và web toolkit. | Pydantic | Chính xác, Pydantic lo kiểm chứng dữ liệu dựa trên Type Hints. | SQLAlchemy | SQLAlchemy là thư viện ORM làm việc với cơ sở dữ liệu. | Uvicorn | Uvicorn là máy chủ web ASGI. | 2 | 4 | BÀI CŨ |
| Chuẩn giao tiếp web ASGI viết tắt của cụm từ nào? | Asynchronous Server Gateway Interface | Chính xác, ASGI hỗ trợ xử lý bất đồng bộ trong Python web. | Advanced System Gate Integration | Không đúng. | Active Service Gateway Interface | Không đúng. | Asynchronous Socket Group Interaction | Không đúng. | 1 | 4 | BÀI CŨ |
| Trong Python, từ khóa nào đi kèm với 'await' dùng để khai báo một hàm bất đồng bộ? | def | Dùng khai báo hàm đồng bộ thường. | async | Không đi độc lập trước tên hàm. | async def | Chính xác, async def dùng để định nghĩa một coroutine hàm bất đồng bộ. | defer | Không phải từ khóa chuẩn của Python. | 3 | 4 | BÀI CŨ |
| Định dạng trao đổi dữ liệu phổ biến nhất giữa client và server trong API hiện đại là gì? | XML | Đã cũ và cồng kềnh hơn. | HTML | Dùng để hiển thị giao diện web. | JSON | Chính xác, JSON nhẹ, dễ đọc, viết dưới dạng các cặp key-value. | Plain Text | Không có cấu trúc rõ ràng. | 3 | 4 | BÀI CŨ |
| Khi tạo môi trường ảo Python trên Windows bằng lệnh python -m venv venv, thư mục chứa file kích hoạt (activate) tên là gì? | bin | Thư mục này trên hệ điều hành Linux/macOS. | Scripts | Chính xác, trên Windows đường dẫn kích hoạt là venv\Scripts\activate. | Include | Chứa các file header C/C++. | Lib | Chứa thư viện Python. | 2 | 4 | BÀI CŨ |
| Trong RESTful API, phương thức HTTP nào thường dùng để tạo mới dữ liệu? | GET | GET dùng để đọc dữ liệu. | POST | Chính xác, POST thường ánh xạ tới hành động Create. | PUT | PUT dùng để cập nhật dữ liệu. | DELETE | DELETE dùng để xóa dữ liệu. | 2 | 4 | BÀI CŨ |
| Mã trạng thái HTTP nào biểu thị việc tài nguyên yêu cầu thành công? | 200 OK | Chính xác, 200 OK dùng cho các phản hồi thành công chung. | 201 Created | Dùng khi tạo tài nguyên thành công. | 400 Bad Request | Dùng khi request bị lỗi cú pháp phía client. | 404 Not Found | Dùng khi không tìm thấy tài nguyên. | 1 | 4 | BÀI CŨ |
| Uvicorn được xây dựng dựa trên những thư viện hiệu năng cao nào? | django-admin và pip | Không liên quan. | uvloop và httptools | Chính xác, đây là các thư viện giúp Uvicorn đạt tốc độ cực lớn. | requests và urllib | Đây là các thư viện client HTTP. | flask và jinja2 | Đây là các thư viện phục vụ Flask template. | 2 | 4 | BÀI CŨ |
| Làm thế nào để chỉ ra một tham số của route là Path Parameter trong FastAPI? | Khai báo trong Query() | Query() dùng cho query parameter. | Bọc tên tham số trong ngoặc nhọn {} ở đường dẫn route | Chính xác, đường dẫn có dạng /items/{item_id} chỉ ra item_id là path parameter. | Đặt giá trị mặc định là Path() | Path() dùng để validate chứ không định nghĩa vị trí. | Khai báo trong Request Body | Request body được lấy từ JSON body. | 2 | 8 | BÀI MỚI |
| Khi nào một tham số trong hàm xử lý route được FastAPI coi là Query Parameter? | Khi nó có kiểu dữ liệu là Pydantic BaseModel | Nó sẽ được hiểu là Request Body. | Khi nó được bọc trong {} ở route path | Nó sẽ được hiểu là Path Parameter. | Khi nó có kiểu dữ liệu nguyên thủy và KHÔNG nằm trong route path | Chính xác, nếu không khai báo trong path, nó mặc định là query parameter. | Khi nó được định nghĩa trong body | Không đúng. | 3 | 8 | BÀI MỚI |
| Lớp cơ sở (Base Class) nào của Pydantic được dùng để kế thừa khi định nghĩa một Request Body Schema? | PydanticModel | Không đúng tên class. | BaseSchema | Không đúng. | BaseModel | Chính xác, từ pydantic import BaseModel. | DataModel | Không đúng. | 3 | 8 | BÀI MỚI |
| Trong FastAPI, tính chất BẮT BUỘC hay TÙY CHỌN của Query Parameter được quyết định bởi yếu tố nào? | Việc khai báo kiểu dữ liệu | Kiểu dữ liệu chỉ dùng để validate và ép kiểu. | Việc nó có giá trị mặc định hay không | Chính xác, nếu không có giá trị mặc định thì bắt buộc; ngược lại là tùy chọn. | Phương thức HTTP sử dụng | Không đúng. | Sử dụng decorator khác nhau | Không đúng. | 2 | 8 | BÀI MỚI |
| Để đặt ràng buộc 'lớn hơn hoặc bằng 1' cho một Path Parameter, ta dùng tùy chọn nào trong Path()? | gt=1 | gt là lớn hơn (Greater Than). | ge=1 | Chính xác, ge viết tắt của Greater than or Equal. | le=1 | le là nhỏ hơn hoặc bằng (Less than or Equal). | lt=1 | lt là nhỏ hơn (Less Than). | 2 | 8 | BÀI MỚI |
| Khi dữ liệu truyền lên từ client không vượt qua được bước xác thực (validate) của FastAPI, mã lỗi HTTP nào được trả về? | 400 Bad Request | Là lỗi cú pháp request nói chung. | 401 Unauthorized | Là lỗi chưa xác thực tài khoản. | 404 Not Found | Là lỗi không tìm thấy tài nguyên. | 422 Unprocessable Entity | Chính xác, 422 Unprocessable Entity là mã lỗi chuẩn mà FastAPI tự sinh khi validate thất bại. | 4 | 8 | BÀI MỚI |
| Đâu là quy tắc sắp xếp route đúng trong FastAPI để tránh xung đột đường dẫn? | Đọc ngẫu nhiên không quan trọng thứ tự | FastAPI duyệt từ trên xuống dưới nên thứ tự rất quan trọng. | Đặt route động (chứa tham số) trước route tĩnh | Nếu đặt động trước, tĩnh sẽ bị nhận nhầm và gây lỗi 422. | Đặt các route tĩnh lên trước các route động | Chính xác, luôn ưu tiên route tĩnh (vd /students/me) trước route động (vd /students/{id}). | Khai báo tất cả route trong một hàm duy nhất | Mỗi route tương ứng một hàm độc lập. | 3 | 8 | BÀI MỚI |
| Trong Pydantic model, hàm nào được dùng để đặt các ràng buộc dữ liệu cho các thuộc tính của model? | Query() | Dùng cho query parameter. | Path() | Dùng cho path parameter. | Field() | Chính xác, Field() từ pydantic dùng để đặt ràng buộc (min_length, gt...) cho thuộc tính trong BaseModel. | Validate() | Không đúng. | 3 | 8 | BÀI MỚI |

— Thuộc [[Session 04 — MOC]]
