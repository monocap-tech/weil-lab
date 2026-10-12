# RC161: combined endpoint functional and positive variational lower

Resume from RC160 (`35dd036a8badd49571194fb4ccd5be662ef56587`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions appear additively in `docs/TERMINOLOGY_RPB108_RC161_COMBINED_ENDPOINT_FUNCTIONAL.md`.

RC160 isolated the conditioned endpoint functional as the dominant enclosure error. RC161 evaluates it through one complete combined action identity rather than propagating independently paid endpoint entries through the conditioned source coefficients.

For the fixed seven inverse trials, H_approx=Sym<q(Y),y(Y)> has an old action part paid by correlated Gram polarization and a new action part paid by RC156-157's directed trial-source blocks. The actual endpoint functional differs by Sym<e,y>. For every signed real or complex mixture, Cauchy and Young give

\[-K\preceq H_Y-H_{approx}\preceq K,\qquad K=\tfrac12(\gamma E+G_y/\gamma).\]

Two valid joint error bounds are tested: RC155's global Gram bound and a weighted seven-column Cauchy bound preserving especially accurate old action columns. Five rational endpoint parameters are checked for each. The selected bound is the weighted column bound, with gamma=2. All candidates are accepted by exact rational PSD and matrix-width checks.

The full endpoint-functional width bound improves from **6.650649 to 0.666942 times the source Gram lower**. On RC158's limiting conditioned direction, the endpoint interval width falls from approximately 6.65064856 to **0.61256356**, an improvement of **10.85707x**.

The resulting complete seven-source variational Loewner lower now passes the exact **PSD positivity check**. Its limiting-direction diagonal is approximately **0.30967142 times the certified source Gram lower**, replacing RC160's negative lower estimate on that direction. This certifies the checked lower; it is not a statement that all prior lower estimates were positive or that a numerical precision gate has closed.

The inverse upper candidates use the same selected joint error bound with RC160's improved nominal residual. With that endpoint bound and the tested residual parameters, the best new paired enclosure has certified relative width **0.726260**, wider than RC160's valid correlated structural enclosure. RC161 therefore retains the sharper existing lower/upper pair at **0.536203**. The half-Gram inverse-width gate remains unproved.

The next target is a sharper joint action-error estimate on the conditioned inverse trials, preserving accurate old columns and the signed correlation of the new action directions. Retain the completed pairing interface, correlated Gram bounds, and improved nominal residual, then recheck the combined endpoint lower and full inverse width separately.

No true inverse uncertainty lower bound, Stage I closure, original Weil/augmented transport, whole-aperture positivity, F4, RH, or Lean closure is asserted.

## Reproduction

```bash
python scripts/validate_rpb108_rc161_combined_endpoint_functional.py \
 --output certificates/rpb108_rc161_combined_endpoint_functional.json \
 certificates/rpb108_rc160_correlated_variational_transport.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json
```

The predecessor chain is hash-checked. Add `--replay` to reverse interval term, error-bound, and rational parameter orders and check exact certificate equality. Historical files are unchanged.
