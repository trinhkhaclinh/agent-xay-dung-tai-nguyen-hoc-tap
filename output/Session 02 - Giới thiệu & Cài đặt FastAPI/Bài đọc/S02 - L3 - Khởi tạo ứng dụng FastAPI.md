---
type: "bai-doc"
title: "Khởi tạo ứng dụng FastAPI"
session: 2
lesson: 3
tags:
  - "type/bai-doc"
  - "session/02"
concepts:
  - "[[Đối tượng FastAPI app]]"
  - "[[Decorator @app.get]]"
  - "[[Hàm xử lý trả Dictionary → JSON]]"
  - "[[Lệnh uvicorn main -app --reload|Lệnh uvicorn main:app --reload]]"
  - "[[Hot Reload]]"
  - "[[127.0.0.1 -8000|127.0.0.1:8000]]"
deliverable_filename: "BÀI ĐỌC_ KHỞI TẠO ỨNG DỤNG FASTAPI ĐẦU TIÊN_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Khởi Tạo Ứng Dụng FastAPI Đầu Tiên

Sau khi đã hiểu kiến trúc web và thiết lập xong môi trường ảo, đây là thời điểm chúng ta biến lý thuyết thành một ứng dụng chạy thật. Bài đọc này hướng dẫn xây dựng một ứng dụng FastAPI tối thiểu nhưng hoàn chỉnh, chạy nó bằng Uvicorn, truy cập qua trình duyệt, và hiểu cơ chế Hot Reload giúp tăng tốc quá trình phát triển. Đây là cột mốc quan trọng: lần đầu tiên chúng ta có một máy chủ API của riêng mình lắng nghe và trả lời các yêu cầu.

Để tránh ví dụ đồ chơi, chúng ta sẽ xây dựng một API thực tế: cổng giám sát trạng thái vận hành của một hệ thống điều phối kho vận Logistics. API này trả về tình trạng tức thời của nhà kho trung tâm dưới dạng JSON — một loại API giám sát rất phổ biến trong vận hành hệ thống thật.

## 1. Kiến Trúc Bộ Đôi: FastAPI Định Nghĩa, Uvicorn Vận Hành

Trước khi viết code, chúng ta cần khắc sâu một nguyên lý đã nêu ở bài đầu tiên: FastAPI và Uvicorn là một bộ đôi với vai trò tách bạch. FastAPI là một framework — nó cho chúng ta công cụ để định nghĩa ứng dụng, khai báo các đường dẫn (route) và viết logic xử lý. Nhưng bản thân FastAPI không tự lắng nghe cổng mạng, không tự nhận kết nối từ trình duyệt.

Để ứng dụng thực sự chạy lên và phục vụ yêu cầu, chúng ta cần Uvicorn — một máy chủ ASGI. Uvicorn lắng nghe trên một cổng mạng, nhận kết nối đến, và chuyển chúng cho ứng dụng FastAPI xử lý. Đây là lý do lệnh khởi động luôn bắt đầu bằng 'uvicorn'. Hiểu sự phân vai này giúp chúng ta không bối rối khi gặp lỗi: nếu code FastAPI sai thì sửa logic, còn nếu server không lên thì soi lại lệnh Uvicorn.

## 2. Quy Trình Ba Bước Để Tạo Một Ứng Dụng FastAPI

Mọi ứng dụng FastAPI, dù lớn hay nhỏ, đều được dựng theo cùng một mạch ba bước. Nắm chắc mạch này, chúng ta có thể khởi tạo bất kỳ project nào mà không cần nhớ máy móc:

1. Nạp lớp FastAPI từ thư viện: import lớp FastAPI vào file của chúng ta.
2. Tạo một thực thể (instance) của ứng dụng: gán vào một biến, theo quy ước đặt tên là 'app'.
3. Định nghĩa route và hàm xử lý: dùng decorator để gắn một đường dẫn URL với một hàm Python sẽ trả về dữ liệu.

Hãy bắt đầu với phiên bản tối giản nhất để thấy rõ ba bước này, sau đó nâng cấp thành API Logistics thực tế.

## 3. Ví Dụ Tối Thiểu: File main.py

Trong thư mục dự án (với môi trường ảo đã kích hoạt từ bài trước), chúng ta tạo file main.py với nội dung sau:

```python
# Bước 1: Nạp lớp FastAPI từ thư viện
from fastapi import FastAPI

# Bước 2: Tạo thực thể ứng dụng, đặt tên biến là app theo quy ước
app = FastAPI()

# Bước 3: Định nghĩa route gốc "/" và hàm xử lý cho nó
@app.get("/")
def read_root():
    return {"message": "Chào mừng đến FastAPI!"}
```

Hãy đọc kỹ từng phần. Dòng 'from fastapi import FastAPI' nạp lớp framework. Dòng 'app = FastAPI()' tạo thực thể ứng dụng — biến app này chính là trái tim của toàn bộ ứng dụng, mọi route sau này đều gắn vào nó. Phần thú vị nhất là dòng '@app.get("/")': đây là một decorator, sẽ được giải thích kỹ ở mục tiếp theo.

## 4. Giải Mã Decorator @app.get Và Cơ Chế Trả JSON

Dòng '@app.get("/")' đặt ngay trên hàm read_root được gọi là một decorator (bộ trang trí). Nó nói với FastAPI rằng: 'Khi có một yêu cầu HTTP với phương thức GET gửi đến đường dẫn "/", hãy gọi hàm ngay bên dưới để xử lý'. Đường dẫn '/' là gốc của ứng dụng — tương ứng với địa chỉ chính của server.

Hàm xử lý read_root trả về một Dictionary của Python: {"message": "Chào mừng đến FastAPI!"}. Đây là điểm tinh tế và rất tiện lợi của FastAPI: chúng ta chỉ cần trả về một Dictionary, FastAPI sẽ TỰ ĐỘNG chuyển nó thành JSON đúng chuẩn trước khi gửi về cho Client. Chúng ta không phải gọi thư viện json hay tự định dạng chuỗi — framework lo phần đó.

> Liên hệ với bài đầu tiên: đây chính là minh chứng sống động cho kiến trúc Decoupled — Server (ứng dụng của chúng ta) trả về dữ liệu thuần dưới dạng JSON, không trả HTML. Một Dictionary Python in ra cửa sổ trình duyệt dưới dạng JSON gọn gàng.

## 5. Chạy Ứng Dụng Bằng Uvicorn

Code đã sẵn sàng, nhưng như đã nhấn mạnh, FastAPI không tự chạy. Chúng ta dùng Uvicorn để khởi động ứng dụng. Tại terminal (đang ở trong thư mục dự án và đã kích hoạt venv), gõ lệnh:

```bash
uvicorn main:app --reload
```

Lệnh này cần được mổ xẻ từng thành phần vì chúng ta sẽ dùng nó hàng trăm lần:

- uvicorn — gọi máy chủ ASGI Uvicorn để chạy ứng dụng.
- main — tên file Python chứa ứng dụng, ở đây là main.py (viết không kèm đuôi .py).
- app — tên biến instance FastAPI bên trong file đó (chính là biến app chúng ta tạo ở Bước 2).
- --reload — cờ bật chế độ Hot Reload, tự khởi động lại server mỗi khi mã nguồn thay đổi.

Cú pháp 'main:app' có thể đọc là 'lấy biến app từ file main'. Nếu file của chúng ta tên là gateway.py thì lệnh tương ứng sẽ là 'uvicorn gateway:app --reload'. Đây là lỗi cấu hình rất hay gặp ở người mới: gõ sai tên file hoặc tên biến khiến Uvicorn không tìm thấy ứng dụng.

## 6. Truy Cập Và Đọc Log Khởi Động

Sau khi chạy lệnh trên, Uvicorn khởi động và mặc định lắng nghe tại địa chỉ http://127.0.0.1:8000 (127.0.0.1 là 'localhost' — chính máy của chúng ta; 8000 là số cổng mặc định). Mở trình duyệt và truy cập địa chỉ này, chúng ta sẽ thấy JSON trả về: {"message":"Chào mừng đến FastAPI!"}.

Đồng thời, terminal sẽ in ra các dòng log. Dòng log quan trọng nhất xác nhận server hoạt động bình thường có dạng như sau:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
INFO:     127.0.0.1:54321 - "GET / HTTP/1.1" 200 OK
```

Dòng cuối cho thấy một yêu cầu GET đến đường dẫn '/' đã được xử lý với mã trạng thái 200 OK — đúng như vòng đời Request-Response chúng ta học ở bài đầu tiên. Mã 200 OK là tín hiệu vàng xác nhận mọi thứ hoạt động. Để dừng server, nhấn tổ hợp phím Ctrl+C.

## 7. Hot Reload: Vì Sao Cờ --reload Quan Trọng

Trong quá trình phát triển, chúng ta sửa code liên tục. Nếu mỗi lần sửa đều phải tự tay dừng và khởi động lại server, công việc sẽ rất chậm và bực bội. Cờ --reload giải quyết điều đó: Uvicorn theo dõi các file mã nguồn, và mỗi khi phát hiện thay đổi được lưu, nó tự động khởi động lại ứng dụng. Đây gọi là cơ chế Hot Reload.

Nhờ Hot Reload, vòng lặp 'sửa code — lưu — xem kết quả' diễn ra gần như tức thì, tăng tốc độ phát triển đáng kể. Tuy nhiên cần lưu ý một nguyên tắc quan trọng về môi trường vận hành:

> Cờ --reload chỉ dùng trong môi trường phát triển (development). KHÔNG bao giờ bật --reload trên môi trường sản xuất (production) thật, vì nó tiêu tốn tài nguyên cho việc theo dõi file và không cần thiết khi code đã ổn định.

## 8. Vận Dụng: API Giám Sát Cổng Điều Phối Logistics

Giờ chúng ta nâng cấp từ ví dụ chào mừng tối giản lên một API thực tế. Tạo file gateway.py mô phỏng cổng giám sát trạng thái vận hành của nhà kho trung tâm trong hệ thống Logistics. API này trả về một cấu trúc JSON giàu thông tin hơn, gồm trạng thái cổng, tỉ lệ tải, các nút đang hoạt động và thông điệp hệ thống:

```python
# gateway.py — Cổng giám sát trạng thái hệ thống điều phối Logistics
from fastapi import FastAPI

# Tạo thực thể ứng dụng
app = FastAPI()

@app.get("/")
def get_system_status():
    """Trả về tình trạng vận hành tức thời của nhà kho trung tâm."""
    return {
        "gateway_status": "operational",       # trạng thái tổng thể của cổng
        "workload_ratio": 0.72,                  # tỉ lệ tải hiện tại (72%)
        "active_nodes": ["VN-SGN-01", "VN-DAD-02"],  # các nút kho đang hoạt động
        "system_message": "Logistics Dispatcher running smoothly."
    }
```

Quan sát cấu trúc dữ liệu trả về: nó bao gồm một chuỗi (gateway_status), một số thực (workload_ratio), một danh sách (active_nodes) và một chuỗi thông điệp. FastAPI vẫn tự động chuyển toàn bộ Dictionary lồng nhau này thành JSON hợp lệ. Hàm còn có một docstring tiếng Việt mô tả nhiệm vụ — chi tiết nhỏ này sẽ trở nên hữu ích ở bài về tài liệu tự động, vì FastAPI có thể đọc docstring để đưa vào tài liệu API.

Để chạy API này, vì file tên gateway.py, lệnh khởi động tương ứng là:

```bash
uvicorn gateway:app --reload
```

Truy cập http://127.0.0.1:8000, chúng ta sẽ thấy JSON trạng thái kho hiện ra. Hãy thử thay đổi giá trị workload_ratio trong code rồi lưu lại: nhờ Hot Reload, chỉ cần tải lại trình duyệt là thấy giá trị mới ngay, không cần khởi động lại server thủ công. Đến đây, chúng ta đã hoàn thành sản phẩm đầu ra của bài học: project FastAPI đầu tiên chạy được bằng Uvicorn.

## Tổng Kết

Bài đọc đã đưa chúng ta từ một thư mục trống đến một máy chủ API đang chạy thật. Những điểm kỹ thuật cốt lõi cần ghi nhớ:

- FastAPI định nghĩa ứng dụng và logic; Uvicorn (máy chủ ASGI) đưa ứng dụng vào vận hành — FastAPI không tự lắng nghe cổng mạng.
- Quy trình ba bước: nạp lớp FastAPI → tạo thực thể app → định nghĩa route bằng decorator và hàm xử lý.
- Hàm xử lý chỉ cần trả về một Dictionary; FastAPI tự động chuyển thành JSON gửi cho Client.
- Lệnh chạy: 'uvicorn main:app --reload', trong đó main là tên file, app là biến instance, --reload bật Hot Reload tự khởi động lại khi sửa code.
- Mặc định server lắng nghe tại http://127.0.0.1:8000; log '200 OK' xác nhận yêu cầu được xử lý thành công; Ctrl+C để dừng.
- Cờ --reload chỉ dùng khi phát triển, không dùng trên môi trường sản xuất.

## Tài Liệu Tham Khảo

- FastAPI Official Documentation — First Steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- FastAPI Official Documentation — Run a Server Manually (Uvicorn): https://fastapi.tiangolo.com/deployment/manually/
- Uvicorn Documentation — Running with the command line: https://www.uvicorn.org/#running-with-the-command-line
- FastAPI Official Documentation — Path Operation Decorators: https://fastapi.tiangolo.com/tutorial/first-steps/#path-operation-decorator
- Python Official Documentation — Data Structures (Dictionaries): https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Khái niệm liên quan

- [[Đối tượng FastAPI app]]
- [[Decorator @app.get]]
- [[Hàm xử lý trả Dictionary → JSON]]
- [[Lệnh uvicorn main -app --reload|Lệnh uvicorn main:app --reload]]
- [[Hot Reload]]
- [[127.0.0.1 -8000|127.0.0.1:8000]]

— Thuộc [[Session 02 — MOC]]
