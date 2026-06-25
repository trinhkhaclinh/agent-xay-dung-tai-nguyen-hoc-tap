---
type: "bai-doc"
title: "Tài liệu API với OpenAPI và Swagger UI"
session: 2
lesson: 5
tags:
  - "type/bai-doc"
  - "session/02"
concepts:
  - "[[Chuẩn OpenAPI]]"
  - "[[Zero Configuration]]"
  - "[[Swagger UI (-docs)|Swagger UI (/docs)]]"
  - "[[ReDoc (-redoc)|ReDoc (/redoc)]]"
  - "[[Try it out - Execute|Try it out / Execute]]"
  - "[[Tags metadata phân nhóm API]]"
deliverable_filename: "BÀI ĐỌC_ TÀI LIỆU API VỚI OPENAPI VÀ SWAGGER UI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Tài Liệu API Tự Động Với OpenAPI Và Swagger UI

Một API dù viết tốt đến đâu cũng vô dụng nếu người khác không biết cách dùng. Trong thực tế, đội Frontend, đối tác tích hợp, và cả chính chúng ta sau này đều cần một tài liệu mô tả rõ: API có những endpoint nào, mỗi endpoint nhận tham số gì, trả về dữ liệu ra sao. Viết và bảo trì tài liệu này bằng tay là việc tốn công và dễ lỗi thời. Đây là nơi FastAPI tỏa sáng: nó tự động sinh tài liệu API hoàn chỉnh, có thể kiểm thử tương tác, mà chúng ta gần như không phải làm gì thêm.

Bài đọc này giải thích chuẩn OpenAPI nền tảng, cơ chế Zero Configuration của FastAPI, cách sử dụng Swagger UI tại /docs để đọc và kiểm thử API trực tiếp, và sự khác biệt với ReDoc. Chúng ta sẽ minh họa bằng một ứng dụng quản lý khóa học cho trung tâm đào tạo.

## 1. Vấn Đề: Vì Sao Tài Liệu API Quan Trọng

Hãy hình dung đội Backend của chúng ta vừa xây xong API quản lý khóa học, còn đội Frontend ở phòng bên cần gọi API đó để dựng giao diện. Nếu không có tài liệu, đội Frontend phải liên tục hỏi: 'Endpoint lấy khóa học tên gì?', 'Trả về những trường nào?', 'Tham số bắt buộc là gì?'. Giao tiếp kiểu này chậm chạp và dễ hiểu nhầm.

Tài liệu API tốt giải quyết vấn đề này: nó là hợp đồng chung giữa các đội, là điểm tham chiếu duy nhất để biết API hoạt động thế nào. Vấn đề là, với cách làm truyền thống, tài liệu viết tay thường lệch khỏi code thật mỗi khi code thay đổi mà tài liệu quên cập nhật. FastAPI giải quyết tận gốc bằng cách sinh tài liệu trực tiếp từ chính code — tài liệu và code luôn đồng bộ.

## 2. Chuẩn OpenAPI: Ngôn Ngữ Mô Tả API

OpenAPI là một tiêu chuẩn quốc tế (trước đây gọi là Swagger Specification) để mô tả các REST API một cách có cấu trúc, máy đọc được. Một tài liệu OpenAPI mô tả đầy đủ: các endpoint, phương thức HTTP, tham số đầu vào, cấu trúc dữ liệu trả về, mã trạng thái có thể có... Vì là chuẩn chung, mọi công cụ trong ngành đều hiểu được nó.

Điểm quan trọng: FastAPI tuân thủ hoàn toàn chuẩn OpenAPI. Mỗi ứng dụng FastAPI tự động tạo ra một tài liệu mô tả OpenAPI dưới dạng JSON (truy cập được tại đường dẫn /openapi.json). Chính tài liệu chuẩn hóa này là nguồn để sinh ra các giao diện đọc tài liệu đẹp mắt như Swagger UI và ReDoc mà chúng ta sẽ tìm hiểu ngay sau đây.

## 3. Zero Configuration: FastAPI Tự Sinh Tài Liệu Như Thế Nào

Zero Configuration (không cần cấu hình) là một trong những điểm hấp dẫn nhất của FastAPI. Chúng ta không phải viết thêm bất kỳ file mô tả tài liệu nào. FastAPI tự đọc cấu trúc các hàm xử lý, các decorator, và đặc biệt là các type hints (gợi ý kiểu dữ liệu) của Python để suy ra toàn bộ thông tin cần cho tài liệu.

Cụ thể, khi chúng ta khai báo một endpoint như ở các bài trước, FastAPI tự động biết: đường dẫn là gì (từ decorator), phương thức HTTP nào (@app.get hay @app.post), tham số tên gì và kiểu gì (từ type hints của hàm). Nhờ nền tảng Pydantic, mọi kiểu dữ liệu đều được phân tích chính xác. Đây chính là 'phần thưởng' cho việc viết type hints sạch sẽ: vừa được kiểm tra dữ liệu, vừa được tài liệu miễn phí.

> Liên hệ bài trước: docstring tiếng Việt chúng ta viết trong hàm get_system_status của file gateway.py cũng được FastAPI đọc và đưa vào phần mô tả của tài liệu. Một dòng docstring nhỏ hóa ra rất hữu ích.

## 4. Swagger UI Tại /docs: Tài Liệu Sống Có Thể Kiểm Thử

Swagger UI là một giao diện web tương tác hiển thị tài liệu API. Với FastAPI, nó có sẵn tại địa chỉ http://localhost:8000/docs ngay khi ứng dụng chạy — không cần cài hay cấu hình gì thêm. Đây không chỉ là tài liệu để đọc, mà còn là một môi trường kiểm thử tương tác đầy đủ.

Khi mở /docs, chúng ta thấy danh sách mọi endpoint của ứng dụng, mỗi cái có màu sắc theo phương thức HTTP (GET màu xanh dương, POST màu xanh lá...), kèm mô tả và cấu trúc dữ liệu. Nhưng điểm mạnh nhất là tính năng kiểm thử trực tiếp ngay trên trình duyệt, sẽ trình bày ở mục tiếp theo.

## 5. Dùng 'Try It Out' Để Kiểm Thử Không Cần Postman

Tính năng nổi bật nhất của Swagger UI là cho phép gọi thử API ngay trên trang tài liệu, không cần mở Postman hay viết code Client. Quy trình thực hiện cho một endpoint quản lý khóa học như sau:

1. Mở trình duyệt tới http://localhost:8000/docs sau khi server đang chạy.
2. Bấm vào endpoint muốn thử, ví dụ GET /courses, để mở rộng chi tiết.
3. Bấm nút 'Try it out' để chuyển sang chế độ kiểm thử; nếu endpoint có tham số, các ô nhập sẽ hiện ra để điền.
4. Bấm nút 'Execute' để gửi yêu cầu thật đến server.
5. Xem kết quả ngay bên dưới: Swagger UI hiển thị mã trạng thái (200 OK), phần body JSON trả về, và cả lệnh curl tương đương.

Lợi ích sư phạm và thực tiễn của tính năng này rất lớn: chúng ta hoàn thành trọn vẹn một vòng đời Request-Response mà không cần rời trình duyệt. Đặc biệt, các endpoint POST/PUT/DELETE — vốn không gửi được trực tiếp bằng cách gõ URL vào trình duyệt — giờ có thể thử dễ dàng qua /docs. Đây là công cụ kiểm thử nhanh hàng đầu trong quá trình phát triển.

## 6. ReDoc Tại /redoc: Giao Diện Đọc Tối Giản

Bên cạnh Swagger UI, FastAPI còn tự động cung cấp một giao diện tài liệu thứ hai là ReDoc, mặc định tại http://localhost:8000/redoc. ReDoc cũng đọc từ cùng tài liệu OpenAPI, nhưng trình bày theo phong cách khác.

| Tiêu chí | Swagger UI (/docs) | ReDoc (/redoc) |
| --- | --- | --- |
| Mục đích chính | Vừa đọc vừa kiểm thử tương tác | Tối ưu cho đọc và tra cứu |
| Kiểm thử trực tiếp | Có (Try it out / Execute) | Không (chỉ để đọc) |
| Bố cục | Một cột, mở rộng từng endpoint | Ba cột tối giản, gọn gàng |
| Phù hợp khi | Lập trình viên đang phát triển, thử API | Đọc tài liệu tổng quan, chia sẻ cho người dùng API |

Chọn dùng cái nào tùy mục đích: khi đang phát triển và muốn thử nhanh, chúng ta dùng /docs (Swagger UI); khi cần một trang tài liệu sạch sẽ để đọc tổng quan hoặc gửi cho đối tác tham khảo, /redoc (ReDoc) thường dễ đọc hơn. Điều tuyệt vời là chúng ta có cả hai miễn phí, đồng bộ tự động với code.

## 7. Vận Dụng: Khai Báo Metadata Cho API Quản Lý Khóa Học

Tài liệu tự sinh đã tốt, nhưng chúng ta có thể làm nó chuyên nghiệp hơn bằng cách khai báo một ít metadata khi tạo ứng dụng: tiêu đề, mô tả, phiên bản. Những thông tin này sẽ hiển thị ở đầu trang /docs, giúp tài liệu trông như một sản phẩm hoàn chỉnh. Ngoài ra, chúng ta dùng tham số tags để phân nhóm các endpoint cho tài liệu gọn gàng:

```python
# main.py — API quản lý khóa học cho trung tâm đào tạo
from fastapi import FastAPI

# Khai báo metadata: tiêu đề, mô tả và phiên bản hiển thị trên Swagger UI
app = FastAPI(
    title="Course Management API",
    description="API quản lý khóa học cho trung tâm đào tạo",
    version="1.0.0"
)

# tags=["courses"] gom endpoint này vào nhóm "courses" trong tài liệu
@app.get("/courses", tags=["courses"])
def list_courses():
    return [{"id": 1, "name": "Web API with FastAPI"}]
```

Phân tích đoạn code. Ba tham số title, description, version truyền vào FastAPI() sẽ xuất hiện ngay ở phần đầu trang /docs — biến tài liệu thành một trang giới thiệu API rõ ràng. Tham số tags=["courses"] trong decorator gắn nhãn nhóm cho endpoint: khi một ứng dụng có nhiều endpoint, việc gom nhóm (ví dụ nhóm 'courses', nhóm 'students', nhóm 'grades') giúp Swagger UI hiển thị tài liệu theo từng mục, dễ tìm hơn nhiều so với một danh sách dài lộn xộn.

Chạy ứng dụng bằng 'uvicorn main:app --reload', rồi mở http://localhost:8000/docs. Chúng ta sẽ thấy tiêu đề 'Course Management API' phiên bản 1.0.0 ở trên cùng, và endpoint /courses được xếp gọn dưới nhóm 'courses'. Bấm 'Try it out' rồi 'Execute' để gọi thử và thấy danh sách khóa học trả về. Đây chính là sản phẩm đầu ra của bài học: Swagger hiển thị và test được API.

## 8. Mở Rộng: Tài Liệu Là Một Phần Của Chất Lượng API

Một bài học tư duy quan trọng: trong các framework cũ, tài liệu thường là việc làm thêm, dễ bị bỏ bê. FastAPI đảo ngược điều đó — tài liệu trở thành sản phẩm phụ tự nhiên của việc viết code đúng cách (khai báo type hints, docstring, tags). Vì vậy, khi viết API với FastAPI, chúng ta nên xem việc khai báo kiểu dữ liệu và mô tả rõ ràng không chỉ để máy hiểu, mà còn để sinh ra tài liệu chất lượng cho con người.

Thói quen tốt cần xây dựng: luôn khai báo title/description/version có ý nghĩa, gắn tags hợp lý cho từng nhóm tài nguyên, và viết docstring ngắn gọn cho mỗi endpoint. Những đầu tư nhỏ này khiến API của chúng ta dễ dùng, dễ bàn giao, và chuyên nghiệp hơn hẳn.

## Tổng Kết

Bài đọc đã khép lại session bằng một trong những tính năng mạnh nhất của FastAPI — tài liệu API tự động. Các điểm cốt lõi cần ghi nhớ:

- OpenAPI là tiêu chuẩn quốc tế mô tả REST API; FastAPI tuân thủ hoàn toàn và tự sinh tài liệu OpenAPI (tại /openapi.json) làm nguồn cho các giao diện đọc.
- Zero Configuration: FastAPI tự đọc cấu trúc hàm, type hints và docstring để sinh tài liệu mà không cần cấu hình thêm — tài liệu luôn đồng bộ với code.
- Swagger UI tại http://localhost:8000/docs vừa là tài liệu vừa là môi trường kiểm thử tương tác: dùng 'Try it out' và 'Execute' để gọi thử API ngay trên trình duyệt, kể cả POST/PUT/DELETE.
- ReDoc tại http://localhost:8000/redoc là giao diện ba cột tối giản, tối ưu cho việc đọc và tra cứu (không kiểm thử trực tiếp).
- Có thể nâng chất lượng tài liệu bằng metadata (title, description, version) và phân nhóm endpoint bằng tags.

## Tài Liệu Tham Khảo

- FastAPI Official Documentation — Interactive API docs: https://fastapi.tiangolo.com/#interactive-api-docs
- FastAPI Official Documentation — Metadata and Docs URLs: https://fastapi.tiangolo.com/tutorial/metadata/
- FastAPI Official Documentation — Path Operation Configuration (tags): https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
- OpenAPI Initiative — The OpenAPI Specification: https://www.openapis.org/
- Swagger UI — Official documentation: https://swagger.io/tools/swagger-ui/
- ReDoc — OpenAPI/Swagger-generated API Reference Documentation: https://github.com/Redocly/redoc

## Khái niệm liên quan

- [[Chuẩn OpenAPI]]
- [[Zero Configuration]]
- [[Swagger UI (-docs)|Swagger UI (/docs)]]
- [[ReDoc (-redoc)|ReDoc (/redoc)]]
- [[Try it out - Execute|Try it out / Execute]]
- [[Tags metadata phân nhóm API]]

— Thuộc [[Session 02 — MOC]]
