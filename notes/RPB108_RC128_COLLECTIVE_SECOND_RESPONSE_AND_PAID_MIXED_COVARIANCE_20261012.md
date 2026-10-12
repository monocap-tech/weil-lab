# RPB108 — RC128: collective second response and paid mixed covariance

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Starting checkpoint RC127, commit 08bb3ae5a77142a6d1a70205c50b175a15a8db02.

## Result and scope

RC128 constructs a single collective finite/analytic energy vector approximating C f_0. Adding it to RC127's family V_e=span{P_0,psi_0,f_0} removes that checkpoint's actual f_0 projected covariance obstruction to prescribed single-action budgets. All analytic output, actual-constant uncertainty, finite polynomial rounding and retained moment rounding are paid.

| Relative C f_0 approximation D norm target | Highest retained analytic order | Internal analytic features | Added energy vectors | Certified relative f_0 covariance upper, outward display |
|---|---:|---:|---:|---:|
| 10^-6 | 0 | 1 | 1 | 6.008610e-13 |
| 10^-12 | 5 | 6 | 1 | 7.039158e-27 |
| 10^-24 | 14 | 15 | 1 | 6.850461e-50 |

The finite part is one rational polynomial of degree 4094, with 2,048 even coefficients. Its analytic features are combined into the same added vector; they are not 15 independent added source directions. A paid distance lower proves the added vector is outside V_e, so the enriched family has dimension four at each stated budget.

The old input family's complete residual mixtures are bounded after projection onto this enriched span, including the psi_0/f_0 correlation. The psi_0 diagonal inherits a conservative upper from RC127. No new smallness theorem for psi_0 is obtained. The new collective vector's own action, full enlarged-family Gram/pairing matrices and inverse response remain open.

The estimates below concern the endpoint contraction and its reference energy. They establish no new original Weil direction, no original positivity extension, no Global/F4 result and no RH result. The original count remains 10–639 below 0.01.

## Definitions before use

Keep D=J+sI, JP_n=H_nP_n, s=c_R+log2+789/125, B=11/10, and the actual endpoint form h=-1/2 log(1-(x/B)^2). The endpoint action C=D^-1 h is the bounded positive contraction on D energy certified in RC121. Put z_n=n(n+1) and d_n=2H_{2n}-2H_n+1/(2n+1)-log2.

RC126's exact symbolic response polynomial is

\[
 f_0=\sum_{\substack{2\le m\le988\\m\text{ even}}}
 b_mP_m,\qquad b_m=\frac{2m+1}{(H_m+s)z_m}>0.
\tag{1}
\]

The inherited psi_0 has the same coefficient expression at every even degree n>=990, and zero elsewhere. The exact identity CP_0=((1-log2)/s)P_0+psi_0+f_0 remains valid.

For an input family V and a projection span U, define its projected action covariance by

\[
R_U(V)=(CV)^*D(I-\Pi_U)CV,
\tag{2}
\]

where Pi_U is D-orthogonal projection. It is a positive Gram matrix. RC127's covariance is R_{V_e}(V_e). In RC128, the input family still has three columns, while the projection span gains one column. R_U(V_e) is therefore a three-by-three matrix; it is not the complete four-by-four R_U(U).

## Exact collective tail of C f_0

For even n>988, the exact endpoint coefficient formula gives

\[
 (Cf_0)_n=\frac{2n+1}{H_n+s}\sum_m\frac{b_m}{z_n-z_m}.
\tag{3}
\]

Separate the output after cutoff L=4095, so its first omitted even degree is 4096. Define lambda=z_988=977132 and

\[
 \rho=\frac{\lambda}{z_{4096}}
 =0.058227390087\ldots<0.059.
\tag{4}
\]

At the original cutoff, z_988/z_990 is approximately 0.995966. Moving the finite output cutoff makes the geometric expansion much less expensive without changing the actual action.

Define the new exact analytic features and positive finite moments by

\[
 (\xi_k)_n=\frac{(2n+1)\lambda^k}{(H_n+s)z_n^{k+1}}
 \quad(n\ge4096,\ n\text{ even}),\qquad
 \mu_k=\sum_m b_m(z_m/\lambda)^k.
\tag{5}
\]

Other xi_k coefficients vanish. Each xi_k is in D energy; xi_k coefficients are bounded by rho^k xi_0 coefficients. Let g be the exact finite output of C f_0 through degree 4094. The geometric expansion in (3) yields the **full** decomposition

\[
 Cf_0=g+\sum_{k=0}^{\infty}\mu_k\xi_k.
\tag{6}
\]

For a retained order K, positivity gives coefficientwise

\[
0\le\left(Cf_0-g-\sum_{k=0}^K\mu_k\xi_k\right)_n
\le(\xi_0)_n\frac{\mu_{K+1}\rho^{K+1}}{1-\rho}.
\tag{7}
\]

This uses the actual moment mu_{K+1}, rather than replacing every finite coefficient by a worst-case endpoint mass. The series converges in D energy by the geometric bound. It is a source-response representation, not an invariant spectral family or an original Weil eigenspace.

## Directed coefficients and complete error budget

The finite output g is computed from

\[
(Cf_0)_n=\frac1{H_n+s}\left[
d_nb_n+\sum_{m\ne n}\frac{(2n+1)b_m}{|z_n-z_m|}\right],
\tag{8}
\]

with b_n=0 outside the support in (1). All relevant entries and input coefficients are positive, so directed 70-digit interval sums enclose every coefficient. Rational centers g_hat use the same 10^-40 coefficient grid as RC127. The generator, coefficient count and joint center/radius SHA-256 are stored for reconstruction.

The finite polynomial squared D error is below 1.879e-64. RC127 used deliberately broad 10^-40 energy rounding for its modest action budgets. RC128 recomputes these same coefficient errors on a 10^-100 energy grid so that this conservative reporting floor does not obstruct a 10^-24 norm target. RC127 is preserved unchanged; this is a sharper additive error certificate, not a claim that its coarse energy sum had higher precision.

Each mu_k is a finite positive sum from (5). Its accepted rational interval supplies a center mu_hat_k and a radius r_k. Moments through order 40 are stored. Let T bound ||xi_0||_D squared. The inherited monotone parity-tail estimate, evaluated at even degree 4094, gives

\[
T\le\frac{B}{(s_{lower}+H_{4094,lower})4093\cdot4094}.
\tag{9}
\]

The collective **single** vector is

\[
 w_K=\hat g+\sum_{k=0}^K\hat\mu_k\xi_k.
\tag{10}
\]

The xi_k retain their exact actual-s definitions. Their numerical Gram matrices and further endpoint actions are not assumed evaluated merely because their representation is supplied.

If E_g bounds ||g-g_hat||_D squared, then

\[
\boxed{\|Cf_0-w_K\|_D\le
\sqrt{E_g}
+\sqrt{T}\sum_{k=0}^Kr_k\rho^k
+\sqrt{T}\frac{\mu_{K+1,upper}\rho^{K+1}}{1-\rho}.}
\tag{11}
\]

This triangle bound is conservative; it does not assume orthogonality among analytic features. Directed scalar sums and exact rational upward square roots accept (11). Both the retained-feature rounding and the complete omitted infinite series are paid.

| Target | Absolute full action norm error upper, outward display |
|---|---:|
| 10^-6 relative to ||f_0||_D | 2.071945e-7 |
| 10^-12 relative to ||f_0||_D | 2.242598e-14 |
| 10^-24 relative to ||f_0||_D | 6.996019e-26 |

These certify one action, not an inverse response at those tolerances. The feature counts are sufficient under (11), not optimal dimension claims.

## What the enlarged projection certifies

Let U_K=span{P_0,psi_0,f_0,w_K}. Equation (11) immediately gives

\[
 (R_{U_K}(V_e))_{ff}\le\|Cf_0-w_K\|_D^2=:\delta_f.
\tag{12}
\]

The exact P_0 residual remains zero because U_K contains V_e. Since projections onto larger spans can only reduce residual energy,

\[
0\le(R_{U_K}(V_e))_{psi,psi}
\le(R_{V_e}(V_e))_{psi,psi}
\le\delta_\psi,
\tag{13}
\]

where delta_psi is RC127's accepted upper, below 6.805270e-8. This is a conservative inherited upper, not a positive lower or a new small-variance assertion.

Residual Cauchy-Schwarz pays the unresolved mixed term:

\[
 |(R_{U_K}(V_e))_{psi,f}|\le\sqrt{\delta_\psi\delta_f}.
\tag{14}
\]

At the 10^-24 target, this absolute mixed covariance upper is below 1.825046e-29. Thus the new f row is controlled together with its old-family mixing; it is not inserted as a diagonal bound while ignoring correlations.

For any positive rational t, equations (12)–(14) give a full old-input Loewner upper

\[
0\preceq R_{U_K}(V_e)\preceq
\operatorname{diag}\left(0,(1+t)\delta_\psi,
(1+1/t)\delta_f\right).
\tag{15}
\]

The certificate stores (15) with t equal to the selected relative norm target. The choice allocates mixed-error payment; it does not change the source metric. It deliberately keeps the remaining psi_0 block visible.

RC127's lower ||(I-Pi_{V_e})Cf_0||_D squared >=0.001327614390662 also implies

\[
\|(I-\Pi_{V_e})w_K\|_D\ge
\sqrt{0.001327614390662}-\|Cf_0-w_K\|_D>0.
\tag{16}
\]

The exact rational certificate uses RC127's stronger undisplayed rational lower and pays square-root rounding. Thus w_K is independent of the old family, and the enriched dimension is exactly four. The new collective vector captures a real action direction; it is not a redundant precision refinement of the exact zero P_0 row.

## Decision and next cursor

RC127's f_0 obstruction is quantitatively removable with one collective response vector. Its infinite tail needs only 15 internal positive moment features at the 10^-24 single-action target after the finite output is retained through degree 4094. The source-family residual matrix now has a tiny paid f row and a remaining psi_0 block.

This does not settle the complete four-vector covariance. C w_K can leave U_K, and such leakage can affect an inverse response through internal coupling even though the old P_0 and f_0 columns close exactly or approximately. RC123's finite-tail nonclosure is not contradicted by the constructed approximation.

**RC129 cursor:** certify the full joint G and H on U_K for a concrete selected K, paying the overlapping polynomial/analytic supports and all finite–tail correlations. Then control the remaining C psi_0 and C w_K block by actual action, covariance or a signed resolvent estimate. The 10^-24 representation is available, but first verify whether that accuracy is needed for the matrix response budget. Merely adding independently certified tail diagonals will not pay their joint correlations.

These are D-energy endpoint/reference calculations. The original completion condition remains Hhat=A_Q+T_Weil^*T_Weil >= eta I and T_Weil Hhat^-1 T_Weil^* <= theta I for theta<1. Original arithmetic actions and this augmented response remain unevaluated. The inherited W_639 floor is not transferred to the new physical response span.

**Certified:** exact tail moment expansion, paid single collective C f_0 approximation, sufficient feature budgets, exact four-dimensional enrichment, and the complete three-input projected residual Loewner upper after enrichment. **Not certified:** the four-vector joint Gram/pairing, full enlarged covariance, a small psi_0 variance, high-accuracy reference inverse, regular action, or original positivity.

## Reproduction and verification

Inputs, in order: RC127, RC126, RC124. Byte-level SHA-256 linkage is checked. The validator imports RC127's directed-arithmetic and exact rational acceptance helpers without modifying that checkpoint. It reconstructs the finite response coefficients and all positive moments. Nine exact rational scalar controls test the geometric identity and remainder at multiple output levels and retained orders. Replay reverses finite-source action and moment sums and compares the complete rational certificate.

```bash
python scripts/validate_rpb108_rc128_collective_second_response.py \
 --output certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc127_enriched_even_endpoint_action.json \
 certificates/rpb108_rc126_finite_response_variance.json \
 certificates/rpb108_rc124_actual_joint_endpoint_moment.json
```

Repeat with --replay. Only additive RC128 validator, certificate and note files are committed; prior RC, Lean and unrelated branch files are preserved.
