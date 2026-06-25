# Hợp đồng định dạng — Quiz Quizizz (Câu hỏi Quiziz session/*.xlsx)

Mục tiêu: ngân hàng câu hỏi trắc nghiệm import thẳng vào Quizizz. Mỗi session có **2 file**:
- **Đầu giờ** (`Import_Quiz_DauGio_*.xlsx`): ôn bài cũ + xem trước bài mới (retrieval practice + interleaving).
- **Cuối giờ** (`Import_Quiz_CuoiGio_*.xlsx`): củng cố nội dung session vừa học.

Renderer: `tools/render_quiz.py`  ·  Input JSON: `quiz_daugio.json`, `quiz_cuoigio.json`.

## Lược đồ cột (CHÍNH XÁC, đúng thứ tự — hàng 1 là header)
```
question_content | answer_1 | explanation_answer_1 | answer_2 | explanation_answer_2 |
answer_3 | explanation_answer_3 | answer_4 | explanation_answer_4 | isCorrect | difficulty | category
```
- 4 đáp án, **mỗi đáp án có 1 ô giải thích** (vì sao đúng/sai).
- `isCorrect`: số nguyên **1–4** = vị trí đáp án đúng.
- `difficulty`: số. Quy ước theo mẫu: **4 = mức cơ bản (bài cũ), 8 = mức cao hơn (bài mới)**.
- `category`: chuỗi. Đầu giờ dùng `BÀI CŨ` / `BÀI MỚI`. Cuối giờ: theo Lesson/chủ đề hoặc `BÀI MỚI`.
- Tên sheet đặt theo chủ đề: vd `Quiz_DauGio_OOP`, `Quiz_CuoiGio_FastAPI`.

## Phân bổ nội dung
- **Đầu giờ**: ~60% `BÀI CŨ` (kiến thức nền/ session trước — lấy `prior_session.review_topics` từ SSOT)
  + ~40% `BÀI MỚI` (xem trước khái niệm session này). Mẫu Session 02: ~30+ câu BÀI CŨ (Python/OOP) + ~15 BÀI MỚI.
- **Cuối giờ**: 100% nội dung session vừa học, phủ đều các Lesson, gồm câu khái niệm + câu áp dụng.
- Distractor (đáp án sai) phải **hợp lý, hay gặp** (vd nhầm cú pháp ngôn ngữ khác); giải thích ngắn gọn vì sao sai.

## Schema `quiz_*.json`
```jsonc
{
  "sheet_name": "Quiz_DauGio_OOP",
  "questions": [
    {
      "q": "Từ khóa nào dùng để khai báo hàm trong Python?",
      "answers": ["define", "func", "function", "def"],
      "explanations": [
        "Không phải từ khóa hợp lệ trong Python.",
        "Là từ khóa của Swift/Go.",
        "Là từ khóa của JavaScript/Go.",
        "'def' được Python dùng để định nghĩa hàm."
      ],
      "correct": 4,
      "difficulty": 4,
      "category": "BÀI CŨ"
    }
  ]
}
```

## Checklist QA
- [ ] Header đúng 12 cột, đúng thứ tự, đúng tên.
- [ ] Mọi câu: 4 đáp án + 4 giải thích, không rỗng.
- [ ] `isCorrect` ∈ {1,2,3,4}; `difficulty` là số; `category` không rỗng.
- [ ] File Đầu giờ có cả `BÀI CŨ` và `BÀI MỚI`.
- [ ] Số câu hợp lý (Đầu giờ ≥ 20, Cuối giờ ≥ 15) — điều chỉnh theo nhu cầu.
