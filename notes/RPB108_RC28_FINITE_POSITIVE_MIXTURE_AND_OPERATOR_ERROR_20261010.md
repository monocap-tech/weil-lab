# RPB108 RC28 — finite positive-mixture approximation with whole-operator error

2026-10-10. Independent research/rpb108-route-consolidation.
Recovered parent: 074fc96f518efa9ba30704327333ab5af0953174 (RC27).
No other research branch is changed.

## Result

At B=11/10 there is an explicit sum Q of 210000 positive Cauchy
operators such that, on physical L2([-B,B]),

    Q - (1/10000) I <= K_B <= Q + (111/250000) I.

In particular ||K_B-Q|| < 1/2000. This is a whole-operator bound,
not an entrywise error or a sampled spectrum. The atoms have not
been evaluated; Q is not a finite-rank operator on physical L2.
Its compression to any finite polynomial trial space is a finite matrix.

## Definitions and small/large tails

Use RC27's C_t(r)=2/(t^2+4 pi^2 r^2) and positive mixture
K=integral_0^infinity (1-exp(-e t)) C_t dt, restricted to the interval.

For delta>0 the small-t operator has whole-line multiplier bounded by

    integral_0^delta (1-exp(-e t))/t dt <= e delta.

Thus 0<=K_small<=e delta I on supported L2, even though the
individual density becomes singular as t approaches zero.
For T>0 use C_t(r)<=2/t^2 and 1-exp(-e t)<=1. The large-t
kernel is bounded by 2/T. Each interval row has length 2B, so
Schur's test gives 0<=K_large<=4B/T I.
These bounds include all endpoint support contributions.

## Logarithmic midpoint sum and error

Set s=log t, a(s)=1-exp(-e exp s), b_u(s)=exp(-u exp s).
The middle mixture has Fourier multiplier
integral_(log delta)^(log T) a(s)b_u(s) ds, u=|xi|.

a increases from 0 to 1 and b_u decreases from 1 to 0 for u>0.
For u=0, b_u=1. For every u>=0,

    integral_R |(a b_u)'| ds
       <= integral_R a' ds + integral_R (-b_u') ds <= 2.

This variation bound is independent of both frequency and interval
length. On a bin of length h with midpoint c, integrating
|g(s)-g(c)| and reversing the integration of |g'| gives a bound
(h/2) integral_bin |g'|. Summing bins gives midpoint error <=h.

Let L=log(T/delta), h=L/N, s_j=log delta+(j+1/2)h, t_j=exp s_j.
Define the physical operator

    Q = sum_(j=0)^(N-1) h t_j (1-exp(-e t_j)) C_(t_j).

Each weight is positive, and its whole-line multiplier is
h a(s_j)b_u(s_j). Hence Q>=0. Plancherel and the uniform
multiplier error prove ||K_middle-Q||<=h before interval restriction.
Compression to the supported interval preserves this norm bound.

Combining this with the positive tails yields

    Q-hI <= K <= Q+(h+e delta+4B/T)I.

No assertion that midpoint quadrature itself is a lower sum is used.

## Certified concrete budget

Take delta=1/10000, T=100000, N=210000. Then T/delta=10^9.
The rational positive exponential partial sum through degree 12
at 7/3 exceeds 10, proving log 10<7/3, hence L<21 and h<1/10000.
Together with e<3 and B=11/10,

    e delta <3/10000,
    4B/T=11/250000,
    h+e delta+4B/T <111/250000 <1/2000.

The standard elementary e<3 bound follows by summing its exponential
series and bounding the factorial tail geometrically.
All constants used here are analytic inequalities, not floating estimates.

## Trial metric interface

For the RC26 physical polynomial mass matrix D, define Q_trial by
the EXACT bilinear integrals of the operator Q. Then

    Q_trial-(1/10000)D <= K_trial
      <= Q_trial+(111/250000)D.

Adding RC26's scalar and exact singular/endpoint components gives

    L_RC26+Q_trial-(1/10000)D <= G
      <= U_RC26+Q_trial+(111/250000)D.

This is an explicit, arbitrarily dimension-independent enclosure
recipe for the complete physical trial metric. It is not yet an
evaluated enclosure matrix. If a computed matrix Qhat has certified
mass-metric error eta, add eta D to both error margins.
An entrywise error eta does not automatically establish that bound.

These are physical trial metrics, not the canonical Riesz Gram
matrices required by RC22/RC23. A small physical source residual is
still needed after a trial solve. The scalar width from RC26 remains
part of the complete metric error budget.

## Validation, cost, and next obligation

Run scripts/validate_rpb108_rc28_positive_mixture.py.
Executed locally: PASS, 12 exact rational budget/interface controls.
The all-frequency variation estimate and both tail estimates are
proved above; these are not numerical tests.

210000 atoms is a conservative explicit cost. Each atom still needs
its polynomial bilinear integrals, and its transcendental parameters
require certified enclosure. No atoms or actual matrix entries have
been computed in this pass. This cost is not the 8600-feature native
head dimension and does not reduce it.

Next: evaluate the low-mode Q_trial matrix with an additional
certified numerical/integration budget, or sharpen the quadrature
to reduce cost. Actual Riesz inversion, whole weak residuals and
native head/source certification remain open. No new original Weil
positivity aperture, RH/F4 theorem, or Lean closure is claimed.
