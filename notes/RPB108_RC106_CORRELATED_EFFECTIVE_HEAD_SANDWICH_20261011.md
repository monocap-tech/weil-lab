# RC106 — correlated effective-head sandwich

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.

RC106 supplies a two-sided, correlation-preserving certificate interface for the exact effective Weil head. Its mathematical interval width is quadratic in the complement residual. For an ideal RC103 polynomial lift, its lower endpoint always improves the old scalar-floor head bound. Exact controls certify positivity in examples rejected by that scalar bound, and separately verify that an upper endpoint can certify an actual negative direction.

These are operator theorems and illustrative controls. No new original arithmetic head entries, complement actions or lifted responses are evaluated. The strong floor remains open.

## Definitions and input boundary

The original canonical operator is \(A_Q=I+i^*Ki\). Keep the complete sufficient head H and its canonical complement E, with

\[
D=P_EA_QP_E|_E,\quad B=P_HA_QP_E,\quad
F=A_H-BD^{-1}B^*.
\]

RC103's complement bracket is \(\alpha I\preceq D\preceq bI\), with \(\alpha=247/2500\), even \(b=2067533/500000\), odd \(b=3239591/1000000\). RC105 supplies conditional accuracy contracts for inexact polynomial lifts. Their exact JSON bytes are bound by SHA-256; the RC105-to-RC103 dependency hash is checked.

Let J map a finite coordinate space into H, let \(Q=J^*A_HJ\), and set \(R=B^*J\). J may parameterize the weak span, a test block, the strong subspace, or the complete head. A conclusion about a small compression is a conclusion about that compression; it does not certify the remaining head.

A lift Y maps those same coordinates into E. Define its exact residual and lifted form:

\[
r=R-DY,\qquad
C=Q-R^*Y-Y^*R+Y^*DY.
\]

Equivalently, C is the original form Gram of the vectors \(J-Y\). This representation preserves the original mixed correlations and may be evaluated through fused responses, rather than separate norms.

## Exact identity and two-sided enclosure

Completing the square gives

\[
\boxed{J^*FJ=C-r^*D^{-1}r.}
\]

Indeed, expand \((R-DY)^*D^{-1}(R-DY)\); the mixed and quadratic Y terms cancel those in C. No accuracy or polynomial assumption on Y is needed.

The spectral bracket implies \(b^{-1}I\preceq D^{-1}\preceq\alpha^{-1}I\). Thus

\[
\boxed{C-\alpha^{-1}r^*r\preceq J^*FJ
\preceq C-b^{-1}r^*r.}
\]

The difference between the displayed endpoints is exactly

\[
(\alpha^{-1}-b^{-1})r^*r.
\]

For rigorous evaluations, suppose common coordinate enclosures satisfy

\[
C_{\rm lo}\preceq C\preceq C_{\rm hi},\qquad
H_{\rm lo}\preceq r^*r\preceq H_{\rm hi}.
\]

Then valid endpoints are

\[
C_{\rm lo}-\alpha^{-1}H_{\rm hi},\qquad
C_{\rm hi}-b^{-1}H_{\rm lo}.
\]

An upper residual enclosure cannot be substituted for the lower in the second endpoint. If no residual lower is certified, use \(H_{\rm lo}=0\), since a Gram is positive semidefinite. This still gives a valid upper C_hi. Errors in the evaluated C and residual Gram are additional interval widths; they are not covered automatically by a complement action accuracy theorem.

## Ideal polynomial lower dominates the scalar-floor head

For the ideal RC103 lift \(Y=q(D)R\), let \(p(D)=I-Dq(D)\). Its spectrum obeys \(|p|\le\epsilon<1\). The lower endpoint becomes

\[
Q-R^*\left[2q(D)-Dq(D)^2+\alpha^{-1}p(D)^2\right]R.
\]

Because \(2q-Dq^2=(1-p^2)D^{-1}\), subtracting the old lower \(Q-\alpha^{-1}R^*R\) leaves

\[
\boxed{R^*(1-p(D)^2)(D-\alpha I)(\alpha D)^{-1}R\succeq0.}
\]

All displayed functions of D commute, and each scalar spectral factor is nonnegative. Consequently

\[
Q-\alpha^{-1}R^*R
\preceq C-\alpha^{-1}r^*r
\preceq J^*FJ.
\]

This is a proved improvement on the actual scalar-floor inequality, not a comparison of two unrelated numerical norms. If only an upper G for \(R^*R\) is available, the old computable lower \(Q-G/\alpha\) is still below the ideal exact endpoint. However, extra enclosure losses in a computed endpoint can destroy the visible improvement; they must be certified. An arbitrary inexact Y retains the two-sided identity but has no automatic scalar-dominance guarantee. The previously proved weak lower L remains available because the exact F still dominates the old head lower.

## Quadratic convergence and the RC105 contract

If \(R^*R\preceq G\), the ideal residual enclosure is \(r^*r\preceq\epsilon_n^2G\). Therefore the mathematical sandwich width satisfies

\[
\mathrm{width}\preceq(\alpha^{-1}-b^{-1})\epsilon_n^2G.
\]

RC105's implemented lift instead satisfies

\[
r^*r\preceq(\epsilon_n+b\eta H_n)^2G.
\]

Its reserved local-error contract makes \(b\eta H_n=\epsilon_n\), so the same width factor is at most \(4(\alpha^{-1}-b^{-1})\epsilon_n^2\). RC106 records exact rational ideal and inexact width factors for every inherited conditional budget. These bounds concern the mathematical residual interval, before evaluation-enclosure widths.

The quadratic dependence matters: certification of the effective form uses the stationarity of complement elimination. A generic first-order inverse norm error discards this benefit.

## Strong-block and spectral interfaces

For a complete parameterization J of the actual strong subspace S, with actual canonical metric \(M=J^*J\), a certified inequality

\[
C_{\rm lo}-H_{\rm hi}/\alpha\succeq\beta M
\]

proves the exact effective strong floor needed by the six-response Schur route. An analytic theorem for the unevaluated part can also complete a blockwise argument. Merely proving this on a test subspace does not certify all of S. The original complement and projections must be retained, since their spectral bracket is an input to this theorem.

More generally, endpoint eigenvalues are monotone under Loewner order. After transforming by the actual positive metric, ordered eigenvalues of the true compression lie between those of the endpoints. Matching endpoint inertia therefore fixes the compression's inertia. A positive lower proves positivity; a negative Rayleigh direction in an upper proves negativity. Failure of a lower to be positive proves neither a negative direction nor a null. These statements become statements about the full head only when the tested coordinate space covers that head, or a separate theorem controls the rest.

The theorem permits targeted compressions and analytic block control. It does not prove that six responses alone suffice to certify an unknown strong subspace, nor that dense reconstruction of the head is necessary.

## Exact validation and independent replay

The validator uses rational arithmetic throughout. For each inherited complement bracket it checks two residual degrees, 9 and 17, on a noncommuting rational D and R. It verifies the exact identity, both Loewner endpoints, the interval-width identity, and scalar-floor dominance. The new lower is strictly positive while the scalar-floor head is not positive semidefinite. These controls involve illustrative head and source matrices, not original arithmetic evaluations.

Additional controls add signed rational perturbations to Y and verify the general inexact sandwich, use a larger residual upper to verify the conservative lower, and modify Q so the upper has a negative coordinate Rayleigh quotient. The last control demonstrates the distinction between lower-bound rejection and a certificate of negativity.

Independent replay uses a direct two-by-two inverse, positive-binomial Chebyshev evaluation, and explicit polynomial powers instead of Horner evaluation. The resulting certificate matches exactly; replay reports PASS. The general operator proofs above are not inferred from the finite controls.

Repository reproduction:

```sh
python scripts/validate_rpb108_rc106_correlated_effective_head_sandwich.py > /tmp/rc106.json
python scripts/validate_rpb108_rc106_correlated_effective_head_sandwich.py --replay /tmp/rc106.json
```

Published artifacts are the validator, `certificates/rpb108_rc106_correlated_effective_head_sandwich.json`, and this note.

The known corrected positive span remains six and the nonpositive spectral dimension upper remains 1,244. Actual strong-floor certification, mode coverage, and six original lifted-response Grams remain open. No whole-aperture extension, RH or Global/F4 theorem is claimed. RC106 gives a sharper acceptance interface for those arithmetic and structural obligations.
