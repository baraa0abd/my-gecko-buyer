# Deployment and rollback

The keyless MCP endpoint is designed for `https://example.invalid/gecko-check` once a host is selected. Deployment was not claimed during the recorded-only build.

The exposed `check_purchase` call accepts an intent and prepared answer, runs the same seven checks as the buyer, and returns `passed`, `field`, `asked`, and `found`. It refuses private or non-HTTPS `rpc_url` values before any fetch.

Redeploy with the chosen host's normal deployment command after tests and `scripts/scan_secrets.py` pass. If it is unavailable during the defence, run `uv run buyer --cases --recorded`; this exercises the same buyer and checks with the recorded transport.
