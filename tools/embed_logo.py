#!/usr/bin/env python3
"""One-shot: take Alfred's logo PNG, strip the flattened white background, and
embed the result straight into home.html's logo config line as a data URI.

    python3 embed_logo.py <path-to-uploaded-logo.png>

Writes assets/centerline-logo-transparent.png (for reference / re-upload) and
rewrites the `logo:` line in home.html. Nothing else is touched.
"""
import base64, io, pathlib, subprocess, sys
from collections import deque
from PIL import Image

ROOT = pathlib.Path("/home/user/Center")
SP = pathlib.Path(__file__).parent


def strip_white(im):
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()

    def is_bg(x, y):
        r, g, b, a = px[x, y]
        if a < 8:
            return True
        return min(r, g, b) >= 206 and (max(r, g, b) - min(r, g, b)) <= 26

    mark = bytearray(w * h)          # 0 unknown, 1 keep, 2 background, 3 pending
    dq = deque()
    for x in range(w):
        dq.append((x, 0)); dq.append((x, h - 1))
    for y in range(h):
        dq.append((0, y)); dq.append((w - 1, y))
    while dq:
        x, y = dq.popleft()
        i = y * w + x
        if mark[i]:
            continue
        if not is_bg(x, y):
            mark[i] = 1; continue
        mark[i] = 2
        if x: dq.append((x - 1, y))
        if x < w - 1: dq.append((x + 1, y))
        if y: dq.append((x, y - 1))
        if y < h - 1: dq.append((x, y + 1))

    # enclosed regions: the space inside the logo's own frame is background too,
    # but small enclosed shapes (letter counters, knocked-out type) are artwork
    min_area, span_x, span_y = w * h * 0.02, w * 0.25, h * 0.25
    for sy in range(h):
        for sx in range(w):
            i = sy * w + sx
            if mark[i]:
                continue
            if not is_bg(sx, sy):
                mark[i] = 1; continue
            comp, q = [], deque([(sx, sy)])
            mark[i] = 3
            mnx = mxx = sx; mny = mxy = sy
            while q:
                x, y = q.popleft(); comp.append((x, y))
                mnx = min(mnx, x); mxx = max(mxx, x)
                mny = min(mny, y); mxy = max(mxy, y)
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        j = ny * w + nx
                        if not mark[j]:
                            if is_bg(nx, ny):
                                mark[j] = 3; q.append((nx, ny))
                            else:
                                mark[j] = 1
            # This logo has no white artwork — CONSTRUCTION is black — so every
            # enclosed near-white region is background: the space inside the
            # frame AND the counters of letters like the R in CENTERLINE.
            for x, y in comp:
                mark[y * w + x] = 2

    cleared = 0
    for y in range(h):
        for x in range(w):
            if mark[y * w + x] != 2:
                continue
            r, g, b, a = px[x, y]
            if a < 8:
                continue
            lum = r * 0.299 + g * 0.587 + b * 0.114
            al = (242 - lum) / 36
            if al <= 0.02:
                px[x, y] = (r, g, b, 0); cleared += 1; continue
            al = min(1.0, al)
            px[x, y] = (
                max(0, min(255, int((r - 255 * (1 - al)) / al))),
                max(0, min(255, int((g - 255 * (1 - al)) / al))),
                max(0, min(255, int((b - 255 * (1 - al)) / al))),
                int(a * al))
            cleared += 1
    return im, cleared


def main():
    src = pathlib.Path(sys.argv[1])
    im = Image.open(src)
    print("source: %s  %s  mode=%s" % (src.name, im.size, im.mode))

    out, cleared = strip_white(im)
    total = out.size[0] * out.size[1]
    print("cleared %d px (%.1f%% of the image)" % (cleared, 100.0 * cleared / total))

    # crop the now-empty margin so the logo fills its box on the page
    bbox = out.getbbox()
    if bbox:
        out = out.crop(bbox)
        print("cropped to artwork: %s" % (out.size,))

    # cap the long edge — the hero shows it at most ~680px wide
    if out.size[0] > 1100:
        out = out.resize((1100, round(out.size[1] * 1100 / out.size[0])), Image.LANCZOS)
        print("resized to %s" % (out.size,))

    # PNG on disk for reference / re-upload, WebP for the inline copy: the gold
    # gradient bands badly in a palette PNG, and full RGBA PNG is ~4x the bytes
    # for no visible gain.
    png = ROOT / "assets/centerline-logo-transparent.png"
    out.save(png, optimize=True)
    print("wrote %s (%.0f KB)" % (png, png.stat().st_size / 1024))

    webp = ROOT / "assets/centerline-logo-transparent.webp"
    out.save(webp, "WEBP", quality=92, method=6)
    raw = webp.read_bytes()
    print("wrote %s (%.0f KB)" % (webp, len(raw) / 1024))

    uri = "data:image/webp;base64," + base64.b64encode(raw).decode()
    print("data URI: %.0f KB" % (len(uri) / 1024))

    home = ROOT / "home.html"
    s = home.read_text(encoding="utf-8")
    import re
    new, n = re.subn(r'(\n  logo:\s+")[^"]*(",)', lambda m: m.group(1) + uri + m.group(2), s, count=1)
    if n != 1:
        sys.exit("could not find the logo: line in home.html")
    home.write_text(new, encoding="utf-8")
    print("embedded into home.html")

    subprocess.run([sys.executable, str(SP / "gen_home.py")], check=True)
    subprocess.run([sys.executable, str(SP / "gen_preview.py")], check=True)


if __name__ == "__main__":
    main()
