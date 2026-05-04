# Langfuse Observability Plugin

This plugin ships bundled with Gengar but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

Pick one:

```bash
# Interactive: walks you through credentials + SDK install + enable
gengar tools  # → Langfuse Observability

# Manual
pip install langfuse
gengar plugins enable observability/langfuse
```

## Required credentials

Set these in `~/.gengar/.env` (or via `gengar tools`):

```bash
GENGAR_LANGFUSE_PUBLIC_KEY=pk-lf-...
GENGAR_LANGFUSE_SECRET_KEY=sk-lf-...
GENGAR_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

## Verify

```bash
gengar plugins list                 # observability/langfuse should show "enabled"
gengar chat -q "hello"              # then check Langfuse for a "Gengar turn" trace
```

## Optional tuning

```bash
GENGAR_LANGFUSE_ENV=production       # environment tag
GENGAR_LANGFUSE_RELEASE=v1.0.0       # release tag
GENGAR_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
GENGAR_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
GENGAR_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Disable

```bash
gengar plugins disable observability/langfuse
```
