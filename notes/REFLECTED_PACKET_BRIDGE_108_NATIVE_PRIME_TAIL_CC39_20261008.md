# RPB108 CC39: actual prime recurrence makes the logarithmic tail rate sharp

Date: 2026-10-08 UTC. Parent: 716dd411df44eb7b9712742bae720e6f85186d22.
Definitions: [native prime recurrence tail](../docs/TERMINOLOGY_RPB108_NATIVE_PRIME_TAIL.md).
Result: the actual complete prime multiplier has canonical high-frequency
tail O_B(1/log R), with a matching lower bound along an unbounded sequence
when 2B>log2. CC38's faster archimedean tail cannot be assigned to it.

## 1. Actual finite-cap arithmetic and its upper bound

Retain every active prime-power coefficient c_n=Lambda(n)/sqrt(n) and both
shifts. The actual prime part of Q-E_log has multiplier

    p_B(xi)=-2 sum c_n cos(2*pi*xi*log n).

Consequently, with S_B=sum c_n, weighted Cauchy-Schwarz gives

    ||C_prime,>R|| <= 2 S_B/log(e+R).                    (1)

This is a whole canonical supported-domain form bound. No prime smearing,
source-coordinate truncation or new explicit-formula identity is used.

## 2. Simultaneous recurrence needs no conjectural prime correlation

Let alpha be the finite vector of active log n values. For each positive
integer K, pigeonhole K^m+1 orbit points q alpha modulo one into K^m cubes.
Two points give an integer 1<=q_K<=K^m whose every phase distance to one
is at most 1/K. If these q_K have an unbounded subsequence, it gives the
required unbounded frequencies. If they remain bounded along infinitely
many K tending to infinity, some nonzero q repeats and q alpha is exactly
integral; its positive multiples give unbounded exact recurrence.
Thus in either case there are xi_j->infinity with every phase tending to1.
No rational independence or zero-divisor assumption is required.

## 3. A genuine native supported modulation test

Assume 2B>log2. Choose log2/2<b<B and a real nonnegative smooth bump phi,
compactly supported in (-B,B), supported in [-b,b] and positive on (-b,b).
Set h_j(x)=exp(2*pi*i*xi_j*x)phi(x), m=||phi||_2^2>0, and

    I_n=int phi(x)phi(x-log n) dx,
    A_phi=2 sum c_n I_n.

All I_n are nonnegative; I_2>0, so A_phi>0. Direct physical translation
pairing, with the actual coefficients, gives

    Q_prime(h_j,h_j)=-2 sum c_n I_n cos(2*pi*xi_j*log n)
                      ->-A_phi.                       (2)

The archimedean remainder diagonal tends to zero: its Fourier argument
is xi_j+u, r_arch tends to zero, and the integrable dominating function
is 8 |phi_hat(u)|^2 by CC37. Both pole moments tend to zero because
exp(+/-x/2)phi(x) is integrable; Riemann-Lebesgue applies. Hence the
COMPLETE actual physical remainder satisfies

    <R_B h_j,h_j>_2 ->-A_phi,
    liminf ||R_B h_j||_2 >= A_phi/sqrt(m)>0.             (3)

This proves noncompactness of the physical remainder on this cap, using
h_j weakly null in physical L2. It does not contradict compactness of
C_B=i_B*R_B i_B on the logarithmic carrier; that inclusion is compact.

## 4. Canonical normalization and a sharp tail lower bound

Modulation translates the Fourier coordinate. Dominated convergence yields

    ||h_j||_D^2/log xi_j -> m.                          (4)

For completeness, log(e+|xi_j+u|)<=log(e+xi_j)+log(e+|u|); for sufficiently
large xi_j this bounds the ratio by 2+log(e+|u|). The smooth bump's Schwartz
Fourier transform makes this dominating product integrable. Pointwise the
weight ratio tends to1.

Take R_j=xi_j/2. On |xi|<=R_j, the translated phi_hat is evaluated at
|u|>=xi_j/2. Its L2 tail decays faster than any power, so the omitted low-band
prime diagonal tends to zero. Equations (2)-(4) therefore imply, for all
sufficiently large j,

    ||C_prime,>R_j|| >= A_phi/[4m log xi_j].             (5)

Indeed the high-band prime diagonal has absolute value at least A_phi/2
and ||h_j||_D^2 is at most 2m log xi_j. Dividing the quadratic form by that
norm proves (5). Since log xi_j=log(2R_j), this matches (1) in order along
the recurrence sequence. It excludes a uniform O(R^-alpha) tail bound
for every alpha>0, including CC38's O(1/[R log R]) archimedean rate.
No exact Fourier cutoff is applied to h_j, which remains compactly supported;
the band restriction is on the multiplier form, so domain support is preserved.

## 5. Why this is not a critical-mode countermodel

The full original quadratic form on these same native test functions is

    Q(h_j,h_j)=||h_j||_D^2-A_phi+o(1),
    Q(h_j,h_j)/||h_j||_D^2 ->1.

Thus the vectors are eventually original-positive, and they are not
asserted to be old critical eigenlifts. Their physical mass is fixed,
while their canonical normalization produces mass tending to zero;
CC34 specifically excludes that escape mechanism for a hypothetical
near-zero-defect sequence of normalized critical lifts. This distinction
prevents the modulation test from being misused as an RH contradiction
or a counterexample to a defect-dependent critical-row estimate.

The result proves an estimator limitation using the actual native arithmetic:
a generic full-remainder tail cannot inherit the archimedean decay.
A selected critical family might still have additional signed correlations.
Neither their absence nor their required suppression is proved here.
The full positive inverse and outward projection in CC35 remain unestimated.

## 6. Recovery, validation and standing

The execution environment was unavailable this turn. The proof is analytic
and is published directly through the repository connector; no executable
validator or local replay is claimed. CC38's recorded 25,993 checks remain
the last recorded total, not a count of verification performed this turn.
Repository content and historical-prefix custody are checked separately.

Concurrent NF9/NF10 handoffs are preserved read-only. NF10 reports a newly
certified original physical complement lower bound17/100 at53/50, outside
the first112 Legendre modes. Its target whole-domain Schur sign remains
pending; the handoff is not rerun here. The whole-domain anchor remains21/20,
even0/odd0, physical margin1/(3*10^63). RH/F4, critical outward suppression,
retained attachment, reusable continuation and Lean closure remain open.
