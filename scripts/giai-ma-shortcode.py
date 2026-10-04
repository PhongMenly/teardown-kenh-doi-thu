#!/usr/bin/env python3
"""Giải mã giờ đăng của bài Instagram từ shortcode (hoặc từ link bài).

Instagram đặt mã bài (shortcode) bằng cách mã hoá base64 một số nguyên 64 bit.
23 bit thấp là phần đệm, phần còn lại là số mili giây kể từ mốc 2011-08-24 21:07:01.721 UTC.

Cách dùng:
  python giai-ma-shortcode.py CxKPoQmS5Q3 https://www.instagram.com/reel/CxKPoQmS5Q3/
  python giai-ma-shortcode.py --test          # tự kiểm tra mã hoá/giải mã khứ hồi
Kết quả: mỗi dòng "shortcode<TAB>thời điểm UTC ISO".
Lưu ý: đây là giờ UTC. Muốn giờ Việt Nam cộng 7 tiếng.
"""
import re
import sys
from datetime import datetime, timedelta, timezone

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
EPOCH_MS = 1314220021721  # 2011-08-24 21:07:01.721 UTC
URL_RE = re.compile(r"instagram\.com/(?:[^/]+/)?(?:p|reel|reels|tv)/([A-Za-z0-9_-]+)")


def extract_shortcode(text: str) -> str:
    m = URL_RE.search(text)
    return m.group(1) if m else text.strip().strip("/")


def shortcode_to_id(shortcode: str) -> int:
    n = 0
    for ch in shortcode:
        n = n * 64 + ALPHABET.index(ch)
    return n


def id_to_datetime(media_id: int) -> datetime:
    ms = (media_id >> 23) + EPOCH_MS
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc)


def shortcode_to_datetime(shortcode: str) -> datetime:
    return id_to_datetime(shortcode_to_id(shortcode))


def datetime_to_shortcode(dt: datetime) -> str:
    """Chỉ dùng để kiểm thử khứ hồi."""
    ms = int(dt.timestamp() * 1000) - EPOCH_MS
    n = ms << 23
    out = ""
    while n:
        n, r = divmod(n, 64)
        out = ALPHABET[r] + out
    return out


def _self_test() -> None:
    base = datetime(2026, 6, 9, 12, 34, 56, tzinfo=timezone.utc)
    for delta in (0, 3600, 86400 * 30, 86400 * 116):
        dt = base + timedelta(seconds=delta)
        sc = datetime_to_shortcode(dt)
        back = shortcode_to_datetime(sc)
        assert abs((back - dt).total_seconds()) < 1, (dt, sc, back)
    assert extract_shortcode("https://www.instagram.com/reel/AbC_d-1/?igsh=x") == "AbC_d-1"
    assert extract_shortcode("https://www.instagram.com/zara/p/XyZ123/") == "XyZ123"
    print("OK: khứ hồi shortcode <-> thời gian chạy đúng")


def main(argv: list) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--test":
        _self_test()
        return 0
    for item in argv:
        sc = extract_shortcode(item)
        try:
            print(f"{sc}\t{shortcode_to_datetime(sc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
        except ValueError:
            print(f"{sc}\tKHÔNG GIẢI MÃ ĐƯỢC (ký tự lạ)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
