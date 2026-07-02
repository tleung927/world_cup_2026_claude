---
description: Log a finished match result and update the lessons-learned bias log
argument-hint: <home> <score>-<score> <away> [note, e.g. "won on penalties"]
---

Log the finished match below and update the improvement loop. Your job is to compare what
was predicted against what actually happened, classify any error **honestly**, and append
the lesson so the `bias-auditor` gets sharper. The entire value of this step is an accurate
record — do not soften a miss to save face, and do not inflate a lucky hit.

Result: $ARGUMENTS

Execute these steps:

1. **Parse** the fixture and the actual result from the input (teams, final score, and any
   note such as "won on penalties" or "after extra time").

2. **Locate the original prediction** in `predictions/` — the file whose teams match. If
   several match, use the most recent. If none exists, say so clearly and stop (there's
   nothing to score against); ask the user to point you at the prediction or run `/predict`
   retroactively.

3. **Read the prediction** and extract what was actually claimed:
   - the match archetype it was classified as
   - direction (winner/advance) + stated confidence
   - game shape (big / medium / tight)
   - both-teams-score call
   - extra-time / penalty risk (for knockouts)
   - the most-likely scoreline (the indicator)

4. **Compare, axis by axis, honestly:**
   - Direction: right or wrong?
   - Shape/margin: right or wrong?
   - Both-teams-score: right or wrong?
   - Extra-time/penalty: right or wrong?
   - Scoreline: how far off, and **in what shape** — e.g. "predicted an underdog goal that
     never came," "predicted a safe middle when it was an extreme (0–0 / blowout)," "forced
     a confident winner in a coin flip that went to penalties."

5. **Classify** against the standing bias catalog in `knowledge/lessons-learned.md`
   (the 9 numbered biases), OR mark **calibration success**. Rules for an honest verdict:
   - If **direction + shape + BTTS were right** and only the exact digits were off by a
     goal → that's a **calibration success** under the prime directive (exact scores are
     luck). Log it as such; don't self-flagellate over the digits.
   - But if a **recurring bias actually reappeared** (a consolation goal materialised again,
     a coin-flip winner was forced, weather/roof was mishandled, an extreme was diluted to a
     middle) → log that prominently, by its catalog number. That's the actionable part.
   - Getting the winner right but repeating a known shape-error is BOTH — note the success
     and the flagged bias.

6. **Append** a structured entry to the **end** of `knowledge/lessons-learned.md`, using
   the case-log template already in that file:
   ```
   ### <date> — <home> vs <away> (<competition>)
   Predicted: <direction / shape / scoreline-as-indicator, as claimed>
   Actual: <final result + any ET/penalty note>
   Category: <one or more of the 9 biases by number, and/or "calibration success">
   Rule (new or reinforced): <the concrete takeaway the auditor should apply going forward>
   ```

7. **If — and only if — a genuinely NEW failure mode emerged** that none of biases 1–9
   cover, add it to the "Standing bias catalog" section of the same file as the next
   numbered item (e.g. BIAS-10), with a one-line description. The auditor reads the catalog
   every run, so this is how a new lesson enters the checklist. Do not invent new categories
   for errors that already fit an existing one — keep the catalog tight.

8. **Report** a short summary in chat (a few lines):
   - what was right, what was wrong
   - the category logged
   - the rule reinforced or added
   Keep it brief; the detail lives in the updated log file.

Reminder: the point of this system is that logged mistakes stop repeating. An honest
"calibration success — direction right, score is luck" is a valid and common outcome. A
sugar-coated miss poisons the loop. Score it straight.
