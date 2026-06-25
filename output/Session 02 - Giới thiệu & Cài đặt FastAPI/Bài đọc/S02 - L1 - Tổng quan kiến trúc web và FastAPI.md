---
type: "bai-doc"
title: "Tổng quan kiến trúc web và FastAPI"
session: 2
lesson: 1
tags:
  - "type/bai-doc"
  - "session/02"
concepts:
  - "[[Mô hình Client-Server]]"
  - "[[Request-Response & HTTP-HTTPS|Request/Response & HTTP/HTTPS]]"
  - "[[Định dạng JSON]]"
  - "[[Kiến trúc Decoupled (Frontend-Backend tách biệt)|Kiến trúc Decoupled (Frontend/Backend tách biệt)]]"
  - "[[SSR vs SPA vs API-first]]"
  - "[[FastAPI = Starlette + Pydantic]]"
  - "[[WSGI vs ASGI]]"
  - "[[Uvicorn (ASGI server)]]"
deliverable_filename: "BÀI ĐỌC_ TỔNG QUAN KIẾN TRÚC WEB VÀ FASTAPI_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Tổng Quan Kiến Trúc Web Và Vị Thế Của FastAPI

Trước khi viết dòng code FastAPI đầu tiên, chúng ta cần một bản đồ tư duy rõ ràng về cách các ứng dụng web vận hành. Nếu không hiểu một yêu cầu (request) đi từ trình duyệt đến máy chủ và quay về như thế nào, chúng ta sẽ chỉ học cú pháp một cách máy móc mà không nắm được vì sao mọi thứ được thiết kế như vậy. Bài đọc này dựng nền tảng kiến trúc: từ mô hình Client-Server, vòng đời Request-Response, định dạng JSON, cho đến lý do FastAPI đạt hiệu năng cao nhờ chuẩn ASGI và máy chủ Uvicorn.

Để các khái niệm không trừu tượng, chúng ta sẽ bám vào một tình huống thực tế quen thuộc: so sánh trải nghiệm khi mở một website tin tức truyền thống với khi dùng một ứng dụng hiện đại (ví dụ một ứng dụng tra cứu khóa học hay theo dõi đơn hàng Logistics). Cùng một thao tác 'xem dữ liệu', nhưng cách hệ thống phục vụ phía sau lại khác nhau căn bản — và chính sự khác biệt đó định hình ra nghề phát triển API mà chúng ta đang theo học.

## 1. Mô Hình Client-Server: Bộ Khung Của Mọi Ứng Dụng Web

Mọi ứng dụng web đều được xây trên một mô hình đơn giản nhưng nền tảng: mô hình Client-Server (máy khách - máy chủ). Client là phía gửi yêu cầu — thường là trình duyệt (Chrome, Firefox), ứng dụng di động, hoặc một công cụ như Postman. Server là phía tiếp nhận yêu cầu, xử lý logic nghiệp vụ, truy vấn dữ liệu và gửi trả kết quả. Hai phía này thường nằm trên hai máy tính khác nhau, giao tiếp qua mạng Internet.

Hãy hình dung một quán cà phê. Client là khách hàng gọi món; Server là người pha chế trong quầy. Khách không tự vào bếp lấy nguyên liệu, mà gửi yêu cầu (gọi món) và chờ nhận lại sản phẩm (ly cà phê). Việc tách bạch vai trò này cho phép một quán phục vụ đồng thời nhiều khách, và cho phép cùng một quầy pha chế phục vụ nhiều loại khách khác nhau. Đây chính là ý tưởng cốt lõi mà chúng ta sẽ thấy lặp lại xuyên suốt khóa học.

Trong vai trò người phát triển backend với FastAPI, chúng ta đứng ở phía Server. Nhiệm vụ của chúng ta là xây dựng một máy chủ biết lắng nghe yêu cầu, hiểu yêu cầu đó muốn gì, và trả về dữ liệu chính xác — bất kể yêu cầu đến từ một trang web, một ứng dụng di động, hay một hệ thống đối tác.

## 2. Vòng Đời Request - Response Qua Giao Thức HTTP/HTTPS

Client và Server không nói chuyện tùy tiện; chúng tuân theo một bộ quy tắc chung gọi là giao thức HTTP (HyperText Transfer Protocol). HTTPS là phiên bản HTTP có mã hóa, bảo mật đường truyền. HTTP/HTTPS là nền tảng của mọi ứng dụng web hiện đại — không có nó, các thiết bị khác nhau sẽ không thể hiểu nhau.

Một cuộc hội thoại HTTP luôn diễn ra theo một vòng đời cố định mà chúng ta gọi là Request-Response (Yêu cầu - Phản hồi):

1. Client tạo một Request (yêu cầu) và gửi đến Server. Request cho biết: muốn làm gì (phương thức), với tài nguyên nào (đường dẫn URL), kèm thông tin gì (headers, body).
2. Server tiếp nhận, phân tích Request, thực thi logic cần thiết (ví dụ tra cứu danh sách khóa học trong cơ sở dữ liệu).
3. Server đóng gói kết quả thành một Response (phản hồi) và gửi ngược về Client.
4. Client nhận Response, đọc mã trạng thái (status code) và phần dữ liệu (body) rồi hiển thị cho người dùng.

Điểm mấu chốt cần nhớ: mỗi Request đều nhận đúng một Response, và bản thân HTTP là giao thức 'stateless' (không nhớ trạng thái) — mỗi cuộc trao đổi là độc lập. Hiểu rõ vòng đời này giúp chúng ta gỡ lỗi nhanh hơn rất nhiều sau này: khi một API không chạy, chúng ta sẽ biết cần soi vào Request đã gửi gì và Response đã trả về mã trạng thái bao nhiêu.

> Mẹo thực hành: Mở DevTools của trình duyệt (phím F12), vào tab Network rồi tải lại một trang. Chúng ta sẽ thấy toàn bộ danh sách Request/Response thực tế — đây là cách trực quan nhất để quan sát giao thức HTTP đang vận hành.

## 3. JSON: Ngôn Ngữ Trao Đổi Dữ Liệu Giữa Frontend Và Backend

Khi Server trả dữ liệu về cho Client, dữ liệu cần một định dạng mà cả hai phía đều hiểu. Định dạng phổ biến nhất hiện nay là JSON (JavaScript Object Notation) — một định dạng văn bản nhẹ, dễ đọc với con người và dễ phân tích với máy tính. Gần như mọi API hiện đại, bao gồm các API chúng ta sẽ viết bằng FastAPI, đều trao đổi dữ liệu bằng JSON.

JSON tổ chức dữ liệu thành các cặp 'khóa - giá trị' (key - value). Quy tắc cú pháp quan trọng: tên khóa và giá trị kiểu chuỗi phải được bọc trong dấu nháy kép, còn giá trị kiểu số và boolean (true/false) thì không cần. Dưới đây là một Response JSON mẫu mà một Server trả về khi Client yêu cầu thông tin một bài viết:

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere",
  "body": "quia et suscipit..."
}
```

Hãy quan sát: "title" và "body" là chuỗi nên có nháy kép, còn "userId" và "id" là số nên đứng trơn. Cấu trúc rõ ràng này cho phép phía Frontend dễ dàng lấy ra từng trường để hiển thị. Khi viết API bằng FastAPI ở các bài sau, chúng ta sẽ thấy framework tự động chuyển một Dictionary của Python thành JSON đúng chuẩn như thế này mà không cần làm thủ công.

## 4. Web Truyền Thống (SSR) So Với Web Service/API (Decoupled)

Đến đây, chúng ta cần phân biệt hai trường phái kiến trúc, vì đây chính là lý do tồn tại của FastAPI và nghề phát triển API.

### Web truyền thống — Server-Side Rendering (SSR)

Trong mô hình SSR, mỗi lần người dùng truy cập, Server dựng sẵn toàn bộ trang HTML hoàn chỉnh (đã trộn dữ liệu và giao diện) rồi gửi cả trang về cho trình duyệt. Mỗi thao tác chuyển trang thường tải lại toàn bộ trang. Đây là cách các website tin tức đời đầu hoạt động. Ưu điểm là đơn giản, nhưng nhược điểm là Server vừa lo dữ liệu vừa lo giao diện, và một Server kiểu này khó tái sử dụng cho ứng dụng di động.

### Kiến trúc tách biệt — Decoupled (Frontend/Backend riêng)

Trong kiến trúc Decoupled hiện đại, Server không trả HTML nữa mà chỉ trả dữ liệu thuần dưới dạng JSON. Phần giao diện (Frontend, thường là một ứng dụng SPA — Single Page Application) tự lấy dữ liệu đó và tự dựng giao diện trong trình duyệt. Backend và Frontend trở thành hai dự án độc lập, giao tiếp với nhau qua API.

Lợi ích lớn nhất của kiến trúc Decoupled: một API duy nhất có thể phục vụ đồng thời nhiều loại Client. Ví dụ trong hệ thống quản lý khóa học, cùng một API trả danh sách khóa học có thể được dùng bởi website tra cứu, ứng dụng di động cho sinh viên, và cả hệ thống của một trường đối tác tích hợp vào. Đây là tinh thần 'API-first': thiết kế API trước, coi nó là sản phẩm trung tâm.

| Tiêu chí | Web truyền thống (SSR) | Kiến trúc Decoupled (API) |
| --- | --- | --- |
| Server trả về | Trang HTML hoàn chỉnh | Dữ liệu thuần (JSON) |
| Dựng giao diện | Tại Server | Tại Client (Frontend/SPA) |
| Tái sử dụng | Khó dùng lại cho mobile | Một API phục vụ web, mobile, đối tác |
| Phân tách vai trò | Server gánh cả dữ liệu lẫn giao diện | Backend lo dữ liệu, Frontend lo giao diện |

FastAPI sinh ra cho thế giới Decoupled này: nó là một framework chuyên dụng để xây dựng API trả JSON nhanh và an toàn — đúng vai trò Backend trong kiến trúc tách biệt.

## 5. FastAPI Là Gì? Starlette + Pydantic

FastAPI không phải là một khối liền mạch tự xây từ con số không. Nó được lắp ráp khéo léo từ hai thư viện trưởng thành, mỗi thư viện lo một mảng việc:

- Starlette — bộ công cụ web (web toolkit) lo phần 'đường đi' của ứng dụng: định tuyến (routing) các yêu cầu đến đúng hàm xử lý, quản lý middleware, xử lý kết nối bất đồng bộ.
- Pydantic — thư viện kiểm tra và xác thực dữ liệu (data validation) dựa trên type hints của Python: tự động kiểm tra dữ liệu đầu vào có đúng kiểu, đúng định dạng hay không.

Cách kết hợp này lý giải hai thế mạnh nổi bật của FastAPI mà chúng ta sẽ tận dụng suốt khóa học. Nhờ Starlette, FastAPI có hiệu năng cao và hỗ trợ bất đồng bộ. Nhờ Pydantic, FastAPI tự kiểm tra dữ liệu và tự sinh tài liệu API — giảm rất nhiều code lặp đi lặp lại cho lập trình viên.

## 6. WSGI So Với ASGI: Vì Sao FastAPI Nhanh

Để hiểu vì sao FastAPI đạt hiệu năng cao, chúng ta cần phân biệt hai chuẩn giao tiếp giữa máy chủ web và ứng dụng Python: WSGI và ASGI.

WSGI (Web Server Gateway Interface) là chuẩn cũ, được các framework như Django và Flask truyền thống sử dụng. WSGI xử lý đồng bộ (synchronous): mỗi yêu cầu chiếm trọn một thread (luồng) cho đến khi xử lý xong. Nếu một yêu cầu phải chờ đợi tác vụ chậm (ví dụ chờ cơ sở dữ liệu trả lời), thread đó bị 'khóa' và không làm việc khác được trong khi chờ.

ASGI (Asynchronous Server Gateway Interface) là chuẩn mới, hỗ trợ xử lý bất đồng bộ (asynchronous) với cú pháp async/await. Với ASGI, trong lúc một yêu cầu đang chờ tác vụ chậm, hệ thống có thể tạm gác nó lại để phục vụ yêu cầu khác, rồi quay lại khi tác vụ chậm hoàn tất. Nhờ vậy cùng một lượng tài nguyên có thể chịu tải đồng thời cao hơn nhiều.

| Tiêu chí | WSGI | ASGI |
| --- | --- | --- |
| Kiểu xử lý | Đồng bộ (synchronous) | Bất đồng bộ (async/await) |
| Framework tiêu biểu | Django, Flask (truyền thống) | FastAPI, Starlette |
| Khi gặp tác vụ chờ | Thread bị khóa cho đến khi xong | Tạm gác, phục vụ yêu cầu khác |
| Khả năng chịu tải | Hạn chế hơn | Cao hơn với cùng tài nguyên |

Cần nhấn mạnh: ASGI là một chuẩn (một quy ước), chứ chưa phải là chương trình thực thi. Để một ứng dụng FastAPI thực sự chạy và lắng nghe trên mạng, chúng ta cần một máy chủ ASGI cụ thể — đó là Uvicorn.

## 7. Uvicorn: Máy Chủ ASGI Đưa FastAPI Vào Vận Hành

Uvicorn là một ASGI server siêu nhanh, được xây trên thư viện uvloop và httptools hiệu năng cao. Vai trò của Uvicorn là lắng nghe các kết nối mạng đến, chuyển chúng cho ứng dụng FastAPI xử lý theo chuẩn ASGI, rồi gửi kết quả trả về. Sự kết hợp FastAPI + Uvicorn đưa hiệu năng của ứng dụng Python tiệm cận với các nền tảng nổi tiếng về tốc độ như NodeJS và Go.

Hãy ghi nhớ một sự thật quan trọng mà chúng ta sẽ gặp lại ở bài về khởi tạo ứng dụng: bản thân FastAPI không tự lắng nghe cổng mạng. FastAPI chỉ định nghĩa logic xử lý; chính Uvicorn mới là phần 'cắm điện' cho ứng dụng chạy lên. Đây là lý do lệnh khởi động sau này luôn là 'uvicorn ...' chứ không phải 'fastapi ...'.

## 8. Sơ Đồ Tổng Thể: Client → API → Database

Ghép tất cả lại, chúng ta có bức tranh kiến trúc đầy đủ của một ứng dụng backend hiện đại. Đây cũng chính là sản phẩm đầu ra của bài học này — vẽ được sơ đồ luồng dữ liệu ba tầng:

```text
[ CLIENT ]                    [ SERVER (API) ]               [ DATABASE ]
 Trình duyệt /                FastAPI + Uvicorn               MySQL / PostgreSQL
 Mobile App / Postman

   |  (1) Gửi HTTP Request           |                              |
   |  GET /courses  ---------------> |                              |
   |                                 |  (2) Xử lý logic, truy vấn    |
   |                                 |  ---------------------------> |
   |                                 |  (3) Trả về bản ghi           |
   |                                 |  <--------------------------- |
   |  (4) HTTP Response (JSON)        |                              |
   |  <----------------------------- |                              |
```

Đọc sơ đồ theo trình tự: (1) Client gửi một HTTP Request, ví dụ yêu cầu lấy danh sách khóa học. (2) Tầng API — gồm FastAPI lo logic và Uvicorn lo lắng nghe mạng — tiếp nhận và xử lý. (3) Nếu cần dữ liệu, API truy vấn Database và nhận về các bản ghi. (4) API đóng gói kết quả thành JSON và trả về cho Client dưới dạng Response. Trong toàn bộ khóa học, chúng ta tập trung xây dựng tầng ở giữa — tầng API.

## 9. Vận Dụng: Quan Sát Một API Thật Bằng Postman

Lý thuyết sẽ vững hơn khi gắn với quan sát thực tế. Chúng ta có thể dùng Postman — một công cụ phổ biến để gửi Request thủ công — để gọi thử một API công khai và đọc Response trả về. Đây cũng là cách chúng ta sẽ kiểm thử các API tự viết ở những bài sau.

1. Mở Postman, tạo một Request mới với phương thức GET.
2. Nhập một URL API mẫu trả JSON (ví dụ một endpoint công khai trả thông tin bài viết hoặc người dùng).
3. Bấm Send để gửi Request đi.
4. Quan sát ô Response: mã trạng thái 200 OK xác nhận thành công, và phần body là dữ liệu JSON tương tự ví dụ ở mục 3.

Qua bài tập nhỏ này, chúng ta đã hoàn thành trọn vẹn một vòng đời Request-Response thực sự: chúng ta đóng vai Client, gửi một Request HTTP đến một Server, và nhận lại một Response JSON. Đó chính xác là những gì các ứng dụng web làm hàng triệu lần mỗi giây.

## Tổng Kết

Bài đọc này đã dựng nền tảng kiến trúc để chúng ta bước vào FastAPI một cách tự tin. Những điểm cốt lõi cần nắm vững:

- Mọi ứng dụng web vận hành theo mô hình Client-Server, giao tiếp qua giao thức HTTP/HTTPS theo vòng đời Request-Response: mỗi yêu cầu nhận đúng một phản hồi.
- JSON là định dạng trao đổi dữ liệu nhẹ và phổ biến: tên khóa và chuỗi bọc trong nháy kép, số và boolean thì không.
- Kiến trúc Decoupled tách Backend (trả JSON) khỏi Frontend (dựng giao diện), cho phép một API phục vụ web, mobile và đối tác — đây là 'sân chơi' của FastAPI.
- FastAPI = Starlette (routing, hiệu năng, async) + Pydantic (xác thực dữ liệu, sinh tài liệu). ASGI cho phép xử lý bất đồng bộ, vượt giới hạn của WSGI đồng bộ.
- FastAPI không tự lắng nghe cổng mạng; Uvicorn là máy chủ ASGI đưa ứng dụng vào vận hành với hiệu năng tiệm cận NodeJS/Go.
- Sơ đồ trục: Client → API (FastAPI + Uvicorn) → Database; trong khóa học, chúng ta xây dựng tầng API ở giữa.

## Tài Liệu Tham Khảo

- FastAPI Official Documentation — Tutorial - User Guide: https://fastapi.tiangolo.com/tutorial/
- Starlette Documentation — The ASGI framework toolkit: https://www.starlette.io/
- Uvicorn Documentation — An ASGI web server for Python: https://www.uvicorn.org/
- MDN Web Docs — An overview of HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
- ASGI Documentation — Asynchronous Server Gateway Interface Specification: https://asgi.readthedocs.io/
- JSON Official Site — Introducing JSON: https://www.json.org/

## Khái niệm liên quan

- [[Mô hình Client-Server]]
- [[Request-Response & HTTP-HTTPS|Request/Response & HTTP/HTTPS]]
- [[Định dạng JSON]]
- [[Kiến trúc Decoupled (Frontend-Backend tách biệt)|Kiến trúc Decoupled (Frontend/Backend tách biệt)]]
- [[SSR vs SPA vs API-first]]
- [[FastAPI = Starlette + Pydantic]]
- [[WSGI vs ASGI]]
- [[Uvicorn (ASGI server)]]

— Thuộc [[Session 02 — MOC]]
