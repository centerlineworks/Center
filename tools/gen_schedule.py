#!/usr/bin/env python3
"""Regenerate squarespace/home-part1 + home-part2 from schedule.html."""
import re, pathlib

root = pathlib.Path("/home/user/Center")
src = (root / "schedule.html").read_text(encoding="utf-8")
lines = src.split("\n")

def idx(pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i
    raise SystemExit("marker not found")

i_meta = idx(lambda l: l.startswith("<meta charset"))
i_style_end = idx(lambda l: l.strip() == "</style>", i_meta)
part1 = [l for l in lines[i_meta:i_style_end + 1] if not l.lstrip().startswith("<title>")]

i_cfg = idx(lambda l: l.strip() == "<script>", i_style_end)
i_end = max(i for i, l in enumerate(lines) if l.strip() == "</script>")
part2 = lines[i_cfg:i_end + 1]

P1_HEAD = """<!-- Centerline SCHEDULE page - PART 1 of 2
     Paste into: Page Settings -> Advanced -> Page Header Code Injection
     for the SCHEDULE page.
     Set the page title in Page Settings -> SEO to:
      Schedule a Free Estimate | Centerline Construction - Holly Springs & Canton, GA -->"""

P2_HEAD = """<!-- Centerline SCHEDULE page - PART 2 of 2
     Paste into a single Code Block (type: HTML) on the Schedule page.
     The short list at the very top is the only thing you would ever edit:
     the email address estimate requests are sent to, and your phone number. -->"""

SQSP = "https://www.centerlineworks.com/s/"


def hosted(text):
    return re.sub(r'(src|poster)="assets/([^"]+)"', lambda m: '%s="%s%s"' % (m.group(1), SQSP, m.group(2)), text)


out1 = P1_HEAD + "\n" + hosted("\n".join(part1)) + "\n"
out2 = P2_HEAD + "\n" + hosted("\n".join(part2)) + "\n"

(root / "squarespace/schedule-part1-header-injection.html").write_text(out1, encoding="utf-8")
(root / "squarespace/schedule-part2-code-block.html").write_text(out2, encoding="utf-8")
print("part1 lines:", out1.count("\n"), "part2 lines:", out2.count("\n"))
print("remaining assets/ refs:", out1.count('"assets/') + out2.count('"assets/'))
