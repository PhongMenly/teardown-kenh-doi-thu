# Kỹ thuật cắt khung video để mổ từng giây

Mục đích: với mỗi video cần mổ, có một ảnh 12 khung đều theo thời lượng, khung ngay sau mỗi lần cắt cảnh có viền đỏ, kèm thời điểm. Ảnh đặt tên `v01.jpg`, `v02.jpg`...

Không tải video về máy. Chỉ vẽ khung đang phát trong trang lên một lớp phủ rồi chụp màn hình lớp phủ đó. (Nếu bắt buộc phải tải video, xin phép người dùng trước và nói rõ tên file, nguồn, dung lượng.)

## Điều kiện để chạy được

1. Mở trang bài trong **tab riêng**, đưa tab lên phía trước (tab nền thường không tải video).
2. Chờ trang tải xong, bấm phát một lần để video có dữ liệu, rồi tạm dừng.
3. Sau mỗi lần dựng lớp phủ, **chờ khoảng 2 giây** rồi mới chụp.
4. Mỗi video một lần dựng, kiểm tra ảnh chụp có đủ 12 khung trước khi sang video khác.

## Mã mẫu chạy trong trang (công cụ chạy JavaScript của trình duyệt)

Trạng thái: **mã mẫu viết lại**, bản gốc dùng ở phiên Zara không còn. Chạy thử trên một video, chỉnh nếu trang đổi cấu trúc. Nếu video khác nguồn (cross-origin) làm vải vẽ bị khoá thì bước phát hiện cắt cảnh sẽ không chạy, khung vẫn vẽ được và khi đó phải đánh dấu cú cắt bằng mắt.

```js
(async () => {
  const v = document.querySelector('video');
  if (!v) return 'không thấy video';
  v.pause();
  const dur = v.duration;
  const N = 12, W = 270, H = Math.round(W * v.videoHeight / v.videoWidth);
  const seek = t => new Promise(r => { v.onseeked = r; v.currentTime = Math.min(t, dur - 0.05); });

  // 1) phát hiện cắt cảnh: lấy mẫu mỗi 0,1 giây, so mức thay đổi hình ảnh
  const cuts = [];
  try {
    const s = document.createElement('canvas'); s.width = 32; s.height = 32;
    const sc = s.getContext('2d', { willReadFrequently: true });
    let prev = null;
    for (let t = 0; t < dur; t += 0.1) {
      await seek(t);
      sc.drawImage(v, 0, 0, 32, 32);
      const d = sc.getImageData(0, 0, 32, 32).data;
      if (prev) {
        let diff = 0;
        for (let i = 0; i < d.length; i += 4) diff += Math.abs(d[i] - prev[i]) + Math.abs(d[i + 1] - prev[i + 1]) + Math.abs(d[i + 2] - prev[i + 2]);
        if (diff / (32 * 32 * 3) > 40) cuts.push(+t.toFixed(2));   // ngưỡng 40, chỉnh nếu bắt sai
      }
      prev = d;
    }
  } catch (e) { cuts.push('KHÔNG_ĐO_ĐƯỢC: ' + e.message); }

  // 2) vẽ 12 khung đều theo thời lượng, khung ngay sau cú cắt có viền đỏ
  const cols = 6, rows = 2, c = document.createElement('canvas');
  c.width = cols * (W + 6) + 6; c.height = rows * (H + 6) + 30;
  const g = c.getContext('2d');
  g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height);
  const numCuts = cuts.filter(x => typeof x === 'number');
  for (let i = 0; i < N; i++) {
    const t = (dur * (i + 0.5)) / N;
    await seek(t);
    const x = 6 + (i % cols) * (W + 6), y = 30 + Math.floor(i / cols) * (H + 6);
    g.drawImage(v, x, y, W, H);
    const prevT = (dur * (i - 0.5)) / N;
    if (numCuts.some(ct => ct > prevT && ct <= t)) { g.strokeStyle = '#e00000'; g.lineWidth = 5; g.strokeRect(x, y, W, H); }
    g.fillStyle = 'rgba(0,0,0,.75)'; g.fillRect(x, y, 64, 18);
    g.fillStyle = '#fff'; g.font = 'bold 12px Arial'; g.fillText((i + 1) + ' · ' + t.toFixed(1) + 's', x + 4, y + 13);
  }
  g.fillStyle = '#000'; g.font = 'bold 14px Arial';
  g.fillText('dài ' + dur.toFixed(1) + 's | cắt cảnh tại: ' + (numCuts.join(', ') || 'không có (1 cảnh liền)'), 8, 20);

  // 3) hiện lớp phủ phủ kín trang để chụp
  c.style.cssText = 'position:fixed;left:0;top:0;z-index:2147483647;max-width:100vw;background:#fff';
  document.body.appendChild(c);
  return { dai_giay: +dur.toFixed(1), cat_canh: cuts };
})()
```

Sau khi chụp xong, xoá lớp phủ: `document.querySelector('canvas[style*="2147483647"]')?.remove()`.

## Chú thích từng video trong báo cáo

Dưới mỗi ảnh ghi: số cảnh, thời điểm cắt, cảnh mở, cảnh kết, chữ trên hình, âm thanh, bối cảnh, nhân vật mặc gì. Ví dụ: "3 cảnh, cắt tại 3,05s và 6,35s. Cảnh 1: cận cực gần một mắt... Cảnh 3 (2 giây cuối): lùi ra chính diện, lộ kết quả."

Nếu video quá dài hoặc không dựng được khung (ví dụ cùng khuôn với video khác), nói rõ trong mục 5 thay vì bỏ qua âm thầm.
