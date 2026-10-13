# RPB108 — RC173: actual canonical inverse response and full residual

Aperture 11/10. Parent RC172: `f5ed7ad1a9144577e96ee76cb1b6161da9d989c3`.
Only `research/rpb108-route-consolidation` is written. Historical checkpoints, the seven-source reference frame and Lean remain unchanged.

RC173 converts the paid P0/P2 canonical actions into an actual canonical inverse-response enclosure. Its accepted uniform width is 0.296983 times source D-energy, so the tested two-source half-Gram gate passes. The finite residual, both infinite endpoint tails, mixed errors and the actual inverse-residual correction are paid. This response uses L, not the reference P or original augmentation Hhat.

| Certified quantity | Sufficient upper |
|---|---:|
| Canonical response enclosure width relative to source D Gram | 0.296983 |
| Vector-trial canonical error energy relative to source D Gram | 0.315858 |
| Vector-trial D-error energy relative to source D Gram | 2.270762 |
| Vector-trial canonical error norm relative to the true image norm | 0.288212 |

The two energy rows are squared error-norm bounds for represented vectors, not matrix widths. The final row is a separately paid warm-start norm bound. This pass has not executed a high-accuracy canonical Riesz iteration. Rejection at the immediately preceding 10^-6 grid point proves the reported width is minimal for the selected enclosure on that grid, not an actual lower bound on inverse uncertainty or an optimum over all possible trials.

## Source, trial and exact identity

Let S=[P0,P2], M=D^-1 L on D energy, G=S^*DS and K=S^*LS. RC121 proves aI<=M<=2I on the full supported form domain, with a=32125/230953. RC172 supplies K's actual full correlated enclosure and the two action trials V=[v0,v2], with their complete D-error Gram upper. The source Gram is exactly diagonal in these symbolic vectors and retains the actual s enclosure.

Choose the rational matrix Y from a 10^-30 rounding of K_mid^-1 G_mid. It is an arbitrary valid vector trial; no equality with the true inverse is assumed. Set y=S Y and r=S-M y. Exact expansion gives

\[
\Sigma=C_Y+r^*D M^{-1}r,
\quad C_Y=GY+Y^*G-Y^*KY.
\]

The residual correction is added. The equivalent correlated Gram functional

\[
C_Y=G-(I-Y)^*G(I-Y)+Y^*(G-K)Y
\]

lets the validator use full G and K Loewner enclosures without replacing signed mixed terms by independent scalar energies. The actual variational lower C_lo is PSD. Using 1/2 I<=M^-1<=a^-1 I and full residual bounds R_lo<=r^*Dr<=R_hi gives

\[
C_{lo}+\tfrac12R_{lo}\preceq\Sigma
\preceq C_{hi}+a^{-1}R_{hi}.
\]

Exact rational checks also show that the selected enclosure improves the structural [G_lower/2, a^-1 G_upper] bounds.

## Full finite and infinite residual

The nominal residual is r_hat=S-VY. All coefficients through even degree 4094 are evaluated with directed arithmetic. The polynomial regular trials end at degree 256. Beyond that, their nominal canonical actions retain actual endpoint coefficients:

\[
(v_0)_n=\eta_n,\quad
(v_2)_n=\eta_n\frac{n(n+1)}{n(n+1)-6},
\quad \eta_n=\frac{2n+1}{n(n+1)(H_n+s)}.
\]

Thus, for each inverse-trial column, the tail is -eta_n[b_i+delta_n c_i], with b_i=Y_0i+Y_1i, c_i=Y_1i and delta_n=6/[n(n+1)-6]. These signed coefficients are combined before bounding. The complete eta-tail energy after degree 4094 is paid by the inherited monotone width-two-cell bound T. With delta_n<=delta_first and any positive t,

\[
N_{tail}\preceq(1+t)T b^*b
 +(1+1/t)T\delta_{first}^2 c^*c.
\]

The implementation chooses t=1/1000. The finite-prefix Gram supplies a full nominal residual lower N_lo; its weighted Loewner upper plus the tail matrix supplies N_hi. Both correlations and every omitted degree remain visible.

If E is the full action-error Gram after congruence by Y, Young's inequalities give

\[
r^*Dr\preceq(1+\tau)N_{hi}+(1+1/\tau)E,
\]

\[
r^*Dr\succeq(1-\sigma)N_{lo}-(1/\sigma-1)E
\quad(0<\sigma<1).
\]

The lower is accepted only when exact PSD checks pass; a zero residual lower remains an available candidate. These inequalities require no sign, orthogonality or statistical assumption about the two action errors.

The selected enclosure uses upper tau=1/100 and lower sigma=1/30. Thirty-five paid candidate combinations are evaluated and compared by exact rational PSD. The selected upper-minus-lower is bounded by 0.296983 G_lower; the full half-Gram gate matrix is stored and accepted exactly. Replay reverses the entire finite residual sum and candidate traversal.

## Vector-error interpretation and remaining work

The represented trial S Y approximates the canonical Riesz image of the physical dual inputs D S. Its D-error Gram is at most R_hi/a^2 and its canonical-error Gram is at most R_hi/a. Both are stored. The midpoint of the response matrix is not a realized inverse-vector map, so no vector-accuracy conclusion is inferred from half the matrix interval width.

An additional exact PSD comparison proves that the canonical-error Gram upper is at most 0.083066 times the selected response lower, hence at most 0.083066 times the true Riesz-image Gram. Taking an outward square root gives uniform canonical norm error below 0.288212 times the true image norm. This is an actual represented two-source warm start, with all complex mixtures and its full residual paid. It follows from the error comparison, not the half-Gram response gate. Successive correction actions and final stopping tolerance remain to be certified.

This pass validates the current actions as an actual canonical inverse-response tool on two sources. The required whole physical source family, its map errors and final tolerance still need coverage. The P0/P2 source space is not the historical seven-source reference space or the original augmentation adjoint range. Enriching inverse trials in the measured residual directions and extending paid polynomial/enriched-source actions are concrete next options.

Stage I's prescribed numerical tolerance remains unspecified. Full seven-source canonical inversion, original Weil/augmented actions, original response below one, whole-aperture positivity, Global/F4, RH and Lean closure remain unclaimed. The original augmentation criterion is unchanged and cannot use L^-1 in place of Hhat^-1.

## Reproduction

Run `python scripts/validate_rpb108_rc173_canonical_inverse_response.py --output certificates/rpb108_rc173_canonical_inverse_response.json certificates/rpb108_rc172_quadratic_regular_action.json certificates/rpb108_rc171_regular_legendre_projection.json certificates/rpb108_rc121_diagonal_metric_equivalence.json certificates/rpb108_rc129_four_vector_joint_moment.json`. Repeat with `--replay`. Only additive RC173 validator, certificate, terminology and note files are committed.
