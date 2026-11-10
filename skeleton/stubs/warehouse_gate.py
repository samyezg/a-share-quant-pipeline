"""Local warehouse quality-gate interface (completeness / gap checks)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class GateReport:
    ok: bool
    missing_symbols: tuple[str, ...]
    notes: str = ""


def check_completeness(symbols: Sequence[str], asof: str) -> GateReport:
    """Return whether required series exist for ``asof`` in production."""
    raise NotImplementedError(
        "Production warehouse gate is omitted from this architecture sample."
    )
