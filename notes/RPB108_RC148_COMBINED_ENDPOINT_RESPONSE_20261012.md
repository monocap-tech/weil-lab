# RC148: the combined narrow endpoint clears a scalar width target

At aperture 11/10, RC147 identified the independent t10 and common/t10 endpoint intervals as the dominant charges for one nearly dependent five-source mixture. RC148 evaluates the endpoint action on the *combined trial vector* itself. It retains the seven-vector carrier and the exact RC145 rational witness. No new vector or unproved correlation is introduced.

Let s be the narrow source, h its five rational frame coefficients, q=S h its seven-vector trial, and t=T h the approximation to Cq from the five paid action columns. Then

\[\langle Cq,q\rangle=\langle t,q\rangle+\langle Cq-t,q\rangle.\]

The action error is charged by the sum of the five coefficient-weighted D norm bounds, multiplied by the certified norm of q. The signed actual D Gram interval bounds the first pairing. Intersecting with the inherited endpoint entry intervals and 0 <= C <= I gives

\[8.0684338919\times10^{-9}\;\leq\langle Cq,q\rangle
\;\leq 3.3119720199\times10^{-7}.\]

Its width is about 3.2313e-7, compared with RC147's 1.7646e-6 endpoint entry-width charge for the same trial. This is an actual combined-vector bound, not a hypothetical reduction of an endpoint input.

The nominal residual and five action errors are also combined directly: the full squared residual is at most 8.9094780e-8, down from RC146's matrix-wide 1.7450870e-7 charge on that diagonal. The scalar variational identity, its nonendpoint signed Gram interval, and the structural inequality I <= I+C <= 2I then certify

\[5.7460083820\times10^{-7}\;\leq\langle s,(I+C)^{-1}s\rangle
\;\leq9.7646767661\times10^{-7}.\]

The interval width is about 4.0186684e-7 and is **less than 0.412163 times the certified lower source energy**. The half-Gram *scalar* width target is met for this narrow mixture. The original five-source *matrix* width certificate remains RC146's 2.051566; this scalar calculation has not supplied its mixed response rows. RC144's sharper four-source matrix remains valid.

## Reproduction

```bash
python scripts/validate_rpb108_rc148_combined_endpoint_response.py \
 --output certificates/rpb108_rc148_combined_endpoint_response.json \
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

Repeat with `--replay` to reverse signed accumulation, rebuild RC147 and all dependencies, and compare the generated certificate exactly. This is a reference-operator scalar response result. The required Stage I matrix tolerance, original Weil and augmented actions, whole-aperture positivity, F4, RH, and Lean remain open.
