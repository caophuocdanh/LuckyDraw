# LuckyDraw-py

LuckyDraw-py là ứng dụng quay số may mắn với giao diện đồ họa trực quan, phù hợp cho các sự kiện, bốc thăm trúng thưởng, hoặc các hoạt động cần chọn ngẫu nhiên người thắng giải.

---

## 📦 Cấu trúc dự án

```
LuckyDraw py/
├── main.py           # Mã nguồn chính, giao diện và logic quay số
├── config.json       # Cấu hình giải thưởng và số lượng người tham gia
├── results.json      # Lưu kết quả quay số (tự động tạo/lưu)
├── win_sound.mp3     # Âm thanh khi có người trúng giải
└── README.md         # Tài liệu hướng dẫn sử dụng
```

## 🚀 Tính năng nổi bật
- **Giao diện fullscreen** hiện đại, dễ sử dụng với tkinter.
- **Tùy chỉnh giải thưởng**: Số lượng, tên, màu sắc linh hoạt qua `config.json`.
- **Hiển thị lưới số**: Trực quan, cập nhật trạng thái từng số khi trúng giải.
- **Lưu lịch sử kết quả**: Không trùng lặp, có thể reset dễ dàng.
- **Hiệu ứng âm thanh** khi có người trúng giải.
- **Nút reset và thoát nhanh** tiện lợi.

## ⚙️ Hướng dẫn cấu hình (`config.json`)
```json
{
  "settings": {
    "title": "Lucky Draw",
    "total_numbers": 48,
    "draw_duration_seconds": 2
  },
  "prizes": [
    { "name": "Giải Nhất", "count": 1, "color": "#f72585" },
    { "name": "Giải Nhì", "count": 1, "color": "#fca311" },
    { "name": "Giải Ba", "count": 2, "color": "#06d6a0" },
    { "name": "Giải Khuyến Khích", "count": 2, "color": "#4361ee" }
  ]
}
```
- `total_numbers`: Tổng số người tham gia/quay số.
- `draw_duration_seconds`: Thời gian hiệu ứng trước khi công bố kết quả.
- `prizes`: Danh sách giải thưởng, mỗi giải có tên, số lượng, màu sắc.

## 🖥️ Hướng dẫn sử dụng
1. **Cài đặt Python 3.x** và các thư viện phụ thuộc:
   ```bash
   pip install pygame
   ```
2. **Chạy chương trình:**
   ```bash
   python main.py
   ```
3. **Quay số:** Nhấn nút 🎁, kết quả sẽ hiển thị và lưu lại.
4. **Reset:** Nhấn nút 🔄 để quay lại từ đầu.

## 📑 Giải thích các file
- `main.py`: Toàn bộ giao diện và logic quay số, lưu/đọc kết quả, phát nhạc.
- `config.json`: Tùy chỉnh số lượng người, giải thưởng, màu sắc.
- `results.json`: Lưu kết quả mỗi lần quay, tự động tạo nếu chưa có.
- `win_sound.mp3`: Âm thanh khi có người trúng giải (có thể thay file khác).

## ❓ Câu hỏi thường gặp
- **Chạy bị lỗi thiếu thư viện?**
  - Cài đặt lại bằng: `pip install pygame`
- **Muốn thêm giải thưởng?**
  - Thêm vào mảng `prizes` trong `config.json`.
- **Muốn đổi màu giải thưởng?**
  - Đổi mã màu hex trong trường `color`.
- **Muốn reset toàn bộ kết quả?**
  - Nhấn nút 🔄 hoặc xóa file `results.json`.

## 📷 Minh họa giao diện
> ![demo](luckydraw.jpg)

## 📝 Tác giả & Đóng góp
- Tự động sinh README bởi GitHub Copilot
- Đóng góp ý kiến, báo lỗi hoặc PR tại repository này!
