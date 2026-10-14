# RPB108 — RC244: four-trial response with certified residual actions

Date: 2026-10-14 UTC. Parent RC243: `43522d039f456eace818be86cee8544d585addca`. Branch: research/rpb108-route-consolidation. Aperture B=11/10.

RC244 evaluates the same original-action inverse sources N0 P0 and N0 P1 using four certified response trials per parity. The trial spaces are span{P0,P2,P4,R0} and span{P1,P3,P5,R1}. The residual-shaped trials have complete original actions from RC242 and complete rational augmented actions from RC243.

The fully paid inverse-response upper bounds improve by about 64–66%, while the nominal retained-center residual energies improve by about 99%. Both signed-gap intervals still cross zero. Full signed positivity, original whole-space positivity, the full auxiliary norm gate, Stage I, RH, F4 and Lean remain open.

## Complete action inputs and common center representation

The original and augmentation faults on P0–P3 retain the RC238/239 refinements. The P4/P5 actions retain RC240. The R0/R1 columns retain RC242/243. No new complete operator actions are claimed here; this pass combines existing certified columns into a response calculation.

Use a common retained-center output array through degree 128. Older degree-64 centers are extended by exact zero coefficients solely to represent their existing finite approximations on this common array. Their complete omitted-output errors are preserved. Zero padding does not assert that the actual operator output vanishes above degree 64. The R columns retain all their certified degree-128 centers.

The response sources remain two. Four trials per parity and eight certified action inputs in this cohort are not eight inverse-response sources and do not evaluate the entire 639-dimensional signed criterion.

## Actual original and frequency cross terms

Retain the old three-by-three original trial form and rational frequency Gram interval blocks exactly. For each new original cross entry, pair the exact input polynomial with the retained original action coefficient intervals and actual D-weight intervals. Both the low-degree polynomial inputs and R inputs have degree at most 64, so every omitted projected output is orthogonal to the input in this pairing. Add the full regular-kernel, prime-arithmetic and pole-Taylor model faults. Intersect the two transposed evaluations using actual original selfadjointness.

The new R diagonal original form interval must equal its RC242 interval exactly. Original-action tail errors remain paid in inverse residuals even though they do not enter these orthogonal form pairings.

For a frequency cross entry between R=sum a_n P_n and an old P_j trial, sum a_n times the already materialized ideal-band column G_(n,j) through the complete input degree 64. All signs of a_n enter the interval sum. The R diagonal ideal-band form comes from its exact physical energy minus the RC243 aggregate outside-band energy. Every cross entry then pays the actual rational-to-band operator error epsilon sqrt(mass_i mass_j). Thus the chosen rational frequency Gram is enclosed, not replaced by its ideal-band comparison.

Symmetric row-sum radii give four-by-four Loewner bounds. The lower frequency Gram and the lower augmented trial form F0+lambda Gy are checked positive definite exactly. All same-parity form cross entries are retained. Complete action errors are not assumed orthogonal: their joint error Gram is bounded by four times the diagonal of their squared error bounds.

## Fully paid residual and signed gap

For O=N0 P_base and the four-component trial Z=Vy, let e=O-NZ. The original source shares its first original action with the P_base trial, so its full fault contribution has coefficient |1-y0|. All remaining original faults have coefficient |y_i|, and all augmentation faults have coefficient |y_i|. Add these full-output fault norms before enclosing residual energy by forward/reverse triangle inequalities in the actual D metric.

The inverse response uses the same positive actual augmented inverse endpoints mu and nu:

\[
\langle O,N^{-1}O\rangle_D
=C_Z+\langle e,N^{-1}e\rangle_D,
\qquad
\|e\|_D^2/\nu\le\langle e,N^{-1}e\rangle_D
\le\|e\|_D^2/\mu.
\]

The correction is added. For the correlated signed gap, with u=e0-y,

\[
\Delta=u^*F_0u+\lambda y^*G_y y-
\langle e,N^{-1}e\rangle_D.
\]

Only in this expression is the residual correction subtracted. All entrywise interval quadratics pay signed same-parity cross terms. Candidate trials include nominal least-residual and Galerkin proposals, rational interpolations and scalings, zero, and the full previous three-component upper trial with a zero R coordinate. Candidate generation does not prove actual-response optimality. New certified intervals are intersected with RC240.

## Fit diagnostics and results

Exact finite-center least-squares calculations compare the old three-dimensional span and the enriched four-dimensional span on the same degree-128 center arrays and midpoint D weights. These diagnostics are not actual full-output residual energies: complete action faults are paid separately in the certified response.

| Nominal retained-center minimum residual energy (approx.) | Even | Odd |
|---|---:|---:|
| Three trials | 0.016083214 | 0.016958340 |
| Four trials | 0.000165516 | 0.000128304 |

The chosen upper-bound trials give R coefficients approximately 0.46467 even and 0.46579 odd, while adjusting the old three coefficients. The large improvement in fit does not remove the inherited original-source uncertainty or the complete new augmentation action faults. Those faults now account for most of the gap between the nominal fit and the certified response estimate.

| Certified quantity | Even | Odd |
|---|---:|---:|
| RC240 inverse response upper, rounded upward | 23.389542374 | 29.021020187 |
| RC244 inverse response lower, rounded downward | 0.011438135 | 0.013401437 |
| RC244 inverse response upper, rounded upward | 8.055899798 | 10.432433658 |
| RC244 signed gap lower, rounded downward | -7.967340602 | -10.335350842 |
| RC244 signed gap upper, rounded upward | 0.077121061 | 0.083681379 |

Both upper bounds and both signed lower bounds improve. Neither parity certifies a positive signed gap or an actual negative original direction. The RC241 tuning obstruction remains valid for its fixed three-trial interface; this calculation uses a different four-trial interface and therefore does not contradict it.

## Verification and remaining work

The validator checks 167 pinned input/helper blobs. Exact replay reverses full retained-center residual summation and requires certificate equality. Exact checks establish symmetry intersections, preservation of the old form blocks, equality of the new original diagonal with RC242, positive-definite frequency and augmented form lower bounds, and monotonic nominal least-squares improvement under trial enlargement. An independent four-dimensional control verifies the residual and signed-gap identities in a nonidentity D metric with noncommuting original and augmented operators, including all four trial coordinates. The inherited rational quadratic and metric controls remain pinned.

Publication adds the validator, certificate and this note to RC243 while preserving existing repository blobs. The original residual trial span retains the RC242 D-form floor 61/250. The separate canonical eight-source metric-inverse width remains 485647/1000000.

Next: reduce the full original-source and residual-trial augmentation uncertainties, or certify a further residual-shaped action or stronger inverse correction. The fit gain identifies a useful direction but does not predict the number of passes to completion. The complete signed criterion still requires all 248 even and 391 odd parameter channels, or an equivalent uniform proof.
