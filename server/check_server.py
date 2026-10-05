"""A keyless MCP server exposing the buyer's refusal boundary."""

from __future__ import annotations

from typing import Any

from mcp.server.mcpserver import MCPServer

from buyer.check import check_all
from buyer.intent import IntentRecord
from buyer.prepared import Prepared
from server.guard import is_public_url

mcp = MCPServer("gecko-purchase-check")


@mcp.tool()
def check_purchase(
    intent: dict[str, Any], prepared_answer: dict[str, Any], rpc_url: str | None = None
) -> dict[str, Any]:
    """Check seven prepared-purchase fields without loading a key or signing."""
    if rpc_url is not None and not is_public_url(rpc_url):
        return {
            "passed": False,
            "field": "rpc_url",
            "asked": "a public HTTPS URL",
            "found": rpc_url,
        }
    verdict = check_all(IntentRecord(**intent), Prepared.from_answer(prepared_answer))
    refusal = verdict.refusal
    return {
        "passed": verdict.passed,
        "field": refusal.field if refusal else None,
        "asked": refusal.asked if refusal else None,
        "found": refusal.found if refusal else None,
        "checks": [result.line() for result in verdict.results],
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
