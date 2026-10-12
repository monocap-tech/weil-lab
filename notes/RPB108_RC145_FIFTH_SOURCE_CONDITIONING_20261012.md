# RC145: fifth-source conditioning audit

The RC144 four-source reference response bound has uniform relative width 0.026434. RC145 adds the existing paid t10 direction as the fifth source, retaining the seven-dimensional carrier at aperture 11/10. This is an exact rational enclosure of the reference inverse response for all five-source mixtures. It is an accuracy audit, not a claim that the five-source matrix has reached a Stage I tolerance.

## Result

The trial solves the midpoint normal equations for all five sources, rounds the rational frame coefficients downward to 10^-20, and then uses the actual entrywise D Gram and endpoint intervals for acceptance. The common endpoint diagonal inherits RC141's positive lower and RC142's centered upper. Signed coefficients are combined before interval evaluation. Entry intervals are converted to Loewner bounds with explicit weights.

For the actual operator I+C, with 0 <= C <= I, the variational matrix L and residual R obey

\[L\preceq\Sigma\preceq L+R^*R.\]

The nominal residual uses the full actual D Gram upper. Four frame action errors are grouped with the four-generator Cauchy bound, while the t10 error has its own rank-one bound; two signed Young inequalities pay all their mixed correlations. Five rational parameter pairs are tested. The best tested choice is tau=gamma=1, with

\[0\preceq\Sigma-\Sigma_L,\qquad \Sigma\preceq\Sigma_U,\qquad
\Sigma_U-\Sigma_L\preceq 2.907751\,G_{source}.\]

The last inequality uses the certified lower source Gram and exact rational PSD. The variational lower matrix itself is not PSD. The structural bound (1/2)G_source <= Sigma <= G_source still supplies a strictly positive five-source lower because I <= I+C <= 2I. Neither this structural fallback nor the broad trial enclosure demonstrates a useful half-Gram matrix width for five sources.

## A concrete narrow direction

In the ordered basis (P0, f0, w14-alpha*psi0, (v10+z_b6)/2, t10), an exact rational witness, rounded from the fifth source's least-energy projection against the first four, is

\[x=(-0.000249199316,\;-0.006595175733,\;0.19564015612,\;-0.866307220693,\;1).\]

For this mixture the certificate checks, using the exact fractions behind these terminating decimals:

| Quantity | Certified bound |
| --- | ---: |
| Actual source energy x*Gx | [0.000000975019387903, 0.000000976467676605] |
| Variational interval contribution to trial width | >= 0.000002583641812019 |
| Paid residual contribution | >= 0.000000174508691938 |
| Total trial enclosure width | >= 0.000002758150503957 |
| Width / actual source energy | > 2.82462 |

The variational interval contributes roughly 93.7% of this trial width. Thus its half-Gram width gate fails on an explicit mixture even if the actual source energy is replaced by its certified upper bound. This tests the present enclosure, not an intrinsic lower bound on the true response or on any future sharper certificate. A refinement should tighten the t10 endpoint and Gram correlations in this near-dependent direction rather than optimizing the residual charge alone.

## Boundary and reproduction

The four-source RC144 result remains the accepted narrow matrix certificate. The five-source addition is a valid but loose reference enclosure with a precise obstruction to the tested accuracy gate. No original Weil or augmented action, whole-aperture positivity, F4, RH, or Lean result follows. The required Stage I matrix tolerance is still unspecified here.

```bash
python scripts/validate_rpb108_rc145_fifth_source_conditioning.py \
 --output certificates/rpb108_rc145_fifth_source_conditioning.json \
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

The same command with `--replay` reverses signed accumulation and candidate order, rebuilds RC144, and checks the complete generated certificate. Earlier checkpoint files are untouched.
