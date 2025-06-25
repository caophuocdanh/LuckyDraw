# LuckyDraw-py

LuckyDraw-py là ứng dụng quay số may mắn với giao diện đồ họa hiện đại, hỗ trợ cấu hình giải thưởng, nhạc nền, hiệu ứng động và lưu kết quả. Phù hợp cho sự kiện, bốc thăm trúng thưởng, hoặc các hoạt động cần chọn ngẫu nhiên người thắng giải.

---

## 📦 Cấu trúc dự án

```
LuckyDraw py/
├── main.py           # Mã nguồn chính, giao diện và logic quay số (PySide6)
├── config.json       # Cấu hình giải thưởng, số lượng người, nhạc nền
├── results.json      # Lưu kết quả quay số (tự động tạo/lưu)
├── win_sound.mp3     # Âm thanh khi có người trúng giải
├── background_music.mp3 # (Tùy chọn) Nhạc nền khi quay
├── icon.md           # Danh sách icon ký tự Unicode
└── README.md         # Tài liệu hướng dẫn sử dụng
```

## 🚀 Tính năng nổi bật
- Giao diện fullscreen hiện đại với PySide6 (Qt for Python)
- Tùy chỉnh giải thưởng: tên, số lượng, màu sắc, thêm/xóa dễ dàng
- Hỗ trợ nhạc nền khi quay và hiệu ứng âm thanh khi trúng giải
- Hiển thị lưới số, hiệu ứng động khi quay và khi công bố kết quả
- Lưu lịch sử kết quả, có thể reset hoặc xóa toàn bộ
- Hỗ trợ cấu hình trực quan qua cửa sổ riêng

## ⚙️ Cài đặt thư viện phụ thuộc
Cài đặt Python 3.x và các thư viện cần thiết:
```bash
pip install PySide6 pygame
```

## 🖥️ Hướng dẫn sử dụng
1. Cấu hình giải thưởng, số lượng người, nhạc nền (nếu muốn) trong `config.json` hoặc qua giao diện cấu hình.
2. Chạy chương trình:
   ```bash
   python main.py
   ```
3. Nhấn nút "👻" để quay số, kết quả sẽ hiển thị và lưu lại.
4. Sử dụng các nút ở góc trên bên phải để cấu hình, reset, xóa kết quả hoặc thoát.

## ⚙️ Ví dụ cấu hình (`config.json`)
```json
{
  "settings": {
    "title": "Lucky Draw",
    "total_numbers": 48,
    "draw_duration_seconds": 2,
    "music": true,
    "music_duration": 20
  },
  "prizes": [
    { "id": 1, "name": "Giải Nhất", "count": 1, "color": "#f72585" },
    { "id": 2, "name": "Giải Nhì", "count": 1, "color": "#fca311" },
    { "id": 3, "name": "Giải Ba", "count": 2, "color": "#06d6a0" },
    { "id": 4, "name": "Giải Khuyến Khích", "count": 2, "color": "#4361ee" }
  ]
}
```

### Giải thích các giá trị
- **`settings`**:
  - `title`: Tiêu đề của cửa sổ ứng dụng.
  - `total_numbers`: Tổng số lượng người tham gia (hoặc số lượng vé).
  - `draw_duration_seconds`: Thời gian (giây) của hiệu ứng quay số trước khi công bố kết quả.
  - `music`: Bật/tắt nhạc nền (`true` hoặc `false`).
  - `music_duration`: Thời gian (giây) phát nhạc nền mỗi lần quay.
- **`prizes`**:
  - `id`: Mã định danh duy nhất cho mỗi giải thưởng.
  - `name`: Tên của giải thưởng (ví dụ: "Giải Nhất").
  - `count`: Số lượng giải cho mỗi loại.
  - `color`: Mã màu (hex) để hiển thị cho giải thưởng đó.

## 📑 Giải thích các file
- `main.py`: Toàn bộ giao diện và logic quay số, lưu/đọc kết quả, phát nhạc, hiệu ứng.
- `config.json`: Tùy chỉnh số lượng người, giải thưởng, nhạc nền, thời gian quay.
- `results.json`: Lưu kết quả mỗi lần quay, tự động tạo nếu chưa có.
- `win_sound.mp3`: Âm thanh khi có người trúng giải (có thể thay file khác).
- `background_music.mp3`: (Tùy chọn) Nhạc nền khi quay số.
- `icon.md`: Danh sách icon ký tự Unicode phổ biến.

## ❓ Câu hỏi thường gặp
- **Lỗi thiếu thư viện?**
  - Cài đặt lại bằng: `pip install PySide6 pygame`
- **Muốn thêm/xóa giải thưởng?**
  - Sử dụng giao diện cấu hình hoặc chỉnh sửa trực tiếp `config.json`.
- **Muốn đổi màu giải thưởng?**
  - Đổi mã màu hex trong trường `color`.
- **Muốn reset toàn bộ kết quả?**
  - Nhấn nút 🗑️ hoặc xóa file `results.json`.
- **Muốn thêm nhạc nền?**
  - Đặt file `background_music.mp3` vào thư mục dự án và bật tùy chọn nhạc nền trong cấu hình.

## 📝 Đóng góp & Liên hệ
- Đóng góp ý kiến, báo lỗi hoặc PR tại repository này!
- Tự động sinh README bởi GitHub Copilot
