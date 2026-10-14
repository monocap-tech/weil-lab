# RPB108 — RC233: actual augmented inverse-response enclosures

Date: 2026-10-14 UTC. Aperture B=11/10. Branch: research/rpb108-route-consolidation. Parent RC232: `fc15a9534376d43e6fb7a60b2543593f3e4c417f`.

RC233 encloses the inverse-response Gram of the **actual RC115 rational augmentation** on the two actual canonical native moment/Riesz sources r0=i*P0 and r1=i*P1. It uses RC232's complete original-plus-augmentation action enclosures, the actual D metric, and the signed variational identity with its added inverse-residual correction. No ideal band inverse replaces the rational augmented inverse.

| Actual canonical source | Augmented inverse response lower | Upper | Generic spectral upper, approximate | Certified upper improvement factor, rounded down |
|---|---:|---:|---:|---:|
| r0, even | 0.1635278206 | 1.3274008190 | 422.613106 | 318.37 |
| r1, odd | 0.0505098736 | 1.0927793471 | 117.321334 | 107.36 |

Response interval endpoints are rounded outward; exact fractions are in the certificate. The comparison is against a generic global spectral enclosure, not a previously measured inverse-response error. The off-diagonal response is exactly zero by parity, so the two diagonal bounds enclose the whole two-source response Gram for every complex coefficient vector.

These are valid but broad **inverse-response enclosures**, not a passed positivity or auxiliary norm gate. Their validation succeeds; Stage I does not close. Dense frequency Grams, full-range auxiliary responses, numerical canonical Riesz images, and iterative inverse solutions are not computed. RC228's canonical metric inverse width 0.485647 remains a different preserved result.

## Exact sources and operator bridge

Let Q=[P0,P1] map two coefficient channels to the physical polynomial sources. These degree-zero and degree-one Legendre polynomials equal the corresponding Chebyshev moment polynomials. The actual canonical source map is S_c=i*Q, not Q itself as a physical polynomial map. Its columns are the genuine Riesz representatives of the native moment functionals.

Let R=D^-1 Q be the same physical functionals represented in D energy. RC230 proves on the full common form domain

\[
 N=M\widehat H,\qquad
 S_c=M^{-1}R,\qquad
 \widehat H^{-1}S_c=N^{-1}R.
\]

M is the canonical form's D-Riesz representative and Hhat is the fixed rational positive augmentation. The inverse response therefore satisfies the exact metric identity

\[
 \boxed{S_c^*\widehat H^{-1}S_c=R^*D N^{-1}R.}
\]

Indeed, the canonical inner product is the D inner product with M in its first pairing, so the factor M cancels the M^-1 in the source. No commutation of M and N is assumed. This is why the response can be certified without first numerically realizing the canonical source images.

RC230 proves that these native sources belong to the complete chosen augmentation's adjoint range. It does not supply normalized auxiliary frequency preimages for them. The present two-source Gram is therefore not the full frequency-space response matrix lambda Fhat N^-1 D^-1 Fhat*. Physical moment-source normalization must not be substituted for the frequency metric.

## Signed response and full residual contracts

For a physical polynomial trial map Y, define e=R-NY. The actual variational center is

\[
 C_Y=Q^*Y+Y^*Q-Y^*DNY.
\]

Expanding the square gives

\[
 \boxed{R^*DN^{-1}R=C_Y+e^*DN^{-1}e.}
\]

All pairings use the actual physical, D, or canonical metric designated by the formula. If mu I<=N<=nu I in D energy, then

\[
 \nu^{-1}e^*De\preceq e^*DN^{-1}e
 \preceq\mu^{-1}e^*De.
\]

The correction is **added**, never subtracted. An upper residual Gram supplies an upper correction; it cannot be used as a lower residual Gram.

The validator includes an exact two-dimensional control with a nonidentity D metric, nonorthogonal source columns and a nonzero correlated residual. It verifies the entire matrix identity and both residual sandwiches. Subtracting the correction fails exact equality. This structural control is not an arithmetic Weil computation; the actual action inputs are the pinned RC232 certificates.

## Actual polynomial trial calculation

For source P_j, j=0,1, the response trial is Y_j=tP_j with t>=0. Its source pairing is exactly Q_j*Y_j=t m_j, m_j=2B/(2j+1). RC232 encloses the actual augmented form F_j=<P_j,NP_j>_D between f_lower and f_upper. Thus

\[
 2tm_j-t^2f_{\rm upper}\le C_t
 \le2tm_j-t^2f_{\rm lower}.
\]

Let A_j be RC232's finite degree-64 polynomial action center, with complete actual error ||NP_j-A_j||_D^2<=E_j. Its error includes original arithmetic, rational augmentation comparison, output truncation, and all finite coefficient uncertainties. RC233 does not add those coefficient radii a second time or omit them.

The exact D source is R_j=P_j/(H_j+s). The actual s interval produces a rational source center gP_j and a paid source-rounding error E_source. For the finite residual center v=gP_j-tA_j, the actual D-energy lower and upper weights give

\[
 v_{\rm lo}^2\le\|v\|_D^2\le v_{\rm hi}^2.
\]

The full residual differs from v by at most

\[
 \delta_t=\sqrt{E_{\rm source}}+t\sqrt{E_j}.
\]

Therefore the **full**, not compressed, residual energy is enclosed by

\[
 \max(0,v_{\rm lo}-\delta_t)^2
 \le\|R_j-tNP_j\|_D^2
 \le(v_{\rm hi}+\delta_t)^2.
\]

Every square root used on an upper bound is rounded upward. The square root on the nominal lower bound is rounded downward before the reverse triangle inequality is applied. The source and action errors are combined in norm; no correlation or orthogonality between them is assumed. The complete action error pays the infinite output omitted from A_j.

Combining the signed center bounds and residual sandwiches supplies a response lower and upper for each exact trial t. The generic independent source-energy sandwich is also retained:

\[
 \frac{m_j}{\nu(H_j+s_{\rm upper})}
 \le R_j^*DN^{-1}R_j
 \le\frac{m_j}{\mu(H_j+s_{\rm lower})}.
\]

The final scalar intervals are intersections of these independently valid enclosures. Different trials may supply the best lower and best upper; they need not be the same trial for their bounds on the same exact response to intersect.

## Exact selection and what the widths mean

The nominal least-residual proposal t0 is the exact rational minimizer of the finite center residual using the midpoint D weights. It is only a proposal: actual acceptance uses the complete paid bounds above. The code evaluates 101 rational multiples k t0/100 for k=50,...,150, the two variational proposals m_j/f_upper and m_j/f_lower, and zero. It chooses bounds deterministically with exact rational comparison. No globally optimal trial or exact solution is claimed.

The selected upper trials have t approximately 0.0769981554 even and 0.0730630758 odd. Their certified full residual energy uppers are approximately 0.0015772673 and 0.0013484296. Division by the small global N lower endpoints still gives a substantial inverse correction. The final response widths are approximately 1.163873 even and 1.042270 odd.

Those widths are enclosure costs, not actual-error lower bounds or negative Weil witnesses. A small nominal residual alone would not suffice; RC232's augmentation and omitted-output error remain paid. The reverse-triangle lower residual may vanish, so no actual obstruction to better response trials is inferred from the present upper costs.

No half-width target from the different canonical M inverse has been imposed on these Hhat responses. The useful completion criterion remains the full selected auxiliary response strictly below its **actual frequency-space identity**, not any threshold applied to these physically normalized moment-source numbers.

## Coverage and next step

N, its inverse and both source/trial maps preserve reflection. Thus the complete inverse-response pairing between the even and odd sources is exactly zero. The diagonal response intervals consequently give a Loewner enclosure on all complex combinations of r0 and r1. This is a genuine actual augmented inverse-response certificate, although it covers only two native moment sources.

Still open are a sufficiently tight response realization on the entire chosen range, its actual auxiliary metric or an equivalent metric-free uniform norm certificate, the full norm below one, and Stage I assembly. The complete rank is still 639, but this does not prescribe 639 separate solves or a dense Gram. Neither source membership in the range nor the two-source enclosure proves full-range exhaustiveness.

The next focused work is tighter/materialized rational or band-comparison augmentation actions and richer actual response trials, followed by full-range residual and frequency-metric contracts. Increasing a trial count alone is not a completion certificate. No original positivity, Stage I, F4, Lean or RH conclusion is made.

## Reproduction and publication

Generation verifies every input Git blob pin and performs only exact rational arithmetic for acceptance. Replay reverses pin and residual accumulation order and requires equality with the complete certificate. The abstract correlated control, actual source constants, action errors, global inverse endpoints and signed response enclosures are all rechecked.

```bash
python scripts/validate_rpb108_rc233_augmented_inverse_response.py --output certificates/rpb108_rc233_augmented_inverse_response.json
python scripts/validate_rpb108_rc233_augmented_inverse_response.py --output certificates/rpb108_rc233_augmented_inverse_response.json --replay
```

Publication adds only this note, the validator and its certificate. An expected-head non-force update and remote comparison/tree readback verify preservation of existing blobs. Conflict-marker checks apply to the three additions, not all historical content.
