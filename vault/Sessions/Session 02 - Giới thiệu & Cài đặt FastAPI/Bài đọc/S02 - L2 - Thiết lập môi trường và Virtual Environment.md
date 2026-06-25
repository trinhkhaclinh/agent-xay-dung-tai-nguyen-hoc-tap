---
type: "bai-doc"
title: "Thiết lập môi trường và Virtual Environment"
session: 2
lesson: 2
tags:
  - "type/bai-doc"
  - "session/02"
concepts:
  - "[[Xung đột phiên bản (version conflict)]]"
  - "[[Virtual Environment (venv)]]"
  - "[[Kích hoạt-Hủy kích hoạt môi trường|Kích hoạt/Hủy kích hoạt môi trường]]"
  - "[[pip]]"
  - "[[requirements.txt]]"
  - "[[gitignore|.gitignore]]"
deliverable_filename: "BÀI ĐỌC_ THIẾT LẬP MÔI TRƯỜNG VÀ VIRTUAL ENVIRONMENT_"
status: "done"
---

# Bài Đọc Chuyên Sâu: Thiết Lập Môi Trường Và Virtual Environment

Một dự án phần mềm chuyên nghiệp luôn bắt đầu bằng việc thiết lập môi trường làm việc đúng cách, trước cả khi viết dòng code chức năng đầu tiên. Nghe có vẻ là một bước thủ tục khô khan, nhưng đây là kỹ năng phân biệt giữa một người mới làm tùy hứng và một lập trình viên có kỷ luật. Bài đọc này giải thích vì sao chúng ta bắt buộc phải dùng môi trường ảo (Virtual Environment), cách tạo và kích hoạt nó trên nhiều hệ điều hành, và cách đóng gói danh sách thư viện để cả nhóm tái tạo môi trường giống hệt nhau.

Tình huống dẫn dắt rất thường gặp trong thực tế: chúng ta đang phụ trách hai dự án song song. Dự án A — hệ thống quản lý sinh viên — cần một thư viện ở phiên bản 1.0. Dự án B — cổng điều phối Logistics — lại cần đúng thư viện đó nhưng ở phiên bản 2.0, vì có những tính năng mới. Nếu cả hai cùng dùng chung một bản cài Python, chúng ta sẽ rơi vào một mớ rắc rối mà phần tiếp theo sẽ mô tả.

## 1. Vấn Đề Cốt Lõi: Xung Đột Phiên Bản Thư Viện

Khi cài một thư viện trực tiếp vào bản Python của hệ thống (gọi là global/system Python), thư viện đó được đặt vào một thư mục dùng chung cho mọi dự án trên máy. Hệ quả là mọi dự án buộc phải dùng chung một phiên bản duy nhất của mỗi thư viện.

Quay lại tình huống của chúng ta: nếu cài thư viện X phiên bản 2.0 cho dự án Logistics, thì dự án quản lý sinh viên (vốn cần phiên bản 1.0) có thể đột nhiên chạy sai hoặc báo lỗi, vì hành vi của thư viện đã thay đổi giữa hai phiên bản. Ngược lại, hạ xuống 1.0 lại làm hỏng dự án Logistics. Đây chính là hiện tượng xung đột phiên bản (version conflict) — một trong những nguyên nhân gây 'lỗi không rõ vì sao' phổ biến nhất với người mới.

> Nguyên tắc vàng: Không bao giờ cài thư viện của dự án trực tiếp vào Python hệ thống. Mỗi dự án xứng đáng có một không gian thư viện riêng, biệt lập với các dự án khác.

## 2. Giải Pháp: Virtual Environment (Môi Trường Ảo)

Virtual Environment (viết tắt venv) là một môi trường Python biệt lập dành riêng cho một dự án. Khi tạo một venv, Python sao chép một trình thông dịch (interpreter) và một bộ công cụ pip riêng vào một thư mục cục bộ của dự án. Mọi thư viện cài trong môi trường ảo này chỉ tồn tại trong dự án đó, hoàn toàn không ảnh hưởng đến Python hệ thống hay các dự án khác.

Hãy hình dung mỗi venv như một 'phòng làm việc kín' riêng cho từng dự án. Dự án quản lý sinh viên có phòng riêng với thư viện X v1.0; dự án Logistics có phòng riêng với thư viện X v2.0. Hai phòng không bao giờ giẫm chân lên nhau. Đây chính là cách giải quyết triệt để vấn đề xung đột phiên bản ở mục 1.

Trong khóa học này, mỗi project FastAPI chúng ta tạo ra đều bắt đầu bằng một venv riêng. Đây không phải khuyến nghị tùy chọn, mà là một chuẩn mực bắt buộc của làm việc nhóm chuyên nghiệp.

## 3. Tạo Môi Trường Ảo

Python từ phiên bản 3.3 trở đi đã tích hợp sẵn module venv, nên chúng ta không cần cài thêm gì. Trước hết, di chuyển terminal vào thư mục gốc của dự án, ví dụ thư mục của cổng điều phối Logistics. Sau đó chạy lệnh tạo môi trường ảo:

```bash
# Tạo một môi trường ảo tên là "venv" ngay trong thư mục dự án
python -m venv venv
```

Giải thích lệnh: 'python -m venv' yêu cầu Python chạy module venv, còn 'venv' cuối cùng là tên thư mục môi trường ảo sẽ được tạo (tên này có thể đặt khác, nhưng 'venv' là quy ước phổ biến nhất). Sau khi chạy xong, một thư mục venv/ xuất hiện trong dự án, bên trong chứa trình thông dịch Python và pip riêng biệt cho dự án này.

> Lưu ý: Việc tạo thư mục venv/ chưa có nghĩa là chúng ta đang dùng nó. Bước tạo và bước kích hoạt là hai việc khác nhau — đây là lỗi nhầm lẫn rất thường gặp ở người mới.

## 4. Kích Hoạt Và Hủy Kích Hoạt Môi Trường

Sau khi tạo, chúng ta phải kích hoạt (activate) môi trường ảo để các lệnh python và pip trong terminal trỏ vào môi trường biệt lập đó thay vì Python hệ thống. Lệnh kích hoạt khác nhau giữa các hệ điều hành.

### Trên Windows

```bash
.\venv\Scripts\activate
```

### Trên macOS và Linux

```bash
source venv/bin/activate
```

Dấu hiệu nhận biết môi trường đã được kích hoạt thành công: phía trước dòng nhập lệnh của terminal xuất hiện tiền tố (venv). Khi thấy tiền tố này, chúng ta yên tâm rằng mọi thư viện cài tiếp theo đều nằm gọn trong môi trường ảo của dự án.

### Hủy kích hoạt khi xong việc

Khi muốn thoát khỏi môi trường ảo (ví dụ để chuyển sang dự án khác), chỉ cần gõ một lệnh chung cho mọi hệ điều hành:

```bash
deactivate
```

Sau lệnh này, tiền tố (venv) biến mất và terminal quay lại dùng Python hệ thống. Quy trình kích hoạt - làm việc - hủy kích hoạt này lặp lại mỗi khi chúng ta mở một phiên làm việc mới.

## 5. Quản Lý Thư Viện Bằng pip

pip là trình quản lý gói (package manager) của Python, dùng để cài đặt, gỡ bỏ và liệt kê các thư viện. Khi môi trường ảo đã được kích hoạt, mọi lệnh pip đều tác động vào riêng môi trường đó. Để dựng một dự án FastAPI, chúng ta cài hai thư viện nền tảng:

```bash
# Cài FastAPI (framework) và Uvicorn (máy chủ ASGI để chạy ứng dụng)
pip install fastapi uvicorn
```

Cần cài cả hai vì như đã học ở bài trước, FastAPI chỉ lo logic xử lý còn Uvicorn mới là phần đưa ứng dụng vào vận hành trên cổng mạng. Sau khi cài, chúng ta có thể kiểm tra danh sách thư viện hiện có bằng lệnh 'pip list'.

## 6. Tái Tạo Môi Trường Với requirements.txt

Một dự án thực tế hiếm khi do một người làm. Khi đồng đội nhận dự án của chúng ta, họ cần cài đúng những thư viện với đúng phiên bản mà chúng ta đang dùng — nếu không, lại quay về vấn đề xung đột phiên bản. Giải pháp chuẩn của cộng đồng Python là file requirements.txt: một danh sách liệt kê mọi thư viện và phiên bản của dự án.

### Bước 1: Đóng gói danh sách thư viện

Khi đã cài xong các thư viện cần thiết, chúng ta xuất danh sách ra file requirements.txt bằng lệnh:

```bash
# Ghi toàn bộ thư viện đang cài (kèm phiên bản) ra file requirements.txt
pip freeze > requirements.txt
```

Lệnh 'pip freeze' liệt kê mọi thư viện đang có trong môi trường kèm số phiên bản chính xác (ví dụ fastapi==0.111.0); dấu '>' chuyển kết quả đó vào file requirements.txt. File này nên được đẩy lên Git để cả nhóm chia sẻ.

### Bước 2: Đồng đội tái tạo môi trường

Khi một thành viên mới clone dự án về, họ chỉ cần tạo venv của riêng mình, kích hoạt nó, rồi cài toàn bộ thư viện từ file đã đóng gói:

```bash
# Cài lại đúng mọi thư viện và phiên bản đã ghi trong requirements.txt
pip install -r requirements.txt
```

Nhờ requirements.txt, môi trường của mọi người trong nhóm trở nên đồng bộ tuyệt đối — ai cũng có cùng bộ thư viện, cùng phiên bản. Đây là cách loại bỏ tận gốc câu nói kinh điển 'máy em chạy được mà máy anh lỗi'.

## 7. Loại Trừ venv Khỏi Git Với .gitignore

Một câu hỏi thường gặp: có nên đẩy thư mục venv/ lên Git không? Câu trả lời dứt khoát là KHÔNG. Thư mục venv/ thường rất nặng (hàng nghìn file), phụ thuộc vào hệ điều hành cụ thể, và hoàn toàn có thể tái tạo lại từ requirements.txt. Đẩy nó lên Git là dư thừa và gây rối kho mã.

Để Git tự động bỏ qua thư mục này, chúng ta tạo một file tên .gitignore ở thư mục gốc dự án và liệt kê venv/ trong đó:

```text
# .gitignore — các mục Git sẽ bỏ qua, không theo dõi
venv/
__pycache__/
*.pyc
.env
```

Như vậy chúng ta chia sẻ requirements.txt (nhẹ, đủ để tái tạo) và bỏ qua venv/ (nặng, máy nào tự dựng máy đó). Đây là quy ước chuẩn cho mọi dự án Python chuyên nghiệp.

## 8. Vận Dụng: Quy Trình Khởi Tạo Hoàn Chỉnh Một Dự Án

Ghép tất cả các bước lại, đây là quy trình mẫu hoàn chỉnh để khởi tạo môi trường cho dự án cổng điều phối Logistics trên Windows — chính là kịch bản chúng ta sẽ dùng lại ở các bài thực hành sau:

```bash
# Bước 1: Tạo môi trường ảo trong thư mục dự án
python -m venv venv

# Bước 2: Kích hoạt môi trường (Windows). Sau lệnh này terminal sẽ có tiền tố (venv)
.\venv\Scripts\activate

# Bước 3: Cài các thư viện nền tảng cho FastAPI
pip install fastapi uvicorn

# Bước 4: Đóng gói danh sách thư viện để cả nhóm tái tạo
pip freeze > requirements.txt
```

Sau bốn bước này, chúng ta đã có một môi trường Python biệt lập, sạch sẽ, đã cài FastAPI và Uvicorn, và sẵn sàng để bước sang bài tiếp theo: viết và chạy ứng dụng FastAPI đầu tiên. Sản phẩm đầu ra của bài học chính là một môi trường Python + FastAPI hoạt động đúng.

## Tổng Kết

Bài đọc đã trang bị cho chúng ta kỹ năng nền tảng đầu tiên của một lập trình viên backend chuyên nghiệp — quản lý môi trường dự án. Các điểm cốt lõi cần ghi nhớ:

- Cài thư viện trực tiếp vào Python hệ thống dễ gây xung đột phiên bản giữa các dự án; môi trường ảo giải quyết triệt để vấn đề này bằng cách cô lập thư viện cho từng dự án.
- Lệnh tạo: 'python -m venv venv'; thư mục venv/ chứa trình thông dịch và pip riêng. Tạo và kích hoạt là hai bước khác nhau.
- Kích hoạt trên Windows: '.\venv\Scripts\activate'; trên macOS/Linux: 'source venv/bin/activate'; dấu hiệu thành công là tiền tố (venv). Thoát bằng 'deactivate'.
- Đóng gói thư viện bằng 'pip freeze > requirements.txt'; đồng đội tái tạo môi trường bằng 'pip install -r requirements.txt'.
- Luôn thêm venv/ vào .gitignore — chia sẻ requirements.txt (nhẹ, tái tạo được) thay vì đẩy cả thư mục venv/ (nặng, phụ thuộc hệ điều hành).

## Tài Liệu Tham Khảo

- Python Official Documentation — venv: Creation of virtual environments: https://docs.python.org/3/library/venv.html
- Python Packaging User Guide — Installing packages using pip and virtual environments: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- pip Documentation — pip freeze và pip install: https://pip.pypa.io/en/stable/cli/
- FastAPI Official Documentation — Installation: https://fastapi.tiangolo.com/#installation
- Git Documentation — gitignore: https://git-scm.com/docs/gitignore

## Khái niệm liên quan

- [[Xung đột phiên bản (version conflict)]]
- [[Virtual Environment (venv)]]
- [[Kích hoạt-Hủy kích hoạt môi trường|Kích hoạt/Hủy kích hoạt môi trường]]
- [[pip]]
- [[requirements.txt]]
- [[gitignore|.gitignore]]

— Thuộc [[Session 02 — MOC]]
