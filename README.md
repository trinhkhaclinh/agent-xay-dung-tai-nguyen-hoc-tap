# Agent sản xuất tài nguyên học tập (PTIT × Rikkei) — md-first + Obsidian

"Nhà máy" AI sinh học liệu cho từng Session của khóa học tại
`daotaohoptacrikkeisoft.ptit.edu.vn`, bắt đầu với môn **IT-215 — Phát triển dịch vụ web với FastAPI**.

**Đầu ra là file `.md`** tổ chức thành một **Obsidian vault** (`vault/`) liên kết logic xuyên toàn chương
trình (wikilinks + MOC + concept notes). Việc chuyển `.md` → thành phẩm (.docx/.pptx/.xlsx/.xmind) là
**stage-2** (đợt sau).

Mỗi session Lý thuyết sinh: **Bài đọc · Outline bài giảng · Kịch bản video · Bài tập (phân tầng Bloom) ·
Quiz (Đầu/Cuối giờ) · Mindmap**, cộng **Session MOC** (hub liên kết) và các **concept note** (atomic).

## Kiến trúc (2 lớp + 2 giai đoạn)
- **LLM sinh nội dung (JSON) → Python render `.md`** (stage-1). JSON là input build tạm trong `output/<session>/_spec/`;
  vault chỉ chứa `.md`.
- **Một nguồn sự thật (SSOT)** `session_content_spec.json` → mọi note dẫn xuất ⇒ nội dung nhất quán.
- **Liên kết logic**: mỗi `key_concept` → 1 concept note trong `vault/Khái niệm/`; artifact ↔ concept ↔ MOC
  nối bằng `[[wikilink]]` ⇒ Obsidian Graph hiện mạng tri thức + thứ tự tiên quyết toàn chương trình.
- **Nền sư phạm**: backwards design, Bloom, retrieval practice, worked examples (`knowledge/pedagogy/`).
- **Stage-2 (đợt sau)**: agent đọc `.md` → .docx/.pptx/.xlsx/.xmind (tái dùng `tools/render_*.py`, đổi input sang parse Markdown).

```
.claude/skills/      8 skill: orchestrator san-xuat-session + 7 playbook (sinh JSON)
.claude/agents/      subagent review nội dung kỹ thuật & sư phạm
knowledge/
  framework.json     khung chương trình đã parse (26 session)
  format-specs/      00–06 hợp đồng JSON + 07-obsidian-vault.md (vault/frontmatter/wikilink/MOC)
  pedagogy/ · style-guide.md
tools/
  extract_framework.py            xlsx -> framework.json
  render_vault.py                 JSON _spec -> note .md + Session MOC + concept notes  [stage-1]
  concept_linker.py · build_moc.py  concept notes (atomic) · Module MOC
  qa_vault.py                     QA vault (frontmatter, wikilink gãy, concept đủ, MOC đủ)
  render_*.py + render_all.py + qa_check.py   [stage-2: JSON -> .docx/.xlsx/.xmind — giữ để dùng sau]
  lib/  md_helpers.py · docx_helpers.py · io_utils.py
vault/               OBSIDIAN VAULT (đầu ra .md)
  00 - Bản đồ chương trình/ IT-215 FastAPI — MOC.md
  Sessions/<Session NN ...>/ {Session NN — MOC, Bài đọc, Kịch bản video, Bài tập, Quiz, Bài giảng (outline), Mindmap}
  Khái niệm/         concept notes atomic (chất keo liên kết)
  _templates/
output/<session>/_spec/   workspace build (JSON, SSOT) — không phải deliverable
```

## Cách dùng

Cài phụ thuộc (một lần):
```
pip install -r requirements.txt
```

Parse lại khung chương trình khi .xlsx đổi:
```
PYTHONIOENCODING=utf-8 python tools/extract_framework.py
```

Sản xuất một session (trong phiên Claude Code):
```
/san-xuat-session 4
```
Orchestrator: dựng SSOT + JSON vào `output/<session>/_spec/` → `render_vault.py` (→ vault .md) →
`build_moc.py` → `qa_vault.py` → báo cáo.

Render / QA vault thủ công:
```
PYTHONIOENCODING=utf-8 python tools/render_vault.py "output/Session 02 - Giới thiệu & Cài đặt FastAPI" vault
PYTHONIOENCODING=utf-8 python tools/build_moc.py vault
PYTHONIOENCODING=utf-8 python tools/qa_vault.py vault
```

## Obsidian
- Mở `vault/` bằng Obsidian ("Open folder as vault") để xem Graph view + backlinks.
- Tích hợp **MCP filesystem `obsidian-mcp`** đã cấu hình ở `.mcp.json` (kích hoạt khi khởi động lại Claude Code).
  Chi tiết: [docs/obsidian-mcp.md](docs/obsidian-mcp.md).

## Lưu ý
- Pipeline đầy đủ hiện tối ưu cho session **Lý thuyết**. Session Thực hành/Mini Project/Hackathon: đợt sau.
- Windows: luôn đặt `PYTHONIOENCODING=utf-8` khi chạy script (tránh lỗi encoding tiếng Việt).
"# agent-xay-dung-tai-nguyen-hoc-tap" 
