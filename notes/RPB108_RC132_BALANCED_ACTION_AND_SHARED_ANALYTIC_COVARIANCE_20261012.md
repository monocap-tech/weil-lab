# RPB108 — RC132: balanced action and shared analytic covariance

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC131, eee0bb519d400f03c5ecd049f1f87f4126692a52.

## Result

The finite balanced action Cb is now certified, with its full infinite output paid. One collective vector z_b approximates Cb. At the selected relative 10^-12 target (scaled by ||w_14||_D), it uses seven internal analytic output features and satisfies

\[
\|Cb-z_b\|_D<5.278037\times10^{-14}.
\]

Let U=span(P_0,psi_0,f_0,w_14), let v_10 denote RC131's selected collective Cg_hat trial, and define the new projection span

\[
E=\operatorname{span}(U,v_{10},z_b).
\]

This span has dimension at most six. Both v_10 and z_b are individually independent of U; independence of their two classes modulo U is not asserted. No six-vector Gram lower is inferred from separate independence checks.

For r_u=(I-Pi_E)Cu, RC131's exact shared-source identity gives

\[
r_w=\alpha r_\psi+\delta,\qquad
\alpha=0.850307215745097778\ldots,
\quad \|\delta\|_D<2.009073\times10^{-7}.
\]

The inherited v_10 trial bounds ||r_w||_D^2 by 3.762965e-9. Consequently the shared relation improves the psi residual upper by more than 7.816781-fold:

\[
\boxed{R_{\psi\psi,E}<5.238639\times10^{-9}.}
\]

It also certifies the correlation identities

\[
\boxed{|R_{\psi w,E}-\alpha R_{\psi\psi,E}|<1.454136\times10^{-11},}
\]
\[
\boxed{|R_{ww,E}-\alpha^2R_{\psi\psi,E}|<2.476960\times10^{-11}.}
\]

These are paid upper bounds around a shared leading residual channel. They establish neither a nonzero leading channel nor an exact rank-one covariance. Enlarged joint Gram, endpoint pairings, new-vector actions and an improved inverse response remain open.

## Definitions and actual source uncertainty

Use RC131's D, C, s, z_n=n(n+1), eta_k and exact source relation

\[
w_{14}=\alpha\psi_0+b+a_1,
\quad b=\hat g-\alpha\psi_{prefix},
\quad Cw_{14}=\alpha C\psi_0+Cb+Ca_1.
\]

The psi prefix is supported on even degrees 990..4094; b on even degrees 0..4094. The alpha coefficient is the exact rational moment center defining w_14. The b coefficients retain their actual dependence on s. The validator encloses that uncertainty; it never substitutes interval centers for b without paying the resulting action error.

RC128's g_hat coefficient hash and RC131's entire b coefficient interval hash are independently reconstructed and matched. The positive b intervals allow directed positive endpoint sums and positive geometric moments.

## Full balanced finite action

For every even n through 8190, evaluate

\[
(Cb)_n=\frac{1}{H_n+s}\left[d_n b_n+
\sum_{m\ne n,\ m\text{ even}}\frac{(2n+1)b_m}{|z_n-z_m|}\right],
\qquad d_n=2H_{2n}-2H_n+\frac1{2n+1}-\log2.
\]

All finite outputs are enclosed in directed 70-digit arithmetic. Rational centers on the inherited 10^-40 grid define p_b_hat; the actual constant uncertainty, b input uncertainty and output rounding are enclosed together and summed in D energy.

Set Lambda=z_4094, rho=Lambda/z_8192<1/4. Positive finite moments

\[
\nu_{b,k}=\sum_m b_m(z_m/\Lambda)^k
\]

give the exact output above 8190 as sum_{k>=0} nu_{b,k} eta_k. The trial is

\[
z_{b,K}=\hat p_b+\sum_{k=0}^K\hat\nu_{b,k}\eta_k.
\]

Using RC131's paid eta_0 energy upper T, the full norm error is enclosed by

\[
\epsilon_b\le\sqrt{E_p}+\sqrt T\sum_{k=0}^K r_k\rho^k
+\sqrt T\frac{\nu_{b,K+1,upper}\rho^{K+1}}{1-\rho}.
\]

The three terms pay all finite output error, retained moment rounding and the entire omitted analytic series. The zero-degree source mass is retained in nu_{b,0}.

| Relative action norm target, scaled by ||w_14||_D | Highest retained order | Internal analytic features | Added collective vectors |
|---|---:|---:|---:|
| 10^-6 | 0 | 1 | 1 |
| 10^-12 | 6 | 7 | 1 |
| 10^-24 | 25 | 26 | 1 |

These are sufficient representation counts, not claims of minimal dimension. Increasing finite action accuracy beyond the selected target hardly changes the shared residual error, which is dominated by the inherited higher analytic action bound.

## Shared covariance in explicit projection spans

For F_b=span(U,z_b), projection contraction and the exact identity imply

\[
\|(I-\Pi_{F_b})Cw-\alpha(I-\Pi_{F_b})C\psi\|_D
\le\epsilon_b+\sqrt{E_{a_1}}=:e.
\]

RC130's psi upper applies by projection monotonicity. Moreover,

\[
\operatorname{dist}_D(z_b,U)\ge
\sqrt{R_{ww,U,lower}}-\alpha\sqrt{R_{\psi\psi,U,upper}}-e>0.
\]

At the selected target its squared lower exceeds 2.664750e-5. Thus F_b has dimension five, independently of RC131's distinct five-dimensional span span(U,v_10). Its own w upper does not improve RC131's v_10 bound; no transfer between those two spans is asserted.

For their union E, both trial bounds apply. Write d_w for RC131's v_10 squared action upper and d_psi for RC130's psi covariance upper. Then

\[
R_{\psi\psi,E}\le
p:=\min\left(d_\psi,\frac{(\sqrt{d_w}+e)^2}{\alpha^2}\right),
\qquad R_{ww,E}\le d_w.
\]

Residual Cauchy-Schwarz gives

\[
|R_{\psi w,E}-\alpha R_{\psi\psi,E}|\le\sqrt p\,e,
\quad
|R_{ww,E}-\alpha^2R_{\psi\psi,E}|\le2\alpha\sqrt p\,e+e^2.
\]

For every complex pair x,y, the certificate also supplies the directional Loewner upper

\[
0\preceq R_E(\psi,w)\preceq
2p\begin{pmatrix}1&\alpha\\\alpha&\alpha^2\end{pmatrix}
+2e^2\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]

This pays arbitrary signed/complex mixtures, including cancellation along x=-alpha*y. It does not diagonalize the covariance or silently omit cross terms. P_0's exact zero residual and f_0's tiny RC128 residual upper are inherited by projection monotonicity, but actions on the new vectors are not evaluated here.

## Evidence boundary and RC133 cursor

RC132 certifies Cb, a full infinite-output action trial, its independence from U, and a shared two-input covariance bound in the explicitly defined union span. The remaining leading analytic action is Cpsi_0; the higher correction remains paid by contraction.

RC133 should certify the selected union family's full joint Gram and endpoint pairings, determine its actual conditioning/dimension, and then certify Cpsi_0 and the added-vector covariance needed for an inverse solve. A near-rank-one old-input residual enclosure cannot substitute for complete enlarged-input covariance in a Schur calculation.

RC130's normalized P_0 reference response interval [0.931327855055,0.931339797136] remains unchanged. No new inverse-response interval, original Weil source action, original positivity, whole-aperture extension, F4, RH or Lean result is claimed.

## Reproduction

Inputs are RC131, RC130, RC129 and RC128 in that order. All byte-level input hash links and the two reconstructed coefficient hashes are checked. Reverse replay reverses action and moment summation order and compares the complete certificate exactly. Six rational geometric controls include zero-degree mass and the maximal finite source degree.

```bash
python scripts/validate_rpb108_rc132_balanced_action_shared_covariance.py \
 --output certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay. Only the additive RC132 validator, certificate and note are included in this checkpoint.
