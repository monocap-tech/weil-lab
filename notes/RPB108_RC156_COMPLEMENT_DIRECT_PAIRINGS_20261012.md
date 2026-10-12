# RC156: direct complementary Gram and mixed endpoint pairings

Resume from RC155 (`19b254d48e558d0288d786fe02d0334759490931`) on `research/rpb108-route-consolidation`, aperture 11/10. Additive definitions appear in `docs/TERMINOLOGY_RPB108_RC156_DIRECT_PAIRINGS.md`.

RC155 paid the seven-source action-error map, but its trial-source intervals were transported from inherited endpoint data. RC156 evaluates the previously uncovered two-source block directly. Sources are ordered (psi0,delta), delta=z_b6-v10; trials are RC154's q_psi and RC153's q_delta.

Both action trials are reconstructed with their full predecessor arithmetic. Their committed finite coefficient/radius hashes and full D-norm error bounds are checked. The direct pairing prefix extends through even degree 16382, including the q_psi midpoint input-tail coefficients at degrees 8192 through 16382. Delta's analytic source continuation after degree 8190 retains the combined signed moment polynomial. After degree 16382, the source and trial tails share eta_n and have prescribed rational polynomial factors. Their signed products pay the entire infinite pairing tails.

All four entries of Q_ij=<q_i,s_j>_D and all three independent entries of the symmetric two-trial Gram are enclosed. Q is not symmetrized: for orientation, Q_psi,delta is approximately -2.873e-8, while Q_delta,psi is approximately -2.823e-8. Their difference is compatible with their paid action errors. Symmetry applies to the true endpoint pairing H_ij=<Cs_i,s_j>, so both directed action identities are intersected with inherited H intervals.

The resulting endpoint widths are:

| Endpoint entry | RC155 inherited width | RC156 direct paid width | Improvement |
| --- | ---: | ---: | ---: |
| psi0, psi0 | 2.638262e-8 | 1.111704e-8 | 2.37317x |
| psi0, delta | 4.481032e-6 | 5.661455e-9 | 791.49820x |
| delta, delta | 1.333094e-5 | 4.195871e-9 | 3177.15551x |

Widths are differences of certified rational interval endpoints; the displayed numbers are rounded for reading. This is an improvement in the enclosure, not a lower bound on true error.

The two-trial Gram entries lie in approximately

\[R_{\psi\psi}\in[3.63316968618,3.64673899905]\times10^{-8},\quad R_{\psi\delta}=-1.79212428714\times10^{-8},\quad R_{\delta\delta}=9.42036542335\times10^{-9}.\]

The certificate retains intervals for all entries, including tiny directed arithmetic uncertainty in the entries displayed as single values. The only infinite trial-Gram tail is q_psi's diagonal, since q_delta is a finite polynomial.

The remaining direct-pairing obligation is now the five-by-two block between the paid five-source frame and these two new trials/sources. RC156 does not assemble a seven-source inverse-response enclosure or infer an inverse-width gate from the action gate. Stage I tolerance, original Weil/augmented transport, whole-aperture positivity, F4, RH, and Lean closure remain open.

Next: evaluate that five-by-two block with the same signed analytic-tail accounting, then assemble the seven-source variational inverse matrix using the paid complementary trial Gram and endpoint block.

## Reproduction

```bash
python scripts/validate_rpb108_rc156_complement_direct_pairings.py \
 --output certificates/rpb108_rc156_complement_direct_pairings.json \
 certificates/rpb108_rc154_centered_analytic_tail_action.json \
 certificates/rpb108_rc153_correlated_difference_action.json \
 certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc151_complement_schur.json
```

RC153's reconstruction also reads the sibling RC152 action-budget certificate, whose hash is verified and recorded. Add `--replay` to reverse inner source and pairing sums and check exact certificate equality. Historical checkpoint files are unchanged.
