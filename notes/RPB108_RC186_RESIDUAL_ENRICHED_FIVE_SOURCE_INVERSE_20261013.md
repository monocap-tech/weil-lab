# RC186: residual enrichment reduces the nominal error but retains the inverse enclosure

Parent: RC185, `a7abe9482eaa49e5d901facd6f1811387bda9d3e`.

RC186 evaluates RC185's exact finite q185 as an additional canonical inverse trial direction. The response family remains S=(P0,P2,f0,psi0,w14), so its residual and inverse-width comparisons with RC184 refer to the same operator, aperture, norm, and source family.

The certified nominal residual relative Gram factor decreases from0.162203 to0.029903. The available inverse enclosure retains RC184's width5.513393; the half-Gram acceptance gate remains failed. The smaller nominal residual is a precision improvement at the represented-residual layer. It is not an improvement in the certified inverse width or closure of the original theorem.

## Paid coordinate change and complete mixed geometry

The raw trial map is T=(P0,P2,f0,psi0,w14,q185). Its full source Gram, source/action mixed matrix, and represented action Gram are accumulated through degree16382. The native analytic tails of psi0 and w14 are evaluated by their unchanged eta and moment formulas. q185 and its represented action are exact finite carriers; the full action error outside those carriers remains paid by RC185's error bound.

The first five source directions retain their native Gram intersections from RC129 and the exact P2/f0 pairing. The q185 energy intersects RC185's finite-polynomial energy enclosure. Every canonical first-moment intersection includes both independently paid directional estimates; the old five-source block and q185's paid diagonal pairing supply additional intersections.

A rounded midpoint D-projection chooses b and an exact rational positive normalization d. The new coordinates retain the first five trial directions and replace q185 by (q185-Sb)/d. The complete transformed Gram lower is PSD and nonsingular, hence positive definite. This proves actual independence of the trial directions and pays the imperfect projection. No actual orthogonality or cutoff invariance is assumed.

Least-residual coefficients are selected in these coordinates, converted to the original six-column trial map, and rounded to a rational grid. Midpoint selection supplies no proof by itself: the actual finite residual and every tail are independently certified afterward.

## Same-family control and complete residuals

A control trial appends a zero q185 row to RC184's selected coefficients. This reproduces RC184's represented residual. The enriched trial uses all six columns.

| Trial, same five response sources | Nominal residual relative Gram upper | Actual residual relative Gram upper | Inverse width upper | Half-Gram gate |
|---|---:|---:|---:|---|
| RC184 baseline, independently reproduced | 0.162203 | 0.340031 | 5.513393 | Failed |
| q185-enriched least-residual trial | 0.029903 | 0.138955 | 5.513393 | Failed |

The nominal quantities bound squared D norm errors for every complex response mixture, relative to G_lower. Their square roots are norm factors. The new upper factor is about18.4% of the old upper factor; this compares certified bounds, not intrinsic actual residual norms.

The selected paid actual residual squared-error factor also decreases from0.340031 to0.138955 in this controlled comparison. These actual residual bounds include the inherited action uncertainty and every mixed error. They still do not close the inverse-width contract.

For each response column j, the actual-to-represented action error is bounded by sum_k |Y_kj| epsilon_k. A diagonal weighted Young matrix pays the sum for all complex mixtures, without declaring column errors orthogonal. An independent six-trial error envelope, transformed by congruence with Y, is also valid. The validator selects whole valid error matrices and records its choice.

The infinite nominal residual tail retains RC184's shared leading eta cancellation and the combined native-w14-source/f0-action coefficient before absolute values. The same four variable remainders and full negative-r factor range are paid. q185 adds no nominal tail because its represented carrier is finite. Its actual omitted action remains in epsilon_q185.

## Actual inverse identity and separate variational enclosures

For U=TY and actual residual R=S-MU, define

\[
 C=\operatorname{Sym}(S^*DU)+\operatorname{Sym}(U^*DR).
\]

Self-adjointness gives C=2 Sym(S*DU)-U*DMU, and the exact identity is

\[
 \Sigma=S^*DM^{-1}S=C+R^*DM^{-1}R.
\]

Using aI<=M<=2I, with a=32125/230953, the residual term lies between R*DR/2 and R*DR/a. Upper and lower Young bounds pay the difference between actual and nominal residuals.

Two independent constructions enclose C. The algebraic construction uses full trial Gram and canonical Gram Loewner bounds. The direct construction accumulates finite U/residual products, uses complete source Gram entries for S/U, and pays infinite U/residual products after shared tail cancellation, along with actual action errors. The direct entry intervals and the selected Loewner endpoints are recorded separately; they need not be from the same construction.

The baseline also retains its historically certified C enclosure. All trials may retain the inherited full inverse endpoints because the target source family is unchanged. The algorithm compares complete lower/upper matrix combinations, with exact PSD and width checks. It never takes entrywise extrema of matrix endpoints.

The selected inverse bounds retain the inherited endpoints. Thus the valid response enclosure still has width5.513393, acceptance ratio11.026786, and no positive half-Gram margin. RC184's exact failed-gate witness remains applicable. The new trial does not establish a narrower true inverse uncertainty bound.

## Replay and next obligation

Twenty-one inputs are hashed: RC185 and its twenty inputs in their historical order. Its bound hashes are checked, and the unchanged RC184 reconstruction checks inherited carrier custody. Replay reverses coefficient summations, candidate order, Young searches, and variational/error enclosure order. The entire certificate must reproduce exactly.

Run:

```
python scripts/validate_rpb108_rc186_residual_enriched_five_source_inverse.py --output certificates/rpb108_rc186_residual_enriched_five_source_inverse.json
python scripts/validate_rpb108_rc186_residual_enriched_five_source_inverse.py --replay --output certificates/rpb108_rc186_residual_enriched_five_source_inverse.json
```

Next: tighten inherited actual canonical endpoint-action and variational enclosures on this same five-source family. In particular, larger paid finite inputs for the centered psi0 and w14 endpoint carriers can be tested as precision refinements. This is a proposed next construction, not a guarantee that it will close the gate. The retained q185 trial can then be evaluated with the tighter actual-action bounds.

The accepted four-source inverse remains intact. Native v10,z_b6,t10 coverage remains open. Original augmented Weil floor/auxiliary response obligations, Stage I, whole-aperture original Weil positivity, RH, F4, and Lean remain open/unclaimed.
