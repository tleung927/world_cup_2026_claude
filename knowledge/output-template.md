# Output Template

The orchestrator writes each final prediction to `predictions/<YYYY-MM-DD>-<home>-vs-<away>.md`
using this structure. The template's shape enforces the prime directive: direction carries
the confidence; the exact scoreline is explicitly an indicator. Do not add hedging
boilerplate — the honesty is structural, not prose.

---

```markdown
# <Home> vs <Away> — <Competition, Round>

**Venue:** <stadium, city>  |  **Kickoff:** <local time>  |  **Date:** <YYYY-MM-DD>
**Match type:** <archetype from classifier>  |  **Roof:** <open-air / closed → weather neutral>

## The call (direction — this is what carries confidence)

- **Winner / advances:** <side> — **confidence: <low / medium / high>**
- **Game shape:** <big margin / medium / tight grind>
- **Both teams to score:** <yes / no> — because <ball-control evidence, not names>
- **Extra-time / penalty risk (knockouts):** <low / real / high>

## Most likely scoreline

**<X–Y>** — *direction indicator, NOT a commitment.* Treat the digits as a lean; the
confidence lives in "the call" above, not here.

## Why (2–4 sentences)

<The core reasoning: quality gap (respected, not compressed), the tactical/stakes read,
and — if a goal is assigned to either side — the evidence that earns it. If a clean sheet
is locked, say why. If it's a coin flip, name the randomness.>

## Watch these (2–4 specific, checkable things)

- <e.g. is the first-choice keeper starting?>
- <e.g. does the favourite rest starters?>
- <e.g. does the low block hold past the hour?>
- <e.g. lightning delay / closed roof confirmation>

## Top scorer lean

<1–2 names, both sides if relevant, with a one-line reason each.>

---
*Gate notes:* <any surviving bias-audit flag or CEO downgrade/caution — one line. If clean,
write "Bias audit clean; CEO approved.">
```

---

## Notes on filling it in

- **Confidence goes on direction, never on the scoreline.** If you catch yourself wanting
  to sound sure about the exact digits, move that certainty up to the winner/shape lines
  or drop it.
- **The BTTS line must cite evidence.** "Both score" or "clean sheet" is only credible with
  the ball-control/chance-creation reasoning attached. This is what the auditor checks.
- **For coin flips (Type D),** the "confidence" on the winner should usually be *low*, and
  the extra-time/penalty line should be prominent. A confident winner here is a red flag.
- **For low-scoring setups (Type E, or elite defences),** don't default to a 1–1 "both
  score" out of habit — 0–0 / 1–0 may be the honest lean.
- **Keep it scannable.** A good prediction is read in fifteen seconds and every line earns
  its place.
