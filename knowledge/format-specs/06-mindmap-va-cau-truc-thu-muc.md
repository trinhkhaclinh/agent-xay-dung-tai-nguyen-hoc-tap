# Hợp đồng định dạng — Mindmap (.xmind) & Cấu trúc thư mục đầu ra

## A. Mindmap — `Mindmap/*.xmind`
Renderer: `tools/render_mindmap.py`  ·  Input JSON: `mindmap.json`.

Định dạng **XMind Zen** = file zip chứa:
- `content.json` — cây nội dung (bắt buộc).
- `metadata.json` — `{}` tối thiểu hợp lệ.
- `manifest.json` — `{ "file-entries": { "content.json": {}, "metadata.json": {} } }`.

Cấu trúc cây (theo mẫu Session 02):
- **Root** = tên session ("Giới thiệu và Cài đặt FastAPI").
- **Cấp 1** = các Lesson, đánh số ("1. Tổng quan kiến trúc web và FastAPI", "2. Virtual environment", ...).
- **Cấp 2-3** = khái niệm con, lấy từ `key_concepts` + `facts` của từng Lesson trong SSOT.

Schema `mindmap.json`:
```jsonc
{
  "filename": "Session 02 - Giới thiệu và Cài đặt FastAPI",
  "subdir": "Mindmap",
  "root": "Giới thiệu và Cài đặt FastAPI",
  "children": [
    { "title": "1. Tổng quan kiến trúc web và FastAPI",
      "children": [
        { "title": "Mô hình client - server & JSON",
          "children": [ { "title": "Client <-> Internet (HTTP) <-> Server" } ] },
        { "title": "WSGI vs ASGI", "children": [ { "title": "Uvicorn: ASGI server siêu nhanh" } ] }
      ] }
  ]
}
```
content.json sinh ra có dạng `[{ "id","class":"sheet","title":"Mind Map","rootTopic": {"id","title","children":{"attached":[...]}} }]`,
mỗi topic con: `{ "id","title","children": {"attached": [...]} }` (bỏ `children` nếu là lá).
`id` sinh xác định (hash từ đường dẫn tiêu đề) để tái lập được, KHÔNG random.

Checklist QA: file mở được bằng `zipfile`; có `content.json`; root khớp tên session; ≥1 nhánh/Lesson.

---

## B. Cấu trúc thư mục đầu ra (giống hệt bộ mẫu)
```
output/<Session NN - Tên>/
├── Bài giảng/                      <Tên>.md  (+ .docx)         [outline]
├── Bài đọc/                        BÀI ĐỌC_ ....docx           [1/chủ đề]
├── Bài tập/                        [Cấp độ] ....docx           [≥6 bài]
├── Câu hỏi Quiziz session/         Import_Quiz_DauGio_*.xlsx
│                                   Import_Quiz_CuoiGio_*.xlsx
├── Kịch bản quay video/            Lesson NN - ....docx        [1/Lesson]
├── Mindmap/                        <Tên>.xmind
└── _spec/                          *.json (SSOT + input renderer; tiện kiểm tra/tái tạo)
```
- Tên thư mục session: lấy từ khung CT, dấu `&` giữ nguyên (mẫu: "Session 02 - Giới thiệu & Cài đặt FastAPI").
- Thư mục con đặt **đúng tên có dấu** như mẫu (kể cả "Quiziz" viết theo mẫu gốc).
