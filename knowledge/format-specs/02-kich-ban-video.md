# Hợp đồng định dạng — Kịch bản quay video (Kịch bản quay video/*.docx)

Mục tiêu: kịch bản lời giảng để quay video E-learning, **mỗi Lesson 1 file**. Giọng giảng viên,
khớp với các phần (section) của slide, có marker hành động cho người quay/dựng.

Renderer: `tools/render_video_script.py`  ·  Input JSON: `video_script.json` (Block Model + `marker`).

## Cấu trúc bắt buộc (theo mẫu Session 02)
1. **`h2` mở đầu** — tên phần đầu tiên (dùng `##` trong text, vd `## Tổng quan về Mô hình Client - Server`).
   *Lưu ý mẫu dùng heading kiểu Markdown `##` trong nội dung; renderer giữ nguyên tiền tố `## `.*
2. **Đoạn chào mở đầu** (`p`): "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei
   Education. Trong bài học hôm nay, thầy và các em sẽ cùng nhau tìm hiểu về ...".
3. **Narration** (`narration` → renderer xử lý như `p`): lời giảng mạch lạc, ngôi "thầy"/"các em".
4. **`marker`**: dòng `**[...]**` báo hành động, ví dụ:
   `[Chuyển tiếp slide]`, `[mở trình duyệt]`, `[mở tab Network trên trình duyệt]`,
   `[mở công cụ Postman]`, `[nhấn nút Send trên Postman]`.
5. **`h2` các phần tiếp theo** xen kẽ narration + marker, bám sát mạch slide.
6. **`h2` "## Tổng kết bài giảng"** + đoạn chốt: "Cảm ơn các em đã theo dõi bài học hôm nay. Hẹn gặp lại...".

## Nguyên tắc nội dung
- Văn nói trôi chảy, giải thích để người xem hình dung (mô tả sơ đồ trên màn hình bằng lời).
- Mỗi đoạn narration là một ý trọn vẹn; nối tiếp tự nhiên giữa các phần ("... Để giải đáp điều này,
  chúng ta sẽ bước sang phần tiếp theo ...").
- Có ≥ 1 phân đoạn demo (marker mở công cụ + mô tả thao tác) nếu Lesson có thực hành.
- Bám nội dung từ SSOT của đúng Lesson đó.

## Schema `video_script.json`
```jsonc
{
  "filename": "Lesson 01  - Tổng quan mô hình client server",
  "subdir": "Kịch bản quay video",
  "lesson_no": 1,
  "blocks": [
    { "type": "h2", "text": "## Tổng quan về Mô hình Client - Server" },
    { "type": "narration", "text": "Chào mừng các em đã quay trở lại với hệ thống Elearning của Rikkei Education..." },
    { "type": "narration", "text": "Nhìn vào sơ đồ kiến trúc tổng quan trên màn hình..." },
    { "type": "marker", "text": "[Chuyển tiếp slide]" },
    { "type": "bullets", "items": ["...", "..."] },
    { "type": "marker", "text": "[mở công cụ Postman]" },
    { "type": "h2", "text": "## Tổng kết bài giảng" },
    { "type": "narration", "text": "Như vậy là trong bài học hôm nay... Cảm ơn các em..." }
  ]
}
```

## Checklist QA
- [ ] Có đoạn chào "Rikkei Education" ở đầu.
- [ ] Có ≥ 2 heading `## ` (mở đầu + Tổng kết).
- [ ] Có mục "Tổng kết bài giảng" và câu chốt "Cảm ơn các em".
- [ ] Có ≥ 1 `marker` `[Chuyển tiếp slide]`.
- [ ] Đủ mỗi Lesson 1 file kịch bản.
