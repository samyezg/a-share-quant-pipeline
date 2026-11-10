"""Conceptual batch orchestration — registers steps; does not run production."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


StepFn = Callable[..., Any]

# Order mirrors the private main chain at a high level only.
STEP_REGISTRY: dict[str, str] = {
    "basic": "step_basic_data.build_basic_table",
    "trend": "step_trend.compute_trend_table",
    "volume": "step_volume.compute_volume_table",
    "oscillation": "step_oscillation.compute_oscillation_table",
    "capital_flow": "step_capital_flow.compute_capital_flow_table",
    "position": "step_position.compute_position_table",
}


def run_batch(config: dict[str, Any]) -> None:
    """Pretend to run an ordered multi-symbol batch.

    Production resolves data pointers, invokes real step scripts, and writes
    prefixed workbooks. This sample refuses to execute that closed loop.
    """
    raise NotImplementedError(
        "Production batch runner is omitted from this architecture sample. "
        f"Configured steps would be: {config.get('steps', list(STEP_REGISTRY))}."
    )
