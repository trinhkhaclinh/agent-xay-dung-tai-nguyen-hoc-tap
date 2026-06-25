# Hợp đồng định dạng — Tổng quan & Block Model dùng chung

Tài liệu này định nghĩa **các hợp đồng JSON** giữa lớp sinh nội dung (skill/LLM) và lớp render
(`tools/render_*.py`). Quy tắc vàng: **LLM sinh JSON, Python render ra file**. Skill KHÔNG tự ghi
`.docx/.xlsx/.xmind`; chỉ tạo JSON đúng schema rồi gọi renderer.

Tất cả file JSON trung gian của một session đặt tại:
`output/<Tên thư mục session>/_spec/`
File đầu ra (artifact) đặt theo đúng cây thư mục con của bộ mẫu (xem `06-cau-truc-thu-muc.md`).

---

## Block Model dùng chung (cho mọi artifact .docx)

Mọi tài liệu Word (bài đọc, kịch bản video, bài tập) được mô tả bằng một **mảng `blocks`**.
Renderer duyệt tuần tự và dựng đoạn văn theo `type`:

| `type`     | Trường           | Render thành |
|------------|------------------|--------------|
| `h1`       | `text`           | Heading 1 |
| `h2`       | `text`           | Heading 2 |
| `h3`       | `text`           | Heading 3 |
| `p`        | `text`           | Đoạn văn thường (style `Normal`) |
| `bullets`  | `items: []`      | Danh sách chấm (`List Bullet`) |
| `numbers`  | `items: []`      | Danh sách số (`List Number`) |
| `code`     | `text`, `lang?`  | Khối code mono (font Consolas, nền xám nhạt) |
| `marker`   | `text`           | Dòng **in đậm** dạng `**[...]**` (chỉ dùng cho kịch bản video) |
| `table`    | `headers: []`, `rows: [[...]]` | Bảng có header in đậm |
| `quote`    | `text`           | Đoạn ghi chú/lưu ý (in nghiêng) |

Ví dụ một block:
```json
{ "type": "code", "lang": "python", "text": "from fastapi import FastAPI\napp = FastAPI()" }
```

Quy ước chung:
- Văn bản tiếng Việt có dấu, UTF-8. Không markdown bên trong `text` (trừ `marker`).
- Code giữ nguyên thụt lề bằng khoảng trắng; xuống dòng bằng `\n`.
- Mỗi artifact có thêm trường `filename` (tên file đầu ra, không kèm đuôi) và `subdir` (thư mục con).

---

## `session_content_spec.json` — Nguồn sự thật duy nhất (SSOT)

Sinh **đầu tiên** trong pipeline (bước backwards design). Mọi artifact dẫn xuất từ đây để đảm bảo
nội dung đồng nhất (bài đọc ↔ slide ↔ video ↔ mindmap dùng chung khái niệm, ví dụ, số liệu).

```jsonc
{
  "session_no": 2,
  "session_id": "Session 02",
  "title": "Giới thiệu & Cài đặt FastAPI cơ bản",
  "module": "[MODULE IT-215] - Phát triển dịch vụ web với FastAPI",
  "hinh_thuc_hoc": "Lý thuyết",
  "summary": "Mô tả 2-3 câu tổng quan session.",
  "lessons": [
    {
      "no": 1,
      "title": "Tổng quan kiến trúc web và FastAPI",
      "objectives": [                 // mục tiêu học tập, gắn động từ Bloom
        "Giải thích (Hiểu) mô hình Client-Server và vòng đời Request-Response",
        "Vẽ (Vận dụng) sơ đồ Client → API → Database"
      ],
      "key_concepts": ["Client-Server", "HTTP/HTTPS", "JSON", "ASGI vs WSGI"],
      "scenario": "Kịch bản nghiệp vụ thực tế dùng xuyên suốt lesson (vd: cổng giám sát Logistics).",
      "facts": [                       // định nghĩa/sự thật cốt lõi, tái dùng cho quiz & mindmap
        "Uvicorn là ASGI server; FastAPI không tự lắng nghe cổng mạng.",
        "Endpoint RESTful đặt tên bằng danh từ số nhiều, hành động do HTTP method quyết định."
      ],
      "code_examples": [
        { "caption": "Ứng dụng FastAPI tối thiểu", "lang": "python",
          "code": "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef root():\n    return {'message': 'Hello'}" }
      ],
      "san_pham_dau_ra": "Vẽ được sơ đồ Client → API → Database"   // copy từ khung CT
    }
  ],
  "prior_session": {                   // phục vụ quiz Đầu giờ phần "BÀI CŨ" (retrieval practice)
    "no": 1,
    "title": "...",
    "review_topics": ["Cú pháp Python cơ bản", "Kiểu dữ liệu", "Hàm"]
  }
}
```

Lưu ý: `objectives` dùng động từ Bloom (Nhớ/Hiểu/Vận dụng/Phân tích/Đánh giá/Sáng tạo) —
chúng định hình tầng bài tập và độ khó quiz. Xem `knowledge/pedagogy/`.
