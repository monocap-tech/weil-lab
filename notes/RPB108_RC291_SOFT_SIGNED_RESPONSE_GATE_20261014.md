# RC291 — signed soft-source response feasibility and missing native action

Parent: RC290 `a967d9095e353a49bf9b998e7fa62f7578c84d51`.
Aperture B=11/10. Globally positive reference rank 317.
The **actual signed inverse response is not yet computed**.

## Target, not a falsely transferred certificate

RC290 identifies the source combination

    v_soft = P4 - t P0,
    t = Gamma_lo[0,4]/Gamma_lo[0,0] ~ 0.823238958176,

where `Gamma_lo` is the certified positive **lower** matrix for the
new-reference P0,P4 native gate. Its orthogonalized soft lower Schur
pivot is `delta ~ 2.7874194061e-5`. The positive hard pivot is
`a ~0.00518134701`.

Let `R` be the 120 remaining even native Legendre channels.
Denote the exact, existing 65-coefficient mixed source trial by
`Zsoft=Z4-t Z0`, and the **as-yet-uncomputed** actual inverse
residual by `Xsoft=G_new^-1 D e_soft`. Then

    U_R*G_new^-1 v_soft = P_R(Zsoft+Xsoft).

The entire 2x2 block-to-rest Schur cross-payment obeys the
genuine (but conditional on signed response data) inequality

    C*Gamma_actual^-1 C <= lambda^2 [
       ||P_R(Z0+X0)||_physical^2/a
       +||P_R(Zsoft+Xsoft)||_physical^2/delta
    ] Mass_R.

The second term alone would be <1 if

    ||P_R(Zsoft+Xsoft)||_physical^2 < delta/lambda^2.

This is only an **optimistic soft-only threshold**. To prove the
complete joint cross majorant <Mass_R, one must also reserve a
strict budget for the nonnegative hard P0 term. Moreover, a
mass-subunit cross majorant is itself only a sufficient intermediate
step, not positivity of the remaining Schur principal form.

## Exact source norm and cancellation window

The validator reconstructs the exact physical mass norm of
the projected rational source center using the pinned RC280
polynomials, parity-cut coordinates and RC290 mixed-source t, and
matches RC290's transformed Gram entry *exactly*:

    A = ||P_R Zsoft||_physical^2 ~ 6.28906646e-7.

The optimistic zero-hard budget has

    T = delta/lambda^2 ~ 2.887e-7.

Because `A>T`, the center alone would exceed this *specific*
soft-only bound. Its actual inverse residual may nevertheless
cancel part of the center. Writing

    E = ||P_R Xsoft||_physical^2,
    L = <P_R Zsoft, P_R Xsoft>_physical,

the sharp signed inequality to certify is

    A + 2L + E < T.

The magnitude of the unknown projected inverse residual must
be *compatible with* a cancellation window:

    (sqrt(A)-sqrt(T))^2 < E < (sqrt(A)+sqrt(T))^2.

The certificate encloses both irrational endpoints by rational
20-digit outward bounds and compares them to RC290's existing
correlated residual inverse-energy payment `Ssoft/d_R`.
The latter exceeds the upper cancellation-window endpoint by
more than a factor of **19**. The existing upper estimate thus
has far too much latitude to decide signed cancellation.

This is a **data-sufficiency diagnosis**, not an assertion that the
actual residual energy saturates the upper bound, nor that the
actual Weil source fails to cancel.

## Why existing covariance Grams cannot determine a sign

RC288 supplies a full positive semidefinite *upper* covariance
matrix on P0,P4, but no mixed inner products of the true inverse
residuals against the trial center. The validator constructs a
precise countercontrol to the inference that the sign could be
recovered from upper Gram data alone.

In an abstract comparison Hilbert space with retained-mode
physical `D` weights, consider candidate residual projections

    X0 = 0,
    X4 = +P_R Zsoft, or X4 = -P_R Zsoft.

The two candidates have **identical quadratic energies** and
produce opposite projected response behavior for the mixed soft
source: respectively `4A` and `0` in physical squared mass.

The rational validator computes an outward upper bound on their
`D` energies from the *actual source trial polynomial coefficients*
and RC129's certified offset interval, then verifies the entire
inherited 2x2 inverse-residual upper matrix minus the candidate's
PSD energy Gram remains strictly positive.

This is a mathematical **information-limitation control** for
covariance upper data. It is not an assertion that either test
candidate is an actual inverse solution for the original Weil
operator; original source actions and their additional structure
may rule either out.

## Native data/action needed at RC292

We must evaluate or interval-enclose the *signed* 120-component
output of `P_R G_new^-1 (P4-tP0)`, or at least certify its
physical norm directly (without summing separate center and
residual upper energies). The program can reuse existing exact
original prime/endpoint source actions and degree-localized
residuals, but an actual bounded inverse/resolvent action on the
soft residual, with full finite and infinite error payments,
is needed to establish the missing signed correlations.

A Chebyshev polynomial approximation to the positive
`D`-normalized inverse is a possible certified route, **provided
each required operator action is actually carried out and every
remaining prime, pole, archimedean and endpoint fault is paid**.
A degree budget alone is not an executed inverse response.

No new original Weil operator action is performed here.
The already established positive three-pivot block remains valid,
as do RC286's separate single-source P0/P1 cross estimates.
The remaining 314-dimensional principal gate, Stage I, global F4,
RH, and Lean are OPEN.

## Replay

```bash
python scripts/validate_rpb108_rc291_soft_signed_response_gate.py --output certificates/rpb108_rc291_soft_signed_response_gate.json
python scripts/validate_rpb108_rc291_soft_signed_response_gate.py --output certificates/rpb108_rc291_soft_signed_response_gate.json --replay
```

All prior certificates are checked by exact immutable Git SHA-1 blobs.
This certifies exact source identities, threshold arithmetic and
the limits of the stored covariance information; it is not
an independent proof of every inherited analytic premise.
