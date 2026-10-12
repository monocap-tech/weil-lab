# RC149: a positive five-source joint reference response matrix

At aperture 11/10, the seven-vector carrier now supports an exact rational **five-source reference inverse response matrix** with a strictly positive lower and a uniform width below half the actual source Gram. The sources are P0, f0, w14-alpha*psi0, (v10+z_b6)/2, and t10. RC149 extends RC148's combined-vector endpoint identity to all mixed trial rows in RC146's rational narrow-coordinate basis.

## Certified matrix

For the reference operator I+C, with 0 <= C <= I, let Sigma be its inverse response on these five sources and G_S their actual D Gram. The certificate gives explicit rational matrices Sigma_L and Sigma_U, transported back to the original source basis, such that

\[0\prec\Sigma_L\preceq\Sigma\preceq\Sigma_U,
\qquad\Sigma_U-\Sigma_L\preceq0.449042\,G_S.\]

This is a matrix statement for **every signed five-source mixture**. The previous RC146 five-source trial width was 2.051566 and its trial lower was indefinite. RC149 passes both an exact rational PSD width gate against the certified source Gram lower and a strictly positive diagonal floor beneath its transformed variational lower. An inverse congruence verifies the width gate and positive lower in the original source basis.

## How the mixed rows are paid

Write each trial q_i as a rational combination of the five existing frame vectors. Its approximate action t_i is the matching combination of the five paid action columns. The action error norm is bounded by the sum of absolute frame coefficients times their individual certified errors. For each endpoint entry, RC149 intersects:

1. The signed inherited frame endpoint interval for <Cq_i,q_j>.
2. The action identity <t_i,q_j>, enlarged by the action error for i times the certified norm of q_j.
3. The reverse action identity <q_i,t_j>, enlarged by the action error for j times the certified norm of q_i.

These are bounds on the same symmetric entry, so intersection is valid; no independence or zero mixed error is assumed. The nonendpoint variational terms combine signed coefficients before D Gram interval evaluation. Entry intervals become Loewner bounds using explicit weights. The full nominal residual uses the actual D Gram upper. A four-generator minor action-error bound and a rank-one t10 major bound are joined with two signed Young inequalities. Seven rational parameter pairs are tested; tau=1/4 and gamma=2 give the smallest certified width, 0.449042. Replay checks reversed signed accumulation and candidate order.

## Boundary

This closes the tested **half-Gram reference matrix width gate** on the five paid sources. It does not establish that 0.449042 is the required Stage I tolerance; that tolerance is not specified by this certificate. Coverage of any additional required native sources and transport to the original Weil or augmented action remain open. There is no whole-aperture positivity, F4, RH, or Lean claim.

## Reproduction

```bash
python scripts/validate_rpb108_rc149_combined_five_matrix.py \
 --output certificates/rpb108_rc149_combined_five_matrix.json \
 certificates/rpb108_rc148_combined_endpoint_response.json \
 certificates/rpb108_rc147_endpoint_budget.json \
 certificates/rpb108_rc146_narrow_coordinate.json \
 certificates/rpb108_rc145_fifth_source_conditioning.json \
 certificates/rpb108_rc144_conditioned_joint_response.json \
 certificates/rpb108_rc143_joint_variational_matrix.json \
 certificates/rpb108_rc142_centered_common_tail.json \
 certificates/rpb108_rc141_positive_common_tail.json \
 certificates/rpb108_rc140_residual_endpoint_probe.json \
 certificates/rpb108_rc139_two_sided_variational_response.json \
 certificates/rpb108_rc138_reference_variational_response.json \
 certificates/rpb108_rc137_seven_input_covariance.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc135_common_response_capture.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc130_remaining_covariance.json
```

Repeat with `--replay` to rebuild RC148 and the preceding chain, reverse signed loops and parameter traversal, and compare the complete rational output. Historical files remain unchanged.
