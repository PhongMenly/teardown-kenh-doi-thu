# Cấu trúc và cách viết báo cáo teardown

Báo cáo là một file HTML một trang, dựng từ `assets/mau-bao-cao.html` (đã có sẵn CSS, nhãn, khung khoanh đỏ, mục lục). Bản mẫu thật đã làm: `vi-du/zara/bao-cao-teardown-zara.html` (trong skill).

## Bố cục thư mục đầu ra

```
teardown-<ten-kenh>/
  bao-cao-teardown-<ten-kenh>.html      báo cáo chính, ảnh gọi từ img/
  bao-cao-teardown-<ten-kenh>-1-file.html   bản một file (ảnh nhúng base64) để gửi đi
  teardown-<ten-kenh>.md                tóm tắt chữ để lưu và tìm lại
  bai-viet.csv                          dữ liệu thô các bài
  img/                                  01-profile.jpg, 02-shop.jpg, v01.jpg ...
```

Đặt tên ảnh: `01-` đến `0x-` cho ảnh trang; `v01`, `v02`... cho tấm 12 khung của từng video; `t01-` cho ảnh quy trình/công cụ; `fail-` cho bài thất bại.

## 13 mục

| # | Mục | Nội dung |
|---|---|---|
| 1 | Hồ sơ và định vị | Ảnh trang cá nhân khoanh A/B/C, số liệu, bio, highlight, họ bán gì cho ai |
| 2 | Phễu bán hàng và giá | Bảng nguồn tiền: sản phẩm, giá, của ai; CTA; bằng chứng họ khoe |
| 3 | Đường tăng trưởng | Bảng nhóm bài theo thời gian, điểm gãy trong khung `.box` |
| 4 | Các tuyến nội dung và hiệu quả | Bảng tuyến: độ dài, lượt xem trung vị, cao nhất, ghi chú |
| 5 | Mổ video từng giây + prompt viết ngược | Mỗi video: ảnh 12 khung, chú thích, ảnh trang bài khoanh đỏ, prompt trong `<pre>` |
| 6 | Bài thất bại | 1 bài thất bại để đối chiếu, các kiểu bài luôn thấp |
| 7 | Công cụ và tính năng họ chọn | Công cụ, quy trình tạo, lựa chọn tạo cảm giác "thật" |
| 8 | Caption, CTA, hashtag, giờ đăng, âm thanh | Khuôn caption, CTA qua các đời, giờ đăng, tỉ lệ tương tác |
| 9 | Khán giả quan tâm điều gì | Ai bình luận, hỏi gì, tương tác thật hay chéo |
| 10 | So với cả ngách | Công thức chung của ngách và điểm riêng của kênh |
| 11 | Nền tảng khác của cùng chủ kênh | TikTok, Threads, YouTube... |
| 12 | Việc chưa làm được | Bảng: việc, tình trạng, cần gì |
| 13 | Kết luận và việc cần quyết | 5 điều rút ra, thứ tự thử cho nhân vật của người dùng, việc cần quyết |

Mục nào không có dữ liệu thì giữ mục đó và viết một dòng "Chưa quét được vì ..." với nhãn Chưa biết. Không xoá mục.

## Nhãn bắt buộc

- `<span class="tag t-ok">Xác nhận</span>`: thấy trực tiếp trên kênh.
- `<span class="tag t-inf">Suy luận</span>`: rút ra từ dữ liệu, chủ kênh chưa nói thẳng.
- `<span class="tag t-unk">Chưa biết</span>`: chưa quét được.

Mỗi nhận định quan trọng phải có một nhãn. Số liệu thì ghi nguồn (đo từ lưới, từ thẻ meta, từ mã bài).

## Ảnh khoanh đỏ

Mỗi ảnh chụp có các ô viền đỏ đánh chữ A, B, C và chú thích bên dưới giải thích từng ô.

```html
<figure>
  <div class="shot"><img src="img/01-profile.jpg" alt="Trang cá nhân">
    <div class="b" style="left:43%;top:8.5%;width:14.5%;height:4.5%"><i>A</i></div>
  </div>
  <figcaption><b>A</b> Nội dung ô A. <b>B</b> Nội dung ô B.</figcaption>
</figure>
```

Toạ độ `left/top/width/height` tính theo phần trăm kích thước ảnh. Cách xác định: mở ảnh, đo vị trí vùng cần chỉ, chia cho kích thước ảnh. Sau khi dựng, mở báo cáo trong trình duyệt và kiểm từng ô có nằm đúng chỗ không.

Hai ảnh cạnh nhau dùng `<div class="grid2">...</div>`.

## Prompt viết ngược (mục 5)

Dùng công thức của Phong (đã lưu trong bộ nhớ: seedance-emotional-arc-prompt-formula), viết **hoàn toàn bằng tiếng Anh**:

```
[Thời lượng][Thể loại],[Nhân vật],[Âm thanh],[Ánh sáng, chất liệu, bối cảnh]

Character: based on @Image1, ...

[Shot 1, 0-3s: ...]
[Shot 2, 3-6s: ...]
[Shot 3, 6-8s: ...]
```

Quy ước: @Image1 là ảnh nhân vật, @Image2 là ảnh trang phục (flat-lay), @Image3 là ảnh bối cảnh. Mỗi video một prompt. Gắn nhãn Suy luận và ghi "chưa chạy thử". Ưu tiên góc cận và cảm xúc, sang trọng, đẳng cấp.

## Văn phong

- Tiếng Việt có dấu đầy đủ, câu ngắn, số liệu cụ thể. Gọi người dùng là "anh", tự xưng "em" (đúng như bản mẫu).
- Số Việt hoá: 1,6 triệu; 19,8 nghìn; viết tắt trong bảng N (nghìn), Tr (triệu).
- Thuật ngữ nhất quán: "teardown", "điểm gãy", "tuyến nội dung", "prompt viết ngược", "một cảnh quay liền".
- Không phóng đại. Nói rõ số mẫu (đã đo bao nhiêu trên tổng).
- Không để lộ thông tin riêng tư của người bình luận (tên, tài khoản cá nhân).

## Rà soát trước khi giao

1. Chính tả tiếng Việt: dấu, "teardown" (một từ), tên kênh, tên công cụ (Seedance, Topview, GPT Image).
2. Mọi số trong chữ khớp với bảng và với script.
3. Mọi ảnh hiện được, khoanh đỏ đúng chỗ.
4. Mỗi mục có ít nhất một nhãn Xác nhận/Suy luận/Chưa biết.
5. Mục 12 liệt kê đủ việc cần xin phép.
6. Không chứa mật khẩu, email, số điện thoại hay tên người bình luận.
