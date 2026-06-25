# -*- coding: utf-8 -*-
"""Script to programmatically generate all 18 spec JSON files for Session 05.
"""
import os
import json

SPEC_DIR = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap\output\Session 05 - CRUD cơ bản\_spec"

def write_json(name, data):
    path = os.path.join(SPEC_DIR, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Generated {name}")

def main():
    # ------------------ READINGS (4 files) ------------------
    # Reading 01
    reading_01 = {
        "filename": "BÀI ĐỌC_ API CREATE TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: API Create - Phương Thức POST Và Trạng Thái 201 Created" },
            { "type": "p", "text": "Thao tác đầu tiên trong chu trình CRUD là Create (Tạo mới). Trong thiết kế hệ thống phần mềm web RESTful API, việc tạo mới một thực thể tài nguyên (như tạo mới một hồ sơ sinh viên hoặc thêm một lớp học mới) luôn được ánh xạ tới phương thức HTTP POST. Bài đọc này giúp chúng ta làm chủ kỹ năng thiết kế Endpoint POST, xử lý mã trạng thái phản hồi chuẩn 201 Created và kiểm tra logic trùng lặp dữ liệu." },
            { "type": "h2", "text": "1. Phương thức POST và kiến trúc RESTful" },
            { "type": "p", "text": "Khác với GET dùng để truy xuất, POST là phương thức dùng để gửi dữ liệu lên server nhằm tạo ra một tài nguyên mới. POST không mang tính chất idempotent (không đồng nhất): nếu client gửi hai request POST giống hệt nhau liên tiếp, server thông thường sẽ tạo ra hai tài nguyên mới có ID khác nhau." },
            { "type": "h2", "text": "2. Trạng thái HTTP 201 Created" },
            { "type": "p", "text": "Khi một tài nguyên được tạo thành công ở phía Backend, mã trạng thái HTTP chuẩn xác cần trả về là 201 Created. Điều này thông báo cho phía Client (Frontend) biết rằng dữ liệu đã được ghi nhận bền vững và hệ thống đã cấp phát định danh (ID) mới cho tài nguyên đó." },
            { "type": "h2", "text": "3. Triển khai API POST và Kiểm tra Trùng lặp" },
            { "type": "p", "text": "Khi viết code tạo mới, chúng ta cần thực hiện các bước: nhận dữ liệu từ request body, kiểm tra logic nghiệp vụ (email không được trùng, mã số học viên phải duy nhất), thêm dữ liệu vào kho lưu trữ (in-memory list hoặc cơ sở dữ liệu), và trả về thông tin đối tượng kèm mã 201 Created." },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI, HTTPException, status\nfrom pydantic import BaseModel\n\napp = FastAPI()\nstudents_db = []\n\nclass StudentCreate(BaseModel):\n    name: str\n    email: str\n\n@app.post(\"/students\", status_code=status.HTTP_201_CREATED)\ndef create_student(student: StudentCreate):\n    # 1. Kiểm tra trùng lặp email\n    for s in students_db:\n        if s[\"email\"] == student.email:\n            raise HTTPException(status_code=400, detail=\"Email đã được sử dụng\")\n            \n    # 2. Tạo đối tượng mới kèm cấp ID tự động\n    new_id = len(students_db) + 1\n    new_student = {\"id\": new_id, \"name\": student.name, \"email\": student.email}\n    \n    # 3. Thêm vào database in-memory\n    students_db.append(new_student)\n    return new_student" },
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Phương thức POST dùng để tạo tài nguyên mới và không mang tính chất idempotent.",
                "HTTP 201 Created là mã phản hồi chuẩn sau khi tạo tài nguyên thành công.",
                "Cần kiểm tra các ràng buộc nghiệp vụ (trùng lặp dữ liệu độc bản) trước khi thêm mới."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "MDN Web Docs - POST: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST",
                "FastAPI Status Codes: https://fastapi.tiangolo.com/tutorial/response-status-code/"
            ]}
        ]
    }
    write_json("reading_01.json", reading_01)

    # Reading 02
    reading_02 = {
        "filename": "BÀI ĐỌC_ API READ TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: API Read - Phương Thức GET, Tìm Kiếm Danh Sách Và Lỗi 404 Not Found" },
            { "type": "p", "text": "Thao tác thứ hai trong chu trình CRUD là Read (Đọc dữ liệu). Trong kiến trúc RESTful API, việc truy xuất thông tin danh sách hoặc lấy chi tiết dữ liệu luôn sử dụng phương thức HTTP GET. Bài đọc này hướng dẫn chi tiết cách viết Endpoint GET lấy danh sách có lọc theo từ khóa và lấy chi tiết tài nguyên kèm xử lý ngoại lệ 404 Not Found." },
            { "type": "h2", "text": "1. Phương thức GET và tính chất Safe / Idempotent" },
            { "type": "p", "text": "GET là phương thức 'an toàn' (safe) vì nó chỉ đọc dữ liệu và không làm thay đổi trạng thái của máy chủ. Nó cũng mang tính 'idempotent' (đồng nhất): việc gọi GET 1 lần hay 100 lần liên tiếp cùng một URL luôn trả về cùng một kết quả dữ liệu (nếu dữ liệu gốc chưa bị tác động bởi thao tác khác)." },
            { "type": "h2", "text": "2. Triển khai API GET lấy danh sách và tìm kiếm" },
            { "type": "p", "text": "Thông thường, API lấy danh sách sẽ hỗ trợ thêm các Query Parameter để lọc kết quả theo từ khóa." },
            { "type": "code", "lang": "python", "text": "@app.get(\"/students\")\ndef list_students(keyword: str = \"\"):\n    if keyword:\n        return [s for s in students_db if keyword.lower() in s[\"name\"].lower()]\n    return students_db" },
            { "type": "h2", "text": "3. Triển khai API GET lấy chi tiết và lỗi 404 Not Found" },
            { "type": "p", "text": "Khi client muốn xem chi tiết một sinh viên cụ thể thông qua ID (Path Parameter), chúng ta phải tìm kiếm trong danh sách. Nếu tìm thấy, trả về thông tin đối tượng kèm mã 200 OK. Nếu duyệt hết danh sách mà không tìm thấy sinh viên nào khớp ID, bắt buộc phải trả về lỗi HTTP 404 Not Found kèm thông điệp báo lỗi rõ ràng." },
            { "type": "code", "lang": "python", "text": "@app.get(\"/students/{student_id}\")\ndef read_student_detail(student_id: int):\n    for s in students_db:\n        if s[\"id\"] == student_id:\n            return s\n    raise HTTPException(status_code=404, detail=\"Không tìm thấy sinh viên yêu cầu\")" },
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "HTTP GET dùng để đọc dữ liệu, có tính chất an toàn (safe) và đồng nhất (idempotent).",
                "API danh sách thường kết hợp query parameter để thực hiện lọc và tìm kiếm.",
                "Khi tìm kiếm theo ID không tồn tại, luôn trả về mã lỗi HTTP 404 Not Found để thông báo chính xác trạng thái."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "MDN Web Docs - GET: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET"
            ]}
        ]
    }
    write_json("reading_02.json", reading_02)

    # Reading 03
    reading_03 = {
        "filename": "BÀI ĐỌC_ API UPDATE TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: API Update - Phương Thức PUT, Ghi Đè Dữ Liệu Và Phân Biệt Với PATCH" },
            { "type": "p", "text": "Thao tác thứ ba trong CRUD là Update (Cập nhật dữ liệu). Trong thiết kế API chuẩn RESTful, thao tác cập nhật toàn bộ thuộc tính của tài nguyên thường sử dụng phương thức HTTP PUT. Bài đọc này giúp học viên triển khai thành công API PUT cập nhật thông tin sinh viên in-memory và phân tích so sánh chi tiết với phương thức PATCH." },
            { "type": "h2", "text": "1. Phương thức PUT và tính chất ghi đè toàn bộ" },
            { "type": "p", "text": "Phương thức PUT đại diện cho hành động thay thế/ghi đè hoàn toàn tài nguyên hiện tại bằng dữ liệu mới gửi lên từ client. Khi gọi PUT, client bắt buộc phải truyền đầy đủ các thuộc tính của đối tượng. Nếu thiếu một trường nào đó, trường đó có thể bị xóa hoặc đặt về giá trị mặc định tùy thiết kế hệ thống." },
            { "type": "h2", "text": "2. Triển khai API PUT cập nhật thông tin trong FastAPI" },
            { "type": "p", "text": "Khi nhận request PUT, đầu tiên ta dùng ID sinh viên để tìm kiếm sinh viên đó. Nếu tìm thấy, thực hiện ghi đè dữ liệu. Nếu không tìm thấy, trả về lỗi 404 Not Found." },
            { "type": "code", "lang": "python", "text": "class StudentUpdateSchema(BaseModel):\n    name: str\n    email: str\n\n@app.put(\"/students/{student_id}\")\ndef update_student_info(student_id: int, student_data: StudentUpdateSchema):\n    for s in students_db:\n        if s[\"id\"] == student_id:\n            s[\"name\"] = student_data.name\n            s[\"email\"] = student_data.email\n            return {\"message\": \"Cập nhật thành công\", \"data\": s}\n    raise HTTPException(status_code=404, detail=\"Không tìm thấy sinh viên để cập nhật\")" },
            { "type": "h2", "text": "3. Phân biệt PUT và PATCH" },
            { "type": "p", "text": "Trong thiết kế API nâng cao, có hai phương thức cập nhật:" },
            { "type": "bullets", "items": [
                "**PUT (Replace):** Thay thế toàn bộ đối tượng. Phải truyền tất cả các trường. Mang tính chất idempotent.",
                "**PATCH (Modify):** Cập nhật từng phần (chỉ sửa các trường gửi lên). Client chỉ gửi các trường cần thay đổi (ví dụ: chỉ đổi mỗi email). Cần xử lý logic kiểm tra các trường truyền lên linh hoạt hơn."
            ]},
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "PUT dùng để ghi đè toàn bộ tài nguyên hiện có và mang tính chất idempotent.",
                "Nếu ID tài nguyên không tồn tại, API PUT phải phản hồi lỗi 404 Not Found.",
                "Phân biệt rõ PUT (ghi đè toàn phần) và PATCH (cập nhật từng phần) khi thiết kế API hệ thống."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "MDN Web Docs - PUT: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT"
            ]}
        ]
    }
    write_json("reading_03.json", reading_03)

    # Reading 04
    reading_04 = {
        "filename": "BÀI ĐỌC_ API DELETE TRONG FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: API Delete - Phương Thức DELETE, Trạng Thái 204 No Content Và Xóa Mềm" },
            { "type": "p", "text": "Thao tác cuối cùng trong CRUD là Delete (Xóa dữ liệu). Trong thiết kế API chuẩn RESTful, việc loại bỏ một tài nguyên khỏi hệ thống sử dụng phương thức HTTP DELETE. Bài đọc này hướng dẫn chi tiết cách triển khai API DELETE xóa sinh viên theo ID, làm quen với mã phản hồi 204 No Content và tìm hiểu về khái niệm Xóa mềm (Soft Delete) trong thiết kế database." },
            { "type": "h2", "text": "1. Phương thức DELETE và tính chất Idempotent" },
            { "type": "p", "text": "Phương thức DELETE dùng để xóa tài nguyên được chỉ định. Đây cũng là một phương thức idempotent: xóa lần đầu thành công trả về 200/204; các lần sau tài nguyên đã biến mất nên hệ thống có thể trả lỗi 404, nhưng trạng thái thực tế của máy chủ không thay đổi thêm (tài nguyên vẫn ở trạng thái đã bị xóa)." },
            { "type": "h2", "text": "2. Triển khai API DELETE với trạng thái 204 No Content" },
            { "type": "p", "text": "Khi xóa thành công, nếu server không có dữ liệu nào cần gửi lại cho client ngoài thông điệp thành công, mã trạng thái HTTP chuẩn xác nhất cần phản hồi là 204 No Content." },
            { "type": "code", "lang": "python", "text": "@app.delete(\"/students/{student_id}\", status_code=status.HTTP_204_NO_CONTENT)\ndef remove_student(student_id: int):\n    global students_db\n    for idx, s in enumerate(students_db):\n        if s[\"id\"] == student_id:\n            students_db.pop(idx)\n            return # Kết thúc hàm, trả về 204 No Content không kèm body\n    raise HTTPException(status_code=404, detail=\"Không tìm thấy sinh viên để xóa\")" },
            { "type": "h2", "text": "3. Xóa vật lý (Hard Delete) và Xóa mềm (Soft Delete)" },
            { "type": "p", "text": "Trong thực tế dự án doanh nghiệp, việc xóa bỏ hoàn toàn dữ liệu khỏi cơ sở dữ liệu (Hard Delete) là hành động mạo hiểm và có thể gây mất tính toàn vẹn dữ liệu liên kết. Thay vào đó, người ta thường dùng Xóa mềm (Soft Delete):" },
            { "type": "bullets", "items": [
                "**Xóa vật lý (Hard Delete):** Dùng lệnh `pop()` hoặc `DELETE FROM` để xóa hoàn toàn bản ghi khỏi bộ nhớ.",
                "**Xóa mềm (Soft Delete):** Thêm một trường trạng thái (ví dụ `is_deleted: bool = False` hoặc `deleted_at: datetime = None`). Khi gọi DELETE, API chỉ chuyển đổi `is_deleted = True`. Các API GET danh sách sau đó sẽ lọc bỏ các sinh viên có `is_deleted == True`."
            ]},
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Phương thức DELETE dùng để loại bỏ tài nguyên và mang tính chất idempotent.",
                "Mã HTTP 204 No Content được sử dụng để phản hồi khi xóa thành công và không cần trả về nội dung body.",
                "Xóa mềm (Soft Delete) là giải pháp tối ưu trong các dự án thực tế để bảo toàn dữ liệu lịch sử."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "MDN Web Docs - DELETE: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE"
            ]}
        ]
    }
    write_json("reading_04.json", reading_04)


    # ------------------ VIDEO SCRIPTS (4 files) ------------------
    # Video 01
    video_01 = {
        "filename": "Lesson 01 - API Create - Tạo dữ liệu với phương thức POST",
        "subdir": "Kịch bản quay video",
        "lesson_no": 1,
        "blocks": [
            { "type": "h2", "text": "## Giới thiệu về API Create và phương thức POST" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về thao tác đầu tiên trong chu trình CRUD - đó chính là API Create, hay tạo mới dữ liệu sử dụng phương thức HTTP POST." },
            { "type": "narration", "text": "Để thực hiện việc này, chúng ta cần gửi dữ liệu lên server thông qua Request Body. Sau khi server ghi nhận thành công, mã phản hồi trả về cần là 201 Created." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Cú pháp khai báo POST API trong FastAPI" },
            { "type": "narration", "text": "Hãy cùng mở mã nguồn lên để xem cách khai báo trong FastAPI. Để quy định mã trả về thành công là 201, chúng ta truyền tham số status_code vào decorator route." },
            { "type": "marker", "text": "[mở trình duyệt hiển thị code API POST sinh viên]" },
            { "type": "narration", "text": "Như các em thấy trong code, trước khi thêm sinh viên mới vào danh sách, thầy tiến hành kiểm tra xem email của sinh viên này đã tồn tại trong danh sách hay chưa. Nếu đã tồn tại, thầy ném ra lỗi HTTP 400 Bad Request. Nếu không, thầy tạo đối tượng mới với ID tự động tăng và thêm vào danh sách." },
            { "type": "marker", "text": "[mở công cụ Postman thực hiện gọi POST /students thành công và thất bại]" },
            { "type": "narration", "text": "Khi thầy gửi request POST qua Postman với email trùng, hệ thống trả ngay mã lỗi 400. Còn khi gửi email mới, kết quả trả về là 201 Created cùng thông tin đối tượng." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Như vậy, chúng ta đã hoàn thành bài học về API Create với phương thức POST và mã trạng thái 201 Created. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở bài học đọc dữ liệu tiếp theo!" }
        ]
    }
    write_json("video_01.json", video_01)

    # Video 02
    video_02 = {
        "filename": "Lesson 02 - API Read - Lấy danh sách và chi tiết dữ liệu với GET",
        "subdir": "Kịch bản quay video",
        "lesson_no": 2,
        "blocks": [
            { "type": "h2", "text": "## Phương thức GET và API đọc dữ liệu" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Hôm nay, thầy và các em sẽ đi tiếp thao tác thứ hai trong chu trình CRUD - đó là thao tác Read, sử dụng phương thức HTTP GET." },
            { "type": "narration", "text": "GET là phương thức an toàn và đồng nhất, có nhiệm vụ trả dữ liệu về mà không thay đổi bất kỳ trạng thái nào trên server." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## API lấy danh sách và tìm kiếm chi tiết" },
            { "type": "narration", "text": "Hãy cùng nhìn vào mã nguồn khai báo GET API. Để hỗ trợ tìm kiếm, chúng ta kết hợp thêm query parameter keyword trong hàm xử lý danh sách." },
            { "type": "marker", "text": "[mở trình duyệt hiển thị code API GET list và GET detail]" },
            { "type": "narration", "text": "Còn đối với API lấy chi tiết một sinh viên cụ thể theo ID, chúng ta khai báo ID dưới dạng path parameter. Thầy dùng vòng lặp để duyệt và tìm kiếm sinh viên. Nếu tìm thấy, chúng ta trả về dữ liệu. Nếu không tìm thấy, chúng ta ném ra lỗi HTTPException với mã lỗi 404 Not Found." },
            { "type": "marker", "text": "[mở Postman gọi GET /students/999 để minh họa lỗi 404]" },
            { "type": "narration", "text": "Khi thầy truyền ID sinh viên là 999 không tồn tại, Postman sẽ nhận ngay phản hồi lỗi 404 Not Found. Đây là cách xử lý lỗi cực kỳ chuẩn mực trong thiết kế API." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Tóm lại, trong bài học này các em đã biết cách lấy danh sách và thông tin chi tiết của đối tượng sử dụng GET và xử lý lỗi 404 Not Found. Cảm ơn các em đã theo dõi. Hẹn gặp lại các em ở bài học cập nhật dữ liệu!" }
        ]
    }
    write_json("video_02.json", video_02)

    # Video 03
    video_03 = {
        "filename": "Lesson 03 - API Update - Cập nhật dữ liệu với PUT",
        "subdir": "Kịch bản quay video",
        "lesson_no": 3,
        "blocks": [
            { "type": "h2", "text": "## Tìm hiểu về API Update và phương thức PUT" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Bài học hôm nay của chúng ta sẽ tập trung vào thao tác Update sử dụng phương thức HTTP PUT." },
            { "type": "narration", "text": "Khi sử dụng PUT, mục đích của chúng ta là thay thế hoặc ghi đè toàn bộ dữ liệu của một tài nguyên đang có bằng một bộ dữ liệu mới gửi lên từ client." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Khai báo API PUT và phân biệt với PATCH" },
            { "type": "narration", "text": "Bây giờ, chúng ta sẽ xem cách viết code API PUT trong FastAPI. Chúng ta cần nhận cả ID của sinh viên qua path parameter và thông tin cập nhật mới qua request body." },
            { "type": "marker", "text": "[mở trình duyệt hiển thị code API PUT]" },
            { "type": "narration", "text": "Khi tìm thấy sinh viên khớp ID, thầy thực hiện ghi đè toàn bộ trường name và email. Nếu không tìm thấy, hệ thống trả lỗi 404. Các em cũng lưu ý sự khác biệt: PUT dùng để ghi đè toàn bộ, trong khi phương thức PATCH được dùng khi chúng ta chỉ muốn cập nhật một hoặc vài thuộc tính riêng lẻ của đối tượng." },
            { "type": "marker", "text": "[mở Postman thực hiện demo API PUT]" },
            { "type": "narration", "text": "Thầy gửi yêu cầu PUT thành công, dữ liệu sinh viên đã thay đổi ngay lập tức trên danh sách in-memory của server." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Như vậy, thầy đã hướng dẫn các em nắm bắt phương thức PUT để cập nhật dữ liệu và cách phân biệt với PATCH. Cảm ơn các em và hẹn gặp lại các em ở bài học xóa dữ liệu tiếp theo!" }
        ]
    }
    write_json("video_03.json", video_03)

    # Video 04
    video_04 = {
        "filename": "Lesson 04 - API Delete - Xóa dữ liệu với phương thức DELETE",
        "subdir": "Kịch bản quay video",
        "lesson_no": 4,
        "blocks": [
            { "type": "h2", "text": "## Thao tác DELETE trong CRUD" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Chúng ta sẽ cùng nhau tìm hiểu thao tác cuối cùng trong chuỗi CRUD - đó là API Delete, sử dụng phương thức HTTP DELETE." },
            { "type": "narration", "text": "Thao tác xóa giúp chúng ta loại bỏ một tài nguyên ra khỏi hệ thống. Khi thực hiện thành công, mã trạng thái phản hồi chuẩn nhất thường là 204 No Content." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Triển khai API DELETE trong FastAPI" },
            { "type": "narration", "text": "Hãy cùng quan sát đoạn code trên màn hình. Để thiết lập mã trả về là 204, chúng ta truyền status.HTTP_204_NO_CONTENT vào decorator route." },
            { "type": "marker", "text": "[mở trình duyệt hiển thị code API DELETE]" },
            { "type": "narration", "text": "Trong hàm, nếu tìm thấy ID, thầy dùng hàm pop() để loại bỏ sinh viên khỏi danh sách và kết thúc hàm bằng lệnh return trống. Khi đó, FastAPI tự hiểu và trả về mã 204 mà không có nội dung body. Còn nếu không tìm thấy, hệ thống vẫn ném ra lỗi 404 như thường lệ." },
            { "type": "marker", "text": "[mở Postman gửi request DELETE /students/1]" },
            { "type": "narration", "text": "Các em thấy trên Postman, response trả về hoàn toàn trống rỗng nhưng mã trạng thái hiển thị rõ là 204 No Content. Đây là kết quả xóa vật lý thành công." },
            { "type": "h2", "text": "## Xóa mềm - Giải pháp thực tế doanh nghiệp" },
            { "type": "narration", "text": "Thầy cũng muốn mở rộng thêm về khái niệm Xóa mềm. Trong các dự án thực tế, người ta rất hạn chế xóa vĩnh viễn dữ liệu. Thay vào đó, chúng ta chỉ thay đổi một cờ trạng thái, ví dụ chuyển is_deleted thành True để ẩn tài nguyên đi." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Như vậy, thầy và các em đã đi qua đầy đủ 4 thao tác CRUD in-memory. Cảm ơn các em đã đồng hành cùng thầy và chúc các em thực hành tốt!" }
        ]
    }
    write_json("video_04.json", video_04)


    # ------------------ EXERCISES (6 files) ------------------
    # Exercise 01
    exercise_01 = {
        "filename": "[Vận dụng cơ bản 1] Sửa lỗi trùng lặp dữ liệu và mã trạng thái trong API POST",
        "subdir": "Bài tập",
        "level": "Vận dụng cơ bản",
        "blocks": [
            { "type": "h1", "text": "Kiểm soát trùng lặp và mã phản hồi chuẩn cho API POST" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Một lập trình viên backend đã viết một API POST để thêm học viên mới vào danh sách. Tuy nhiên, API này đang gặp hai vấn đề nghiêm trọng: một là cho phép thêm các học viên trùng lặp email, hai là trả về mã trạng thái mặc định 200 OK thay vì mã chuẩn 201 Created." },
            { "type": "h2", "text": "2. Vấn đề hiện tại" },
            { "type": "p", "text": "Học viên cần xác định lỗi logic trong code, sửa lại để chặn trùng lặp email và cấu hình đúng mã phản hồi HTTP 201." },
            { "type": "h2", "text": "3. Mã nguồn hiện tại (Legacy Code)" },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\nstudents_db = []\n\nclass StudentCreate(BaseModel):\n    name: str\n    email: str\n\n# Đang sử dụng mã mặc định 200 và chưa kiểm tra email trùng\n@app.post(\"/students\")\ndef add_student(student: StudentCreate):\n    new_student = {\"id\": len(students_db) + 1, \"name\": student.name, \"email\": student.email}\n    students_db.append(new_student)\n    return new_student" },
            { "type": "h2", "text": "4. Yêu cầu đầu ra" },
            { "type": "h3", "text": "Nhiệm vụ 1: Phân tích lỗi" },
            { "type": "bullets", "items": [
                "Giải thích vì sao mã 201 Created phù hợp hơn mã 200 OK cho thao tác tạo mới dữ liệu.",
                "Chỉ ra rủi ro khi hệ thống để lọt email trùng lặp."
            ]},
            { "type": "h3", "text": "Nhiệm vụ 2: Viết mã nguồn sửa đổi" },
            { "type": "bullets", "items": [
                "Chỉnh sửa route decorator để thiết lập `status_code=201`.",
                "Dùng vòng lặp kiểm tra trùng lặp email, nếu trùng ném ra lỗi `HTTPException` với mã lỗi `400 Bad Request`."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session05", "ex": "Ex01",
            "example": "HNKS25CNTT1_FastAPI_Session05_Ex01"
        }
    }
    write_json("exercise_01.json", exercise_01)

    # Exercise 02
    exercise_02 = {
        "filename": "[Vận dụng cơ bản 2] Bổ sung kiểm tra lỗi 404 cho API xóa và cập nhật",
        "subdir": "Bài tập",
        "level": "Vận dụng cơ bản",
        "blocks": [
            { "type": "h1", "text": "Xử lý lỗi 404 Not Found khi xóa và sửa đổi tài nguyên" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Trong ứng dụng quản lý, khi client gửi request yêu cầu cập nhật hoặc xóa một học viên theo ID, hệ thống phải kiểm tra xem học viên đó có tồn tại hay không. Nếu không, hệ thống cần phản hồi lỗi 404 Not Found thay vì chạy tiếp dẫn đến lỗi runtime hoặc trả về kết quả thành công giả." },
            { "type": "h2", "text": "2. Mã nguồn hiện tại (Legacy Code)" },
            { "type": "code", "lang": "python", "text": "from fastapi import FastAPI\n\napp = FastAPI()\nstudents_db = [{\"id\": 1, \"name\": \"Nguyen Van An\", \"email\": \"an@gmail.com\"}]\n\n# Chưa kiểm tra ID tồn tại trước khi xóa\n@app.delete(\"/students/{student_id}\")\ndef delete_student(student_id: int):\n    global students_db\n    students_db = [s for s in students_db if s[\"id\"] != student_id]\n    return {\"message\": \"Xóa thành công\"}" },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "h3", "text": "Nhiệm vụ 1: Triển khai mã nguồn mới" },
            { "type": "bullets", "items": [
                "Sửa đổi API DELETE để kiểm tra xem `student_id` có tồn tại trong `students_db` hay không.",
                "Nếu không tồn tại, ném lỗi 404 Not Found.",
                "Nếu tồn tại, thực hiện xóa và trả về mã trạng thái HTTP 204 No Content."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session05", "ex": "Ex02",
            "example": "HNKS25CNTT1_FastAPI_Session05_Ex02"
        }
    }
    write_json("exercise_02.json", exercise_02)

    # Exercise 03
    exercise_03 = {
        "filename": "[Vận dụng chuyên sâu] Triển khai API PATCH cập nhật từng phần",
        "subdir": "Bài tập",
        "level": "Vận dụng chuyên sâu",
        "blocks": [
            { "type": "h1", "text": "Phát triển tính năng cập nhật từng phần với PATCH" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Mặc dù phương thức PUT rất phổ biến, nhưng đôi khi người dùng chỉ muốn sửa đổi một thuộc tính duy nhất (ví dụ: chỉ sửa đổi email của học viên mà giữ nguyên họ tên). Nếu dùng PUT, người dùng buộc phải gửi lại cả họ tên cũ. Giải pháp thay thế tối ưu là sử dụng phương thức PATCH." },
            { "type": "h2", "text": "2. Quy tắc nghiệp vụ" },
            { "type": "bullets", "items": [
                "Sử dụng decorator `@app.patch`.",
                "Schema nhận vào phải cho phép các trường có giá trị tùy chọn (tất cả các trường đều có mặc định là None).",
                "Chỉ cập nhật những thuộc tính được client gửi lên thực sự trong request body."
            ]},
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "h3", "text": "(1) Thiết kế Pydantic Schema cho PATCH" },
            { "type": "bullets", "items": [
                "Tạo `StudentPatchSchema` với các trường `name: str | None = None` và `email: str | None = None`."
            ]},
            { "type": "h3", "text": "(2) Viết logic cập nhật động" },
            { "type": "bullets", "items": [
                "Duyệt danh sách tìm kiếm học viên theo ID.",
                "Sử dụng hàm `.dict(exclude_unset=True)` của Pydantic để chỉ lấy ra các trường được truyền lên và cập nhật vào đối tượng gốc.",
                "Trả lỗi 404 nếu không tìm thấy."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session05", "ex": "Ex03",
            "example": "HNKS25CNTT1_FastAPI_Session05_Ex03"
        }
    }
    write_json("exercise_03.json", exercise_03)

    # Exercise 04
    exercise_04 = {
        "filename": "[Phân tích] Phân tích tính Idempotent của các phương thức HTTP",
        "subdir": "Bài tập",
        "level": "Phân tích",
        "blocks": [
            { "type": "h1", "text": "Phân tích so sánh tính Idempotent của các HTTP Methods" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Khi thiết kế hệ thống API chịu tải lớn và có khả năng xảy ra mất kết nối giữa chừng, tính chất Idempotent (đồng nhất kết quả khi gọi nhiều lần) của các phương thức HTTP đóng vai trò quyết định thiết kế an toàn hệ thống." },
            { "type": "h2", "text": "2. Yêu cầu phân tích" },
            { "type": "p", "text": "Sinh viên cần lập bảng phân tích so sánh tính chất an toàn (Safe) và tính chất đồng nhất (Idempotent) của 4 phương thức HTTP GET, POST, PUT, DELETE." },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "h3", "text": "(1) Lập bảng so sánh" },
            { "type": "table", "headers": ["Phương thức HTTP", "Safe (An toàn)", "Idempotent (Đồng nhất)", "Mô tả hành vi khi gọi liên tiếp"], "rows": [
                ["GET", "", "", ""],
                ["POST", "", "", ""],
                ["PUT", "", "", ""],
                ["DELETE", "", "", ""]
            ]},
            { "type": "h3", "text": "(2) Giải thích ứng dụng thực tế" },
            { "type": "bullets", "items": [
                "Giải thích vì sao DELETE được coi là idempotent mặc dù lần gọi thứ 2 có thể trả về lỗi 404 thay vì 204.",
                "Vì sao không được dùng GET để thực hiện hành động xóa hoặc thay đổi dữ liệu."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session05", "ex": "Ex04",
            "example": "HNKS25CNTT1_FastAPI_Session05_Ex04"
        }
    }
    write_json("exercise_04.json", exercise_04)

    # Exercise 05
    exercise_05 = {
        "filename": "[Sáng tạo] Thiết kế cơ chế Xóa mềm (Soft Delete) trong FastAPI",
        "subdir": "Bài tập",
        "level": "Sáng tạo",
        "blocks": [
            { "type": "h1", "text": "Xây dựng cơ chế ẩn dữ liệu (Soft Delete)" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Để bảo toàn lịch sử hoạt động và tránh lỗi liên kết dữ liệu trong các dự án thực tế, người ta thường dùng Xóa mềm (Soft Delete) thay vì xóa vật lý khỏi bộ nhớ." },
            { "type": "h2", "text": "2. Thử thách Sáng tạo" },
            { "type": "p", "text": "Hãy tự thiết kế và cài đặt một hệ thống API quản lý sinh viên có hỗ trợ Xóa mềm. Mỗi sinh viên ban đầu có thuộc tính `is_deleted = False`." },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Viết API DELETE `/students/{student_id}` thực hiện chuyển đổi `is_deleted = True` thay vì dùng pop().",
                "Chỉnh sửa API GET `/students` để mặc định chỉ trả về các học viên chưa bị xóa (is_deleted == False).",
                "Viết thêm một API đặc biệt dành cho Admin: GET `/students/trash` để hiển thị danh sách các học viên đã bị xóa mềm, hỗ trợ khôi phục dữ liệu."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session05", "ex": "Ex05",
            "example": "HNKS25CNTT1_FastAPI_Session05_Ex05"
        }
    }
    write_json("exercise_05.json", exercise_05)

    # Exercise 06
    exercise_06 = {
        "filename": "[BTTH] Phát triển ứng dụng quản lý sách thư viện hoàn chỉnh",
        "subdir": "Bài tập",
        "level": "Tổng hợp",
        "blocks": [
            { "type": "h1", "text": "Bài tập thực hành tổng hợp: CRUD Thư viện Sách" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Học viên cần xây dựng một ứng dụng nhỏ quản lý sách trong thư viện trường học in-memory đầy đủ 4 thao tác tạo mới, lấy danh sách, sửa đổi và xóa sách." },
            { "type": "h2", "text": "2. Yêu cầu kỹ thuật" },
            { "type": "bullets", "items": [
                "POST `/books`: Thêm sách mới gồm `title` (str, >=2 ký tự), `author` (str), `isbn` (str, phải duy nhất). Trả về 201 Created.",
                "GET `/books`: Trả về danh sách sách, hỗ trợ lọc theo query `author` (tùy chọn).",
                "GET `/books/{book_id}`: Trả về chi tiết sách theo ID, lỗi 404 nếu không tìm thấy.",
                "PUT `/books/{book_id}`: Ghi đè cập nhật sách, lỗi 404 nếu không thấy.",
                "DELETE `/books/{book_id}`: Xóa sách, trả về 204 No Content, lỗi 404 nếu không thấy."
            ]},
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Viết file `main.py` hoàn chỉnh, cấu hình đầy đủ Pydantic Schemas và chạy được bằng Uvicorn.",
                "Thực hiện demo đầy đủ cả 5 API trên Swagger UI."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session05", "ex": "Ex06",
            "example": "HNKS25CNTT1_FastAPI_Session05_Ex06"
        }
    }
    write_json("exercise_06.json", exercise_06)


    # ------------------ QUIZZES (2 files) ------------------
    # Quiz Đầu giờ
    quiz_daugio = {
        "sheet_name": "Quiz_DauGio_FastAPI_05",
        "questions": [
            # 12 câu ôn bài cũ (Session 04)
            {
                "q": "Nếu route khai báo là /users/{id} và ta muốn id chỉ nhận giá trị lớn hơn hoặc bằng 1, ta cấu hình như thế nào?",
                "answers": ["id: int = Path(..., gt=1)", "id: int = Path(..., ge=1)", "id: int = Query(..., ge=1)", "id: int = Field(..., ge=1)"],
                "explanations": ["gt là lớn hơn hẳn (Greater Than).", "Chính xác, ge là lớn hơn hoặc bằng (Greater than or Equal) và sử dụng Path() cho path parameter.", "Query() dùng cho query parameter.", "Field() dùng cho thuộc tính trong BaseModel."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Tham số nào của hàm được xem là Query Parameter mặc định trong FastAPI?",
                "answers": [
                    "Tham số nằm trong ngoặc nhọn {} ở route decorator",
                    "Tham số kế thừa từ BaseModel của Pydantic",
                    "Tham số không nằm trong route path và có kiểu dữ liệu nguyên thủy (số, chuỗi, boolean)",
                    "Tham số được khai báo trong Request Body"
                ],
                "explanations": ["Đó là Path Parameter.", "Đó là Request Body.", "Chính xác, FastAPI tự động phân giải các tham số này từ query string trên URL.", "Không đúng."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Khi validate dữ liệu thất bại, FastAPI mặc định trả về mã lỗi HTTP nào?",
                "answers": ["400 Bad Request", "404 Not Found", "500 Internal Server Error", "422 Unprocessable Entity"],
                "explanations": ["Lỗi request không hợp lệ nói chung.", "Lỗi không tìm thấy tài nguyên.", "Lỗi hệ thống phía server.", "Chính xác, mã 422 được tự động sinh kèm thông tin chi tiết lỗi."],
                "correct": 4, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Từ khóa nào đại diện cho giá trị bắt buộc truyền khi sử dụng Path() hoặc Query()?",
                "answers": ["None", "Required", "... (Ellipsis)", "True"],
                "explanations": ["None biểu thị tham số tùy chọn.", "Không phải cú pháp Python.", "Chính xác, dấu ba chấm biểu thị giá trị bắt buộc phải có.", "Không đúng."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Trường 'loc' trong JSON lỗi 422 của FastAPI dùng để chỉ ra điều gì?",
                "answers": ["Thời gian xảy ra lỗi", "Vị trí của tham số gây lỗi trong request", "Mô tả thông điệp lỗi bằng tiếng Anh", "Loại lỗi lập trình"],
                "explanations": ["Không đúng.", "Chính xác, loc viết tắt của Location (ví dụ: ['body', 'email'] chỉ ra email trong request body bị lỗi).", "Đó là trường msg.", "Đó là trường type."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Hàm Field() dùng để đặt ràng buộc dữ liệu được import từ thư viện nào?",
                "answers": ["fastapi", "starlette", "pydantic", "typing"],
                "explanations": ["FastAPI cung cấp Query và Path.", "Không cung cấp Field.", "Chính xác, Field() được cung cấp bởi pydantic.", "Cung cấp các type hint."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Đâu là quy tắc vàng để tránh xung đột đường dẫn route trong FastAPI?",
                "answers": [
                    "Khai báo route động trước, route tĩnh sau",
                    "Đặt tên các route hoàn toàn giống nhau",
                    "Luôn khai báo route tĩnh lên trước các route động",
                    "Không được dùng quá 2 route trong ứng dụng"
                ],
                "explanations": ["Gây xung đột lỗi 422.", "Gây lỗi đè route.", "Chính xác, đặt route cụ thể lên trước giúp FastAPI định tuyến chính xác.", "Không đúng."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Pydantic BaseModel chủ yếu được dùng để làm gì khi khai báo ở tham số hàm POST?",
                "answers": [
                    "Đọc dữ liệu từ Path Parameter",
                    "Định nghĩa cấu trúc (schema) và đại diện cho dữ liệu nhận từ Request Body",
                    "Tự động kết nối tới cơ sở dữ liệu MySQL",
                    "Render giao diện trang web"
                ],
                "explanations": ["Không đúng.", "Chính xác, giúp nhận và kiểm chứng dữ liệu JSON gửi lên từ client.", "Đó là ORM model.", "Không đúng."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Để kiểm tra định dạng email bằng regex trong Field() của Pydantic v2, ta dùng tham số nào?",
                "answers": ["regex", "pattern", "format", "match"],
                "explanations": ["Đã bị bỏ ở bản cũ.", "Chính xác, pattern nhận biểu thức chính quy để kiểm tra định dạng chuỗi.", "Không đúng.", "Không đúng."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Ý nghĩa của tham số response_model trong route decorator là gì?",
                "answers": [
                    "Tăng tốc độ xử lý của API",
                    "Chuẩn hóa dữ liệu đầu ra và tự động lọc bỏ các trường thông tin nhạy cảm trước khi trả về client",
                    "Tự động kết nối với MySQL",
                    "Quy định kiểu dữ liệu của request body"
                ],
                "explanations": ["Không ảnh hưởng tốc độ.", "Chính xác, ví dụ dùng để ẩn mật khẩu người dùng trước khi phản hồi.", "Không đúng.", "Đó là Pydantic model trong tham số hàm."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Trong Python, làm thế nào để khai báo một trường tùy chọn kiểu chuỗi có mặc định là None?",
                "answers": ["email: str", "email: str | None = None", "email: Optional", "email: None = str"],
                "explanations": ["Đây là trường bắt buộc.", "Chính xác, cú pháp Union type hoặc Optional giúp biểu thị trường tùy chọn.", "Không đúng cú pháp gán mặc định.", "Sai cú pháp."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Khi validate thành công, đối tượng Pydantic có thể chuyển đổi thành kiểu Dictionary của Python bằng phương thức nào?",
                "answers": ["to_dict()", "dict()", "json()", "convert()"],
                "explanations": ["Không đúng.", "Chính xác, student.dict() (hoặc model_dump() trong Pydantic v2).", "Chuyển thành chuỗi JSON.", "Không đúng."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            # 8 câu bài mới (Session 05)
            {
                "q": "Trong chu trình CRUD, thao tác 'Create' thường ánh xạ tới phương thức HTTP nào?",
                "answers": ["GET", "POST", "PUT", "DELETE"],
                "explanations": ["GET dùng cho Read.", "Chính xác, POST dùng cho Create.", "PUT dùng cho Update.", "DELETE dùng cho Delete."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Mã trạng thái HTTP chuẩn nhất biểu thị việc tạo mới tài nguyên thành công là gì?",
                "answers": ["200 OK", "201 Created", "204 No Content", "400 Bad Request"],
                "explanations": ["Dùng cho các thao tác thành công chung.", "Chính xác, 201 Created.", "Dùng khi thành công nhưng không có nội dung trả về.", "Dùng khi request bị lỗi cú pháp."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Phương thức HTTP nào được thiết kế để ghi đè toàn bộ thông tin của tài nguyên đang tồn tại?",
                "answers": ["POST", "PATCH", "PUT", "GET"],
                "explanations": ["Dùng để tạo mới.", "Dùng để cập nhật từng phần.", "Chính xác, PUT ghi đè toàn bộ tài nguyên.", "Dùng để đọc."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Nếu xóa tài nguyên thành công và server không muốn gửi lại bất kỳ dữ liệu nào trong body, mã HTTP phản hồi là gì?",
                "answers": ["200 OK", "201 Created", "204 No Content", "404 Not Found"],
                "explanations": ["Trả về dữ liệu kèm body.", "Dùng cho tạo mới.", "Chính xác, 204 No Content biểu thị thành công và body trống.", "Không tìm thấy tài nguyên."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Tính chất 'Idempotent' của một phương thức HTTP có nghĩa là gì?",
                "answers": [
                    "Phương thức đó chạy rất nhanh",
                    "Thực hiện gọi API nhiều lần liên tiếp với cùng dữ liệu luôn cho kết quả trạng thái hệ thống giống nhau",
                    "Yêu cầu phải có mật khẩu xác thực",
                    "Không cho phép truyền tham số"
                ],
                "explanations": ["Không đúng.", "Chính xác, ví dụ gọi PUT sửa thông tin hoặc DELETE xóa đối tượng nhiều lần thì kết quả cuối cùng đối tượng vẫn chỉ bị sửa/xóa như vậy.", "Không đúng.", "Không đúng."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Cơ chế 'Soft Delete' (Xóa mềm) hoạt động như thế nào trong thực tế?",
                "answers": [
                    "Xóa hoàn toàn dữ liệu khỏi RAM",
                    "Chỉ xóa dữ liệu khi máy tính tắt",
                    "Thay đổi trạng thái của cờ đánh dấu (ví dụ is_deleted = True) thay vì xóa vật lý khỏi database",
                    "Tự động gửi email thông báo cho người dùng khi xóa"
                ],
                "explanations": ["Đó là xóa vật lý.", "Không đúng.", "Chính xác, giúp bảo toàn tính toàn vẹn dữ liệu và lưu lịch sử.", "Không đúng."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Để ném ra lỗi không tìm thấy tài nguyên khi client gọi GET hoặc DELETE sai ID, ta dùng cú pháp nào?",
                "answers": [
                    "raise HTTPException(status_code=400, detail='...')",
                    "raise HTTPException(status_code=404, detail='...')",
                    "return {'error': 'Not Found'}",
                    "sys.exit(1)"
                ],
                "explanations": ["400 là Bad Request.", "Chính xác, mã 404 biểu thị Not Found.", "Chỉ trả về dict thường, mã HTTP phản hồi vẫn là 200 OK.", "Dừng ứng dụng server lập tức, gây crash."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Sự khác biệt lớn nhất giữa PUT và PATCH là gì?",
                "answers": [
                    "PUT chạy nhanh hơn PATCH",
                    "PUT ghi đè toàn bộ thuộc tính; PATCH chỉ cập nhật các thuộc tính được truyền lên (cập nhật từng phần)",
                    "PATCH là phương thức an toàn (safe), PUT thì không",
                    "FastAPI không hỗ trợ PATCH, chỉ hỗ trợ PUT"
                ],
                "explanations": ["Hiệu năng tương đương.", "Chính xác, đây là quy chuẩn thiết kế RESTful.", "Cả hai đều là update không safe.", "FastAPI hỗ trợ đầy đủ các phương thức."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            }
        ]
    }
    write_json("quiz_daugio.json", quiz_daugio)

    # Quiz Cuối giờ
    quiz_cuoigio = {
        "sheet_name": "Quiz_CuoiGio_FastAPI_05",
        "questions": [
            {
                "q": "Để khai báo mã trạng thái HTTP trả về mặc định khi gọi API thành công trong route decorator, ta dùng đối số nào?",
                "answers": ["code", "status", "status_code", "response_status"],
                "explanations": ["Không đúng.", "Không đúng.", "Chính xác, ví dụ: @app.post('/...', status_code=201).", "Không đúng."],
                "correct": 3, "difficulty": 5, "category": "DECORATOR"
            },
            {
                "q": "Khi thực hiện API POST tạo mới đối tượng, nếu phát hiện email gửi lên đã tồn tại trong danh sách, lập trình viên nên xử lý như thế nào?",
                "answers": [
                    "Vẫn cho ghi đè đè lên đối tượng cũ",
                    "Ném ra lỗi HTTPException với mã lỗi 400 Bad Request để thông báo email đã tồn tại",
                    "Trả về thông tin đối tượng cũ với mã 201 Created",
                    "Crash server bằng lệnh exit"
                ],
                "explanations": [
                    "Gây mất dữ liệu người dùng cũ.",
                    "Chính xác, đây là cách validate logic nghiệp vụ cơ bản.",
                    "Sai logic nghiệp vụ và mã phản hồi.",
                    "Không được phép làm sập ứng dụng."
                ],
                "correct": 2, "difficulty": 6, "category": "VALIDATION"
            },
            {
                "q": "Vì sao phương thức HTTP GET được coi là an toàn (safe)?",
                "answers": [
                    "Vì dữ liệu truyền lên luôn được mã hóa",
                    "Vì nó chỉ thực hiện đọc dữ liệu và không làm thay đổi trạng thái tài nguyên trên máy chủ",
                    "Vì nó không cho phép truyền bất kỳ tham số nào",
                    "Vì nó bắt buộc phải chạy qua giao thức HTTPS"
                ],
                "explanations": [
                    "Không đúng.",
                    "Chính xác, GET không làm ghi nhận mới, sửa đổi hay xóa dữ liệu.",
                    "GET cho phép truyền query và path parameters.",
                    "GET chạy được cả trên HTTP."
                ],
                "correct": 2, "difficulty": 6, "category": "SAFE_METHOD"
            },
            {
                "q": "Thao tác cập nhật in-memory list bằng PUT yêu cầu logic xử lý nào sau khi tìm thấy ID khớp?",
                "answers": [
                    "Xóa phần tử cũ đi và dùng append() thêm phần tử mới",
                    "Ghi đè giá trị mới lên các thuộc tính tương ứng của phần tử cũ",
                    "Chuyển đổi cờ is_deleted sang True",
                    "Trả về lỗi 400 Bad Request"
                ],
                "explanations": [
                    "Không cần thiết và thay đổi thứ tự phần tử.",
                    "Chính xác, ghi đè giá trị giúp giữ nguyên tham chiếu đối tượng trong danh sách.",
                    "Đây là thao tác xóa mềm.",
                    "Thao tác thành công nên không trả lỗi 400."
                ],
                "correct": 2, "difficulty": 6, "category": "UPDATE"
            },
            {
                "q": "Khi xóa thành công một đối tượng và trả về mã trạng thái HTTP 204 No Content, body của HTTP response sẽ chứa thông tin gì?",
                "answers": [
                    "Chuỗi JSON {'message': 'Success'}",
                    "Hoàn toàn trống rỗng (không chứa dữ liệu)",
                    "Mã ID của đối tượng vừa bị xóa",
                    "Thông tin chi tiết đối tượng bị xóa để đối chiếu"
                ],
                "explanations": [
                    "Mã 204 yêu cầu body phải trống.",
                    "Chính xác, No Content nghĩa là không có nội dung body.",
                    "Không đúng.",
                    "Không đúng."
                ],
                "correct": 2, "difficulty": 7, "category": "DELETE"
            },
            {
                "q": "Trong thực tế, khi triển khai API DELETE, phương thức nào dưới đây an toàn hơn để bảo toàn lịch sử dữ liệu?",
                "answers": ["Xóa vật lý (Hard Delete)", "Xóa mềm (Soft Delete)", "Reset lại toàn bộ máy chủ", "Tự động sao lưu dữ liệu sang ổ đĩa khác rồi xóa vật lý"],
                "explanations": [
                    "Mất dữ liệu vĩnh viễn và có thể gây lỗi khóa ngoại.",
                    "Chính xác, chỉ cập nhật cờ ẩn dữ liệu giúp khôi phục dễ dàng.",
                    "Gây gián đoạn dịch vụ toàn bộ hệ thống.",
                    "Tốn kém tài nguyên và phức tạp."
                ],
                "correct": 2, "difficulty": 5, "category": "SOFT_DELETE"
            },
            {
                "q": "Khi client gọi API GET /students/100 (trong đó ID 100 không tồn tại), mã trạng thái HTTP nào là chuẩn nhất để trả về?",
                "answers": ["200 OK", "400 Bad Request", "404 Not Found", "500 Internal Server Error"],
                "explanations": [
                    "Không đúng, API thất bại.",
                    "Lỗi cú pháp request, còn ở đây request đúng cú pháp nhưng không có dữ liệu.",
                    "Chính xác, 404 Not Found biểu thị tài nguyên không tồn tại.",
                    "Lỗi hệ thống phía server."
                ],
                "correct": 3, "difficulty": 5, "category": "READ"
            },
            {
                "q": "Đối với API GET danh sách sinh viên, việc truyền thêm tham số keyword: str = '' đóng vai trò gì?",
                "answers": [
                    "Là path parameter bắt buộc để định vị sinh viên",
                    "Là query parameter tùy chọn dùng để lọc kết quả theo tên sinh viên",
                    "Là request body nhận dữ liệu JSON",
                    "Là cấu hình bảo mật bắt buộc"
                ],
                "explanations": [
                    "Không đúng.",
                    "Chính xác, mặc định chuỗi rỗng để trả về toàn bộ nếu không truyền keyword.",
                    "Không đúng.",
                    "Không liên quan."
                ],
                "correct": 2, "difficulty": 5, "category": "READ"
            },
            {
                "q": "Thao tác cập nhật từng phần (PATCH) trong Pydantic được thực hiện thuận tiện nhờ phương thức chuyển đổi dữ liệu nào?",
                "answers": [
                    "student.dict(exclude_unset=True)",
                    "student.dict()",
                    "student.json()",
                    "str(student)"
                ],
                "explanations": [
                    "Chính xác, exclude_unset=True giúp loại bỏ các trường client không truyền lên (giữ lại None mặc định).",
                    "Phương thức này sẽ lấy toàn bộ các trường kể cả các trường mặc định None.",
                    "Trả về chuỗi JSON.",
                    "Trả về chuỗi biểu diễn đối tượng."
                ],
                "correct": 1, "difficulty": 8, "category": "PATCH"
            },
            {
                "q": "Khi thiết kế RESTful API, Endpoint dùng để xóa sinh viên có ID là 5 nên đặt đường dẫn và phương thức nào?",
                "answers": [
                    "GET /students/delete/5",
                    "DELETE /students/5",
                    "POST /students/5/delete",
                    "PUT /students/5"
                ],
                "explanations": [
                    "Sai phương thức và vi phạm RESTful naming.",
                    "Chính xác, dùng đúng phương thức DELETE và path parameter định danh tài nguyên.",
                    "Sai phương thức.",
                    "PUT dùng cho cập nhật ghi đè."
                ],
                "correct": 2, "difficulty": 6, "category": "REST_DESIGN"
            },
            {
                "q": "Phương thức HTTP POST có tính chất Idempotent hay không?",
                "answers": [
                    "Có, luôn trả về cùng kết quả",
                    "Không, mỗi lần gọi POST thành công thường tạo thêm một tài nguyên mới trong hệ thống",
                    "Có, chỉ khi chạy trên máy chủ Uvicorn",
                    "Không, nhưng có tính chất Safe"
                ],
                "explanations": [
                    "Không đúng.",
                    "Chính xác, gọi nhiều lần sinh ra nhiều tài nguyên khác nhau.",
                    "Không liên quan tới máy chủ.",
                    "POST không an toàn vì làm thay đổi trạng thái máy chủ."
                ],
                "correct": 2, "difficulty": 6, "category": "POST"
            },
            {
                "q": "Khi viết hàm delete_student(student_id: int) thao tác trên list in-memory của Python, từ khóa nào cần dùng để thay đổi danh sách bên ngoài phạm vi hàm?",
                "answers": ["local", "nonlocal", "global", "import"],
                "explanations": [
                    "Không đúng.",
                    "Dùng cho hàm lồng nhau.",
                    "Chính xác, sử dụng global students_db để khai báo biến danh sách toàn cục.",
                    "Dùng để import thư viện."
                ],
                "correct": 3, "difficulty": 6, "category": "PYTHON"
            },
            {
                "q": "Tại sao không nên dùng phương thức HTTP GET cho hành động xóa dữ liệu?",
                "answers": [
                    "Vì GET không hỗ trợ truyền tham số",
                    "Vì các công cụ tìm kiếm (crawler) hoặc trình duyệt có thể tự động gọi trước (prefetch) các link GET, dẫn tới vô tình xóa sạch dữ liệu hệ thống",
                    "Vì GET chạy chậm hơn các phương thức khác",
                    "Vì dữ liệu xóa bằng GET sẽ bị lỗi hiển thị"
                ],
                "explanations": [
                    "GET hỗ trợ truyền tham số trên URL.",
                    "Chính xác, đây là lỗ hổng bảo mật nghiêm trọng nếu dùng GET để thay đổi trạng thái hệ thống.",
                    "Tốc độ tương đương.",
                    "Không liên quan."
                ],
                "correct": 2, "difficulty": 7, "category": "REST_DESIGN"
            },
            {
                "q": "Nếu client gửi request PUT đến /students/5 mà thiếu trường email bắt buộc trong schema, FastAPI phản hồi lỗi gì?",
                "answers": ["400 Bad Request", "404 Not Found", "422 Unprocessable Entity", "500 Internal Server Error"],
                "explanations": [
                    "Không đúng.",
                    "Không đúng.",
                    "Chính xác, do dữ liệu không vượt qua bước validate cấu trúc Pydantic của request body.",
                    "Không đúng."
                ],
                "correct": 3, "difficulty": 5, "category": "VALIDATION"
            },
            {
                "q": "Khi thực hiện xóa mềm (Soft Delete), API GET lấy danh sách thông thường cần bổ sung logic gì?",
                "answers": [
                    "Không cần bổ sung gì",
                    "Chỉ lấy các phần tử có cờ trạng thái is_deleted == False",
                    "Xóa sạch bộ nhớ cache",
                    "Tự động phục hồi các bản ghi đã xóa"
                ],
                "explanations": [
                    "Sẽ hiển thị cả đối tượng đã bị xóa mềm.",
                    "Chính xác, lọc bỏ các đối tượng đã bị đánh dấu xóa mềm để ẩn chúng khỏi danh sách hiển thị thông thường.",
                    "Không liên quan.",
                    "Không đúng."
                ],
                "correct": 2, "difficulty": 6, "category": "SOFT_DELETE"
            }
        ]
    }
    write_json("quiz_cuoigio.json", quiz_cuoigio)


    # ------------------ MINDMAP ------------------
    mindmap = {
        "filename": "Session 05 - CRUD co ban",
        "subdir": "Mindmap",
        "root": "Thao tác CRUD cơ bản in-memory",
        "children": [
            {
                "title": "1. Create (Tạo dữ liệu)",
                "children": [
                    { "title": "HTTP Method: POST" },
                    { "title": "HTTP Status Code: 201 Created" },
                    { "title": "Logic nghiệp vụ: Kiểm tra trùng lặp email/ID trước khi lưu" }
                ]
            },
            {
                "title": "2. Read (Đọc dữ liệu)",
                "children": [
                    { "title": "HTTP Method: GET" },
                    { "title": "HTTP Status Code: 200 OK" },
                    { "title": "GET list: Lọc danh sách theo Query Parameter keyword" },
                    { "title": "GET detail: Lấy theo ID, trả lỗi 404 Not Found nếu không tồn tại" }
                ]
            },
            {
                "title": "3. Update (Cập nhật)",
                "children": [
                    { "title": "HTTP Method: PUT (Ghi đè toàn bộ tài nguyên)" },
                    { "title": "HTTP Method: PATCH (Cập nhật từng phần linh hoạt)" },
                    { "title": "Tính chất: Idempotent (cập nhật nhiều lần cùng kết quả)" },
                    { "title": "Xử lý lỗi: Trả 404 Not Found nếu ID không hợp lệ" }
                ]
            },
            {
                "title": "4. Delete (Xóa dữ liệu)",
                "children": [
                    { "title": "HTTP Method: DELETE" },
                    { "title": "HTTP Status Code: 204 No Content (thành công, body trống)" },
                    { "title": "Hard Delete (Xóa vật lý): Xóa vĩnh viễn bằng pop() hoặc DELETE FROM" },
                    { "title": "Soft Delete (Xóa mềm): Đổi cờ trạng thái is_deleted = True để bảo toàn dữ liệu" }
                ]
            }
        ]
    }
    write_json("mindmap.json", mindmap)


    # ------------------ SLIDE OUTLINE ------------------
    slide_outline = {
        "filename": "Session 05 - CRUD co ban",
        "subdir": "Bài giảng",
        "title": "CRUD cơ bản",
        "module": "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI",
        "version": "1.0",
        "slides": [
            {
                "layout": "title",
                "title": "CRUD cơ bản",
                "content": ["Session 05", "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI", "Phiên bản: 1.0"]
            },
            {
                "layout": "agenda",
                "section": "NỘI DUNG",
                "title": "Nội dung bài học",
                "content": [
                    "1. API Create: Tạo dữ liệu (POST)",
                    "2. API Read: Đọc dữ liệu (GET)",
                    "3. API Update: Cập nhật dữ liệu (PUT)",
                    "4. API Delete: Xóa dữ liệu (DELETE)"
                ]
            },
            # Lesson 1
            {
                "layout": "section-title",
                "section": "1. API Create",
                "title": "Phần 1: API Create - Tạo mới dữ liệu",
                "content": ["Phương thức HTTP POST", "Mã phản hồi 201 Created", "Kiểm tra trùng lặp in-memory"]
            },
            {
                "layout": "bullets",
                "section": "1. API Create",
                "title": "Thao tác Create với POST",
                "content": [
                    "Dùng để gửi dữ liệu từ Request Body lên server nhằm tạo tài nguyên mới.",
                    "Không mang tính chất idempotent: mỗi lần gọi POST thành công sinh ra 1 tài nguyên mới.",
                    "Phản hồi thành công: HTTP 201 Created kèm đối tượng vừa tạo."
                ]
            },
            {
                "layout": "code",
                "section": "1. API Create",
                "title": "Triển khai POST API trong FastAPI",
                "content": [
                    "@app.post(\"/students\", status_code=201)\ndef create(student: StudentCreate):\n    # logic validate email trùng lặp\n    # append vào list in-memory\n    return new_student"
                ],
                "speaker_notes": "Hướng dẫn cấu hình status_code=201 trong decorator và xử lý trùng lặp email."
            },
            # Lesson 2
            {
                "layout": "section-title",
                "section": "2. API Read",
                "title": "Phần 2: API Read - Truy xuất dữ liệu",
                "content": ["Phương thức HTTP GET", "Lọc danh sách theo keyword", "Xử lý chi tiết và lỗi 404 Not Found"]
            },
            {
                "layout": "bullets",
                "section": "2. API Read",
                "title": "Thao tác Read với GET",
                "content": [
                    "Đọc dữ liệu từ server, mang tính chất an toàn (Safe) và đồng nhất (Idempotent).",
                    "GET /students: Lấy danh sách toàn bộ, kết hợp query parameter để tìm kiếm.",
                    "GET /students/{id}: Lấy chi tiết. Trả về 404 Not Found nếu ID không tồn tại."
                ]
            },
            {
                "layout": "code",
                "section": "2. API Read",
                "title": "Triển khai GET API trong FastAPI",
                "content": [
                    "@app.get(\"/students/{student_id}\")\ndef detail(student_id: int):\n    # tìm sinh viên khớp ID\n    # không thấy -> raise HTTPException(status_code=404)\n    return student"
                ],
                "speaker_notes": "Giải thích mã lỗi 404 Not Found và cách ném lỗi với HTTPException."
            },
            # Lesson 3
            {
                "layout": "section-title",
                "section": "3. API Update",
                "title": "Phần 3: API Update - Cập nhật dữ liệu",
                "content": ["Phương thức HTTP PUT", "Tính chất ghi đè toàn bộ", "Phân biệt PUT và PATCH"]
            },
            {
                "layout": "bullets",
                "section": "3. API Update",
                "title": "Thao tác Update với PUT",
                "content": [
                    "PUT dùng để ghi đè/thay thế hoàn toàn tài nguyên đang tồn tại.",
                    "Client phải gửi lên toàn bộ các trường của schema.",
                    "Khác biệt với PATCH: PATCH chỉ cập nhật một vài trường được chỉ định (cập nhật từng phần)."
                ]
            },
            {
                "layout": "code",
                "section": "3. API Update",
                "title": "Triển khai PUT API trong FastAPI",
                "content": [
                    "@app.put(\"/students/{student_id}\")\ndef update(student_id: int, data: StudentUpdate):\n    # tìm ID -> ghi đè name, email\n    # không thấy -> raise 404 Not Found\n    return updated_student"
                ],
                "speaker_notes": "Hướng dẫn cách viết logic ghi đè thuộc tính in-memory."
            },
            # Lesson 4
            {
                "layout": "section-title",
                "section": "4. API Delete",
                "title": "Phần 4: API Delete - Xóa dữ liệu",
                "content": ["Phương thức HTTP DELETE", "Mã trạng thái 204 No Content", "Xóa vật lý vs Xóa mềm (Soft Delete)"]
            },
            {
                "layout": "bullets",
                "section": "4. API Delete",
                "title": "Thao tác Delete với DELETE",
                "content": [
                    "DELETE dùng để loại bỏ tài nguyên ra khỏi hệ thống.",
                    "Xóa thành công thường trả về mã 204 No Content (body trống) hoặc 200 OK.",
                    "Phân loại: Xóa vật lý (xóa vĩnh viễn) và Xóa mềm (chỉ đổi cờ trạng thái is_deleted = True)."
                ]
            },
            {
                "layout": "code",
                "section": "4. API Delete",
                "title": "Triển khai DELETE API trong FastAPI",
                "content": [
                    "@app.delete(\"/students/{student_id}\", status_code=204)\ndef delete(student_id: int):\n    # tìm ID -> pop khỏi list\n    # không thấy -> raise 404\n    return # 204 trả về body rỗng"
                ],
                "speaker_notes": "Giải thích mã 204 No Content và cách trả về body trống khi xóa thành công."
            },
            # Ending slides
            {
                "layout": "summary",
                "section": "TỔNG KẾT",
                "title": "Tổng kết bài học",
                "content": [
                    "Create: HTTP POST, trả về 201 Created.",
                    "Read: HTTP GET, an toàn/idempotent, trả lỗi 404 Not Found.",
                    "Update: HTTP PUT, ghi đè toàn bộ, phân biệt với PATCH cập nhật từng phần.",
                    "Delete: HTTP DELETE, xóa vật lý hoặc xóa mềm, trả về 204 No Content."
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

    print("Successfully generated all 18 specification JSON files for Session 05!")

if __name__ == "__main__":
    main()
