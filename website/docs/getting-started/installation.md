---
sidebar_position: 2
title: "Installation"
description: "Install Gengar on Linux, macOS, WSL2, or Android via Termux"
---

# Installation

Get Gengar up and running in under two minutes with the one-line installer.

## Quick Install

### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/jamesfincher/gengar/main/scripts/install.sh | bash
```

### Android / Termux

Gengar now ships a Termux-aware installer path too:

```bash
curl -fsSL https://raw.githubusercontent.com/jamesfincher/gengar/main/scripts/install.sh | bash
```

The installer detects Termux automatically and switches to a tested Android flow:
- uses Termux `pkg` for system dependencies (`git`, `python`, `nodejs`, `ripgrep`, `ffmpeg`, build tools)
- creates the virtualenv with `python -m venv`
- exports `ANDROID_API_LEVEL` automatically for Android wheel builds
- installs a curated `.[termux]` extra with `pip`
- skips the untested browser / WhatsApp bootstrap by default

If you want the fully explicit path, follow the dedicated [Termux guide](./termux.md).

:::warning Windows
Native Windows is **not supported**. Please install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and run Gengar from there. The install command above works inside WSL2.
:::

### What the Installer Does

The installer handles everything automatically — all dependencies (Python, Node.js, ripgrep, ffmpeg), the repo clone, virtual environment, global `gengar` command setup, and LLM provider configuration. By the end, you're ready to chat.

#### Install Layout

Where the installer puts things depends on whether you're installing as a normal user or as root:

| Installer | Code lives at | `gengar` binary | Data directory |
|---|---|---|---|
| Per-user (normal) | `~/.gengar/gengar/` | `~/.local/bin/gengar` (symlink) | `~/.gengar/` |
| Root-mode (`sudo curl … \| sudo bash`) | `/usr/local/lib/gengar/` | `/usr/local/bin/gengar` | `/root/.gengar/` (or `$GENGAR_HOME`) |

The root-mode **FHS layout** (`/usr/local/lib/…`, `/usr/local/bin/gengar`) matches where other system-wide developer tools land on Linux. It's useful for shared-machine deployments where one system install should serve every user. Per-user config (auth, skills, sessions) still lives under each user's `~/.gengar/` or explicit `GENGAR_HOME`.

### After Installation

Reload your shell and start chatting:

```bash
source ~/.bashrc   # or: source ~/.zshrc
gengar             # Start chatting!
```

To reconfigure individual settings later, use the dedicated commands:

```bash
gengar model          # Choose your LLM provider and model
gengar tools          # Configure which tools are enabled
gengar gateway setup  # Set up messaging platforms
gengar config set     # Set individual config values
gengar setup          # Or run the full setup wizard to configure everything at once
```

---

## Prerequisites

The only prerequisite is **Git**. The installer automatically handles everything else:

- **uv** (fast Python package manager)
- **Python 3.11** (via uv, no sudo needed)
- **Node.js v22** (for browser automation and WhatsApp bridge)
- **ripgrep** (fast file search)
- **ffmpeg** (audio format conversion for TTS)

:::info
You do **not** need to install Python, Node.js, ripgrep, or ffmpeg manually. The installer detects what's missing and installs it for you. Just make sure `git` is available (`git --version`).
:::

:::tip Nix users
If you use Nix (on NixOS, macOS, or Linux), there's a dedicated setup path with a Nix flake, declarative NixOS module, and optional container mode. See the **[Nix & NixOS Setup](./nix-setup.md)** guide.
:::

---

## Manual / Developer Installation

If you want to clone the repo and install from source — for contributing, running from a specific branch, or having full control over the virtual environment — see the [Development Setup](../developer-guide/contributing.md#development-setup) section in the Contributing guide.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `gengar: command not found` | Reload your shell (`source ~/.bashrc`) or check PATH |
| `API key not set` | Run `gengar model` to configure your provider, or `gengar config set OPENROUTER_API_KEY your_key` |
| Missing config after update | Run `gengar config check` then `gengar config migrate` |

For more diagnostics, run `gengar doctor` — it will tell you exactly what's missing and how to fix it.
