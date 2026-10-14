# RPB108 — RC247: response with materialized residual augmentation

Date: 2026-10-14 UTC. Parent RC246: `36ff5ec47fdadbbac35f98704a7941e7a7421705`. Branch: research/rpb108-route-consolidation. Aperture B=11/10.

RC247 recomputes the same two original-action inverse responses using RC246's materialized R0/R1 augmented actions and RC245's refined original-source errors. The trial spaces remain span{P0,P2,P4,R0} and span{P1,P3,P5,R1}. Both certified inverse upper bounds improve by about 27%.

Neither signed-gap interval proves positivity or an actual negative original direction. There are still two response sources and four trials per parity, not exhaustive evaluation of the complete 639-dimensional signed criterion. Full signed positivity, original whole-space positivity, the full auxiliary norm gate, Stage I, RH, F4 and Lean remain open.

## Updated complete action columns

Retain the actual original actions and all P0–P5 augmentation columns from the pinned preceding certificates. Replace the R0/R1 augmented centers with the materialized degree-128 columns from RC246. Their complete original, band omitted-output, finite-rounding and rational comparison faults remain paid. Every center array has 129 entries; old degree-64 arrays retain their zero padding together with their full omitted-output error bounds.

Evaluate both RC245 source representations:

- The old degree-64 original source center with its sharper orthogonal-output-split complete error bound, paired with the consistently certified old first augmented trial center.
- The extended degree-128 original source center, paired with the correspondingly extended first augmented trial center.

Each representation uses the same actual source O=N0 P_base and the same actual operators. Its source and first original trial action share their model fault, so that fault has coefficient |1-y0| in the residual. The actual augmentation center difference and its separate fault are preserved. Changing center representation does not create a new physical source or trial.

## Actual cross forms

The actual original form interval matrix is unchanged. The physical inputs and original operator are the same, and the older sharp form certificates remain valid independently of these approximation-center changes.

For each rational frequency cross entry involving R, intersect the preceding actual interval with RC246's new materialized ideal-band entry plus/minus the paid rational-to-band form error epsilon sqrt(mass_i mass_R). For the R diagonal use RC246's intersected band input form and the same actual rational error. Thus every frequency cross term remains paid for the chosen rational augmentation.

Recompute four-dimensional row-sum Loewner enclosures and verify positive-definiteness of the frequency and augmented trial-form lower matrices exactly. No same-parity input-column error independence is assumed. The extended representation's complete action-error Gram upper bound is four times the diagonal of its squared column faults; each response evaluation separately uses the complete scalar faults of its own representation.

## Paid inverse and signed-gap estimates

Use the unchanged global positive augmented endpoints mu and nu. With e=O-NVy, the inverse response uses the variational center plus the residual correction. Its upper correction is the complete residual D-energy upper divided by mu. The correlated signed gap uses u=e0-y and subtracts that same residual correction from u*F0u+lambda y*Gy y. Every signed interval cross term remains included.

Exact finite-center least-residual and Galerkin solutions provide proposals, together with rational variations, zero and the preceding four-component upper trial. Their optimality for the actual response is not claimed. The old-center evaluation is intersected with RC245; the extended-center evaluation is then intersected with that result. Both enclose the same actual response, so combining their endpoint bounds is valid.

The final certificate records which center representation supplies each selected endpoint. Each selected trial's own certified endpoint must equal the corresponding accepted final endpoint exactly. Both final upper endpoints come from the old source-center representation. The even lower endpoint comes from the extended representation; the odd lower endpoint comes from the old representation. This avoids attaching a bound to a trial evaluated with different center/error data.

| Certified quantity | Even | Odd |
|---|---:|---:|
| RC245 inverse response upper, rounded upward | 7.395622002 | 9.616684253 |
| RC247 inverse response lower, rounded downward | 0.011438428 | 0.013407513 |
| RC247 inverse response upper, rounded upward | 5.415606202 | 7.063101491 |
| RC247 signed gap lower, rounded downward | -5.327047006 | -6.966018675 |
| RC247 signed gap upper, rounded upward | 0.077120768 | 0.083675302 |

Both upper responses, both signed lower endpoints and both inverse lower endpoints improve. The signed intervals continue to cross zero. These are original-action sources through the positive augmented inverse, not an inverse of the original operator and not the separate canonical metric inverse.

## Fit versus complete uncertainty

For the updated materialized centers, the nominal retained-center minimum residual energies are approximately:

| Source-center representation | Even | Odd |
|---|---:|---:|
| Old degree-64 center | 0.000385527 | 0.000274152 |
| Extended degree-128 center | 0.001002800 | 0.001489696 |

These are midpoint-metric finite-center diagnostics. Complete faults are added separately in the accepted response bounds. The extended source representation has a smaller action-error bound but a larger nominal residual in the current trial spaces; it does not supply the strongest upper response. Materializing the R actions improves their accuracy while changing their centers, so nominal residual diagnostics need not decrease at each such refinement.

The complete original source fault and remaining trial-action faults still limit the estimate after division by the small global mu. Their reduction, a trial shaped to the newly exposed source output, or a stronger valid residual inverse estimate are potential next steps. The current improvements do not determine a number of passes to completion.

## Verification and remaining gate

The validator checks 176 pinned input/helper blobs. Exact replay reverses residual-energy summation and requires certificate equality. Exact checks cover common center dimensions, cross-interval intersections, positive-definite form lower bounds, preservation of the source/first-trial correlation, and matching of the selected endpoint witnesses to the final response endpoints. The pinned four-dimensional nonidentity D control verifies the inverse and signed residual identities with noncommuting operators.

Publication adds the validator, certificate and this note to RC246 while preserving existing repository blobs. The original residual trial span retains its D-form floor 61/250. The separate canonical eight-source metric-inverse width remains 485647/1000000.

Next: sharpen dominant complete source/trial faults or obtain a stronger residual inverse correction. Complete signed positivity still requires all 248 even and 391 odd parameter channels, or an equivalent uniform proof.
