# Architecture summary

Public portfolio rewrite. **Not** a dump of the private course tree.

## Intent

Build a **repeatable A-share research pipeline**:

1. Land daily quotes + capital-flow style inputs into a basic table.
2. Compute multi-dimension technical overlays (trend, volume, oscillation, capital flow, price position).
3. Attach fundamental / valuation / stage-model layers where configured.
4. Emit operation / risk tables and multi-symbol summaries for human review.
5. Gate research on a **local warehouse** completeness story; keep realtime monitor / news / mobile alerts as side systems.

## Conceptual main chain

```text
data pointers / warehouse
        ↓
  basic table (OHLCV + flow fields)
        ↓
  dimension steps (trend / volume / oscillation / ATR / capital / position)
        ↓
  resonance / risk tables / stage & grid overlays
        ↓
  fundamental risk-return & valuation overlays
        ↓
  multi-symbol summary / research exports
```

Batch orchestration (concept): register ordered steps → resolve per-symbol config → write prefixed workbook outputs under a data folder. **Production runners are omitted here.**

## Dimensions (names only)

| Dimension | Examples of concerns (production; not implemented in this sample) |
|:---|:---|
| Trend | Moving averages, MACD-family, BBI-style composites |
| Volume | Volume ratio, price-volume alignment, OBV-family |
| Oscillation | KDJ / RSI / WR style oscillators |
| Capital flow | Flow-score style overlays |
| Position | Range / Fibonacci / Bollinger-style location scores |
| Fundamental overlays | Forecast-derived scores, risk scores, valuation bands |
| Stage models | Stage framing research overlays |

## Side systems (boundaries)

See [`docs/module-map.md`](./docs/module-map.md). Highlights:

| Subsystem | Role in the full workspace | In this repo |
|:---|:---|:---|
| Local data warehouse | SQLite / folder audit, gap & completeness | Interface stub only |
| Formal backtest | Separate L2 research package | Map only |
| Intraday monitor / news | Live side paths + optional messaging | Map only |
| Flutter stock alert app | Shipped product sample | External link only |

## External dependencies in practice

For real A-share use, the private system typically needs:

- **Market-data APIs** — daily quotes, fundamentals / valuation inputs (vendor-specific credentials stay local)
- **Optional messaging** — alert / digest delivery channels (tokens never shipped)
- **Optional research-document inputs** — knowledge-base or report-side feeds for environment notes (credentials never shipped)

Public A-share market context may reference widely known terminals or data vendors in prose; this sample does **not** embed product keys, endpoint secrets, or private integration playbooks.

## Deliberate omissions

- Full Python step implementations and private rule constants
- Credentials for market-data, messaging, and internal research APIs
- Warehouse databases and Excel/Parquet artifacts
- Absolute machine paths from the author’s workstation
- Duplication of [stock-alert-assistant](https://github.com/samyezg/stock-alert-assistant)

## Sample code policy

- `skeleton/stubs/step_*.py` — signatures + docs; raise `NotImplementedError`
- `skeleton/stubs/toy_ma.py` — tiny educational MA on fake CSV; **≠** production rules
- `docs/photos/panels/` — **synthetic** layout demos; not production books
