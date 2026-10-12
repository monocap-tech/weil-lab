# RC164: changed delta pairings and coherent inverse reassembly

Resume from RC163 (`36123323ace400c74bfb856ce69c876c28a738b4`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are added in `docs/TERMINOLOGY_RPB108_RC164_DIFFERENCE_PAIRING_REBASE.md`.

RC163 reduced the full delta action error bound to 4.947728908995e-6 and the changed inverse trials' uniform marginal error factor to 0.113762. Its new physical action trial required new pairings before either number could enter a reference inverse enclosure. RC164 pays those entries directly.

The validator reconstructs the RC156/157 carrier and action trials, retaining every predecessor coefficient hash check. It checks the RC163 corrected finite trial hash and each analytic output moment against the canonical rational delta coefficients. It evaluates the new delta trial's seven trial-source entries and seven trial Gram entries, including the new diagonal. Finite pairings use directed intervals through even degree 16382. Every remaining vector shares eta_n times its prescribed polynomial; signed coefficient products pay the full analytic pairing tails. Mixed signs, orthogonality, and trial-source symmetry are not assumed.

The unchanged psi trial row and its Gram diagonal are retained. The changed delta row, psi-delta Gram entry, and delta diagonal replace their historical counterparts. The nominal residual is rebuilt as the aggregate native carrier term plus the two physical action trials. The combined endpoint approximation uses the correlated old action Gram polarization and the new two-row direct pairing matrix.

For the unchanged source/resolvent vectors y=WY, the paid source Gram identity still gives the non-endpoint functional. The endpoint error and residual error use fresh action-error uppers for q_delta_new. Weighted Cauchy and the RC163 uniform bound are blended at fractions 0, 1/2, and 1; endpoint Young parameters 1, 2, 3, and 4 are tested. Each is compared with residual Young parameters 1/4, 1/2, 1, 2, and 4 and the structural upper. The best full inverse width is selected across the complete tested family, with the previous RC162 enclosure retained if sharper.

The best tested endpoint width improves from **0.666942** to **0.568012**. The rebuilt nominal residual relative upper is **0.048838**, compared with the old physical trial's **0.046640**. A tighter action error norm therefore did not improve every separate budget: the physical trial and its direct tail pairings changed as well.

Across all 72 tested inverse candidates, the best new width is **0.585022** (weighted fraction 1, endpoint gamma 2, structural upper). The positive variational lower passes PSD checks. RC162's **0.536203** inverse enclosure is sharper and is retained unchanged. The half-Gram inverse-width gate remains open. These are widths of the selected certified enclosures, not lower bounds on true uncertainty or obstructions to the target theorem.

On the previously recorded limiting conditioned coordinate e6, the approximate endpoint interval width rises from **0.02712750** to **0.03402527** times the source Gram lower. The improved marginal action bound more than offsets that increase in the full endpoint estimate, but the changed analytic trial has not preserved every previous cancellation budget.

Recomputing the shares on RC163's own maximizing marginal control gives approximately:

| Action column | Share of the new marginal norm-budget control |
| --- | ---: |
| t10 | 44.93087% |
| psi0 | 32.43345% |
| delta | 18.66720% |
| (v10+z_b6)/2 | 3.96111% |
| w14-alpha*psi0 | 0.00738% |
| P0 and f0 | negligible at displayed precision |

These are contributions to the artificial marginal norm-budget control, not a measured decomposition of actual error. With the delta rebase paid, the next physical action target is t10, followed by psi0; preserving conditioned analytic-tail cancellations remains a separate precision target.

This certificate concerns the reference inverse of I+C on the seven-source carrier. Original Weil/augmented transport and the final Stage I tolerance remain separate obligations. Stage I, whole-aperture positivity, F4, RH, and Lean closure are not asserted.

## Reproduction

```bash
python scripts/validate_rpb108_rc164_difference_pairing_rebase.py \
 --output certificates/rpb108_rc164_difference_pairing_rebase.json \
 certificates/rpb108_rc163_centered_difference_tail_action.json \
 certificates/rpb108_rc162_trial_signed_error_optimum.json \
 certificates/rpb108_rc161_combined_endpoint_functional.json \
 certificates/rpb108_rc160_correlated_variational_transport.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json \
 certificates/rpb108_rc157_five_by_two_cross_pairings.json
```

The implicit predecessor files are selected by their exact checkpoint hashes. Add `--replay` to reverse coefficient sums, interval term orders, and candidate traversal and compare exact certificate equality. Historical files are unchanged.

Width search can use an optional NumPy eigenvalue estimate to propose a rational grid point. The proposal is accepted only if exact rational PSD checks accept that grid width and reject its immediate predecessor; otherwise the validator uses exact bisection. The numerical estimate is not a proof input. This optimization was checked against the previously certified 0.113762 action-error and 0.536203 inverse-width controls.
