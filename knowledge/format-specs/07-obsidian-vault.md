# Hợp đồng — Obsidian Vault (md-first)

Đợt 2: mọi đầu ra là `.md` trong vault Obsidian `vault/`, liên kết logic xuyên chương trình.
Renderer: `tools/render_vault.py` (JSON `_spec/*.json` → note `.md`), `tools/concept_linker.py`,
`tools/build_moc.py`. Helper Markdown: `tools/lib/md_helpers.py` (map từ Block Model).

## A. Cấu trúc thư mục
```
vault/
├── 00 - Bản đồ chương trình/  IT-215 FastAPI — MOC.md
├── Sessions/<Session NN - Tên>/
│   ├── Session NN — MOC.md
│   ├── Bài đọc/        S<NN> - L<k> - <tên>.md
│   ├── Kịch bản video/ S<NN> - Lesson <k> - <tên>.md
│   ├── Bài tập/        S<NN> - [<Cấp độ>] <tên>.md
│   ├── Quiz/           S<NN> - Quiz Đầu giờ.md, S<NN> - Quiz Cuối giờ.md
│   ├── Bài giảng (outline)/  S<NN> - Bài giảng (Outline).md
│   ├── Mindmap/        S<NN> - Mindmap.md
│   └── _spec/          *.json  (input build nội bộ; KHÔNG phải deliverable)
├── Khái niệm/          <Tên khái niệm>.md     (atomic, tên DUY NHẤT toàn vault)
└── _templates/         *.md
```

**Quy tắc đặt tên (QUAN TRỌNG):** basename note phải **duy nhất toàn vault** để `[[wikilink]]` phân giải đúng.
- Artifact: tiền tố `S<NN> - ...` (vd `S02 - L1 - Tổng quan kiến trúc web và FastAPI`).
- Concept note: đúng tên khái niệm, duy nhất (vd `ASGI vs WSGI`). Đây là chất keo liên kết.
- Session MOC: `Session NN — MOC`. Module MOC: `IT-215 FastAPI — MOC`.

## B. Frontmatter YAML (mọi note)
Khóa chung: `type`, `title`, `tags` (mảng), `status` (draft|review|done).
Theo loại (`type`):
| type | khóa thêm |
|------|-----------|
| `bai-doc` | `session`, `lesson`, `concepts` ([[..]]), `deliverable_filename` |
| `kich-ban-video` | `session`, `lesson`, `concepts`, `deliverable_filename` |
| `bai-tap` | `session`, `level`, `bloom`, `concepts`, `ex_code`, `deliverable_filename` |
| `quiz` | `session`, `quiz_type` (daugio|cuoigio), `sheet_name`, `deliverable_filename` |
| `bai-giang-outline` | `session`, `slide_count`, `deliverable_filename` |
| `mindmap` | `session`, `deliverable_filename` |
| `session-moc` | `session`, `hinh_thuc_hoc`, `lessons` |
| `module-moc` | `module` |
| `khai-niem` | `aliases`, `introduced_in`, `related` ([[..]]) |

`deliverable_filename` = tên file gốc theo mẫu gold-standard (để stage-2 tái tạo .docx/.xlsx đúng tên).
Ví dụ frontmatter bài đọc:
```yaml
---
type: bai-doc
title: "Tổng quan kiến trúc web và FastAPI"
session: 2
lesson: 1
tags: [type/bai-doc, session/02]
concepts: ["[[Client-Server]]", "[[JSON]]", "[[ASGI vs WSGI]]"]
deliverable_filename: "BÀI ĐỌC_ TỔNG QUAN KIẾN TRÚC WEB VÀ FASTAPI_"
status: done
---
```

## C. Thân note — map từ Block Model sang Markdown (`md_helpers.py`)
| block | Markdown |
|-------|----------|
| h1 | `# text` |
| h2 | `## text` |
| h3 | `### text` |
| p / narration | đoạn văn |
| bullets | `- item` |
| numbers | `1. item` |
| code | ```` ```lang \n text \n ``` ```` |
| marker (video) | `**[text]**` trên dòng riêng |
| table | bảng Markdown (header + `---`) |
| quote | `> text` |

- Video: heading nội dung đã là `## ...` (giữ nguyên).
- Quiz: KHÔNG dùng block; render thành **bảng Markdown 12 cột** đúng thứ tự lược đồ (xem `04-quiz.md`)
  để stage-2 ánh xạ thẳng sang .xlsx. Có thêm dòng frontmatter `sheet_name`.
- Mindmap: render thành **danh sách lồng nhau** (`- ` thụt 2 space mỗi cấp) từ cây `root/children`.

## D. Wikilink & liên kết logic
- Artifact: trong thân, lần đầu nhắc một khái niệm cốt lõi → bọc `[[Tên khái niệm]]`; đồng thời liệt kê ở
  frontmatter `concepts`. (render_vault tự chèn mục "## Khái niệm liên quan" liệt kê các `[[..]]`.)
- **Concept note** (`Khái niệm/`): atomic, 1 khái niệm. Có mục `## Xuất hiện ở` liệt kê `[[Session NN — MOC]]`
  kèm vai trò (giới thiệu/vận dụng). `concept_linker.py` cập nhật idempotent khi session mới dùng lại khái niệm
  ⇒ graph Obsidian hiện mạng tri thức + thứ tự tiên quyết toàn chương trình.
- **Session MOC**: hub — liệt kê & link MỌI note của session theo nhóm, kèm mục tiêu (objectives/Lesson) và
  danh sách `[[khái niệm]]`. Link `[[IT-215 FastAPI — MOC]]` (lên module).
- **Module MOC**: bảng 30 session (từ `framework.json`), mỗi session link `[[Session NN — MOC]]` (stub nếu chưa sinh).

## E. Checklist QA vault (`qa_vault.py`)
- [ ] Mọi `.md` (trừ _templates) có frontmatter hợp lệ + khóa bắt buộc theo `type`.
- [ ] Mọi `[[wikilink]]` trỏ tới note tồn tại (hoặc stub MOC có chủ đích) — báo link gãy.
- [ ] Mỗi `key_concepts` của SSOT có 1 concept note trong `Khái niệm/`.
- [ ] Session MOC tồn tại và link đủ các nhóm artifact đã render.
- [ ] Không còn placeholder ngoài ý muốn (giữ ngoại lệ `# TODO:` trong code bài tập).
