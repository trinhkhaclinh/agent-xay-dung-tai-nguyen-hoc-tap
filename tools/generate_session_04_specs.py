# -*- coding: utf-8 -*-
"""Script to programmatically generate all 17 spec JSON files for Session 04.
"""
import os
import json

SPEC_DIR = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap\output\Session 04 - Parameters, Request body & Pydantic Validation\_spec"

def write_json(name, data):
    path = os.path.join(SPEC_DIR, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Generated {name}")

def main():
    # ------------------ READING 01: Path Parameters ------------------
    reading_01 = {
        "filename": "BÀI ĐỌC_ PATH PARAMETERS TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: Path Parameters - Định Danh Và Lấy Dữ Liệu Từ URL" },
            { "type": "p", "text": "Trong kiến trúc RESTful API, tài nguyên hệ thống được định danh thông qua đường dẫn URL. Khi chúng ta muốn thao tác trên một tài nguyên cụ thể (ví dụ: lấy thông tin của sinh viên có mã số 123), chúng ta cần truyền định danh đó vào URL. Trong FastAPI, cơ chế giúp chúng ta lấy phần biến động này từ URL được gọi là Path Parameters. Bài đọc này sẽ hướng dẫn chi tiết cách khai báo, ép kiểu dữ liệu và xử lý xung đột đường dẫn khi làm việc với Path Parameters." },
            { "type": "h2", "text": "1. Khái niệm và Cách hoạt động của Path Parameters" },
            { "type": "p", "text": "Path parameters (tham số đường dẫn) là các phần biến động nằm trực tiếp trong URL, được dùng để xác định tài nguyên cụ thể mà client muốn truy cập. Khác với query parameters (dùng cho tìm kiếm/lọc), path parameter đóng vai trò định vị tài nguyên độc bản." },
            { "type": "p", "text": "Hãy tưởng tượng một tòa nhà ký túc xá. Địa chỉ chung là 'Ký túc xá A'. Nếu muốn tìm đúng phòng của một sinh viên, chúng ta cần số phòng cụ thể: 'Ký túc xá A / Phòng 402'. Ở đây, '402' chính là tham số đường dẫn để chỉ định căn phòng duy nhất. Tương tự, trong ứng dụng quản lý đào tạo, URL '/students/123' cho biết chúng ta đang muốn tương tác với sinh viên có mã số là 123." },
            { "type": "h2", "text": "2. Khai báo Path Parameters trong FastAPI" },
            { "type": "p", "text": "Để khai báo một path parameter trong FastAPI, chúng ta sử dụng dấu ngoặc nhọn `{}` trong đường dẫn của route decorator. Đồng thời, hàm xử lý bên dưới phải nhận một tham số có tên trùng khớp chính xác với tên tham số nằm trong dấu ngoặc nhọn." },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\n\napp = FastAPI()\n\n# 1. Khai báo path parameter '{student_id}' trong route\n@app.get(\"/students/{student_id}\")\ndef get_student_detail(student_id: int): # 2. Khai báo tham số hàm trùng tên và có type hint\n    # student_id đã được FastAPI tự động ép sang kiểu dữ liệu int\n    return {\n        \"student_id\": student_id,\n        \"name\": \"Nguyen Van An\",\n        \"email\": \"an.nv@gmail.com\",\n        \"status\": \"Active\"\n    }" },
            { "type": "p", "text": "Trong ví dụ trên, khi client gửi yêu cầu đến GET `/students/123`, FastAPI sẽ trích xuất giá trị '123' từ URL, tự động chuyển đổi nó sang kiểu số nguyên `int` và truyền vào hàm `get_student_detail` dưới dạng tham số `student_id`." },
            { "type": "h2", "text": "3. Ép kiểu và Tự động Validate dữ liệu (Lỗi 422)" },
            { "type": "p", "text": "Một thế mạnh cực lớn của FastAPI là khả năng tự động kiểm tra (validate) kiểu dữ liệu dựa trên Type Hints của Python. Khi chúng ta khai báo `student_id: int`, FastAPI hiểu rằng tham số này bắt buộc phải là số nguyên." },
            { "type": "p", "text": "Nếu client gửi request hợp lệ như GET `/students/123`, hệ thống trả về kết quả 200 OK. Tuy nhiên, nếu client gửi request sai kiểu như GET `/students/abc` (trong đó 'abc' không thể chuyển đổi sang số nguyên), FastAPI sẽ ngay lập tức chặn lại và trả về mã trạng thái HTTP 422 (Unprocessable Entity) kèm thông báo lỗi chi tiết dạng JSON mà chúng ta không cần viết thêm bất kỳ dòng code kiểm tra nào." },
            { "type": "code", "lang": "json", "text": "{\n  \"detail\": [\n    {\n      \"loc\": [\"path\", \"student_id\"],\n      \"msg\": \"value is not a valid integer\",\n      \"type\": \"type_error.integer\"\n    }\n  ]\n}" },
            { "type": "p", "text": "Cơ chế này giúp loại bỏ hoàn toàn các lỗi runtime do sai kiểu dữ liệu bên trong logic xử lý của ứng dụng, làm cho backend của chúng ta cực kỳ an toàn và ổn định." },
            { "type": "h2", "text": "4. Thứ tự khai báo Route và tránh xung đột" },
            { "type": "p", "text": "Khi khai báo nhiều route có cấu trúc đường dẫn tương tự nhau, thứ tự khai báo trong code là cực kỳ quan trọng. FastAPI phân giải các route theo thứ tự từ trên xuống dưới." },
            { "type": "p", "text": "Giả sử chúng ta muốn có một route tĩnh là `/students/me` để lấy thông tin của chính sinh viên đang đăng nhập, và một route động `/students/{student_id}` để lấy thông tin sinh viên bất kỳ. Nếu chúng ta đặt route động `/students/{student_id}` phía TRƯỚC route tĩnh, khi client gọi GET `/students/me`, FastAPI sẽ khớp chuỗi 'me' vào tham số động `{student_id}`, cố gắng ép kiểu 'me' sang `int` và trả về lỗi 422." },
            { "type": "p", "text": "Do đó, quy tắc vàng là: **Luôn đặt các route tĩnh (cụ thể) lên TRƯỚC các route động (chứa tham số).**" },
            { "type": "code", "lang": "python", "text": "# ĐÚNG: Route tĩnh đặt trước\n@app.get(\"/students/me\")\ndef get_my_profile():\n    return {\"student_id\": 999, \"name\": \"Sinh viên hiện tại (Tôi)\"}\n\n# Route động đặt sau\n@app.get(\"/students/{student_id}\")\ndef get_student_by_id(student_id: int):\n    return {\"student_id\": student_id, \"message\": f\"Thông tin chi tiết sinh viên {student_id}\"}" },
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Path parameters là các tham số biến động nằm trong URL dùng để định danh duy nhất một tài nguyên.",
                "FastAPI sử dụng Type Hints để tự động ép kiểu và validate dữ liệu của path parameter.",
                "Nếu truyền sai kiểu dữ liệu yêu cầu, FastAPI tự động trả về lỗi HTTP 422 Unprocessable Entity kèm mô tả chi tiết vị trí lỗi.",
                "Thứ tự khai báo route trong FastAPI rất quan trọng: Luôn đặt các route cụ thể (tĩnh) lên phía trước các route động chứa tham số để tránh xung đột đường dẫn."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "FastAPI Official Documentation - Path Parameters: https://fastapi.tiangolo.com/tutorial/path-params/",
                "Python Type Hints Tutorial: https://docs.python.org/3/library/typing.html"
            ]}
        ]
    }
    write_json("reading_01.json", reading_01)

    # ------------------ READING 02: Query Parameters ------------------
    reading_02 = {
        "filename": "BÀI ĐỌC_ QUERY PARAMETERS TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: Query Parameters - Lọc, Tìm Kiếm Và Quản Lý Tham Số Tùy Chọn" },
            { "type": "p", "text": "Khi thiết kế API, không phải lúc nào chúng ta cũng chỉ lấy một tài nguyên cụ thể qua ID. Thông thường, client cần tìm kiếm, lọc danh sách, hoặc phân trang dữ liệu (ví dụ: lấy danh sách khóa học có từ khóa 'Python', thuộc cấp độ 'beginner'). Để thực hiện việc này mà không làm thay đổi cấu trúc URL chính, chúng ta sử dụng Query Parameters. Bài đọc này giúp chúng ta làm chủ cách nhận diện, khai báo các tham số bắt buộc và tùy chọn trong FastAPI." },
            { "type": "h2", "text": "1. Khái niệm Query Parameters và điểm khác biệt với Path Parameters" },
            { "type": "p", "text": "Query parameters (tham số truy vấn) là các cặp khóa - giá trị nằm ở sau dấu hỏi chấm `?` trên đường dẫn URL, và nối với nhau bằng dấu và `&`. Ví dụ: `/courses?keyword=python&level=beginner`." },
            { "type": "p", "text": "Điểm khác biệt cốt lõi: Path parameter dùng để định vị một tài nguyên cụ thể, mang tính bắt buộc. Trong khi đó, Query parameter dùng để thay đổi cách hiển thị tài nguyên (lọc, sắp xếp, tìm kiếm, phân trang) và thường mang tính tùy chọn." },
            { "type": "h2", "text": "2. Khai báo Query Parameters trong FastAPI" },
            { "type": "p", "text": "Trong FastAPI, bất kỳ tham số nào của hàm xử lý route mà **KHÔNG** nằm trong khai báo đường dẫn của route decorator sẽ tự động được hiểu là một Query Parameter." },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\n\napp = FastAPI()\n\ncourses_db = [\n    {\"id\": 1, \"name\": \"Lập trình Python cơ bản\", \"level\": \"beginner\", \"price\": 1200000},\n    {\"id\": 2, \"name\": \"Xây dựng Web API với FastAPI\", \"level\": \"intermediate\", \"price\": 2000000},\n    {\"id\": 3, \"name\": \"Lập trình Python nâng cao\", \"level\": \"advanced\", \"price\": 3000000},\n]\n\n# Tham số 'keyword' và 'level' không nằm trong đường dẫn '/courses'\n@app.get(\"/courses\")\ndef filter_courses(keyword: str = \"\", level: str | None = None):\n    results = courses_db\n    if keyword:\n        results = [c for c in results if keyword.lower() in c[\"name\"].lower()]\n    if level:\n        results = [c for c in results if c[\"level\"] == level]\n    return results" },
            { "type": "p", "text": "Khi client gọi URL `/courses?keyword=python&level=beginner`, FastAPI sẽ trích xuất `keyword='python'` và `level='beginner'` để truyền vào hàm `filter_courses`." },
            { "type": "h2", "text": "3. Tham số Bắt buộc (Required) vs Tùy chọn (Optional)" },
            { "type": "p", "text": "Trong FastAPI, tính chất bắt buộc hay tùy chọn của một query parameter được quyết định bởi việc tham số đó có **giá trị mặc định** hay không:" },
            { "type": "bullets", "items": [
                "**Tham số tùy chọn (Optional):** Có giá trị mặc định (ví dụ: `keyword: str = \"\"` hoặc `level: str | None = None`). Nếu client không truyền tham số này trên URL, hàm vẫn chạy và nhận giá trị mặc định.",
                "**Tham số bắt buộc (Required):** Không khai báo giá trị mặc định (ví dụ: `api_key: str`). Nếu client không truyền tham số này trên URL (ví dụ gọi trơn `/courses`), FastAPI sẽ lập tức chặn lại và trả về lỗi 422 kèm thông báo thiếu tham số bắt buộc."
            ]},
            { "type": "code", "lang": "python", "text": "# Định nghĩa kết hợp tham số bắt buộc và tùy chọn\n@app.get(\"/services\")\ndef get_services(\n    service_type: str,            # Bắt buộc (không có giá trị mặc định)\n    limit: int = 10,              # Tùy chọn (mặc định là 10)\n    keyword: str | None = None    # Tùy chọn (mặc định là None)\n):\n    return {\"type\": service_type, \"limit\": limit, \"keyword\": keyword}" },
            { "type": "h2", "text": "4. Ép kiểu dữ liệu thông minh với kiểu Boolean" },
            { "type": "p", "text": "FastAPI hỗ trợ ép kiểu dữ liệu thông minh cho các query parameter kiểu logic (`bool`). Khi khai báo một query parameter có kiểu `bool`, FastAPI nhận diện rất nhiều giá trị chuỗi khác nhau từ URL và tự động chuyển về đúng giá trị logic của Python:" },
            { "type": "bullets", "items": [
                "Giá trị là `true`, `1`, `yes`, `on` hoặc `True` -> chuyển thành `True` trong Python.",
                "Giá trị là `false`, `0`, `no`, `off` hoặc `False` -> chuyển thành `False` trong Python."
            ]},
            { "type": "code", "lang": "python", "text": "@app.get(\"/items\")\ndef read_items(is_active: bool = True):\n    # Truy cập /items?is_active=false -> is_active = False\n    # Truy cập /items?is_active=1 -> is_active = True\n    return {\"is_active\": is_active}" },
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Query parameters là các tham số nằm sau dấu '?' trên URL dùng để lọc, tìm kiếm hoặc phân trang dữ liệu.",
                "Tham số không nằm trong route path thì tự động được xem là query parameter.",
                "Query parameter có giá trị mặc định là tùy chọn; không có giá trị mặc định là bắt buộc.",
                "FastAPI hỗ trợ ép kiểu tự động cho kiểu dữ liệu số, chuỗi, và đặc biệt là cơ chế phân giải kiểu bool linh hoạt từ URL."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "FastAPI Official Documentation - Query Parameters: https://fastapi.tiangolo.com/tutorial/query-params/"
            ]}
        ]
    }
    write_json("reading_02.json", reading_02)

    # ------------------ READING 03: Request Body with Pydantic ------------------
    reading_03 = {
        "filename": "BÀI ĐỌC_ REQUEST BODY VỚI PYDANTIC_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: Request Body - Nhận Và Kiểm Chứng Dữ Liệu JSON Bằng Pydantic Model" },
            { "type": "p", "text": "Khi client muốn tạo mới hoặc cập nhật một tài nguyên lớn (ví dụ: đăng ký tài khoản sinh viên mới gồm họ tên, email, ngày sinh, mật khẩu), việc gửi dữ liệu qua URL là không an toàn và bị giới hạn độ dài. Thay vào đó, dữ liệu được đóng gói trong phần thân của yêu cầu (Request Body) dưới định dạng JSON. Trong FastAPI, chúng ta sử dụng Pydantic để định nghĩa cấu trúc dữ liệu mong muốn (Schema) và tự động xác thực toàn bộ dữ liệu JSON này." },
            { "type": "h2", "text": "1. Khái niệm Request Body và vai trò của Pydantic BaseModel" },
            { "type": "p", "text": "Request Body là phần thân chứa dữ liệu của HTTP request (thường đi với POST, PUT, PATCH). Để nhận diện và kiểm chứng cấu trúc của dữ liệu JSON gửi lên từ client, FastAPI tích hợp chặt chẽ với Pydantic - một thư viện xác thực dữ liệu hàng đầu trong Python." },
            { "type": "p", "text": "Pydantic giúp chúng ta định nghĩa một class kế thừa từ `BaseModel`. Mỗi thuộc tính khai báo trong class này đại diện cho một trường thông tin mà chúng ta yêu cầu client phải gửi lên, kèm theo kiểu dữ liệu mong muốn của trường đó." },
            { "type": "h2", "text": "2. Triển khai Request Body với Pydantic trong FastAPI" },
            { "type": "p", "text": "Để nhận request body, đầu tiên ta định nghĩa lớp kế thừa `BaseModel`. Sau đó khai báo tham số hàm route có kiểu dữ liệu là lớp vừa định nghĩa." },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\n# 1. Định nghĩa Schema (cấu trúc dữ liệu mong muốn)\nclass StudentCreate(BaseModel):\n    name: str\n    email: str\n    age: int\n    is_enrolled: bool = True # Trường tùy chọn có giá trị mặc định\n\n# 2. Áp dụng schema vào route xử lý POST\n@app.post(\"/students\")\ndef create_student(student: StudentCreate): \n    # FastAPI tự động đọc JSON từ Request Body, validate cấu trúc,\n    # và chuyển đổi thành một đối tượng student kiểu StudentCreate.\n    student_dict = student.dict()\n    # Thao tác xử lý dữ liệu (ví dụ lưu vào DB)\n    student_dict[\"id\"] = 101 \n    return {\n        \"message\": \"Tạo sinh viên thành công\",\n        \"student\": student_dict\n    }" },
            { "type": "p", "text": "Khi client gửi một POST request đến `/students` với body JSON:\n`{\"name\": \"Nguyen Van An\", \"email\": \"an.nv@gmail.com\", \"age\": 20}`\nFastAPI sẽ kiểm tra tính hợp lệ và truyền đối tượng `student` đã được xác thực vào hàm. Chúng ta có thể truy cập thuộc tính bằng cú pháp hướng đối tượng `student.name` hoặc chuyển thành dict bằng `student.dict()`." },
            { "type": "h2", "text": "3. Tự động kiểm chứng JSON và xử lý lỗi 422" },
            { "type": "p", "text": "Nếu client gửi một JSON không đúng cấu trúc đã định nghĩa, ví dụ: thiếu trường `name` bắt buộc, hoặc truyền trường `age` dưới dạng chuỗi chữ không thể ép kiểu (ví dụ `\"twenty\"`), FastAPI sẽ tự động chặn request lại và trả về lỗi 422 Unprocessable Entity kèm theo thông tin chi tiết chính xác lỗi xảy ra ở đâu, thuộc loại nào." },
            { "type": "p", "text": "Nhờ đó, lập trình viên không phải viết hàng chục dòng code `if/else` để kiểm tra sự tồn tại và tính hợp lệ của từng trường dữ liệu, giúp code backend ngắn gọn, sạch sẽ và an toàn hơn." },
            { "type": "h2", "text": "4. Lợi ích của response_model và Pydantic lồng nhau" },
            { "type": "p", "text": "Pydantic còn hỗ trợ mô tả các cấu trúc dữ liệu phức tạp (lồng nhau) và kiểm soát dữ liệu trả về thông qua `response_model`:" },
            { "type": "bullets", "items": [
                "**Pydantic model lồng nhau:** Một thuộc tính trong model có thể có kiểu dữ liệu là một model khác (ví dụ: trường `address` có kiểu dữ liệu là model `AddressSchema` gồm tỉnh/thành phố, quận/huyện).",
                "**response_model:** Khai báo trong decorator (ví dụ `@app.post('/students', response_model=StudentOut)`), giúp lọc bớt dữ liệu nhạy cảm trước khi trả về cho client (ví dụ ẩn mật khẩu sinh viên hoặc ngày tạo) và đảm bảo cấu trúc response trả về chuẩn hóa."
            ]},
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Request body dùng để truyền tải dữ liệu có cấu trúc lớn và phức tạp dưới dạng JSON trong thân HTTP request.",
                "FastAPI sử dụng Pydantic BaseModel để định nghĩa cấu trúc (schema) dữ liệu.",
                "FastAPI tự động validate toàn bộ dữ liệu body JSON gửi lên và trả về lỗi 422 nếu dữ liệu không khớp với schema.",
                "Pydantic hỗ trợ các cấu trúc dữ liệu lồng nhau và giúp chuẩn hóa đầu ra của API qua tham số response_model."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "FastAPI Official Documentation - Request Body: https://fastapi.tiangolo.com/tutorial/body/",
                "Pydantic Official Documentation: https://docs.pydantic.dev/"
            ]}
        ]
    }
    write_json("reading_03.json", reading_03)

    # ------------------ READING 04: Type Hints in FastAPI ------------------
    reading_04 = {
        "filename": "BÀI ĐỌC_ TYPE HINTS TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: Ràng Buộc Dữ Liệu Nâng Cao Bằng Type Hints Và Thư Viện FastAPI" },
            { "type": "p", "text": "Xác định kiểu dữ liệu (như số hay chuỗi) là chưa đủ đối với một hệ thống thực tế. Chúng ta cần những ràng buộc chặt chẽ hơn: từ khóa tìm kiếm phải có độ dài từ 2 đến 50 ký tự; số trang phải lớn hơn hoặc bằng 1; giá sản phẩm phải lớn hơn 0; hay mã số sinh viên phải tuân theo một định dạng nhất định. FastAPI cung cấp các công cụ đắc lực như `Path()`, `Query()`, và `Field()` tích hợp trực tiếp vào hệ thống Type Hints để khai báo các ràng buộc dữ liệu này một cách trực quan nhất. Bài đọc này giúp chúng ta làm chủ kỹ năng này." },
            { "type": "h2", "text": "1. Vai trò của Type Hints làm nền tảng cho validation tự động" },
            { "type": "p", "text": "Type hints trong Python ban đầu sinh ra chỉ để phục vụ cho việc nhắc mã nguồn và kiểm tra tĩnh. Tuy nhiên, FastAPI và Pydantic đã tận dụng tối đa sức mạnh của nó để thực hiện kiểm chứng dữ liệu động khi runtime. Không có type hints, FastAPI không thể biết cách ép kiểu và validate dữ liệu." },
            { "type": "h2", "text": "2. Sử dụng Query() để validate Query Parameters" },
            { "type": "p", "text": "Để thêm các ràng buộc validation (độ dài chuỗi, biểu thức chính quy, mô tả hiển thị trên Swagger) cho query parameter, chúng ta sử dụng hàm `Query()` từ thư viện `fastapi` làm giá trị mặc định của tham số." },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI, Query\n\napp = FastAPI()\n\n@app.get(\"/products\")\ndef search_products(\n    keyword: str = Query(\n        None, \n        min_length=2, \n        max_length=50, \n        description=\"Từ khóa tìm kiếm sản phẩm\"\n    ),\n    page: int = Query(1, ge=1, description=\"Số trang, tối thiểu là 1\")\n):\n    return {\"keyword\": keyword, \"page\": page}" },
            { "type": "p", "text": "Trong đoạn code trên:\n- `min_length=2`: từ khóa tìm kiếm phải có ít nhất 2 ký tự.\n- `max_length=50`: tối đa 50 ký tự.\n- `ge=1` (Greater than or Equal): số trang phải lớn hơn hoặc bằng 1. Nếu client vi phạm, FastAPI lập tức trả lỗi 422." },
            { "type": "h2", "text": "3. Sử dụng Path() để validate Path Parameters" },
            { "type": "p", "text": "Tương tự như `Query()`, chúng ta sử dụng `Path()` để đặt các ràng buộc cho path parameter. Tuy nhiên, vì path parameter luôn luôn là bắt buộc, đối số đầu tiên truyền vào `Path()` phải là dấu ba chấm `...` (biểu thị required)." },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI, Path\n\napp = FastAPI()\n\n@app.get(\"/students/{student_id}\")\ndef get_student(\n    student_id: int = Path(..., ge=1, le=1000, description=\"Mã ID sinh viên, từ 1 đến 1000\")\n):\n    return {\"student_id\": student_id}" },
            { "type": "p", "text": "Nếu client gọi `/students/0` hoặc `/students/1500`, yêu cầu sẽ bị chặn lại ngay lập tức do vi phạm ràng buộc số học `ge=1` và `le=1000`." },
            { "type": "h2", "text": "4. Sử dụng Field() để validate thuộc tính Pydantic Model" },
            { "type": "p", "text": "Để áp dụng validation bên trong Pydantic model (request body), chúng ta dùng hàm `Field()` từ thư viện `pydantic`. Các đối số ràng buộc của `Field()` hoàn toàn tương đồng với `Query()` và `Path()`." },
            { "type": "code", "lang": "python", "text": "from pydantic import BaseModel, Field\n\nclass StudentCreateSchema(BaseModel):\n    name: str = Field(..., min_length=2, max_length=100, description=\"Họ và tên sinh viên\")\n    email: str = Field(..., pattern=r\"^\\S+@\\S+\\.\\S+$\", description=\"Email đúng định dạng\")\n    age: int = Field(..., gt=18, lt=100, description=\"Tuổi phải từ 19 đến 99\")\n    gpa: float = Field(0.0, ge=0.0, le=4.0, description=\"GPA hệ 4, từ 0 đến 4.0\")" },
            { "type": "p", "text": "Lưu ý:\n- Đối số đầu tiên `...` chỉ ra rằng thuộc tính đó là bắt buộc phải truyền.\n- `pattern`: Sử dụng regex (biểu thức chính quy) để kiểm tra định dạng email.\n- `gt=18` (Greater Than): lớn hơn 18 tuổi.\n- `lt=100` (Less Than): nhỏ hơn 100 tuổi." },
            { "type": "h2", "text": "5. Phân tích cấu trúc lỗi 422 (Unprocessable Entity)" },
            { "type": "p", "text": "Khi một ràng buộc bị vi phạm, FastAPI trả về mã lỗi 422 kèm cấu trúc JSON lỗi chuẩn hóa. Dưới đây là phân tích chi tiết cấu trúc này:" },
            { "type": "bullets", "items": [
                "`loc` (Location): Vị trí xảy ra lỗi, ví dụ `[\"body\", \"age\"]` chỉ ra lỗi nằm trong request body ở trường age; hoặc `[\"query\", \"keyword\"]` chỉ ra lỗi nằm ở query parameter keyword trên URL.",
                "`msg` (Message): Mô tả chi tiết về lỗi xảy ra (ví dụ: 'ensure this value is greater than 18').",
                "`type` (Type): Mã loại lỗi để lập trình viên frontend có thể bắt lỗi tự động (ví dụ `value_error.number.not_gt`)."
            ]},
            { "type": "p", "text": "Hiểu rõ cấu trúc này giúp các nhà phát triển frontend dễ dàng bắt lỗi và hiển thị cảnh báo đỏ trên giao diện người dùng một cách chính xác nhất." },
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "FastAPI tích hợp Type Hints để khai báo validation cực kỳ tường minh.",
                "Dùng Query() để validate query parameter, Path() để validate path parameter và Field() để validate Pydantic model.",
                "Các ràng buộc bao gồm: độ dài chuỗi (min_length, max_length), khoảng số học (ge, le, gt, lt), regex pattern.",
                "Lỗi 422 chứa thông tin chi tiết về vị trí (loc), thông điệp (msg), và loại lỗi (type), giúp lập trình viên dễ dàng debug."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "FastAPI Query Parameters and String Validations: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/",
                "FastAPI Path Parameters and Numeric Validations: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/"
            ]}
        ]
    }
    write_json("reading_04.json", reading_04)

    # ------------------ VIDEO SCRIPTS ------------------
    # Video 01
    video_01 = {
        "filename": "Lesson 01 - Path Parameters - Lấy dữ liệu từ URL",
        "subdir": "Kịch bản quay video",
        "lesson_no": 1,
        "blocks": [
            { "type": "h2", "text": "## Giới thiệu về Path Parameters" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về một khái niệm rất quan trọng trong thiết kế và xây dựng API - đó chính là Path Parameters, hay còn gọi là tham số đường dẫn." },
            { "type": "narration", "text": "Hãy cùng nhìn lên sơ đồ kiến trúc URL trên màn hình. Mỗi tài nguyên trong hệ thống đều cần một định danh duy nhất. Khi các em muốn truy xuất thông tin cụ thể của một sinh viên nào đó, các em không thể gọi chung chung là đường dẫn học sinh được. Chúng ta cần một mã số định danh cụ thể, ví dụ như mã số 123. Phần thay đổi này nằm trực tiếp trong đường dẫn và đó chính là Path Parameter." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Cách khai báo Path Parameter trong FastAPI" },
            { "type": "narration", "text": "Bây giờ, chúng ta sẽ mở công cụ soạn thảo mã nguồn VS Code lên để xem cách khai báo trong code FastAPI nhé. Trong FastAPI, các em chỉ cần bọc tên biến trong cặp dấu ngoặc nhọn ở đường dẫn của route decorator. Đồng thời, các em khai báo tên tham số đó trong hàm xử lý bên dưới." },
            { "type": "marker", "text": "[mở trình duyệt và hiển thị code FastAPI]" },
            { "type": "narration", "text": "Như các em thấy trên màn hình, khi chúng ta đặt student_id có kiểu dữ liệu là int, FastAPI sẽ thực hiện hai việc. Một là ép kiểu chuỗi nhận từ URL sang kiểu int. Hai là tự động kiểm chứng dữ liệu. Nếu người dùng truyền vào chữ thay vì số, FastAPI sẽ trả về lỗi HTTP 422." },
            { "type": "marker", "text": "[mở công cụ Postman và thực hiện demo gọi API /students/abc]" },
            { "type": "narration", "text": "Khi thầy gửi request với tham số abc, các em sẽ thấy ngay mã lỗi 422 Unprocessable Entity hiển thị dưới dạng JSON. Đây chính là tính năng tự động validate cực kỳ mạnh mẽ của FastAPI." },
            { "type": "h2", "text": "## Thứ tự khai báo route để tránh xung đột" },
            { "type": "narration", "text": "Một lưu ý cực kỳ quan trọng mà các em cần nhớ: đó là thứ tự khai báo route. Vì FastAPI phân giải đường dẫn từ trên xuống dưới, các em luôn phải đặt route tĩnh ví dụ như /students/me lên trước route động là /students/student_id. Nếu không, route tĩnh sẽ bị nhận nhầm là một giá trị của route động." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Như vậy là trong bài học này, thầy đã hướng dẫn các em hiểu rõ cách hoạt động của Path Parameter, cách khai báo và thứ tự sắp xếp route để tránh xung đột đường dẫn. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em trong bài học tiếp theo nhé!" }
        ]
    }
    write_json("video_01.json", video_01)

    # Video 02
    video_02 = {
        "filename": "Lesson 02 - Query Parameters - Nhận tham số tìm kiếm",
        "subdir": "Kịch bản quay video",
        "lesson_no": 2,
        "blocks": [
            { "type": "h2", "text": "## Tìm hiểu về Query Parameters" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học này, thầy và các em sẽ cùng nhau nghiên cứu về Query Parameters - tham số truy vấn." },
            { "type": "narration", "text": "Khác với Path Parameter dùng để định vị một đối tượng cụ thể, Query Parameter dùng để lọc, sắp xếp, tìm kiếm hoặc phân trang dữ liệu. Chúng xuất hiện sau dấu hỏi chấm trên URL và được phân tách bởi dấu và." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Khai báo Query Parameter trong FastAPI" },
            { "type": "narration", "text": "Bây giờ, chúng ta hãy xem cách khai báo trong FastAPI. Các em hãy chú ý: bất kỳ tham số nào của hàm xử lý route mà KHÔNG nằm trong route decorator sẽ mặc định được FastAPI hiểu là Query Parameter." },
            { "type": "marker", "text": "[mở trình duyệt và hiển thị code API tìm kiếm khóa học]" },
            { "type": "narration", "text": "Ở đây, thầy khai báo keyword kiểu str với giá trị mặc định là chuỗi rỗng và level kiểu str hoặc None với mặc định là None. Do có giá trị mặc định, các tham số này trở thành tham số tùy chọn. Nếu client không truyền, ứng dụng vẫn chạy bình thường. Còn nếu các em bỏ giá trị mặc định đi, tham số đó sẽ trở thành bắt buộc." },
            { "type": "marker", "text": "[mở công cụ Postman gửi request /courses?keyword=python]" },
            { "type": "narration", "text": "Khi thầy gửi request này, các em thấy server trả về đúng các khóa học có chứa chữ python trong tên. Và đặc biệt, FastAPI còn tự động ép kiểu boolean cực kỳ thông minh khi các em truyền true, false, 1, 0 từ URL." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Qua bài học hôm nay, các em đã nắm vững cách khai báo và sử dụng Query Parameter để lọc dữ liệu, cũng như phân biệt được tham số bắt buộc và tùy chọn. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở bài học tiếp theo!" }
        ]
    }
    write_json("video_02.json", video_02)

    # Video 03
    video_03 = {
        "filename": "Lesson 03 - Request Body với Pydantic - Nhận dữ liệu JSON",
        "subdir": "Kịch bản quay video",
        "lesson_no": 3,
        "blocks": [
            { "type": "h2", "text": "## Giới thiệu về Request Body và Pydantic" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Hôm nay, thầy và các em sẽ cùng tìm hiểu về cách truyền dữ liệu lớn và phức tạp vào server bằng Request Body sử dụng thư viện Pydantic." },
            { "type": "narration", "text": "Khi các em muốn đăng ký một sinh viên mới hay thêm một khóa học mới, thông tin gửi lên rất nhiều. Việc truyền qua URL là không khả thi. Chúng ta sẽ đóng gói dữ liệu dưới dạng JSON và đặt trong Request Body." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Tạo Pydantic BaseModel để kiểm chứng dữ liệu" },
            { "type": "narration", "text": "Để FastAPI hiểu được cấu trúc JSON gửi lên, chúng ta sẽ định nghĩa một lớp kế thừa từ Pydantic BaseModel. Hãy cùng nhìn lên màn hình." },
            { "type": "marker", "text": "[mở trình duyệt hiển thị code định nghĩa class StudentCreate]" },
            { "type": "narration", "text": "Chúng ta khai báo các thuộc tính name, email kiểu str và age kiểu int. Khi áp dụng class này làm kiểu dữ liệu cho tham số của route xử lý POST, FastAPI sẽ tự động phân giải JSON từ request body và validate. Nếu dữ liệu gửi lên bị thiếu trường bắt buộc hoặc sai kiểu dữ liệu, FastAPI lập tức trả lỗi 422 mà các em không cần tự viết code validation." },
            { "type": "marker", "text": "[mở Postman thực hiện demo POST /students với body JSON hợp lệ và không hợp lệ]" },
            { "type": "narration", "text": "Như các em thấy, khi thầy truyền thiếu trường name, API lập tức phản hồi mã trạng thái 422 kèm mô tả rõ ràng lỗi thiếu trường name. Điều này giúp code backend của chúng ta cực kỳ an toàn." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Tóm lại, trong bài học này các em đã biết cách sử dụng Pydantic BaseModel để định nghĩa schema và tự động validate dữ liệu gửi lên trong Request Body. Cảm ơn các em đã chú ý lắng nghe. Hẹn gặp lại các em trong các bài học sau!" }
        ]
    }
    write_json("video_03.json", video_03)

    # Video 04
    video_04 = {
        "filename": "Lesson 04 - Type Hints trong FastAPI - Ràng buộc dữ liệu",
        "subdir": "Kịch bản quay video",
        "lesson_no": 4,
        "blocks": [
            { "type": "h2", "text": "## Đặt các ràng buộc dữ liệu nâng cao" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu cách thiết lập các ràng buộc nâng cao cho dữ liệu bằng cách sử dụng Query, Path, và Field." },
            { "type": "narration", "text": "Trong thực tế, chỉ định nghĩa kiểu dữ liệu là số hay chuỗi chưa đủ. Chúng ta cần những ràng buộc chi tiết hơn như: tuổi phải lớn hơn 18, từ khóa tìm kiếm phải dài ít nhất 2 ký tự, hay email phải đúng định dạng." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Sử dụng Query, Path, và Field" },
            { "type": "narration", "text": "Hãy cùng theo dõi ví dụ trên màn hình. Để ràng buộc query parameter, chúng ta dùng Query(). Để ràng buộc path parameter, chúng ta dùng Path() và để đặt ràng buộc cho thuộc tính của Pydantic model, chúng ta dùng Field()." },
            { "type": "marker", "text": "[mở trình duyệt hiển thị code ví dụ kết hợp Query, Path và Field]" },
            { "type": "narration", "text": "Các em có thể dùng tham số min_length, max_length cho chuỗi; ge, le, gt, lt cho số và pattern để dùng biểu thức chính quy kiểm tra email. Tất cả các ràng buộc này không chỉ tự động kiểm chứng khi chạy mà còn hiển thị rất rõ ràng trên tài liệu Swagger UI tự động." },
            { "type": "marker", "text": "[mở tài liệu Swagger UI tại đường dẫn /docs và demo kiểm thử]" },
            { "type": "narration", "text": "Khi thầy nhập thử tuổi là 15 vào API tạo sản phẩm, Swagger UI sẽ hiển thị ngay lỗi 422. Cấu trúc lỗi này gồm loc chỉ ra vị trí lỗi, msg mô tả lỗi và type phân loại lỗi, giúp lập trình viên frontend dễ dàng lập trình hiển thị thông báo lỗi lên giao diện." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Như vậy là chúng ta đã cùng nhau làm chủ kỹ thuật validate dữ liệu nâng cao với Query, Path, Field và hiểu sâu cấu trúc lỗi 422. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở session học tiếp theo nhé!" }
        ]
    }
    write_json("video_04.json", video_04)


    # ------------------ EXERCISES (6 files) ------------------
    # Exercise 01
    exercise_01 = {
        "filename": "[Vận dụng cơ bản 1] Sửa lỗi xung đột thứ tự Route trong API Sinh viên",
        "subdir": "Bài tập",
        "level": "Vận dụng cơ bản",
        "blocks": [
            { "type": "h1", "text": "Sửa lỗi xung đột thứ tự Route trong API Sinh viên" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Một hệ thống quản lý học tập đang phát triển các endpoint để quản lý thông tin sinh viên. Nhà phát triển đã viết mã để hỗ trợ hai tính năng: một route lấy hồ sơ cá nhân của sinh viên hiện tại đăng nhập qua đường dẫn '/students/me' và một route lấy thông tin sinh viên bất kỳ qua ID học sinh '/students/{student_id}'." },
            { "type": "h2", "text": "2. Vấn đề hiện tại" },
            { "type": "p", "text": "Tuy nhiên, khi gọi API `/students/me`, hệ thống liên tục trả về lỗi mã trạng thái 422 Unprocessable Entity với thông điệp báo rằng 'me' không phải số nguyên hợp lệ. Sinh viên cần xác định nguyên nhân và sửa lại mã nguồn." },
            { "type": "h2", "text": "3. Mã nguồn hiện tại (Legacy Code)" },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\n\napp = FastAPI()\n\n# Lấy chi tiết sinh viên bất kỳ theo ID\n@app.get(\"/students/{student_id}\")\ndef get_student_by_id(student_id: int):\n    return {\"student_id\": student_id, \"name\": \"Nguyen Van An\", \"role\": \"student\"}\n\n# Lấy thông tin sinh viên hiện tại\n@app.get(\"/students/me\")\ndef get_my_profile():\n    return {\"student_id\": 999, \"name\": \"Sinh viên hiện tại (Tôi)\", \"role\": \"admin\"}" },
            { "type": "h2", "text": "4. Yêu cầu đầu ra" },
            { "type": "h3", "text": "Nhiệm vụ 1: Phân tích nguyên nhân lỗi" },
            { "type": "bullets", "items": [
                "Hãy giải thích chi tiết cơ chế phân giải đường dẫn của FastAPI và tại sao lỗi này xảy ra khi gọi GET `/students/me`.",
                "Chỉ ra dòng code gây ra xung đột."
            ]},
            { "type": "h3", "text": "Nhiệm vụ 2: Sửa lỗi mã nguồn" },
            { "type": "bullets", "items": [
                "Sắp xếp lại các route để sửa dứt điểm lỗi xung đột.",
                "Viết code hoàn thiện và chạy thử nghiệm trên Uvicorn."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session04", "ex": "Ex01",
            "example": "HNKS25CNTT1_FastAPI_Session04_Ex01"
        }
    }
    write_json("exercise_01.json", exercise_01)

    # Exercise 02
    exercise_02 = {
        "filename": "[Vận dụng cơ bản 2] Ràng buộc dữ liệu số học với Path Parameters",
        "subdir": "Bài tập",
        "level": "Vận dụng cơ bản",
        "blocks": [
            { "type": "h1", "text": "Thiết lập ràng buộc số học cho Path Parameters" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Hệ thống quản lý đào tạo yêu cầu mã ID của sinh viên phải luôn là số nguyên dương lớn hơn hoặc bằng 1 và không vượt quá 99999. Nếu client gửi yêu cầu với ID bằng 0 hoặc số âm, hệ thống cần phát hiện lỗi ngay từ tầng API validation để tránh truy vấn vô ích vào cơ sở dữ liệu." },
            { "type": "h2", "text": "2. Yêu cầu bài toán" },
            { "type": "p", "text": "Hãy chỉnh sửa API endpoint nhận ID sinh viên để áp dụng các ràng buộc số học nêu trên sử dụng Path() của FastAPI. Đảm bảo các ràng buộc được mô tả rõ ràng để tự động sinh Swagger document." },
            { "type": "h2", "text": "3. Mã nguồn hiện tại (Legacy Code)" },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/students/{student_id}\")\ndef get_student_detail(student_id: int):\n    # Hiện tại chưa có ràng buộc giá trị min/max cho student_id\n    return {\"student_id\": student_id, \"message\": \"Thành công\"}" },
            { "type": "h2", "text": "4. Yêu cầu đầu ra" },
            { "type": "h3", "text": "Nhiệm vụ 1: Triển khai mã nguồn mới" },
            { "type": "bullets", "items": [
                "Nhúng Path() của fastapi vào tham số student_id.",
                "Áp dụng ràng buộc lớn hơn hoặc bằng 1 (ge=1) và nhỏ hơn hoặc bằng 99999 (le=99999).",
                "Thêm mô tả 'ID định danh của sinh viên' vào tài liệu."
            ]},
            { "type": "h3", "text": "Nhiệm vụ 2: Kiểm thử" },
            { "type": "bullets", "items": [
                "Demo cấu trúc lỗi JSON trả về khi gọi API với ID bằng 0."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session04", "ex": "Ex02",
            "example": "HNKS25CNTT1_FastAPI_Session04_Ex02"
        }
    }
    write_json("exercise_02.json", exercise_02)

    # Exercise 03
    exercise_03 = {
        "filename": "[Vận dụng chuyên sâu] Thiết kế và validate API Đăng ký môn học",
        "subdir": "Bài tập",
        "level": "Vận dụng chuyên sâu",
        "blocks": [
            { "type": "h1", "text": "Đăng ký khóa học với Request Body lồng nhau" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Hệ thống đăng ký học tập cần một API nhận thông tin đăng ký của sinh viên. Mỗi bản đăng ký gồm: mã số sinh viên, danh sách mã các môn học muốn đăng ký (tối thiểu đăng ký 1 môn, tối đa 5 môn), và thông tin người bảo trợ liên hệ khẩn cấp (gồm tên và số điện thoại)." },
            { "type": "h2", "text": "2. Quy tắc nghiệp vụ" },
            { "type": "bullets", "items": [
                "Mã số sinh viên phải lớn hơn 0.",
                "Danh sách môn học phải chứa các chuỗi ký tự mã môn (ví dụ 'IT215'), độ dài danh sách từ 1 đến 5.",
                "Thông tin liên hệ khẩn cấp là bắt buộc, số điện thoại phải có định dạng số điện thoại Việt Nam (10 chữ số)."
            ]},
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "h3", "text": "(1) Thiết kế Pydantic Schemas" },
            { "type": "bullets", "items": [
                "Định nghĩa `EmergencyContactSchema` chứa name và phone.",
                "Định nghĩa `CourseRegistrationSchema` chứa student_id, course_codes (kiểu list[str]) và contact (kiểu EmergencyContactSchema)."
            ]},
            { "type": "h3", "text": "(2) Viết API Endpoint và chạy thử" },
            { "type": "bullets", "items": [
                "Viết endpoint POST `/registrations` nhận body JSON tương ứng.",
                "Kiểm tra validation khi gửi dữ liệu sai quy tắc."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session04", "ex": "Ex03",
            "example": "HNKS25CNTT1_FastAPI_Session04_Ex03"
        }
    }
    write_json("exercise_03.json", exercise_03)

    # Exercise 04
    exercise_04 = {
        "filename": "[Phân tích] Lựa chọn Path Parameters vs Query Parameters",
        "subdir": "Bài tập",
        "level": "Phân tích",
        "blocks": [
            { "type": "h1", "text": "Phân tích so sánh Path Parameters và Query Parameters" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Một công ty công nghệ giáo dục đang tái thiết kế hệ thống API của mình. Có hai nghiệp vụ cần thiết kế:\nNghiệp vụ A: Xem danh sách bài học của một khóa học cụ thể.\nNghiệp vụ B: Tìm kiếm khóa học theo từ khóa và sắp xếp theo giá tiền." },
            { "type": "h2", "text": "2. Yêu cầu phân tích" },
            { "type": "p", "text": "Sinh viên cần lập bảng phân tích so sánh và chọn giải pháp thiết kế URL tối ưu cho hai nghiệp vụ trên." },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "h3", "text": "(1) Lập bảng so sánh" },
            { "type": "table", "headers": ["Tiêu chí", "Path Parameters", "Query Parameters"], "rows": [
                ["Mục đích sử dụng chính", "", ""],
                ["Tính bắt buộc", "", ""],
                ["Ảnh hưởng cấu trúc URL", "", ""],
                ["Khả năng caching ở phía Client", "", ""]
            ]},
            { "type": "h3", "text": "(2) Thiết kế API thực tế" },
            { "type": "bullets", "items": [
                "Đề xuất URL và viết code triển khai API cho cả Nghiệp vụ A và Nghiệp vụ B trong FastAPI.",
                "Giải thích lý do lựa chọn của mình dựa trên quy chuẩn RESTful API."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session04", "ex": "Ex04",
            "example": "HNKS25CNTT1_FastAPI_Session04_Ex04"
        }
    }
    write_json("exercise_04.json", exercise_04)

    # Exercise 05
    exercise_05 = {
        "filename": "[Sáng tạo] Xây dựng API Quản lý sản phẩm với validation động",
        "subdir": "Bài tập",
        "level": "Sáng tạo",
        "blocks": [
            { "type": "h1", "text": "Xây dựng Hệ thống Validation động cho sản phẩm" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Nhà trường muốn các học viên tự thiết kế một hệ thống kiểm chứng sản phẩm cho trang thương mại điện tử. Yêu cầu sản phẩm phải chứa mã vạch (phải bắt đầu bằng chữ 'PROD-' và theo sau bởi 5 chữ số), giá tiền phải lớn hơn 1000 VNĐ, và danh sách thẻ phân loại (tags) của sản phẩm không được rỗng." },
            { "type": "h2", "text": "2. Thử thách Sáng tạo" },
            { "type": "p", "text": "Hãy tự đề xuất cấu trúc Pydantic Model đầy đủ và viết API POST `/products` nhận sản phẩm đó. Đồng thời viết thêm một route GET `/products/search` sử dụng Query parameter với ràng buộc tùy chọn lọc theo khoảng giá từ `min_price` đến `max_price` (phải đảm bảo min_price <= max_price thông qua hàm tự viết validate)." },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Viết code đầy đủ chứa các model Pydantic nâng cao.",
                "Viết hàm kiểm chứng tùy biến (custom validator) sử dụng `@validator` hoặc `@model_validator` của Pydantic để đảm bảo logic min_price <= max_price.",
                "Hướng dẫn chi tiết cách chạy và kiểm tra lỗi 422 trên Swagger UI."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session04", "ex": "Ex05",
            "example": "HNKS25CNTT1_FastAPI_Session04_Ex05"
        }
    }
    write_json("exercise_05.json", exercise_05)

    # Exercise 06
    exercise_06 = {
        "filename": "[BTTH] Phát triển bộ API quản lý điểm sinh viên hoàn chỉnh",
        "subdir": "Bài tập",
        "level": "Tổng hợp",
        "blocks": [
            { "type": "h1", "text": "Bài tập thực hành tổng hợp: Quản lý điểm thi" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Học viên cần xây dựng một ứng dụng nhỏ quản lý điểm thi của lớp học. Ứng dụng cần hỗ trợ các chức năng: xem danh sách điểm thi (có lọc theo tên môn và lọc sinh viên đỗ/trượt), xem điểm của một sinh viên cụ thể theo ID, và nhập điểm thi mới cho sinh viên." },
            { "type": "h2", "text": "2. Yêu cầu kỹ thuật" },
            { "type": "bullets", "items": [
                "GET `/grades`: Lọc theo query `subject` (tùy chọn) và `passed` (bool, mặc định True để lấy danh sách đỗ - điểm >= 5).",
                "GET `/grades/{student_id}`: Path parameter student_id phải >= 1.",
                "POST `/grades`: Request body nhận JSON gồm `student_id` (int, >=1), `subject` (str, 2-50 ký tự), và `score` (float, từ 0.0 đến 10.0)."
            ]},
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Viết file `main.py` hoàn chỉnh chạy được.",
                "Tạo dữ liệu giả lập (mock database) dưới dạng List các dict trong Python.",
                "Thực hiện demo đầy đủ 3 API trên Swagger UI."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session04", "ex": "Ex06",
            "example": "HNKS25CNTT1_FastAPI_Session04_Ex06"
        }
    }
    write_json("exercise_06.json", exercise_06)


    # ------------------ QUIZZES ------------------
    # Quiz Đầu giờ
    quiz_daugio = {
        "sheet_name": "Quiz_DauGio_FastAPI_04",
        "questions": [
            # 12 câu Bài cũ (Session 02/03)
            {
                "q": "FastAPI được xây dựng dựa trên hai thư viện chính nào?",
                "answers": ["Flask và Django", "Tornado và Twisted", "Starlette và Pydantic", "Pyramid và Bottle"],
                "explanations": ["Không đúng, Flask và Django là các framework độc lập.", "Không đúng, Tornado và Twisted là các thư viện mạng cũ.", "Chính xác, FastAPI là sự kết hợp của Starlette (cho web) và Pydantic (cho validate dữ liệu).", "Không đúng, đây là các micro-framework khác."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Lệnh nào dùng để khởi động server Uvicorn cho file main.py có khai báo app = FastAPI()?",
                "answers": ["python main.py", "fastapi run main.py", "uvicorn main:app --reload", "run uvicorn mainapp"],
                "explanations": ["Chỉ chạy file script Python thường, không khởi chạy uvicorn trừ khi viết code khởi động bên trong.", "Không phải lệnh chuẩn của FastAPI đời đầu.", "Chính xác, uvicorn <tên_file>:<tên_biến_app> --reload để tự động tải lại code.", "Sai cú pháp lệnh."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Để truy cập tài liệu Swagger UI tự sinh của ứng dụng FastAPI, ta dùng đường dẫn nào?",
                "answers": ["/swagger", "/api/docs", "/docs", "/redoc/ui"],
                "explanations": ["Không đúng.", "Không đúng.", "Chính xác, FastAPI mặc định cấu hình Swagger UI tại đường dẫn /docs.", "Không đúng."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Kiểu kiến trúc nào phân tách hoàn toàn mã nguồn giao diện (Frontend) và xử lý dữ liệu (Backend)?",
                "answers": ["Server-Side Rendering (SSR)", "Monolithic Architecture", "Decoupled Architecture (API-first)", "MVC Pattern"],
                "explanations": ["SSR trộn cả giao diện và dữ liệu tại server.", "Monolithic gộp chung toàn bộ hệ thống làm một.", "Chính xác, kiến trúc tách rời (decoupled) sử dụng API làm trung tâm giao tiếp.", "MVC là mẫu thiết kế phần mềm, không phải kiến trúc hệ thống decoupled."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Thư viện nào trong FastAPI chịu trách nhiệm kiểm tra tính hợp lệ của dữ liệu đầu vào?",
                "answers": ["Starlette", "Pydantic", "SQLAlchemy", "Uvicorn"],
                "explanations": ["Starlette lo phần routing và web toolkit.", "Chính xác, Pydantic lo kiểm chứng dữ liệu dựa trên Type Hints.", "SQLAlchemy là thư viện ORM làm việc với cơ sở dữ liệu.", "Uvicorn là máy chủ web ASGI."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Chuẩn giao tiếp web ASGI viết tắt của cụm từ nào?",
                "answers": ["Asynchronous Server Gateway Interface", "Advanced System Gate Integration", "Active Service Gateway Interface", "Asynchronous Socket Group Interaction"],
                "explanations": ["Chính xác, ASGI hỗ trợ xử lý bất đồng bộ trong Python web.", "Không đúng.", "Không đúng.", "Không đúng."],
                "correct": 1, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Trong Python, từ khóa nào đi kèm với 'await' dùng để khai báo một hàm bất đồng bộ?",
                "answers": ["def", "async", "async def", "defer"],
                "explanations": ["Dùng khai báo hàm đồng bộ thường.", "Không đi độc lập trước tên hàm.", "Chính xác, async def dùng để định nghĩa một coroutine hàm bất đồng bộ.", "Không phải từ khóa chuẩn của Python."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Định dạng trao đổi dữ liệu phổ biến nhất giữa client và server trong API hiện đại là gì?",
                "answers": ["XML", "HTML", "JSON", "Plain Text"],
                "explanations": ["Đã cũ và cồng kềnh hơn.", "Dùng để hiển thị giao diện web.", "Chính xác, JSON nhẹ, dễ đọc, viết dưới dạng các cặp key-value.", "Không có cấu trúc rõ ràng."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Khi tạo môi trường ảo Python trên Windows bằng lệnh python -m venv venv, thư mục chứa file kích hoạt (activate) tên là gì?",
                "answers": ["bin", "Scripts", "Include", "Lib"],
                "explanations": ["Thư mục này trên hệ điều hành Linux/macOS.", "Chính xác, trên Windows đường dẫn kích hoạt là venv\\Scripts\\activate.", "Chứa các file header C/C++.", "Chứa thư viện Python."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Trong RESTful API, phương thức HTTP nào thường dùng để tạo mới dữ liệu?",
                "answers": ["GET", "POST", "PUT", "DELETE"],
                "explanations": ["GET dùng để đọc dữ liệu.", "Chính xác, POST thường ánh xạ tới hành động Create.", "PUT dùng để cập nhật dữ liệu.", "DELETE dùng để xóa dữ liệu."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Mã trạng thái HTTP nào biểu thị việc tài nguyên yêu cầu thành công?",
                "answers": ["200 OK", "201 Created", "400 Bad Request", "404 Not Found"],
                "explanations": ["Chính xác, 200 OK dùng cho các phản hồi thành công chung.", "Dùng khi tạo tài nguyên thành công.", "Dùng khi request bị lỗi cú pháp phía client.", "Dùng khi không tìm thấy tài nguyên."],
                "correct": 1, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Uvicorn được xây dựng dựa trên những thư viện hiệu năng cao nào?",
                "answers": ["django-admin và pip", "uvloop và httptools", "requests và urllib", "flask và jinja2"],
                "explanations": ["Không liên quan.", "Chính xác, đây là các thư viện giúp Uvicorn đạt tốc độ cực lớn.", "Đây là các thư viện client HTTP.", "Đây là các thư viện phục vụ Flask template."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            # 8 câu Bài mới (Session 04)
            {
                "q": "Làm thế nào để chỉ ra một tham số của route là Path Parameter trong FastAPI?",
                "answers": ["Khai báo trong Query()", "Bọc tên tham số trong ngoặc nhọn {} ở đường dẫn route", "Đặt giá trị mặc định là Path()", "Khai báo trong Request Body"],
                "explanations": ["Query() dùng cho query parameter.", "Chính xác, đường dẫn có dạng /items/{item_id} chỉ ra item_id là path parameter.", "Path() dùng để validate chứ không định nghĩa vị trí.", "Request body được lấy từ JSON body."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Khi nào một tham số trong hàm xử lý route được FastAPI coi là Query Parameter?",
                "answers": ["Khi nó có kiểu dữ liệu là Pydantic BaseModel", "Khi nó được bọc trong {} ở route path", "Khi nó có kiểu dữ liệu nguyên thủy và KHÔNG nằm trong route path", "Khi nó được định nghĩa trong body"],
                "explanations": ["Nó sẽ được hiểu là Request Body.", "Nó sẽ được hiểu là Path Parameter.", "Chính xác, nếu không khai báo trong path, nó mặc định là query parameter.", "Không đúng."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Lớp cơ sở (Base Class) nào của Pydantic được dùng để kế thừa khi định nghĩa một Request Body Schema?",
                "answers": ["PydanticModel", "BaseSchema", "BaseModel", "DataModel"],
                "explanations": ["Không đúng tên class.", "Không đúng.", "Chính xác, từ pydantic import BaseModel.", "Không đúng."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Trong FastAPI, tính chất BẮT BUỘC hay TÙY CHỌN của Query Parameter được quyết định bởi yếu tố nào?",
                "answers": ["Việc khai báo kiểu dữ liệu", "Việc nó có giá trị mặc định hay không", "Phương thức HTTP sử dụng", "Sử dụng decorator khác nhau"],
                "explanations": ["Kiểu dữ liệu chỉ dùng để validate và ép kiểu.", "Chính xác, nếu không có giá trị mặc định thì bắt buộc; ngược lại là tùy chọn.", "Không đúng.", "Không đúng."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Để đặt ràng buộc 'lớn hơn hoặc bằng 1' cho một Path Parameter, ta dùng tùy chọn nào trong Path()?",
                "answers": ["gt=1", "ge=1", "le=1", "lt=1"],
                "explanations": ["gt là lớn hơn (Greater Than).", "Chính xác, ge viết tắt của Greater than or Equal.", "le là nhỏ hơn hoặc bằng (Less than or Equal).", "lt là nhỏ hơn (Less Than)."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Khi dữ liệu truyền lên từ client không vượt qua được bước xác thực (validate) của FastAPI, mã lỗi HTTP nào được trả về?",
                "answers": ["400 Bad Request", "401 Unauthorized", "404 Not Found", "422 Unprocessable Entity"],
                "explanations": ["Là lỗi cú pháp request nói chung.", "Là lỗi chưa xác thực tài khoản.", "Là lỗi không tìm thấy tài nguyên.", "Chính xác, 422 Unprocessable Entity là mã lỗi chuẩn mà FastAPI tự sinh khi validate thất bại."],
                "correct": 4, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Đâu là quy tắc sắp xếp route đúng trong FastAPI để tránh xung đột đường dẫn?",
                "answers": ["Đọc ngẫu nhiên không quan trọng thứ tự", "Đặt route động (chứa tham số) trước route tĩnh", "Đặt các route tĩnh lên trước các route động", "Khai báo tất cả route trong một hàm duy nhất"],
                "explanations": ["FastAPI duyệt từ trên xuống dưới nên thứ tự rất quan trọng.", "Nếu đặt động trước, tĩnh sẽ bị nhận nhầm và gây lỗi 422.", "Chính xác, luôn ưu tiên route tĩnh (vd /students/me) trước route động (vd /students/{id}).", "Mỗi route tương ứng một hàm độc lập."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Trong Pydantic model, hàm nào được dùng để đặt các ràng buộc dữ liệu cho các thuộc tính của model?",
                "answers": ["Query()", "Path()", "Field()", "Validate()"],
                "explanations": ["Dùng cho query parameter.", "Dùng cho path parameter.", "Chính xác, Field() từ pydantic dùng để đặt ràng buộc (min_length, gt...) cho thuộc tính trong BaseModel.", "Không đúng."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            }
        ]
    }
    write_json("quiz_daugio.json", quiz_daugio)

    # Quiz Cuối giờ
    quiz_cuoigio = {
        "sheet_name": "Quiz_CuoiGio_FastAPI_04",
        "questions": [
            {
                "q": "Nếu route định nghĩa là /students/{student_id} và hàm xử lý là def get_student(student_id: int), chuyện gì xảy ra khi client gọi GET /students/123?",
                "answers": [
                    "student_id sẽ nhận giá trị kiểu chuỗi '123'",
                    "Hệ thống báo lỗi 500 Internal Server Error",
                    "student_id sẽ được ép kiểu thành số nguyên 123 và trả về kết quả thành công",
                    "Hệ thống tự động chuyển hướng sang trang chủ"
                ],
                "explanations": [
                    "Không đúng, FastAPI tự ép kiểu sang int theo type hint.",
                    "Không đúng, request hoàn toàn hợp lệ.",
                    "Chính xác, FastAPI ép kiểu thông minh dựa trên type hint.",
                    "Không đúng."
                ],
                "correct": 3, "difficulty": 6, "category": "PATH_PARAMETER"
            },
            {
                "q": "Khi định nghĩa route tĩnh /students/me và route động /students/{student_id}, vì sao phải đặt route tĩnh lên trước?",
                "answers": [
                    "Để code trông đẹp hơn",
                    "Để tránh FastAPI nhận nhầm chuỗi 'me' là giá trị student_id của route động và cố ép sang kiểu int",
                    "Để tăng tốc độ thực thi của máy chủ Uvicorn",
                    "Đó là quy tắc bắt buộc của Python, không xếp trước sẽ lỗi cú pháp Python"
                ],
                "explanations": [
                    "Không đúng.",
                    "Chính xác, nếu xếp route động trước, request /students/me sẽ khớp vào {student_id} và trả về lỗi 422 do 'me' không phải int.",
                    "Tốc độ thực thi không đổi.",
                    "Python không kiểm soát thứ tự này, đây là cơ chế định tuyến của FastAPI/Starlette."
                ],
                "correct": 2, "difficulty": 6, "category": "ROUTE_ORDER"
            },
            {
                "q": "Trong hàm def read_items(keyword: str = '', category: str | None = None), hai tham số này thuộc loại nào?",
                "answers": [
                    "Path parameters bắt buộc",
                    "Query parameters tùy chọn (optional)",
                    "Request body bắt buộc",
                    "Query parameters bắt buộc"
                ],
                "explanations": [
                    "Không đúng, chúng không có mặt trong đường dẫn route.",
                    "Chính xác, vì chúng không có trong route path và đều có giá trị mặc định ('', None).",
                    "Không đúng.",
                    "Không đúng, chúng là tùy chọn vì có giá trị mặc định."
                ],
                "correct": 2, "difficulty": 6, "category": "QUERY_PARAMETER"
            },
            {
                "q": "Để khai báo một Query Parameter là BẮT BUỘC trong FastAPI, chúng ta phải làm thế nào?",
                "answers": [
                    "Đặt kiểu dữ liệu là Required",
                    "Bọc tên tham số trong dấu ngoặc nhọn",
                    "Không gán giá trị mặc định cho tham số đó trong hàm xử lý route",
                    "Sử dụng decorator @app.required"
                ],
                "explanations": [
                    "Python không có kiểu dữ liệu Required.",
                    "Đó là khai báo Path Parameter.",
                    "Chính xác, không gán giá trị mặc định nghĩa là client buộc phải truyền giá trị đó trên URL.",
                    "Không có decorator này."
                ],
                "correct": 3, "difficulty": 7, "category": "QUERY_PARAMETER"
            },
            {
                "q": "FastAPI hỗ trợ ép kiểu logic (bool) từ query parameter. Giá trị nào dưới đây truyền trên URL sẽ được ép kiểu thành False?",
                "answers": ["1", "yes", "0", "true"],
                "explanations": ["1 được hiểu là True.", "yes được hiểu là True.", "Chính xác, 0, false, no, off đều được FastAPI ép kiểu thành False.", "true được hiểu là True."],
                "correct": 3, "difficulty": 5, "category": "QUERY_PARAMETER"
            },
            {
                "q": "Khi khai báo class StudentCreate(BaseModel), đối tượng này đóng vai trò gì khi khai báo trong tham số hàm của route POST?",
                "answers": [
                    "Lấy dữ liệu từ Path Parameter",
                    "Tự động ánh xạ tới bảng trong database",
                    "Định nghĩa cấu trúc (schema) và đại diện cho dữ liệu nhận từ Request Body",
                    "Dùng để render file HTML"
                ],
                "explanations": [
                    "Không đúng, path parameter khai báo trên URL.",
                    "Đó là ORM model (SQLAlchemy), BaseModel của Pydantic chỉ mô tả schema dữ liệu truyền nhận.",
                    "Chính xác, FastAPI nhận diện tham số kiểu BaseModel và đọc dữ liệu từ thân request (JSON body).",
                    "Không đúng."
                ],
                "correct": 3, "difficulty": 6, "category": "REQUEST_BODY"
            },
            {
                "q": "Cấu trúc thông báo lỗi 422 Unprocessable Entity của FastAPI gồm 3 trường thông tin chính nào cho mỗi lỗi?",
                "answers": [
                    "code, message, status",
                    "loc (vị trí), msg (thông báo), type (loại lỗi)",
                    "error, timestamp, path",
                    "file, line, expression"
                ],
                "explanations": [
                    "Không đúng.",
                    "Chính xác, đây là các trường chuẩn của cấu trúc lỗi FastAPI giúp dễ gỡ lỗi.",
                    "Không đúng.",
                    "Không đúng."
                ],
                "correct": 2, "difficulty": 7, "category": "ERROR_HANDLING"
            },
            {
                "q": "Ký hiệu '...' (dấu ba chấm / Ellipsis) truyền vào đối số đầu tiên của Path() có ý nghĩa gì?",
                "answers": [
                    "Tham số này có thể nhận bất kỳ giá trị nào",
                    "Đánh dấu đây là tham số tùy chọn (optional)",
                    "Đánh dấu đây là tham số bắt buộc phải truyền (required)",
                    "Bỏ qua bước xác thực kiểu dữ liệu"
                ],
                "explanations": [
                    "Không đúng.",
                    "Không đúng.",
                    "Chính xác, Ellipsis dùng để báo với FastAPI rằng tham số này là bắt buộc trong cấu trúc validation.",
                    "Không đúng."
                ],
                "correct": 3, "difficulty": 7, "category": "VALIDATION"
            },
            {
                "q": "Ràng buộc 'ge=18' trong Field(..., ge=18) của Pydantic model có ý nghĩa gì?",
                "answers": [
                    "Giá trị thuộc tính phải lớn hơn 18",
                    "Giá trị thuộc tính phải nhỏ hơn hoặc bằng 18",
                    "Giá trị thuộc tính phải lớn hơn hoặc bằng 18",
                    "Độ dài chuỗi thuộc tính phải bằng 18 ký tự"
                ],
                "explanations": [
                    "Lớn hơn là gt (Greater Than).",
                    "Nhỏ hơn hoặc bằng là le (Less than or Equal).",
                    "Chính xác, ge viết tắt của Greater than or Equal.",
                    "Độ dài chuỗi là min_length / max_length."
                ],
                "correct": 3, "difficulty": 5, "category": "VALIDATION"
            },
            {
                "q": "Khi cần kiểm tra độ dài tối đa của một chuỗi truyền vào Query Parameter là 50 ký tự, ta khai báo như thế nào?",
                "answers": [
                    "Query(max_length=50)",
                    "Query(le=50)",
                    "Query(lt=50)",
                    "Query(size=50)"
                ],
                "explanations": [
                    "Chính xác, max_length dùng cho kiểu dữ liệu chuỗi (string).",
                    "le dùng cho giới hạn số học (nhỏ hơn hoặc bằng).",
                    "lt dùng cho giới hạn số học (nhỏ hơn).",
                    "Không có tham số size."
                ],
                "correct": 1, "difficulty": 5, "category": "VALIDATION"
            },
            {
                "q": "Để kiểm tra định dạng email của một trường trong Pydantic BaseModel bằng Regex, ta truyền regex vào tham số nào của Field()?",
                "answers": ["regex", "pattern", "format", "match"],
                "explanations": ["Đã bị loại bỏ trong Pydantic v2.", "Chính xác, trong Pydantic v2 ta sử dụng tham số pattern để chỉ định biểu thức chính quy.", "Không phải tham số hợp lệ.", "Không phải tham số hợp lệ."],
                "correct": 2, "difficulty": 8, "category": "VALIDATION"
            },
            {
                "q": "Tham số response_model trong route decorator của FastAPI mang lại lợi ích gì?",
                "answers": [
                    "Tăng tốc độ truy vấn cơ sở dữ liệu lên gấp đôi",
                    "Giúp chuẩn hóa dữ liệu đầu ra và tự động lọc bớt các thông tin nhạy cảm trước khi trả về client",
                    "Chuyển đổi giao diện sang chế độ tối",
                    "Tự động mã hóa toàn bộ dữ liệu trả về thành dạng nhị phân"
                ],
                "explanations": [
                    "Không tác động trực tiếp tới tốc độ database.",
                    "Chính xác, ví dụ giúp ẩn trường mật khẩu của tài khoản người dùng trước khi trả về.",
                    "Không liên quan.",
                    "Dữ liệu vẫn là JSON văn bản."
                ],
                "correct": 2, "difficulty": 7, "category": "RESPONSE_MODEL"
            },
            {
                "q": "Sự khác biệt lớn nhất về mặt nghiệp vụ giữa Path Parameter và Query Parameter là gì?",
                "answers": [
                    "Path Parameter chỉ nhận số, Query Parameter chỉ nhận chữ",
                    "Path Parameter định danh duy nhất tài nguyên, mang tính bắt buộc; Query Parameter dùng để lọc/sắp xếp/tìm kiếm tài nguyên, mang tính tùy chọn",
                    "Path Parameter chạy nhanh hơn Query Parameter",
                    "Query Parameter bắt buộc phải viết mã hóa bảo mật hơn"
                ],
                "explanations": [
                    "Cả hai đều có thể nhận bất kỳ kiểu dữ liệu nào.",
                    "Chính xác, đây là quy chuẩn thiết kế RESTful chuẩn hóa toàn cầu.",
                    "Hiệu năng xử lý tương đương nhau.",
                    "Mức độ bảo mật như nhau."
                ],
                "correct": 2, "difficulty": 6, "category": "REST_DESIGN"
            },
            {
                "q": "Hàm Field() được import từ thư viện nào?",
                "answers": ["fastapi", "typing", "pydantic", "starlette"],
                "explanations": ["Fastapi cung cấp Query() và Path().", "Typing cung cấp các type hint như Optional.", "Chính xác, Field() được cung cấp bởi pydantic.", "Starlette là framework core ở dưới."],
                "correct": 3, "difficulty": 5, "category": "VALIDATION"
            },
            {
                "q": "Nếu client gửi JSON có thêm một số trường lạ không khai báo trong Pydantic BaseModel, FastAPI sẽ xử lý như thế nào mặc định?",
                "answers": [
                    "Báo lỗi 422 Unprocessable Entity lập tức",
                    "Bỏ qua các trường thừa đó và chỉ lấy các trường có khai báo trong Model",
                    "Crash toàn bộ ứng dụng server",
                    "Tự động thêm các trường đó vào database"
                ],
                "explanations": [
                    "Không báo lỗi.",
                    "Chính xác, mặc định Pydantic lọc bỏ các trường không được định nghĩa trong schema.",
                    "Server vẫn hoạt động bình thường.",
                    "FastAPI không tự lưu database."
                ],
                "correct": 2, "difficulty": 8, "category": "REQUEST_BODY"
            }
        ]
    }
    write_json("quiz_cuoigio.json", quiz_cuoigio)


    # ------------------ MINDMAP ------------------
    mindmap = {
        "filename": "Session 04 - Parameters, Request body và Pydantic Validation",
        "subdir": "Mindmap",
        "root": "Parameters, Request body & Pydantic Validation",
        "children": [
            {
                "title": "1. Path Parameters (Định danh tài nguyên)",
                "children": [
                    { "title": "Khai báo: dùng cặp ngoặc nhọn trong URL, ví dụ /students/{student_id}" },
                    { "title": "Tự động ép kiểu & validate theo Type Hints của Python" },
                    { "title": "Tránh xung đột route: Luôn đặt route tĩnh trước route động" }
                ]
            },
            {
                "title": "2. Query Parameters (Lọc & Tìm kiếm)",
                "children": [
                    { "title": "Khai báo: các tham số hàm không có trong route path" },
                    { "title": "Phân loại: Bắt buộc (không mặc định) vs Tùy chọn (có mặc định)" },
                    { "title": "Ép kiểu Boolean linh hoạt từ URL: true/false, 1/0, yes/no" }
                ]
            },
            {
                "title": "3. Request Body với Pydantic (Dữ liệu phức tạp)",
                "children": [
                    { "title": "Pydantic BaseModel: Định nghĩa cấu trúc dữ liệu JSON (Schema)" },
                    { "title": "Tự động validate đầu vào & Trả lỗi 422 Unprocessable Entity" },
                    { "title": " response_model: Lọc dữ liệu đầu ra và bảo mật thông tin nhạy cảm" }
                ]
            },
            {
                "title": "4. Type Hints & Validation nâng cao",
                "children": [
                    { "title": "Ràng buộc Query Parameter: Dùng Query(min_length, max_length, ge, le)" },
                    { "title": "Ràng buộc Path Parameter: Dùng Path(..., ge, le, description)" },
                    { "title": "Ràng buộc thuộc tính Model: Dùng Field(..., gt, pattern)" },
                    { "title": "Cấu trúc lỗi 422: Gồm loc (vị trí lỗi), msg (thông báo), type (loại lỗi)" }
                ]
            }
        ]
    }
    write_json("mindmap.json", mindmap)


    # ------------------ SLIDE OUTLINE ------------------
    slide_outline = {
        "filename": "Session 04 - Parameters, Request body và Pydantic Validation",
        "subdir": "Bài giảng",
        "title": "Parameters, Request body & Pydantic Validation",
        "module": "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI",
        "version": "1.0",
        "slides": [
            {
                "layout": "title",
                "title": "Parameters, Request body & Pydantic Validation",
                "content": ["Session 04", "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI", "Phiên bản: 1.0"]
            },
            {
                "layout": "agenda",
                "section": "NỘI DUNG",
                "title": "Nội dung bài học",
                "content": [
                    "1. Path Parameters: Định danh & Lấy dữ liệu từ URL",
                    "2. Query Parameters: Tìm kiếm & Lọc dữ liệu",
                    "3. Request Body với Pydantic: Đọc & Validate JSON",
                    "4. Type Hints: Ràng buộc dữ liệu nâng cao với Query, Path, Field"
                ]
            },
            # Lesson 1
            {
                "layout": "section-title",
                "section": "1. Path Parameters",
                "title": "Phần 1: Path Parameters - Lấy dữ liệu từ URL",
                "content": ["Định danh tài nguyên RESTful", "Cú pháp khai báo trong FastAPI", "Ép kiểu dữ liệu tự động"]
            },
            {
                "layout": "bullets",
                "section": "1. Path Parameters",
                "title": "Khái niệm Path Parameters",
                "content": [
                    "Là phần thay đổi trực tiếp nằm trên URL nhằm xác định tài nguyên cụ thể.",
                    "Ví dụ: Trong đường dẫn /students/123, '123' là mã số của sinh viên cần lấy.",
                    "Sử dụng cho các trường hợp lấy chi tiết, cập nhật hoặc xóa một tài nguyên cụ thể."
                ],
                "diagram_hint": "Hình minh họa URL /students/{student_id} với mũi tên chỉ vào {student_id} chú thích 'Path Parameter'"
            },
            {
                "layout": "code",
                "section": "1. Path Parameters",
                "title": "Khai báo Path Parameter trong code",
                "content": [
                    "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get(\"/students/{student_id}\")\ndef read_student(student_id: int):\n    return {\"student_id\": student_id}"
                ],
                "speaker_notes": "Giải thích cách bọc ngoặc nhọn ở route và khai báo kiểu int ở hàm."
            },
            {
                "layout": "bullets",
                "section": "1. Path Parameters",
                "title": "Quy tắc thứ tự khai báo Route",
                "content": [
                    "FastAPI phân giải các route từ trên xuống dưới.",
                    "Nếu route động đặt trước route tĩnh, route tĩnh sẽ bị nuốt chửng và lỗi validate 422.",
                    "Giải pháp: Đặt route tĩnh (ví dụ /students/me) trước route động (ví dụ /students/{student_id})."
                ],
                "speaker_notes": "Nhấn mạnh lỗi thường gặp của học viên khi làm API thông tin cá nhân."
            },
            # Lesson 2
            {
                "layout": "section-title",
                "section": "2. Query Parameters",
                "title": "Phần 2: Query Parameters - Tìm kiếm và Lọc",
                "content": ["Khái niệm tham số truy vấn", "Khai báo tham số tùy chọn", "Ép kiểu logic Boolean"]
            },
            {
                "layout": "bullets",
                "section": "2. Query Parameters",
                "title": "Khái niệm Query Parameters",
                "content": [
                    "Là các cặp key-value xuất hiện sau dấu '?' trên URL.",
                    "Ví dụ: /courses?keyword=python&level=beginner.",
                    "Dùng để lọc dữ liệu, phân trang hoặc tìm kiếm. Không trực tiếp làm thay đổi định danh đường dẫn chính."
                ]
            },
            {
                "layout": "code",
                "section": "2. Query Parameters",
                "title": "Khai báo Query Parameter",
                "content": [
                    "@app.get(\"/courses\")\ndef get_courses(keyword: str = \"\", level: str | None = None):\n    # keyword và level là các query parameter tùy chọn vì có giá trị mặc định\n    return {\"keyword\": keyword, \"level\": level}"
                ],
                "speaker_notes": "So sánh: tham số không khai báo ở route decorator chính là query parameter."
            },
            # Lesson 3
            {
                "layout": "section-title",
                "section": "3. Request Body với Pydantic",
                "title": "Phần 3: Request Body - Đọc & Validate JSON",
                "content": ["Giới thiệu Request Body", "Kế thừa Pydantic BaseModel", "Cơ chế validate tự động"]
            },
            {
                "layout": "bullets",
                "section": "3. Request Body với Pydantic",
                "title": "Vì sao cần Request Body?",
                "content": [
                    "Khi cần gửi dữ liệu lớn, có cấu trúc và cần bảo mật (như đăng ký sinh viên mới).",
                    "Dữ liệu được gửi ẩn trong thân HTTP request dưới định dạng JSON.",
                    "FastAPI kết hợp với Pydantic để tự động hóa việc đọc và kiểm tra cấu trúc dữ liệu này."
                ]
            },
            {
                "layout": "code",
                "section": "3. Request Body với Pydantic",
                "title": "Sử dụng Pydantic BaseModel",
                "content": [
                    "from pydantic import BaseModel\n\nclass StudentCreate(BaseModel):\n    name: str\n    email: str\n    age: int\n\n@app.post(\"/students\")\ndef create(student: StudentCreate):\n    return student"
                ],
                "speaker_notes": "Hướng dẫn cách viết BaseModel và tích hợp vào hàm POST."
            },
            # Lesson 4
            {
                "layout": "section-title",
                "section": "4. Type Hints",
                "title": "Phần 4: Ràng buộc dữ liệu nâng cao",
                "content": ["Sử dụng Query() và Path() của FastAPI", "Sử dụng Field() của Pydantic", "Phân tích cấu trúc lỗi 422"]
            },
            {
                "layout": "code",
                "section": "4. Type Hints",
                "title": "Validate với Query() và Path()",
                "content": [
                    "from fastapi import Query, Path\n\n@app.get(\"/items/{id}\")\ndef read(\n    id: int = Path(..., ge=1),\n    keyword: str = Query(None, min_length=2)\n):\n    return {\"id\": id, \"keyword\": keyword}"
                ],
                "speaker_notes": "Giải thích ge=1 là lớn hơn hoặc bằng 1, và min_length=2 là độ dài chuỗi tối thiểu."
            },
            {
                "layout": "code",
                "section": "4. Type Hints",
                "title": "Validate thuộc tính với Field()",
                "content": [
                    "from pydantic import Field, BaseModel\n\nclass Product(BaseModel):\n    name: str = Field(..., min_length=2)\n    price: float = Field(..., gt=0)"
                ],
                "speaker_notes": "Giải thích cách dùng Field() trong BaseModel để kiểm soát chặt chẽ giá trị thuộc tính."
            },
            {
                "layout": "bullets",
                "section": "4. Type Hints",
                "title": "Cơ chế báo lỗi HTTP 422",
                "content": [
                    "Khi dữ liệu gửi lên vi phạm bất kỳ ràng buộc nào, FastAPI lập tức chặn lại.",
                    "Phản hồi mã trạng thái 422 Unprocessable Entity.",
                    "JSON trả về chứa loc (vị trí xảy ra lỗi), msg (thông điệp chi tiết) và type (mã lỗi)."
                ],
                "diagram_hint": "Sơ đồ JSON lỗi 422 chỉ ra ba thành phần loc, msg, type"
            },
            # Ending slides
            {
                "layout": "summary",
                "section": "TỔNG KẾT",
                "title": "Tổng kết bài học",
                "content": [
                    "Path Parameter: Dùng ngoặc nhọn {}, định danh duy nhất tài nguyên.",
                    "Query Parameter: Lọc & tìm kiếm, mặc định khi không khai báo ở route.",
                    "Request Body: Đọc dữ liệu JSON phức tạp qua Pydantic BaseModel.",
                    "Query(), Path(), Field(): Đặt ràng buộc dữ liệu trực quan trên Type Hints.",
                    "Lỗi 422: Tự động trả về khi validate thất bại, chứa chi tiết vị trí lỗi."
                ]
            },
            {
                "layout": "closing",
                "title": "KẾT THÚC",
                "content": ["HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN"]
            }
        ]
    }
    write_json("slide_outline.json", slide_outline)

    print("Successfully generated all 17 specification JSON files!")

if __name__ == "__main__":
    main()
