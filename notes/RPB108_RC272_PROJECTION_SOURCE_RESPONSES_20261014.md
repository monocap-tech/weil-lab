# RPB108 — RC272: paid projection-source inverse responses

Parent RC271: `a568390fb3ba6634a4a3142a8055bf92a0e545e2`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC272 evaluates the first two actual auxiliary-source inverse responses for
RC271's rank-608 diagonal projection reference. Each uses four existing polynomial
trials, the complete original-action error certificates, a fresh exact augmentation
form and a projection-aware inverse bound. These are sources P0 and P1, not the
legacy sources N0 P0 and N0 P1. The old positive signed pivots are preserved but
are not transferred to this different response problem.

Neither new native gate lower bound is positive. Both upper bounds are positive,
so these enclosures also prove no negative gate or original negative direction.
Stage I, full coupled positivity, RH, F4 and Lean remain open.

| New source | Actual inverse response upper, approximately | Native auxiliary gate interval, approximately |
|---|---:|---:|
| P0, even | 0.108516697581 | [-0.048726428658, 0.003923980835] |
| P1, odd | 0.036461134964 | [-0.056932372418, 0.004078339145] |

The displayed intervals are explanatory; the certificate contains exact outward
fractions. Gate units are native physical mass, not normalized canonical energy.

## Fresh trial solve in the exact projection metric

The reference is H_P=A_Q+lambda i*P i, and its D-Riesz representative is
N_P=N0+lambda D^-1 P. Its auxiliary metric is exactly diagonal in physical
Legendre coordinates. For each parity use trials

\[
 (P_0,P_2,P_4,R_0)\quad\text{or}\quad(P_1,P_3,P_5,R_1).
\]

The rational R0/R1 inputs are exactly RC242's degree-64 polynomials. All trial
degrees lie in the retained projection range, so PZ=Z for every trial combination.
Thus the new trial form is exactly

\[
 G_{trial}=F_0+\lambda M_{trial},\qquad
 (M_{trial})_{ij}=\sum_n\frac{2B}{2n+1}a_{i,n}a_{j,n}.
\]

F0 is the original-form interval matrix from RC247; M_trial is evaluated as exact
rational arithmetic. No legacy frequency Gram or augmentation comparison error
is used. For source P_b, the exact pairing vector is
f_i=mass(b)*a_i,b. The trial coefficients are the componentwise downward 10^-60-grid
rounding of midpoint(G_trial)^-1 f. This proposes an exact rational trial rather
than treating the midpoint solution as an actual inverse response.

| Coefficient | Even, approximately | Odd, approximately |
|---|---:|---:|
| First native trial | 0.0481653757503 | 0.0458633670227 |
| Second native trial | -0.000451264738243 | -0.000635656508892 |
| Third native trial | -0.000765713280840 | -0.000860298168592 |
| R trial | -0.0148659498507 | -0.0142192211627 |

The full trial Legendre coefficients, exact trial Gram, original-action error
bounds, source pairings and augmented form intervals are materialized in the JSON.

## Actual residual, including all action faults

For an auxiliary source P_b and exact trial Z, set

\[
 e=D^{-1}P_b-N_P Z
   =D^{-1}(P_b-\lambda Z)-N_0Z.
\]

The first term is diagonal and is enclosed using the inherited interval
s_lo<=s<=s_hi in D P_n=(H_n+s)P_n. The retained original-action centers come from
RC245 for P_b, RC237 for P_(b+2), RC240 for P_(b+4), and RC242 for R_b. Degree-64
centers are padded with zeros to degree 128; their complete omitted-output errors
are retained, not silently reduced by padding.

Writing each original-action error bound as E_i in actual D energy, the combined
original-action fault norm is bounded by

\[
 \epsilon_0=\sum_i|y_i|\sqrt{E_i}.
\]

No independence or same-parity orthogonality is assumed. Complete column errors
include their finite coefficient radii, original arithmetic errors and omitted
outputs. The source-diagonal uncertainty from the common actual s is paid
separately. The physical augmentation itself is exact on these trials.

## Retained projection makes the inverse bound sharper

RC271 used theta=1 to prove a positive reference floor. For the same fixed N_P and
lambda=2p, choose a fresh 0<theta<1 in its lower-form proof. RC270's concentration
bound and RC271's physical projection argument give

\[
 G_P\succeq\alpha L+\kappa P,\quad
 \alpha=\gamma-p(1+\theta^{-1})\delta^2>0,
 \quad\kappa=\lambda-p(1+\theta)>0.
\]

Using L>=(32125/230953)D, this gives in D energy

\[
 N_P\succeq a\alpha I_D+\kappa D^{-1}P,
 \qquad a=32125/230953.
\]

The right side is diagonal. Its inverse bounds N_P^-1 from above by operator
order, even though N_P need not commute with that diagonal operator. With an
outward lower floor d=a*alpha and the retained index set I, safe weights are

\[
 w_n=\left[d+\frac{\kappa}{H_n+s_{hi}}\mathbf1_{n\in I}\right]^{-1}.
\]

For retained residual center c and source-diagonal radii r, compute

\[
 V\ge\sum_{n=0}^{128}\mathrm{mass}(n)(H_n+s_{hi})|c_n|^2w_n,
 \qquad
 R\ge\sum_{n=0}^{128}\mathrm{mass}(n)(H_n+s_{hi})r_n^2w_n.
\]

The complete original-action fault uses the global weight 1/d because its entire
location inside or outside the retained projection has not been resolved:

\[
 C\ge\langle e,N_P^{-1}e\rangle_D,
 \qquad C=\left(\sqrt V+\sqrt R+\sqrt{\epsilon_0^2/d}\right)^2.
\]

All roots, floors and final sums are rounded outward. The script searches only
theta=k/100, k=1,...,99, retaining candidates with positive alpha and kappa and
selecting the smallest certified C. The accepted theta is 0.70 even and 0.63 odd.
The fresh reference operator and trial are unchanged by this inverse-bound search.

| Paid inverse-residual bound | Even | Odd |
|---|---:|---:|
| Uniform RC271-floor correction | 0.00726029306344 | 0.00912755824021 |
| Projection-weighted correction C | 0.00254074861591 | 0.00281490107852 |
| Retained-center contribution V | 0.000005321080001 | 0.000006332019315 |
| Complete original-action fault contribution epsilon0^2/d | 0.00231352269725 | 0.00255421992964 |

The combined correction is a squared norm sum, not the sum of the last two rows.
Projection-aware weighting improves the complete correction by factors about
2.86 and 3.24. The original-action fault allowance dominates the present bound.
In particular the refined first-column certificate still pays substantial prime
and endpoint omitted output. A paid global action error does not become a retained
projection error merely because the input trial has low degree.

## Response interval and quantitative remaining budget

The actual inverse response is

\[
 T_b=2\langle P_b,Z\rangle_2-G_P(Z,Z)
       +\langle e,N_P^{-1}e\rangle_D.
\]

The inverse residual correction is added. Evaluating the trial form with exact
interval sign handling gives a variational lower bound and a center upper bound;
adding C gives the actual upper bound. The native auxiliary gate interval then is

\[
 \mathrm{mass}(b)-\lambda T_b.
\]

For these fixed trial centers, a sufficient correction allowance for a positive
gate is approximately 0.000189359378257 even and 0.000188165666059 odd. The current
certified corrections are about 13.42 and 14.96 times these allowances. This is a
concrete error-budget comparison for these particular sources and trials, not a
completion percentage or an assertion that unchanged centers can attain that
budget. Extending the output centers changes the retained residual and must be
recertified together with the remaining action error.

The new source tests are not directly the same quantities as RC267's positive
signed gaps for N0 P0/N0 P1 under the rank-639 reference. RC272 preserves those
results without declaring a superior route or transferring their pivots. It shows
that removing the frequency metric does not alone remove the original arithmetic
action-tail obligation. Only two of the 608 auxiliary sources have been tested,
and the complete same-parity cross response matrix remains unevaluated.

## Reproduction and next step

```bash
python scripts/validate_rpb108_rc272_projection_source_responses.py \
  --output certificates/rpb108_rc272_projection_source_responses.json
python scripts/validate_rpb108_rc272_projection_source_responses.py \
  --output certificates/rpb108_rc272_projection_source_responses.json --replay
```

All 251 inherited blob pins are verified. Replay reverses dependency traversal,
the Young-parameter search and output summation, then compares the complete
certificate exactly. Exact finite controls check the diagonal inverse-order error
payment and retain RC271's noncommuting bridge, nullity and added-covariance
controls. These are analytic/exact-arithmetic certificates, not Lean proofs.

Next: extend or sharpen original-action omitted-output bounds for these new trial
combinations, separating the part inside the retained projection from the part
beyond it. Pay their inverse-weighted covariance before accepting a positive
source gate, and then address the full coupled source range. The inherited
original below-0.01 count ceiling 608, nonpositive ceiling 582 and separate
eight-source inverse width 485647/1000000 are unchanged.
