# RC158: seven-source inverse assembly and failed precision audit

Resume from RC157 (`fe3375694afaad01a879f069fff8b18a3df630f4`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are entered additively in `docs/TERMINOLOGY_RPB108_RC158_INVERSE_ASSEMBLY.md`.

The full seven-source variational inverse candidate has been assembled. The old trial columns and narrow source coordinate from RC145-149 are retained, including RC149's endpoint block evaluated after signed conditioning. RC156 supplies the complementary direct trial/source and trial Gram block; RC157 supplies the cross blocks. RC155 supplies the joint action-error map. All declared certificate hashes and these interfaces are checked.

The source coordinates eliminate the paid five from psi0 and delta with the certified Gram lower. The last coordinate is the paid-coordinate-adjusted delta+0.4828795091395692... psi0 direction. Rational least-residual coefficients for the two new inverse trials are chosen using assembled Gram centers; center matrices are not used for acceptance.

For A=I+C and trial matrix Y, the complete matrix identity is

\[\Sigma=L+r^*A^{-1}r,\qquad L=S^*Y+Y^*S-Y^*AY,\qquad r=AY-S.\]

All source/old-action coefficients are combined before interval evaluation. The nominal residual's new action-trial terms use the directly paid mixed pairings and trial Gram. Signed Young bounds combine that nominal residual with RC155's full action-error map, with five rational parameters tested. Every resulting matrix-width candidate is checked against the complete conditioned source Gram lower by exact rational PSD bisection.

The variational Loewner lower does **not** pass positivity. In the last conditioned source coordinate its diagonal divided by the certified source Gram lower is approximately -4.02148. This is a failure of the enclosure's lower estimate, not evidence that the true reference inverse is nonpositive.

The variational upper candidates, after pairing with the positive structural lower, have relative widths:

| Signed Young parameter | Certified inverse-width upper |
| --- | ---: |
| 1/4 | 5.876761 |
| 1/2 | 5.547763 |
| 1 | 5.432899 |
| 2 | 5.474707 |
| 4 | 5.694196 |

The best checked full enclosure therefore retains the structural baseline

\[\tfrac12G_{Lo}\preceq\Sigma\preceq G_{Hi}.\]

It is positive on all seven sources and is transported back to the native seven-vector coordinates. Its certified matrix width is **2.514662 times G_Lo**, which fails the half-Gram precision gate. The seventh conditioned unit vector is an exact rational failure witness: its checked inverse enclosure width divided by its source Gram lower is approximately **2.5107758955**.

The source Gram enclosure itself has relative width at most **2.014662**. On that same conditioned direction its Gram-width-to-lower-energy ratio is approximately **2.0107758955**. Thus the numerical Gram interval, especially its correlated analytic tail in the near-dependent direction, is already too broad for the selected structural inverse enclosure. The conditioned variational functional intervals also need refinement; RC155's 0.485070 action gate alone cannot substitute for either check.

This pass completes and audits the assembly, with a valid positive baseline inverse enclosure. It does not certify the desired inverse precision, Stage I closure, original Weil/augmented transport, whole-aperture positivity, F4, RH, or Lean closure. No lower bound on true inverse uncertainty or impossibility of later refinement is inferred.

The next smallest calculation is correlated source-Gram tail refinement in the seventh conditioned direction, retaining cancellations between the prescribed eta-moment tails instead of paying the inherited independent diagonal tail majorant. Then refine the conditioned functional intervals and rerun the full variational width audit. The direct pairing blocks are available and do not need to be declared missing again.

## Reproduction

```bash
python scripts/validate_rpb108_rc158_seven_inverse_assembly.py \
 --output certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc157_five_by_two_cross_pairings.json \
 certificates/rpb108_rc156_complement_direct_pairings.json \
 certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc149_combined_five_matrix.json \
 certificates/rpb108_rc138_reference_variational_response.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc145_fifth_source_conditioning.json \
 certificates/rpb108_rc146_narrow_coordinate.json
```

Add `--replay` to reverse interval term and parameter orders and check exact certificate equality. Historical checkpoint files are unchanged.
