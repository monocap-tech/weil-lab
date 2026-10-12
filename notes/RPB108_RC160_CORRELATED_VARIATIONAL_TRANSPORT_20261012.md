# RC160: correlated Gram transport and inverse re-audit

Resume from RC159 (`7564929eb405a7f9a0874f60d1ec8ff48f082001`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are entered additively in `docs/TERMINOLOGY_RPB108_RC160_CORRELATED_FUNCTIONAL_TRANSPORT.md`.

RC159 refined the complete source Gram. RC160 carries that bound into the nonendpoint variational functional and the nominal residual while retaining RC158's source coordinates and rational inverse trials. All RC158 dependency hashes are checked before reconstructing its fixed old endpoint block and new direct cross blocks.

For Y=S V and Z=I-V, the exact identity

\[S^*Y+Y^*S-Y^*Y=G-Z^*GZ\]

gives correlated bounds directly from RC159's Loewner Gram interval. This avoids extracting independently uncertain Gram entries before the variational cancellation. The endpoint functional is evaluated separately from the existing paid conditioned endpoint blocks.

The nominal residual is decomposed as a native carrier combination plus the two new action trials. Its carrier energy is paid by congruence with the correlated Gram upper; all new mixed terms retain RC156-157's direct intervals. The resulting nominal-residual upper is checked PSD and compared to RC158's upper against the same Gram lower. Its relative bound improves from **0.133133 to 0.046640**, approximately **2.85x**. The tighter new bound is selected. RC155's action-error map remains paid and unchanged.

The complete variational upper candidates are rerun with five rational Young parameters. The variational lower still fails positivity, and the best selected enclosure remains the correlated structural baseline. Its certified inverse-width bound is **0.536203 times G_Lo**, above the half-Gram gate. On RC158's limiting direction the selected width is approximately 0.53314950 times its source Gram lower.

The separate budgets on that direction identify the next refinement:

| Quantity divided by the same source Gram lower | Certified value or enclosure diagnostic |
| --- | ---: |
| Nonendpoint Gram-functional interval width | 0.03818286 |
| Endpoint-functional interval width | 6.65064856 |
| Selected nominal residual energy upper | 0.04430470 |
| Inherited joint action error energy upper | 0.18106169 |
| Variational Loewner lower diagonal | -2.70751700 |

The endpoint-functional interval now dominates the nonendpoint Gram-functional width by more than two orders of magnitude. Its broadness reflects interval propagation after conditioning, not a true negative endpoint energy or a lower bound on inverse uncertainty. The direct pairing blocks and correlated Gram data remain available.

Next: bound the conditioned endpoint functional through the combined action identity and the paid joint action-error map, retaining correlations instead of independently charging all conditioned endpoint entries. Keep the improved nominal residual and rerun positivity and the full inverse-width gate separately.

No half-Gram inverse gate, Stage I closure, original Weil/augmented transport, whole-aperture positivity, F4, RH, or Lean closure is asserted.

## Reproduction

```bash
python scripts/validate_rpb108_rc160_correlated_variational_transport.py \
 --output certificates/rpb108_rc160_correlated_variational_transport.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json
```

RC158's eight named sibling dependencies are hash-checked. Add `--replay` to reverse interval term and parameter orders and check exact certificate equality. Historical files remain unchanged.
