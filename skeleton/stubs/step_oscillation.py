"""Oscillation dimension stub (KDJ / RSI / WR style concerns)."""

from __future__ import annotations

from pathlib import Path


def compute_oscillation_table(basic_table: Path, out_dir: Path) -> Path:
    """Compute oscillation overlays from the basic table in production."""
    raise NotImplementedError(
        "Production oscillation engine is omitted from this architecture sample."
    )
