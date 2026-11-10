# Portfolio photos

| Path | Notes |
|:---|:---|
| `architecture/` | System overview + module boundaries (illustrative) |
| `pipeline/` | Conceptual step strip (names only) |
| `panels/` | **Synthetic** English sample panels for layout demonstration |
| `charts/` | **Synthetic** chart forms: index-level wave schematics + valuation percentile bars |

## Panels (scheme B)

| File | Demonstrates |
|:---|:---|
| `panel-val.png` | Valuation-style watchlist table layout |
| `panel-wave.png` | Wave-structure multi-block layout (Fibonacci multipliers as public math only) |
| `panel-matrix.png` | Cross-section industry matrix layout |
| `panel-timing.png` | Dual-cluster timing layout + generic state machine |

## Charts (synthetic forms)

| File | Demonstrates |
|:---|:---|
| `panel-wave-schematic.png` | Index-level A->B->C1->C2->C3 polyline + label table (form only) |
| `panel-val-percentile.png` | PE vs PB percentile horizontal bars |

Symbols (`SYM-*`, `SYM-IDX-*`, `E-*`) and numeric cells are **fabricated**.  
Footer on each panel: *Sample data for layout demonstration · archived snapshot · Not investment advice*.

Regenerate:

```text
python scripts/render_panels_sample.py
python scripts/render_charts_sample.py
```

Private source-faithful PDF packs (not public default) live under the course tree  
`artifacts/canvases/_exports/pdf/` — do not copy those into this repo slice.
