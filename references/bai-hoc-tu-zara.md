# Bài học từ lần teardown đầu tiên (@iamfacelesszara, 03/10/2026)

Đây là "bộ nhớ" của skill: ví dụ đã làm thật, những gì tìm ra, và những chỗ vấp. Đọc trước khi làm một kênh mới để khỏi vấp lại và biết một báo cáo tốt trông thế nào.

Bản đầy đủ: `D:\XÂY AI AGENT\teardown-zara\bao-cao-teardown-zara.html` (có ảnh) và `D:\XÂY AI AGENT\teardown-iamfacelesszara.md` (chữ).

## Kênh đó là gì (một đoạn)

AI influencer nữ "Zara", chủ kênh không lộ mặt. Bắt đầu 08/06/2026 sau khi mất tài khoản cũ 33 nghìn follower. Sau chưa đầy 4 tháng: 47,8 nghìn follower, 189 bài, khoảng 10,8 triệu lượt xem Reels. Sản phẩm thật là dạy dựng AI avatar; thời trang, làm đẹp, nấu ăn chỉ là nội dung mồi. Chủ kênh là affiliate của khoá học 197 USD và bộ prompt 67 USD, chỉ mentorship 650–1.099 USD là của cô ấy. CTA duy nhất lặp lại: nhắn từ khoá "222".

## Điều tìm ra, đáng nhớ

- **Điểm gãy:** 60 bài đầu kiểu dạy học ("AI Realism Hack") gần như không ai xem. Kênh chỉ lên khi chuyển sang video thuần hình ảnh GRWM/outfit và dời hết lời bán xuống caption.
- **Khuôn thắng:** 5 trong 10 video top là **một cảnh quay liền** 10–14 giây, máy cố định, toàn thân (lớp nền, mặc quần, mặc áo, cúi xỏ giày, cầm túi, tạo dáng). Video cao nhất (1,6 triệu) là makeup cận mắt 8 giây, 3 cảnh.
- **Thắng nhờ số lượng biến thể:** cùng khuôn, cùng nhạc, đăng cách một ngày, lượt xem lệch từ 20 nghìn đến 1,1 triệu. Phải đăng nhiều.
- **Khán giả lạnh:** bình luận rất ít (bài 1,6 triệu chỉ 122 bình luận), mua hàng đến từ tin nhắn theo từ khoá, không đến từ bình luận.
- **Tuyến yếu ổn định:** nấu ăn, quảng cáo trả tiền, bài dạy học.
- **Quy trình sản xuất cô ấy tự kể:** ảnh nhân vật cố định + ảnh trang phục xếp flat-lay + custom GPT viết prompt, rồi Seedance. Ba khuôn thử đồ: một bộ, chia đôi màn hình, nhiều bộ chuyển cảnh.

## Việc chưa làm được lần đó (để biết phải xin phép)

Tái tạo video bằng nhân vật của mình, nhắn "222" để đi hết phễu, mua bộ bot 67 USD. Cả ba đều cần Phong cho phép hoặc tự làm.

## Chỗ đã vấp và cách tránh

| Vấp | Cách tránh |
|---|---|
| Tab đang xem bị Phong dùng chung, trang tự nhảy hoặc cuộn lệch, bấm nhầm | Làm ở **tab riêng** (tab-7 trở lên), chụp màn hình ngay trước khi bấm |
| Cửa sổ popup (đăng nhập) chặn công cụ trình duyệt, không điều hướng được | Nhờ Phong đóng popup, không cố vượt |
| Lệnh trình duyệt thiếu `tabId` bị chặn bởi hook bảo vệ tab | Luôn truyền `tabId` tường minh |
| Video không hiện khung khi tab ở nền | Đưa tab lên phía trước, chờ khoảng 2 giây rồi mới chụp |
| Tab Chrome ẩn không vẽ được khung video | Dùng khung trình duyệt trong app, không dùng Chrome ẩn |
| Lưu nhầm ảnh Pinterest (ảnh trang phục xếp rời khi Phong muốn ảnh người mặc) | Khi chọn ảnh mẫu, **cho Phong duyệt trước khi lưu**, nói rõ loại ảnh đã chọn |
| Nhầm giờ đăng do múi giờ | Giờ giải mã từ mã bài là UTC; giờ Việt Nam là cộng 7 |
| Số đo không đủ bài | Ghi rõ đã đo bao nhiêu trên tổng, đừng nói như đã đo hết |

## Công cụ đã dùng được

- Giờ đăng từ mã bài Instagram (`scripts/giai-ma-shortcode.py`).
- Lượt thích, bình luận, caption từ thẻ `og:description` của trang bài khi chưa đăng nhập.
- Ảnh 12 khung vẽ lên lớp phủ (`references/ky-thuat-cat-khung-video.md`; mã mẫu viết lại, chưa chạy thử lại).
- Báo cáo HTML và bản một file (`scripts/dong-goi-1-file.py`, đã thử: ra đúng bản Zara, cùng dung lượng).

## Phong ưu tiên gì khi học một kênh mẫu

Góc cận và cảm xúc, nhân vật xinh đẹp, sang trọng, đẳng cấp. Khi lọc "đáng học" thì ưu tiên các cảnh cận mặt, cận môi, cận mắt, cận tay, rồi nửa người, sau cùng mới toàn thân. Bỏ các tuyến lệch thương hiệu (hút thuốc, đồ hoá trang lạ, nấu ăn dùng dao).
