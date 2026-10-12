# RC146: signed intervals in the fifth-source narrow coordinate

At aperture 11/10, RC145 found a nearly dependent t10 mixture in the existing five-source, seven-carrier reference calculation. RC146 uses that exact rational mixture as the fifth basis vector **before** evaluating the uncertain endpoint and D Gram entries. This is a source-coordinate change, with an invertible upper triangular rational matrix; all five-source mixtures remain covered.

## Certified improvement

The transformed source, trial, frame coefficients, and nominal residual are computed first. For every transformed variational matrix entry, the signed coefficient of each uncertain Gram entry is aggregated across S*Y+Y*S-Y*Y, followed by the signed endpoint contribution -D*H D. Entry intervals are then converted to Loewner bounds. The five action-error generators and their mixed correlations are charged as in RC145, without an orthogonality assumption.

Five rational Young-parameter pairs were evaluated. The selected tau=gamma=1 yields the exact rational PSD gate

\[\Sigma_U-\Sigma_L\preceq 2.051566\,G_{source}.\]

The certified original-source matrices are obtained by inverse congruence, and the same width gate is checked again against the original certified source Gram lower. RC145's 2.907751 width is reduced by at least a factor of 1.417332. This is an improvement in the paid five-source trial, not a change to the operator or carrier.

For the new fifth coordinate (the exact RC145 witness), the source energy remains between 0.000000975019387903 and 0.000000976467676605. Its new variational interval width is at most 0.000001820211032893, and the residual charge at most 0.000000174508691939. The total width exceeds 0.000001994719724830 and is greater than 2.042791 times even the upper source-energy bound. The half-Gram gate therefore still fails for this enclosure.

The transformed trial lower matrix is indefinite. The separate structural inequality (1/2)G_source <= Sigma <= G_source continues to provide a positive reference lower. No prescribed Stage I accuracy budget is claimed, and the sharper RC144 four-source matrix remains intact.

## Boundary and replay

This is a rational reference-operator matrix enclosure. It does not certify the original Weil or augmented action, whole-aperture positivity, F4, RH, or Lean. Further work must constrain the t10 endpoint and Gram correlations in the narrow mixture to reduce its variational interval.

```bash
python scripts/validate_rpb108_rc146_narrow_coordinate.py \
 --output certificates/rpb108_rc146_narrow_coordinate.json \
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

Repeat with `--replay` to reverse the signed summations and candidate traversal, rebuild RC145 and its ancestors, and check the generated certificate for exact equality. Historical files remain unchanged.
