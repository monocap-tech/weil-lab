# NF636 — moment-derived original payments PASS; integer-only Taylor gates

## Confirmed major numerical milestone
NF621 complete schedule run 44338849733, transformed-payments job 134968354605 SUCCESS. Full NF622 moment-derived physical matrix artifact 14448816424 and immutable original frame artifact 14443252637 used. Exact finite rational result: row defect bound <= 1/100 PASS and selected payments 242/242 PASS. Retained receipt nf623-moment-payments, artifact 14454853220, zip digest sha256:24fb793dd5f3f91b6afe0283641e32c44bf9e6274a3dd31e52a709dc2c6e0907. This is the first complete moment-derived finite payment success, separate from the earlier Arb baseline. It remains conditional on analytic enclosure validity; not a Lean proof of the original solve. NF631 reference-compatible widening/payment rerun and the newer endpoint jobs were still queued at initial inspection.

## Computational pivot
Avoid normalizing large rational expressions inside Taylor segments. Store a ball as integer center and radius units at Q=10^2600. To certify a directed rounded scaled numerator m and radius numerator r over positive integer d, require
  c*d <= m < (c+1)*d,
  (R-2)*d < r <= (R-1)*d.
The second bracket is exactly ceil(r/d)+1, retaining the incumbent +1 radius fee. The checker calculates integer quotient proposals and independently checks these brackets. No approximation, no unchecked quotient, no native oracle. For multiplication, d=Q, m=xy, r=|x|s+|y|t+ts for input radii t,s. For division, d is the positive jet degree. Candidate proofs attach the integer checks to the original NF591/633 exact rational rounded step, then compose entire segments through the existing prefix theorem. The new gates do not require rational arithmetic in the concrete transition checker. This is a feasibility intervention, not a measured speedup.

Independent BigInt experiment in-session reproduced both full original 1200-step Taylor cases (h=1 and f=37/32), plus final rounded squarings. All 14,412 integer floor/ceil brackets passed; all 57,648 one-unit center/radius mutations were rejected. Final radius pairs agree with NF633: (8330,8330) and (49418,48736) units. New Python emitter proposes four genuine initial/terminal 32-step comparisons and one corrupted terminal state per segment, checked only by kernel evaluation. Terminal starting states remain proposals. Python emitter and new Lean proofs not executed in-session; generic theorem and actual local truth await CI, no full endpoint proof or performance measurements yet.

No main merge. No global Weil positivity or RH promotion.
