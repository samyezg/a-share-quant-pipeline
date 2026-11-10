# -*- coding: utf-8 -*-
"""Synthetic English sample panels for public portfolio (scheme B).

Revision 2 (P1-P4):
  P1  dynamic canvas height -> crop to content bottom + footer
  P2  panel-matrix cluster aggregates recomputed from detail rows
  P3  panel-val restored to 3 tables; panel-wave restored to 3 symbol chains
  P4  panel-timing judge variants widened; cross-panel E-* id note added
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# This file lives at: <course>/G github/scripts/render_panels_sample.py
REPO = Path(__file__).resolve().parents[1]  # .../G github
OUT = REPO / "docs" / "photos" / "panels"

WIDTH = 1200
BG = (248, 249, 251)
NAVY = (30, 58, 95)
INK = (20, 30, 45)
SUB = (90, 100, 110)
BODY = (35, 45, 55)
ZEBRA = (238, 242, 246)
FOOT = "Sample data for layout demonstration · archived snapshot · Not investment advice"

ROW_H = 30
HEAD_H = 32


def font(size: int):
    for name in ("segoeui.ttf", "arial.ttf", "msyh.ttc"):
        p = Path(r"C:\Windows\Fonts") / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def draw_table(d, x, y, headers, rows, col_w, fs=12, hfs=13, row_h=ROW_H):
    total = sum(col_w)
    d.rectangle([x, y, x + total, y + HEAD_H], fill=NAVY)
    cx = x
    for h, w in zip(headers, col_w):
        d.text((cx + 7, y + 8), str(h), fill=(255, 255, 255), font=font(hfs))
        cx += w
    y += HEAD_H
    for i, row in enumerate(rows):
        bg = (255, 255, 255) if i % 2 == 0 else ZEBRA
        d.rectangle([x, y, x + total, y + row_h], fill=bg)
        cx = x
        for cell, w in zip(row, col_w):
            s = str(cell)
            limit = max(int(w / 6.4), 6)
            if len(s) > limit:
                s = s[: limit - 1] + "…"
            d.text((cx + 7, y + 8), s, fill=BODY, font=font(fs))
            cx += w
        y += row_h
    d.rectangle([x, y - 1, x + total, y], fill=(214, 220, 226))
    return y + 14


def new_canvas():
    img = Image.new("RGB", (WIDTH, 2400), BG)
    return img, ImageDraw.Draw(img)


def head(d, title, sub):
    d.text((30, 26), title, fill=INK, font=font(30))
    d.text((30, 68), sub, fill=SUB, font=font(14))
    return 106


def section(d, y, text, color=NAVY):
    d.text((30, y), text, fill=color, font=font(16))
    return y + 27


def save_crop(img, y_end, name):
    h = max(y_end + 52, 360)
    out = img.crop((0, 0, WIDTH, h))
    d = ImageDraw.Draw(out)
    d.text((30, h - 32), FOOT, fill=(120, 120, 120), font=font(12))
    OUT.mkdir(parents=True, exist_ok=True)
    out.save(OUT / name)
    print("OK", name, out.size)


# ---------------------------------------------------------------- panel-val
VAL_T1 = (
    ["Name", "Type", "Close", "Read", "PE-q20", "Gap PE", "PB/Px-q20", "Gap",
     "Strict", "Gap S", "Loose", "Driver"],
    [
        ["SYM-A", "etf", "10.20", "Price not in cheap band", "—", "—", "9.40", "-7.8%", "9.40", "-7.8%", "9.40", "price-q20"],
        ["SYM-B", "stock", "22.50", "Cheap-ish, not dual-low", "18.00", "-20.0%", "21.00", "-6.7%", "18.00", "-20.0%", "21.00", "PE"],
        ["SYM-C", "stock", "55.00", "Single-leg extreme, no dual-low", "55.00", "0.0%", "42.00", "-23.6%", "55.00", "0.0%", "55.00", "PE"],
    ],
    [90, 62, 68, 214, 74, 68, 88, 62, 62, 62, 62, 62],
)

VAL_T2 = (
    ["Name", "Close", "Wave stage", "C-low", "Watch band", "Strict", "Cross-read"],
    [
        ["SYM-A", "10.20", "C3 in progress", "10.16", "9.90-10.40", "9.98", "Structure first, valuation band still deep"],
        ["SYM-B", "22.50", "C3 ~1.0x", "22.23", "21.00-24.60", "21.80", "Price above C-low; band below valuation strict"],
        ["SYM-C", "55.00", "C3 ext. 2.0x", "53.25", "37.50-72.50", "50.52", "Structure and valuation band roughly coincide"],
    ],
    [90, 70, 130, 84, 130, 70, 330],
)

VAL_T3 = (
    ["Name", "Close", "PE", "PE pct", "PE band", "PB", "PB pct", "PB band", "Dual-low", "Note"],
    [
        ["SYM-A", "10.20", "—", "—", "ETF: no PE", "—", "—", "ETF: no PB", "—", "price-only proxy"],
        ["SYM-B", "22.50", "18.00", "61.0%", "middle noise zone", "1.20", "32.7%", "cheap", "Y", "PE percentile mid, PB low"],
        ["SYM-C", "55.00", "55.00", "10.2%", "extreme cheap band", "6.80", "53.6%", "middle noise zone", "Y", "PE extreme, PB mid"],
    ],
    [90, 68, 68, 70, 168, 68, 70, 172, 82, 210],
)


def panel_val():
    img, d = new_canvas()
    y = head(d, "Sample panel · Valuation (watchlist-style)",
             "asof 2026-11-06 · archived snapshot · synthetic symbols")
    d.rounded_rectangle([30, 96, WIDTH - 30, 154], radius=10, outline=(200, 205, 210), fill=(255, 252, 240))
    d.text((46, 112), "Layout demo only. Values are synthetic. Not a live book. Not investment advice.",
           fill=(90, 70, 30), font=font(14))
    y = 176
    y = section(d, y, "Valuation read")
    y = draw_table(d, 30, y, *VAL_T1)
    y = section(d, y + 6, "Read vs structure (cross-read)")
    y = draw_table(d, 30, y, *VAL_T2)
    y = section(d, y + 6, "Valuation bands")
    y = draw_table(d, 30, y, *VAL_T3)
    save_crop(img, y, "panel-val.png")


# --------------------------------------------------------------- panel-wave
def wave_chain(anchor: float, width: float):
    c3_1 = anchor - width * 1.0
    c3_1618 = anchor - width * 1.618
    d1128 = anchor - width * 1.128
    d1272 = anchor - width * 1.272
    c4_0382 = c3_1 + width * 0.382
    c4_050 = c3_1 + width * 0.50
    c5_1 = c4_050 - width * 1.0
    c5_1618 = c4_050 - width * 1.618
    fail = c3_1 - width * 0.05
    f = lambda v: f"{v:.2f}"
    return [
        ["C1", f"width {width:.2f} ({anchor:.2f}→{c3_1:.2f})", "—", "base swing", "—"],
        ["C3 cand.", f"1.0×={f(c3_1)} · 1.618×={f(c3_1618)}",
         f"1.128×={f(d1128)} · 1.272×={f(d1272)}", "illustrative", f"fail {f(fail)}"],
        ["C4 cand.", f"0.382×={f(c4_0382)} · 0.50×={f(c4_050)}", "—", "locked until C3 ends", "—"],
        ["C5 cand.", f"1.0×={f(c5_1)} · 1.618×={f(c5_1618)}", "—", "locked until C3 ends", "—"],
        ["Discipline", "Do not preempt C4/C5 before C3 end", "formula kept; k hidden",
         "structure only", "P-weak / P-strong demo"],
    ]


WAVE_SUMMARY = (
    ["Symbol", "Close", "Anchor", "Stage", "Today vs structure", "Next watch"],
    [
        ["SYM-A", "10.20 (+0.6%)", "11.00@M1", "C3 ~1.0x", "Near structure low; no C4 lift", "Wait confirmation"],
        ["SYM-B", "22.50 (+1.0%)", "28.00@M1", "C3 ~1.0x", "Structure low refreshed", "No catch knife"],
        ["SYM-C", "55.00 (-8.0%)", "90.00@M0", "C3 extension", "Broke prior low zone", "Digest; no chase"],
    ],
    [80, 116, 100, 110, 300, 210],
)

WAVE_COLS = (["Block", "Width / candidates", "Dense band", "Select", "Fail / weak / strong"],
             [100, 300, 270, 170, 220])


def panel_wave():
    img, d = new_canvas()
    y = head(d, "Sample panel · Wave structure (multi-block)",
             "asof 2026-11-06 · archived snapshot · Fibonacci multipliers kept (public math)")
    y = section(d, y, "Cross-read summary (synthetic)")
    y = draw_table(d, 30, y, *WAVE_SUMMARY)
    for tag, anchor, width, caption in (
        ("SYM-A", 11.00, 0.80, "projection chain"),
        ("SYM-B", 28.00, 5.50, "projection chain"),
        ("SYM-C", 90.00, 35.00, "projection chain (extension)"),
    ):
        y = section(d, y + 4, f"{tag} · illustrative {caption}")
        y = draw_table(d, 30, y, WAVE_COLS[0], wave_chain(anchor, width), WAVE_COLS[1])
    d.text((30, y + 2), "Note: internal rule IDs omitted. Multipliers 0.382 / 0.50 / 1.0 / 1.618 are public Fibonacci math.",
           fill=(80, 80, 80), font=font(12))
    y += 30
    save_crop(img, y, "panel-wave.png")


# ------------------------------------------------------------- panel-matrix
MATRIX_DETAIL = [
    ["E-01", "Semi materials", "01 AI Compute", "-14.0", "-12.0", "+2.0", "+20.0", "22.0"],
    ["E-02", "AI basket", "01 AI Compute", "-13.0", "-18.0", "-20.0", "-8.0", "12.0"],
    ["E-03", "Semiconductors", "01 AI Compute", "-13.0", "-14.0", "-12.0", "+4.0", "15.0"],
    ["E-04", "Telecom", "01 AI Compute", "-22.0", "-24.0", "-28.0", "-15.0", "8.0"],
    ["E-05", "Cloud compute", "01 AI Compute", "-6.0", "-12.0", "-16.0", "-10.0", "20.0"],
    ["E-06", "Robotics", "02 Humanoid Robotics", "-1.0", "-8.0", "-12.0", "-9.0", "25.0"],
    ["E-07", "Green power", "03 New Energy", "-1.0", "-3.0", "-2.0", "n/a", "48.0"],
    ["E-08", "Battery storage", "03 New Energy", "-7.0", "-12.0", "-25.0", "-18.0", "18.0"],
    ["E-09", "Solar", "03 New Energy", "-2.0", "-9.0", "-22.0", "-14.0", "20.0"],
    ["E-10", "Grid equipment", "03 New Energy", "-8.0", "-13.0", "-20.0", "n/a", "14.0"],
    ["E-11", "Innovative drugs", "04 Biopharma", "-0.2", "+1.0", "+0.2", "+0.8", "55.0"],
    ["E-12", "Chemicals", "09 Allocation", "-5.0", "-8.0", "-18.0", "-10.0", "16.0"],
    ["E-13", "Utilities", "09 Allocation", "+0.3", "-2.0", "-3.0", "+2.0", "30.0"],
    ["E-14", "Consumer", "09 Allocation", "+6.0", "+2.0", "-4.0", "-8.0", "50.0"],
    ["E-15", "Broad beta", "09 Allocation", "-7.0", "-10.0", "-14.0", "-9.0", "12.0"],
    ["E-16", "Dividend style", "09 Allocation", "-1.0", "+2.0", "+1.0", "+8.0", "70.0"],
]

MATRIX_NOTES = {
    "01 AI Compute": "Near-month soft",
    "02 Humanoid Robotics": "Follow-through soft",
    "03 New Energy": "YTD heavy (sample)",
    "04 Biopharma": "Relative resilient",
    "09 Allocation": "Defensive bias",
}


def matrix_agg():
    """Aggregate detail rows per cluster; n/a cells excluded from the mean."""
    buckets = {}
    for row in MATRIX_DETAIL:
        buckets.setdefault(row[2], []).append(row)
    out = []
    for order, (cluster, rows) in enumerate(buckets.items(), 1):
        cells = []
        for idx in (3, 4, 5, 6, 7):
            vals = [float(r[idx]) for r in rows if r[idx] != "n/a"]
            cells.append(f"{sum(vals) / len(vals):+.1f}" if vals else "n/a")
        out.append([cluster, MATRIX_NOTES.get(cluster, ""), str(len(rows))] + cells)
    return out


def panel_matrix():
    img, d = new_canvas()
    y = head(d, "Sample panel · Cross-section matrix",
             "asof 2026-11-06 · archived snapshot · industry labels kept · codes synthetic")
    y = section(d, y, "Cluster aggregates (computed from rows below)")
    y = draw_table(d, 30, y,
                   ["Cluster", "Note", "n", "m1", "m3", "m6", "ytd", "pos"],
                   [c for c in matrix_agg()],
                   [186, 230, 48, 70, 70, 70, 70, 70])
    y = section(d, y + 4, "Constituents")
    y = draw_table(d, 30, y,
                   ["Code", "Short", "Cluster", "m1", "m3", "m6", "ytd", "pos"],
                   MATRIX_DETAIL,
                   [78, 150, 182, 70, 70, 70, 70, 70])
    d.text((30, y + 2), "Note: aggregate rows are the mean of the rows below; n/a cells are excluded. E-* IDs are local to this panel.",
           fill=(80, 80, 80), font=font(12))
    y += 30
    save_crop(img, y, "panel-matrix.png")


# ------------------------------------------------------------- panel-timing
TIMING_WEAK = [
    ["SYM-01", "Name-01", "-28.0", "-5.0", "10.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ["SYM-02", "Name-02", "-26.0", "-12.0", "8.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ["SYM-03", "Name-03", "-22.0", "+8.0", "15.0", "FALL", "Below band, wait", "NO_EXEC"],
    ["SYM-04", "Name-04", "-20.0", "+30.0", "25.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ["SYM-05", "Name-05", "-18.0", "+1.0", "12.0", "FALL", "Near support, watch", "NO_EXEC"],
    ["SYM-06", "Name-06", "-16.0", "-10.0", "9.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ["SYM-07", "Name-07", "-14.0", "+6.0", "7.0", "FALL", "Below band, wait", "NO_EXEC"],
    ["SYM-08", "Name-08", "-12.0", "-20.0", "11.0", "SKIP_ADJ", "Ex-rights, review and avoid", "NO_EXEC"],
    ["SYM-09", "Name-09", "-11.0", "-8.0", "10.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ["SYM-10", "Name-10", "-10.0", "+4.0", "14.0", "FALL", "Near support, watch", "NO_EXEC"],
]

TIMING_STRONG = [
    ["SYM-11", "Name-11", "+40.0", "-10.0", "55.0", "WATCH", "Extended, no chase", "NO_EXEC"],
    ["SYM-12", "Name-12", "+18.0", "-12.0", "45.0", "WATCH", "Watch", "NO_EXEC"],
    ["SYM-13", "Name-13", "+15.0", "-15.0", "35.0", "WATCH", "Watch", "NO_EXEC"],
    ["SYM-14", "Name-14", "+12.0", "-6.0", "60.0", "WATCH", "Extended, no chase", "NO_EXEC"],
    ["SYM-15", "Name-15", "+6.0", "+10.0", "32.0", "WATCH", "Watch", "NO_EXEC"],
    ["SYM-16", "Name-16", "+4.0", "-20.0", "18.0", "TURN", "Low size, small add on corroboration", "NO_EXEC"],
    ["SYM-17", "Name-17", "-0.2", "-18.0", "20.0", "WATCH", "Watch", "NO_EXEC"],
    ["SYM-18", "Name-18", "-1.0", "-22.0", "16.0", "WATCH", "Trend intact, hold watch", "NO_EXEC"],
    ["SYM-19", "Name-19", "-5.0", "-14.0", "12.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ["SYM-20", "Name-20", "-6.0", "-9.0", "15.0", "WATCH", "Watch", "NO_EXEC"],
]

TIMING_COLS = ["code", "name", "m1", "ytd", "pos", "state", "judge", "gate"]
TIMING_W = [80, 92, 68, 68, 58, 86, 300, 86]


def panel_timing():
    img, d = new_canvas()
    y = head(d, "Sample panel · Timing dual-cluster",
             "asof 2026-11-06 · archived snapshot · state machine kept · names synthetic")
    d.text((30, 96), "Weak leg: sector ETF (cluster soft)     Strong leg: theme ETF (cluster firmer)",
           fill=(60, 60, 60), font=font(14))
    d.text((30, 120), "SYM-* IDs are local to this panel.", fill=(110, 110, 110), font=font(12))
    y = 148
    y = section(d, y, "Weak cluster", (140, 50, 40))
    y = draw_table(d, 30, y, TIMING_COLS, TIMING_WEAK, TIMING_W)
    y = section(d, y + 4, "Strong cluster", (40, 110, 70))
    y = draw_table(d, 30, y, TIMING_COLS, TIMING_STRONG, TIMING_W)
    save_crop(img, y, "panel-timing.png")


def main():
    panel_val()
    panel_wave()
    panel_matrix()
    panel_timing()
    print("DONE")


if __name__ == "__main__":
    main()
