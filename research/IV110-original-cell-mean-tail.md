# IV110 — Original fixed-window finite-codimension tail

Status: mathematical derivation / formalization specification, not a Lean receipt.
Root: dual-certified IV103 at 018f7e59f4129ce521cd3ae86d1afd59d3b64b5f.
The IV108 and IV109 bounds referenced below are candidate results pending native verification.

## Actual Fourier normalization and finite constraints

Fix a > 0, with original physical support [-a,a], and use the Mathlib
Fourier convention Fv(xi) = integral v(x) exp(-2 pi i xi x) dx.
Partition [-a,a] into N equal disjoint measurable cells I_j (endpoints
allocated once), each of length delta = 2a/N. Pick a left endpoint x_j.
For a supported Schwartz v impose the N complex linear constraints
integral over I_j of v = 0. These are physical L2-continuous functionals.
They are not pointwise vanishing conditions and do not require an
improper sharp Fourier truncation of a compactly supported test.

By subtracting the constant phase in each cell, exactly,

Fv(xi) = sum_j integral_{I_j} v(x)
  [exp(-2 pi i xi x) - exp(-2 pi i xi x_j)] dx.

For real t,s, |exp(it)-exp(is)| <= |t-s|, by integration of the
unit-norm derivative along the real segment. Hence
|Fv(xi)| <= 2 pi |xi| delta integral_{-a}^a |v|
           <= 2 pi |xi| delta sqrt(2a) ||v||_2,
using Cauchy-Schwarz on the finite physical window.
For T > 0, integrating the squared bound gives

integral_{-T}^T |Fv(xi)|^2 dxi
 <= epsilon ||v||_2^2,
epsilon = (16 pi^2 a / 3) delta^2 T^3.

By Plancherel, the complement of the band has mass at least
(1-epsilon)||v||_2^2. For the original weight
w(xi) = log(exp(1)+|xi|), monotonicity and nonnegativity give

||Jv||_log^2 >= log(exp(1)+T) (1-epsilon) ||v||_2^2.

No Fourier compact-support assumption is made. The same estimate
applies to the physical L2 representative using the Fourier agreement
already attached to the Schwartz lift.

## Consequence for the response-corrected form

Let E_a = native logarithmic error + physical pole energy constant.
Conditional on the staged IV108 row budget and IV109 physical row bounds,
D_k = (5/2) sum_i C_i^2 / m_i is finite and

S_k(v) = Q_a(v) - Q_a(Rv)
 >= ||Jv||_log^2 - (E_a + D_k)||v||_2^2

on the original fixed window with its packed sector (a=11/10).
For any desired margin eta > 0 choose T > 0 so that
log(exp(1)+T) >= 2(E_a + D_k + eta), then choose N so that
N^2 >= (128 pi^2 a^3 / 3) T^3.
This ensures epsilon <= 1/2, so
S_k(v) >= eta ||v||_2^2 on the common kernel of the N cell means,
intersected with the k packed physical orthogonality constraints.

The two cutoff constants follow by substituting delta = 2a/N.
The choice is existential and may be very large: E_a and D_k are
not yet effectively evaluated here.

## Scope and non-implications

This supplies a candidate explicit finite-codimension tail coercivity
argument, not a nonnegative finite head and not a completed global Schur
comparison. On the physical packed complement, the cell-mean kernel has
complex codimension at most N. On the whole supported test space, the
intersection has complex codimension at most k+N. The complement must be
chosen in the actual supported Schwartz/form domain, e.g. from a basis
of the finite constraint image with smooth preimages; piecewise constant
cell indicators are functionals, not admissible Schwartz basis vectors.

One still needs an exact decomposition, control of signed head-tail
interactions (or a valid response/Schur comparison using the coercive
tail), and positivity of the finite remaining form. A finite index bound
alone does not exclude even a single negative direction. There is no
claimed transfer to Canonical Return's numerical head, no uniform
support extension, and no RH claim.

## Formalization order

1. Cell partition and mean functionals; disjoint union integrals.
2. Unit-phase difference estimate and support-local Cauchy-Schwarz.
3. Low-band squared Fourier mass and Plancherel complement.
4. Logarithmic energy lower bound; explicit N and T cutoff arithmetic.
5. Combine with native Garding and accepted directional response budget
   when IV104–109 are certified and the two source lineages integrated.
6. Construct smooth finite constraint representatives and prove exact
   decomposition; derive a valid finite head / infinite tail comparison.
