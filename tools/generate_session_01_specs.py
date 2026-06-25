# -*- coding: utf-8 -*-
"""Script to programmatically generate all 12 spec JSON files for Session 01.
"""
import os
import json

SPEC_DIR = r"d:\AI-Agent-trinhkhaclinh\Agent-xaydungtainguyenhoctap\output\Session 01 - Định hướng học tập, demo sản phẩm cuối môn\_spec"

def write_json(name, data):
    path = os.path.join(SPEC_DIR, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Generated {name}")

def main():
    # ------------------ READING 01: Orientation & Roadmap ------------------
    reading_01 = {
        "filename": "BÀI ĐỌC_ LỘ TRÌNH VÀ PHƯƠNG PHÁP HỌC FASTAPI_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: Định Hướng Học Tập & Lộ Trình Môn Học IT-215" },
            { "type": "p", "text": "Chào mừng các bạn đến với khóa học IT-215: Phát triển dịch vụ web với FastAPI. Đây là bước đi đầu tiên trên con đường trở thành một lập trình viên Backend chuyên nghiệp với ngôn ngữ Python. Để học tập hiệu quả, chúng ta cần một bản đồ lộ trình rõ ràng, hiểu rõ các công cụ cần thiết và làm quen với phương pháp học tập chủ động tại Rikkei Education." },
            { "type": "h2", "text": "1. Lộ trình học tập môn IT-215 FastAPI" },
            { "type": "p", "text": "Môn học IT-215 được thiết kế gồm 26 buổi lý thuyết kết hợp thực hành và dự án thực tế. Khóa học được chia làm các giai đoạn chính:" },
            { "type": "bullets", "items": [
                "Giai đoạn 1: Làm quen với FastAPI cơ bản, định tuyến Route, Parameters, Request và Response.",
                "Giai đoạn 2: Kết nối cơ sở dữ liệu MySQL sử dụng thư viện SQLAlchemy ORM và thiết kế cấu trúc dự án chuẩn.",
                "Giai đoạn 3: Phân quyền bảo mật (Authentication & Authorization) sử dụng mã hóa mật khẩu và token JWT.",
                "Giai đoạn 4: Thiết kế & Xây dựng RESTful API tổng hợp (Mini Project và Hackathon).",
                "Giai đoạn 5: Phát triển sản phẩm cuối môn (Final Project) và bảo vệ trước hội đồng."
            ]},
            { "type": "h2", "text": "2. Chuẩn bị Môi trường Học tập Cá nhân" },
            { "type": "p", "text": "Để tham gia thực hành đầy đủ, học viên bắt buộc phải thiết lập môi trường phát triển trên máy tính cá nhân bao gồm các công cụ sau:" },
            { "type": "numbers", "items": [
                "Python 3.10+: Ngôn ngữ lập trình chính được dùng để viết backend.",
                "VS Code: Trình soạn thảo mã nguồn gọn nhẹ, hỗ trợ nhiều plugin đắc lực cho Python.",
                "Git: Hệ thống quản lý mã nguồn giúp lưu trữ phiên bản và nộp bài tập qua GitHub.",
                "Postman: Công cụ đắc lực dùng để gọi thử và kiểm thử các API Endpoint."
            ]},
            { "type": "code", "lang": "bash", "text": "# Kiểm tra cài đặt thành công từ terminal\npython --version\ngit --version" },
            { "type": "h2", "text": "3. Phương pháp Lập trình Chủ động (Active Learning)" },
            { "type": "p", "text": "Tại Rikkei Education, chúng ta không học theo cách thụ động nghe giảng rồi chép code. Chúng ta áp dụng phương pháp lập trình chủ động dựa trên Backwards Design (Thiết kế ngược):" },
            { "type": "p", "text": "Học viên được tiếp cận mục tiêu sản phẩm đầu ra trước, sau đó đi ngược lại tìm hiểu những kiến thức, công cụ cần thiết để hoàn thành sản phẩm đó. Việc tự tìm lỗi, sửa lỗi và trace code là kỹ năng sống còn giúp học viên trưởng thành nhanh chóng." },
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Khóa học IT-215 kéo dài 26 buổi nhằm trang bị kỹ năng xây dựng Web API chuyên nghiệp bằng FastAPI.",
                "Học viên cần cài đặt đầy đủ Python, VS Code, Git và Postman ngay trong buổi học đầu tiên.",
                "Học tập chủ động bằng cách thực hành viết code liên tục và tự gỡ lỗi."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "FastAPI Official Site: https://fastapi.tiangolo.com/",
                "Git Documentation: https://git-scm.com/doc"
            ]}
        ]
    }
    write_json("reading_01.json", reading_01)

    # ------------------ READING 02: Final Project Demo ------------------
    reading_02 = {
        "filename": "BÀI ĐỌC_ PHÂN TÍCH SẢN PHẨM CUỐI MÔN_",
        "subdir": "Bài đọc",
        "blocks": [
            { "type": "h1", "text": "Bài Đọc Chuyên Sâu: Demo & Phân Tích Kiến Trúc Sản Phẩm Cuối Môn" },
            { "type": "p", "text": "Đích đến của môn học IT-215 là xây dựng một hệ thống Web API chất lượng cao cho một dự án thực tế (ví dụ: Hệ thống quản lý trung tâm đào tạo hoặc Hệ thống bán hàng). Để hình dung rõ sản phẩm này, chúng ta cần phân tích kiến trúc hệ thống Client-Server-Database và tìm hiểu các tính năng nghiệp vụ bắt buộc phải có." },
            { "type": "h2", "text": "1. Tổng quan Kiến trúc Client-API-Database" },
            { "type": "p", "text": "Một ứng dụng web hiện đại thường tuân theo kiến trúc 3 tầng tách biệt giúp nâng cao khả năng mở rộng:" },
            { "type": "bullets", "items": [
                "**Client (Giao diện):** Nơi người dùng tương tác trực tiếp (giao diện Web React/Vue hoặc ứng dụng di động Mobile App).",
                "**API Server (Backend):** Máy chủ viết bằng FastAPI tiếp nhận request, kiểm tra nghiệp vụ, tương tác với database và trả dữ liệu JSON.",
                "**Database (Cơ sở dữ liệu):** MySQL lưu trữ các bảng thông tin một cách bền vững."
            ]},
            { "type": "p", "text": "API đóng vai trò là chiếc cầu nối duy nhất truyền tải thông tin an toàn giữa giao diện người dùng và cơ sở dữ liệu." },
            { "type": "h2", "text": "2. Cấu trúc Thư mục Dự án FastAPI mẫu" },
            { "type": "p", "text": "Để dự án lớn không bị rối và dễ bảo trì, chúng ta tổ chức code theo cấu trúc phân lớp chức năng tiêu chuẩn:" },
            { "type": "code", "lang": "text", "text": "my_project/\n├── app/                         # Thư mục chính chứa mã nguồn\n│   ├── main.py                  # Điểm chạy khởi tạo ứng dụng\n│   ├── database.py              # Cấu hình kết nối MySQL\n│   ├── models.py                # Định nghĩa các bảng cơ sở dữ liệu (ORM)\n│   ├── schemas.py               # Định nghĩa schema validate dữ liệu (Pydantic)\n│   ├── services.py              # Xử lý logic nghiệp vụ chính\n│   └── routers/                 # Quản lý định tuyến chia nhỏ API\n│       ├── users.py             # Các API liên quan đến người dùng\n│       └── courses.py           # Các API liên quan đến môn học\n├── requirements.txt             # Danh sách thư viện cần cài đặt\n└── README.md                    # Hướng dẫn chạy dự án" },
            { "type": "h2", "text": "3. Các Tính năng Cốt lõi của Sản phẩm Cuối khóa" },
            { "type": "p", "text": "Dự án cuối khóa của học viên bắt buộc phải có tối thiểu các nhóm chức năng sau:" },
            { "type": "numbers", "items": [
                "Quản lý CRUD: Cho phép tạo mới, hiển thị chi tiết, cập nhật và xóa tài nguyên.",
                "Tìm kiếm & Phân trang: Lọc danh sách theo từ khóa, giới hạn số bản ghi trả về.",
                "Xác thực & Phân quyền: Đăng ký, đăng nhập nhận token JWT; phân chia quyền Admin và User.",
                "Tài liệu API Swagger UI: Mọi API phải được mô tả đầy đủ tham số và phản hồi lỗi chuẩn xác."
            ]},
            { "type": "h2", "text": "Tổng Kết" },
            { "type": "bullets", "items": [
                "Sản phẩm cuối môn là một Web API hoàn chỉnh viết bằng FastAPI kết nối MySQL.",
                "Mô hình kiến trúc Client-API-Database giúp phân tách giao diện và xử lý dữ liệu độc lập.",
                "Cấu trúc dự án phân lớp rõ ràng (models, schemas, services, routers) là yêu cầu kỹ thuật bắt buộc."
            ]},
            { "type": "h2", "text": "Tài Liệu Tham Khảo" },
            { "type": "bullets", "items": [
                "FastAPI Project Structure Best Practices: https://fastapi.tiangolo.com/tutorial/bigger-applications/"
            ]}
        ]
    }
    write_json("reading_02.json", reading_02)

    # ------------------ VIDEO SCRIPTS ------------------
    # Video 01
    video_01 = {
        "filename": "Lesson 01 - Định hướng lộ trình học tập FastAPI",
        "subdir": "Kịch bản quay video",
        "lesson_no": 1,
        "blocks": [
            { "type": "h2", "text": "## Chào mừng và Định hướng môn học" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Thầy rất vui được đồng hành cùng các em trong môn học IT-215 - Phát triển dịch vụ web với FastAPI." },
            { "type": "narration", "text": "Trong thời đại ứng dụng web và di động phát triển bùng nổ như hiện nay, việc xây dựng các API Backend nhanh, hiệu năng cao và an toàn là kỹ năng cực kỳ quan trọng. FastAPI chính là công cụ đắc lực nhất giúp chúng ta thực hiện điều đó một cách dễ dàng nhất." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Lộ trình 26 buổi học IT-215" },
            { "type": "narration", "text": "Hãy cùng nhìn lên lộ trình học tập trên màn hình. Môn học của chúng ta kéo dài 26 buổi. Chúng ta sẽ bắt đầu từ các khái niệm định tuyến cơ bản, đi qua phần tích hợp cơ sở dữ liệu SQLAlchemy, thực hiện phân quyền bảo mật bằng token JWT, làm việc nhóm qua các buổi Hackathon và cuối cùng là hoàn thành dự án cuối khóa để tốt nghiệp." },
            { "type": "marker", "text": "[mở trình duyệt và hiển thị slide phương pháp học tập ngược]" },
            { "type": "narration", "text": "Phương pháp học tập của chúng ta tuân thủ triết lý Thiết kế ngược. Chúng ta đặt ra mục tiêu sản phẩm thực tế trước, từ đó tìm kiếm kiến thức để giải quyết nó. Điều này đòi hỏi các em phải chủ động thực hành viết code liên tục." },
            { "type": "h2", "text": "## Chuẩn bị công cụ phát triển" },
            { "type": "narration", "text": "Trước khi kết thúc buổi học đầu tiên, các em hãy nhớ cài đặt đầy đủ Python phiên bản mới nhất, trình soạn thảo mã nguồn VS Code, hệ thống quản lý mã nguồn Git để nộp bài tập và công cụ Postman để kiểm thử API nhé." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Như vậy, thầy đã giới thiệu tổng quan lộ trình môn học và các công cụ cần thiết. Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em ở bài học giới thiệu sản phẩm tiếp theo!" }
        ]
    }
    write_json("video_01.json", video_01)

    # Video 02
    video_02 = {
        "filename": "Lesson 02 - Phân tích sản phẩm cuối môn và Kiến trúc hệ thống",
        "subdir": "Kịch bản quay video",
        "lesson_no": 2,
        "blocks": [
            { "type": "h2", "text": "## Giới thiệu sản phẩm cuối môn" },
            { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học này, thầy và các em sẽ cùng nhau phân tích chi tiết sản phẩm cuối khóa mà các em sẽ tự tay xây dựng." },
            { "type": "narration", "text": "Đích đến kỹ thuật của môn học là một hệ thống Web API hoàn chỉnh. Để hiểu rõ sản phẩm hoạt động thế nào, hãy cùng nhìn vào sơ đồ kiến trúc 3 tầng Client-API-Database trên màn hình." },
            { "type": "marker", "text": "[Chuyển tiếp slide]" },
            { "type": "h2", "text": "## Phân tích kiến trúc 3 tầng và API" },
            { "type": "narration", "text": "Trong kiến trúc này, phía giao diện người dùng gửi các HTTP Request chứa dữ liệu đến Backend FastAPI. Backend của chúng ta tiếp nhận, thực thi nghiệp vụ và tương tác với cơ sở dữ liệu MySQL thông qua SQLAlchemy ORM để truy xuất hoặc lưu trữ thông tin, sau đó trả dữ liệu JSON về cho Client." },
            { "type": "marker", "text": "[mở tài liệu Swagger UI của sản phẩm mẫu]" },
            { "type": "narration", "text": "Như các em thấy trên màn hình là tài liệu Swagger UI của sản phẩm mẫu. Chúng ta có các API đăng ký, đăng nhập bảo mật, các API quản lý lớp học, sinh viên với đầy đủ chức năng tạo mới, hiển thị, cập nhật và xóa. Đây chính là cấu trúc giao diện mà các em sẽ hoàn thiện." },
            { "type": "h2", "text": "## Cấu trúc thư mục dự án tiêu chuẩn" },
            { "type": "narration", "text": "Để dự án không bị rối, các em cần tuân thủ cấu trúc chia thư mục rõ ràng. Chúng ta chia nhỏ code thành models chứa cấu trúc bảng CSDL, schemas chứa lớp validate Pydantic, services xử lý nghiệp vụ và routers quản lý đường dẫn API." },
            { "type": "h2", "text": "## Tổng kết bài giảng" },
            { "type": "narration", "text": "Tóm lại, trong bài học này các em đã hiểu rõ mục tiêu sản phẩm cuối khóa cũng như cấu trúc dự án mẫu cần hướng tới. Hãy chuẩn bị tinh thần học tập thật tốt. Cảm ơn các em và chúc các em học tập hiệu quả!" }
        ]
    }
    write_json("video_02.json", video_02)


    # ------------------ EXERCISES (6 files) ------------------
    # Exercise 01
    exercise_01 = {
        "filename": "[Vận dụng cơ bản 1] Thiết lập Git và thực hiện Commit đầu tiên",
        "subdir": "Bài tập",
        "level": "Vận dụng cơ bản",
        "blocks": [
            { "type": "h1", "text": "Thiết lập Git quản lý mã nguồn dự án" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Học viên chuẩn bị bắt đầu dự án môn học IT-215. Để nộp bài tập và quản lý các phiên bản code, việc cài đặt và làm quen với Git là yêu cầu bắt buộc ngay từ buổi học đầu tiên." },
            { "type": "h2", "text": "2. Yêu cầu bài toán" },
            { "type": "p", "text": "Hãy khởi tạo một kho lưu trữ Git cục bộ trong thư mục dự án mẫu, cấu hình thông tin cá nhân và tạo commit đầu tiên chứa file README.md." },
            { "type": "h2", "text": "3. Mã nguồn hiện tại (Legacy Code)" },
            { "type": "code", "lang": "bash", "text": "# Thực hiện chạy các lệnh trong terminal\n# Bước 1: Khởi tạo git\ngit init\n\n# Bước 2: Cấu hình thông tin cá nhân\ngit config --global user.name \"Tên của bạn\"\ngit config --global user.email \"email@gmail.com\"" },
            { "type": "h2", "text": "4. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Tạo file README.md mô tả dự án học tập cá nhân.",
                "Thêm file vào khu vực theo dõi (staging area) bằng lệnh `git add`.",
                "Tạo commit đầu tiên bằng `git commit -m 'Initial commit'`.",
                "Chụp màn hình log lịch sử commit (`git log`)."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session01", "ex": "Ex01",
            "example": "HNKS25CNTT1_FastAPI_Session01_Ex01"
        }
    }
    write_json("exercise_01.json", exercise_01)

    # Exercise 02
    exercise_02 = {
        "filename": "[Vận dụng cơ bản 2] Đọc và vẽ lại sơ đồ kiến trúc Client-API-Database",
        "subdir": "Bài tập",
        "level": "Vận dụng cơ bản",
        "blocks": [
            { "type": "h1", "text": "Phân tích sơ đồ luồng dữ liệu 3 lớp" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Khi phát triển phần mềm, việc hiểu rõ đường đi của dữ liệu từ giao diện người dùng đến database giúp chúng ta dễ dàng thiết kế cấu trúc API phù hợp và xử lý sự cố nhanh chóng." },
            { "type": "h2", "text": "2. Yêu cầu bài toán" },
            { "type": "p", "text": "Hãy tự vẽ lại sơ đồ kiến trúc Client-API-Database minh họa rõ các bước từ lúc người dùng nhấn nút đăng ký học, cho đến khi database MySQL lưu trữ thông tin sinh viên thành công." },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Vẽ sơ đồ luồng bằng công cụ online (draw.io / Lucidchart) hoặc vẽ tay.",
                "Giải thích rõ vai trò của FastAPI và Database MySQL trong sơ đồ.",
                "Mô tả định dạng dữ liệu (JSON) truyền tải giữa Client và API."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session01", "ex": "Ex02",
            "example": "HNKS25CNTT1_FastAPI_Session01_Ex02"
        }
    }
    write_json("exercise_02.json", exercise_02)

    # Exercise 03
    exercise_03 = {
        "filename": "[Vận dụng chuyên sâu] Lên danh sách API Endpoints cho Đăng nhập và Đăng ký",
        "subdir": "Bài tập",
        "level": "Vận dụng chuyên sâu",
        "blocks": [
            { "type": "h1", "text": "Thiết kế danh sách API Endpoint ban đầu cho dự án" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Dự án cuối khóa yêu cầu tính năng đăng nhập và đăng ký tài khoản người dùng để bảo mật hệ thống. Trước khi viết code, đội ngũ phân tích cần xác định rõ các Endpoint cần xây dựng." },
            { "type": "h2", "text": "2. Quy tắc nghiệp vụ" },
            { "type": "bullets", "items": [
                "Đường dẫn API phải tuân theo chuẩn RESTful.",
                "Xác định đúng HTTP Method (GET, POST, PUT, DELETE) cho từng chức năng.",
                "Mô tả định dạng Request Body JSON tối thiểu cần thiết."
            ]},
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Thiết kế Endpoint tạo tài khoản mới (đăng ký).",
                "Thiết kế Endpoint xác thực tài khoản nhận token (đăng nhập).",
                "Mô tả chi tiết các trường JSON gửi lên của mỗi API."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session01", "ex": "Ex03",
            "example": "HNKS25CNTT1_FastAPI_Session01_Ex03"
        }
    }
    write_json("exercise_03.json", exercise_03)

    # Exercise 04
    exercise_04 = {
        "filename": "[Phân tích] So sánh Postman và Swagger UI trong kiểm thử API",
        "subdir": "Bài tập",
        "level": "Phân tích",
        "blocks": [
            { "type": "h1", "text": "So sánh các công cụ kiểm thử API phổ biến" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "FastAPI tự động sinh tài liệu Swagger UI tại đường dẫn `/docs`. Tuy nhiên, trong phát triển dự án thực tế, các lập trình viên vẫn sử dụng thêm công cụ Postman để kiểm thử API nâng cao." },
            { "type": "h2", "text": "2. Yêu cầu đầu ra" },
            { "type": "h3", "text": "(1) Lập bảng so sánh tính năng" },
            { "type": "table", "headers": ["Tiêu chí so sánh", "Swagger UI tự động", "Postman Desktop"], "rows": [
                ["Khởi tạo dữ liệu kiểm thử", "", ""],
                ["Hỗ trợ cấu hình biến môi trường", "", ""],
                ["Khả năng lưu trữ lịch sử request", "", ""],
                ["Tự động cập nhật khi sửa code", "", ""]
            ]},
            { "type": "h3", "text": "(2) Đánh giá tình huống" },
            { "type": "bullets", "items": [
                "Đưa ra nhận định: khi nào nên ưu tiên dùng Swagger UI, khi nào nên dùng Postman.",
                "Giải thích vai trò của việc tạo Collection trong Postman."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session01", "ex": "Ex04",
            "example": "HNKS25CNTT1_FastAPI_Session01_Ex04"
        }
    }
    write_json("exercise_04.json", exercise_04)

    # Exercise 05
    exercise_05 = {
        "filename": "[Sáng tạo] Đề xuất ý tưởng tính năng mở rộng cho dự án cuối khóa",
        "subdir": "Bài tập",
        "level": "Sáng tạo",
        "blocks": [
            { "type": "h1", "text": "Đề xuất giá trị cộng thêm cho sản phẩm tốt nghiệp" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Hội đồng đánh giá dự án cuối khóa của Rikkei Education đánh giá rất cao các dự án có tính ứng dụng thực tế và có sự sáng tạo thêm các tính năng độc đáo ngoài yêu cầu tối thiểu." },
            { "type": "h2", "text": "2. Thử thách sáng tạo" },
            { "type": "p", "text": "Hãy lựa chọn một chủ đề dự án (ví dụ: Quản lý khóa học trực tuyến) và đề xuất ít nhất 2 tính năng nâng cao (ví dụ: Xuất báo cáo điểm sang file PDF, tự động gửi email thông báo kết quả cho học viên)." },
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Mô tả nghiệp vụ chi tiết của 2 tính năng đề xuất.",
                "Vẽ hoặc mô tả luồng xử lý API Backend của 2 tính năng đó.",
                "Giải thích lợi ích thực tế mang lại cho người dùng cuối."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session01", "ex": "Ex05",
            "example": "HNKS25CNTT1_FastAPI_Session01_Ex05"
        }
    }
    write_json("exercise_05.json", exercise_05)

    # Exercise 06
    exercise_06 = {
        "filename": "[BTTH] Viết tài liệu đặc tả yêu cầu SRS tối giản cho dự án học tập",
        "subdir": "Bài tập",
        "level": "Tổng hợp",
        "blocks": [
            { "type": "h1", "text": "Tài liệu đặc tả yêu cầu phần mềm mức cơ bản" },
            { "type": "h2", "text": "1. Bối cảnh nghiệp vụ" },
            { "type": "p", "text": "Học viên cần xây dựng một tài liệu đặc tả yêu cầu (SRS) ngắn gọn cho dự án cá nhân để định hướng công việc viết code trong suốt 26 buổi học tiếp theo." },
            { "type": "h2", "text": "2. Yêu cầu kỹ thuật" },
            { "type": "bullets", "items": [
                "Xác định rõ chủ đề dự án (Quản lý thư viện / Cửa hàng bán sách / Quản lý điểm sinh viên).",
                "Liệt kê danh sách các bảng dữ liệu dự kiến cần lưu trữ (Database Tables).",
                "Mô tả các Endpoint API CRUD cơ bản phục vụ cho một nghiệp vụ cụ thể."
            ]},
            { "type": "h2", "text": "3. Yêu cầu đầu ra" },
            { "type": "bullets", "items": [
                "Trình bày tài liệu đặc tả dưới định dạng Markdown.",
                "Thiết kế sơ đồ quan hệ thực thể (ERD) mức logic tối giản giữa các bảng dữ liệu.",
                "Cam kết tiến độ và đặt ra các mốc thời gian hoàn thiện dự kiến."
            ]}
        ],
        "submission": {
            "lop": "[Tên Lớp]", "mon": "FastAPI", "session": "Session01", "ex": "Ex06",
            "example": "HNKS25CNTT1_FastAPI_Session01_Ex06"
        }
    }
    write_json("exercise_06.json", exercise_06)


    # ------------------ QUIZZES ------------------
    # Quiz Đầu giờ
    quiz_daugio = {
        "sheet_name": "Quiz_DauGio_FastAPI_01",
        "questions": [
            # OOP & Python Basic
            {
                "q": "Để khai báo một phương thức khởi tạo trong một Class của Python, ta dùng định nghĩa hàm nào?",
                "answers": ["def init(self):", "def __init__(self):", "def create(self):", "def constructor(self):"],
                "explanations": ["Không đúng tên hàm khởi tạo.", "Chính xác, __init__ (dunder init) là hàm khởi dựng của class trong Python.", "Không đúng.", "Không đúng."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Kiểu dữ liệu nào trong Python biểu diễn một danh sách có thứ tự và có thể thay đổi (mutable)?",
                "answers": ["Tuple", "List", "Set", "Dictionary"],
                "explanations": ["Tuple là danh sách không thể thay đổi sau khi tạo (immutable).", "Chính xác, List được khai báo bằng ngoặc vuông và có thể thêm/bớt phần tử.", "Set là tập hợp không trùng lặp và không có thứ tự.", "Dictionary lưu trữ dữ liệu dạng cặp key-value."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Trong Python, làm thế nào để chuyển đổi một chuỗi ký tự '15' thành số nguyên?",
                "answers": ["str(15)", "int('15')", "convert('15', int)", "float('15')"],
                "explanations": ["Đây là chuyển số thành chuỗi.", "Chính xác, int() được dùng để ép kiểu sang số nguyên.", "Hàm convert không tồn tại mặc định trong Python.", "Đây là chuyển sang số thực."],
                "correct": 2, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Phương thức nào dùng để thêm một phần tử vào cuối danh sách List trong Python?",
                "answers": ["add()", "push()", "append()", "insert()"],
                "explanations": ["Không dùng cho list.", "Là phương thức của mảng trong JavaScript.", "Chính xác, append() thêm phần tử vào cuối danh sách.", "insert() chèn phần tử vào một chỉ số cụ thể."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Từ khóa nào trong Python được dùng để kế thừa một Class cha?",
                "answers": ["extends", "inherits", "Khai báo tên Class cha trong ngoặc đơn sau tên Class con", "implements"],
                "explanations": ["Là từ khóa của Java/PHP.", "Không phải từ khóa của Python.", "Chính xác, ví dụ: class Con(Cha):", "Là từ khóa của Java/TypeScript."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            {
                "q": "Cú pháp để lấy ra toàn bộ các keys của một Dictionary tên là 'student' là gì?",
                "answers": ["student.all()", "student.get_keys()", "student.keys()", "student.items()"],
                "explanations": ["Không đúng.", "Không đúng.", "Chính xác, student.keys() trả về dict_keys chứa toàn bộ các khóa.", "student.items() trả về các cặp key-value."],
                "correct": 3, "difficulty": 4, "category": "BÀI CŨ"
            },
            # Preview concepts
            {
                "q": "FastAPI là framework chuyên dụng để xây dựng sản phẩm gì là chính?",
                "answers": ["Trang web giao diện tĩnh", "Ứng dụng di động cục bộ", "Dịch vụ Web API (RESTful API)", "Hệ điều hành máy tính"],
                "explanations": ["FastAPI chủ yếu trả JSON, không tối ưu cho giao diện tĩnh truyền thống.", "Ứng dụng di động dùng Flutter/Kotlin.", "Chính xác, FastAPI sinh ra để xây dựng Web API nhanh và hiệu quả.", "Không đúng."],
                "correct": 3, "difficulty": 8, "category": "BÀI MỚI"
            },
            {
                "q": "Công cụ nào được dùng phổ biến để kiểm thử gửi request và đọc response từ API?",
                "answers": ["Git", "Postman", "VS Code Extension Store", "MySQL Workbench"],
                "explanations": ["Git để quản lý mã nguồn.", "Chính xác, Postman là client HTTP chuyên dụng cho kiểm thử API.", "Dùng để cài plugin.", "Dùng để quản lý CSDL MySQL."],
                "correct": 2, "difficulty": 8, "category": "BÀI MỚI"
            }
        ]
    }
    write_json("quiz_daugio.json", quiz_daugio)

    # Quiz Cuối giờ
    quiz_cuoigio = {
        "sheet_name": "Quiz_CuoiGio_FastAPI_01",
        "questions": [
            {
                "q": "Khóa học IT-215 FastAPI sử dụng phương pháp giảng dạy nào làm cốt lõi?",
                "answers": [
                    "Thiết kế ngược (Backwards Design) và Lập trình chủ động",
                    "Nghe giảng lý thuyết thuần túy không thực hành",
                    "Lập trình hướng đối tượng nâng cao",
                    "Chỉ viết code theo mẫu có sẵn"
                ],
                "explanations": [
                    "Chính xác, học từ sản phẩm đầu ra đi ngược lại lý thuyết giúp học chủ động.",
                    "Không đúng.",
                    "Đó là mô hình lập trình.",
                    "Học viên phải tự thiết kế và sửa lỗi."
                ],
                "correct": 1, "difficulty": 6, "category": "DIENTICH"
            },
            {
                "q": "Mô hình kiến trúc nào phân tách hoàn toàn Frontend và Backend thông qua cổng API dữ liệu JSON?",
                "answers": [
                    "Monolithic Architecture",
                    "Decoupled Architecture (Tách biệt)",
                    "Server-Side Rendering (SSR)",
                    "Kiến trúc hướng sự kiện"
                ],
                "explanations": [
                    "Monolithic gộp chung giao diện và backend.",
                    "Chính xác, giúp API backend có thể dùng chung cho cả Web và App mobile.",
                    "SSR dựng HTML tại server.",
                    "Không đúng."
                ],
                "correct": 2, "difficulty": 6, "category": "KIEN_TRUC"
            },
            {
                "q": "Công cụ Git được sử dụng trong môn học IT-215 với mục đích gì?",
                "answers": [
                    "Chạy server web FastAPI",
                    "Lưu trữ cơ sở dữ liệu MySQL",
                    "Quản lý phiên bản mã nguồn dự án và nộp bài tập cá nhân",
                    "Thiết kế giao diện người dùng"
                ],
                "explanations": [
                    "Uvicorn chạy server web.",
                    "MySQL lưu database.",
                    "Chính xác, Git quản lý mã nguồn và hỗ trợ đẩy bài lên GitHub.",
                    "Không đúng."
                ],
                "correct": 3, "difficulty": 5, "category": "CONG_CU"
            },
            {
                "q": "Trong sơ đồ kiến trúc Client-API-Database, FastAPI đóng vai trò ở tầng nào?",
                "answers": [
                    "Tầng Client (máy khách)",
                    "Tầng API Server (máy chủ trung gian)",
                    "Tầng Database (cơ sở dữ liệu)",
                    "Tầng Network (đường truyền vật lý)"
                ],
                "explanations": [
                    "Client là trình duyệt/điện thoại.",
                    "Chính xác, FastAPI xử lý request và trả dữ liệu JSON.",
                    "Database là MySQL.",
                    "Không đúng."
                ],
                "correct": 2, "difficulty": 6, "category": "KIEN_TRUC"
            },
            {
                "q": "Mục tiêu đầu ra lớn nhất của khóa học IT-215 đối với mỗi học viên là gì?",
                "answers": [
                    "Cài đặt thành công Python",
                    "Xây dựng hoàn chỉnh một ứng dụng Web API thực tế (Final Project)",
                    "Vẽ thành công sơ đồ Client-Server",
                    "Đạt điểm tối đa các bài quiz đầu giờ"
                ],
                "explanations": [
                    "Đây chỉ là bước chuẩn bị ban đầu.",
                    "Chính xác, sản phẩm cuối môn hoàn chỉnh chứng minh năng lực lập trình backend.",
                    "Chỉ là bài tập cơ bản buổi đầu.",
                    "Quiz chỉ dùng để ôn luyện kiến thức."
                ],
                "correct": 2, "difficulty": 5, "category": "DINH_HUONG"
            }
        ]
    }
    write_json("quiz_cuoigio.json", quiz_cuoigio)


    # ------------------ MINDMAP ------------------
    mindmap = {
        "filename": "Session 01 - Định hướng học tập và demo sản phẩm cuối môn",
        "subdir": "Mindmap",
        "root": "Định hướng & Demo sản phẩm cuối môn",
        "children": [
            {
                "title": "1. Lộ trình môn học IT-215",
                "children": [
                    { "title": "26 buổi kết hợp lý thuyết và thực hành dự án" },
                    { "title": "Mục tiêu đầu ra: Thiết kế & Xây dựng RESTful API hoàn chỉnh" }
                ]
            },
            {
                "title": "2. Chuẩn bị môi trường phát triển",
                "children": [
                    { "title": "Ngôn ngữ: Python 3.10+" },
                    { "title": "IDE: VS Code" },
                    { "title": "Quản lý mã nguồn: Git" },
                    { "title": "Kiểm thử API: Postman" }
                ]
            },
            {
                "title": "3. Kiến trúc hệ thống 3 tầng",
                "children": [
                    { "title": "Client: Trình duyệt/Mobile App gửi Request" },
                    { "title": "Server: FastAPI xử lý logic, trả JSON" },
                    { "title": "Database: MySQL lưu trữ dữ liệu bền vững" }
                ]
            },
            {
                "title": "4. Phương pháp học tập chủ động",
                "children": [
                    { "title": "Thiết kế ngược (Backwards Design): Học đi đôi với làm sản phẩm" },
                    { "title": "Kỹ năng sửa lỗi, gỡ lỗi (Debugging) là ưu tiên số một" }
                ]
            }
        ]
    }
    write_json("mindmap.json", mindmap)


    # ------------------ SLIDE OUTLINE ------------------
    slide_outline = {
        "filename": "Session 01 - Định hướng học tập và demo sản phẩm cuối môn",
        "subdir": "Bài giảng",
        "title": "Định hướng học tập & Demo sản phẩm cuối môn",
        "module": "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI",
        "version": "1.0",
        "slides": [
            {
                "layout": "title",
                "title": "Định hướng học tập & Demo sản phẩm",
                "content": ["Session 01", "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI", "Phiên bản: 1.0"]
            },
            {
                "layout": "agenda",
                "section": "NỘI DUNG",
                "title": "Nội dung bài học",
                "content": [
                    "1. Định hướng học tập & Lộ trình môn học IT-215",
                    "2. Chuẩn bị công cụ phát triển phần mềm",
                    "3. Sơ đồ kiến trúc 3 tầng Client-API-Database",
                    "4. Demo sản phẩm cuối khóa (Final Project) mẫu"
                ]
            },
            # Lesson 1
            {
                "layout": "section-title",
                "section": "1. Định hướng & Lộ trình",
                "title": "Phần 1: Định hướng học tập & Lộ trình IT-215",
                "content": ["Tổng quan chương trình học", "Chuẩn đầu ra môn học", "Phương pháp học tập chủ động"]
            },
            {
                "layout": "bullets",
                "section": "1. Định hướng & Lộ trình",
                "title": "Lộ trình khóa học FastAPI",
                "content": [
                    "Khóa học gồm 26 buổi tập trung thực hành phát triển Web API.",
                    "Lý thuyết tinh gọn (ASGI, Pydantic, SQLAlchemy ORM, JWT Token).",
                    "Thực hành lập trình, thiết kế cơ sở dữ liệu MySQL và viết code API."
                ]
            },
            # Lesson 2
            {
                "layout": "section-title",
                "section": "2. Sơ đồ kiến trúc",
                "title": "Phần 2: Kiến trúc hệ thống & Demo sản phẩm",
                "content": ["Kiến trúc 3 lớp phân tách", "Cấu trúc thư mục dự án chuẩn", "Demo sản phẩm thực tế"]
            },
            {
                "layout": "bullets",
                "section": "2. Sơ đồ kiến trúc",
                "title": "Kiến trúc Client - API Server - Database",
                "content": [
                    "Client (Frontend): gửi yêu cầu HTTP và nhận dữ liệu JSON.",
                    "API Server (FastAPI): trung tâm tiếp nhận, kiểm tra dữ liệu và xử lý logic.",
                    "Database (MySQL): lưu trữ và bảo toàn thông tin hệ thống."
                ],
                "diagram_hint": "Sơ đồ Client ↔ API Server ↔ Database liên kết bằng mũi tên hai chiều"
            },
            {
                "layout": "code",
                "section": "2. Sơ đồ kiến trúc",
                "title": "Cấu trúc dự án FastAPI tiêu chuẩn",
                "content": [
                    "my_project/\n├── app/\n│   ├── main.py (Khởi chạy)\n│   ├── models.py (ORM Models)\n│   ├── schemas.py (Pydantic Schemas)\n│   └── routers/ (Định tuyến API)\n└── requirements.txt (Thư viện)"
                ],
                "speaker_notes": "Giải thích vai trò của việc chia nhỏ dự án lớn thành các file nhỏ dễ kiểm soát."
            },
            # Ending slides
            {
                "layout": "summary",
                "section": "TỔNG KẾT",
                "title": "Tổng kết bài học",
                "content": [
                    "Mục tiêu môn học: Tự tay hoàn thành ứng dụng Web API tốt nghiệp.",
                    "Chuẩn bị đầy đủ: Python, VS Code, Git và Postman.",
                    "Phương pháp: Học chủ động, thiết kế ngược từ sản phẩm thực tế.",
                    "Cấu trúc dự án tiêu chuẩn là yêu cầu bắt buộc khi viết code."
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

    print("Successfully generated all 12 specification JSON files for Session 01!")

if __name__ == "__main__":
    main()
