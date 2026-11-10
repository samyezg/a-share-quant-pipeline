"""Teaching moving-average demo on fake CSV bars.

Deliberately NOT the production five-dimension indicator engine.
"""

from __future__ import annotations

import csv
from pathlib import Path


def simple_ma(closes: list[float], window: int) -> list[float | None]:
    out: list[float | None] = []
    for i in range(len(closes)):
        if i + 1 < window:
            out.append(None)
        else:
            chunk = closes[i + 1 - window : i + 1]
            out.append(sum(chunk) / window)
    return out


def main() -> None:
    csv_path = Path(__file__).resolve().parents[1] / "samples" / "toy_ohlcv.csv"
    dates: list[str] = []
    closes: list[float] = []
    with csv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row["date"])
            closes.append(float(row["close"]))
    ma5 = simple_ma(closes, 5)
    print("toy_ma demo (fake bars; not production rules)")
    print(f"{'date':12} {'close':>8} {'ma5':>8}")
    for d, c, m in zip(dates, closes, ma5, strict=True):
        m_s = f"{m:.4f}" if m is not None else "-"
        print(f"{d:12} {c:8.2f} {m_s:>8}")


if __name__ == "__main__":
    main()
