# Quy trình teardown chi tiết (8 bước)

Làm đúng thứ tự. Cuối mỗi bước ghi vào sổ tạm (một file `ghi-chu.md` trong thư mục teardown) những gì **xác nhận**, **suy luận**, **chưa biết**. Cuối cùng báo cáo chỉ là sổ tạm được trình bày lại.

Nguyên tắc chung: chỉ đọc nội dung công khai, không đăng nhập thay người dùng, mỗi thao tác cách nhau vài giây như người thật, dùng một tab riêng (không phải tab của agent khác).

## Bước 1. Định vị

Mở trang cá nhân. Chụp màn hình (đặt tên `01-profile.jpg`). Ghi:

- Số follower, số đang theo dõi, có tick xanh không, số bài.
- Bio từng dòng: lời hứa, từ khoá kêu gọi (ví dụ "222 To Start"), link.
- Highlight: tên từng cái, cái nào là bằng chứng bán hàng, cái nào dạy quy trình.
- Họ bán gì, cho ai, định vị trong một câu.

Với kênh có trang bán hàng/link trong bio: mở trang đó, chụp (`02-shop.jpg`), ghi từng sản phẩm, giá, sản phẩm của ai.

## Bước 2. Kiểm kê toàn bộ bài

Mục tiêu: có đủ danh sách bài, ngày đăng, lượt xem, thích, bình luận, caption để chạy script.

Cách lấy dữ liệu, thử lần lượt:

1. **Lưới trang cá nhân**: cuộn hết lưới, mỗi ô Reels hiện lượt xem. Ghi lại số lượt xem của từng ô theo thứ tự.
2. **Mở từng bài ở chế độ chưa đăng nhập** (hoặc trang bài công khai): thẻ `og:description` thường có số thích, bình luận và caption. Có thể lấy bằng cách tải trang bài rồi đọc thẻ meta, không cần đăng nhập.
3. **Giờ đăng**: giải mã từ mã bài bằng `scripts/giai-ma-shortcode.py` (giờ UTC, cộng 7 là giờ Việt Nam). Không cần mở từng bài.
4. Điền vào CSV theo mẫu `assets/mau-posts-gia-dinh.csv` (cột: shortcode, posted_at, views, likes, comments, tuyen, caption).

Nếu kênh có hàng trăm bài mà chỉ lấy được một phần: ghi rõ đã đo bao nhiêu trên tổng số, đừng nói như đã đo hết.

## Bước 3. Đo hiệu quả và đường tăng trưởng

Chạy:

```bash
python scripts/phan-tich-so-lieu.py bai-viet.csv --nhom 21
```

Lấy từ kết quả: tổng quan (trung vị, số bài vượt ngưỡng), bảng nhóm bài theo thời gian, top 10, nhịp đăng, tỉ lệ tương tác, giờ đăng hay gặp. Dán vào mục 3 và 8 của báo cáo.

Số liệu follower theo mốc: tìm các highlight/bài ghi mốc ("1K followers", "2K in 24h") và chụp làm bằng chứng.

## Bước 4. Tìm điểm gãy

Điểm gãy là lúc đường lượt xem đổi hẳn (trung vị nhảy lên, hoặc xuất hiện bài vượt trội đầu tiên). Cách tìm:

1. Nhìn bảng nhóm bài: nhóm nào trung vị tăng gấp đôi trở lên so với nhóm trước.
2. Mở các bài quanh thời điểm đó, ghi **cái gì khác** so với các bài trước: định dạng, nhịp đăng, chủ đề, caption, nhạc.
3. Viết kết luận trong khung `.box` ở mục 3: "trước điểm gãy làm X, sau điểm gãy làm Y".

## Bước 5. Phân loại tuyến nội dung

Gán tay cột `tuyen` trong CSV cho từng bài (chỉ cần cho các bài đo được). Chạy lại script để có bảng theo tuyến. Một bài thuộc một tuyến. Tên tuyến ngắn, nhất quán. Ghi tuyến nào mạnh, tuyến nào luôn yếu, tuyến nào bán hàng nhưng ít xem.

## Bước 6. Mổ video

Chọn 5–10 video hay nhất, cộng 1 bài thất bại cùng khuôn để đối chiếu. Với mỗi video (xem `ky-thuat-cat-khung-video.md`):

1. Cắt 12 khung đều theo thời lượng, ghi thời điểm mỗi khung.
2. Đánh dấu khung ngay sau mỗi lần cắt cảnh (viền đỏ).
3. Ghi: độ dài, số cảnh, thời điểm cắt, cảnh mở, cảnh kết, chữ trên hình, âm thanh, bối cảnh, nhân vật mặc gì.
4. **Prompt viết ngược**: viết prompt Seedance theo công thức của Phong (xem `cau-truc-bao-cao.md`, mục 5) để tái tạo video đó. Gắn nhãn "Suy luận, chưa chạy thử".

## Bước 7. Lần theo tiền

Mọi link, giá, sản phẩm, của ai, CTA qua các đời. Ghi mỗi CTA đổi vào lúc nào (đối chiếu ngày đăng). Ghi bằng chứng họ khoe (ảnh người mua, con số). Ghi rõ cái gì là của chính họ, cái gì họ chỉ làm affiliate.

Tuyệt đối không mua hàng, không đăng ký, không nhắn tin cho họ trong bước này. Nếu cần để hiểu phễu, ghi vào mục "Việc chưa làm được" và hỏi người dùng.

## Bước 8. Đọc khán giả

Đọc bình luận của 5–10 bài lớn nhất. Ghi: ai bình luận (tệp nào, nước nào), họ hỏi gì, tương tác thật hay chéo giữa các kênh cùng ngách. **Ẩn danh**: không ghi tên người bình luận, không ghi thông tin cá nhân.

So 3–4 kênh cùng ngách (chọn từ danh sách đề xuất/bình luận): cái gì là công thức chung của ngách, cái gì là riêng của kênh này.

## Kết thúc

1. Điền mục "Ba việc chưa làm được" cho mọi việc bị chặn (cần đăng nhập, cần mua, cần nhắn tin).
2. Viết kết luận: 5 điều rút ra, thứ tự thử cho nhân vật của người dùng, các việc cần quyết.
3. Cuối cùng chia ba cột: **xác nhận / suy luận / chưa biết**.

## Kênh không phải Instagram

- **TikTok**: lượt xem hiện trên lưới; giờ đăng thường suy được từ ID bài (số nguyên 64 bit, 32 bit cao là mốc giây Unix; cần kiểm lại với một bài đã biết giờ); caption, nhạc, hashtag ở trang bài.
- **YouTube**: lượt xem, ngày đăng, thời lượng ở tab Video; mô tả, thẻ, chương ở trang video; Shorts ở tab Shorts.
- **Facebook**: số tương tác ở bài; hạn chế quyền xem nên ghi rõ phần không lấy được.

Phần "giải mã giờ đăng từ mã bài" chỉ áp dụng cho Instagram; với nền tảng khác đọc ngày hiển thị.
