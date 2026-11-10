"""Price-position dimension stub (range / Fibonacci / band-style location)."""

from __future__ import annotations

from pathlib import Path


def compute_position_table(basic_table: Path, out_dir: Path) -> Path:
    """Compute price-position overlays from the basic table in production."""
    raise NotImplementedError(
        "Production position engine is omitted from this architecture sample."
    )
