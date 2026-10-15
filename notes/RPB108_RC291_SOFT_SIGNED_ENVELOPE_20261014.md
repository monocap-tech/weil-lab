# RC291 — soft signed-response identifiability test on 120 even coordinates

Parent RC290: `a967d9095e353a49bf9b998e7fa62f7578c84d51`.
Original Weil action unchanged; aperture B=11/10. Full Stage I/RH OPEN.

## Purpose

RC290 localized RC289's poor joint even cross-payment to the soft
positive source `v=P4-tP0`, where the rational mixing coefficient
`t=Gamma04/Gamma00` is derived from the *certified lower gate*.
RC291 tests whether the EXISTING complete inverse-residual covariance
upper bound, together with all exact RC280 trial polynomial
coefficients, can determine a signed response on the 120 retained
even modes outside the positive P0,P4 pivot span.

## Exact energy comparison

Let `R` be the remaining 120-dimensional even retained Legendre
subspace, `Z=Z4-tZ0` be the exact rational trial for `v`, and
`X=G_new^{-1}D e_v` be the actual, unknown inverse-residual
correction. RC288 certifies a full correlated upper `q` on

    <X,G_new X> <= q.

For the actual reduced positive reference, RC278/RC283 also establish

    0 < G_new <= G_old <= nu_old D,

with the same whole-domain D. Therefore EVERY finite
`Y` supported in the retained projection obeys

    <Y,G_new Y> <= nu_old <Y,D Y>.

Calculate the exact signed projected rational polynomial `Z_R=P_R Z`
using all RC280 degree-0..64 coefficients, removing precisely the
P0 and P4 pivot coordinates. Pay the upper RC129 D offset and round
all degree contributions outward, to obtain

    E = upper sum_{n in R} mass_n (H_n+s) Z_n^2.

The exact validator checks

    4 nu_old E < q.

This is a **strict feasible-energy inclusion**: the inherited energy
ball `{Y:<Y,G_new Y> <=q}` contains `Y=-Z_R` and both
`Y=-2Z_R`, `Y=+2Z_R` because their actual G_new form energy is
bounded by nu_old D. These yield projected candidate responses

    Z_R+Y = 0,   -Z_R,   3Z_R,

respectively. The latter two have reversed and amplified signed
orientations. All 120 coordinates are treated jointly, not sampled.

**Crucial limitation:** these are *hypothetical test vectors* within
the **upper-energy constraint**. They are NOT asserted to solve
`G_new X = D e_v`, nor to satisfy the exact original source data.
RC291 therefore proves a limitation of the existing scalar/Gram
upper-bound method, NOT non-identifiability from every piece of
underlying original-action data, and NOT a counterexample to RH.

The same exact source-response enclosure preserves the native
positive P0,P4 block (RC288), the smaller RC285 P0/P1 pivots and
RC286 subunit single-pivot cross estimates. Nothing here changes
the original index census or the remaining 314-dimensional Schur
principal obligation.

## Why this is more than an error-size observation

Unlike an abstract 2x2 toy example, the comparison tests the actual
RC280 **soft-source trial polynomial** against the inherited,
globally paid **new-reference** covariance budget, under the exact
physical Legendre masses, whole-domain reference upper form, and
the RC129 archimedean s interval.

It provides a concrete threshold for additional information:
merely reprocessing the same source covariance-energy upper bounds
cannot establish the sign of the complete retained response.
At minimum, a signed projected inverse-response (or a suitable
dual-resolvent certificate with a controlled remainder) must constrain
`P_R X` beyond its norm. Refining the estimates may eventually
exclude sign reversal, but doing so requires a much tighter source
certificate.

The old positive pivot/center cross method already has a center-only
mass payment exceeding one. A coordinate relabeling alone does not
decrease it; signed cancellation between the actual trial center
and the actual residual correction is the key open possibility.

## RC292 work contract

Either carry out new original operator action evaluations needed for
a certified polynomial/resolvent approximation of
`G_new^{-1}(P4-tP0)`, or build dual test-vector identities for
`<P_n,G_new^{-1}(P4-tP0)>` on n in the 120 retained modes with
explicit residual bounds. Preserve all original arithmetic prime,
archimedean, endpoint and infinite output-tail payments, and use the
**new** reference inverse. No guessed signed coefficients.

## Reproduction

```bash
python scripts/validate_rpb108_rc291_soft_signed_envelope.py --output certificates/rpb108_rc291_soft_signed_envelope.json
python scripts/validate_rpb108_rc291_soft_signed_envelope.py --output certificates/rpb108_rc291_soft_signed_envelope.json --replay
```

The validator checks exact-rational input blob pins for RC129, RC278,
RC280, RC288, RC289 and RC290 and reproduces the new energy comparison.
CI replay is a custody and arithmetic test, not independent validation
of the inherited analytic assumptions.
