# RC203: paid q202 enrichment of the six-source inverse

Starting head:7fc63d0356e3bd218d2dcd4cf0f9e3527a822e6f (RC202). Definitions are in docs/TERMINOLOGY_RPB108_RC203_RESIDUAL_ENRICHED_SIX_SOURCE_INVERSE.md. Aperture11/10, actual supported canonical M=D^-1 L and D-energy norm remain fixed.

The raw trial basis is P0,P2,f0,psi0,w14,q185,v10,q202. Response order remains P0,P2,f0,psi0,w14,v10. Both response source-Gram endpoints are reproduced exactly against RC201. The eight-trial source-Gram lower is positive definite by exact rational elimination. q202 is auxiliary; the native frame remains unchanged.

| Same-family precision measurement | RC201 | RC203 |
|---|---:|---:|
| Selected inverse width relative to G_lower | 1.823489 | 0.743003 |
| Width/half-Gram threshold ratio | 3.646978 | 1.486006 |
| Threshold minus width | -1.323489 | -0.243003 |
| Selected nominal residual squared upper | 0.176780 | 0.036914 |
| Selected adaptive action-error squared upper | 0.001905 | 0.002504 |
| Selected variational width | 0.335944 | 0.452039 |
| Exact half-Gram gate | Failed | Failed |

Galerkin gives width0.880612; least residual gives the selected0.743003, using refined endpoints. The selected action Young parameter is1/100, tail parameter1, and actual residual upper parameter1/3; the actual residual lower contribution is zero. The same-family inverse width improves by more than2.454 times, but its gate remains open. The nominal residual upper improves by more than4.788 times. Action-error and variational payments increase for the new trial, and must remain visible rather than be described as improving quantities.

## Full mixed-row attachment

RC202's exact finite polynomial and complete endpoint/regular/negative-r action carrier are attached to the reconstructed inherited carriers. Every mixed source, canonical and represented-action row is recomputed through65534. The q202 source polynomial ends at512, so its source mixed rows have no omitted source tail. Its action contains25 exact signed endpoint-output moments from4096 onward. Beyond65534, absolute moment amplitudes pay both sides of signed action pairings; diagonal action tail energy is nonnegative.

Actual canonical mixed entries intersect both self-adjoint orientations. The q202-source orientation needs only the inherited complete action error; the opposite orientation also pays the source/output tail and q202 action error. The q202 diagonal is intersected with RC202's independently certified actual canonical pairing. Actual action-Gram pairings are separately paid using the full-domain norm bound2 and both individual action errors, without error orthogonality.

## Residual and variational proof

The complete source, canonical and represented-action Grams define both Galerkin and least-residual eight-trial maps, rounded to exact rational coefficients. Every finite trial residual and source/residual pairing is reconstructed. q202's signed leading endpoint moment is retained in the common eta cancellation; its nonleading absolute moments supply an eighth remainder term. The tail sum-of-squares coefficient increases from21 to24 times the common eta energy, paying all eight terms.

The trial-source tail is unchanged in structure because q202 is finite. Response-adapted triangle weights pay all eight action errors. Exact PSD checks select the variational and residual Young parameters. RC201's independently valid inverse endpoints are available as candidate endpoints alongside refined and structural bounds.

## Verification and continuation

The main certificate SHA-256 binds RC202,RC201 and the entire input ancestry. Replay reverses inherited coefficient construction, mixed-row order, signed moment sums and trial/parameter searches, and requires exact equality of the whole certificate. The Git blob hashes of125 inherited certificate and validator files match the starting branch.

```
python scripts/validate_rpb108_rc203_residual_enriched_six_source_inverse.py --output certificates/rpb108_rc203_residual_enriched_six_source_inverse.json
python scripts/validate_rpb108_rc203_residual_enriched_six_source_inverse.py --replay --output certificates/rpb108_rc203_residual_enriched_six_source_inverse.json
```

Next: tighten the variational/action-error payments for the paid enriched trial, retaining its complete residual and signed tail data, then retest the same six-source gate. The remaining certified width deficit is0.243003 G_lower. This deficit concerns the selected enclosure, not a proved lower bound on true inverse uncertainty.

The accepted RC196 five-source result remains intact. Native z_b6/t10 complete action coverage, original Stage I source-range and augmented acceptance obligations, original Weil positivity,RH,F4 and Lean closure remain open/unclaimed.
