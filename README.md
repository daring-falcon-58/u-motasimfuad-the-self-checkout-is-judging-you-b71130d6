# The Self-Checkout Is Judging You

## Methodology (read first)

- **Tournament, not a guess.** 40 candidate lines were generated from fresh angles
  (double-scan accusation, reduced stickers, weighing scales, age checks, loyalty
  points, receipts, meal-deal maths) — deliberately avoiding the live field's
  saturated angles (twelve yoghurts / no spoon / cry for help / "place your feelings
  in the bagging area" / loyalty-card welfare check).
- **Scored against the judge's published criteria, in order:** (1) funny single-line
  remark from a judgmental self-checkout machine, (2) real laugh on a single read
  with a twist a stranger gets with no context, (3) machine's voice, smug and petty
  about the basket and the bagging, (4) tight, no padding, (5) fresh.
  Weighted score C2×3 + C3×2 + C4×2 + C5×1 (max 40). Full table in `tournament.md`.
- **Head-to-head, both orders:** top 8 went through quarterfinals, semifinals and a
  3-round final, each duel judged in both orders. Winner re-confirmed on a fresh read.
- **Blind test:** the tournament above is the blind test — 40 candidates, scored,
  duelled, verdicts recorded per duel in `tournament.md`, not asserted.
- **Collision check:** the winner was checked against all 50 live titles; no duplicate
  or near-duplicate. The double-scan accusation angle appears in no live title.
- **Winner (49 chars):** "I saw you scan that twice. Bold. Wrong, but bold."
  Final verdict: criterion 3 decided it — the runner-up ("ID, please. For the energy
  drink. You look twelve.") could be said by a human cashier; only the machine that
  watched the scan could say the winner.

## The entry

`main.py` writes the winning line to `/output/entry.txt`. The gate requires UTF-8
text of 1–200 characters, not only whitespace; the program asserts the count and
re-reads the file after writing to verify it is byte-identical to the winner.

## Run

```
python3 main.py   # writes /output/entry.txt (49 chars)
```

## Competition

- make.fun — "The Self-Checkout Is Judging You"
  (https://make.fun/c/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
- Deadline 2026-11-26T18:20:00Z; top 10 split $2 (1st $0.63).
- Harness program/v1; judged pairwise by the house judge (stand-up head writer persona).
