"""Volume dimension stub (volume ratio / price-volume / OBV-family)."""

from __future__ import annotations

from pathlib import Path


def compute_volume_table(basic_table: Path, out_dir: Path) -> Path:
    """Compute volume overlays from the basic table in production."""
    raise NotImplementedError(
        "Production volume engine is omitted from this architecture sample."
    )
