"""SSRF guard for the optional public RPC read."""

from __future__ import annotations

import ipaddress
import socket
from urllib.parse import urlparse


def is_public_url(url: str) -> bool:
    """Accept HTTPS only when every resolved address is globally routable."""
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        return False
    try:
        addresses = {
            ipaddress.ip_address(item[4][0])
            for item in socket.getaddrinfo(parsed.hostname, parsed.port or 443)
        }
    except (OSError, ValueError):
        # Fail closed: an unresolved name cannot be proven public.
        return False
    return bool(addresses) and all(address.is_global for address in addresses)
