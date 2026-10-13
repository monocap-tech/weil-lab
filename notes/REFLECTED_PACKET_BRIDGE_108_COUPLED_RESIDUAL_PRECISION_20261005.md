# RPB108: coupled residual pilot and its precision obstruction

## Terminology and task

A **coupled residual pilot** evaluates all eight actual polynomial interior sources together and retains their residual Gram matrix, including within-parity mixed entries. A **recorded-matrix discrepancy certificate** concerns exact differences between two stored approximate matrices; it does not enclose the actual operator.

The target is the established exact lower bound S>=Q_8-5R for the restriction of the 64-dimensional Schur form to the first eight low sources, with approximate lift Z=0. R is the physical Gram of source residuals after projection away from degrees 0..63. Unlike a diagonal bound, this matrix retains cancellations between source directions.

## Actual source evaluation

`scripts/explore_native_coupled_residual.py` evaluates the previously proved actual source constructor for normalized physical Legendre vectors v_n=sqrt(2n+1)P_n(2x), n=0,...,7, at a=1/2. The outer integral is split at the two actual prime discontinuities. The archimedean difference integrals use 64 inner Gauss nodes; pole moments use the same vectors and native modified spherical Bessel values. All values here are floating and uncertified.

The script constructs the full eight-column source map, projects away the first 64 physical Legendre functions, and integrates the residual outer products. It uses the previous physical finite matrix Q_8 independently. No complement inverse, retained membership, raw multiplicity observation or changed source vector is introduced.

## Pilot result

Recorded data: `notes/data/RPB108_COUPLED_RESIDUAL_PILOT_20261005.json`.

| Nodes per outer panel | Smallest even lower pilot eigenvalue | Smallest odd lower pilot eigenvalue | Max source-pairing discrepancy from Q_8 |
|---|---:|---:|---:|
| 512 | 4.9393034e-6 | 3.8176670e-4 | 1.1064937e-5 |
| 1024 | 4.9392322e-6 | 3.8169676e-4 | 2.7688253e-6 |

Every displayed lower-pilot eigenvalue is positive. This is evidence that the no-lift residual certificate may work on this eight-source span; it is not a certified Schur sign. The 1024-node residual operator norm display is about 0.209679. The narrow even direction, in normalized degrees 0,2,4,6, has coefficients approximately (0.793620,-0.572114,0.203928,-0.035579). Its cancellation is lost by treating source residuals as independent scalar worst cases.

The full residual Gram repeat-difference operator norm display is about 1.14217e-4, much larger than the repeat difference in the smallest eigenvalue. Thus stable repeated minimum displays do not by themselves provide a useful operator enclosure.

## Exact recorded precision obstruction

Treat each stored decimal entry as its exact rational value. The difference in the degree-seven residual diagonal between the two stored matrices is

0.00004765793868862 > 4e-5.

For any common candidate actual Gram R, the operator norm of each approximation error bounds its diagonal error. By the triangle inequality, at least one approximation has operator error at least half of this diagonal discrepancy, greater than 2e-5. In particular both cannot have operator errors <=1e-6.

`scripts/audit_coupled_residual_precision.py` checks this statement exactly using rational parsing of the recorded matrices. Its output is `notes/data/RPB108_COUPLED_PRECISION_AUDIT_20261005.json`. This theorem concerns the two specified approximate matrices and any common target. It does not identify which approximation is farther from the actual R, certify either error, or prove the actual Schur form has a negative direction.

For the elementary isotropic certificate using the displayed minimum near 4.94e-6, a residual Gram error below roughly 9.88e-7 is needed even if Q_8 were exact, because its error is multiplied by five. The recorded discrepancy rules out both runs meeting that scale. Tighter arithmetic alone does not remove the quadrature truncation disagreement; an independent integration remainder bound or structural singularity treatment is required.

## Lawful source-enclosure criterion

Here is the precise criterion for replacing that exploratory step. Let V:C^8 to L2 be the actual source map, and let an explicitly represented approximate source map V_tilde satisfy ||V-V_tilde||<=eta. Physical complement projection has norm one. Put R_tilde=(P_F V_tilde)* (P_F V_tilde), and suppose ||P_F V_tilde||<=M. Expanding the Gram difference gives

||R-R_tilde|| <= eta(2M+eta).

If Q_8 has a rigorously enclosed matrix error delta_Q and the computed lower matrix has a rigorously certified eigenvalue margin mu, then

delta_Q+5 eta(2M+eta)<mu

certifies the exact corrected eight-source restriction. A mixed error enclosure that preserves the narrow direction may replace this isotropic sufficient bound. None of eta, delta_Q or mu is obtained from repeat agreement alone. Even such an eight-source corrected certificate would leave the other 56 coordinates of the full Schur form unresolved.

## Cursor

The coupled pilot found no evidence of failure of the no-lift eight-source matrix. The exact arithmetic audit certifies a precision obstruction to treating both existing quadrature runs as tight operator enclosures. The next computational input must control endpoint logarithms and source Gram errors rigorously, preserving within-parity correlations, or use a better complement lift if subsequent corrected signs require it. The previous certified constant-linear block remains valid and unchanged.

No full corrected sign, whole-domain positivity, actual negative/null witness, endpoint exclusion or RH result is promoted. F4 entry and FULL TRANSPORT CLOSED remain open. Lean source/checkpoint and CI claims are unchanged.
