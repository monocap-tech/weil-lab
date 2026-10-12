# RC151: structural conditional response on the two uncovered sources

RC150 completed the seven-vector carrier by adding psi0 and delta=z_b6-v10 to RC149's five paid response sources. RC151 determines what the existing operator inequalities alone say about these two directions after minimizing over the paid five. This is an exact rational conditional-response enclosure, not an evaluation of their missing action columns.

For a positive block matrix M on the five paid directions and two complementary directions, its Schur complement is the least M-energy among paid-coordinate adjustments to each complementary vector. This variational description makes Schur complementation monotone. Applying

\[(1/2)G\preceq\Sigma=(I+C)^{-1}\preceq G\]

and the certified actual D Gram bounds yields

\[(1/2)\operatorname{Schur}(G_{Lo})
\preceq\operatorname{Schur}(\Sigma)
\preceq\operatorname{Schur}(G_{Hi}).\]

The lower is strictly positive. The upper-minus-lower has certified relative width at most **2.514658** against the conditional source Gram lower. A rational mixture (0.482879509139 psi0 + delta) has conditional source energy between about 1.3243e-9 and 3.9871e-9, while the width of this structural enclosure exceeds 3.3249e-9. Its width is more than 0.833929 times even the source-energy upper, so this enclosure fails the half-Gram target on a concrete mixture. This does not imply a lower bound on uncertainty in the true response; direct paid action data can sharpen it, as RC148–149 did for t10.

The certificate also checks two positive two-by-two response matrices with the same diagonal blocks and opposite mixed entries. They obey the same structural interval, yet their mixed rows differ. This finite control illustrates the interface: completing only the complement diagonals would still leave the mixed response rows unresolved.

The next pass must evaluate psi0 and delta actions, or certify a native-source reduction that removes them, including their mixed response rows. The Stage I numerical response tolerance and original Weil action transport are not supplied by this structural calculation. No whole-aperture positivity, F4, RH, or Lean closure follows.

## Reproduction

```bash
python scripts/validate_rpb108_rc151_complement_schur.py \
 --output certificates/rpb108_rc151_complement_schur.json \
 certificates/rpb108_rc150_source_coverage.json \
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

`--replay` checks exact equality after rebuilding all predecessors. Earlier checkpoint files are unchanged.
