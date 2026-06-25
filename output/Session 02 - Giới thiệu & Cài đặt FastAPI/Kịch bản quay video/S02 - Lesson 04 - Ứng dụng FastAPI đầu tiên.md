---
type: "kich-ban-video"
title: "Lesson 04 - Ứng dụng FastAPI đầu tiên"
session: 2
lesson: 3
tags:
  - "type/kich-ban-video"
  - "session/02"
concepts:
  - "[[Đối tượng FastAPI app]]"
  - "[[Decorator @app.get]]"
  - "[[Hàm xử lý trả Dictionary → JSON]]"
  - "[[Lệnh uvicorn main -app --reload|Lệnh uvicorn main:app --reload]]"
  - "[[Hot Reload]]"
  - "[[127.0.0.1 -8000|127.0.0.1:8000]]"
deliverable_filename: "Lesson 04 - Ứng dụng FastAPI đầu tiên"
status: "done"
---

## Cấu trúc một ứng dụng FastAPI tối thiểu

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về cách khởi tạo ứng dụng FastAPI đầu tiên trong file main.py, cách chạy server bằng Uvicorn để truy cập vào địa chỉ localhost cổng 8000, và cơ chế Hot Reload giúp các em phát triển nhanh hơn.

Sau hai bài đầu về lý thuyết và một bài về thiết lập môi trường, hôm nay là lúc các em được viết những dòng code FastAPI đầu tiên của mình. Thầy hứa với các em rằng nó đơn giản đến bất ngờ. Chỉ với vài dòng, chúng ta đã có một web API hoạt động được.

**[Chuyển tiếp slide]**

Các em hãy nhìn vào đoạn code mẫu trên màn hình. Đây là một ứng dụng FastAPI tối thiểu, được đặt trong file tên là main.py.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chào mừng đến FastAPI!"}
```

Thầy sẽ giải thích cho các em quy trình ba bước cốt lõi mà bất kỳ ứng dụng FastAPI nào cũng tuân theo. Bước thứ nhất, ở dòng đầu tiên, chúng ta nạp lớp FastAPI từ thư viện fastapi vào, bằng câu lệnh from fastapi import FastAPI. Bước thứ hai, chúng ta tạo một thực thể của lớp đó và đặt tên là app, qua dòng app bằng FastAPI mở đóng ngoặc. Biến app này chính là trái tim của ứng dụng, là đối tượng đại diện cho toàn bộ web API của chúng ta.

Bước thứ ba là phần thú vị nhất: định nghĩa route và hàm xử lý. Các em hãy để ý dòng có ký hiệu a còng app chấm get, kèm theo một đường dẫn trong ngoặc. Dòng này được gọi là decorator. Nó nói với FastAPI rằng: khi có ai đó gửi một Request theo phương thức GET đến đường dẫn này, thì hãy gọi hàm nằm ngay bên dưới để xử lý.

- Bước 1: nạp lớp FastAPI bằng from fastapi import FastAPI.
- Bước 2: tạo thực thể app = FastAPI().
- Bước 3: định nghĩa route bằng decorator @app.get và hàm xử lý.

Trong ví dụ này, đường dẫn là một dấu gạch chéo, tức là trang gốc của ứng dụng. Hàm xử lý read_root chỉ làm một việc đơn giản: trả về một dictionary của Python, ở đây là một cặp khóa message và giá trị là câu chào. Và đây là điểm thầy muốn các em ghi nhớ thật kỹ: khi hàm xử lý trả về một dictionary, FastAPI sẽ tự động chuyển nó thành JSON cho các em, đúng như định dạng chúng ta đã học ở những bài đầu.

**[Chuyển tiếp slide]**

## Một ví dụ nghiệp vụ thực tế

Để các em thấy FastAPI không chỉ dùng để chào hỏi, thầy sẽ đưa ra một ví dụ gần với công việc thực tế hơn. Hãy hình dung chúng ta cần xây một API giám sát trạng thái cho một cổng điều phối kho vận, tức một hệ thống Logistics. File này thầy đặt tên là gateway.py.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_system_status():
    """Trả về tình trạng vận hành tức thời của nhà kho trung tâm."""
    return {
        "gateway_status": "operational",
        "workload_ratio": 0.72,
        "active_nodes": ["VN-SGN-01", "VN-DAD-02"],
        "system_message": "Logistics Dispatcher running smoothly."
    }
```

Các em thấy đấy, cấu trúc vẫn y hệt ba bước ban nãy. Chỉ khác là hàm xử lý get_system_status bây giờ trả về một dictionary phong phú hơn: trạng thái cổng đang vận hành, tỷ lệ tải công việc là 0 phẩy 72, danh sách các nút kho đang hoạt động, và một thông điệp hệ thống. Tất cả những dữ liệu này sẽ được FastAPI gói thành JSON và gửi về cho bất kỳ ai gọi đến endpoint này, dù đó là một bảng điều khiển giám sát hay một ứng dụng di động.

**[Chuyển tiếp slide]**

## Chạy server bằng Uvicorn

Viết code xong rồi, nhưng các em còn nhớ điều thầy nhấn mạnh ở bài về kiến trúc không? FastAPI tự nó không lắng nghe cổng mạng. Nó cần một ASGI server để vận hành, và server đó chính là Uvicorn mà chúng ta đã cài đặt. Bây giờ thầy sẽ chạy ứng dụng.

**[mở terminal]**

```bash
uvicorn main:app --reload
```

Các em hãy nhìn kỹ lệnh này, thầy sẽ mổ xẻ từng phần. Đầu tiên là từ khóa uvicorn để gọi server. Tiếp theo là main hai chấm app. Phần main là tên file của các em, ở đây là main.py nên ghi là main. Phần app sau dấu hai chấm là tên biến instance mà chúng ta đã tạo, chính là biến app. Như vậy main hai chấm app có nghĩa là: hãy tìm biến app nằm trong file main.

- uvicorn: gọi ASGI server để chạy ứng dụng.
- main: tên file Python, ở đây là main.py.
- app: tên biến thực thể FastAPI bên trong file đó.
- --reload: tự động khởi động lại server mỗi khi code thay đổi.

Sau khi chạy lệnh, các em hãy quan sát log hiện ra trong terminal. Uvicorn báo rằng server đang lắng nghe tại địa chỉ http hai chấm gạch chéo gạch chéo 127 chấm 0 chấm 0 chấm 1 cổng 8000, đây cũng chính là localhost cổng 8000. Đây là địa chỉ mặc định mà các em cần nhớ và sẽ dùng xuyên suốt khóa học.

**[mở trình duyệt]**

Bây giờ thầy mở trình duyệt và truy cập vào địa chỉ localhost cổng 8000. Các em nhìn vào màn hình: trình duyệt hiển thị đúng đoạn JSON mà hàm xử lý của chúng ta trả về. Đồng thời, nếu các em quay lại terminal, sẽ thấy một dòng log mới với mã 200 OK. Con số 200 OK này xác nhận rằng Request đã được xử lý thành công. Vậy là ứng dụng FastAPI đầu tiên của các em đã thực sự hoạt động.

**[Chuyển tiếp slide]**

## Cơ chế Hot Reload

Phần cuối cùng, thầy muốn giải thích cho các em về cái cờ gạch gạch reload mà chúng ta đã thêm vào cuối lệnh chạy. Đây là một tính năng cực kỳ tiện lợi trong quá trình phát triển, gọi là Hot Reload.

Bình thường, mỗi khi các em sửa code, các em sẽ phải tắt server đi rồi khởi động lại để thay đổi có hiệu lực. Việc này lặp đi lặp lại rất mất thời gian. Cờ gạch gạch reload giải quyết điều đó: nó yêu cầu Uvicorn theo dõi file của các em, và mỗi khi phát hiện code thay đổi, nó sẽ tự động khởi động lại server giúp các em.

Để các em thấy rõ, thầy sẽ thử sửa nội dung câu chào trong code rồi lưu lại. Các em hãy nhìn terminal: Uvicorn lập tức báo nó đang reload và khởi động lại. Bây giờ thầy tải lại trang trên trình duyệt, nội dung mới đã xuất hiện ngay mà thầy không cần làm gì thêm. Tuy nhiên thầy lưu ý các em: cờ gạch gạch reload chỉ dùng trong môi trường phát triển, khi đưa lên môi trường thật để chạy chính thức thì chúng ta sẽ tắt nó đi.

**[Chuyển tiếp slide]**

## Tổng kết bài giảng

Như vậy là trong bài học hôm nay, thầy và các em đã xây dựng được ứng dụng FastAPI đầu tiên với quy trình ba bước: nạp lớp FastAPI, tạo thực thể app, và định nghĩa route bằng decorator. Chúng ta đã biết hàm xử lý trả về dictionary sẽ được tự động chuyển thành JSON, biết cách chạy server bằng lệnh uvicorn main hai chấm app gạch gạch reload, truy cập tại localhost cổng 8000, xác nhận thành công qua log 200 OK, và hiểu cơ chế Hot Reload. Vậy là project FastAPI đầu tiên của các em đã chạy bằng Uvicorn.

Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em trong các bài học tiếp theo.

## Khái niệm liên quan

- [[Đối tượng FastAPI app]]
- [[Decorator @app.get]]
- [[Hàm xử lý trả Dictionary → JSON]]
- [[Lệnh uvicorn main -app --reload|Lệnh uvicorn main:app --reload]]
- [[Hot Reload]]
- [[127.0.0.1 -8000|127.0.0.1:8000]]

— Thuộc [[Session 02 — MOC]]
