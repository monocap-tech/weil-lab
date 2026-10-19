# MG09 — Certified original endpoint-remainder strong Fourier tail

October 19, 2026. Method gate for original W-ODD-NEG OPEN; even, Weil, CC27 and RH OPEN. Stacks on MG08 #257, whose physically sampled diagnostic passed Actions 39334386411.

## MG08 measurement and motivation

MG08 measured 25 original physically supported SI10 source directions with all genuine original 107 negative blocks / 890 columns and 14 SI29 reference functions. The sampled strong residual squared trace was 0.835747 (4096 points) and 0.835824 (8192 points); the MG07 reference-weighted residual Gram was around 0.02848 of the scalar baseline, but generalized t=1 residual bounds remained around 3.7 billion, vastly above the **conditional** whole-470 acceptance threshold 51/56. These are numerical, not rigorous original resolvent measurements.

SM41 had already rigorously bounded the original supported odd positive multiplier by a_o(xi) <= 17+ln|xi| for |xi|>=1. On the selected true SI10 25 physical Fourier transforms it established |Tf_j(xi)|<=u_j/|xi| for |xi|>=2 max cluster center, with u_j=1/2 (sine degree 0), 7/10 (xcos degree 1), 2/5 (odd sinh pole). Thus the ENTIRE source strong high tail is bounded in Loewner order by C_SM41(Lambda)=O((ln Lambda)^2/Lambda). The scalar high tail is expensive at small target residual norms.

## New exact integration-by-parts endpoint split

For the genuine original physical zero-extended source f supported [-B,B], B=11/10, twice integrate by parts:

T_f(xi)= -(f(B)exp(-2 pi i xi B)-f(-B)exp(2 pi i xi B))/(2 pi i xi) + E_f(xi),

E_f(xi)= -(f'(B)exp(-2 pi i xi B)-f'(-B)exp(2 pi i xi B))/(2 pi i xi)^2
        + (2 pi i xi)^-2 integral[-B,B] f''(x)exp(-2 pi i xi x) dx.

Consequently |E_f(xi)| <= D_f/(2 pi |xi|)^2, with D_f=|f'(B)|+|f'(-B)|+integral[-B,B] |f''(x)| dx. The first 1/xi JUMP TERM IS NOT LOST OR DECLARED ZERO. This is only the remainder after removing it.

MG09 uses exact rational SI10 cluster center c, B and pi upper to enclose the original selected 25 generators:
- sine degree 0, w=2 pi_upper c: D_f <=2w+2B w^2;
- xcos degree 1: D_f <=2+6B w+B^2 w^2;
- original sinh pole: D_f <2+B/2, using B/2<ln2.

For Lambda=2^k, k>=11, upper-bound ln Lambda by k*(347/500), put v=17+k*(347/500), and D2=sum_j D_j^2. The complete-source coefficient-norm remainder strong-action inequality is

|| a_o(xi) sum_j z_j E_j(xi) ||^2_(|xi|>Lambda)
 <= C_remainder(Lambda) ||z||^2,

C_remainder(Lambda) = [2 D2/(6^4 Lambda^3)] * [v^2/3+2v/9+2/27].

The exact elementary integral of (17+ln xi)^2/xi^4 on [Lambda,infty) is responsible for Lambda^-3. This new 25-source operator upper is valid on every source combination. Crucially it bounds ONLY the endpoint-peeled remainder, NOT the full positive action or the jump contribution. The explicit jump still needs independent certified oscillatory covariance, as do low-frequency signed/positive source integrals. No complete strong Galerkin residual is constructed.

The validator independently replays SM41's full original 25-source bound at dyadic cutoffs and calculates rational cutoff thresholds for several illustrative source-coefficient-squared targets. Its tiny target 311/10^14=3.11e-12 is an SM35 conditional scalar tolerance comparison, not a necessary original whole-source condition. The dyadic crossing of the remainder-only bound MUST NOT be confused with a crossing of the original full tail.

## Acceptance and strategy

Successful exact-rational arithmetic establishes the original-scope endpoint separation and a true fast-decaying remainder. The remaining gate is to certify the *explicit leading endpoint jump action and all cross interactions* through complete original physical Fourier covariance, plus rigorous positive/signed low band. If those can be paid without excess scalar loss, attach a true original-source strong residual and then expand to 470 source coefficients. Otherwise refine boundary subtraction or switch to sourcewise analytic Fourier transforms. Original form/domain identity, complete odd/even Weil and RH are open.

Reproduce with python scripts/validate_rpb108_mg09_original_endpoint_tail_budget.py.
