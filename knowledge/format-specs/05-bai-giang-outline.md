# Hợp đồng định dạng — Outline bài giảng (Bài giảng/*.md + *.docx)

⚠️ Quyết định dự án: agent **chỉ sinh outline nội dung** (KHÔNG render .pptx). Người dùng tự hoàn thiện
thiết kế trên template PowerPoint của Rikkei. Outline phải đủ chi tiết để map **1:1** lên các slide.

Renderer: `tools/render_slide_outline.py` → xuất `<title>.md` (chính) + `<title>.docx` (bản đọc).
Input JSON: `slide_outline.json`.

## Cấu trúc deck (theo mẫu Session 02 — ~25 slide cho 5 Lesson)
1. **Slide tiêu đề**: Module, tên session, "Phiên bản: 1.0".
2. **Slide NỘI DUNG** (agenda): liệt kê các phần = các Lesson.
3. **Các phần theo Lesson**: mỗi Lesson mở bằng slide tiêu đề phần "N. <Tên Lesson> - 1", rồi các slide nội dung
   "N. ... - 2/3/4..." (đánh số chạy trong phần).
4. **Slide TỔNG KẾT**: tóm tắt mỗi Lesson 1 dòng.
5. **Slide KẾT THÚC**: "KẾT THÚC" + "HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN".

## Mỗi slide cần
- `section`: số/tên phần (vd "1. Tổng quan về kiến trúc web và FastAPI").
- `title`: tiêu đề slide hiển thị.
- `layout`: gợi ý bố cục — một trong:
  `title | agenda | section-title | bullets | 3-card | comparison-table | code | quadrant | table | summary | closing`.
- `content`: danh sách ý/khối nội dung (text ngắn gọn như trên slide, KHÔNG phải văn xuôi dài).
- `diagram_hint` (tùy chọn): mô tả sơ đồ/hình cần vẽ (vd "sơ đồ Client ↔ Internet ↔ Server").
- `speaker_notes`: ghi chú người trình bày — **liên kết với kịch bản video** của Lesson tương ứng.

## Schema `slide_outline.json`
```jsonc
{
  "filename": "Session 02 - Giới thiệu và Cài đặt FastAPI",
  "subdir": "Bài giảng",
  "title": "Giới thiệu và Cài đặt FastAPI",
  "module": "Module: Training Program Preparation",
  "version": "1.0",
  "slides": [
    { "layout": "title", "title": "Giới thiệu và Cài đặt FastAPI",
      "content": ["Session 02", "Module: Training Program Preparation", "Phiên bản: 1.0"] },
    { "layout": "agenda", "section": "NỘI DUNG", "title": "Nội dung",
      "content": ["Tổng quan kiến trúc Web và FastAPI", "Thiết lập môi trường ..."] },
    { "layout": "comparison-table", "section": "1. Tổng quan ...", "title": "Web Truyền Thống vs Web Service",
      "content": ["SSR: server trả toàn bộ HTML", "Decoupled: server chỉ trả JSON"],
      "diagram_hint": "Bảng 2 cột SSR | API",
      "speaker_notes": "Khớp Kịch bản video Lesson 01 phần So sánh SSR và API." },
    { "layout": "closing", "title": "KẾT THÚC",
      "content": ["HỌC VIỆN ĐÀO TẠO LẬP TRÌNH CHẤT LƯỢNG NHẬT BẢN"] }
  ]
}
```

## Định dạng file .md (đầu ra chính)
```
# <Tên session> — Outline bài giảng
> Module · Phiên bản 1.0 · N slide

## Slide 1 — [layout] Tiêu đề
- nội dung 1
- nội dung 2
**Sơ đồ:** <diagram_hint>
**Speaker notes:** <speaker_notes>
```

## Checklist QA
- [ ] Có slide tiêu đề, agenda, TỔNG KẾT, KẾT THÚC.
- [ ] Mỗi Lesson có ≥ 1 phần (section-title) và các slide nội dung.
- [ ] Mỗi slide nội dung có `speaker_notes`.
- [ ] Số slide hợp lý (≈20–28 cho 4–6 Lesson).
