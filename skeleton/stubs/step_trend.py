"""Trend dimension stub (MA / MACD-family / BBI-style concerns)."""

from __future__ import annotations

from pathlib import Path


def compute_trend_table(basic_table: Path, out_dir: Path) -> Path:
    """Compute trend overlays from the basic table in production."""
    raise NotImplementedError(
        "Production trend engine is omitted from this architecture sample."
    )
