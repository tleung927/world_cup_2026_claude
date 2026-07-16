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
11. **Schedule-blind record trust** — treating a headline aggregate record ("best defence
    in the tournament", "2 conceded from 40 shots") as intrinsic quality without asking WHO
    it was compiled against, while under-weighting direct matchup evidence that points the
    other way (e.g., the opposing striker's proven scoring record vs these exact defenders).
    Aggregate stats can be reputation too — the second-order form of BIAS-9. When a
    schedule-soft record meets a schedule-proof weapon, the record is the weaker input.
12. **Extra-time over-prediction in even knockouts** — calling ET/penalty risk HIGH just
    because two sides are evenly matched. Knockouts reach ET only ~1-in-5; single-game
    variance usually separates even sides inside 90 (two straight ET-HIGH calls —
    Mexico–England 3-2 and USA–Belgium 4-1 — both settled decisively in regulation).
    Default an even Type D knockout to "ET is a live ~1-in-4 possibility," not "HIGH."
    Reserve a HIGH ET call for specific low-event/ultra-defensive stylistic evidence,
    not mere parity. Two-sided: don't suppress ET to zero either — calibrate to the base rate.

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

### 2026-07-04 — Paraguay vs France (World Cup 2026, Round of 16)
Predicted: Type B (France clear favourite, Paraguay hard low block). Direction — France win/advance, HIGH confidence. Shape — medium (~2 goals), modal 2-0, capped (no 4-0 blowout), with 1-0 named as "possible but under-rates France." BTTS — NO (France clean sheet the lean). ET/penalty — low-medium, SECONDARY. Scoreline indicator — 2-0 France. Corners read — France win the corner count comfortably (bands France ~7–10, total ~10–12; flagged high-variance).
Actual: **France 1-0 Paraguay, won in 90** (Mbappé penalty, 70', via VAR). Clean sheet; Paraguay had 2 shots / 0 on target and just 54% passing accuracy (the lowest in a WC knockout on record); France were frustrated to 4 shots / 0.15 xG at half-time.
Category: **Calibration success** (with a margin fine-tune). Direction (France advance, high confidence), BTTS(no)/clean sheet, and ET-not-firing all correct; corners direction correct (France dominated a 5-4-1). The exact margin landed at the LOW end (1-0, not the 2-0 modal) — a named possibility and pure exact-digit variance under the prime directive.
Rule (reinforced): This is the corrective counterpart to the Canada–Morocco miss and it LANDED — we respected the favourite (France win, high confidence, clean sheet) WITHOUT overcorrecting into a blowout (capped at ~2, not 4-0), and Paraguay's block did its job. Margin fine-tune for the Type B toolkit: against an EXTREME physical low block (Paraguay 5-4-1, 54% passing — lowest in WC knockout history; France held to 0.15 xG at half and 4 shots), lean the favourite's *modal* toward the LOW end (1-0 over 2-0) — a genuinely elite block caps the margin harder than the quality gap alone implies, and the favourite often needs a set-piece/penalty to break through (Mbappé's 70th-min penalty was the game's only goal). This sharpens BIAS-5: "don't inflate vs a real block" applies to the modal digit, not just to ruling out the 4-0. Corners note (first logged corners read): direction (France win the count) was right; the exact totals likely came in at/below the low end of the band because France were frustrated into a low-event game (4 shots) — a clean live illustration of the "corner direction is knowable, exact count is high-variance" framing.

### 2026-07-05 — Brazil vs Norway (World Cup 2026, Round of 16)
Predicted: Type C (leaky-but-dangerous underdog). Direction — **Brazil to advance, HIGH confidence** (~74% advance implied; decomposed as win-in-90 ~54% = medium-high plus a named ~24% ET tail). Shape — medium. BTTS — YES (earned lean ~55–60%, via the verified-fit Ødegaard/Nusa/Haaland chain). ET/pens — real but secondary. Scoreline indicator — 2-1 Brazil (adjacent 2-0/3-1). Corners — Brazil win the count, total band ~9–12. Gate note: Gate 2 flagged BIAS-2 and the direction label was UPGRADED from medium-high to HIGH.
Actual: **Brazil 1–2 Norway, decided in 90 minutes.** 0-0 until the 79th; Haaland 79' (header, Schjelderup cross) and 90' (low drive from outside the box); Neymar 90'+10 penalty — the last kick of the game. Brazil missed a 13th-minute penalty (Bruno Guimarães, saved by Nyland) and won the chance count by ESPN's full-time xG ~2.73–0.84. Norway's first-ever WC quarter-final; Brazil's earliest exit since 1990. (Corner counts were not published in the sources checked at log time — the corners read is scored as UNRESOLVED, not claimed. A possession split circulating from one auto-extract showed a Norway-possession inversion; it could not be corroborated and is deliberately NOT logged as fact.)
Category: **DIRECTION MISS at the run's highest stated confidence — predominantly variance, plus one under-weighted signal now logged as NEW BIAS-11 (schedule-blind record trust).** Axis honesty: BTTS(yes) RIGHT; ET-secondary RIGHT (no extra time); shape mechanism substantially right (favourite dominated chance quality, clinical underdog struck late — the exact "Morocco blueprint + Haaland's first clean look" path our own watch-list named); the digits "2-1" were right but the WRONG WAY — the purest illustration yet that digits are luck. NOT a calibration success: direction is the headline axis and it was wrong.
Rule (new + reinforced):
(a) **Variance honesty cuts both ways.** A ~74% favourite losing is a ~1-in-4 event, and by chances created (xG 2.73–0.84, a missed 13' penalty) the game-read was largely right — the result swung on a penalty save and two elite finishes. Do NOT overcorrect into distrusting every strong favourite; that just rebuilds BIAS-2 from the other side.
(b) **NEW BIAS-11 — schedule-blind record trust.** Brazil's "tournament-best defence" (2 conceded from 40 shots) was compiled against Morocco/Haiti/Scotland/Japan — no elite finisher faced. Our own draft cited Haaland's 9 goals in 11 club meetings vs Marquinhos/Gabriel as "a real, checkable red flag, not just narrative" — and then still used the aggregate record as the primary clean-sheet/margin support without schedule-adjusting it. Second occurrence of this exact shape in three knockout rounds (Argentina's unbroken group-stage clean-sheet record → conceded twice to Cape Verde). Rule for the auditor: whenever a draft leans on a headline record, demand the "against whom?" adjustment, and when direct matchup evidence conflicts with the aggregate record, the matchup evidence outranks it.
(c) **Gate-2 must stay two-sided.** The BIAS-2 upgrade (medium-high → HIGH) was procedurally defensible — 74% is HIGH territory in this system's own language, and the label change had zero effect on direction. But the case law now contains two upward pushes (Canada–Morocco, this flag) and one tail-hit at HIGH. "Respect the number" must include interrogating whether the number itself rests on schedule-soft inputs (see b) — do not let "don't compress" drift into "always upgrade."
(d) **BIAS-1 inversion, for colour:** the game's actual consolation goal was scored by the FAVOURITE (Neymar, 90'+10, last kick, 1–2). Consolation-goal logic is team-agnostic — a favourite chasing a lost game gets the same unearned-goal scrutiny as an underdog.

### 2026-07-05 — Mexico vs England (World Cup 2026, Round of 16)
Predicted: Type D (coin flip; secondary borderline B). Direction — ~50/50, thinnest lean **England, confidence LOW**. Shape — tight, "a one-moment game," **goals should be scarce** (England's low-block impotence vs Mexico's tournament-best defence: 6 SoT allowed in 4 games, 0.56 xG/game against, 4 clean sheets). BTTS — **coin-flip leaning NO** (0-0/1-0/1-1 the live shapes). ET/penalty — **HIGH, co-primary path** (altitude fade + England's slow knockout starts). Scoreline indicator — 1-1 → ET, co-equal with 1-0 either way. Corners — England edge the count (bands England ~6–8, Mexico ~4–6, total ~10–13). Gate note: first CLEAN pass with the new BIAS-11 schedule check applied to both records.
Actual: **England 3–2 Mexico, decided in 90 minutes** (no extra time). Bellingham 2 (two goals in 98 sec, first half, open play) → 2-0; Quiñones volley → 2-1 HT; Quansah straight red 54' (VAR, England to 10 men); Kane penalty ~60' → 3-1; Raúl Jiménez penalty (VAR on Kane) → 3-2; no equaliser. England advance to the QF vs Norway.
Category: **DIRECTION RIGHT at correctly-LOW confidence (the coin-flip resolved to the thin lean) — but a genuine SHAPE/GOAL-EXPECTATION MISS that is BIAS-11 recurring.** Axis honesty: Direction — RIGHT (England advanced; a thin LOW-confidence lean, so limited credit, but the headline axis landed and no confident winner was forced — clean Type D behaviour). Margin — RIGHT in one sense (one-goal final, 3-2, "one-moment game" via a red card and two penalties) but the "**goals scarce**" texture was WRONG (5-goal game; already **2-1 at halftime in open play**, before the red card). BTTS — WRONG (leaned no; both scored). ET — WRONG (HIGH co-primary didn't fire; settled in 90). NOT a clean calibration success — direction landed but the whole low-scoring/BTTS-no/ET-likely texture was the opposite of what happened.
Rule (reinforced + sharpened):
(a) **BIAS-11 sharpened — a schedule-soft flag must MOVE the call, not just appear in the prose.** The draft explicitly noted Mexico's clean sheets "came against no Kane-tier attack" and England's Ghana impotence was "a one-game sample" — it did the *first half* of BIAS-11 (flagged the softness) but then still built the shape call ("goals scarce," "BTTS lean no") on that same fortress record. England scored twice in open play in the first half against the "tournament-best defence." Rule for the auditor: when a draft flags a headline record as schedule-soft, verify the flag actually changed the goal-expectation/BTTS/margin call. A softness note that is written and then overridden is the flag failing, not passing. Direct matchup evidence (Kane/Bellingham tier vs a soft-schedule clean-sheet record) should have pushed goal-expectation UP.
(b) **Confound honesty (do not over-attribute to the red card).** Two of the five goals were penalties and the 54' red card opened the game — real variance that inflated the count. BUT it was already 2-1 at halftime, in open play, before the red — so the defensive read was refuted *before* the confounds arrived. The shape miss is real, not a red-card artifact; resist the urge to excuse it entirely on the sending-off.
(c) **ET-HIGH has now failed to fire in consecutive R16 coin flips** (Paraguay–France, Mexico–England both settled in 90). This is a SMALL SAMPLE within probability — two independent ~40% ET calls both not firing is ~36% likely, entirely normal. Do NOT start suppressing ET calls in Type D knockouts to "correct" this; that would just rebuild a bias from the other side (cf. BIAS-11(a) variance-honesty-cuts-both-ways). Logged as a watch-point, not an actionable change.
(d) **The situational-underdog offsets under-delivered, but the lean was still right.** Mexico's altitude + 80k crowd + perfect defensive record were credited as full offsets to England's talent to reach 50/50; England won anyway, with 10 men, "overcoming hostility and altitude" (match reports). The thin-lean-England was vindicated — no overcorrection needed — but it's a reminder that stacking situational factors for a host can over-flatten a real talent edge. Not a new bias; a calibration note that the LOW-confidence England lean, if anything, could have been a touch firmer.

### 2026-07-06 — USA vs Belgium (World Cup 2026, Round of 16)
Predicted: Type D (coin flip). Direction — NO confident winner, LOW confidence; faint lean **USA** on the one "concrete asymmetry" (Belgium's 120-min fatigue vs Senegal + home crowd → a late-game/ET tilt on legs). Shape — **tight, "one goal or less, decided by a lapse rather than a gulf in class."** BTTS — **YES**. ET/penalty — **HIGH** ("named, not decorative"). Scoreline indicator — 2-2 into extra time (regulation 1-1/2-1 either way). Corners — marginal Belgium, total ~9-12.
Actual: **Belgium 4–1 USA, decided in 90 minutes** (no extra time). De Ketelaere 2 (both first half); Tillman free-kick briefly made it 1-1; Belgium restored the lead ~1 min later; Vanaken 57' off a Matt Freese error → 3-1; Lukaku 90'+ → 4-1. "Embarrassing defensive mistakes" (Yahoo). Belgium advance to the QF vs Spain.
Category: **NOT a calibration success — a real miss. Direction lean WRONG, shape WRONG (tight → 4-1 rout), ET WRONG (HIGH, nowhere near); only BTTS right. Primary actionable: NEW BIAS-12 (extra-time over-prediction in even knockouts). Secondary: overriding the one model number with a soft fatigue narrative.** Axis honesty: Direction — the faint lean pointed at USA; Belgium won by three. BUT no confident winner was forced — **BIAS-7 did NOT fire** (calling it a coin flip was correct; the error is the *direction and reasoning* of the faint lean, not false certainty). Shape — badly wrong on paper (predicted "decided by a lapse not a gulf in class"; got a gulf), but **primarily VARIANCE** (see rule c). BTTS — RIGHT (Tillman scored; both scored). ET — WRONG (HIGH didn't fire; a 4-1 is the opposite of a long, tight game).
Rule (NEW + reinforced):
(a) **NEW BIAS-12 — extra-time over-prediction in even knockouts.** My two explicit ET-**HIGH** calls are now **0-for-2** and both games were multi-goal decisive, not close: Mexico–England 3-2 and USA–Belgium 4-1, **both settled in 90**. (This corrects the Mexico–England note (c), which lumped in Paraguay–France — that was a correctly-**LOW** ET call that stayed in 90, not an ET-HIGH miss; the real pattern is the two HIGH calls above.) Base-rate fix: knockout games reach extra time only ~1-in-5; **"two evenly-matched sides" does NOT push ET to HIGH** — single-game variance (an early goal, one defensive meltdown, individual quality) usually separates even sides inside 90. Rule for the auditor: default a generic Type D coin flip to **"ET is a live ~1-in-4/-5 possibility,"** not "HIGH/co-primary." Reserve a genuinely HIGH ET call for **specific low-event/ultra-defensive stylistic evidence** (two sides who both prioritise not-losing, low xG for/against), not mere parity. Two-sided guard: do NOT swing to suppressing ET to zero — a coin flip CAN go long; the fix is calibrating to the base rate, not deleting the call.
(b) **Respect the one model number over the soft narrative** (CLAUDE.md hard rule "respect the model probability"; BIAS-2/9 spirit). The only quantitative model (Squawka 57% Belgium) leaned Belgium; the market was near-even. I flattened the model to 50/50 ("model-market disagreement = balance") and then leaned **faintly USA** on a fatigue + home-crowd story — overriding the one number that pointed at the eventual winner. Belgium's supposed "120-minute fatigue" never showed (De Ketelaere bagged two in the first half; Lukaku scored in the 90th+). When your only model number points one way and you lean the other on a narrative, you are overriding evidence with a story: the lean should have been faintly Belgium or truly neutral, **never USA**.
(c) **Shape miss = primarily VARIANCE; do NOT overcorrect.** A 4-1 out of a ~50/50 is a tail outcome, aggravated by USA individual errors (Freese's gift for 3-1). The near-even market and the 57% model predicted a rout for *nobody* — calling the game "tight" was reasonable ex-ante. Do NOT start predicting blowouts out of coin flips; that just rebuilds BIAS-2/BIAS-7 from the other side. Honest headline: the coin landed hard, plus the two calibration lessons (a, b).
(d) **Gate honesty — a soft narrative passed all three gates.** The faint-USA fatigue lean was actively **endorsed by the CEO gate** ("a sharper, more defensible lean"). A freshness story cleared classifier, bias-audit, and CEO and was still wrong. Antidote: the model number outranks a fatigue/freshness narrative at every gate — Gate 3 should *challenge* a narrative-based lean that contradicts the one model probability, not reinforce it. BTTS-yes was the single axis all gates got right.

### 2026-07-07 — Argentina vs Egypt (World Cup 2026, Round of 16)  *(logged retroactively — skipped in the 07-08 postmatch run, which picked USA–Belgium; filling the gap for loop integrity)*
Predicted: Type C (strong favourite, leaky-but-dangerous underdog). Direction — Argentina win/advance, MEDIUM-HIGH. Shape — medium, "Argentina by one-to-two goals, NOT a blowout." BTTS — YES (moderate), earned; and the *mechanism* was named: "Egypt's goal most likely comes from a transition or **set-piece** moment, not sustained buildup." ET/penalty — MEDIUM (~18.5% Opta), explicitly not high. Scoreline indicator — 2-1 Argentina (2-0/3-1 live). Corners — low-count, Argentina, ~7-10.
Actual: **Argentina 3–2 Egypt, decided in 90 minutes.** Egypt led 2-0 (Yasser Ibrahim 15', Mostafa Zico 67') before an Argentina comeback in the last 11 min: Romero 79', Messi 83' (record-extending 21st WC goal, after missing a first-half penalty), Enzo Fernández 90'+2' header. Both Egypt goals came from crosses/set-pieces into Argentina's aerial vulnerability — exactly the named route. Argentina to the QF.
Category: **Calibration success.** Direction RIGHT (Argentina advanced, medium-high). Shape RIGHT (narrow one-goal final, not a blowout — the "medium" call held on the *final shape* even though the game's *path* was dramatic). BTTS RIGHT — and earned via the **exact predicted mechanism** (Egypt scored twice from set-pieces/crosses vs Argentina's aerial weakness, not a gifted consolation → clean anti-BIAS-1/BIAS-11 execution). ET correctly held MEDIUM and stayed in 90 (the ~82% base-rate outcome — a correctly-calibrated low ET call, the positive counterpart to the USA–Belgium ET-HIGH miss). Only the exact digits (2-1 vs 3-2) were off, and 3-1 was a named alternate — pure luck under the prime directive.
Rule (reinforced): (a) **Predict final SHAPE, not game PATH.** "Medium / narrow one-goal Argentina win" was right despite Egypt leading 2-0 at one point — the scoreline path (0-2 then three goals in 11 minutes) is exactly the kind of within-game variance we correctly do NOT try to call; the defensible axes (direction, final margin band, BTTS-via-mechanism) all landed. (b) **Naming the mechanism is what makes a BTTS-yes honest** — "Egypt scores from set-pieces into Argentina's aerial weakness" is checkable and it happened twice; this is the BIAS-1 antidote working (a route, not a name). (c) The **schedule-adjusted "no automatic Argentina clean sheet"** (BIAS-11, from the Cape Verde concessions) was vindicated hard — Argentina conceded twice again. Both Egypt goals from the aerial route also became the load-bearing input for the very next prediction (Argentina–Switzerland), where the same Argentina aerial weakness was cited — the loop feeding forward correctly.

### 2026-07-11 — Argentina vs Switzerland (World Cup 2026, Quarter-final)
Predicted: Type B (clear favourite vs hard low-block). Direction — Argentina win/advance, MEDIUM-HIGH. Shape — tight-to-medium, "Argentina by one-to-two goals (1-0/2-1), NOT a blowout." BTTS — genuine ~50/50, faint lean YES (Switzerland's goal earned via a set-piece/transition route into Argentina's aerial weakness; 1-0 clean sheet also live). ET/penalty — **MEDIUM (~24% Opta), the legitimate BIAS-12 exception** (bona-fide low-event Swiss side, 210 scoreless knockout minutes), explicitly anchored to the model, NOT inflated to high. Scoreline indicator — 2-1 Argentina (1-0/2-0/0-0-into-ET all live). Corners — Argentina 60/40, ~8-11.
Actual: **Argentina 3–1 Switzerland (after extra time).** Mac Allister 10' (1-0); Ndoye 67' (1-1); **1-1 after 90 → extra time**; Álvarez 112' (2-1, long-range strike); Lautaro 120'+1' (3-1, last kick — a report noted it "only served to make the 3-1 look easier than it was"). Effectively a one-goal game until the final seconds. Argentina to the semi-final vs England.
Category: **Calibration success — and the two-sided vindication of BIAS-12.** Direction RIGHT (Argentina advanced, medium-high). Shape RIGHT (tight, decided late, one-goal margin for 119 minutes — NOT a rout; the France–Paraguay "narrow favourite vs a block" template held). BTTS RIGHT — Switzerland took their ~one real chance (Ndoye), exactly the "functional, one-or-two-chances, not zero" framing, not a gift. **ET call RIGHT — the headline lesson:** having *just* created BIAS-12 off the USA–Belgium ET-HIGH miss, the very next knockout was correctly identified as the *legitimate low-event exception* — ET kept at MEDIUM on stylistic grounds (not reflexively high, not suppressed to zero), and the game **went to extra time.** Scoreline indicator 2-1 was literally the score until 120'+1'.
Rule (reinforced): (a) **BIAS-12 is two-sided and it worked both ways within four days.** USA–Belgium: "don't reflexively call ET-high in a generic coin flip" → 4-1 in 90. Argentina–Switzerland: "DO keep ET live (medium) when there is genuine low-event/ultra-defensive stylistic evidence" → 1-1 into extra time. The lesson was never "call less ET" — it was "calibrate ET to the *style and the model number*, not to reflex." This is the cleanest possible confirmation that the carve-out in BIAS-12 is correct, not a hedge. (b) **Type B margin discipline held again** (cf. Paraguay–France 1-0): against a proven block, capping the favourite at a narrow one-to-two-goal win — and refusing the rout the #1-vs-#19 gap might tempt — was right; the 3-1 *looks* like a two-goal win but was a one-goal game decided by an extra-time moment of magic (Álvarez's strike), exactly the "needs a moment to break the block" read. (c) **The forward-fed input paid off:** citing Argentina's aerial/defensive vulnerability (proven by both Egypt goals) to keep BTTS at a genuine ~50/50 rather than crediting a clean sheet was again vindicated — Switzerland scored.

### 2026-07-15 — Argentina vs England (World Cup 2026, Semi-final)
Predicted: Type D (two strong sides, coin flip). Direction — genuine coin flip, **marginal lean ENGLAND, confidence LOW** (Opta ~52/48 England to advance; lean taken *because the model pointed there* + a mechanism — England's aerial/set-piece threat into Argentina's proven knockout-long aerial leak — explicitly NOT a Messi-narrative override). Shape — tight/medium, one-goal-or-less, plausibly into ET, not a blowout. BTTS — YES. ET/penalty — MEDIUM (~29% Opta), cited directly, not inflated; if pens, Argentina team-pedigree edge. Scoreline indicator — 2-1 England, with "1-1/2-2 into ET **and 2-1 Argentina** all equally live."
Actual: **Argentina 2–1 England, decided in 90 minutes.** Gordon 55' (England 1-0); **Argentina scored twice in six minutes** — Enzo Fernández 85' (20-yard strike, Messi assist) and Lautaro Martínez 90'+2' (header from a Messi cross). Argentina come from behind AGAIN and reach the final vs Spain.
Category: **LOW-confidence coin-flip DIRECTION MISS — pure variance, NOT a bias, NOT a process error.** Every non-direction axis was RIGHT: Shape RIGHT (2-1, one-goal, tight, not a blowout). BTTS RIGHT (both scored, earned on both sides). ET RIGHT (held MEDIUM ~29%, stayed in 90 — the ~71% base-rate outcome; textbook BIAS-12 calibration, the opposite of the USA–Belgium reflexive ET-HIGH). Scoreline shape RIGHT to the exact digits — the call was **2-1 and 2-1 Argentina was explicitly named as equally live**; it finished 2-1 Argentina. The *only* wrong axis is the marginal lean (England), and the model (52/48) leaned the same way and was equally "wrong" — a 52/48 call resolving to the ~48% side is expected ~half the time. BIAS-7 did NOT fire (LOW confidence, coin flip named, no forced winner).
Rule (reinforced — and an explicit anti-overcorrection guard):
(a) **Do NOT overcorrect this into "we should have trusted the Messi/Argentina narrative."** The post-USA–Belgium lesson was "respect the model number, don't override it with a narrative" — and that is exactly what this draft did (leaned England because the model did). Had we instead leaned Argentina on a Messi-clutch story and been "right," it would have been right *for the wrong reason* and would have rebuilt the very bias (narrative-over-model) that USA–Belgium taught us to kill. A correctly-priced coin flip landing on the other side is NOT evidence the process was wrong. Respecting a 52/48 model does not mean the 52% side wins — it means over many such calls you're calibrated; individual ones are luck.
(b) **A LOW-confidence direction miss with every other axis right is the system working as designed, not a failure.** The prime directive is "confident about direction *when there is an edge*, honest about luck when there isn't." Here there was no real edge (52/48), we said so (LOW, "genuine coin flip" as the headline), and we nailed shape/BTTS/ET/scoreline-shape. This is close to the best a coin flip can be scored — do not self-flagellate over the one variance axis.
(c) **Observation for the final (not a bias): Argentina's late-surge/comeback trait is now a real, repeated pattern** — decisive goals at 79'+83'+90+2' (Egypt, from 2-0 down), 112'+120+1' (Switzerland, in ET), 85'+90+2' (England, from 1-0 down): four straight knockouts won by scoring late and/or from behind. This is high-variance and partly survivorship (we only see the wins), so it does NOT justify overriding a model coin flip — but it is a genuine, checkable team trait: **do not treat Argentina as beaten while the game is within one goal, even late.** Carry this as a watch-note into the Argentina–Spain final, weighted as a tie-breaker, not a lean.
