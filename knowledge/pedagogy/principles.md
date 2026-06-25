# Lớp tri thức sư phạm — Nguyên tắc & cách áp dụng vào artifact

Tinh chắt từ `github.com/GarethManning/education-agent-skills` (các domain dẫn bên dưới) cùng các nguồn
nghiên cứu nền tảng. Mục đích: định hướng **chất lượng sư phạm** cho mọi tài nguyên agent sinh ra.

> Tham chiếu domain trong repo: `curriculum-assessment`, `curriculum-alignment`, `memory-learning-science`,
> `explicit-instruction`, `questioning-discussion`, `self-regulated-learning`, `ai-learning-science`.

## 1. Backwards Design (Thiết kế ngược) → bước lập SSOT
*Nguồn: Wiggins & McTighe, "Understanding by Design"; repo domain `curriculum-assessment`/`curriculum-alignment`.*
Quy trình 3 bước, áp cho mỗi Lesson khi dựng `session_content_spec`:
1. **Xác định kết quả mong muốn** → viết `objectives` (gắn động từ Bloom) bám cột "Sản phẩm đầu ra" của khung CT.
2. **Xác định bằng chứng** → quiz Cuối giờ + bài tập chính là bằng chứng đạt mục tiêu.
3. **Lập kế hoạch dạy** → bài đọc/slide/video truyền tải để đạt mục tiêu.
⇒ Mọi artifact phải "truy vết" được về một `objective`. Không có nội dung thừa, không thiếu bằng chứng.

## 2. Thang Bloom → phân tầng bài tập & độ khó quiz
*Nguồn: Anderson & Krathwohl (2001), bản sửa đổi Bloom. Xem bảng động từ: `bloom-verbs-vi.md`.*
- Bài tập phủ thang từ thấp → cao: **Vận dụng cơ bản** (Apply: sửa lỗi) → **Phân tích** (Analyze: so sánh
  thiết kế) → **Vận dụng chuyên sâu** → **Sáng tạo** (Create). Đây chính là bộ cấp độ trong mẫu Session 02.
- Quiz: `difficulty` thấp (4) cho câu Nhớ/Hiểu; cao (8) cho câu Vận dụng/Phân tích.
- `objectives` trong SSOT phải dùng đúng động từ Bloom để tự suy ra tầng bài tập tương ứng.

## 3. Retrieval Practice + Spacing + Interleaving → thiết kế quiz Đầu giờ
*Nguồn: Roediger & Karpicke (2006); repo domain `memory-learning-science`.*
- **Retrieval practice**: kiểm tra để củng cố trí nhớ (không chỉ ôn đọc lại) ⇒ vai trò của 2 bộ quiz.
- **Spacing**: ôn lại sau khoảng cách ⇒ quiz Đầu giờ phần `BÀI CŨ` kiểm tra session/kiến thức trước.
- **Interleaving**: trộn chủ đề ⇒ Đầu giờ trộn `BÀI CŨ` + `BÀI MỚI`. Đây là lý do file Đầu giờ có 2 category.
- Mỗi đáp án có giải thích ⇒ **feedback tức thì**, biến quiz thành công cụ học chứ không chỉ đo lường.

## 4. Explicit / Direct Instruction + Worked Examples → cấu trúc bài đọc & slide
*Nguồn: Rosenshine "Principles of Instruction"; Sweller "Worked Example Effect"; repo domain `explicit-instruction`.*
- Trình tự: **khái niệm → ví dụ mẫu chi tiết (worked example) → vận dụng**. Bài đọc Session 02 theo đúng mạch
  này (giải thích → code `gateway.py` từng bước → mở rộng `--reload`).
- Chia nhỏ thành bước rõ ràng (mẫu dùng "Quy trình ba bước thiết lập code").
- Giảm tải nhận thức: mỗi slide một ý; code kèm comment đánh số bước.

## 5. Rubrics + Distractor Design → tiêu chí chấm & chất lượng quiz
*Nguồn: repo domain `curriculum-assessment`, `questioning-discussion`.*
- Bài tập nên nêu rõ tiêu chí đạt (bảng so sánh, "Yêu cầu đầu ra" cụ thể) ⇒ minh bạch như rubric.
- **Distractor (đáp án nhiễu) chất lượng**: phản ánh hiểu lầm phổ biến (vd nhầm cú pháp ngôn ngữ khác),
  không phi lý lộ liễu. Mỗi distractor có giải thích đúng vì sao sai → sửa quan niệm sai.

## 6. Bản đồ Nguyên tắc → Artifact (tóm tắt)
| Nguyên tắc            | Artifact áp dụng |
|-----------------------|------------------|
| Backwards design      | session_content_spec (objectives) |
| Bloom                 | bài tập (tầng), quiz (difficulty) |
| Retrieval/Spacing/Interleaving | quiz Đầu giờ & Cuối giờ |
| Worked examples / Explicit instruction | bài đọc, slide outline |
| Rubrics / Distractors | bài tập (yêu cầu), quiz (giải thích) |
| Dual coding (lời + hình) | mindmap + diagram_hint trên slide |
