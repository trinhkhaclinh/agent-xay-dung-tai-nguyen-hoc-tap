---
name: viet-kich-ban-video
description: Viết Kịch bản quay video (video_*.json) cho từng Lesson, giọng giảng viên "thầy/các em", có marker chuyển slide và thao tác demo. Dùng khi cần kịch bản quay/lồng tiếng bài giảng E-learning, hoặc khi orchestrator yêu cầu sinh kịch bản video.
---

# Viết Kịch bản video → video_<NN>.json (mỗi Lesson 1 file)

Đầu vào: `session_content_spec.json`. Đầu ra: `_spec/video_<NN>.json` cho từng Lesson.

## Đọc trước
- `_spec/session_content_spec.json`.
- `knowledge/format-specs/02-kich-ban-video.md` (cấu trúc + marker + schema + checklist).
- `knowledge/style-guide.md` mục 2 (giọng "thầy/các em", câu mở/chốt chuẩn Rikkei).

## Cách làm
Mỗi Lesson → 1 kịch bản, bám đúng các phần (sẽ thành các slide tương ứng).
Dựng `blocks`:
- `h2` mở đầu dạng `"## <Tên phần>"` (giữ tiền tố `## `).
- `narration` mở đầu: câu chào "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education...".
- Các `narration` giảng giải mạch lạc; mô tả sơ đồ/giao diện trên màn hình bằng lời.
- `marker` cho hành động: `[Chuyển tiếp slide]`, `[mở trình duyệt]`, `[mở công cụ Postman]`, `[nhấn nút Send...]`.
- Kết bằng `h2 "## Tổng kết bài giảng"` + `narration` chốt "Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại...".

- Nội dung khớp 100% với bài đọc/slide của cùng Lesson (cùng khái niệm, cùng ví dụ). Code/tên file nhắc đến
  phải **trích từ `code_examples` của SSOT** — không tự chế ví dụ khác.
- Nếu Lesson có thực hành: thêm ≥1 phân đoạn demo (marker mở công cụ + mô tả thao tác từng bước).

## Đặt tên file
`filename`: `"Lesson NN - <Tên Lesson>"` (theo mẫu). `subdir`: `"Kịch bản quay video"`. Đặt `lesson_no`.

## Tự kiểm
Theo checklist `02-kich-ban-video.md`: có câu chào Rikkei; ≥2 `## `; có "Tổng kết bài giảng" + "Cảm ơn các em";
≥1 `[Chuyển tiếp slide]`.
