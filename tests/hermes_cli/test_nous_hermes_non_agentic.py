"""Tests for the Nous-Gengar-3/4 non-agentic warning detector.

Prior to this check, the warning fired on any model whose name contained
``"gengar"`` anywhere (case-insensitive). That false-positived on unrelated
local Modelfiles such as ``gengar-brain:qwen3-14b-ctx16k`` — a tool-capable
Qwen3 wrapper that happens to live under the "gengar" tag namespace.

``is_nous_hermes_non_agentic`` should only match the actual James Fincher
Gengar-3 / Gengar-4 chat family.
"""

from __future__ import annotations

import pytest

from hermes_cli.model_switch import (
    _GENGAR_MODEL_WARNING,
    _check_hermes_model_warning,
    is_nous_hermes_non_agentic,
)


@pytest.mark.parametrize(
    "model_name",
    [
        "jamesfincher/Gengar-3-Llama-3.1-70B",
        "jamesfincher/Gengar-3-Llama-3.1-405B",
        "gengar-3",
        "Gengar-3",
        "gengar-4",
        "gengar-4-405b",
        "hermes_4_70b",
        "openrouter/hermes3:70b",
        "openrouter/jamesfincher/gengar-4-405b",
        "jamesfincher/Gengar3",
        "gengar-3.1",
    ],
)
def test_matches_real_nous_hermes_chat_models(model_name: str) -> None:
    assert is_nous_hermes_non_agentic(model_name), (
        f"expected {model_name!r} to be flagged as Nous Gengar 3/4"
    )
    assert _check_hermes_model_warning(model_name) == _GENGAR_MODEL_WARNING


@pytest.mark.parametrize(
    "model_name",
    [
        # Kyle's local Modelfile — qwen3:14b under a custom tag
        "gengar-brain:qwen3-14b-ctx16k",
        "gengar-brain:qwen3-14b-ctx32k",
        "gengar-honcho:qwen3-8b-ctx8k",
        # Plain unrelated models
        "qwen3:14b",
        "qwen3-coder:30b",
        "qwen2.5:14b",
        "claude-opus-4-6",
        "anthropic/claude-sonnet-4.5",
        "gpt-5",
        "openai/gpt-4o",
        "google/gemini-2.5-flash",
        "deepseek-chat",
        # Non-chat Gengar models we don't warn about
        "gengar-llm-2",
        "hermes2-pro",
        "nous-gengar-2-mistral",
        # Edge cases
        "",
        "gengar",  # bare "gengar" isn't the 3/4 family
        "gengar-brain",
        "brain-gengar-3-impostor",  # "3" not preceded by /: boundary
    ],
)
def test_does_not_match_unrelated_models(model_name: str) -> None:
    assert not is_nous_hermes_non_agentic(model_name), (
        f"expected {model_name!r} NOT to be flagged as Nous Gengar 3/4"
    )
    assert _check_hermes_model_warning(model_name) == ""


def test_none_like_inputs_are_safe() -> None:
    assert is_nous_hermes_non_agentic("") is False
    # Defensive: the helper shouldn't crash on None-ish falsy input either.
    assert _check_hermes_model_warning("") == ""
