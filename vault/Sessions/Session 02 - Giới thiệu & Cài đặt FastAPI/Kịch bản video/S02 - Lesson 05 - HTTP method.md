---
type: "kich-ban-video"
title: "Lesson 05 - HTTP method"
session: 2
lesson: 4
tags:
  - "type/kich-ban-video"
  - "session/02"
concepts:
  - "[[HTTP Request (Method-URL-Headers-Body)|HTTP Request (Method/URL/Headers/Body)]]"
  - "[[HTTP Response (Status Code-Headers-Body)|HTTP Response (Status Code/Headers/Body)]]"
  - "[[Ánh xạ CRUD ↔ HTTP Method]]"
  - "[[Endpoint định danh tài nguyên]]"
  - "[[RESTful naming]]"
  - "[[Decorator routing (@app.get-post-put-delete)|Decorator routing (@app.get/post/put/delete)]]"
  - "[[Routing Engine]]"
deliverable_filename: "Lesson 05 - HTTP method"
status: "done"
---

## Cấu trúc HTTP Request và Response

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về cấu trúc của HTTP Request và Response, các phương thức HTTP cốt lõi, quy chuẩn đặt tên endpoint theo phong cách RESTful, và cách FastAPI định tuyến Request đến đúng hàm xử lý qua decorator.

Ở những bài trước, chúng ta đã tạo được endpoint trả về JSON. Nhưng một ứng dụng thật sự cần làm được nhiều việc hơn là chỉ đọc dữ liệu: nó còn phải tạo mới, cập nhật, và xóa. Để làm được điều đó một cách bài bản, các em cần hiểu sâu hơn về HTTP.

**[Chuyển tiếp slide]**

Các em hãy nhìn vào sơ đồ trên màn hình. Mỗi cuộc hội thoại trên web đều gồm hai phần: một Request do Client gửi đi, và một Response do Server trả về. Đây chính là nền tảng của mọi RESTful API mà các em sẽ xây dựng.

Một HTTP Request gồm bốn thành phần chính. Thứ nhất là Method, tức phương thức, cho biết Client muốn làm gì. Thứ hai là URL, tức địa chỉ tài nguyên muốn tác động tới. Thứ ba là Headers, chứa các thông tin đi kèm như định dạng dữ liệu hay thông tin xác thực. Thứ tư là Body, chứa dữ liệu mà Client gửi lên, thường có ở các thao tác tạo mới hay cập nhật.

- HTTP Request gồm: Method, URL, Headers, Body.
- HTTP Response gồm: Status Code, Headers, Body.
- Mỗi cuộc hội thoại HTTP luôn là một cặp Request và Response.

Tương ứng, một HTTP Response cũng có các thành phần: Status Code, tức mã trạng thái cho biết kết quả ra sao, ví dụ 200 là thành công, 404 là không tìm thấy. Tiếp đến là Headers và Body chứa dữ liệu trả về. Khi các em hiểu rõ cấu trúc này, các em sẽ đọc được mọi cuộc trao đổi giữa Client và Server.

**[Chuyển tiếp slide]**

## Các phương thức HTTP và ánh xạ CRUD

Bây giờ chúng ta đi vào trọng tâm: các phương thức HTTP cốt lõi. Thầy muốn các em ghi nhớ năm phương thức quan trọng nhất và ý nghĩa của chúng, bởi vì chúng ánh xạ trực tiếp với bốn thao tác cơ bản trên dữ liệu mà ta gọi tắt là CRUD: Create, Read, Update, Delete.

Các em hãy nhìn bảng ánh xạ trên màn hình. Phương thức GET dùng để đọc dữ liệu, tương ứng với Read. Phương thức POST dùng để tạo mới dữ liệu, tương ứng với Create. Phương thức PUT dùng để cập nhật toàn bộ một tài nguyên. Phương thức PATCH dùng để cập nhật một phần. Và phương thức DELETE dùng để xóa, tương ứng với Delete.

- GET tương ứng Read: đọc dữ liệu.
- POST tương ứng Create: tạo mới dữ liệu.
- PUT: cập nhật toàn bộ tài nguyên.
- PATCH: cập nhật một phần tài nguyên.
- DELETE tương ứng Delete: xóa dữ liệu.

Đây là điểm mấu chốt mà thầy muốn các em khắc cốt ghi tâm: hành động được xác định bởi HTTP Method, chứ không phải bởi URL. Nghĩa là cùng một địa chỉ, ví dụ đường dẫn students, nhưng nếu gửi bằng GET thì nghĩa là đọc danh sách sinh viên, còn nếu gửi bằng POST thì lại là tạo một sinh viên mới. Phương thức mới là thứ quyết định ý nghĩa của hành động.

**[Chuyển tiếp slide]**

## Quy chuẩn đặt tên endpoint RESTful

Hiểu được rằng phương thức quyết định hành động, các em sẽ thấy việc đặt tên endpoint trở nên gọn gàng hơn rất nhiều. Đây chính là tinh thần của quy chuẩn RESTful mà thầy muốn các em tuân theo ngay từ đầu để tạo thói quen tốt.

Quy tắc thứ nhất: endpoint nên đặt tên bằng danh từ số nhiều để chỉ một tập hợp tài nguyên. Ví dụ trong hệ thống quản lý sinh viên, chúng ta dùng đường dẫn students cho tập hợp sinh viên, và courses cho tập hợp khóa học. Quy tắc thứ hai, cũng rất quan trọng: tuyệt đối không nhúng động từ vào trong URL.

- Đúng: /students, /courses, /students/{id}/grades.
- Sai: /getStudents, /createCourse vì đã nhúng động từ vào URL.
- Hành động lấy hay tạo do HTTP Method quyết định, không phải do URL.

Các em hãy nhìn các ví dụ trên màn hình. Cách viết đúng là dùng danh từ số nhiều như students hay courses. Cách viết sai là những kiểu như getStudents hay createCourse, vì các em đã nhét động từ get và create vào URL. Điều này thừa thãi, bởi vì việc lấy hay tạo đã do phương thức GET hoặc POST đảm nhiệm rồi. Với những tài nguyên lồng nhau, ta có thể viết như students gạch chéo id gạch chéo grades để chỉ bảng điểm của một sinh viên cụ thể.

**[Chuyển tiếp slide]**

## Routing Engine và endpoint trong FastAPI

Bây giờ thầy sẽ cho các em thấy tất cả những điều trên được thể hiện trong code FastAPI như thế nào. Các em hãy nhìn đoạn code mẫu trên màn hình, gồm một endpoint hello đơn giản và vài endpoint cho hệ thống quản lý sinh viên.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello!"}

@app.get("/students")
def list_students():
    return [{"id": 1, "name": "An"}]

@app.post("/students")
def create_student(name: str):
    return {"id": 2, "name": name}
```

Các em hãy quan sát kỹ. Endpoint đầu tiên dùng a còng app chấm get với đường dẫn hello, gọi hàm say_hello trả về một lời chào. Đây là endpoint hello đơn giản mà sản phẩm đầu ra của bài yêu cầu các em làm được. Tiếp theo, hãy để ý hai endpoint cùng trỏ tới đường dẫn students nhưng khác phương thức: một cái là app chấm get để liệt kê danh sách sinh viên, một cái là app chấm post để tạo sinh viên mới. Đây chính là minh chứng sống động cho điều thầy đã nói: cùng URL, khác method, khác hành động.

Vậy FastAPI làm cách nào để biết phải gọi hàm nào? Đó là nhờ một bộ phận gọi là Routing Engine, tức là động cơ định tuyến. Khi một Request đến, Routing Engine của FastAPI sẽ dò xét cặp gồm đường dẫn URL và phương thức HTTP, rồi đối chiếu với các decorator mà các em đã khai báo, để ánh xạ Request đó tới đúng hàm xử lý Python tương ứng.

Như vậy, cái decorator a còng app chấm get hay app chấm post mà các em viết không chỉ là cú pháp trang trí. Nó chính là cách các em đăng ký với Routing Engine rằng: cặp method và đường dẫn này sẽ do hàm này phụ trách. Hiểu được điều này, các em đã nắm được linh hồn của việc xây dựng API với FastAPI.

**[Chuyển tiếp slide]**

## Tổng kết bài giảng

Như vậy là trong bài học hôm nay, thầy và các em đã hiểu rõ cấu trúc HTTP Request gồm Method, URL, Headers, Body và Response gồm Status Code, Headers, Body. Chúng ta đã nắm năm phương thức cốt lõi và cách chúng ánh xạ với CRUD: GET là Read, POST là Create, PUT và PATCH là Update, DELETE là Delete. Chúng ta cũng học được quy chuẩn đặt tên RESTful với danh từ số nhiều và không nhúng động từ, ghi nhớ rằng hành động do method quyết định, và hiểu Routing Engine của FastAPI dò method cùng path để gọi đúng hàm. Endpoint hello của các em đã hoạt động.

Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em trong các bài học tiếp theo.

## Khái niệm liên quan

- [[HTTP Request (Method-URL-Headers-Body)|HTTP Request (Method/URL/Headers/Body)]]
- [[HTTP Response (Status Code-Headers-Body)|HTTP Response (Status Code/Headers/Body)]]
- [[Ánh xạ CRUD ↔ HTTP Method]]
- [[Endpoint định danh tài nguyên]]
- [[RESTful naming]]
- [[Decorator routing (@app.get-post-put-delete)|Decorator routing (@app.get/post/put/delete)]]
- [[Routing Engine]]

— Thuộc [[Session 02 — MOC]]
