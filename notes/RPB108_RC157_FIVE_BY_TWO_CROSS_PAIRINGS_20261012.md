# RC157: five-by-two direct mixed pairing blocks

Resume from RC156 (`50a537144260f63e735d2d2b579a785f8c097ea3`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions appear additively in `docs/TERMINOLOGY_RPB108_RC157_CROSS_PAIRINGS.md`.

The old sources are (P0,f0,w14-alpha*psi0,(v10+z_b6)/2,t10); the new sources are (psi0,delta), delta=z_b6-v10. RC157 reconstructs RC156's two action trials and directly reconstructs t10's finite polynomial. All three finite coefficient/radius hashes are verified against their predecessor certificates. The nine RC156 dependencies and the additional collective-vector checkpoints are checked by their stored hashes.

The direct finite pairing prefix reaches even degree 16382. Source coefficients include the original symbolic f0, w14's rational finite polynomial and prescribed analytic moments, v10 and z_b6's separate rational center polynomials and analytic moments, and t10's rational polynomial and output-tail moments. The old action trials are exactly RC138's carrier-coordinate columns. The new q_psi includes RC154's midpoint input tail and its distinct analytic output-tail expansion; q_delta is RC153's finite polynomial.

All twenty directed old/new trial-source pairings are enclosed: ten entries <q_old,i,s_new,j> and ten entries <q_new,j,s_old,i>. These two blocks are not assumed to be transposes. All ten mixed old/new trial Gram entries are also enclosed. Every remaining infinite pairing tail is paid after multiplying the signed common-eta polynomial factors; no independent-tail orthogonality or error sign is assumed.

For each of the ten symmetric source endpoint cross entries, both action directions are intersected with the inherited endpoint interval after paying epsilon_old||s_new|| and epsilon_new||s_old||. The certificate records the resulting rational intervals and every width improvement.

| Old source | psi0 width improvement | delta width improvement |
| --- | ---: | ---: |
| P0 | 2.22376x | 60.09422x |
| f0 | 17.81845x | 60.13050x |
| w14-alpha*psi0 | 105.32288x | 90004.06519x |
| (v10+z_b6)/2 | 164.59539x | 801.49002x |
| t10 | 12.41750x | 22.05504x |

These displayed improvement factors are rounded down from the exact rational ratios. All ten endpoint intervals tighten. They measure an improvement of certified interval widths, not a lower bound on actual trial errors.

The direct pairing interface is now available on the complete seven-source split: preceding RC149 and carrier certificates supply the paid old block, RC156 supplies the complementary block, and RC157 supplies the cross blocks. A seven-source variational inverse-response matrix can now be assembled from those data and RC155's joint action-error bound. Its positivity and full matrix width still require their own checks. No inverse-response closure is inferred merely from pairing availability.

Stage I tolerance, original Weil/augmented transport, whole-aperture positivity, F4, RH, and Lean closure remain open. The next pass is the seven-source variational inverse assembly and an exact rational matrix-width audit.

## Reproduction

```bash
python scripts/validate_rpb108_rc157_five_by_two_cross_pairings.py \
 --output certificates/rpb108_rc157_five_by_two_cross_pairings.json \
 certificates/rpb108_rc156_complement_direct_pairings.json \
 certificates/rpb108_rc138_reference_variational_response.json \
 certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc135_common_response_capture.json
```

The validator resolves RC156's nine explicitly named sibling dependencies and RC153's hash-checked RC152 dependency. Add `--replay` to reverse the source and pairing sums, then check exact certificate equality. Historical checkpoint files are unchanged.
