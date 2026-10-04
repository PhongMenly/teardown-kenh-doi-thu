#!/usr/bin/env python3
"""Phân tích số liệu các bài của một kênh để điền mục 3, 4, 8 của báo cáo teardown.

Đầu vào: file CSV UTF-8, mỗi dòng một bài, các cột:
  shortcode   mã bài (hoặc để trống nếu đã có posted_at)
  posted_at   thời điểm đăng ISO, ví dụ 2026-07-04T09:30:00Z (để trống thì suy ra từ shortcode, chỉ Instagram)
  views       lượt xem (để trống nếu bài là ảnh, không đo được)
  likes       lượt thích
  comments    số bình luận
  tuyen       tên tuyến nội dung bạn gán tay (makeup, thử đồ, nấu ăn...) - tuỳ chọn
  caption     caption - tuỳ chọn

Cách dùng:
  python phan-tich-so-lieu.py bai-viet.csv [--nhom 21] [--nguong 100000,1000000]
Kết quả in ra Markdown: tổng quan, bảng nhóm theo thời gian, top 10, thống kê theo tuyến,
nhịp đăng theo 4 tuần, tỉ lệ tương tác. Số Việt hoá: N = nghìn, Tr = triệu.
"""
import argparse
import csv
import importlib.util
import os
import statistics
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_shortcode_module():
    spec = importlib.util.spec_from_file_location("gm", os.path.join(HERE, "giai-ma-shortcode.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def vn(n: float) -> str:
    """1600000 -> '1,6 Tr'; 19800 -> '19,8 N'; 950 -> '950'."""
    n = float(n)
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}".replace(".", ",").replace(",0", "") + " Tr"
    if n >= 1_000:
        return f"{n / 1_000:.1f}".replace(".", ",").replace(",0", "") + " N"
    return str(int(round(n)))


def to_int(s):
    s = (s or "").strip().replace(",", "").replace(".", "")
    return int(s) if s.isdigit() else None


def parse_time(row, gm):
    t = (row.get("posted_at") or "").strip()
    if t:
        return datetime.fromisoformat(t.replace("Z", "+00:00")).astimezone(timezone.utc)
    sc = (row.get("shortcode") or "").strip()
    if sc:
        return gm.shortcode_to_datetime(sc)
    return None


def load(path):
    gm = _load_shortcode_module()
    rows = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            r["_t"] = parse_time(r, gm)
            r["_views"] = to_int(r.get("views"))
            r["_likes"] = to_int(r.get("likes"))
            r["_comments"] = to_int(r.get("comments"))
            rows.append(r)
    rows = [r for r in rows if r["_t"] is not None]
    rows.sort(key=lambda r: r["_t"])
    return rows


def fmt_date(dt):
    return dt.strftime("%d/%m")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--nhom", type=int, default=21, help="số bài mỗi nhóm khi chia theo thời gian")
    ap.add_argument("--nguong", default="10000,100000,1000000", help="các ngưỡng lượt xem, cách nhau dấu phẩy")
    a = ap.parse_args()
    rows = load(a.csv)
    if not rows:
        print("Không có dòng nào có thời gian đăng.")
        return 1
    reels = [r for r in rows if r["_views"] is not None]
    views = [r["_views"] for r in reels]
    days = max((rows[-1]["_t"] - rows[0]["_t"]).days, 1)

    print("## Tổng quan\n")
    print(f"- Bài đầu tiên: {rows[0]['_t']:%d/%m/%Y} (UTC). Bài mới nhất: {rows[-1]['_t']:%d/%m/%Y}.")
    print(f"- Tổng {len(rows)} bài trong {days} ngày, tức {str(round(len(rows) / days, 1)).replace('.', ',')} bài/ngày.")
    if views:
        print(f"- Có {len(reels)} bài đo được lượt xem. Tổng lượt xem khoảng {vn(sum(views))}. "
              f"Trung vị {vn(statistics.median(views))}, trung bình {vn(statistics.mean(views))}, cao nhất {vn(max(views))}.")
        ths = [int(x) for x in a.nguong.split(",") if x.strip()]
        for th in sorted(ths, reverse=True):
            print(f"- {sum(1 for v in views if v >= th)} bài từ {vn(th)} lượt xem trở lên.")
        print(f"- {sum(1 for v in views if v < min(ths))} bài dưới {vn(min(ths))} lượt xem.")

    print("\n## Nhóm bài theo thời gian (tìm điểm gãy)\n")
    print("| Nhóm bài | Giai đoạn | Lượt xem trung vị | Cao nhất |")
    print("|---|---|---|---|")
    for i in range(0, len(rows), a.nhom):
        g = rows[i:i + a.nhom]
        gv = [r["_views"] for r in g if r["_views"] is not None]
        med = vn(statistics.median(gv)) if gv else "-"
        mx = vn(max(gv)) if gv else "-"
        print(f"| {i + 1}–{i + len(g)} | {fmt_date(g[0]['_t'])} – {fmt_date(g[-1]['_t'])} | {med} | {mx} |")

    if reels:
        print("\n## 10 bài xem nhiều nhất\n")
        print("| Hạng | Ngày đăng | Lượt xem | Thích | Bình luận | Mã bài |")
        print("|---|---|---|---|---|---|")
        for k, r in enumerate(sorted(reels, key=lambda r: -r["_views"])[:10], 1):
            print(f"| {k} | {r['_t']:%d/%m/%Y} | {vn(r['_views'])} | "
                  f"{vn(r['_likes']) if r['_likes'] is not None else '-'} | "
                  f"{r['_comments'] if r['_comments'] is not None else '-'} | {r.get('shortcode', '')} |")

    tuyen = {}
    for r in reels:
        t = (r.get("tuyen") or "").strip()
        if t:
            tuyen.setdefault(t, []).append(r["_views"])
    if tuyen:
        print("\n## Theo tuyến nội dung\n")
        print("| Tuyến | Số bài | Trung vị | Cao nhất |")
        print("|---|---|---|---|")
        for t, vs in sorted(tuyen.items(), key=lambda kv: -statistics.median(kv[1])):
            print(f"| {t} | {len(vs)} | {vn(statistics.median(vs))} | {vn(max(vs))} |")

    print("\n## Nhịp đăng theo 4 tuần\n")
    print("| Giai đoạn | Số bài | Bài/ngày |")
    print("|---|---|---|")
    start = rows[0]["_t"]
    buckets = {}
    for r in rows:
        buckets.setdefault((r["_t"] - start).days // 28, []).append(r)
    for b in sorted(buckets):
        g = buckets[b]
        print(f"| {fmt_date(g[0]['_t'])} – {fmt_date(g[-1]['_t'])} | {len(g)} | {str(round(len(g) / 28, 1)).replace('.', ',')} |")

    eng = [(r["_likes"] / r["_views"], r) for r in reels if r["_likes"] is not None and r["_views"]]
    if eng:
        ratios = [e for e, _ in eng]
        print("\n## Tỉ lệ tương tác\n")
        med_pct = f"{statistics.median(ratios) * 100:.1f}".replace(".", ",")
        max_pct = f"{max(ratios) * 100:.1f}".replace(".", ",")
        print(f"- Thích/lượt xem: trung vị {med_pct}%, cao nhất {max_pct}%.")
        com = [r["_comments"] / r["_views"] for r in reels if r["_comments"] is not None and r["_views"]]
        if com:
            com_pct = f"{statistics.median(com) * 100:.2f}".replace(".", ",")
            print(f"- Bình luận/lượt xem: trung vị {com_pct}%.")

    hours = {}
    for r in rows:
        hours[(r["_t"].hour + 7) % 24] = hours.get((r["_t"].hour + 7) % 24, 0) + 1
    top_h = sorted(hours.items(), key=lambda kv: -kv[1])[:3]
    print("\n## Giờ đăng hay gặp (giờ Việt Nam)\n")
    print("- " + ", ".join(f"{h}h ({n} bài)" for h, n in top_h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
