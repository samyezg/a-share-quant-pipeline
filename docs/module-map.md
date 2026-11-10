# Module map (boundaries only)

This page describes **subsystem boundaries** in the full private workspace.  
Implementations, databases, and credentials are **not** in this repository.

## Local data warehouse

- **Purpose:** Persist daily bars / fund-flow style series; audit folder layout; completeness & gap checks before research runs.
- **Consumers:** Pipeline batch jobs, valuation helpers, offline charts.
- **Not here:** SQLite files, fetch scripts with live tokens, production audit logs.

## Formal backtest (L2 research)

- **Purpose:** Event / rule evaluation on historical series; separate from the daily Excel-oriented main chain.
- **Boundary:** Research package with its own runners and reports.
- **Not here:** Full backtest engines, large result trees, parameter grids.

## Intraday monitor side path

- **Purpose:** Watchlist-oriented live or near-live polling, plan/digest hooks, optional messaging.
- **Boundary:** Shares *concepts* with the alert app, but PC/monitor runtime stays private.
- **Not here:** Monitor services, real watchlists, webhook secrets.

## News / briefing side path

- **Purpose:** Ingest and format market news / digests for human review (optional image delivery).
- **Boundary:** Independent pipeline; must not embed API keys in source.
- **Not here:** Prompt packs with secrets, raw news caches, bot tokens.

## Flutter stock alert app

- **Purpose:** Shipped A-share watchlist alert product (local notifications).
- **Public sample:** https://github.com/samyezg/stock-alert-assistant  
- **Not here:** Dart sources, Android/iOS projects (already omitted in that repo as well).

## How to read this map

| You see in this sample | You do **not** get |
|:---|:---|
| Names + responsibility lines | Runnable production modules |
| Example JSON pointers | Real market data or keys |
| Stub interfaces | Closed-loop trading automation |
