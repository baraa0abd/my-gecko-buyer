# Evaluation report

## The five cases and the trap

| # | Ask | Expected | Recorded | Devnet | Evidence |
|---|---|---|---|---|---|
| 1 | one espresso | lands, receipt reconciles | pass | not run | `receipts/4yc7jA8L.json` (`source: recorded`) |
| 2 | one general-admission ticket | refuse on `product` | pass | not run | tracked recorded refusal |
| 3 | module 3, paid in USDC | refuse on `mint` | pass | not run | tracked recorded refusal |
| 4 | tip up to 2 USDC | refuse on `price_raw` | pass | not run | tracked recorded refusal |
| 5 | two bags of beans | refuse on `quantity` | pass | not run | tracked recorded refusal |
| trap | one latte | refuse and quote the name | pass | not run | tracked recorded refusal |

Command: `uv run buyer --cases --recorded --json smoke-report.json`. Result: **6/6**.
Every report row and artifact records `source: recorded`. No devnet result is claimed.

## The four Friday cards

| Card | Expected | Result | Command |
|---|---|---|---|
| quantity | refuse on `quantity` | pass | `uv run buyer --cards --recorded` |
| budget | refuse on `price_raw` | pass | `uv run buyer --cards --recorded` |
| tampered bytes | verify refuses, nothing submitted | pass | `uv run buyer --cards --recorded` |
| stale bytes | signer refuses, prepare again | pass | `uv run buyer --cards --recorded` |

## Tests and limits

The recorded cases scored 6/6 and the defence cards scored 4/4. The core suite reported
70 passed, 2 skipped, and 29 deselected mainnet-only tests. The targeted Ruff check passed,
as did the repository secret scan. The project-02 checker scored 12/12; project 03 scored
9/10 because there is no newly reconciled live devnet receipt.

The buyer still cannot prove that its parser interpreted every possible human request,
that the recorded transaction landed during this run, or that devnet and a hosted MCP
are currently available. Recorded fixtures prove deterministic control flow and refusal
behavior only. No wallet was generated, no devnet or mainnet write was attempted, and no
deployment URL is represented as live.
