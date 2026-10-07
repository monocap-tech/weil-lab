# RPB-108: combined prime power-four bound and actual positivity at 93/100

The analytic/rational aperture lane now certifies the actual whole native form
on D_(93/100), with all 84 physical degrees and all nine source panels retained:

- Q(h) >= 9e-28 ||h||_2^2;
- Q(h) >= 3.9e-30 Elog(h), where Elog has weight log(exp(1)+abs(xi)).

These are rounded-down consequences of the exact rational certificate. This
closes the fixed-aperture weak kernel and unit domination at 93/100. It does
not close the global endpoint, infinite-divisor transport, historical packet
attachment, F4, or Lean assembly. Lean files are unchanged.

## Why the previous scalar estimator failed

The original two-band complement lower bound was 2/3. An exact rational
negative direction for Q-(3/2)R is archived with an independent endpoint-sum
audit. Its estimator Rayleigh upper is approximately -1.08514e-25, whereas
its actual native physical energy is positive (Rayleigh lower 4.05353e-24).
This is an obstruction to that sufficient scalar estimator, not a native
counterexample. No negative conclusion about the full form follows.

## Combined prime operator, with every intermediate support test

Let I=(-93/100,93/100), and extend functions by zero outside I. Define the
bounded self-adjoint translation operator

T h(x) = sum over n in {2,3,4,5} of A_n [1_I(x+log n) h(x+log n)
                                      +1_I(x-log n) h(x-log n)],

where A_n=Lambda(n)/sqrt(n), including Lambda(4)=log(2). Its native prime
contribution is -<h,T h>. This expression is on the physical support carrier;
no divisor sampling identity is assumed. Since log(5)<2a<log(7), these are
exactly the active prime powers.

T has a nonnegative kernel in the order sense; positivity as a quadratic
operator is neither assumed nor needed. T^4 has the same order property and
is self-adjoint. Its row mass r4=T^4 1_I sums all 8^4=4096 oriented walks,
with all four prefix support conditions. Schur's test, or weighted
Cauchy-Schwarz for this finite translation sum, gives ||T^4||_2 <= ess sup r4.
Self-adjointness gives ||T||_2^4=||T^4||_2.

Each reachable prefix displacement is u log(2)+v log(3)+w log(5). The exact
support-change points are +/-a minus those displacements. Interval logs
isolate and order all 76 cuts, giving 75 open panels. Unique factorization
identifies equal displacements; all distinct cut enclosures are disjoint.
Every prefix support predicate is constant on each actual panel, so a
certified interior point determines its complete walk list. The omitted
finite set of boundary points does not change the essential supremum.

Positive rational upper amplitudes are propagated through every walk. The
constructor uses a dynamic recurrence; the independent auditor separately
enumerates all 4096 words on every panel (307200 path-region tests), verifies
the complete boundary set with finer logs, and exactly matches every row sum.
The maximum rational upper row mass is approximately 12.33485412377453,
strictly below (15/8)^4=12.359619140625. Thus ||T|| <=15/8.
The auditor also rejects a too-small fourth-power row-mass ceiling. That
control is not an L2 operator-norm lower bound.

## Complement and corrected sign

The old separated prime losses sum to approximately 1.976915143739919.
Replacing their sum by 15/8 improves the same two-band bound to
0.7742721420391677..., without changing its archimedean masses, pole bound,
projection, or any native/source/Gram entry. The exact direct endpoint sum
is independently recomputed together with both complete inherited mass
audits and the exhaustive combined-prime audit. We use c=77/100, beta=100/77.

The complete Gram and its complete nine-panel recovery checkpoint are
archived losslessly as gzip. Uncompressed Gram SHA256:
f5ea5eb0ff24dabef080a463a5cb751aed920d1ab7913059b361ab8a413f55ee.
Native compact SHA256:
186d274000156edb0ba5e69e35aa9c992c90c99fbd784337a7a1538d97715981.
Uncompressed source SHA256:
b81e9a4fa0e21a168ad9974da13aa67cffb9c0d72499fc37079f9097927486cb.

All 7056 native/source pairings include both interval widths. The complete
residual Gram retains all mixed terms. With source error eta and residual
map bound M, the actual correction is delta=eta(2M+eta), recomputed exactly.
The sign constructor certifies Q-beta R-(beta delta+tau)I at 160 decimal grid
digits. It and the complete native/source/Gram inputs repeat byte for byte.
The independent whole-domain auditor widens the stored inputs to an
80-digit grid and recomputes all 84 positive shifted pivots, delta, trace,
lift bound, and physical/logarithmic conversions, with rejected controls.

The certified corrected margin tau is approximately 5.960464477539063e-26.
The integer lift bound is L=8. Completion of squares gives the exact
mu=tau*c/[tau+c(1+L^2)] approximately 9.169945350060097e-28; the conversion
matrix has positive diagonals and determinant mu^2. Doubling mu fails that
sufficient conversion test and is rejected.

## Logarithmic-domain conversion

The certified actual quarter-line symbol satisfies m0 >= w/10-6: use the
global floor -27/5 below |xi|=1 and log|xi|-7/(216 xi^2) above it, together
with exp(1)<3 and log(4)<2. The absolute prime loss is less than 5, with both
orientations and Lambda(4)=log(2). The pole loss is at most 4a exp(a)<12
because a<1. Hence Q >= Elog/10-23||h||_2^2 on the actual form domain.
Combining it with the physical bound gives
kappa=mu/[10(mu+23)] approximately 3.986932760895694e-30.
The independent auditor checks the aperture, active-prime cutoff, absolute
prime sum, elementary logarithmic inequalities, and the exact conversions.
This extends to smaller apertures by physical inclusion.

## Reproduction

Use the scripts certify/validate_native_prime5_joint_power4_093.py,
certify_native_prime5_power4_complement84_093.py,
validate_native_prime5_power4_complement_093.py,
certify_native_prime5_power4_schur84_093.py, and
validate_native_prime5_power4_whole_093.py. The sign and whole-domain scripts
read either raw JSON or the lossless archived gzip for source and Gram.
Certificates and independent reports are in notes/data with matching POWER4,
JOINT_POWER4, PAIRING, and TWOBAND_OBSTRUCTION names dated 20261007.

Next aperture work requires a fresh 94/100 complement, support geometry,
native/source/complete Gram and corrected sign. This result grants no
numerical aperture beyond 93/100 and no global/F4 arithmetic conclusion.
