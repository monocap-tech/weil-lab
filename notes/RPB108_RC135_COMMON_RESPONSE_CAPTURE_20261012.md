# RPB108 — RC135: common response capture

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC134, ca2ca9d1003aacc72d305855b1c4024cb75c969d.

## Result

One collective trial for C(v+z)/2 captures both new-vector leakage coordinates. At the selected relative 10^-12 finite-source norm target, eleven internal analytic output features give

\[
\|Cu_{finite}-t_{10}\|_D<1.356825\times10^{-14},
\quad \|Cu-t_{10}\|_D<2.573638\times10^{-5}.
\]

For F=span(E,t_10),

\[
\boxed{R_{vv,F},R_{zz,F}<4.134492\times10^{-9}.}
\]

The new v upper is more than 200.767868 times smaller than RC134's old v lower. The new trial's squared distance to E exceeds 7.170422e-7, certifying dim(F)=7. No old v lower is transferred to F.

The common residual satisfies R_uu,F<6.623610e-10; the full old-six residual covariance, including signed common/difference correlations, is paid. The complete seven-input covariance and inverse response remain open.

| Relative finite-source action norm target | Internal analytic output features | Added vectors |
|---|---:|---:|
| 10^-6 | 2 | 1 |
| 10^-12 | 11 | 1 |
| 10^-24 | 30 | 1 |

The feature counts are sufficient under the certified geometric bound. Increasing finite action accuracy beyond the selected target has negligible effect on the full action bound, which is dominated by the paid analytic input action. The coordinate bound additionally pays the v-z residual difference.

## Definitions and target

Retain the exact old six-vector family U=(P_0,psi_0,f_0,w_14,v_10,z_b,6), E=span(U), D and its positive contraction C. Set

\[
u=\frac{v_{10}+z_{b,6}}2,\qquad
\delta=z_{b,6}-v_{10}.
\]

The new target is the action Cu on the common source u. Both u and delta lie in E. A single collective vector t_K represents the full action of u's finite polynomial, with all output and moment errors paid; u's entire analytic input tail is retained as a contraction error.

For a projection span F containing E, write r_x,F=(I-Pi_F)Cx. Then

\[
r_v=r_u-\frac12r_\delta,\qquad
r_z=r_u+\frac12r_\delta.
\]

This preserves the signed common/difference structure. Neither action is silently identified with the other.

## Full finite common source and output

The finite rational polynomial of u has even support 0..8190, averaging the exact finite centers defining v_10 and z_b,6. Its generator and SHA-256 are recorded. The historical g_hat, b and both collective polynomial hashes are independently reconstructed and checked through RC133. All common polynomial coefficients are positive.

The exact finite-source endpoint action is enclosed at every even output through degree 16382. Rational centers on the inherited 10^-40 grid define p_hat; the actual s/log2 uncertainty and output rounding are summed in D energy. The finite polynomial is not confused with the full analytic action.

Let Lambda=z_8190 and rho=Lambda/z_16384<1/4. Define analytic output features

\[
(\eta^{new}_k)_n=\frac{(2n+1)\Lambda^k}{(H_n+s)z_n^{k+1}}
\quad(n\ge16384,\ n\text{ even}).
\]

Positive moments nu_k=sum_m u_m(z_m/Lambda)^k give the exact infinite finite-source output sum_{k>=0} nu_k eta_new,k. The added collective vector is

\[
t_K=\hat p+\sum_{k=0}^K\hat\nu_k\eta^{new}_k.
\]

For a paid eta_new,0 energy upper T_new, finite rounding E_p and moment radii r_k, the entire finite-source action error obeys

\[
\epsilon_{fin}\le\sqrt{E_p}+\sqrt{T_{new}}\sum_{k=0}^K r_k\rho^k
+\sqrt{T_{new}}\frac{\nu_{K+1,upper}\rho^{K+1}}{1-\rho}.
\]

Zero-degree source mass is retained in nu_0. Exact rational geometric controls test the zero-degree contribution, maximal source degree, multiple output levels and retained orders.

## Common analytic input and paid full action

Above 8190, the input tails of v and z already share RC131's eta_k basis. Their exact positive moment centers are averaged before bounding the input tail. If a_k denotes those averaged moments, then

\[
\|Cu_{tail}\|_D^2\le\|u_{tail}\|_D^2
\le T_{old}\left(\sum_k a_k\rho_{old}^k\right)^2=:E_a.
\]

No analytic-source action is assigned zero. The full action error is

\[
\boxed{\|Cu-t_K\|_D\le\epsilon_{fin}+\sqrt{E_a}=:\epsilon.}
\]

The finite and analytic output images are not assumed orthogonal; their norm triangle cross term is included. The entire finite source through 8190 is used, improving the input-error floor relative to RC134's shorter source prefix.

## Difference residual, two-coordinate capture and independence

RC134 pays the full delta source energy d_delta. Positive contraction yields an additional factor of four for its projected action: delta/2 is a valid projection trial in every F containing E, so

\[
\|r_\delta,F\|_D^2\le d_\delta/4.
\]

For F_K=span(E,t_K), the common trial gives ||r_u,F_K||<=epsilon. Consequently

\[
\boxed{R_{vv,F_K},R_{zz,F_K}
\le\left(\epsilon+\frac14\sqrt{d_\delta}\right)^2.}
\]

Thus one added vector captures both old leakage coordinates, with the signed difference still paid. This does not claim exact closure, zero difference residual or a minimal response dimension.

RC134's positive old v residual lower is used *only* to prove the new trial independent of E:

\[
\operatorname{dist}_D(t_K,E)\ge
\sqrt{R_{vv,E,lower}}-\frac14\sqrt{d_\delta}-\epsilon>0.
\]

The exact six-dimensional old Gram certificate then implies dim(F_K)=7. The old lower is not retained as a covariance lower after enrichment.

## Full old-six covariance in the enlarged projection

Retain RC132's psi upper p, RC128's tiny f upper and the paid w-alpha*psi difference e_w^2. Choose generators

\[
q=(r_\psi,r_f,r_w-\alpha r_\psi,r_u,r_\delta)
\]

with squared norm uppers (p,d_f,e_w^2,epsilon^2,d_delta/4). The old six residuals have coefficients

\[
(0,0,0,0,0),\ (1,0,0,0,0),\ (0,1,0,0,0),\
(\alpha,0,1,0,0),\ (0,0,0,1,-1/2),\ (0,0,0,1,1/2).
\]

As in RC134, five-generator Cauchy-Schwarz supplies a full Loewner upper A[5 diag(d)]A*. It is valid for every complex old-six source mixture. Exact controls test that v-z cancels the common generator and (v+z)/2 cancels the difference generator. Sharper separate coordinate uppers are recorded alongside this conservative joint upper.

These are six *input* bounds with a seven-dimensional projection span. They are not the complete seven-input covariance, because Ct_K has not been certified. They cannot be transferred to an old six-dimensional compression or inserted into a seven-input Schur inverse without the missing joint data.

## Evidence boundary and next cursor

The added common response is independent of the old family and pays the full finite action, analytic input action floor, both old new-vector residuals and every old-six mixture. The new vector's own action, full seven-vector Gram and endpoint pairings, and complete seven-input covariance remain open.

RC136 cursor: certify the selected seven-vector joint family, preserving common/difference correlations and the analytic-source action error. Then refine the remaining analytic actions and the enlarged Schur enclosure. High finite-source representation accuracy does not itself give high full-action or inverse accuracy.

RC130's normalized P_0 response interval [0.931327855055,0.931339797136] remains unchanged. No original Weil action, original positivity, whole-aperture extension, F4, RH or Lean result is claimed.

## Reproduction

```bash
python scripts/validate_rpb108_rc135_common_response_capture.py \
 --output certificates/rpb108_rc135_common_response_capture.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json \
 certificates/rpb108_rc133_six_vector_joint_matrices.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay to reverse reconstruction, positive action and moment sums and compare the entire rational certificate. Historical files are unchanged; the RC135 validator, certificate and note are additive.
