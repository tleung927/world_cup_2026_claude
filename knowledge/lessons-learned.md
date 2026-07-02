# Lessons Learned — Living Bias Log

**This is the most important file in the system.** The `bias-auditor` reads it on every
run, so every logged mistake actively prevents its own repetition. Append to it after
each match resolves. Do not delete history — the record is the value.

Format for each entry: what was predicted, what happened, the **error category**, and the
**rule** it produced (or reinforced).

---

## Standing bias catalog (the checklist the auditor enforces)

These are the recurring failure modes, extracted from the case log below. The auditor
checks every draft against all of them.

1. **Consolation goal** — gifting the underdog a goal that isn't earned by ball-control
   evidence. *The single most repeated error.*
2. **Probability compression** — pairing a big win probability with a timid margin.
3. **Exact-score overreach** — presenting a precise scoreline as a confident prediction.
4. **Roof / environment miss** — applying weather logic to an indoor game, or not
   checking the roof; missing a delay/altitude effect.
5. **Underdog mis-classification** — treating a soft blowout as a hard block, or vice versa.
6. **Ignoring favourite motivation/rotation** — predicting a rout from a resting side, or
   missing a must-win firepower spike.
7. **False confidence in a coin flip** — forcing a confident winner in an even knockout.
8. **Half-split overreach** — asserting precise per-half scores.
9. **Reputation over evidence** — trusting names where recent stats/results disagree.

---

## Case log

### The consolation-goal cluster (errors 1, 3, 5, 9 — the big one)

The most persistent, most expensive pattern. Predicted an underdog goal "for
respectability" in a lopsided game; the goal repeatedly failed to appear.

**Case — strong favourite vs. soft, collapsing underdog.**
Predicted a 1-goal margin with an underdog consolation. Actual: a clean-sheet rout by a
much larger margin. **Category:** consolation goal + probability compression. **Rule:**
soft underdog (Type A) → lock the clean sheet, push the margin; an extreme signal
(defence in freefall) deserves an extreme conclusion, not a polite middle.

**Case — must-win favourite vs. already-eliminated underdog.**
Repeated the consolation error even after the previous miss — predicted a 1-goal margin
with an underdog goal; actual was a clean-sheet blowout by a wide margin. **Category:**
consolation goal (repeat) + underestimated must-win firepower. **Rule:** a fired-up
favourite under must-win pressure *amplifies* output; an already-eliminated side has no
stable scoring. Do not gift the goal. (Also: logging a lesson is not the same as changing
behaviour — the auditor exists precisely because good intentions failed here twice.)

**Case — top side vs. underdog with a strong-name attack but a leaky defence.**
Predicted an underdog goal on the strength of the underdog's *reputable forwards*. Actual:
the underdog was pinned back, starved of the ball (barely any shots on target), and scored
zero — the game would have been an even bigger rout but for the underdog's goalkeeper.
**Category:** reputation over evidence + consolation goal. **Rule — the key insight of the
whole system:** *the test for "can the underdog score?" is ball control and chance
creation, not attacker names.* A strong forward line behind a leaky defence gets starved.
This is why BIAS-1 and BIAS-9 are separate, strict checks, and why Type A vs. Type C hinges
on evidence, not names.

### The environment miss (error 4)

**Case — favourite vs. soft underdog, open-air stadium, storms forecast.**
Predicted the right winner and a near-right margin, but assigned the underdog a goal and,
critically, never factored a weather delay. Actual: a long lightning delay; on the restart
the shallower side made errors and conceded again — the opposite of the predicted underdog
goal. **Category:** environment miss + consolation goal. **Rule:** environment is an
independent variable that amplifies the gap and hurts the weaker/shallower side. Always
check roof, delay risk, heat, and altitude baselines. (Roof-closed games are the inverse
trap: don't apply weather logic indoors.)

### The "both teams score" over-assumption (error 3, in a tight game)

**Case — two strong sides, one needing only a draw.**
Predicted a 1–1, assuming both marquee attacks would score. Actual: 0–0 — both defences
were excellent, the pragmatic side killed the game, and the other couldn't break the block.
36 shots, no goals. **Category:** exact-score overreach / failure to predict the extreme
low. **Rule:** when *every* signal points to "goals will be very hard" (elite defences +
one side content with a draw + conditions slowing the game), dare to predict 0–0. This is
the mirror image of the consolation bias: the same reluctance to commit to an extreme,
pulling the call toward a "safe" middle. Type E logic exists because of this.

### The coin-flip over-confidence (error 7)

**Case — two top-ten sides, even knockout.**
Predicted a confident 1-goal win for the nominal favourite. Actual: 1–1 through extra time,
decided by a penalty shootout the other side won. The favourite led and was pegged back in
stoppage time. **Category:** false confidence in a coin flip + ignored team habits. **Rules:**
(a) in an even knockout, name the extra-time/penalty randomness instead of forcing a winner;
a shootout is near-random. (b) Weigh hidden habits the silo agents miss — one side had a
recurring "leads then concedes" pattern; the other had genuine big-match penalty pedigree.
These belong to the CEO's structural-blind-spot check.

### Calibration successes (what "right" looked like)

Logged so the system knows which behaviours to keep, not just which to avoid.

- **Hard-underdog game handled correctly:** recognised a disciplined low block, predicted a
  narrow favourite win, did *not* inflate the margin — correct. (Type B done right.)
- **Soft-underdog game handled correctly (after the cluster above):** locked the clean sheet
  and predicted a wide margin against a collapsed, eliminated side — correct. (Type A done
  right; the consolation instinct was finally overridden.)
- **Hard block, clean sheet locked but margin restrained:** favourite vs. a physical low
  block; predicted a clean-sheet *small* win rather than a rout — correct on both counts.
  (Getting BOTH the clean sheet AND the restrained margin right.)

**Meta-lesson from the whole run:** the *direction* calls (winner, big/small, BTTS,
extra-time risk) were consistently right. The misses were almost all *exact scoreline* —
and almost always the same shape: an underdog goal that never came, or a "safe middle" when
the truth was an extreme. Hence the prime directive: confident on direction, honest that the
exact score is mostly luck.

---

## Append new cases below this line
<!-- Template:
### <date> — <home> vs <away> (<competition>)
Predicted: <direction / margin / scoreline-as-indicator>
Actual: <result>
Category: <one or more of the 9 biases, or "calibration success">
Rule (new or reinforced): <the takeaway the auditor should apply going forward>
-->
