# RC195: reconstruct the five-source inverse with RC192–194

Starting head:1271113c5c7b9e7617f8c20e7a272b7f9496dda0 (RC194). The aperture11/10, supported canonical M=D^-1 L, D-energy norm, and five response sources P0,P2,f0,psi0,w14 remain unchanged.

| Same-family inverse measurement | RC191 | RC195 |
|---|---:|---:|
| Certified inverse enclosure width relative to G_lower | 1.254303 | 0.571911 |
| Width/half-Gram threshold ratio | 2.508606 | 1.143822 |
| Threshold minus width, relative to G_lower | -0.754303 | -0.071911 |
| Half-Gram acceptance | Failed | Failed |

This is a narrower actual inverse enclosure, not merely a smaller nominal residual. Both selected endpoints are newly reconstructed for the enriched trial. The baseline still selects the inherited RC191 enclosure. The exact PSD test fails for the selected enriched enclosure. The historical RC184 rational source probe (-1/120,3/50,-14/25,-26/25,1) has negative quadratic value in its gate matrix, approximately-1.445439805862202e-5. This witnesses failure of this enclosure, not impossibility of the true inverse meeting the tolerance.

## Full action attachment

All finite mixed rows are rebuilt through degree65534. The low polynomial regular coefficients are replaced by RC192, f0's regular coefficients by RC193, and the q185 action gains RC194's signed analytic endpoint tail at every even degree>=4096. RC188's complete psi0 carrier and RC190's endpoint/regular w14 carriers remain attached. The unchanged source Gram is checked against RC191 exactly.

The raw trial order is P0,P2,f0,psi0,w14,q185. Its complete absolute action-error bounds are approximately9.67707e-9,9.67723e-9,9.04844e-6,6.85965e-6,1.69508e-5,1.05331e-9. The new trial selection, normalization, full mixed Grams, action-error transformations, finite residuals and variational response are rebuilt. No old mixed matrix is reused with a substituted error bound.

## Signed tail and residual accounting

At every finite output n>=4096, the q185 action coefficient is its signed moment polynomial times eta_n, with D_n interval uncertainty paid in the mixed calculation. Beyond65534, an absolute moment envelope bounds the whole represented q185 action tail. Mixed source/q185-action pairings are enclosed on both sides. Action Gram off-diagonal pairings involving q185 are also enclosed on both sides; diagonal omitted energies remain nonnegative.

For the residual, the common leading eta factor retains the signed zeroth moment term -mu_q0 Y_q. The nonconstant q185 moments contribute a fifth remainder envelope. The full residual-tail Gram uses3T/2 for the shared leading outer product and15T for the sum of five squared remainder outer products. This follows from (a+b)^2<=3a^2/2+3b^2 and |sum_{i=1}^5 b_i|^2<=5 sum_i |b_i|^2, and applies to complex source mixtures. Input and action errors are separately paid by the existing correlated variational proof.

## Enclosure and acceptance

The RC191 variational solver is reused through explicit, checked source refinements; historical files remain unchanged. For each baseline/enriched trial, exact rational PSD checks search the action/tail Young parameters and actual-residual bounds, retaining inherited and structural inverse endpoints as alternatives. The certified width is the exact PSD majorization of the selected enclosure gap by beta G_lower.

The enriched nominal residual squared-error factor is0.029934, and its variational response width is0.281851. Its selected action Young parameter is1/300, tail parameter1/3 and residual upper parameter1/3. The remaining inverse gap is0.071911 above the half-Gram threshold. The full result, exact matrix endpoints and parameter selections are stored in the certificate. A smaller width on this unchanged family records certified precision progress while acceptance remains open.

## Verification and continuation

All new and inherited certificates are bound by SHA-256. RC191 ancestry and direct RC192/RC193/RC194 attachments are checked. Replay reverses finite summation, trial order and parameter search order, and requires equality of the complete generated certificate.

```
python scripts/validate_rpb108_rc195_refined_five_source_inverse.py --output certificates/rpb108_rc195_refined_five_source_inverse.json
python scripts/validate_rpb108_rc195_refined_five_source_inverse.py --replay --output certificates/rpb108_rc195_refined_five_source_inverse.json
```

Five-source inverse acceptance and original Stage I remain open. Native v10,z_b6,t10 coverage, original augmented Weil floor/auxiliary response, original positivity, RH,F4 and Lean closure remain open/unclaimed. Accepted smaller-family results are unchanged.

Next: tighten the remaining f0/psi0/w14 action and correlated variational payments or enrich the controlled residual. Reevaluate this same five-source gate before moving to native v10,z_b6,t10 coverage. The gap0.071911 is a bound deficit, not an error floor or a completion percentage.
