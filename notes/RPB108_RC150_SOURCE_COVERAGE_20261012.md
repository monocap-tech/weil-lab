# RC150: exact source coverage after the five-source matrix

RC149 certifies a positive reference inverse response matrix of width at most 0.449042 times the actual source Gram for five paid directions at aperture 11/10. RC150 audits which parts of the seven-vector native carrier that statement reaches. The result is a precise two-direction remainder, not another response estimate.

The carrier order is (P0, psi0, f0, w14, v10, z_b6, t10). The paid response frame is (P0, f0, w14-alpha*psi0, (v10+z_b6)/2, t10). Add psi0 and delta=z_b6-v10. The resulting 7-by-7 rational matrix has an exact inverse, checked in both source coordinates and the original carrier coordinates. Thus the five paid directions have rank five and the two added directions complete the carrier.

The actual D Gram's certified Loewner lower remains positive in this augmented frame. Its Schur complement after eliminating the paid five is positive definite. For orientation, its two-by-two entries are approximately

| | psi0 residual | delta residual |
| --- | ---: | ---: |
| psi0 residual | 9.412431e-8 | -4.545070e-8 |
| delta residual | -4.545070e-8 | 2.327147e-8 |

The validator verifies an exact rational positive diagonal floor below this Schur complement. These are conditional *D Gram* energies; they do not provide the missing inverse response entries. The five-source response certificate cannot be promoted to a seven-source response certificate by a basis relabeling.

The next route is now explicit: pay the psi0 and delta response columns and their mixed rows, or establish a native-source reduction that truly eliminates them. The repository's RC notes do not specify a numerical Stage I matrix tolerance, and original Weil and augmented action transport remains separate. RC149's half-Gram gate therefore remains a reference calculation on the five named sources, with no whole-aperture positivity, F4, RH, or Lean closure.

## Reproduction

```bash
python scripts/validate_rpb108_rc150_source_coverage.py \
 --output certificates/rpb108_rc150_source_coverage.json \
 certificates/rpb108_rc149_combined_five_matrix.json \
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

`--replay` rebuilds the predecessor chain and checks the complete generated certificate. Historical files are untouched.
