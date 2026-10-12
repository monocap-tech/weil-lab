# RC168: positive eta tail moments and reference inverse re-audit

Resume from RC167 (`515236e9c87245d5252c30791c0177886bf72def`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are added in `docs/TERMINOLOGY_RPB108_RC168_POSITIVE_ETA_MOMENTS.md`.

RC167 combined the fixed trials' signed analytic tails and reduced the selected inverse width to 0.504196. Its remaining tail estimates bounded each nonnegative monomial between zero and the full eta energy. RC168 pays the positive moment measure itself, including lower bounds, and combines products of the same degree before charging their signs.

For each moment order through 48, directed arithmetic sums every even degree 16384..65534 using the exact D-energy weight 2a(2n+1)/(n^2(n+1)^2 D_n). Harmonic numbers and s are enclosed with the established directed arithmetic. No point sample stands in for an infinite sum. Monotonic preceding width-two cells pay the full remaining eta energy, and the maximal omitted monomial ratio pays each higher moment. The result is 49 rigorous finite-plus-infinite moment intervals.

The full source, inverse-trial, action, and nominal residual eta polynomials are unchanged. Their signed products are first convolved by monomial degree. Each resulting coefficient then uses the correct directed lower or upper moment endpoint. This preserves cancellations both between physical-vector contributions and between product terms sharing a moment.

RC167's finite-prefix bounds are reused by exact linear decomposition. At the original fixed Loewner weights, its full entry interval was the sum of its finite-prefix interval and the exact old analytic tail interval, with outward rounding margins. The Loewner map is linear in those entry endpoints. Subtracting that specific old interval map therefore recovers a valid prefix enclosure; its rounding margins stay with the prefix. The new moment interval map is added afterward. This argument does not subtract an arbitrary tail upper from an unrelated Gram upper.

The source Gram is refined separately: RC159's finite-prefix lower is retained, its recorded analytic Young upper is removed from its full upper to recover the prefix upper, and the new paid full tail Gram interval is added to both bounds. The resulting source Gram lower and upper, endpoint interval gap, recovered finite residual Gram upper, and updated residual Gram upper pass exact PSD checks as applicable.

The source vectors, three action approximants, conditioning X, inverse-source coefficients Y, and action-column error norms remain unchanged. The previously paid error matrices remain fixed valid quadratic uppers. The new source Gram is transported through the same correlated functional identity, and all tested inverse candidates are checked against the refined source Gram lower. The prior RC167 enclosure remains available and is compared using the same new lower.

The full reference half-Gram gate is retested. Whether it passes or fails, Stage I's required final tolerance and original Weil/augmented transport remain distinct obligations. No whole-aperture positivity, F4, RH, or Lean closure is asserted.

The **reference half-Gram width gate passes**. Across **144** tested candidates, the selected inverse width is **0.450692**, using weighted fraction 1, endpoint gamma 3, residual tau 2, a positive variational lower, and the paid variational upper. The full seven-by-seven matrix (1/2)G_lower-(U-L) is stored and passes exact rational PSD checks. The certified width is **0.049308 below** the 0.5 threshold.

The source Gram relative width improves from **0.036203** to **0.002348**. The approximate endpoint interval width improves from **0.009503** to **0.000516**, while the nominal residual relative upper is **0.020109** and the best full endpoint width **0.330127**.

The comparison uses a stronger certified lower for the same physical source Gram. RC167's unchanged inverse enclosure has width **0.490212** against this new lower, compared with its previously reported **0.504196** against the old lower. The newly rebuilt RC168 enclosure improves further to **0.450692** against that same new lower. Thus the gain includes both improved source normalization and tighter endpoint/residual transport; it is not an improvement in action-error norms.

This closes the specific reference half-Gram component gate. The next pass must audit and discharge the actual required Stage I tolerance and source transport obligations, rather than infer Stage I or whole-aperture positivity from this component certificate alone.

## Reproduction

```bash
python scripts/validate_rpb108_rc168_eta_tail_moment_enclosure.py \
 --output certificates/rpb108_rc168_eta_tail_moment_enclosure.json \
 certificates/rpb108_rc167_combined_action_tail_transport.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc160_correlated_variational_transport.json \
 certificates/rpb108_rc165_centered_t_action.json \
 certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json
```

Add `--replay` to reverse finite moment sums, polynomial coefficient checks, and candidate traversal and compare exact JSON equality. Numerical eigenvalue estimates propose grid widths only; exact rational PSD acceptance and rejection of the immediate predecessor certify every width. Historical files are unchanged.
