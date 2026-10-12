# RPB108 — RC144: tuned mixed errors improve the joint response

Date: 2026-10-12 UTC. Aperture a=11/10. Branch `research/rpb108-route-consolidation`. Parent RC143, `ffc8edbb172a97d1eb5d7a5fe7397ff73163910d`.

The four-source full-carrier reference inverse matrix has a new enclosure

\[
0<\Sigma_L\preceq\Sigma_S\preceq\Sigma_U,
\qquad\Sigma_U-\Sigma_L\preceq0.026434\,G_S.
\]

This reduces RC143's uniform relative width from 0.042648 to 0.026434, at least a 1.613376-fold tightening. It covers every signed mixture in the same source family S=(P_0,f_0,w_14-alpha*psi_0,(v_10+z_b,6)/2), inside the existing seven-vector carrier. RC142's sharper scalar P_0 interval remains separately available.

## Accepted construction

RC143's rational trial map is retained. The variational identity remains Sigma_S=L+R^*(I+C)^-1 R. Before evaluating uncertain Gram entries, RC144 combines the full signed coefficient of S^*Y+Y^*S-Y^*Y for each actual Gram entry. This preserves cancellations between the three terms. The endpoint contribution uses RC141 and RC142's common-source energy bounds.

Two rational coordinate choices are tested: the original source basis and a unit upper triangular Gram-Schmidt transform chosen from the certified source Gram lower. All transformed source, trial, residual and action-error coefficients are computed before interval acceptance. The coordinate choice is only a choice of enclosure; the final matrices are transported back to the original sources by an exact inverse congruence.

## Mixed errors and selected parameters

Write the actual action-trial error as E=E_major+E_minor, where the major term is the common-source action error multiplied by the fourth trial coefficient row. The other three source errors form the minor term. Their correlations are paid by the three-generator norm bound. For any positive rational tau,

\[
E^*E\preceq(1+\tau)M_{major}+(1+1/\tau)M_{minor}.
\]

For R=R_nom+E and any positive rational gamma,

\[
R^*R\preceq(1+\gamma)R_{nom}^*R_{nom}
+(1+1/\gamma)E^*E.
\]

Every nominal norm uses the full actual Gram upper. The major bound is a rank-one matrix with its full mixed entries. The minor bound is a congruence of three diagonal generator norm budgets. Neither inequality assumes that error columns are orthogonal. Six exact scalar signed controls check Young's inequality for aligned and opposing errors.

Ten candidates are checked: five parameter pairs for each coordinate choice. The winner retains the original coordinates with tau=1/100 and gamma=1/20. Its width is 0.026434; the same parameters in the tested orthogonalized coordinates give 0.026452. Thus this particular coordinate transform does not improve acceptance. The large gain comes from replacing RC143's fixed factor-two residual charge and four-generator action charge with the tested unequal weights, together with signed Gram cancellation.

The final width is accepted by exact rational PSD comparison against the actual source Gram's certified lower. The adjacent lower grid point on a 10^-6 grid fails that sufficient gate. A strictly positive diagonal floor is also certified below Sigma_L. The certificate contains both original-source response matrices, candidate widths, selected parameters and the exact sign controls.

## Evidence boundary

This is an improved joint reference matrix enclosure on the same four-source family. The required Stage I response tolerance has not been specified in this certificate, and complete native-source coverage and original Weil transport remain open. Whole-aperture positivity, F4, RH and Lean are not advanced by this result. The next step should attribute the remaining width to variational energy uncertainty versus actual residual leakage and compare those components with the concrete Stage I budget.

## Reproduction

```bash
python scripts/validate_rpb108_rc144_conditioned_joint_response.py \
 --output certificates/rpb108_rc144_conditioned_joint_response.json \
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

Repeat with `--replay` to reverse signed sums, coordinate choices and candidate traversal, rebuild RC143, and compare the complete rational certificate. Historical files remain unchanged.
