---
description: Run the full multi-agent prediction pipeline for a fixture
argument-hint: <home> vs <away>, <competition>, <venue> [, kickoff]
---

Run the complete prediction pipeline for the fixture below, following the fixed order
and gates defined in `CLAUDE.md`. You are the orchestrator — you sequence the subagents,
assemble the draft, pass both gates, and write the final file. You do not analyse
directly; the specialists do.

Fixture: $ARGUMENTS

**If no fixture was given above** (empty `$ARGUMENTS`): select it automatically. Via web
search of the current 2026 World Cup schedule, find the SOONEST upcoming match that has not
yet kicked off and does not already have a file in `predictions/`, and use that fixture.
State which one you picked. (If a fixture *was* given, use it as-is — a specific request or
a deliberate near-kickoff re-run.)

Execute in this exact order:

1. **Gate 1 — classify.** Invoke `match-type-classifier`. Do not proceed without a
   match archetype.

2. **Analyse (parallel).** Invoke `match-analyst` (conditioned on the archetype),
   `weather-analyst`, and `squad-analyst`.

3. **Assemble the draft call** yourself: direction + confidence, goal expectation
   (big/medium/tight, BTTS yes/no), extra-time/penalty risk, a most-likely scoreline
   labelled "direction indicator, not a commitment", and 2–4 key variables.

4. **Gate 2 — bias audit.** Invoke `bias-auditor` on the draft. If it returns REVISE,
   fix every flag before continuing.

5. **Gate 3 — CEO.** Invoke `ceo-veto` on the revised draft. Apply any downgrade; if
   vetoed, make the required change and re-run only this step. Proceed only on APPROVE.

6. **Write the final prediction** to `predictions/<YYYY-MM-DD>-<home>-vs-<away>.md`
   using `knowledge/output-template.md`. Note any surviving CEO caution or bias flag.
   Include the **Corners read** section (from the match-analyst's corner profile) — corner
   direction plus high-variance per-team and total bands, per the template. Corners are a
   supplementary read, not a gated call, so they bypass the two gates.

7. **Write the Simplified-Chinese translation.** Translate the final prediction into
   Simplified Chinese and write it to `predictions/<YYYY-MM-DD>-<home>-vs-<away>-zh.md`.
   The English `.md` is the canonical source; the Chinese `.md` is the additional
   deliverable produced every run. **Markdown only — do NOT generate a PDF.**

8. **Commit and push.** Stage the new prediction files (and any updated knowledge files),
   commit with a descriptive per-fixture message ending in the
   `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` line, and push to the current
   branch. `.claude/settings.local.json` stays git-ignored. Do this automatically every
   run — do not ask first.

Keep your chat-side summary to a few lines — the detail lives in the written file.

Reminder of the prime directive: **be confident about direction, honest about exact
scores.** If you feel the urge to gift the underdog a consolation goal, that instinct
has been wrong before — apply the ball-control test instead.
