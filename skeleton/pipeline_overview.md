# Pipeline overview (conceptual)

Ordered research steps in the private workspace (names only).  
**None of these full scripts are shipped in this sample.**

| Step | Concern |
|:---:|:---|
| 1 | Optional interactive data-source pointer |
| 2 | Build basic table from quotes + fund-flow style inputs |
| 2.1 | Forecast-derived / Z-style risk overlays |
| 3 | Trend dimension |
| 4 | Volume dimension |
| 5 | Oscillation dimension |
| 6 | ATR / volatility helpers |
| 7 | Capital-flow dimension |
| 8 | Price-position dimension |
| 9 | Buy/sell resonance composite |
| 10–11 | Short / medium operation risk tables |
| 12–13 | Market stage / grid overlays |
| 14 | Combined snapshot exports |
| 15–16 | Fundamental risk-return & valuation |
| 17 | Stage-model (e.g. Weinstein-style) research overlay |
| 18 | Multi-symbol summary |

Batch runners resolve per-symbol prefixes and write workbooks under a data folder.  
This repository only keeps **stubs** under `stubs/` plus a toy MA demo.
