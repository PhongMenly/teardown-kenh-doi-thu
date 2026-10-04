#!/usr/bin/env python3
"""Gộp báo cáo teardown thành MỘT file HTML duy nhất (ảnh nhúng base64) để gửi đi.

Cách dùng:
  python dong-goi-1-file.py bao-cao-teardown-<ten>.html
Kết quả: bao-cao-teardown-<ten>-1-file.html nằm cạnh file gốc.
Ảnh được tìm theo đường dẫn trong thuộc tính src, tính từ thư mục chứa file HTML.
Ảnh thiếu thì giữ nguyên src và in cảnh báo (không dừng).
"""
import base64
import mimetypes
import os
import re
import sys

IMG_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', re.I)


def main(argv):
    if len(argv) != 1 or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    src = os.path.abspath(argv[0])
    base = os.path.dirname(src)
    html = open(src, encoding="utf-8").read()
    missing, done = [], 0

    def repl(m):
        nonlocal done
        path = m.group(2)
        if path.startswith(("data:", "http:", "https:")):
            return m.group(0)
        full = os.path.normpath(os.path.join(base, path))
        if not os.path.isfile(full):
            missing.append(path)
            return m.group(0)
        mime = mimetypes.guess_type(full)[0] or "image/jpeg"
        b64 = base64.b64encode(open(full, "rb").read()).decode("ascii")
        done += 1
        return f'{m.group(1)}data:{mime};base64,{b64}{m.group(3)}'

    out = IMG_RE.sub(repl, html)
    dst = os.path.splitext(src)[0] + "-1-file.html"
    open(dst, "w", encoding="utf-8").write(out)
    print(f"Đã nhúng {done} ảnh. Ghi: {dst} ({os.path.getsize(dst) // 1024} KB)")
    for p in missing:
        print("CẢNH BÁO: thiếu ảnh", p)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
