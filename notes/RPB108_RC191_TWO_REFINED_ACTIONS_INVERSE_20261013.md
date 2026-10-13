# RC191: five-source inverse with both refined complete action carriers

Parent: RC190, `060f4476d36f50f4aee22cd651d08ae145a79ece`.

RC191 attaches the improved w14 endpoint and regular carriers to the canonical inverse, retaining RC188's refined psi0 carrier. Full mixed rows and residuals are rebuilt. The certified width decreases from1.654087 to1.254303 on the same five response sources and the same source-Gram normalization. The half-Gram gate remains failed, with acceptance ratio2.508606.

## Correct complete w14 action attachment

The native w14 source is unchanged. The RC190 materialized carrier bytes and retained native-source hash are checked. Its finite endpoint centers extend through65534, its centered native input tail begins at32768, and its new regular output polynomial extends through1536. The full w14 action-error norm upper is0.000016950765.

The negative-r finite correction remains inherited on0..4094, and its analytic correction remains exact on every native tail degree>=4096. The centered half-source addition starts only at32768; the old4096 centered cutoff is not reused with the new endpoint input.

Above65534, write the native source amplitude as A_w(n), and the new endpoint output amplitude as B_w(n). The represented w14 action is

\[
 \eta_n\left((3/2-r/D_n)A_w(n)+B_w(n)\right).
\]

The two moment systems have different roles. A_w uses the native fifteen moments and scale977132. B_w uses the twenty-five RC190 endpoint moments and scale32766*32767. The new B_w tail contributes to every complete source/action and represented action/action upper, rather than being assigned zero.

## Rebuilt source geometry, mixed rows, and residual tails

All finite source/action, represented action/action, residual, and trial/residual cross terms are recomputed through degree65534. The native source Gram remains the same target, and the five-source normalization endpoints are held identical to RC189's.

Actual canonical first-moment intervals intersect both independently paid directional estimates with available historical actual intervals. The full six-trial source Gram lower is verified positive after the paid coordinate change. Rational least-residual trial coefficients are selected anew from the updated represented geometry; the RC184 coefficient matrix with a zero q185 row remains the baseline control.

The new endpoint zeroth moment changes the w14 leading residual coefficient from c_w mu_0 to c_w mu_0+omega_0. Its higher endpoint moments are added to the w14 product remainder. Since both act on the same w14 coefficient row, their absolute amplitude bounds are merged before paying the four variable residual terms. The existing shared native-w14-source/f0-action cancellation and the entire negative-r factor range are retained.

The raw-trial and response-column action-error matrices are rebuilt using RC188's psi error and RC190's w14 error, together with the unchanged other complete action errors. All mixed errors are paid for every complex response mixture; none are declared orthogonal.

## Correlated variational enclosure and comparison

RC187's simultaneous matrix Young method is retained for the actual-action uncertainty and disjoint infinite trial/residual cross terms. Whole valid inverse lower/upper combinations are tested against the inherited RC189 and structural bounds. No entrywise matrix optimization is used.

| Same five response sources | Variational width upper | Inverse width upper | Gate |
|---|---:|---:|---|
| RC189 selected enriched trial, old w14 action | 1.074989 | 1.654087 | Failed |
| RC191 baseline control | 0.635209 | 1.654087, retained | Failed |
| RC191 enriched trial, selected | 0.793260 | 1.254303 | Failed |

The selected enriched inverse endpoints both use the new refined construction. Its variational action parameter is1/100, its tail parameter1/3, and its residual upper parameter1; the residual lower is zero. Its nominal residual squared-error factor is0.029947 relative to G_lower. The represented residual and its selected coefficients changed with the action carrier; that nominal factor is separate from the improved actual inverse width.

For the local inverse-width threshold1/2,

\[
 \rho\le 1.254303/(1/2)=2.508606,
 \qquad \text{guaranteed margin}\ge-0.754303.
\]

The contract has no positive acceptance margin. An independent exact evaluation of the stored gate with RC184's rational source witness x=(-1/120,3/50,-14/25,-26/25,1) gives x*H*x<-0.00018446596. Thus the selected enclosure still fails the gate. It does not establish an impossibility result or an intrinsic uncertainty lower bound.

## Remaining witness-direction error budget

For the selected coefficients Y and that same x, the direct bound on the actual-to-represented trial-action error is the sum of |(Yx)_i| epsilon_i. An exact rational calculation gives the following outward upper payments:

| Raw trial direction | D norm payment upper |
|---|---:|
| P0 | 0.000003697005 |
| P2 | 0.000090350315 |
| f0 | 0.000156022791 |
| psi0 | 0.000020517443 |
| w14 | 0.000043571954 |
| q185 | 0.000017685097 |

Their exact sum is below0.000331844603. The f0 and P2 terms comprise about74% of this chosen bound. This is single-witness bound accounting, not74% of true error or of the full inverse width. It identifies their inherited regular-action carriers as concrete next precision candidates. The q185 endpoint output tail is also a candidate for analytic-moment retention instead of the existing coarse omitted-output payment.

## Verification and scope

Twenty-eight inputs are hashed: RC190 main and its materialized carrier, RC189, and RC189's twenty-five historical inputs. Carrier bytes, native source custody, full error bounds, and parent ancestry are checked. Exact replay reverses finite sums, trial order, and the variational and residual parameter searches; the entire JSON must reproduce exactly.

Run:

```
python scripts/validate_rpb108_rc191_two_refined_actions_five_source_inverse.py --output certificates/rpb108_rc191_two_refined_actions_five_source_inverse.json
python scripts/validate_rpb108_rc191_two_refined_actions_five_source_inverse.py --replay --output certificates/rpb108_rc191_two_refined_actions_five_source_inverse.json
```

Next: tighten the inherited f0/P2 regular-action payments and evaluate analytic retention for q185's endpoint output tail, then rebuild the same five-source inverse. Required acceptance remains a certified matrix inequality; a particular number of remaining passes is not guaranteed.

The accepted four-source result and native source frame remain intact. Native v10,z_b6,t10 action/inverse coverage remains open. Original augmented Weil floor and auxiliary-response targets, Stage I, whole-aperture original Weil positivity, RH, F4, and Lean remain open/unclaimed.
