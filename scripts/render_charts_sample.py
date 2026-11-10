# -*- coding: utf-8 -*-
"""Synthetic English chart samples for public portfolio (scheme B).

Two chart types derived from private PDFs:
  panel-wave-schematic.png  -- index-level A->B->C1->C2->C3 polyline + label table
  panel-val-percentile.png  -- PE vs PB percentile horizontal bars
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Lives at: <course>/G github/scripts/render_charts_sample.py
REPO = Path(__file__).resolve().parents[1]  # .../G github
OUT = REPO / "docs" / "photos" / "charts"

WIDTH = 1200
BG = (248, 249, 251)
NAVY = (30, 58, 95)
INK = (20, 30, 45)
SUB = (90, 100, 110)
BODY = (35, 45, 55)
ZEBRA = (238, 242, 246)
RED = (190, 60, 60)
PE_BLUE = (52, 100, 160)
PB_GREEN = (60, 140, 90)
FOOT = "Sample data for layout demonstration · archived snapshot · Not investment advice"

ROW_H = 22
HEAD_H = 24

WAVE = [
    # name, A-low, B-peak, C1, C2, C3
    ("SYM-IDX-1", 1020.0, 1100.0, 1050.0, 1075.0, 1010.0,
     ["2026-07-20", "2026-09-01", "2026-09-28", "2026-10-08", "2026-10-23"]),
    ("SYM-IDX-2", 2250.0, 2800.0, 2450.0, 2525.0, 2220.0,
     ["2026-08-18", "2026-09-28", "2026-10-08", "2026-11-03", "2026-11-10"]),
    ("SYM-IDX-3", 5500.0, 9000.0, 6800.0, 7250.0, 5325.0,
     ["2026-08-18", "2026-09-28", "2026-10-08", "2026-11-03", "2026-11-10"]),
]
KIND = ["bottom", "top", "bottom", "top", "bottom"]
LABELS5 = ["A-low", "B-peak", "C1", "C2", "C3"]

VAL_BARS = [
    ("SYM-IDX-1", 78.0, 42.0),
    ("SYM-IDX-2", 32.0, 15.0),
    ("SYM-IDX-3", 8.0, 18.0),
    ("SYM-IDX-4", 65.0, 20.0),
    ("SYM-IDX-5", 55.0, 54.0),
    ("SYM-IDX-6", 83.0, 45.0),
]


def font(size: int):
    for name in ("segoeui.ttf", "arial.ttf", "msyh.ttc"):
        p = Path(r"C:\Windows\Fonts") / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def new_canvas():
    img = Image.new("RGB", (WIDTH, 2400), BG)
    return img, ImageDraw.Draw(img)


def head(d, title, sub):
    d.text((30, 26), title, fill=INK, font=font(28))
    d.text((30, 66), sub, fill=SUB, font=font(14))
    return 100


def draw_table(d, x, y, headers, rows, col_w, fs=11, hfs=12, row_h=ROW_H):
    total = sum(col_w)
    d.rectangle([x, y, x + total, y + HEAD_H], fill=NAVY)
    cx = x
    for h, w in zip(headers, col_w):
        d.text((cx + 6, y + 5), str(h), fill=(255, 255, 255), font=font(hfs))
        cx += w
    y += HEAD_H
    for i, row in enumerate(rows):
        bg = (255, 255, 255) if i % 2 == 0 else ZEBRA
        d.rectangle([x, y, x + total, y + row_h], fill=bg)
        cx = x
        for cell, w in zip(row, col_w):
            d.text((cx + 6, y + 5), str(cell), fill=BODY, font=font(fs))
            cx += w
        y += row_h
    return y + 8


def save_crop(img, y_end, name):
    h = max(y_end + 52, 360)
    out = img.crop((0, 0, WIDTH, h))
    d = ImageDraw.Draw(out)
    d.text((30, h - 32), FOOT, fill=(120, 120, 120), font=font(12))
    OUT.mkdir(parents=True, exist_ok=True)
    out.save(OUT / name)
    print("OK", name, out.size)


# ------------------------------------------------------ wave schematics
def panel_wave_schematic():
    img, d = new_canvas()
    y = head(d, "Sample chart · Wave schematics (index-level)",
             "asof 2026-11-06 · synthetic index labels · A->B->C1->C2->C3 form kept")
    for i, row in enumerate(WAVE):
        name = row[0]
        pts = list(row[1:6])
        dates = row[6]
        y0 = y + i * 268
        d.text((30, y0), f"{name} · now {pts[-1]:.1f}", fill=NAVY, font=font(15))
        # plot area: x 40..1160, y 18..118 relative to y0
        pmin, pmax = min(pts), max(pts)
        span = pmax - pmin or 1.0
        xs = [40, 320, 600, 880, 1160]
        ys = [y0 + 118 - (v - pmin) / span * 95 for v in pts]
        poly = list(zip(xs, ys))
        d.line(poly, fill=(50, 50, 50), width=2)
        cx, cy = poly[-1]
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
        for x, lab in zip(xs, LABELS5):
            d.text((x - 22, y0 + 124), lab, fill=(90, 90, 90), font=font(11))
        # label table
        ty = y0 + 144
        table_rows = [
            [LABELS5[j], f"{pts[j]:.1f}", KIND[j], dates[j]] for j in range(5)
        ]
        draw_table(d, 40, ty, ["Label", "px", "kind", "date"], table_rows,
                   [80, 80, 90, 110], fs=11, row_h=20)
    d.text((30, y + 3 * 268 + 8),
           "Note: index labels, prices and dates are synthetic. Shape form A->B->C1->C2->C3 only.",
           fill=(80, 80, 80), font=font(12))
    save_crop(img, y + 3 * 268 + 30, "panel-wave-schematic.png")


# ------------------------------------------------------ percentile bars
def panel_val_percentile():
    img, d = new_canvas()
    y = head(d, "Sample chart · Valuation percentile bars",
             "asof 2026-11-06 · synthetic indices · PE vs PB percentile (%)")
    bar_x = 170
    max_w = 820
    d.text((bar_x, y - 22), "0%", fill=(140, 140, 140), font=font(10))
    d.text((bar_x + max_w - 20, y - 22), "100%", fill=(140, 140, 140), font=font(10))
    for i, (name, pe, pb) in enumerate(VAL_BARS):
        y0 = y + 20 + i * 58
        d.text((30, y0 + 12), name, fill=INK, font=font(13))
        d.rectangle([bar_x, y0 + 6, bar_x + int(pe / 100 * max_w), y0 + 22],
                    fill=PE_BLUE)
        d.rectangle([bar_x, y0 + 28, bar_x + int(pb / 100 * max_w), y0 + 44],
                    fill=PB_GREEN)
        tag_x = bar_x + int(max(pe, pb) / 100 * max_w) + 10
        d.text((tag_x, y0 + 12), f"PE {pe:.1f} / PB {pb:.1f}",
               fill=(80, 80, 80), font=font(12))
    d.text((30, y + 20 + 6 * 58 + 4),
           "Note: blue = PE percentile, green = PB percentile. Values and names are synthetic.",
           fill=(80, 80, 80), font=font(12))
    save_crop(img, y + 20 + 6 * 58 + 30, "panel-val-percentile.png")


def main():
    panel_wave_schematic()
    panel_val_percentile()
    print("DONE")


if __name__ == "__main__":
    main()
