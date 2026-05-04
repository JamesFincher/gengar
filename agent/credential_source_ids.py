"""Shared credential source identifiers and legacy aliases."""

from __future__ import annotations

SOURCE_MANUAL = "manual"

ANTHROPIC_PKCE_SOURCE = "gengar_pkce"
LEGACY_ANTHROPIC_PKCE_SOURCE = "her" "mes_pkce"
ANTHROPIC_PKCE_SOURCES = {
    ANTHROPIC_PKCE_SOURCE,
    LEGACY_ANTHROPIC_PKCE_SOURCE,
}


def manual_source(source: str) -> str:
    return f"{SOURCE_MANUAL}:{source}"


def is_anthropic_pkce_source(source: str) -> bool:
    raw = str(source or "")
    if raw.startswith(f"{SOURCE_MANUAL}:"):
        raw = raw.split(":", 1)[1]
    return raw in ANTHROPIC_PKCE_SOURCES


def current_source_for(source: str) -> str:
    raw = str(source or "")
    if raw == LEGACY_ANTHROPIC_PKCE_SOURCE:
        return ANTHROPIC_PKCE_SOURCE
    legacy_manual = manual_source(LEGACY_ANTHROPIC_PKCE_SOURCE)
    if raw == legacy_manual:
        return manual_source(ANTHROPIC_PKCE_SOURCE)
    return raw
