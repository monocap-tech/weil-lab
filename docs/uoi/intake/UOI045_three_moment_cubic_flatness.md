# Weil-Lab — UOI045: cubic local Fourier interpolation, uniform Gamma budget, and finite-stage spectral transfer

**Status (2026-11-21): analytic theorem with exact rational arithmetic checks, no new Lean kernel compilation or strict named-axiom audit, no GitHub/CI action, no numerical NF gate promotion, and no claim of support-independent original Weil positivity or RH.**

## Source and prior analytical evidence

Research source is pinned at `monocap-tech/weil-lab` commit `614ba879f7389fdb620c474adaee273b00eac71c`, as examined in UOI037–UOI044.

- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean` (source blob `eacb18946673c62f9c39bf02bccf01f3f2cff06e`) states, for an arbitrary complex Schwartz test, `Gamma(f) >= (11/10)||f||_2^2 - (67/10) int_{-5}^5 |Ff(xi)|^2 dxi`. This is a source-level theorem statement; this report performs no fresh kernel audit.
- `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean` (source blob `f2ce89e5e020f09de54d1864da928bd99a841cbd`) fixes the two exponential moment functionals and their crossed, rank-two pole form.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean` (source blob `5ed0be00fdfefe2f0b21223858c36e3870cda5f7`) fixes the full original von Mangoldt quadratic with the two `±log n` correlations. No prime term is deleted or relabeled in this note.
- UOI040 established the *nested*, three-moment-neutral collar family and a uniform Gamma bound `G_old = 2195428693/1996093750`. UOI043 defined its full-prime Gamma-relative generalized spectral quotient `rho_m`. UOI044 supplied an analytic exact-rational ten-stage arithmetic-envelope screen with the upper `lambda_max(B_10) <= 13369883/14093750 < 949/1000`, not a native Lean certificate. The present result uses that screen **only conditionally as prior analytic evidence**.

The separately unproved extension of the old-collar-specific **literal Gamma − Prime + Pole** formula to arbitrary nested support, and the distinct full source-to-native Weil form identification, remain F01/F08 obligations in master ledger #898. These are not discharged by this theorem.

## 1. Exactly the same nested test domain

Let `t=log 8`, `c_j=(j+1/2)t`, `delta_j=8^(−j)/1000`, and `I_j=(c_j−delta_j,c_j+delta_j)` for `j>=0`. For `m>=1`, let `D_m=union_{j<m} I_j` and let `S_m` consist of complex compact smooth tests `f=sum_{j<m} f_j` with `supp f_j subset I_j` and three **separate per-collar** vanishing moments:

`int f_j(x) dx = int f_j(x) exp(x/2) dx = int f_j(x) exp(−x/2) dx = 0`.

Equivalently in the collar-relative coordinate `y=x−c_j`, the three test moments against `1`, `cosh(y/2)`, and `sinh(y/2)` vanish. The translation/scalar factors do not change these zero conditions. The union is increasing under zero extension `S_m -> S_(m+1)` and contains infinitely many smooth tests. An explicit local generator is `(D^3−D/4) eta_j` for any compact smooth bump `eta_j` supported inside `I_j`.

On these tests the original pole quadratic vanishes exactly, and the original literal form, **once the broad-support algebraic source identity is attached**, is `W_lit(f)=Gamma(f)−P(f)`.

## 2. Exact local interpolation gives a cubic physical remainder

Use the negative-exponent, unitary `2π` Fourier transform, `Ff(xi)=int f(x)exp(−2π i xi x)dx`. Set `q=2π xi`, and define

`R_q(y) := exp(−i q y) − 1 + 4q^2(cosh(y/2)−1) + 2 i q sinh(y/2)`.

Each of the three subtracted/interpolating functions lies in the linear span of the three moments, hence its integral against every `f_j(c_j+y)` vanishes. Therefore **exactly**, without Taylor approximation,

`Ff(xi) = sum_{j<m} exp(−i q c_j) int_{−delta_j}^{delta_j} f_j(c_j+y) R_q(y)dy`.

A direct derivative calculation yields

`R_q(0)=R'_q(0)=R''_q(0)=0`,

`R'''_q(y) = i q^3 exp(−i q y) + (q^2/2)sinh(y/2) + (i q/4)cosh(y/2)`.

For `|xi|<=5`, `|q|<=10π<32`; and for all `|y|<=delta_0=1/1000`, `cosh(|y|/2)<2`, `sinh(|y|/2)<1/1000`. Thus

`|R'''_q(y)| < 32^3 + (32^2/2)(1/1000) + (32/4)*2 < 32785`.

The integral Taylor remainder, valid for complex functions of a real variable, gives

`|R_q(y)| <= (32785/6)|y|^3`.

This **does not** imply `Ff` has a third-order zero as a function of xi at xi=0; only the integral of the locally interpolated physical-coordinate remainder is `O(delta_j^3)` at fixed bounded frequencies. The three prescribed spectral evaluation zeros are at `xi=0, ±i/(4π)`, and these are not a triple zero at one point.

## 3. Uniform low-frequency mass, independent of stage

For any `f∈S_m`, by Cauchy–Schwarz within each collar and then across collars,

`|Ff(xi)| <= (32785/6) sum_{j<m} delta_j^3 sqrt(2 delta_j) ||f_j||_2`
`<= (32785/6) sqrt(2 sum_{j<m}delta_j^7) ||f||_2` for `|xi|<=5`.

Hence, using the band length ten,

`int_{−5}^5 |Ff(xi)|^2 dxi <= (5/9)*32785^2 * (sum_{j<m}delta_j^7) ||f||_2^2`.

The exact geometric-series bound is

`sum_{j<m} delta_j^7 <= delta_0^7/(1−8^(−7)) = 1/999999523162841796875`.

Therefore

\[
\boxed{
 \int_{-5}^{5}|\widehat f(\xi)|^2\,d\xi
 \le B_3\|f\|_2^2,
 \quad B_3=\frac{42994249}{71999965667724609375}
 < 5.972\times10^{-13}.}
\]

This is a uniform bound on **every finite nested stage** and the algebraic union, using no arithmetic prime hypothesis. The calculation is infinite-dimensional; no truncation is being mistaken for an all-stage argument.

## 4. Improved uniform signed Gamma margin

Insert the above in the original signed lower inequality:

\[
\boxed{
\Gamma(f)\ge G_3\|f\|_2^2,
\qquad G_3=\frac{11}{10}-\frac{67}{10}B_3
=\frac{395999811171045044221}{359999828338623046875}.
}
\]

Numerically `G_3≈1.09999999999599914`, and rationally `G_3>1.099999999995`. Compared with the earlier UOI040 `G_old≈1.099862515476`, the **guaranteed margin improves by approximately 0.00013748452**. This nearly saturates the `11/10` high-frequency floor of the *particular two-band signed Gamma estimate*, not the exact Gamma contribution itself.

All original pole moments are zero on this domain, while the full prime term remains unchanged. Thus every previously derived *finite-stage* valid prime upper envelope `P(f) <= B_m ||f||_2^2` automatically upgrades to

`W_lit(f) >= (G_3−B_m)||f||_2^2`.

For example, **using UOI044's separate analytic stage-ten upper envelope** `B_10 <= 13369883/14093750` gives

\[
\boxed{W_{\mathrm{lit}}(f)\ge (G_3-13369883/14093750)\|f\|_2^2
\approx0.151360851437\|f\|_2^2\qquad (f\in S_{10}).}
\]

The earlier simpler certificate `W_lit(f)>(G_3−949/1000)||f||_2^2>0.150999999995||f||_2^2` follows. Neither is a new kernel/CI result, and the general form/core transport still requires proof.

For UOI043's generalized eigenvalues, the existing envelope translates to `rho_10 <= (13369883/14093750)/G_3 < 0.8624`, relative to the full original prime quadratic and the **actual** positive Gamma metric on the completed restricted form domain (subject to the source/core assumptions explicitly recorded in UOI043). The estimate uses the full prime form, not a ladder surrogate.

## 5. Preservation and limits

The local three-moment annihilator is a **filtration-dependent** subspace, not an intrinsic subspace of the unrestricted original Weil form. Under a proposed projection dictionary, all stated estimates transfer only when the map preserves the three local observation functionals (or their joint kernel), the physical Fourier low-band norm, the actual Gamma quadratic, and the full prime mixed form with the given normalization. A unitary preserving only the complete signed form need not preserve this intermediate decomposition.

Crucially, `G_3` is **uniform in the number of collars**, but no estimate here bounds the full-prime supremum `rho_m` uniformly in `m`: UOI041 proved an off-ladder physical `L²` growth phenomenon, while UOI042 showed associated Gamma costs for selected packets. Neither settles the all-vector Gamma-normalized problem. The source/native identity F01/F08 is independent and remains open.

## 6. Lean-ready obligations, no CI fan-out

1. In the existing master ledger #898, F10, formalize the exact three-moment interpolation `R_q` on each collar and the cubic Taylor remainder, retaining `2π` Fourier normalization and complex Schwartz integrability.
2. Prove the finite-collar Cauchy–Schwarz estimate and the uniform geometric sum of `delta_j^7`. Produce an exact rational bound `B_3`, then combine with the existing signed Gamma bracket theorem.
3. Under F25/F26, **reuse**, rather than recertify or silently change, UOI044's independent exact ten-stage full-prime envelope and upgrade the analytic signed margin.
4. Under F01/F08, extend the original fixed-collar literal RHS/form identity to arbitrary supported compact Schwartz tests before asserting native source equivalence; preserve all poles and original von Mangoldt coefficients.
5. Require real Lean compilation and standard-only axiom receipts before any theorem is promoted as certified. Do not submit a competing broad CI job or treat arithmetic Python checks as kernel acceptance.

**Arithmetic reproduction:** `check_uoi045.py` verifies the rational Taylor envelope, geometric-series sum, signed-Gamma fractions, and inherited ten-stage numerical inequalities. It is not a formal proof, compiler result, or independent audit of UOI044's source ledger.
