# NF590 — canonical original jet recurrence and analytic identification

Stacked on NF589 #620. New Lean proofs and ungrouped Arb replay are pending.

## New verified receipts

NF589 run 44128563458 job 134199008546 has completed. The independent elementary complex disc majorants module passed (actual imaginary-part sine/cosine bounds, sinh bound, normalized disc geometry, oscillator bound). The entire canonical normalized Cauchy coefficient series module passed, including the circle estimate, the real value series and the differentiated series. These are two substantive accepted analytic components. The original finite source sum and full-box disc theorem are not yet accepted.

The same job reports original frozen-source regularity failure (large node-list equality recursion and nested array indexing lexer), normalized tail failure (only two rational-to-real large-power comparison casts), and consequent budget/complexification failures. NF590 repairs nested indexing throughout source, disc and recurrence modules, increases recursion/heartbeat budget for the exact node comparison, and uses exponentiation.threshold 1000 for the exact rational-power arithmetic in the real tail theorem. No new Lean acceptance is inferred from these changes. NF589 endpoint job 134199007847 reported twisted panel failure; other endpoint steps still running at inspection. Graph correction failure remains unresolved. NF588 numeric job 134199013298 has completed SUCCESS again, including direct full-box recomputation and all-400 ceiling/budget audit.

## Exact recurrence of the literal source

Let B=11/10, D=-1/500. For any complex lambda define e_0(lambda)=1, e_{n+1}(lambda)=e_n(lambda) lambda/(n+1). This is lambda^n/n! and its power series sums to exp(lambda w). Multiply by the finite binomial polynomial (B+D w)^k using zero-padded shifts. The nth coefficient is exactly
C_n(B,D,lambda,k)=sum_{m=0}^{min(k,n)} choose(k,m) B^(k-m) D^m e_{n-m}(lambda).
For omega=2*pi*f, lambda=i*omega*D and alpha=-i for even k, 1 for odd k, the original real oscillator coefficient is Re(alpha exp(i omega B) C_n). This is exactly the oscillator coefficient architecture of NF587. The genuine sinh pole coefficient is Re(exp(11/20)e_n(-1/1000)-exp(-11/20)e_n(1/1000))/2; this is the exponential-difference form of the earlier parity recurrence.

The new generic recurrence module develops HasSum identities, polynomial shifts and finite sums. Its real-series uniqueness lemma uses a radius at least 1 (from convergence of each coefficient sequence at w=1) and Mathlib's uniqueness of formal multilinear series. The original source module sums all 242 original selected generators and four complete critical shapes, proves the real series represents the original U(B-w/500), and identifies its sequence with neutralNF588NormalizedCoefficient for ALL n by uniqueness. No cutoff, source bound or imported intervals are required for this identity. All new proofs pending.

The terminal candidate neutralNF590SourceBounds_of_recurrence replaces the canonical-Cauchy-jet inequality premise by the explicit recurrence inequality, for the same a,b in the frozen box. It does not assert that the numerical interval is a proved Lean inequality.

## Numerical custody

New independent ungrouped interval script computes all 374 primitive contributions (242 selected plus 4*(32+1) critical contributions), retaining the same primitive coefficient boxes and true pole, with the two exponential recurrences rather than the parity pole implementation. No grouped-coefficient assumption or previous interval input. It checks directly that all 400 prior upward-rounded ceilings dominate the new intervals and that U(B)<-1e-11. This is an implementation-matching numerical verification, not a new refinement of the source. New CI pending; no local replay or compiler build this pass.

The remaining proof obligation is a Lean-checkable transcendental interval enclosure for this explicit finite recurrence, plus the original correlated solve's membership in its archived coefficient box; the exact full-disc assembly and terminal graph correction still need compiler recovery. No main merge. Full signed Weil coercivity, W_ODD_NEG and RH remain OPEN.
