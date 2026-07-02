# Football Match Predictor — Multi-Agent System

**English** · [简体中文](README.zh-CN.md)

A [Claude Code](https://claude.com/claude-code) multi-agent pipeline for football (soccer)
match prediction. Advisory subagents each own one data domain; the main Claude Code session
acts as the deterministic orchestrator; a Bias Auditor and a CEO/Veto layer gate the final call.

This is deliberately built in the same shape as a trading desk: specialist analysts feed a
controller, a risk/bias check runs before anything ships, and a senior veto has the final
word. LLM agents are **advisory only** — the pipeline order and the final assembly are
deterministic and defined in `CLAUDE.md`.

> **Disclaimer.** This is an educational/experimental project. Predictions are AI-generated,
> can be wrong, and are **not betting advice**. Do not wager money based on its output.

---

## Why it's built this way

The methodology encoded here was developed the hard way, across an extended run of real
World Cup 2026 predictions. The single biggest lesson: **direction (who wins, big vs. small,
both-teams-score or not) is genuinely predictable; the exact scoreline is mostly luck.** The
agents are tuned to be confident about direction and honest about the limits of precision.
See `knowledge/lessons-learned.md` — it is the heart of the system and the reason the Bias
Auditor exists.

---

## Architecture

```
                          ┌─────────────────────────────┐
                          │   MAIN SESSION (Orchestrator)│
                          │   governed by CLAUDE.md      │
                          │   invoked via /predict       │
                          └──────────────┬──────────────┘
                                         │ fixed pipeline order
          ┌───────────────┬─────────────┼─────────────┬───────────────┐
          ▼               ▼             ▼              ▼               ▼
   ┌────────────┐  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
   │ match-type │  │  match-    │ │  weather-  │ │  squad-    │ │  (data     │
   │ classifier │─▶│  analyst   │ │  analyst   │ │  analyst   │ │  gather)   │
   │  (GATE 1)  │  │  (coach)   │ │            │ │            │ │            │
   └────────────┘  └────────────┘ └────────────┘ └────────────┘ └────────────┘
          │               │             │              │
          └───────────────┴──────┬──────┴──────────────┘
                                 ▼
                        ┌─────────────────┐
                        │  DRAFT CALL      │  assembled by main session
                        └────────┬─────────┘
                                 ▼
                        ┌─────────────────┐
                        │  bias-auditor    │  GATE 2 — mechanical bias check
                        └────────┬─────────┘
                                 ▼
                        ┌─────────────────┐
                        │  ceo-veto        │  GATE 3 — final senior judgment
                        └────────┬─────────┘
                                 ▼
                        ┌─────────────────┐
                        │  FINAL PREDICTION│  written to predictions/
                        └─────────────────┘
```

## The agents — 6 subagents + 1 orchestrator

The pipeline is **6 project-scoped subagents**. The "7th" role is the orchestrator, which is
*not* a subagent file — it's the main Claude Code session itself, governed by `CLAUDE.md`.

| # | Agent | Role | Gate? |
|---|-------|------|-------|
| 1 | **match-type-classifier** | Decides *what kind of match* this is, so the right logic gets applied. Runs first because everything downstream depends on it. | Gate 1 |
| 2 | **match-analyst** ("the coach") | Team quality differential, tactical matchup, stakes/motivation, home advantage. Produces the core read. | — |
| 3 | **weather-analyst** | Temperature, rain, **roof open/closed**, altitude, delay risk. Environment amplifies mismatches. | — |
| 4 | **squad-analyst** | Confirmed lineups, injuries, form, key scorers, **goalkeeper status**, rotation risk. | — |
| 5 | **bias-auditor** | Runs the draft against the logged catalog of known recurring errors *before* it ships. Purely mechanical checklist. | Gate 2 |
| 6 | **ceo-veto** | Final senior judgment. Can veto, downgrade confidence, or send it back. Challenges *reasoning quality*, never just supplies a rival score. | Gate 3 |
| — | *orchestrator* | *Not a subagent.* The main Claude Code session, governed by `CLAUDE.md` and triggered by `/predict`. | — |

---

## Setup

Requires [Claude Code](https://claude.com/claude-code) v2.x.

1. Clone the repo:
   ```bash
   git clone https://github.com/tleung927/world_cup_2026_claude.git
   cd world_cup_2026_claude
   ```
2. Launch Claude Code in the project folder:
   ```bash
   claude
   ```
   The `.claude/agents/` and `.claude/commands/` folders are picked up automatically as
   **project-scoped** subagents and slash commands.
3. Verify the agents loaded — run `/agents` inside Claude Code; you should see all six.
4. Run a prediction:
   ```
   /predict France vs Sweden, World Cup 2026 Round of 32, MetLife Stadium
   ```
5. The final prediction is written to `predictions/<date>-<teams>.md`.
6. After the match resolves, log the outcome:
   ```
   /postmatch France 2-1 Sweden — <what actually happened>
   ```

### Data wiring

Agents use `WebSearch` / `WebFetch` out of the box. On first run, Claude Code will prompt to
allow the domains each analyst fetches (a personal allowlist is saved to the git-ignored
`.claude/settings.local.json`). If you later add a paid feed (Opta, SportRadar) or a scraper,
expose it as an MCP server or a local script and the analyst agents will use it.

---

## File map

```
world_cup_2026_claude/
├── README.md                     ← you are here (English)
├── README.zh-CN.md               ← 简体中文
├── LICENSE                       ← MIT
├── CLAUDE.md                     ← orchestration rules for the main session
├── .claude/
│   ├── agents/
│   │   ├── match-type-classifier.md
│   │   ├── match-analyst.md
│   │   ├── weather-analyst.md
│   │   ├── squad-analyst.md
│   │   ├── bias-auditor.md
│   │   └── ceo-veto.md
│   └── commands/
│       ├── predict.md            ← /predict   — run the full pipeline
│       └── postmatch.md          ← /postmatch — log a result, update the bias log
├── knowledge/
│   ├── prediction-framework.md   ← the full methodology
│   ├── match-type-taxonomy.md    ← the match-type gate logic
│   ├── lessons-learned.md        ← LIVING bias log (update after every match)
│   └── output-template.md        ← standard prediction format
└── predictions/                  ← generated predictions land here (sample included)
```

## The improvement loop

After each match resolves, `/postmatch` appends the outcome to `knowledge/lessons-learned.md`:
what was predicted, what happened, and — if wrong — *which category* of error it was. The Bias
Auditor reads that file on every run, so logged mistakes actively prevent their own repetition.
This is the whole point of the system.

---

## Contributing

Contributions are welcome — especially new entries in `knowledge/lessons-learned.md` (with the
evidence that earns them) and refinements to the match-type taxonomy. Keep the prime directive
intact: **confident about direction, honest about exact scores.** Open an issue or a PR.

## License

[MIT](LICENSE) © 2026 Tony Leung.
