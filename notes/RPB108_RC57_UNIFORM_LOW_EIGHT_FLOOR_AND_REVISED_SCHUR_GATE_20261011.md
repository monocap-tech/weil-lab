# RPB108 RC57 — full low-eight positivity and a revised conditional Schur gate

RC57 certifies a uniform floor for the **entire actual low-eight native head** at cap B=11/10:

\[
\boxed{Q_8\succeq \frac{1}{2{,}900{,}000}M_8.}
\]

This holds for every complex coefficient vector in the span of the eight actual canonical Riesz features, not only for the two RC56 witness directions or the previously certified four-feature subspace. The proof preserves the full correlated residual and original-source Gram matrices and accepts the final matrix inequalities by exact rational arithmetic.

RC56's obstruction remains valid: a uniform floor 1/4000 is impossible on this head and any head containing it. RC57 supplies a smaller positive floor, rather than attempting to restore the disproved threshold.

## Certified matrix construction

Use the unchanged 32-mode trials V and the precision attachment from RC56. Let:

- T be their exact physical trial Gram;
- Qres_up be RC47's correlated upper Gram for the old nominal physical residual;
- Uplus_up be RC54's correlated upper Gram for the old nominal original trial source;
- Gnom be the canonical trial metric center;
- Hnom be the center of the complete signed bounded-remainder trial head from RC52;
- d be the certified constant-midpoint correction from RC56;
- rho=252/257 and k_even, k_odd be the inherited physical bounded-operator parity norm upper bounds.

RC56 supplies delta_R, delta_S, delta_H, including the correction from the old nominal centers, kernel tails, and rounding. With t=1/256, u=1/65536, form

\[
B=(1+t)Q_{\rm res,up}+(1+1/t)\delta_R^2T,
\qquad
U_a=(1+u)U_{\rm plus,up}+(1+1/u)\delta_S^2T.
\]

Both are checked positive semidefinite. They give simultaneous whole-map inequalities

\[
E^*E\preceq\rho B,\qquad
E_{\rm phys}^*E_{\rm phys}\preceq\rho^2B,\qquad
F_{\rm plus,trial}^*F_{\rm plus,trial}\preceq U_a.
\]

The exact original-source cancellation identity inherited from RC54 is

\[
Q_8=G_{\rm trial}+H_{\rm trial}
+E_{\rm phys}^*F_{\rm plus,trial}+F_{\rm plus,trial}^*E_{\rm phys}
-E^*E+E_{\rm phys}^*KE_{\rm phys}.
\]

Take s=42 in the source-linear Young inequality. The nominal combined head is N=Gnom+Hnom+dT; the c-dependent Fourier projection terms were cancelled before taking norms in RC56. If D is the diagonal row-sum enclosure of the nominal H entry-rounding errors, the actual head has the whole-matrix lower bound

\[
Q_8\succeq L_{\rm pre}
=N-\delta_HT-D-\rho B-\rho^2(s+k_{\rm parity})B-U_a/s.
\]

The parity factor acts separately on the even and odd blocks, whose cross entries vanish exactly. The term -rho B pays the negative canonical Riesz error Gram once. The bounded quadratic remainder is paid by -rho^2 k_parity B. No columnwise replacement of the residual or source covariance is made.

## Actual canonical metric upper bound

Let J=R*V be the exact physical native-feature/trial pairing. The exact Riesz identity is

\[
M_8=J+J^*-G_{\rm trial}+E^*E.
\]

The distance from the old nominal metric center is bounded by delta_G T, where

delta_G = 2(|d|+dc_new) + E_metric,old - 2 dc_old.

Therefore

\[
M_8\preceq M_{\rm pre}=J+J^*-G_{\rm nom}+\delta_GT+\rho B.
\]

Both matrix bounds are rounded outward to denominator 10^30, with diagonal row-sum error transport. The emitted matrices satisfy L <= Lpre and Mpre <= Mup, checked exactly. This rounding produces a compact replayable certificate and retains the full off-diagonal correlations.

The validator accepts the exact rational inequality

\[
L-\frac{1}{2{,}900{,}000}M_{\rm up}\succ0.
\]

Since Q8>=L and M8<=Mup, this proves the stated actual canonical head floor.

## Exact parity and Schur replay

For the target lower matrix L-h Mup, h=1/2,900,000, eliminate strong features {0,6} in the even block and {1,7} in the odd block. Both resulting 2x2 weak Schur matrices are positive definite. The following rounded values are displays of exact positive rational pivots stored in the certificate.

| Parity | LDL feature order | First pivot | Second pivot | Third pivot | Fourth pivot |
|---|---|---:|---:|---:|---:|
| Even | 0,6,2,4 | 0.02679429 | 0.04987254 | 1.66308391e-5 | 6.74044237e-8 |
| Odd | 1,7,3,5 | 0.02993060 | 0.02857765 | 8.42309233e-4 | 7.37641563e-7 |

Replay reconstructs trial metric and mass pairings by scalar sums, checks outward Loewner rounding, verifies positive LDL pivots in two orders, and independently verifies the strong inverses by their 2x2 adjugates and exact Schur completion. The final certificate does not rely on a floating eigensolver. Floating diagnostics were used only to choose the rational Young parameters and proposed floor; all accepted claims are then checked exactly.

## Revised conditional 1250-feature gate

The inherited RC44 complement floor is a=247/2500 on the **1250-feature orthogonal complement**. It is not a floor on the low-eight complement, so it cannot be combined directly with the new low-eight head certificate to conclude whole-aperture positivity.

A sufficient replacement gate for the 1250-feature head is:

| Obligation | Proposed certified threshold | Current status |
|---|---:|---|
| Actual full 1250-head floor | A1250 >= M1250/2,900,000 | Open; RC57 proves only its low-eight restriction |
| Actual projected canonical source-residual Gram | Gamma1250 <= M1250/64,000,000 | Open |
| Equivalent cross-norm bound | <= 1/8000 | Open |
| Complement floor | >= 247/2500 | Inherited from RC44 |

If the two open head/source obligations hold, the head Schur reserve is exactly

\[
\frac1{2{,}900{,}000}
-\frac{1/64{,}000{,}000}{247/2500}
=\frac{4279}{22{,}921{,}600{,}000}
>\frac1{5{,}800{,}000}>0.
\]

This rederived gate is sufficient and conditional. Its squared source-residual threshold is 6400/9, approximately **711.1 times tighter**, than the former 1/90,000 threshold; its cross-norm threshold is 80/3 times smaller than 1/300. The old gate's head floor was disproved by RC56, so it cannot remain the operational target.

A larger head may have a smaller floor than its low-eight restriction. RC57 does not establish that the proposed smaller floor survives all 1242 additional features or their interactions. A blockwise gate can retain distinct strong and weak floors, but would require its corresponding actual source-coupling estimates.

## Artifacts, verification, and scope

From the repository root:

```sh
python scripts/validate_rpb108_rc57_uniform_low_head_floor.py > certificates/rpb108_rc57_uniform_low_head_floor.json
python scripts/validate_rpb108_rc57_uniform_low_head_floor.py --replay certificates/rpb108_rc57_uniform_low_head_floor.json
```

Generation and independent replay pass. The certificate records input SHA-256 hashes, exact lower-head and upper-metric matrices, outward rounding allowances, positive parity Schur certificates, and all conditional gate arithmetic.

The RC53 low-eight projected source-residual upper bound 3.2375584721 M remains valid; RC57 does not tighten it. That bound concerns projection onto the low-eight span and is not a certificate of the required full 1250-head projected source bound.

No full 1250 projection or head matrix is constructed here. No whole-aperture positivity, aperture extension, RH, or F4 completion is claimed.

The next frontier is to extend the certified positive head beyond eight features while keeping the weak-direction covariance, and to certify the actual projected source coupling against a compatible Schur budget. The uniform low-eight positivity obligation is now closed.
