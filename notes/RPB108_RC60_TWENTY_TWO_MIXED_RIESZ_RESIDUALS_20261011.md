# RPB108 RC60 — 22-feature mixed Riesz residual covariance

RC60 certifies the complete mixed physical operator-residual Gram for the 22 trial responses introduced in RC59, at cap B=11/10. It transports that covariance into actual canonical and physical Riesz-error Gram upper bounds. An exact rational PSD check verifies that the new canonical error upper matrix is below RC59's energy-based upper matrix in Loewner order. All original eight trial columns remain exactly unchanged.

This is a whole-matrix error improvement for every complex coefficient vector, including correlations between features. It does not certify an enlarged original Weil head floor or the enlarged projected-source threshold.

Every diagonal canonical squared-error upper bound improves by more than **730 times** relative to RC59. For native feature 21, the upper bound falls from approximately **0.5018576** to **0.00012129994**, an improvement of more than **4,100 times**. These ratios compare certified upper bounds; they do not assert a reduction in the fixed trials' actual errors. The trials themselves are unchanged.

The finer previously certified low-eight error estimates remain available separately; this comparison is with RC59's broad 22-feature energy bound.

## Residual construction and exact covariance

First construct the rounded 32-mode trial solutions for Legendre targets of degrees 0 through 21, using the identical denominator-10^30 rounding rule from RC38 and RC59. The exact Chebyshev conversion C22 transforms these into the already certified native trial columns V22. Equality with every RC59 coefficient is checked.

For each Legendre target, the nominal physical operator residual f_j=q_j-L_nom V_j is represented as

\[
f_j(y)=A_j(y)+B_j(y)\log y+C_j(y)\log(1-y),\qquad y=(x/B+1)/2.
\]

The additive generalized builder retains RC38's degree-192 regular/log kernel expansion, old rational constant center, and rigorously bounded series remainder. It extends the target count to 22 without changing historical validators. Computing Legendre residuals before the exact native congruence avoids confusing a Legendre target with a Chebyshev target.

All 132 same-parity upper-triangle mixed Gram entries are evaluated using directed 220-digit interval arithmetic and the six exact log-moment families inherited from RC38. The other 121 upper-triangle entries vanish by parity. Rational endpoints use denominator 10^20. Entrywise uncertainty is paid by diagonal row sums, yielding a certified nominal residual Gram upper matrix Q_leg,up. Exact congruence gives

\[
Q_{\rm native,up}=C_{22}^*Q_{\rm leg,up}C_{22}.
\]

## Actual constant correction and Riesz transport

Let d be RC56's corrected constant-center shift and delta_c its new radius. Keep the nominal residual functions above and pay their actual operator correction explicitly:

\[
\delta_R=2(|d|+\delta_c)+\varepsilon_{\rm series}.
\]

The factor 2 bounds the constant derivative I+Pi_e. Let T be the exact physical trial Gram, and choose t=1/1024. Matrix Young's inequality yields the actual physical operator-residual bound

\[
B_R=(1+t)Q_{\rm native,up}+(1+t^{-1})\delta_R^2T.
\]

The final matrix is rounded upward to denominator 10^24, with another exact diagonal row-sum allowance. For the actual Riesz errors E22=R22-V22 and rho=252/257, the canonical embedding gives

\[
E_{22}^*E_{22}\preceq\rho B_R,
\qquad (iE_{22})^*(iE_{22})\preceq\rho^2B_R.
\]

The physical operator residual, canonical Riesz error, and physical Riesz error are distinct objects; all three upper matrices are stored separately. The new canonical upper is checked below the RC59 upper by exact rational LDL. No floating eigensolver contributes to acceptance.

## Additional actual native Gram upper bound

The exact Riesz identity gives J=R22*V22 by physical pairing. With GT_nom the nominal canonical trial Gram, epsilon=10^-7 the inherited actual metric-error budget, and Ec_up the new canonical Riesz-error upper,

\[
M_{22}\preceq J+J^*-G_{T,\rm nom}+\epsilon T+E_{c,\rm up}.
\]

This additional upper matrix is stored and checked above RC59's Ritz lower matrix. RC59's physical-Gram conditioning and validated inverse enclosure remain available. RC60 does not replace that inverse enclosure with an unevaluated exact actual inverse.

## Independent replay

Generation expands all nine log-product integrals for each mixed Gram entry. Replay instead uses same-parity reflection to reduce the pairing to five integrals:

\[
R\left(\int AX+2\int AY\log y+2\int BX\log y+
2\int BY\log^2y+2\int BZ\log y\log(1-y)\right).
\]

Replay recomputes the residual functions, verifies every saved rational entry enclosure against this alternate formula, reconstructs the exact native congruence and transports, and checks the whole-matrix improvement over RC59. It also verifies input hashes and exact preservation of the original eight trial columns.

Generation and independent reflection-based replay both pass.

From the repository root:

```sh
python scripts/validate_rpb108_rc60_twenty_two_mixed_residuals.py > certificates/rpb108_rc60_twenty_two_mixed_residuals.json
python scripts/validate_rpb108_rc60_twenty_two_mixed_residuals.py --replay certificates/rpb108_rc60_twenty_two_mixed_residuals.json
```

## Remaining frontier

The next attachment is the signed original 22-feature Weil head and complete source covariance, followed by its actual projected-source bound. The existing low-eight floor remains valid, but no 22-feature floor or source threshold is established here. The inherited complement floor applies to the 1250-feature complement, not the 22-feature complement. No whole-aperture positivity, aperture extension, RH, or F4 completion is claimed.
