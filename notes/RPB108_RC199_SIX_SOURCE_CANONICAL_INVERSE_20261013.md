# RC199: certify the expanded six-source inverse and test acceptance

Starting head:af1ecbf6e1743eb378771c777857ae74c699c602 (RC198). Aperture11/10, supported canonical M=D^-1 L and D-energy norm remain unchanged. Response coverage expands to P0,P2,f0,psi0,w14,v10, with seven raw trial directions including q185.

| Six-source acceptance measurement | RC199 |
|---|---:|
| Selected certified inverse width relative to source G_lower | 4.039743 |
| Half-Gram threshold | 0.5 |
| Width/threshold ratio | 8.079486 |
| Threshold minus width | -3.539743 |
| Exact half-Gram acceptance | Failed |

Both Galerkin and least-residual candidates give valid actual inverse enclosures. The selected least-residual enclosure uses newly evaluated refined lower and upper endpoints. Its width4.039743 is tighter than the Galerkin candidate's6.693364. The latter selects structural endpoints. An exact coordinate witness (1,0,0,0,0,0), corresponding to P0, has negative quadratic value in the selected gate matrix (approximately-2.801553449153311).

This is an expanded-family enclosure, not a same-family comparison with RC196's accepted five-source width0.307029. The old five-source result remains intact. A witness against the new enclosure does not refute that accepted result or prove that the true six-source inverse cannot meet the tolerance.

## Actual variational construction

All seven source/action carriers are reconstructed through65534 using RC198's complete source definitions and RC192–197 action refinements. The seven-by-six Galerkin and least-residual maps are chosen from rational midpoint matrices and rounded to1e-30. Midpoints select trials; every acceptance endpoint is obtained from directed interval and full-tail data.

For each trial, the finite nominal residual Gram and the trial/residual cross entries are evaluated directly from every retained coefficient. The full residual keeps the shared leading eta cancellation. Its seven remainder terms cover P2, the native w14 source/f0-action difference, psi0 action, w14 action, signed q185 action, v10 source and v10 action. The full residual-tail upper uses3T/2 for the leading outer product and21T for the remainder outer-product sum. The trial-source tail keeps its shared leading source moment and pays the two nonconstant native w14/v10 source terms separately.

Response-adapted positive triangle weights pay all seven individual actual action errors. The exact Cauchy Gram inequality is verified before transporting it through the trial map. The selected nominal residual squared-error envelope is0.323779 G_lower and the selected adaptive action-error squared envelope is0.040835 G_lower. These are separate squared-error measurements, not norm-error percentages.

The variational identity C=Sym(S*D U)+Sym(U*D R_actual) is enclosed using correlated source/trial Gram bounds, direct finite cross entries, omitted-tail Young payments and full actual action-error payments. The actual inverse response is C+R_actual*D M^-1 R_actual; the structural aI<=M<=2I bounds give the residual enclosure. Exact PSD checks select valid lower and upper alternatives and certify the final gap<=beta G_lower. The selected variational width is1.449072, action Young parameter1/30, tail parameter1 and actual residual upper parameter1/3. The selected residual lower parameter iszero.

## Bound diagnostic and next target

On the selected trial, the terms epsilon_k/t_k in the adapted triangle factor have approximate shares: v10 85.22%, psi0 9.66%, w14 4.27%, f0 0.85%; the remaining terms are small. This is accounting for a certified upper bound, not a decomposition of the actual error or the inverse width. The exact individual errors and rational weights are stored or SHA-256 bound by the certificate.

The dominant v10 action payment suggests tightening its centered endpoint input-tail approximation first. The nominal residual is also material, so action accuracy alone is not promised to close acceptance. A further residual-enrichment direction or sharper variational enclosure may still be needed.

## Verification and scope

RC198 and its entire input ancestry are SHA-256 bound. The source Gram and represented action-Gram entry data are reproduced before trial/residual evaluation. Exact replay reverses coefficient summation and trial/parameter search order and must reproduce the entire certificate.

```
python scripts/validate_rpb108_rc199_six_source_canonical_inverse.py --output certificates/rpb108_rc199_six_source_canonical_inverse.json
python scripts/validate_rpb108_rc199_six_source_canonical_inverse.py --replay --output certificates/rpb108_rc199_six_source_canonical_inverse.json
```

The actual six-source canonical inverse is now enclosed, but its half-Gram gate remains open. RC196's accepted five-source contract is unchanged. Native z_b6/t10 complete action coverage, original Stage I source-range and signed augmented acceptance obligations, original Weil positivity, RH,F4 and Lean closure remain open/unclaimed.

Next: refine v10's dominant endpoint/input-tail action payment and then reevaluate this six-source family; use a paid residual enrichment if the nominal residual remains the limiting term.
