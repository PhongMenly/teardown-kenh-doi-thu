---
name: teardown-kenh-doi-thu
description: Mổ xẻ (teardown) một kênh đối thủ hoặc kênh mẫu trên Instagram, TikTok, YouTube, Facebook rồi dựng báo cáo HTML có ảnh khoanh đỏ, bảng số liệu, mổ video từng giây và prompt viết ngược, y như bản @iamfacelesszara. Dùng khi Phong nói "teardown", "tear down", "mổ kênh", "bóc kênh", "phân tích đối thủ", "học kênh mẫu", hoặc đưa link/tên một kênh và muốn biết họ làm gì để Uyên Linh hoặc nhân vật khác làm theo.
---

# Teardown kênh đối thủ

Một lần teardown ra: báo cáo HTML 13 mục có ảnh khoanh đỏ, một file chữ tóm tắt, dữ liệu thô các bài, và thứ tự thử cho nhân vật của anh. Làm theo skill này thì lần sau không phải nghĩ lại cách làm.

Bản mẫu thật: `vi-du/zara/bao-cao-teardown-zara.html` trong chính skill này (kênh @iamfacelesszara, quét 03/10/2026; ảnh ở `vi-du/zara/img/`). Mở thẳng bằng trình duyệt hoặc qua máy chủ cục bộ ở cuối file này. Làm kênh mới thì xem bản mẫu này trước để biết một báo cáo xong trông ra sao.

## Khi nào dùng

- Phong đưa một kênh (tên, handle hoặc link) và nói "teardown", "mổ kênh", "xem kênh này làm gì".
- Cần học khuôn nội dung, công cụ, phễu bán của một kênh để dựng nội dung cho Uyên Linh hoặc nhân vật khác.

Không dùng khi chỉ cần liệt kê ý tưởng nội dung (dùng `content-research-ideas`).

## Đầu vào cần

1. Kênh cần mổ (link hoặc handle) và nền tảng.
2. Mục đích (ví dụ: dựng kênh cho Uyên Linh, so với kênh của anh).
3. Nhân vật của anh để so sánh ở mục 13.

Thiếu cái nào thì chỉ hỏi đúng cái đó. Đã có đủ thì làm luôn, không hỏi thêm.

## Quy tắc an toàn (đọc trước khi làm)

- Chỉ đọc nội dung công khai. Không nhập mật khẩu, không đăng nhập hộ. Nếu cần đăng nhập thì nhờ Phong tự làm.
- **Không** nhắn tin, bình luận, theo dõi, mua hàng, đăng ký form của đối thủ. Việc nào cần thì ghi vào mục 12 và hỏi Phong trước.
- Không tải video về máy khi chưa xin phép. Chỉ vẽ khung đang phát lên lớp phủ rồi chụp.
- Ẩn danh người bình luận. Không ghi email, số điện thoại, mật khẩu, tên cá nhân.
- Làm việc ở **tab riêng** (id không thuộc `tab-map.json`, ví dụ tab-7 trở lên), mỗi lệnh trình duyệt phải có `tabId`. Thao tác cách nhau vài giây như người thật.
- Khi Phong đang xem cùng tab, trang có thể tự cuộn lệch. Làm ở tab riêng của em và chụp màn hình ngay trước khi bấm.

## Quy trình 8 bước

Chi tiết từng bước, kèm cách lấy dữ liệu: `references/quy-trinh-chi-tiet.md`.

1. **Định vị**: trang cá nhân, bio, highlight, trang bán hàng. Họ bán gì cho ai.
2. **Kiểm kê toàn bộ bài**: đủ ngày đăng, lượt xem, thích, bình luận, caption vào `bai-viet.csv`. Giờ đăng giải mã từ mã bài bằng `scripts/giai-ma-shortcode.py`.
3. **Đo hiệu quả**: chạy `scripts/phan-tich-so-lieu.py` ra trung vị, bảng nhóm bài, top 10, nhịp đăng.
4. **Tìm điểm gãy**: lúc đường lượt xem đổi, và họ đã đổi cái gì.
5. **Phân loại tuyến nội dung**: gán tay cột `tuyen`, chạy lại script.
6. **Mổ video** 5–10 video hay nhất + 1 bài thất bại: ảnh 12 khung (`references/ky-thuat-cat-khung-video.md`), prompt viết ngược theo công thức Seedance của Phong.
7. **Lần theo tiền**: link, giá, sản phẩm của ai, CTA qua các đời, bằng chứng họ khoe.
8. **Đọc khán giả** và so 3–4 kênh cùng ngách.

Cuối cùng phân ba cột: **xác nhận / suy luận / chưa biết**.

## Dựng báo cáo

1. Tạo thư mục `D:\XÂY AI AGENT\teardown-<ten-kenh>\` có `img/`.
2. Chép `assets/mau-bao-cao.html` thành `bao-cao-teardown-<ten-kenh>.html`, thay mọi `{{...}}`, điền 13 mục theo `references/cau-truc-bao-cao.md`.
3. Chụp ảnh đặt vào `img/`, khoanh đỏ theo toạ độ phần trăm.
4. Tạo bản một file (ảnh nhúng base64) để gửi đi, và `teardown-<ten-kenh>.md` tóm tắt chữ.

Xem báo cáo trên máy: thêm một mục vào `D:\XÂY AI AGENT\.claude\launch.json`:

```json
{ "name": "teardown-<ten-kenh>", "runtimeExecutable": "python",
  "runtimeArgs": ["-m", "http.server", "<cong>", "--directory", "D:\\XÂY AI AGENT\\teardown-<ten-kenh>"], "port": <cong> }
```

Mở `http://localhost:<cong>/bao-cao-teardown-<ten-kenh>.html#s1`. Cổng bản Zara là 8791, chọn cổng khác nếu đã dùng.

## Giao kết quả

Trả lời ngắn trong chat, theo thứ tự:

1. Hai ba dòng: kênh này thắng nhờ đâu.
2. Đường dẫn báo cáo (localhost và file).
3. Điểm gãy và thứ tự thử cho nhân vật của anh.
4. Việc cần Phong quyết hoặc cho phép (mục 12 và 13).

## Rà soát trước khi giao

- Chính tả tiếng Việt, dấu, thuật ngữ nhất quán ("teardown" viết một từ).
- Số trong chữ khớp bảng và script.
- Mọi ảnh hiện được, khoanh đỏ đúng chỗ (mở báo cáo ra xem từng ảnh).
- Mỗi mục có nhãn Xác nhận / Suy luận / Chưa biết.
- Mọi việc cần xin phép đã nằm trong mục 12.
- Không có dữ liệu riêng tư.

## Sau khi xong (bắt buộc, để skill có bộ nhớ)

1. Thêm một dòng vào **đầu** bảng trong `nhat-ky-teardown.md` (ngày, kênh, nền tảng, đường dẫn báo cáo, điều rút ra, việc dang dở).
2. Ghi một file ngắn vào bộ nhớ của Claude (loại reference): kênh, ngày quét, đường dẫn báo cáo, 3–5 điều rút ra, việc dang dở. Thêm một dòng vào MEMORY.md.
3. Có bài học mới (chỗ vấp, mẹo lấy dữ liệu, công cụ mới) thì thêm vào `references/bai-hoc-tu-zara.md` hoặc tạo `references/bai-hoc-<ten-kenh>.md`, rồi sửa skill nếu quy trình đổi.
4. Có thể chạy `scripts/dong-goi-1-file.py` để ra bản một file gửi đi.

## Trước khi bắt đầu một kênh mới

Đọc `references/bai-hoc-tu-zara.md` (ví dụ đã làm + chỗ đã vấp) và liếc `nhat-ky-teardown.md` xem kênh đó đã mổ chưa. Nếu đã mổ thì quét lại và so với lần trước.

## Tệp trong skill

| Tệp | Dùng để |
|---|---|
| `references/quy-trinh-chi-tiet.md` | Cách làm từng bước, cách lấy dữ liệu, kênh không phải Instagram |
| `references/cau-truc-bao-cao.md` | 13 mục, nhãn, khoanh đỏ, văn phong, danh sách rà soát |
| `references/ky-thuat-cat-khung-video.md` | Cắt 12 khung, đánh dấu cú cắt, mã JavaScript mẫu |
| `references/bai-hoc-tu-zara.md` | Bộ nhớ của skill: kênh đã mổ, điều tìm ra, chỗ đã vấp, ưu tiên của Phong |
| `nhat-ky-teardown.md` | Sổ các lần teardown đã làm (thêm dòng mới sau mỗi lần) |
| `scripts/giai-ma-shortcode.py` | Giờ đăng từ mã bài Instagram (đã kiểm thử khứ hồi) |
| `scripts/phan-tich-so-lieu.py` | Số liệu từ CSV ra bảng Markdown (đã kiểm thử bằng dữ liệu giả) |
| `scripts/dong-goi-1-file.py` | Gộp báo cáo + ảnh thành một file HTML (đã thử: ra đúng bản Zara) |
| `assets/mau-bao-cao.html` | Khung báo cáo với CSS và 13 mục |
| `assets/mau-posts-gia-dinh.csv` | CSV mẫu **số giả**, chỉ để biết các cột, không dùng làm số thật |

## Trạng thái đã kiểm chứng

- Ba script: đã chạy thử, đúng (gói một file cho ra cùng dung lượng bản Zara gốc).
- Mã JavaScript cắt khung: viết lại sau phiên Zara, **chưa chạy thử trên trang thật**. Lần đầu dùng, thử trên một video và chỉnh ngưỡng nếu cần.
- Mẫu HTML: dựng từ CSS của bản Zara; khi dựng báo cáo mới thì mở xem để chắc bố cục hiện đúng.
