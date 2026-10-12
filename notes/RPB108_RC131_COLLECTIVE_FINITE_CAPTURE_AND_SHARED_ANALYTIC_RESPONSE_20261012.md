# RPB108 — RC131: collective finite capture and shared analytic response

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Starting checkpoint RC130, commit c3bf608700e4be85f67fc2bee1de5c46982738e3.

## Result

RC131 captures the dominant finite-source part of Cw_14 in one collective vector. It keeps the entire analytic-source action paid by contraction and certifies every old four-input residual mixture after enrichment. At the selected 10^-12 finite-source norm target, the new w_14 coordinate satisfies

\[
\boxed{R_{ww,new}/\|w_{14}\|_D^2<6.276805\times10^{-7}.}
\]

Its absolute upper is below 3.762965e-9, over 7,562 times smaller than RC130's actual coordinate lower before enrichment. This demonstrates that the earlier w_14 obstruction is collectively removable; it does not assert an exact zero row or high-accuracy full action on the analytic part.

The remaining analytic source has an exact shared-leading-action relation:

\[
\boxed{Cw_{14}=\alpha C\psi_0+Cb+Ca_1,\qquad
\alpha=0.850307215745097778\ldots,}
\]

where b is one finite polynomial with certified positive coefficient intervals and

\[
 \boxed{\|Ca_1\|_D^2<4.037\times10^{-14},
 \qquad\|Ca_1\|_D<2.009072\times10^{-7}.}
\]

The leading analytic action is therefore shared with Cpsi_0. Numerical Cb, the corresponding near-rank-one residual reduction and its enlarged joint Gram remain to be certified. The exact identity and paid remainder are established here; the action of b is not hidden in the certificate.

RC130's reference P_0 response interval is inherited unchanged. No new inverse-response interval or original Weil positivity is certified in this pass.

## Definitions and source split

Keep D=J+sI, JP_n=H_nP_n, s=c_R+log2+789/125, B=11/10, endpoint form h=-1/2 log(1-(x/B)^2), and positive D-energy contraction C=D^-1 h. Set z_n=n(n+1) and d_n=2H_{2n}-2H_n+1/(2n+1)-log2.

Let U=[P_0,psi_0,f_0,w_14] be RC129's four-vector family, with complete Gram and endpoint pairing data. RC128's selected w_14 has the exact representation

\[
 w_{14}=\hat g+a,\qquad
 a=\sum_{k=0}^{14}\hat\mu_k\xi_k,
\]

\[
 (\xi_k)_n=\frac{(2n+1)\lambda^k}{(H_n+s)z_n^{k+1}}
 \quad(n\ge4096,\ n\text{ even}),\qquad\lambda=z_{988}.
\tag{1}
\]

Other xi_k coefficients vanish. The rational polynomial g_hat has even support 0..4094. All its coefficients and the retained mu_hat_k are positive. RC131 reconstructs g_hat and checks its center/radius coefficient SHA-256 against RC128 before applying C.

Linearity gives Cw_14=Cg_hat+Ca. RC130 pays the full analytic input energy:

\[
 \|Ca\|_D^2\le\|a\|_D^2\le E_a,
 \qquad E_a<3.762965\times10^{-9}.
\tag{2}
\]

This conservative upper follows from C's contraction, not from evaluating or zeroing the analytic-source action.

For any projection span E and input family V, define

\[
 R_E(V)=(CV)^*D(I-\Pi_E)CV,
\tag{3}
\]

where Pi_E is D-orthogonal projection. The new covariance bounds below are for R_E(U), with four input columns and a five-dimensional projection span. They are not the complete five-input covariance R_E(E).

## One collective approximation to the finite-source action

Apply the exact positive endpoint coefficient formula

\[
 (C\hat g)_n=\frac1{H_n+s}
 \left[d_n\hat g_n+
 \sum_{m\ne n\atop m\text{ even}}
 \frac{(2n+1)\hat g_m}{|z_n-z_m|}\right].
\tag{4}
\]

Directed 70-digit arithmetic encloses every finite output through even degree 8190. Rational centers on a 10^-40 grid give a single polynomial p_hat. The actual s/log2 uncertainty and polynomial rounding are summed in D energy on a 10^-100 grid. Its generator, 4,096 coefficient count and center/radius SHA-256 are stored for reconstruction.

After output cutoff O=8191, define Lambda=z_4094=16764930, rho=Lambda/z_8192<1/4, and new analytic output features

\[
 (\eta_k)_n=\frac{(2n+1)\Lambda^k}{(H_n+s)z_n^{k+1}}
 \quad(n\ge8192,\ n\text{ even}).
\tag{5}
\]

Other eta_k coefficients vanish. Define nu_0=sum_m g_hat_m, and for k>=1,

\[
 \nu_k=\sum_m\hat g_m(z_m/\Lambda)^k.
\tag{6}
\]

These positive finite moments differ from the inherited mu_hat_k in (1). They describe Cg_hat's output tail, not the input analytic tail of w_14.

Writing p for the exact finite output of Cg_hat, the geometric denominator expansion gives

\[
 C\hat g=p+\sum_{k=0}^{\infty}\nu_k\eta_k.
\tag{7}
\]

For retained order K, the omitted coefficients are bounded by eta_0,n nu_{K+1} rho^(K+1)/(1-rho). The full leading eta_0 D energy is bounded by the monotone parity-tail estimate at even degree 8190. Thus the entire infinite output is paid; no finite output trial is identified with Cg_hat.

The added **single** vector is

\[
 v_K=\hat p+\sum_{k=0}^K\hat\nu_k\eta_k,
\tag{8}
\]

where the moment centers and radii are enclosed from positive finite sums. The finite polynomial and all retained analytic features are combined into one energy vector, rather than added independently to the source family.

If E_p is the finite polynomial squared error, T_eta bounds ||eta_0||_D squared and r_k are the nu_k interval radii, then

\[
\|C\hat g-v_K\|_D\le
\sqrt{E_p}+\sqrt{T_\eta}\sum_{k=0}^K r_k\rho^k
+\sqrt{T_\eta}\frac{\nu_{K+1,upper}\rho^{K+1}}{1-\rho}.
\tag{9}
\]

Directed scalar sums and exact rational upward square roots accept (9). Its three parts pay finite output rounding, retained moment rounding, and the full omitted analytic series.

| Finite-source action norm target, relative to ||w_14||_D | Highest retained order | Internal output-tail features | Added energy vectors |
|---|---:|---:|---:|
| 10^-6 | 1 | 2 | 1 |
| 10^-12 | 10 | 11 | 1 |
| 10^-24 | 29 | 30 | 1 |

The norm scaling uses the old w_14 source energy, not a newly claimed native spectral norm. The counts are sufficient under (9), not optimal dimension claims.

## Dominant residual capture, analytic remainder retained

From (2), (9) and the norm triangle inequality,

\[
\boxed{\|Cw_{14}-v_K\|_D
\le\|C\hat g-v_K\|_D+\sqrt{E_a}.}
\tag{10}
\]

The images of the finite and analytic input parts are not assumed D-orthogonal. Paying their norm triangle cross term is necessary even though the original input supports are disjoint.

At the selected 10^-12 finite-source target,

\[
 \|C\hat g-v_{10}\|_D<3.396778\times10^{-14},
 \quad\|Cw_{14}-v_{10}\|_D<6.134301\times10^{-5}.
\tag{11}
\]

The full bound is dominated by E_a. Increasing the finite-source target to 10^-24 makes almost no change to the whole-action upper. This is an information limit of the present sufficient bound, not a lower bound on the actual analytic-source action or its projected residual.

Let E_K=span(U,v_K). The distance estimate using RC130's old positive w_14 residual gives

\[
\|(I-\Pi_U)v_K\|_D\ge
\sqrt{R_{ww,old,lower}}-\|Cw_{14}-v_K\|_D>0.
\tag{12}
\]

Exact rational root rounding is paid. Thus v_K is independent of U and E_K has dimension five. At the selected target, the accepted squared distance lower exceeds 2.780502e-5.

The new coordinate upper follows immediately from the trial v_K in E_K:

\[
 (R_{E_K}(U))_{ww}\le\|Cw_{14}-v_K\|_D^2.
\tag{13}
\]

At K=10 this is below 3.762965e-9 in absolute D energy and below 6.276805e-7 relative to actual G_ww. RC130's old lower cannot be retained as a lower for this enlarged projection; it is used only to prove the new vector independent and quantify the capture.

## Every old-input residual mixture paid

The P_0 row remains exactly zero. Projection monotonicity preserves the old f_0 upper and gives

\[
 (R_{E_K}(U))_{\psi\psi}\le\delta_\psi,
 \quad (R_{E_K}(U))_{ff}\le\delta_f,
 \quad (R_{E_K}(U))_{ww}\le\delta_w,
\tag{14}
\]

where delta_psi is RC130's accepted upper below 4.094930e-8, delta_f is RC128's tiny accepted f_0 upper, and delta_w is (13). Residual Cauchy-Schwarz bounds every off-diagonal magnitude by sqrt(delta_i delta_j). In particular, at the selected target,

\[
 |(R_{E_K}(U))_{\psi,w}|<1.241333\times10^{-8}.
\tag{15}
\]

The certificate stores the signed entry enclosure and the full Loewner upper

\[
0\preceq R_{E_K}(U)\preceq
 3\operatorname{diag}(0,\delta_\psi,\delta_f,\delta_w).
\tag{16}
\]

Equation (16) follows by Cauchy-Schwarz for the three potentially nonzero residual vectors and is valid for every complex source mixture. It does not assert that the covariance is diagonal, or that the remaining psi_0 coordinate is small relative to its own source energy.

These are four-input residual bounds. They cannot replace the complete five-input covariance in a new Schur inverse calculation: Cv_K and the full enlarged joint Gram/pairing remain uncomputed.

## Exact shared analytic source identity

Let psi_prefix be the psi_0 polynomial supported at even degrees 990..4094. The exact coefficient definitions imply xi_0=psi_0-psi_prefix. Set

\[
 \alpha=\hat\mu_0,
 \quad b=\hat g-\alpha\psi_{prefix},
 \quad a_1=\sum_{k=1}^{14}\hat\mu_k\xi_k.
\tag{17}
\]

Here alpha is the rational center already used in the exact definition of w_14; it is not substituted for the unrounded mu_0 of Cf_0. Therefore

\[
 w_{14}=\alpha\psi_0+b+a_1,
 \qquad Cw_{14}=\alpha C\psi_0+Cb+Ca_1
\tag{18}
\]

are exact identities. Every finite b coefficient interval is reconstructed from the actual s enclosure and verified positive. Their SHA-256 and support are stored. Cb is not evaluated by the Cg_hat certificate; the two finite sources differ.

Using rho_old=lambda/z_4096 and RC129's leading input-tail D energy T_old,

\[
 \|Ca_1\|_D^2\le\|a_1\|_D^2\le
 T_{old}\left(\sum_{k=1}^{14}\hat\mu_k\rho_{old}^k\right)^2
 <4.037\times10^{-14}.
\tag{19}
\]

This isolates the higher analytic correction after the shared Cpsi_0 term. It is an actual norm upper for the full higher-source action, not a sampled tail approximation.

If a future projection span contains a trial z_b with ||Cb-z_b||_D<=epsilon_b, then its residuals obey

\[
 \|r_w-\alpha r_\psi\|_D\le
 \epsilon_b+\sqrt{\|Ca_1\|_{D,upper}^2}=:e.
\tag{20}
\]

Consequently the remaining two-column covariance has paid near-rank-one identities

\[
 |R_{\psi,w}-\alpha R_{\psi\psi}|
 \le\sqrt{R_{\psi\psi,upper}}\,e,
\]

\[
 |R_{ww}-\alpha^2R_{\psi\psi}|
 \le2\alpha\sqrt{R_{\psi\psi,upper}}\,e+e^2.
\tag{21}
\]

Equations (20)–(21) are conditional on a paid finite balanced-source action trial. They are not asserted for the currently certified E_K merely because Cg_hat was captured. This gives a concrete shared-response route for the next correlation investigation, instead of assuming that Cw_14 requires an unrelated full analytic direction.

## Decision and next cursor

The dominant Cw_14 residual can be captured in one vector, with over a 7,562-fold certified coordinate reduction at a sufficient 10^-12 finite-source target. The remaining uncertainty is genuinely at the analytic-source layer. The exact source identity shares its leading action with Cpsi_0 and pays the higher correction at about 2.010e-7 in D norm.

**RC132 cursor:** evaluate the finite balanced action Cb in (17) and test the quantitative shared residual relation (20)–(21) against the signed response budget. This can expose a single shared leading analytic response, with a paid higher-tail correction. Any selected enlarged family must receive its own full joint Gram and endpoint pairing before its covariance is used in a new Schur inverse bound. The independently certified E_10 finite-part capture remains available as a comparison certificate; no covariance or conditioning is transferred between distinct projection spans without proof.

RC130's normalized P_0 reference response interval [0.931327855055,0.931339797136] remains the latest certified inverse-response enclosure. RC131 does not tighten it. Its high finite-source accuracy is a single-action representation budget, not full Cw_14 accuracy or an inverse solve.

D-energy endpoint covariance is still distinct from original Weil source leakage. Original completion requires Hhat=A_Q+T_Weil^*T_Weil >= eta I and T_Weil Hhat^-1T_Weil^* <= theta I with theta<1 after original source actions. The inherited original count and W_639 floor are unchanged. No original positivity, Global/F4, RH or Lean extension is claimed.

**Certified:** one collective finite-source response, paid whole Cw_14 error, exact five-dimensional enrichment, full four-input residual mixtures, dominant coordinate capture, positive balanced-source coefficient intervals, exact shared analytic identity and paid higher-source action. **Conditional:** near-rank-one residual after a paid Cb trial. **Not performed:** Cb, full five-vector Gram/pairing or covariance, Cv_K, a new inverse-response interval, regular/original actions or original positivity.

## Reproduction

Inputs: RC130, RC129, RC128, in that order. Byte-level SHA-256 links and the independently reconstructed g_hat coefficient hash are checked. Positive finite action and moment sums use directed 70-digit arithmetic; tail, norm, independence and covariance acceptance uses exact rational bounds. Six exact rational geometric controls include the zero-degree source mass, multiple retained orders and output levels. Replay reverses finite-source action and moment sums and compares the complete rational certificate, including the balanced-source coefficient hash.

```bash
python scripts/validate_rpb108_rc131_finite_part_response_capture.py \
 --output certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay. Only additive RC131 script, certificate and note files are committed; historical RC, Lean and unrelated branch work is preserved.
