# Tích hợp Obsidian (MCP filesystem)

Vault Obsidian của dự án nằm tại `vault/` (trong repo). Agent đọc/ghi/tìm/liên kết ghi chú qua
**MCP server `obsidian-mcp`** (filesystem — không cần mở Obsidian, không cần plugin).

## 1. Yêu cầu
- **Node.js** (đã có: `node -v` → v24). `npx` tự tải `obsidian-mcp` lần đầu.
- (Tùy chọn) **Obsidian app** để xem vault: mở Obsidian → "Open folder as vault" → trỏ vào thư mục `vault/`.

## 2. Cấu hình MCP (đã tạo sẵn `.mcp.json` ở gốc repo)
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "obsidian-mcp",
               "D:\\AI-Agent-trinhkhaclinh\\Agent-xaydungtainguyenhoctap\\vault"]
    }
  }
}
```
- `.mcp.json` là cấu hình MCP **phạm vi dự án** của Claude Code. Server nạp ở **lần khởi động Claude Code kế tiếp**;
  khi được hỏi, **chấp thuận/tin tưởng** server `obsidian` để bật.
- Nếu chuyển repo sang máy/đường dẫn khác: sửa đường dẫn tuyệt đối tới `vault/` trong `.mcp.json`.
- Nếu `cmd /c npx` không chạy: thử `"command": "npx"` (bỏ `cmd /c`), hoặc cài toàn cục `npm i -g obsidian-mcp`
  rồi `"command": "obsidian-mcp"`.

## 3. Kiểm tra
Sau khi khởi động lại Claude Code và bật server, agent sẽ có các tool `mcp__obsidian__*`
(đọc/ghi/tìm note, quản lý link). Thử: "liệt kê note trong vault" hoặc "tìm các note nhắc tới ASGI".

## 4. Vai trò trong pipeline
- **Sinh nội dung (stage-1)**: `tools/render_vault.py` ghi note `.md` trực tiếp (không cần MCP).
- **MCP hữu ích cho**: truy vấn/bảo trì vault khi lớn dần (tìm backlink, phát hiện link gãy, liên kết
  khái niệm giữa các session, để agent khác đọc kho tri thức). Đây là lý do tích hợp MCP filesystem.

## 5. Lựa chọn thay thế (không dùng ở đợt này)
- `obsidian-mcp-server` (REST API + Local REST API plugin) — tích hợp 'sống' với Obsidian đang chạy,
  giàu tính năng hơn nhưng thiết lập phức tạp hơn. Có thể cân nhắc sau.
