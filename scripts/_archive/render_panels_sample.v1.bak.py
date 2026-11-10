# -*- coding: utf-8 -*-
"""Synthetic English sample panels for public portfolio (scheme B)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "G github" / "docs" / "photos" / "panels"
LOCAL = ROOT / "P photo" / "05-panels-sample"
FOOT = "Sample data for layout demonstration · archived snapshot · Not investment advice"


def font(size: int):
    for name in ("segoeui.ttf", "arial.ttf", "msyh.ttc"):
        p = Path(r"C:\Windows\Fonts") / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def draw_table(d, x, y, headers, rows, col_w, row_h=28):
    cx = x
    d.rectangle([x, y, x + sum(col_w), y + row_h], fill=(30, 58, 95))
    for h, w in zip(headers, col_w):
        d.text((cx + 6, y + 6), str(h), fill=(255, 255, 255), font=font(12))
        cx += w
    y += row_h
    for i, row in enumerate(rows):
        bg = (255, 255, 255) if i % 2 == 0 else (238, 242, 246)
        d.rectangle([x, y, x + sum(col_w), y + row_h], fill=bg)
        cx = x
        for cell, w in zip(row, col_w):
            s = str(cell)
            if len(s) > 42:
                s = s[:40] + "…"
            d.text((cx + 6, y + 6), s, fill=(35, 45, 55), font=font(11))
            cx += w
        y += row_h
    return y + 16


def save(img: Image.Image, name: str):
    OUT.mkdir(parents=True, exist_ok=True)
    LOCAL.mkdir(parents=True, exist_ok=True)
    p1 = OUT / name
    p2 = LOCAL / name
    img.save(p1)
    img.save(p2)
    print("OK", p1)


def panel_val():
    img = Image.new("RGB", (1600, 900), (248, 249, 251))
    d = ImageDraw.Draw(img)
    d.text((40, 28), "Sample panel · Valuation (watchlist-style)", fill=(20, 30, 45), font=font(28))
    d.text((40, 68), "asof 2026-11-06 · archived snapshot · synthetic symbols", fill=(90, 100, 110), font=font(14))
    d.rounded_rectangle([40, 100, 1560, 170], radius=10, outline=(200, 205, 210), fill=(255, 252, 240))
    d.text((56, 118), "Layout demo only. Values are synthetic. Not a live book. Not investment advice.", fill=(90, 70, 30), font=font(14))
    headers = ["Name", "Type", "Close", "Read", "PE→q20", "Gap PE", "PB/Px→q20", "Gap", "Strict", "Gap S", "Loose", "Driver"]
    rows = [
        ["SYM-A", "etf", "10.20", "Price not in cheap band", "—", "—", "9.40", "-7.8%", "9.40", "-7.8%", "9.40", "price-q20"],
        ["SYM-B", "stock", "22.50", "Cheap-ish, not dual-low", "18.00", "-20.0%", "21.00", "-6.7%", "18.00", "-20.0%", "21.00", "PE"],
        ["SYM-C", "stock", "55.00", "Single-leg extreme, not dual-low", "55.00", "0.0%", "42.00", "-23.6%", "55.00", "0.0%", "55.00", "PE"],
    ]
    draw_table(d, 40, 190, headers, rows, [100, 70, 70, 200, 80, 70, 90, 70, 70, 70, 70, 90])
    d.text((40, 860), FOOT, fill=(120, 120, 120), font=font(12))
    save(img, "panel-val.png")


def panel_wave():
    img = Image.new("RGB", (1600, 1400), (248, 249, 251))
    d = ImageDraw.Draw(img)
    d.text((40, 28), "Sample panel · Wave structure (multi-block)", fill=(20, 30, 45), font=font(28))
    d.text((40, 68), "asof 2026-11-06 · archived snapshot · Fibonacci multipliers kept (public math)", fill=(90, 100, 110), font=font(14))
    y = 110
    # summary 3-row
    d.text((40, y), "Cross-read summary (synthetic)", fill=(30, 58, 95), font=font(16))
    y += 28
    y = draw_table(
        d,
        40,
        y,
        ["Symbol", "Close", "Anchor", "Stage", "Today vs structure", "Next watch"],
        [
            ["SYM-A", "10.20 (+0.6%)", "11.00@M1", "C3↓ ~1.0x", "Near structure low; no C4 lift", "Wait confirmation"],
            ["SYM-B", "22.50 (+1.0%)", "28.00@M1", "C3↓ ~1.6x", "Structure low refreshed", "No catch knife"],
            ["SYM-C", "55.00 (−8.0%)", "90.00@M0", "C3↓ extension", "Broke prior low zone", "Digest; no chase"],
        ],
        [100, 120, 110, 120, 280, 200],
    )
    # C1 block style
    d.text((40, y), "SYM-A · illustrative projection chain", fill=(30, 58, 95), font=font(16))
    y += 28
    y = draw_table(
        d,
        40,
        y,
        ["Block", "Width / candidates", "Dense band", "Select", "Fail / weak / strong"],
        [
            ["C1", "width 0.80 (11.00→10.20)", "—", "base swing", "—"],
            ["C3 cand.", "1.0×=10.20 · 1.618×=9.70", "1.128×=10.10 · 1.272×=9.98", "illustrative", "fail 10.05"],
            ["C4 cand.", "0.382×=10.50 · 0.50×=10.60", "—", "locked until C3 ends", "—"],
            ["C5 cand.", "1.0×=9.90 · 1.618×=9.40", "—", "locked until C3 ends", "—"],
            ["Discipline", "Do not preempt C4/C5 before C3 end", "formula kept; k hidden", "structure only", "P-weak / P-strong demo"],
        ],
        [110, 320, 280, 200, 220],
    )
    d.text((40, y), "Note: internal rule IDs omitted. Multipliers 0.382 / 0.50 / 1.0 / 1.618 are public Fibonacci math.", fill=(80, 80, 80), font=font(13))
    d.text((40, 1360), FOOT, fill=(120, 120, 120), font=font(12))
    save(img, "panel-wave.png")


def panel_matrix():
    img = Image.new("RGB", (1600, 1200), (248, 249, 251))
    d = ImageDraw.Draw(img)
    d.text((40, 28), "Sample panel · Cross-section matrix", fill=(20, 30, 45), font=font(28))
    d.text((40, 68), "asof 2026-11-06 · archived snapshot · industry labels kept · codes synthetic", fill=(90, 100, 110), font=font(14))
    y = 110
    y = draw_table(
        d,
        40,
        y,
        ["Cluster", "Note", "n", "m1", "m3", "m6", "ytd", "pos"],
        [
            ["01 AI Compute", "Near-month soft", "5", "-12.0", "-15.0", "-10.0", "-2.0", "18.0"],
            ["02 Humanoid Robotics", "Follow-through soft", "1", "-1.0", "-8.0", "-12.0", "-9.0", "25.0"],
            ["03 New Energy", "YTD heavy (sample)", "4", "-5.0", "-9.0", "-18.0", "-16.0", "30.0"],
            ["04 Biopharma", "Relative resilient", "1", "+0.5", "+1.0", "+0.2", "+1.5", "55.0"],
            ["09 Allocation", "Defensive bias · internal mix", "5", "-2.0", "-4.0", "-8.0", "-3.0", "40.0"],
        ],
        [180, 220, 50, 70, 70, 70, 70, 70],
    )
    rows = [
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
    y = draw_table(
        d,
        40,
        y,
        ["Code", "Short", "Cluster", "m1", "m3", "m6", "ytd", "pos"],
        rows,
        [80, 140, 180, 70, 70, 70, 70, 70],
    )
    d.text((40, 1160), FOOT, fill=(120, 120, 120), font=font(12))
    save(img, "panel-matrix.png")


def panel_timing():
    img = Image.new("RGB", (1600, 1300), (248, 249, 251))
    d = ImageDraw.Draw(img)
    d.text((40, 28), "Sample panel · Timing dual-cluster", fill=(20, 30, 45), font=font(28))
    d.text((40, 68), "asof 2026-11-06 · archived snapshot · state machine kept · names synthetic", fill=(90, 100, 110), font=font(14))
    d.text((40, 100), "Weak leg: E-01 Sector ETF (cluster soft)    Strong leg: E-06 Theme ETF (cluster firmer)", fill=(60, 60, 60), font=font(14))
    y = 140
    d.text((40, y), "Weak cluster", fill=(140, 50, 40), font=font(18))
    y += 28
    weak = [
        ["SYM-01", "Name-01", "-28.0", "-5.0", "10.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-02", "Name-02", "-26.0", "-12.0", "8.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-03", "Name-03", "-22.0", "+8.0", "15.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-04", "Name-04", "-20.0", "+30.0", "25.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-05", "Name-05", "-18.0", "+1.0", "12.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-06", "Name-06", "-16.0", "-10.0", "9.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-07", "Name-07", "-14.0", "+6.0", "7.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-08", "Name-08", "-12.0", "-20.0", "11.0", "SKIP_ADJ", "Corporate action review", "NO_EXEC"],
        ["SYM-09", "Name-09", "-11.0", "-8.0", "10.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-10", "Name-10", "-10.0", "+4.0", "14.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
    ]
    y = draw_table(d, 40, y, ["code", "name", "m1", "ytd", "pos", "state", "judge", "gate"], weak, [90, 100, 70, 70, 60, 90, 220, 90])
    d.text((40, y), "Strong cluster", fill=(40, 110, 70), font=font(18))
    y += 28
    strong = [
        ["SYM-11", "Name-11", "+40.0", "-10.0", "55.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-12", "Name-12", "+18.0", "-12.0", "45.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-13", "Name-13", "+15.0", "-15.0", "35.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-14", "Name-14", "+12.0", "-6.0", "60.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-15", "Name-15", "+6.0", "+10.0", "32.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-16", "Name-16", "+4.0", "-20.0", "18.0", "TURN", "Low size, small add on corroboration", "NO_EXEC"],
        ["SYM-17", "Name-17", "-0.2", "-18.0", "20.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-18", "Name-18", "-1.0", "-22.0", "16.0", "WATCH", "Watch", "NO_EXEC"],
        ["SYM-19", "Name-19", "-5.0", "-14.0", "12.0", "FALL", "Sharp drop, no entry", "NO_EXEC"],
        ["SYM-20", "Name-20", "-6.0", "-9.0", "15.0", "WATCH", "Watch", "NO_EXEC"],
    ]
    y = draw_table(d, 40, y, ["code", "name", "m1", "ytd", "pos", "state", "judge", "gate"], strong, [90, 100, 70, 70, 60, 90, 280, 90])
    d.text((40, 1260), FOOT, fill=(120, 120, 120), font=font(12))
    save(img, "panel-timing.png")


def main():
    panel_val()
    panel_wave()
    panel_matrix()
    panel_timing()
    print("DONE")


if __name__ == "__main__":
    main()
