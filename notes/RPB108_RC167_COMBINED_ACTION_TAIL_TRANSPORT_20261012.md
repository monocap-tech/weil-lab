# RC167: signed aggregate action-tail transport

Resume from RC166 (`a29a689a4ca2ced03e136b444886dc69ef9256e6`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are added in `docs/TERMINOLOGY_RPB108_RC167_COMBINED_ACTION_TAILS.md`.

RC166 paid the complete three-action interface and improved endpoint width to 0.348822. Its selected reference inverse width remained 0.536203. The 144 inverse candidates were tested separately; they did not all have the selected width.

RC167 leaves the seven canonical sources, all three physical action approximants, their marginal error norms, the source conditioning X, and inverse-source coefficients Y unchanged. It targets uncertainty introduced by paying separate analytic pairing tails before signed conditioning.

The validator reconstructs the RC166 coefficient and pairing interface and retains all predecessor hashes. For each inverse trial column, it sums exact native action coefficients and the q_t/q_psi/q_delta tail polynomials before any tail product or absolute bound. It also constructs the inverse source tail and the complete nominal residual tail. The exact identity residual_tail=action_tail+inverse_source_tail-conditioned_source_tail is checked coefficient by coefficient.

Finite combined-vector pairings are paid with directed intervals through even degree 16382. Infinite pairings use the common eta energy upper and signed products of the already combined polynomial coefficients. The endpoint approximation is the symmetric pairing of the combined approximate action with the fixed inverse-source vector. The nominal residual Gram uses the complete combined residual, including its diagonal and all cross entries. No mixed-error sign, tail orthogonality, or exact invariance of the seven-source span is assumed.

These direct full-vector enclosures are compared with RC166's valid block-transport enclosures. Only whole matrix enclosures are selected, not entrywise minima. The unchanged weighted and uniform action-error uppers are then tested with the same endpoint and residual Young parameters. Structural and positive variational lower bounds remain independent candidates. Each full-matrix grid width is accepted and its immediate predecessor rejected by exact rational PSD checks; numerical estimates only supply proposals.

This is an enclosure-transport refinement, not an improvement in actual action norm information or a change to the physical trials. The selected inverse enclosure and half-Gram width gate are audited separately from the endpoint and nominal residual budgets. No lower bound on true uncertainty, Stage I closure, original Weil/augmented transport, whole-aperture positivity, F4, RH, or Lean closure is asserted.

Both combined enclosures are selected. The approximate endpoint relative width falls from **0.035496** to **0.009503**, and the nominal residual relative upper from **0.050269** to **0.020571**. After the unchanged action-error budget is paid, the best full endpoint width improves from **0.348822** to **0.331159**.

Across **144** tested inverse candidates, the selected full reference inverse width improves from **0.536203** to **0.504196**. The half-Gram width gate remains open: this enclosure is **0.004196** above its 0.5 target. This is an actual improvement in the certified inverse enclosure, achieved without a new action trial or a better marginal error norm.

On the recorded limiting conditioned coordinate, the approximate endpoint width falls from **0.03534992** to **0.00950250**, and the nominal residual upper from **0.04916411** to **0.01700226**, relative to the same source Gram lower. These directional figures diagnose the paid bounds; the full-matrix PSD checks, not a single direction, establish the selected width.

Before increasing an action cutoff, the remaining correlated-tail precision can be targeted by paying positive eta-weighted tail moments with lower and upper bounds, rather than bounding every nonnegative monomial only between zero and the full eta tail energy. Products with the same monomial degree can also be combined before their signs are charged. Those refinements are not included in this certificate and no gate closure from them is assumed.

## Reproduction

```bash
python scripts/validate_rpb108_rc167_combined_action_tail_transport.py \
 --output certificates/rpb108_rc167_combined_action_tail_transport.json \
 certificates/rpb108_rc166_three_action_pairing_rebase.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json
```

Implicit RC166 predecessors are located by exact checkpoint hashes. Add `--replay` to reverse finite source sums, coefficient checks, interval terms, and candidate traversal and compare exact JSON equality. Historical files are unchanged.
