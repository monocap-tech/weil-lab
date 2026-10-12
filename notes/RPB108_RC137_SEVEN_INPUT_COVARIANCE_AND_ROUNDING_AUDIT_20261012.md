# RPB108 — RC137: seven-input covariance and additive rounding audit

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC136, b2b0ed487da50cbf6e251d7f7b1356fb98619434.

## Result

The complete seven-input projected covariance now has a paid Loewner upper. This includes Ct_10 and every old analytic/new-vector mixture in the same seven-dimensional span; old-six covariance is not mislabeled as complete seven-input data.

The new t_10 row has genuine residual leakage:

\[
7.895606\times10^{-9}<R_{tt}<6.857201\times10^{-8},
\qquad
\boxed{R_{tt}/G_{tt}\ge0.000038248723.}
\]

Thus the seven-vector family cannot satisfy a relative t-coordinate small-variance target below 0.000038248723. This does not itself exclude an accurate P_0 inverse response or original Weil positivity; those have different acceptance criteria.

An additive rounding audit repairs a projection-pairing gap in RC134's lower-bound arithmetic. The reported decimal obstruction 0.000844756653 and RC135's displayed independence floor survive. The exact audited rational bounds in this certificate replace the historical unpadded lower for reuse; no historical file is edited.

The numerical complementary Schur lower test still fails with the current sufficient endpoint/covariance intervals. Independently, positive contraction implies an exact structural Schur lower by the Gram. Structural invertibility and a tight numerical inverse enclosure remain distinct.

## Family and retained Ct action

Retain RC136's exact seven-vector family U_7=(P_0,psi_0,f_0,w_14,v_10,z_b,6,t_10), E_7=span(U_7), and r_u=(I-Pi_E7)Cu. The full covariance is R_ij=<r_i,D r_j>.

RC135's t_10 polynomial and all seven finite coefficient prefixes are independently reconstructed, with the historical hashes and full finite Gram matched. The actual finite t input through even degree 4094 is acted on by the positive endpoint formula, enclosing all even outputs through 8190.

A rational trial y=sum_i Y_i U_i is chosen by finite-prefix least squares. The retained-output Gram is recomputed through 8190; RC136's larger 16382 prefix is not used as if it were the retained-output projection Gram. Its finite Loewner lower is positive.

The coefficient solve only chooses a trial. Acceptance uses an independently enclosed actual finite residual, including parameter uncertainty and output rounding, with D-energy summed upwards. Signed interval multiplication handles the trial coefficients.

## Entire omitted trial, output and input paid

The chosen trial has nonzero coefficients beyond the retained output cutoff. Its actual finite coefficients at even degrees 8192..16382 are combined across all source vectors before their squared norm is enclosed. Above 16382, every analytic component shares psi's leading eta_0 factor; the exact signed moment polynomial is likewise combined before absolute values are taken.

The resulting full Ct error bound is

\[
\|Ct-y\|_D\le\sqrt{E_{finite,res}}
+\sqrt{E_{trial,finite+analytic\ tail}}
+\sqrt{E_{retained\ source,output\ tail}}
+\sqrt{E_{omitted\ input}}.
\]

The input error includes *all* actual t coefficients beyond degree 4094, both finite and analytic. The output error includes the entire action tail after 8190. No images are assumed orthogonal; the full norm triangle cross term is paid.

Since y lies in E_7, this bounds the t residual. The accepted upper is intersected with G_tt,upper/4, valid for every source in E_7 under positive contraction by the trial t/2.

## Actual finite-distance lower

For the retained finite t input, let a be its output through 8190. Its actual second moment has lower Q_L, and every actual finite pairing q_i=<U_i,D a> is enclosed using the full action coefficient intervals. The projection upper uses the inverse of a positive Loewner Gram lower:

\[
\operatorname{dist}_D(a,U_7|_{\le8190})^2
\ge Q_L-\sup q^*G_{prefix,L}^{-1}q=:\ell.
\]

Signed rational interval products pay the pairing uncertainty in the supremum. The actual full Ct output can differ from a on the retained coordinates only through the omitted input action. Restricting output cannot increase distance to the full source span, hence

\[
\|r_t\|_D\ge\max(0,\sqrt\ell-\sqrt{E_{omitted\ input}}).
\]

A rational downward square-root allowance is included. The accepted positive lower is independent of the selected least-squares trial's quality.

## Additive RC134 audit

RC134 used rounded finite action centers to compute the projection pairings in its residual lower, while its second-moment lower used actual action enclosures. The center-to-action rounding uncertainty was not explicitly padded in those projection pairings. This was a precision-accounting gap in that lower-bound calculation; it does not affect its directly paid action-trial upper or RC135's covariance upper.

RC137 independently recomputes the RC134 finite Cv action using actual interval pairings throughout the projection upper. It accepts a repaired positive v lower and rechecks

\[
R_{vv,old}/G_{vv,old}\ge0.000844756653,
\]

and the downstream collective trial distance lower exceeding 7.170422e-7 in squared D norm. RC136's direct seven-vector positive Gram floor is independently retained. Thus the reported decimal conclusions and current seven-dimensional covariance span survive; exact historical rational lower endpoints are superseded for reuse by the audited RC137 fields.

No old lower is transferred across enrichment. RC135's old-six covariance in E_7 keeps zero lower diagonals where appropriate, and its proof of the added vector's independence has now also been revalidated with the repaired predecessor lower.

## Full seven-input covariance and signed mixtures

Let B_6 be RC135's paid correlated old-six Loewner upper in E_7, and d_t the new t-coordinate upper. For any complex old-six coefficient vector x and seventh coefficient c,

\[
\left\|\sum_{i<7}x_i r_i+c r_t\right\|_D^2
\le2x^*B_6x+2|c|^2d_t.
\]

Therefore

\[
\boxed{0\preceq R_E7(U_7)\preceq
2\operatorname{diag}(B_6,d_t).}
\]

This conservative joint upper retains the old common/difference correlations. Its zero cross block does not assert that the actual cross covariance vanishes: the factor-two norm inequality pays all such cross terms. Separate entry enclosures use residual Cauchy-Schwarz, include the positive t lower, and preserve the exact P_0 zero row. The inherited analytic psi/w bounds remain valid in the same E_7; a full independent Cpsi evaluation is not asserted.

## Complementary Schur boundary

The numerical lower G_L+H_L-R_U is tested as an exact rational PSD matrix and fails with these current sufficient enclosures. That failure must not be interpreted as a singular actual compression.

In D-orthonormal coordinates on E_7, write A=Pi C Pi and B=Pi C(I-Pi). Positive contraction gives C^2<=C, hence

\[
A^2+BB^*\preceq A.
\]

The complement's I+C operator has inverse at most I. Thus the actual Schur compression satisfies

\[
M=I+A-B(I+C_{comp})^{-1}B^*
\succeq I+A-BB^*\succeq I+A^2\succeq I.
\]

In source coordinates this gives M>=G+H G^-1 H>=G. It proves structural invertibility, while a tighter numerical bound is needed to improve the actual reference-response interval. No failed numerical test is relabeled as passed.

## RC138 cursor and standing

Covariance coverage is now complete for the seven-input family. The remaining task is quantitative inverse control: refine the common analytic response and t residual in a conditioned Schur or directly validated reference-response trial, preserving signed correlations and all tail errors. The genuine t lower rules out an arbitrarily small full-family variance target, but does not require enlargement if the inverse-response budget can tolerate that direction.

RC130's normalized P_0 response interval [0.931327855055,0.931339797136] remains unchanged. No original Weil source action, original positivity, whole-aperture extension, F4, RH or Lean result is claimed.

## Reproduction

```bash
python scripts/validate_rpb108_rc137_seven_input_covariance.py \
 --output certificates/rpb108_rc137_seven_input_covariance.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc135_common_response_capture.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json \
 certificates/rpb108_rc133_six_vector_joint_matrices.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay. Reverse reconstruction, Ct/Cv action, finite Gram, residual and pairing sums must reproduce the complete rational certificate, including the rounding audit and canonical action/residual hash. Only additive RC137 files are committed.
