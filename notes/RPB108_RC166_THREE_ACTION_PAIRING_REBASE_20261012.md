# RC166: paid t10 mixed pairings and three-action inverse reassembly

Resume from RC165 (`22d8ab30361a167cbb586712c35bb045bcae3935`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are added in `docs/TERMINOLOGY_RPB108_RC166_THREE_ACTION_REASSEMBLY.md`.

RC165 reduced the full t10 action error bound to 3.666443165323e-5 and the changed inverse trials' marginal error factor to 0.056779. RC166 pays the new physical trial's pairings before using either bound in reference inverse reassembly.

The validator reconstructs the completed RC164 finite source and action interface with all predecessor coefficient checks. It reconstructs the new direct Ct prefix, verifies RC165's finite action and corrected trial hashes, recomputes every output moment, and reproduces the complete action norm certificate. The new trial uses canonical t finite centers through degree 16382. Its action output tail starts earlier, at 8192, so these two transitions remain distinct.

Seven new t trial-source pairings and eight old/new trial Gram pairings are evaluated directly through even degree 16382, with signed eta-polynomial products paying their entire infinite tails. The eight trial crosses include the old fitted Ct for audit, both q_psi and q_delta_new, and the new t trial diagonal. The old fitted Ct is not used as its replacement in the inverse calculation.

The unchanged q_psi/q_delta source rows and two-trial Gram block are retained from RC164. The new t row and mixed Gram entries form a three-by-seven source interface and three-by-three trial Gram. The source matrix W, conditioned source transform X, and rational inverse-source coefficients Y stay unchanged.

Reference reassembly removes the old fitted Ct native action column. The native action is T4 Y[0..3], and the native nominal residual is W(Y-X)+T4 Y[0..3]. All three non-native action columns are then included in the endpoint approximation and residual Gram, using their paid mixed matrices. The unchanged correlated source Gram identity still pays the non-endpoint functional.

The RC165 uniform error upper and a fresh weighted-column Cauchy upper are blended with fractions 0, 1/2, and 1. Endpoint Young parameters 1, 2, 3, and 4 and residual parameters 1/4, 1/2, 1, 2, and 4 are tested, together with the structural upper. Both the structural half-Gram lower and any PSD variational lower are tested independently. This avoids selecting a weaker lower merely because it is positive. A numerical eigenvalue hint only proposes a rational grid point: exact PSD acceptance at that point and rejection of its immediate predecessor certify every reported width.

The certificate records limiting-direction endpoint, nominal residual, action-error, and inverse-width budgets. These are upper-bound diagnostics, not lower bounds on true inverse uncertainty or impossibility results. Original Weil/augmented transport, the required final Stage I tolerance, whole-aperture positivity, F4, RH, and Lean closure are separate obligations and are not asserted here.

The best tested full endpoint width improves from RC164's **0.568012** to **0.348822**. Its variational lower passes exact PSD. The rebuilt nominal residual relative upper is **0.050269**, compared with **0.048838** for the old physical Ct approximation. A sharper action norm has therefore not reduced every separate uncertainty budget.

All **144** tested inverse candidates are certified. The selected full inverse width remains **0.536203**, attained by the structural half-Gram lower and correlated structural upper. The new variational estimates do not beat it. The reference half-Gram width gate remains open; no Stage I closure is inferred from the endpoint improvement.

On the recorded limiting conditioned coordinate, the approximate endpoint interval width is **0.03534992**, nominal residual upper **0.04916411**, selected marginal action-error upper **0.056779**, and retained inverse width **0.53314950**, each relative to the same source Gram lower. The next precision target is the actual q_psi action bound or stronger preservation of conditioned analytic-tail correlations, with all three paid action columns retained.

## Reproduction

```bash
python scripts/validate_rpb108_rc166_three_action_pairing_rebase.py \
 --output certificates/rpb108_rc166_three_action_pairing_rebase.json \
 certificates/rpb108_rc165_centered_t_action.json \
 certificates/rpb108_rc164_difference_pairing_rebase.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json \
 certificates/rpb108_rc160_correlated_variational_transport.json
```

Implicit RC164 predecessors are selected by exact checkpoint hashes. Add `--replay` to reverse source sums, interval terms, and candidate traversal and check exact JSON equality. Historical files are unchanged.
