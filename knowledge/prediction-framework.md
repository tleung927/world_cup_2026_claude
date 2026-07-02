# Prediction Framework

The methodology every agent shares. Distilled from an extended run of real match
predictions. Read this alongside `match-type-taxonomy.md` and `lessons-learned.md`.

---

## Prime directive

**Direction is predictable. Exact scorelines are mostly luck.**

Across a long prediction run, one pattern held: the *direction* calls (who wins, big vs.
small margin, both-teams-score or not, extra-time risk) were reliably right, while the
*exact scoreline* was wrong far more often than not — usually by a single goal, and
usually because a predicted underdog goal never came. The conclusion is not "try harder
on the score." It's "the exact score is largely unknowable; stake your credibility on
direction and be explicit that the scoreline is only an indicator." Professional books
price goal *totals* (over/under 1.5, 2.5), not exact scores, for the same reason.

Everything below serves that directive.

---

## The four analytical dimensions

1. **Team quality differential** — rankings, supercomputer win probabilities, market
   odds. Respect them (see Rule 1).
2. **Motivation & stakes** — must-win vs. already-qualified, rotation, morale, records
   being chased. As important as talent (see Rule 4).
3. **Physical conditions** — heat, altitude, pitch, roof, delay risk (see Rule 5 and the
   weather agent).
4. **Underdog vulnerability type** — *which kind of weak* the weaker side is. The most
   decision-relevant judgment in the whole framework (see Rule 3 and the taxonomy).

---

## The rules (learned, not assumed)

### Rule 1 — Respect the model probability; never compress it
A ~60%+ win probability is a **large** edge at international level. The instinct that
"two national teams are never that far apart" is wrong and leads to timid margins. If the
number says big favourite, let the margin expectation reflect it.

### Rule 2 — Extreme signals deserve extreme conclusions
When a data point is extreme (a side shipping double-digit goals across two games; a
supercomputer at 85%+), extrapolate toward the extreme instead of diluting it to a
"respectable" middle. Do not average an extreme back to the mean out of politeness.

### Rule 3 — Classify the underdog correctly (the core skill)
"Weak" is not one thing:
- **Soft underdog** — collapsing morale, leaky defence, no stable scoring. → clean sheet,
  big margin.
- **Hard underdog** — disciplined low block, defends well, little firepower. → favourite
  wins narrow; do not inflate the margin.
- **Leaky-but-dangerous** — can genuinely create and convert (real chances, not names).
  → favourite wins, both teams likely score.

**The test for "can the underdog score?" is whether it can hold possession and create
real chances — NOT whether it has famous attackers.** A strong forward line behind a
leaky defence gets pinned back and starved of the ball; it frequently scores zero despite
the names. This single confusion — reputation vs. actual ball control — was behind a
whole run of "gave the underdog a goal that never came" misses.

### Rule 4 — Weigh the strong side's motivation as much as the underdog's quality
An already-qualified favourite that will rotate and coast suppresses the margin — a rout
prediction from a resting side is a mistake. A must-win situation *amplifies* a strong
side's output. A side in freefall (fresh coach, collapsing morale) usually gets worse,
not better; a new manager rarely repairs a defence in days.

### Rule 5 — Environment amplifies the gap and hurts the weaker/less-deep side
Heat, altitude, slick pitch, and especially long weather delays punish the shallower,
rougher, less-disciplined side. Two caveats that have bitten before:
- **Check the roof.** A closed roof neutralises weather entirely — do not then apply
  heat/rain/delay logic.
- **Check altitude baselines.** A "high-altitude home edge" is worthless against an
  opponent whose own home sits even higher.
In a two-strong matchup, conditions hurt both roughly equally.

### Rule 6 — Separate "who wins" from "by how much"
These are two independent judgments with different error sources. You can be right about
the winner and wrong about the margin (and usually are). Decide direction first, margin
second, and never let a confident direction call masquerade as a confident scoreline.

### Rule 7 — In even knockouts, name the randomness
When two strong sides are ~50/50, the honest output flags realistic extra-time and
penalty risk rather than forcing a confident winner. A shootout is close to a coin flip;
"I can't predict the shootout" is a *more accurate* statement than a fake confident pick.
Also weigh hidden habits here: a side that leads then concedes; a team with genuine
big-match penalty pedigree.

### Rule 8 — Halves are mostly luck; only trends are knowable
Whether a goal lands in the 44th or 48th minute is not predictable. The defensible
trends: second-half goals usually exceed first-half (fatigue, chasing sides pushing,
substitutions); cagey feel-out openers tend to stay low. State those; label the rest as
luck.

### Rule 9 — Evidence over reputation, always
Where a player's or team's reputation and their recent evidence (shots, shots on target,
big chances, actual results) disagree, trust the evidence. Reputation is the slowest-
updating and least reliable input.

---

## How the rules combine into a call

1. Classify the match (taxonomy) → fixes which rules dominate.
2. Read quality, tactics, stakes, conditions (Rules 1–5).
3. Decide **direction** with calibrated confidence (Rule 6).
4. Decide **goal expectation & margin** — apply the underdog-type/ball-control test to
   the both-teams-score question (Rule 3).
5. For knockouts, set **extra-time/penalty risk** honestly (Rule 7).
6. Offer a **most-likely scoreline as an indicator, not a commitment** (Prime directive).
7. Pass through bias audit (catches Rules 1–9 violations) and CEO (calibration + blind
   spots).

---

## What "good" looks like

A good prediction from this system says, in effect:
> "Team A is clearly more likely to advance (strong edge). Expect a [big/medium/tight]
> game; [both teams / only A] likely to score, because [ball-control evidence]. In a
> knockout, [low/real] chance it goes to extra time. Most likely something like X–Y, but
> treat that as a direction indicator, not a promise. Watch [2–4 specific things]."

It does **not** say "It'll be exactly 3–1." That precision isn't real, and pretending
otherwise is the mistake this whole framework exists to prevent.
