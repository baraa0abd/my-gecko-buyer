# The buyer signs only when seven fields match the pinned intent

## Status and date

accepted, 2026-10-05

## Context

The buyer controls a key that can move the full pinned budget. Gecko prepares unsigned bytes, so the buyer must independently decide whether those bytes express the pinned request.

## Decision

Before signing, compare the prepared transaction with `intents/<file>.json` and refuse on the first mismatch, naming both values.

| Field | Compared how | Why this one |
|---|---|---|
| program | exact IDL program address; no extra non-plumbing program | prevents a substituted instruction or hidden program call |
| store | PDA derived from the pinned store name | rejects similar names and swapped store accounts |
| product | exact product string | prevents a different item, including VIP-for-general-admission substitution |
| price_raw | whole integer at or below budget | caps the amount that may leave the buyer |
| mint | exact address | token symbols are labels and cannot identify an asset |
| quantity | exact integer | one prepared unit cannot satisfy a request for two |
| destination | derived authority token account for the pinned mint | prevents payment redirection |
| signed bytes | Gecko verification before submission | catches signer substitution and tampering |

## What this forbids

No partial matches, floating-point prices, symbol-based mint checks, unchanged retries after refusal, signing without a passing simulation, signing stale bytes, re-signing a retry, or submitting before signed-byte verification.

## What I left out, and why

The buyer does not infer the person's real-world intent beyond the small parser. The pin is the boundary; adding model inference would make the decision less deterministic.

## What would reverse this

A verified protocol binding that cryptographically covers a field and is enforced by the signer could make the duplicate local check unnecessary. Removal requires an adversarial regression test showing the signer still refuses a substituted value.

## What this does not prove

That the pin was right. The buyer faithfully signs a wrong request.
