# RPB108 — CC105: resolve the selected response obstruction

Parent: CC104, `0230c9ec6cb034f1713b30c7652568fcaafc30c5`.
Read-only Native Source: NF52, `19c11a4f9f8f03b039fcb30a8addf4d96029c53c`.
Read-only DNE recovery head: `3dbaa8a43b92682ed671936b273603f6e65dc69b`; DNE40 is preparation, DNE39 remains the certified integration.
Definitions: `docs/TERMINOLOGY_RPB108_CC105_SELECTED_SOURCE_RECONSTRUCTION.md`.

Fresh original-source reconstructions resolve both CC104 late trials. At the proved original high floor kappa=289/500, the NF52 source-response sufficient lower bound is strictly negative on both selected physical vectors, although their original native energies are strictly positive. This rejects positivity of that sufficient matrix, not positivity of the original Weil form. The integrated positive span remains 56 retained directions plus every original infinite high vector, with physical guard greater than 1e-38; 56 retained directions remain uncovered.

## Reconstruction and evidence

The physical trial is the exact rational CC104 candidate in the unchanged Native P,T53 frame. Its physical Legendre coefficients are combined before computing the source, preserving cancellations that entrywise matrix enclosures lose. Each trial is divided by a rational upper bound for its exact physical norm. The independent consumer reconstructs the three-constraint frame by rational Gaussian elimination, verifies the exact normalization, authenticates every recovered NF52 high column and checks their exact physical Gram. There are eleven even and ten odd high columns; maximum physical degree is 244 even and 243 odd.

Eight fresh analytic computations evaluate the original source: selected source stars at regular-kernel orders 360 and 400 with outward Decimal precisions 760 and 800; trial-only native computations at orders 580 and 620 with precisions 1000 and 1040, in each parity. They use the inherited analytic identities and immutable original-source helper, including exact endpoint logs, all six prime powers with both clipped translations, seven half-panels, and analytic regular and pole tail payments. These are fresh analytic runs, not independent derivations of the inherited identities. The separate rational consumer checks source projections, source norm and rounding payments, physical L2 error payments, primary/replay containment, high-order native energy payments, and both orientations of the native trial/high crosses.

The complete projected trial source and signed trial/high crosses are fresh. High/high source off-diagonals remain authenticated NF52 data; their diagonal enclosures are intersected with fresh computations. This is a selected source star, not a new full high/high Gram. Reconstructed high surplus and inverse denominator are proved positive by rational congruences and inverse residual bounds. The final consumer passes 1,742 exact rational checks.

For original high restriction A and physical high family H, let M=H*H, QH=H*AH, GH=(AH)*(AH), B=Q(f,H), S=(P_F Lf)*AH, q=Q(f,f), g=||P_F Lf||^2. With C=QH-kappa M>0, N=GH/kappa-QH>0 and w=S-kappa B, the sufficient scalar lower value is

    l=q-g/kappa+w N^-1 w*/kappa^2.

The following decimal displays are approximate centers; exact outward rational intervals are saved in the validation report.

| Quantity at proved kappa=0.578 | Even | Odd |
|---|---:|---:|
| Original native energy q | 4.1298533694e-32 | 4.9566950762e-28 |
| Plain remaining-source lower value | -1.1674314278e-33 | -9.6794857417e-30 |
| Positive response credit | 1.0607172396e-33 | 9.1218297646e-30 |
| Refined response lower value | -1.0671418823e-34 | -5.5765597705e-31 |

The rigorous refined intervals are [-1.067141900214154e-34,-1.067141864311268e-34] even and [-5.576559771989191e-31,-5.576559769037068e-31] odd, with decimal endpoints rounded outward. The exact native lower endpoints are positive. The reconstructed intervals are over 3.48e12 and 2.44e11 times narrower than the corresponding physically normalized CC104 entrywise trial intervals. CC104's unresolved trials remain historical; this fresh evidence resolves those selected sufficient-bound signs.

## Strength and cost comparison

The CC93 response method adds a positive semidefinite term to the same-floor remaining-source matrix. It is therefore never weaker when its hypotheses and all payments hold. A strict improvement of matrix values does not alone prove a whole collective packet passes response while failing the remaining-source criterion.

CC105 also pays a conditional comparison at kappa=29/50=0.580. Both high surplus and denominator remain positive. On these same genuine original-source trials the plain values remain negative, while the response values are rigorously positive: approximately 3.56077157e-35 even and 1.1472963293e-30 odd. This establishes a strict directional separation at a common conditional floor. That original floor has not been proved here, and positivity on two trials is not collective positivity.

There is no demonstrated computational saving. The response calculation retains the complete source information required by the plain criterion, adds high native/source mixed data, positivity checks and a verified inverse. Selected source reconstruction is an economical diagnostic relative to rebuilding the entire matrix, but cannot replace a collective certificate. No matched-cost benchmark or cheaper complete collective algorithm has been established.

The next concrete target is a certified original floor of at least 0.580, for example by rigorously certifying a higher positive prime weight iteration, followed by a coherently paid complete collective response matrix. An exploratory prime-weight probe is not a floor certificate. Even a certified 0.580 floor would only activate the two directional successes above; all collective gates still require proof.

## Reproduction and scope

The ten analytic/physical JSON artifacts are stored as deterministic gzip (mtime zero) plus base64. Decoded and stored hashes are recorded in `notes/data/RPB108_CC105_CUSTODY_20261010.json`. New Native imports preserve their original Git blob identities under `notes/cc105-source/`; their source provenance and hashes are recorded separately. Existing CC104 and CC101 dependencies remain immutable.

```sh
python scripts/materialize_cc105_selected_sources.py even --output notes/data/RPB108_CC105_EVEN_PHYSICAL_PACKET_20261010.json
python scripts/materialize_cc105_selected_sources.py odd --output notes/data/RPB108_CC105_ODD_PHYSICAL_PACKET_20261010.json
```

For each parity, reproduce the full source star with DNE16_ORDER=360 DNE16_PRECISION=760 (PRIMARY) and DNE16_ORDER=400 DNE16_PRECISION=800 (REPLAY), using `scripts/certify_cc105_selected_source_star.py PARITY --output PATH`. Reproduce the native trial computations with orders/precisions 580/1000 and 620/1040 and add `--trial-only`. Use the corresponding published SOURCE_PRIMARY, SOURCE_REPLAY, NATIVE_PRIMARY and NATIVE_REPLAY JSON names. The packet builder materializes plaintext physical inputs for the producer. To audit published data without recomputation:

```sh
python scripts/validate_cc105_selected_response.py --output notes/data/RPB108_CC105_SELECTED_RESPONSE_VALIDATION_20261010.json
```

The consumer accepts the compressed published artifacts automatically. Fresh analytic computations, rational stored-data audits and inherited analytic identities are distinguished above. No Native or DNE branch receives writes. Whole original positivity at 53/50, RH, F4 and Lean remain open; the whole-aperture anchor remains 21/20.
