---
type: "kich-ban-video"
title: "Lesson 06 - Tài liệu API tự động"
session: 2
lesson: 5
tags:
  - "type/kich-ban-video"
  - "session/02"
concepts:
  - "[[Chuẩn OpenAPI]]"
  - "[[Zero Configuration]]"
  - "[[Swagger UI (-docs)|Swagger UI (/docs)]]"
  - "[[ReDoc (-redoc)|ReDoc (/redoc)]]"
  - "[[Try it out - Execute|Try it out / Execute]]"
  - "[[Tags metadata phân nhóm API]]"
deliverable_filename: "Lesson 06 - Tài liệu API tự động"
status: "done"
---

## Chuẩn OpenAPI và tài liệu tự động

Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về chuẩn OpenAPI và khả năng tự sinh tài liệu của FastAPI, cách sử dụng Swagger UI tại đường dẫn docs để đọc và kiểm thử API ngay trên trình duyệt, cũng như cách phân biệt Swagger UI với ReDoc.

Đây là một trong những tính năng khiến rất nhiều lập trình viên yêu thích FastAPI ngay từ lần đầu sử dụng. Các em hãy hình dung: thông thường, sau khi viết API xong, người ta còn phải ngồi viết tài liệu mô tả từng endpoint cho người khác dùng, vừa tốn công vừa dễ lạc hậu so với code. FastAPI giải quyết triệt để vấn đề này.

**[Chuyển tiếp slide]**

Trước hết, thầy giới thiệu với các em chuẩn OpenAPI. Đây là một tiêu chuẩn quốc tế dùng để mô tả các REST API một cách thống nhất, để máy móc và con người đều hiểu được cấu trúc của một API. Và điều tuyệt vời là FastAPI tuân thủ hoàn toàn chuẩn OpenAPI này.

Vậy FastAPI tận dụng điều đó như thế nào? Đây chính là khái niệm thầy muốn các em ghi nhớ: Zero Configuration, nghĩa là không cần cấu hình gì thêm. FastAPI tự động đọc cấu trúc các hàm xử lý của các em, đọc các kiểu dữ liệu mà các em khai báo, rồi từ đó tự sinh ra tài liệu API hoàn chỉnh. Các em không phải viết thêm một dòng tài liệu nào, mà tài liệu vẫn luôn khớp với code, vì nó được sinh ra trực tiếp từ code.

- OpenAPI: tiêu chuẩn quốc tế mô tả REST API, FastAPI tuân thủ hoàn toàn.
- Zero Configuration: FastAPI tự sinh tài liệu, không cần cấu hình thêm.
- Tài liệu luôn khớp với code vì được sinh ra từ chính cấu trúc hàm và kiểu dữ liệu.

**[Chuyển tiếp slide]**

## Trải nghiệm Swagger UI

Lý thuyết là vậy, bây giờ thầy sẽ cho các em thấy tài liệu tự động đó trông như thế nào trong thực tế. Giả sử chúng ta đang chạy ứng dụng quản lý khóa học. Thầy sẽ mở trình duyệt và truy cập vào giao diện tài liệu.

**[mở trình duyệt]**

Giao diện tài liệu mặc định của FastAPI gọi là Swagger UI, và nó nằm tại địa chỉ localhost cổng 8000, thêm đường dẫn gạch chéo docs. Thầy gõ địa chỉ này vào trình duyệt. Các em hãy nhìn vào màn hình: một trang web đẹp mắt hiện ra, liệt kê toàn bộ các endpoint mà chúng ta đã định nghĩa, kèm phương thức HTTP của từng cái được tô màu khác nhau cho dễ phân biệt.

Điều đặc biệt của Swagger UI là nó không chỉ để đọc. Thầy muốn các em ghi nhớ: Swagger UI vừa là tài liệu, vừa là một môi trường kiểm thử tương tác. Nghĩa là các em có thể gọi thử API ngay tại đây, mà không cần đến công cụ ngoài như Postman.

Để các em thấy rõ, thầy sẽ bấm vào một endpoint, ví dụ endpoint lấy danh sách khóa học. Khi mở rộng ra, các em thấy có một nút mang tên Try it out. Thầy bấm vào nút Try it out này. Bây giờ giao diện cho phép thầy nhập tham số nếu cần, và xuất hiện thêm một nút Execute để thực thi.

**[nhấn nút Try it out trên Swagger UI]**

**[nhấn nút Execute trên Swagger UI]**

Thầy bấm nút Execute. Các em hãy quan sát phần kết quả phía dưới. Swagger UI hiển thị ngay Response mà server trả về: bao gồm mã trạng thái, ví dụ 200, và phần Body chứa dữ liệu JSON. Như vậy chỉ với vài cú nhấp chuột, các em đã kiểm thử được endpoint của mình ngay trên trình duyệt, cực kỳ tiện lợi khi vừa phát triển vừa muốn thử nhanh.

**[Chuyển tiếp slide]**

## Tùy biến tài liệu và ReDoc

Tài liệu tự động đã đẹp sẵn, nhưng FastAPI còn cho phép các em làm cho nó chuyên nghiệp hơn nữa bằng cách khai báo một số thông tin mô tả. Các em hãy nhìn đoạn code trên màn hình.

```python
from fastapi import FastAPI

app = FastAPI(
    title="Course Management API",
    description="API quản lý khóa học cho trung tâm đào tạo",
    version="1.0.0"
)

@app.get("/courses", tags=["courses"])
def list_courses():
    return [{"id": 1, "name": "Web API with FastAPI"}]
```

Khi tạo thực thể FastAPI, các em có thể truyền vào tiêu đề qua tham số title, mô tả qua description, và phiên bản qua version. Những thông tin này sẽ hiển thị ngay trên đầu trang tài liệu, giúp người đọc biết họ đang xem API của hệ thống nào. Ngoài ra, các em để ý ở decorator có thêm tham số tags. Tham số này dùng để phân nhóm các endpoint lại với nhau, giúp tài liệu gọn gàng khi API của các em lớn dần lên với hàng chục endpoint.

- title, description, version: hiển thị thông tin tổng quan đầu trang tài liệu.
- tags: phân nhóm các endpoint cho tài liệu gọn gàng, dễ tra cứu.

Cuối cùng, thầy muốn giới thiệu thêm cho các em một giao diện tài liệu thứ hai mà FastAPI cũng tự sinh ra, đó là ReDoc. ReDoc nằm tại địa chỉ localhost cổng 8000 thêm đường dẫn gạch chéo redoc. Thầy mở thử địa chỉ này trên trình duyệt.

Các em hãy so sánh hai giao diện. Swagger UI ở đường dẫn docs mạnh về tương tác và kiểm thử, với các nút Try it out và Execute. Còn ReDoc ở đường dẫn redoc có giao diện ba cột tối giản, được tối ưu cho việc đọc và tra cứu tài liệu một cách thoải mái, phù hợp khi các em muốn chia sẻ tài liệu cho đối tác đọc. Cùng một API, các em có hai cách trình bày để chọn lựa tùy mục đích.

- Swagger UI tại /docs: tài liệu cộng kiểm thử tương tác, có Try it out và Execute.
- ReDoc tại /redoc: giao diện ba cột tối giản, tối ưu cho đọc và tra cứu.

**[Chuyển tiếp slide]**

## Tổng kết bài giảng

Như vậy là trong bài học hôm nay, thầy và các em đã hiểu chuẩn quốc tế OpenAPI và khả năng tự sinh tài liệu theo tinh thần Zero Configuration của FastAPI. Chúng ta đã trải nghiệm Swagger UI tại đường dẫn docs, vừa đọc tài liệu vừa kiểm thử API bằng Try it out và Execute ngay trên trình duyệt. Chúng ta cũng biết cách bổ sung title, description, version và dùng tags để phân nhóm endpoint, cũng như phân biệt được Swagger UI với ReDoc tại đường dẫn redoc. Đến đây Swagger đã hiển thị và test được API của các em.

Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại các em trong các bài học tiếp theo.

## Khái niệm liên quan

- [[Chuẩn OpenAPI]]
- [[Zero Configuration]]
- [[Swagger UI (-docs)|Swagger UI (/docs)]]
- [[ReDoc (-redoc)|ReDoc (/redoc)]]
- [[Try it out - Execute|Try it out / Execute]]
- [[Tags metadata phân nhóm API]]

— Thuộc [[Session 02 — MOC]]
