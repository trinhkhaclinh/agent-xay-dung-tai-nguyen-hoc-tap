---
name: san-xuat-session
description: Sản xuất trọn bộ tài nguyên học tập (dạng .md trong Obsidian vault) cho một Session của khóa học PTIT × Rikkei — bài đọc, outline bài giảng, kịch bản video, bài tập, quiz, mindmap, kèm liên kết wikilink/MOC/concept. Dùng khi người dùng nói "sản xuất session N", "tạo tài nguyên cho session", "làm học liệu session", "/san-xuat-session N".
---

# Orchestrator: Sản xuất tài nguyên một Session (md-first → Obsidian vault)

Bạn là nhạc trưởng điều phối pipeline. **Đầu ra là file `.md`** trong vault Obsidian `vault/`, liên kết
logic xuyên chương trình (wikilinks + MOC + concept notes). Việc chuyển `.md` → thành phẩm
(.docx/.pptx/.xlsx/.xmind) là **stage-2 (đợt sau)** — KHÔNG làm ở đây.

Tuân thủ NGHIÊM NGẶT hợp đồng trong `knowledge/format-specs/` (đặc biệt `07-obsidian-vault.md`) và
nguyên tắc sư phạm trong `knowledge/pedagogy/`.

## Tham số
`/san-xuat-session <số>` — ví dụ `/san-xuat-session 4`. Nếu thiếu, hỏi số session.

## Đọc bối cảnh trước khi làm (BẮT BUỘC)
1. `knowledge/framework.json` — lấy session theo `session_no`.
2. `knowledge/format-specs/00-...` (block model + SSOT), `01`–`06` (nội dung từng artifact), `07-obsidian-vault.md` (vault/frontmatter/wikilink/MOC).
3. `knowledge/style-guide.md` + `knowledge/pedagogy/principles.md` + `bloom-verbs-vi.md`.

Nếu `hinh_thuc_hoc` ≠ "Lý thuyết", báo người dùng pipeline tối ưu cho session Lý thuyết và hỏi có tiếp tục không.

## Quy trình

### Bước 1 — Dựng SSOT
Tạo `output/<folder_name>/_spec/session_content_spec.json` theo schema `00-...md` (backwards design:
objectives Bloom, key_concepts, scenario thực tế, facts, code_examples chạy được, prior_session).
`folder_name` = `Session NN - <title>` (giữ dấu `&`). Đây là NGUỒN SỰ THẬT — mọi note dẫn xuất từ đây.

**Cổng SSOT — BẮT BUỘC trước khi fan-out (shift-left).** Lỗi ở SSOT lan ra cả 6 nhóm artifact và tốn
6× công sửa, nên chặn ngay tại đây:
```
PYTHONIOENCODING=utf-8 python tools/qa_spec.py "output/<folder_name>/_spec/session_content_spec.json"
PYTHONIOENCODING=utf-8 python tools/verify_code.py "output/<folder_name>/_spec/session_content_spec.json" --run
```
`qa_spec.py`: đủ khóa, mỗi objective có nhãn Bloom, cả session ≥3 bậc Bloom, prior_session có review_topics,
cú pháp code_examples. `verify_code.py --run`: chạy thử thật mọi app FastAPI trong code_examples.
**Chỉ sang Bước 2 khi cả hai exit 0** (sửa SSOT tới khi hết BLOCKER; cân nhắc cả cảnh báo NÊN SỬA).

### Bước 2 — Sinh JSON cho từng artifact (fan-out)
Ghi JSON vào `output/<folder_name>/_spec/` (đây là workspace build; vault sẽ chỉ chứa .md). Dùng các skill
playbook (đọc SKILL của chúng) — có thể giao mỗi nhóm cho 1 subagent (Task tool), mỗi subagent đọc SSOT +
format-spec + style-guide rồi GHI JSON:
- `soan-bai-doc` → `reading_<NN>.json` (1/Lesson) · `soan-outline-bai-giang` → `slide_outline.json`
- `viet-kich-ban-video` → `video_<NN>.json` (1/Lesson) · `thiet-ke-bai-tap` → `exercise_<NN>.json` (≥6)
- `tao-quiz` → `quiz_daugio.json` + `quiz_cuoigio.json` · `tao-mindmap` → `mindmap.json`

**Nhất quán (chống drift khi chạy song song):** các subagent độc lập dễ bịa ví dụ/tên file khác nhau cho
cùng một Lesson. Quy tắc cứng: **code, tên file (`main.py`/`gateway.py`…), `scenario` và số liệu dùng chung
phải TRÍCH LẠI nguyên văn từ SSOT** (`code_examples`/`scenario`/`facts`), không tự sáng tác ví dụ mới. SSOT
là hợp đồng — artifact chỉ diễn giải, không phát minh dữ kiện mới.

### Bước 3 — Render ra vault (.md)
```
PYTHONIOENCODING=utf-8 python tools/render_vault.py "output/<folder_name>" vault
PYTHONIOENCODING=utf-8 python tools/build_moc.py vault
```
`render_vault.py`: JSON → note `.md` có frontmatter + wikilinks trong `vault/Sessions/<folder_name>/`,
tự tạo/cập nhật concept notes (`vault/Khái niệm/`) và Session MOC. `build_moc.py`: cập nhật Module MOC.

### Bước 4 — QA (2 lớp)

**Lớp A — QA tự động (cổng cứng, BẮT BUỘC PASS).** Chạy 2 tool; cả hai phải exit 0:
```
PYTHONIOENCODING=utf-8 python tools/verify_code.py "output/<folder_name>/_spec" --run
PYTHONIOENCODING=utf-8 python tools/qa_vault.py vault
```
- `verify_code.py --run`: cú pháp Python + chạy thử app FastAPI (file `exercise_`/`quiz_` chỉ kiểm cú pháp vì
  cố tình chứa code lỗi để học viên sửa).
- `qa_vault.py`: frontmatter, wikilink không gãy, Session MOC + concept note đủ.

**Lớp B — Review bàn giao (BẮT BUỘC trước khi báo cáo).** Giao subagent `chuyen-gia-noi-dung-fastapi`
review `output/<folder_name>` để bắt phần mà tool tự động KHÔNG thấy: nhất quán bài đọc↔slide↔video↔mindmap,
độ phủ backwards design (mỗi objective có được DẠY và KIỂM), chất lượng distractor quiz, đúng tầng Bloom,
giọng văn. Mọi mục `BLOCKER` của agent phải xử lý.

**Vòng lặp sửa:** với mọi FAIL (Lớp A) hoặc BLOCKER (Lớp B) → **sửa JSON trong `_spec/`** (không sửa thẳng
`.md` vì sẽ bị render ghi đè) → render lại (Bước 3) → chạy lại Lớp A. Lặp tới khi sạch.

### Bước 5 — Báo cáo
Liệt kê note đã tạo theo nhóm + Session MOC + concept notes mới; kết quả QA; nhắc người dùng mở `vault/`
bằng Obsidian (Graph view) để xem mạng liên kết; ghi chú stage-2 (md→thành phẩm) sẽ làm sau.

## Nguyên tắc chất lượng
- KHÔNG render binary ở đợt này — chỉ sinh JSON đúng schema rồi `render_vault.py` dựng `.md`.
- **3 cổng chặn**: SSOT (`qa_spec` + `verify_code`, sau Bước 1) → tự động (`verify_code` + `qa_vault`,
  Bước 4 Lớp A) → review người-máy (`chuyen-gia-noi-dung-fastapi`, Bước 4 Lớp B). Không bỏ qua cổng nào.
- Ví dụ/code thực tế, chạy được (đã được `verify_code --run` kiểm), nhất quán xuyên suốt (style-guide mục 3 & 5).
- Mỗi key_concept nên thành 1 concept note liên kết (tự động qua render_vault) → xây mạng tri thức toàn chương trình.
- Tiếng Việt có dấu; Windows luôn đặt `PYTHONIOENCODING=utf-8` khi chạy script.
