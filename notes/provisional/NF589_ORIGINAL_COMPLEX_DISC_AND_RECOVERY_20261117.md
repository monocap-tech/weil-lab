# NF589 — original full-box complex-disc majorant and recovery

Stacked on NF588 #619. New Lean scripts remain compiler-pending.

## Verified receipts

- NF582 run 44114733587 job 134149591640 completed SUCCESS, including the actual half-carrier uniform strip and fixed sample limit. NF586 run 44114730820 job 134149583233 independently accepted half and odd sequence Fourier transport, plus all preceding logarithmic split, twisted derivative and Schwartz seed packaging. Thus the actual odd approximation family is now formally endowed with the conditional uniform strip bound and pointwise scalar convergence.
- NF588 run 44114730860 job 134149585740 completed SUCCESS: another direct primitive full-box 4096-bit interval replay and the independent 400 normalized ceiling and both exact budgets audit. No new numerical algorithm or refinement needed.
- NF583 run 44114730159 job 134149579530 accepted Gram, actual L2, exact Fourier transport, scale, Schwartz packaging and full conditional physical graph. Terminal seed attachment failed on one redundant tactic and two let-bound window/physical unfolding rewrites. Repairs committed.
- NF588 Lean job 134149586329 failed on weighted-tail association, two large-power rational comparisons, explicit shifted-sequence inference, Nat binder inference, and two Cauchy series API details. Repaired all observed diagnostics, using exact rational kernel decisions for large-power tails. NF587 data module timed out during elaboration of 241 rational nodes; raise heartbeat budget, preserving exact source values. Twisted panels failed on the |* lexer; repair whitespace.
- NF586 correction job 134149582640 still failed at mkContinuous because of source graph typeclass mismatch, physical synthesis change, and large elaboration timeout. No claim of completed correction; not modified further in this pass.

## New literal complex disc chain

For normalized complex w, |w|<=20, put x=B-w/500. Then |x|<=2 and |Im x|<=1/25. All original oscillator frequencies satisfy 0<=f<=883 and k<=13. Bound the sine and cosine directly with their exact exponential identities:
|sin z|, |cos z| <= exp(|Im z|).
Since |Im(2 pi f x)|<=2*4*883/25<283 and exp(1)<3, the individual oscillator norm is <= Q=2^13*3^283. The genuine sinh pole obeys |sinh(x/2)|<=exp(|x/2|)<=3<=Q. Each complete critical shape is bounded by 33 Q, since its 32 rational sine and one rational sinh coefficients have absolute value <=1. For arbitrary real coefficients in the original primitive box, midpoint+radius <=10^143 implies each coefficient has absolute value <=10^143. Therefore the exact original complex source satisfies
|F(w)| <= (242+4*33)*10^143 Q <= 400*10^143 Q <=10^400.
This is a full closed-disc bound, not a finite set of sampled points or an enclosure of a different polynomial.

Implemented three candidate modules: elementary complex bounds, literal full-source sum from finite scalar inequalities, and separate exact rational kernel decisions transferring the frozen primitive box to those inequalities. With this chain the new collar theorem requires only box membership and the first 400 canonical Cauchy coefficient bounds. Full formal identification of the Arb Taylor coefficients with the canonical Cauchy coefficients and a Lean-checkable transcendental interval certificate remain pending; the repeated Arb/Fraction audit is not a proof term. Exact original correlated-solve coefficient custody remains separate.

No local Lean build, no main merge. All NF589 proofs unverified. Full signed Weil coercivity, W_ODD_NEG, RH OPEN.
