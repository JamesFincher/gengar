<p align="center">
  <img src="assets/banner.png" alt="Gengar" width="100%">
</p>

# Gengar ☤

<p align="center">
  <a href="https://github.com/jamesfincher/gengar"><img src="https://img.shields.io/badge/Docs-gengar--agent.jamesfincher.com-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://github.com/jamesfincher/gengar"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/jamesfincher/gengar/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://github.com/jamesfincher"><img src="https://img.shields.io/badge/Built%20by-James%20Fincher-blueviolet?style=for-the-badge" alt="Built by James Fincher"></a>
</p>

**The self-improving AI agent built by [James Fincher](https://github.com/jamesfincher).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai) (200+ models), [NVIDIA NIM](https://build.nvidia.com) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI, or your own endpoint. Switch with `gengar model` — no code changes, no lock-in.

<table>
<tr><td><b>A real terminal interface</b></td><td>Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.</td></tr>
<tr><td><b>Lives where you do</b></td><td>Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.</td></tr>
<tr><td><b>A closed learning loop</b></td><td>Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. <a href="https://github.com/plastic-labs/honcho">Honcho</a> dialectic user modeling. Compatible with the <a href="https://agentskills.io">agentskills.io</a> open standard.</td></tr>
<tr><td><b>Scheduled automations</b></td><td>Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.</td></tr>
<tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
<tr><td><b>Runs anywhere, not just your laptop</b></td><td>Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster.</td></tr>
<tr><td><b>Research-ready</b></td><td>Batch trajectory generation, Atropos RL environments, trajectory compression for training the next generation of tool-calling models.</td></tr>
</table>

---

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/jamesfincher/gengar/main/scripts/install.sh | bash
```

Works on Linux, macOS, WSL2, and Android via Termux. The installer handles the platform-specific setup for you.

> **Android / Termux:** The tested manual path is documented in the [Termux guide](https://github.com/jamesfincher/gengar/tree/main/website/docs/getting-started/termux). On Termux, Gengar installs a curated `.[termux]` extra because the full `.[all]` extra currently pulls Android-incompatible voice dependencies.
>
> **Windows:** Native Windows is not supported. Please install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and run the command above.

After installation:

```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
gengar              # start chatting!
```

---

## Getting Started

```bash
gengar              # Interactive CLI — start a conversation
gengar model        # Choose your LLM provider and model
gengar tools        # Configure which tools are enabled
gengar config set   # Set individual config values
gengar gateway      # Start the messaging gateway (Telegram, Discord, etc.)
gengar setup        # Run the full setup wizard (configures everything at once)
gengar claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
gengar update       # Update to the latest version
gengar doctor       # Diagnose any issues
```

📖 **[Full documentation →](https://github.com/jamesfincher/gengar)**

## CLI vs Messaging Quick Reference

Gengar has two entry points: start the terminal UI with `gengar`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
|---------|-----|---------------------|
| Start chatting | `gengar` | Run `gengar gateway setup` + `gengar gateway start`, then send the bot a message |
| Start fresh conversation | `/new` or `/reset` | `/new` or `/reset` |
| Change model | `/model [provider:model]` | `/model [provider:model]` |
| Set a personality | `/personality [name]` | `/personality [name]` |
| Retry or undo the last turn | `/retry`, `/undo` | `/retry`, `/undo` |
| Compress context / check usage | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]` |
| Browse skills | `/skills` or `/<skill-name>` | `/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message | `/stop` or send a new message |
| Platform-specific status | `/platforms` | `/status`, `/sethome` |

For the full command lists, see the [CLI guide](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/cli) and the [Messaging Gateway guide](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/messaging).

---

## Documentation

All documentation lives at **[github.com/jamesfincher/gengar](https://github.com/jamesfincher/gengar)**:

| Section | What's Covered |
|---------|---------------|
| [Quickstart](https://github.com/jamesfincher/gengar/tree/main/website/docs/getting-started/quickstart) | Install → setup → first conversation in 2 minutes |
| [CLI Usage](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/cli) | Commands, keybindings, personalities, sessions |
| [Configuration](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/configuration) | Config file, providers, models, all options |
| [Messaging Gateway](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/messaging) | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/security) | Command approval, DM pairing, container isolation |
| [Tools & Toolsets](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/features/tools) | 40+ tools, toolset system, terminal backends |
| [Skills System](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/features/skills) | Procedural memory, Skills Hub, creating skills |
| [Memory](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/features/memory) | Persistent memory, user profiles, best practices |
| [MCP Integration](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/features/mcp) | Connect any MCP server for extended capabilities |
| [Cron Scheduling](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/features/cron) | Scheduled tasks with platform delivery |
| [Context Files](https://github.com/jamesfincher/gengar/tree/main/website/docs/user-guide/features/context-files) | Project context that shapes every conversation |
| [Architecture](https://github.com/jamesfincher/gengar/tree/main/website/docs/developer-guide/architecture) | Project structure, agent loop, key classes |
| [Contributing](https://github.com/jamesfincher/gengar/tree/main/website/docs/developer-guide/contributing) | Development setup, PR process, code style |
| [CLI Reference](https://github.com/jamesfincher/gengar/tree/main/website/docs/reference/cli-commands) | All commands and flags |
| [Environment Variables](https://github.com/jamesfincher/gengar/tree/main/website/docs/reference/environment-variables) | Complete env var reference |

---

## Migrating from OpenClaw

If you're coming from OpenClaw, Gengar can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`gengar setup`) automatically detects `~/.openclaw` and offers to migrate before configuration begins.

**Anytime after install:**

```bash
gengar claw migrate              # Interactive migration (full preset)
gengar claw migrate --dry-run    # Preview what would be migrated
gengar claw migrate --preset user-data   # Migrate without secrets
gengar claw migrate --overwrite  # Overwrite existing conflicts
```

What gets imported:
- **SOUL.md** — persona file
- **Memories** — MEMORY.md and USER.md entries
- **Skills** — user-created skills → `~/.gengar/skills/openclaw-imports/`
- **Command allowlist** — approval patterns
- **Messaging settings** — platform configs, allowed users, working directory
- **API keys** — allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
- **TTS assets** — workspace audio files
- **Workspace instructions** — AGENTS.md (with `--workspace-target`)

See `gengar claw migrate --help` for all options, or use the `openclaw-migration` skill for an interactive agent-guided migration with dry-run previews.

---

## Contributing

We welcome contributions! See the [Contributing Guide](https://github.com/jamesfincher/gengar/tree/main/website/docs/developer-guide/contributing) for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-gengar.sh`:

```bash
git clone https://github.com/jamesfincher/gengar.git
cd gengar
./setup-gengar.sh     # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/gengar
./gengar              # auto-detects the venv, no need to `source` first
```

Manual path (equivalent to the above):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

> **RL Training (optional):** The RL/Atropos integration (`environments/`) ships via the `atroposlib` and `tinker` dependencies pulled in by `.[all,dev]` — no submodule setup required.

---

## Community

- 💬 [Discord](https://github.com/jamesfincher/gengar)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/jamesfincher/gengar/issues)
- 🔌 [GengarClaw](https://github.com/AaronWong1999/hermesclaw) — Community WeChat bridge: Run Gengar and OpenClaw on the same WeChat account.

---

## License

MIT — see [LICENSE](LICENSE).

Built by [James Fincher](https://github.com/jamesfincher).
