# RPB108 RC99 — Signed source entries and the projection interface

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC98, commit `168430a74d3f831f3b4ee6e225a3f033c0329eae`.
Aperture B=1.10. Actual sufficient canonical Riesz head rank 1250.

RC99 encloses the four signed physical mixed source-residual entries requested after RC98. Their signs are rigorous. It then converts the complete three-input source Gram uppers into valid intervals for the unknown actual projected covariance entries. This narrows the RC98 intervals, but does not certify the six-dimensional corrected span.

The central interface distinction is now explicit: a signed physical residual Gram upper is a Loewner upper for the projected covariance, not an entrywise approximation to it. Its off-diagonal sign cannot simply be assigned to the projected entry. RC99 supplies the correct polarization bounds and an exact sharp counterexample to that inference.

All six selected directions remain individually corrected-positive from RC94/95/98. Their whole span, strong coverage, full positivity and Global/F4 remain open.

## Four mixed physical entries

For each parity use the actual trial/input combinations weak_0, weak_1 and positive_control. Let F_i=q_i+K_nom V_i be their nominal complete original sources. Subtract the fixed physical Legendre capture below degree 64, using the existing pairing centers, to obtain r_i.

RC99 contracts the complete signed RC68 source Gram and RC83 pairings before taking a matrix bound. It encloses the physical mixed residual entries <r_i,r_control>:

| Parity | Mixed weak input | Physical nominal residual entry, display | Certified sign |
| --- | --- | ---: | --- |
| Even | weak_0 | about -1.28650e-14 | Negative |
| Even | weak_1 | about 1.2428202e-12 | Positive |
| Odd | weak_0 | about 1.2663359e-12 | Positive |
| Odd | weak_1 | about -1.459286822e-10 | Negative |

The JSON contains exact rational interval endpoints. These are nominal physical entries, not actual canonical projected covariance entries. Actual-source approximation and Riesz-error terms are attached collectively below. No new source integration is needed.

## 1. Common three-input residual Gram

Let U_ij be the nominal complete source entry center, h_ni the physical source pairing center against P_n, and m_n=R/(2n+1). The fixed polynomial subtraction yields the residual center

    W_ij = U_ij − sum_(n<64) h_ni h_nj / m_n.

Its paid radius is the contracted source-entry radius plus

    sum_(n<64) [|h_ni| radius_nj + |h_nj| radius_ni] / m_n.

Because the subtraction uses fixed center coefficients, this is an exact linear error attachment; no pairing-radius square is omitted from the defining residual identity.

Weighted symmetric row bounds on all six same-parity entries produce a common positive-semidefinite physical residual Gram upper W_upper. The interval scales are (100,1,1) even and (80,1,1) odd. A corresponding common three-input nominal operator-residual upper is contracted from RC81 before row inflation and attached to the actual physical Riesz-error matrix.

The physical subtraction degree is 64; the canonical projection rank remains 1250. Since the subtracted polynomials map into H1250, RC95's tau1250 bound gives

    N = tau1250² W_upper.

RC89's remainder-transfer bounds scale by tau1250/tau38, as in RC98. With rho=252/257 and nu=1/65536,

    Ep = rho² [(1+nu) E_nom,upper
                + (1+1/nu) delta_L² T_trial],
    E = rho(1+nu) k1250² Ep
        + (1+1/nu) delta_K² tau1250² T_trial.

For every tested positive rational t, the actual projected covariance obeys

    0 <= Gamma1250 <= A(t)=(1+t)N+(1+1/t)E.

All operators and uncertainties are paid on the common three-input block. Signs are retained in its off-diagonal entries before matrix bounds. Exact row-sum Loewner rounding on a 1e-40 grid prevents unnecessary denominator growth; its matrix inflation is checked and does not rely on floating tolerance.

## 2. Correct Loewner-to-entry polarization

For any positive-semidefinite covariance Gamma and upper A with 0<=Gamma<=A,

    (A_ij − sqrt(A_ii A_jj))/2
      <= Gamma_ij
      <= (A_ij + sqrt(A_ii A_jj))/2.

To prove the upper, apply the upper quadratic bound to

    sqrt(s) e_i + e_j/sqrt(s),

and the nonnegative lower quadratic bound to the corresponding minus vector. Their difference gives

    Gamma_ij <= [s A_ii + A_jj/s + 2 A_ij]/4.

Minimizing over s>0 gives the displayed upper; the lower follows by changing the sign of e_j. A zero upper diagonal forces the relevant row to vanish, giving the same limiting formula. Outward rational square roots make both endpoints safe.

These intervals are generally biased toward the sign of A_ij, but always include zero. Thus they can narrow uncertainty without certifying a nonzero sign. The physical nominal residual sign alone supplies no lower projected energy.

An exact example makes the distinction sharp. For

    A = [[1,3/5],[3/5,1]],

both projected covariances

    Gamma_plus  = [[4/5,4/5],[4/5,4/5]],
    Gamma_minus = [[1/5,-1/5],[-1/5,1/5]]

satisfy 0<=Gamma<=A. Their cross entries attain the polarization endpoints 4/5 and -1/5. The upper A has positive cross entry, while an allowed Gamma has a negative cross entry. Exact PSD tests certify all four required matrices. This is a finite algebra example; it is not a model of the original arithmetic source.

## 3. Intersect with the existing actual diagonal bounds

RC98 already gives a positive control diagonal upper g for Gamma1250, and RC94/95 give a weak-pair covariance upper G. Therefore each actual mixed covariance also obeys the scalar PSD Cauchy interval

    -sqrt(G_ii g) <= Gamma_i,control <= sqrt(G_ii g).

RC99 intersects those intervals with the polarization intervals from ten valid rational Young choices. Every inequality applies to the same actual covariance, so intersection is legitimate even though the optimal parameter differs between entries. The computation does not claim that this grid exhausts all possible projected-covariance estimates.

The resulting interval width ratios, relative to the prior Cauchy bounds, are:

| Parity | weak_0/control | weak_1/control |
| --- | ---: | ---: |
| Even | 0.92750847 | 0.73455699 |
| Odd | 0.56417375 | 0.56769405 |

Thus even widths fall by about 7.25% and 26.54%; odd widths fall by about 43.58% and 43.23%. The projection interface does recover some useful signed information. It does not recover a signed approximation to the actual projected entries.

## 4. Six-mode completion remains unresolved

Use the retained corrected weak lower L and positive added diagonal lower d from RC98. Subtract the newly enclosed projected mixed covariance from the signed original head entries to enclose the corrected cross vector c. As before, the robust rectangular sufficient condition is

    d > max_(box vertices) c* L^(-1) c.

The maximum occurs at a vertex because the inverse quadratic is convex. Exact evaluation gives worst penalty-to-diagonal ratios:

| Parity | RC98 box | RC99 intersected box |
| --- | ---: | ---: |
| Even | 16.71647719 | 14.38104495 |
| Odd | 2780.16877343 | 2591.61231336 |

Neither three-mode robust box passes. These negative margins are values of relaxed enclosure matrices. Their vertex covariances need not satisfy all joint Loewner constraints or be realizable by the original operator. No actual negative or null direction is proved.

A common signed Gram upper has therefore helped but has not closed the missing correlation estimate. No new six-dimensional positive-subspace certificate is obtained, and the nonpositive spectral-dimension upper remains 1246.

## 5. Full weak-block covariance gives an ellipsoid

Let x be the actual two-component mixed coupling vector. Since the complete coupling covariance is positive semidefinite, Gamma_weak<=G and Gamma_control<=g imply

    [[G,x],[x*,g]] >= 0,
    x* G^(-1) x <= g.

This retains the weak-pair correlation and is stronger than treating the two entries as independent scalar Cauchy bounds. If the exact rational test gives G<=lambda L, then

    x* L^(-1) x <= lambda g.

After the alpha^(-1) correction, the pure source contribution is bounded above by lambda g/alpha². Relative to the added corrected diagonal d, that upper is approximately 6.569477 even and 1544.721136 odd.

These are sufficient upper estimates for an interaction, not lower bounds on actual coupling. Their size alone does not prove a necessary obstruction or exclude cancellation with the original head cross. RC99 does not evaluate the full head-plus-source ellipsoid optimization. It records the matrix-correlated source bound to define a more faithful target than the rectangular relaxation.

## 6. Next theorem-facing target

The missing information concerns the projected source itself. A sharper physical tail estimate at rank 1250, shared across the three inputs, could reduce the common covariance upper enough for a direct matrix Schur test. Alternatively one can certify projected canonical responses or the combined inverse-weighted corrected cross, including head/source cancellation.

The structural RC95 jump/weighted-derivative argument is a candidate for a common three-input tail, but its extra control derivative entries and the odd jump profile require new certification. They cannot be inferred by copying the four current nominal physical signs into the canonical covariance.

The investigation should now target that projection-sensitive correlation. Another improvement to an isolated positive diagonal would not address the demonstrated gap. Dense evaluation of the complete 1250-head is not required by any test introduced here.

## Verification and deliverables

Inputs are RC98 followed by its eleven dependencies in the same order. Their byte SHA-256 hashes must match RC98 exactly. RC98 already verifies the matching trial, source, norm and projection attachments.

Generation uses ordered interval contractions; independent algebra replay uses symmetric triangles, column-first products and weighted Gram row identities. Both recheck all Loewner upper tests, polarization endpoints, interval intersections, ellipsoid relative bounds and completion vertices. The JSON must match exactly. No floating eigenvalue, new quadrature or Lean formalization is accepted as evidence.

- `scripts/validate_rpb108_rc99_signed_source_projection_bounds.py`
- `certificates/rpb108_rc99_signed_source_projection_bounds.json`
- `notes/RPB108_RC99_SIGNED_SOURCE_PROJECTION_INTERFACE_20261011.md`

No changes to other branches or research fronts. Full positivity, RH and Global/F4 remain open.
