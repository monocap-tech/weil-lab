# RPB108 — RC143: four-source joint reference inverse matrix

Date: 2026-10-12 UTC. Aperture a=11/10. Branch `research/rpb108-route-consolidation`. Parent RC142, `d6c1dda4b8c9950768f2d0c4424d99701d103b98`.

## Result and definitions

The full-carrier reference inverse is now enclosed jointly on the source family

\[
S=(P_0,f_0,w_{14}-\alpha\psi_0,(v_{10}+z_{b,6})/2).
\]

This is a four-source family inside the existing seven-dimensional carrier, not an added carrier vector or a new native Weil family. Define the actual response and source Gram matrices by

\[
\Sigma_S=S^*(I+C)^{-1}S,\qquad G_S=S^*S,
\]

where stars and products use the D inner product. The certificate provides rational matrices `Sigma_L,Sigma_U` such that

\[
0<\Sigma_L\preceq\Sigma_S\preceq\Sigma_U,
\qquad
0\preceq\Sigma_U-\Sigma_L\preceq0.042648\,G_S.
\]

The strict positive lower matrix is checked by exact rational LDL arithmetic. The width bound covers every signed mixture of all four sources, including mixed response entries. It is proved against a certified lower bound for the actual source Gram, rather than by comparing four independent diagonal widths. The smallest accepted upper grid value on a 10^-6 grid is recorded; the adjacent lower value fails the same sufficient PSD gate. This does not assert optimality among other matrix enclosures.

| Source | Certified response / own D-energy lower | Upper |
|---|---:|---:|
| P_0 | 0.931328619460 | 0.931330403787 |
| f_0 | 0.822727152693 | 0.822757498279 |
| w_14-alpha*psi_0 | 0.723795080683 | 0.723944804640 |
| (v_10+z_b,6)/2 | 0.694405536065 | 0.695011540551 |

These diagonals belong to the joint Loewner enclosure and are rounded outward. RC142's separately certified sharper P_0 interval [0.931329492307642,0.931329517490064] remains available. Entrywise intersection with that scalar interval is not asserted to preserve this matrix's Loewner bounds.

## Joint variational identity

Let A=I+C and choose a four-column trial map Y for the four source columns. With R=AY-S, set

\[
L=S^*Y+Y^*S-Y^*AY.
\]

Expanding the full-carrier products gives the exact matrix identity

\[
\Sigma_S=L+R^*A^{-1}R.
\]

Because I<=A<=2I, the residual correction is positive and bounded above by R^*R. No complementary block or mixed correction is dropped. Three exact scalar spectral models at C=0,1/2,1 use two signed sources and nonzero mixed residuals to check the matrix identity and both residual inequalities.

## Paid acceptance

The source/action frame uses the first four RC138 combinations and their fully paid action errors. The nominal action matrix K=S+T selects a rational trial coefficient matrix D by least residual fitting with a center Gram; each coefficient is rounded to a 10^-20 rational grid. Set Y=SD and R_nom=KD-S. The center solve only chooses trials. All acceptance uses actual Gram and endpoint enclosures.

The variational matrix entries enclose both mixed source-trial pairings, the trial Gram and the signed endpoint energy. RC141 and RC142's tighter lower and upper H(u,u) entries are included. Weighted interval radii then give valid Loewner bounds L_L,L_U.

If E_0 denotes the four full action error columns and epsilon_j their paid norms, Cauchy gives

\[
E_0^*E_0\preceq4\operatorname{diag}(\epsilon_j^2).
\]

Thus E=E_0 D has a full mixed Gram upper, and

\[
R^*R\preceq
2R_{nom}^*R_{nom}+2E^*E
\preceq R_U.
\]

The nominal Gram uses the full seven-vector Gram upper, and the action-error Gram uses a congruence of the four-generator diagonal bound. The generators may be correlated; zero cross terms in the diagonal majorant are not a claim that actual errors are orthogonal. The accepted matrices are Sigma_L=L_L and Sigma_U=L_U+R_U. Their PSD gap and its relative source-Gram width are checked exactly.

## Remaining obligation

RC143 supplies an actual matrix response enclosure for this four-source family, with a uniform width of 4.2648% of source D-energy. It does not specify or meet an asserted Stage I target tolerance, extend the response matrix to every required native source, or certify original Weil source transport. The next pass should compare this achieved width with an explicit response budget, then refine the conditioning or endpoint/action data that dominate that budget. Whole-aperture positivity, F4, RH and Lean remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc143_joint_variational_matrix.py \
 --output certificates/rpb108_rc143_joint_variational_matrix.json \
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

Repeat with `--replay` to reverse the signed seven-vector and four-frame sums and compare the complete rational certificate. Historical files remain unchanged.
