"""Step 2 concept: build a basic OHLCV + flow table.

Production reads quote / fund-flow workbooks and writes a prefixed basic table.
This stub documents the boundary only.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def build_basic_table(data_source: dict[str, Any], out_dir: Path) -> Path:
    """Return path to a basic table workbook in production.

    Parameters
    ----------
    data_source:
        Pointers such as daily quote path, fund-flow path, sheet names.
    out_dir:
        Destination folder for prefixed Excel outputs.
    """
    raise NotImplementedError(
        "Production basic-table builder is omitted from this architecture sample."
    )
