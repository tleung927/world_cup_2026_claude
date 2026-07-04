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
10. **Static-block fallacy in must-win knockouts** — trusting a low-block underdog's
    group-stage clean sheets in a single-elimination tie, when the must-win format forces
    them to abandon the block once level/behind, opening the game up (BTTS→yes, goals up),
    especially in extra time. Don't lean hard on a clean sheet / BTTS-no against a must-win
    underdog — and don't trust the favourite's clean-sheet record to hold either.

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

### 2026-07-02 — Portugal vs Croatia (World Cup 2026, Round of 32)
Predicted: Type C. Direction — Portugal to advance, medium-high confidence. Shape — medium margin, heat-tempered toward the lower end. BTTS — lean yes, but with a Portugal clean sheet flagged as "meaningfully live" (Croatia's goal routes = set-pieces / transition / Baturina, explicitly *not* a gifted consolation). ET/penalty risk — real but downweighted to ~22–26%. Scoreline indicator — 2–1 Portugal.
Actual: Portugal 2–1 Croatia, won in 90 minutes (no extra time).
Category: **Calibration success** — direction, shape, and BTTS all correct; ET risk correctly named and correctly downweighted. Every axis landed. No recurring bias reappeared.
Rule (reinforced): (a) The exact 2–1 match is **luck, not skill** — do not over-credit the digits; the value is that every *direction* axis was right. (b) Positive lesson for BIAS-1 vs BIAS-9: Gate 2 pushed the draft toward a clean sheet, but we *held* a lean-yes because Croatia's scoring routes were evidenced (set-piece/transition threat that had produced goals all group stage) rather than name-based. The goal came exactly via that route. Takeaway: an *evidenced* underdog goal is not a consolation-goal error even when the auditor pressures toward a shutout — the ball-control/chance-creation test cuts both ways, and here it correctly said "lean yes." Keep distinguishing an earned BTTS-yes from a reflexive gift.

### 2026-07-02 — Switzerland vs Algeria (World Cup 2026, Round of 32)
Predicted: Type C (possession inversion — the underdog held the ball). Direction — Switzerland to advance, medium-high; 90-min win ~even, extra time named as a near-primary path. Shape — medium. BTTS — coin-flip tilting NO, Switzerland clean sheet made co-modal. ET/penalty risk — medium-high (~30%), with Kobel's penalty-specialist edge noted. Scoreline indicator — 1–0 / 2–0 Switzerland (co-primary with 2–1).
Actual: Switzerland 2–0 Algeria, won in 90 minutes (no extra time). Algeria scored zero.
Category: **Calibration success — and a direct BIAS-1 save.** Direction, shape, and BTTS(no) all correct; 2–0 matched a stated co-primary; ET correctly named but did not fire.
Rule (reinforced): This is the counterpart to the Portugal case and the one the system exists for. The *original* draft had 2–1 (Algeria scoring) as the modal outcome; Gate 2 flagged BIAS-1 because the main striker (Amoura) was injured out, breaking Algeria's possession→chance chain, so their goal was demoted from default to a live-but-secondary set-piece/Mahrez route. **Algeria scored zero.** Had the gate not fired, we would have logged the catalog's #1 error — a consolation goal that never came. Takeaway: high possession does NOT earn a BTTS-yes when the striker who converts it is absent; possession is necessary, not sufficient. Together with the Portugal case, this confirms the rule: run the ball-control test on the *actual available* attack, and let it push either way — lean-yes when the routes survive (Croatia), lean-no when the finisher is gone (Algeria).

### 2026-07-03 — Australia vs Egypt (World Cup 2026, Round of 32)
Predicted: Type D (coin flip) after a fresh near-kickoff re-run. Direction — Egypt a SLIGHT edge to advance, LOW confidence; explicitly coin-flip-adjacent, winner not forced. Shape — tight (1-0/1-1/2-1). BTTS — ~50/50 lean yes; Australia's goal held as live-but-secondary (evidenced routes only), not banked. ET/penalty risk — HIGH, named as CO-EQUAL with an Egypt regulation win; shootout called near-random and not predicted through. Scoreline indicator — 1-0 Egypt, with 1-1→ET and 0-0→ET as co-equal alternatives.
Actual: Australia 1–1 Egypt after extra time; **Egypt won 4–2 on penalties.** Both teams scored; the tie went to a shootout.
Category: **Calibration success — a textbook BIAS-7 win.** Direction (Egypt advance), shape (tight), BTTS (yes), and the extra-time/penalty path all correct; 1-1→ET matched a stated co-equal exactly.
Rule (reinforced): This is the MIRROR IMAGE of the coin-flip-over-confidence case already in the catalog (which was a MISS for forcing a confident winner that lost the shootout). Here we did it right: in a genuine Type D, we named Egypt as only a slight edge at LOW confidence, elevated 1-1/0-0→ET to co-equal, and called the shootout near-random rather than predicting a winner through it. Egypt advancing on penalties is a ~coin-flip that broke their way — we correctly did NOT claim skill over it. Two process lessons: (a) when the model says ~40/32/28 with ranks near-level, that IS Type D — resist upgrading it to a comfortable favourite. (b) The near-kickoff re-run materially improved the call: the earlier draft had this as "C borderline-D, medium confidence"; fresh Opta numbers + Salah leaning bench correctly reframed it as a coin flip, and the coin-flip framing is what landed. Re-running for late team news near kickoff has value when a swing variable (here, Salah's start) is still unresolved.

### 2026-07-03 — Argentina vs Cape Verde (World Cup 2026, Round of 32)
Predicted: Type B (hard low block). Direction — Argentina win, HIGH confidence. Shape — TIGHT, narrow 1-0/2-0, explicitly warned against inflating the margin. BTTS — NO (lean); Argentina clean sheet the lean; Cape Verde's goal framed as "live-but-secondary" via set-piece/long-range/keeper-error only. ET/penalty — low-medium, envisioned as a 0-0 stalemate path, with Martinez tilting any shootout to Argentina. Scoreline indicator — 1-0 Argentina.
Actual: 1–1 after 90; **Argentina won 3–2 after extra time.** Cape Verde scored TWICE; Argentina (who had not conceded all group stage) conceded twice; five goals total.
Category: **Direction success wrapped around a real MISS — BIAS-5 (underdog mis-classification) + new BIAS-10 (static-block fallacy in must-win knockouts).** Direction (Argentina advance) correct, and ET was correctly named as a live path — but the BTTS-no/clean-sheet lean was WRONG (Cape Verde scored twice) and the "tight 1-0" modal badly under-shot a 5-goal extra-time thriller. NOT a calibration success — BTTS and shape were both wrong.
Rule (new): We read Cape Verde as a pure Type-B hard block on the strength of two group-stage clean sheets (0-0 Spain, 0-0 Saudi), under-weighting (a) the 2-2 vs Uruguay that showed they *can* be drawn into an open game, and (b) the decisive knockout dynamic: a low-block underdog that MUST win to advance cannot sit for 120 minutes — once level or behind it abandons the block, and the game opens up (BTTS→yes, goals climb), most sharply in extra time. Two concrete takeaways for the auditor: (1) BIAS-10 — do NOT lean hard on a clean sheet / BTTS-no against a must-win low-block underdog in a knockout, even one with a strong group-stage defensive record; the format itself breaks the block late. (2) Don't over-trust the FAVOURITE's clean-sheet record either — Argentina hadn't conceded all group stage and shipped two. What we got right (direction, high confidence, ET as a live path, not gifting an *early* consolation) stands; the miss was treating a group-stage defensive record as a static property rather than something the knockout math actively dismantles.

### 2026-07-03 — Colombia vs Ghana (World Cup 2026, Round of 32)
Predicted: Type B (hard low block), with BIAS-10 applied deliberately (first live test of the new rule). Direction — Colombia win, HIGH confidence. Shape — tight, narrow 1-0/2-0. BTTS — NO, but explicitly held as a LEAN not a LOCK (clean sheet tempered per BIAS-10; Ghana's goal "elevated-and-live" via set-piece/Semenyo counter, but when the block opens a Colombia 2nd was judged more likely than a Ghana 1st, given Kudus OUT and worst-tier creation). ET/penalty — low-medium, with heat + storm-delay risk noted as reducing Ghana's chance of holding that long. Scoreline indicator — 1-0 Colombia.
Actual: **Colombia 1–0 Ghana, won in 90 minutes.** Ghana scored zero; Colombia clean sheet held.
Category: **Calibration success — and the CONTROL case that validates BIAS-10's correct application.** Every axis landed: direction, tight shape, BTTS(no)/clean sheet, ET correctly not firing; 1-0 matched the modal exactly.
Rule (reinforced — this is the pair that calibrates BIAS-10): Cape Verde (prior case) and Ghana are the two poles of the same rule. BIAS-10 says the must-win format ELEVATES the underdog's goal probability — it does NOT say "always predict BTTS-yes." The correct application, shown here, is to (a) hold the clean sheet as a LEAN not a LOCK, then (b) size the underdog-goal probability to their ACTUAL attacking ceiling. Cape Verde had genuine attackers + a 2-2 pedigree → forced-open goal was live enough that leaning hard on the clean sheet was the miss. Ghana had NO Kudus and worst-in-tournament creation → their forced-open ceiling was genuinely low, so BTTS-no as a lean (not a lock) was right and the clean sheet held. Takeaway for the auditor: after flagging BIAS-10, do not overcorrect into a reflexive BTTS-yes — the must-win dynamic raises the goal chance from the underdog's *own* baseline; a side with no creator stays near-zero even when forced to open up. The tempered-lean posture (not a lock, not a flip) is the calibrated response, and Gate 2 passed it CLEAN on both counts.

### 2026-07-04 — Canada vs Morocco (World Cup 2026, Round of 16)
Predicted: Type D (coin flip with a Morocco lean). Direction — Morocco advance, LOW-MEDIUM confidence. Shape — tight/low, explicitly "a comfortable 2+ goal Morocco win is NOT the modal." BTTS — LEAN YES (Canada's goal framed "earned but contingent" via David behind Morocco's high line). ET/penalty — HIGH, named as a PRIMARY co-equal path (Opta 25.6%), with Bounou's shootout edge. Scoreline indicator — 2-1 Morocco or 1-1→ET (co-equal), 1-0 also live.
Actual: **Morocco 3–0 Canada, won comfortably in 90 minutes.** Canada scored zero; Morocco kept a clean sheet; a three-goal blowout with no extra time.
Category: **Direction success wrapped around a real MISS — BIAS-2 (probability compression) + BIAS-1 (consolation-goal lean).** Direction (Morocco advance) correct and the roof handled right, but shape (predicted tight, was a blowout), BTTS (predicted lean-yes, was a Morocco clean sheet), and ET (predicted PRIMARY, never fired) all missed in the SAME direction: we under-rated Morocco and over-credited Canada. NOT a calibration success.
Rule (reinforced — two lessons we had the evidence for but under-applied): (1) BIAS-2 probability compression. Morocco were ~76% to advance AND had dominant underlying control — they smothered a BETTER attack than Canada's (Netherlands) to 0.33 xG over 120 minutes — while Canada's attack was concretely degraded (Koné OUT, Davies only part-fit; our own squad read said David would be "starved," ~2-4 SoT). That combination should have driven a *more confident* Morocco call — a control win with a plausible clean sheet — not a "tight coin flip, ET-primary, 2+ goals not the modal" framing. We compressed a genuine favourite toward 50/50 and inflated the ET tail. A Type D *lean* is not a 50/50: when the favourite has dominant control metrics AND the underdog's key creators are absent/unfit, resolve toward the favourite, not toward the extra-time tail. (2) BIAS-1 via the Switzerland–Algeria "actual available attack" rule: we leaned BTTS-yes on Canada's transition threat, but the supply chain was broken (Koné, the creator, out; Davies, the pace, compromised) — by our own prior lesson we should have run the ball-control test on the ACTUAL FIT attack and leaned toward a Morocco clean sheet. Canada scored zero. Process watch-point (not a new catalog item — fits BIAS-1/2): possible RECENCY CONTAMINATION — the previous match (Australia–Egypt) was a coin-flip SUCCESS and this draft explicitly reached for "the Australia–Egypt template," which may have primed a coin-flip framing for a game that was closer to a clear-favourite control win. Do not let the last match's archetype set this match's prior.
