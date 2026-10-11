# RC80: two-allowance boundary and rank-only limit

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC80 audits the remaining quantitative bottleneck after RC79. It proves a boundary for the retained positive-Young upper-enclosure family, not a lower bound on actual source leakage. It also shows why generic canonical compactness, with the current Riesz-error allowance retained, cannot make rank-only enlargement a practical budget certificate.

## Fixed rank-38 enclosure boundary

Let N be RC79's projected nominal canonical residual Gram upper and E its projected canonical transfer Gram upper. Both are positive semidefinite. The retained method forms

A(t)=(1+t_p)N+(1+1/t_p)E+D,

where t_p>0 may differ by parity and D is any positive-semidefinite outward allowance. For a fixed same-parity vector v, write w=v*Nv and e=v*Ev. These are values of upper-enclosure matrices, not actual error energies. Scalar arithmetic gives

inf_{t>0} [(1+t)w+(1+1/t)e]=(sqrt(w)+sqrt(e))^2.

This is the exact directional optimum, attained at t=sqrt(e/w). There need not be a single parity parameter that attains all directional optima simultaneously. Thus every uniform relative bound A(t)<=lambda M_actual must obey

lambda >= (sqrt(w)+sqrt(e))^2 / (rho*v*P*v),

using the actual canonical input upper M_actual<=rho P, rho=252/257. The denominator upper makes the displayed lower bound conservative.

The validator checks 44 exact directions: all 22 native Chebyshev coordinate vectors and all 22 physical Legendre coordinate vectors converted exactly to native coordinates. Root floors on a rational grid give certified lower bounds for sqrt(w*e), rather than numerical square roots.

The strongest tested direction is the physical Legendre target of degree 20. In this direction:

| Enclosure quantity relative to rho times physical input Gram | Approximate value |
| --- | --- |
| Nominal allowance alone | 0.03557598215037 |
| Transfer allowance alone | 0.00801671986094 |
| Optimally Young-balanced two-allowance lower bound | 0.07736859179544 |
| Balanced lower bound divided by inherited budget ceiling | 4.5285746967 billion |
| Necessary nominal allowance reduction factor | 2.0823500704 billion |
| Necessary transfer allowance reduction factor | 469.2384063 million |

The exact rational certificates are stored in the JSON; these decimals are summaries. The comparison ceiling is RC63's strict scalar source-budget ceiling, approximately 1.7084534755e-11, derived using its weak head bound and the inherited 1250-feature complement floor. RC80 does not assert that this complement floor applies to the rank-38 complement.

Even if the transfer allowance were set to zero, retaining the current nominal allowance would still prevent this family from certifying that ceiling. Conversely, setting the nominal allowance to zero while retaining the transfer allowance also fails. Changing Young parameters alone cannot overcome either comparison. These counterfactual comparisons concern the certificate family, not the actual mathematical residual.

Both allowances must be sharpened, replaced, or treated by a method retaining additional correlations. The result does not require two independent research projects: a changed source approximation or a correlated source-specific calculation could improve both at once.

## Why generic rank enlargement is insufficient with retained error data

Consider only the generic prime-transfer part, discard all nominal and arch/pole allowances, and retain RC67's physical Riesz-error Gram upper E_phys, RC76's full physical prime norm allowance kappa=11669/4096, and transfer Young parameter nu=1/65536. These are paid upper-enclosure constants, not lower bounds for the actual prime norm or actual Riesz errors.

At arbitrary rank m, use the RC78 geometric Legendre tail prescription for the canonical adjoint embedding estimate. Its validity requires

L < (2m+3)/(2*pi*B), with B=11/10.

For m>=1, pi>3 implies L<m. Its prescribed squared tail upper is at least 1/log(e+L), since the positive low-band allowance appears as the factor 1/(1-theta). With e<3, this is greater than 1/log(4m).

The generic retained prime-transfer upper matrix therefore pays at least

(1+nu)*kappa^2*E_phys / log(4m).

In the degree-20 direction, any relative certificate based on this retained matrix must satisfy

lambda >= C/log(4m),

C=(1+nu)*kappa^2*(v*E_phys*v)/(rho*v*P*v).

The exact C and C/gamma, with gamma the inherited ceiling, are stored in the rank-only certificate. To certify the ceiling requires log(4m)>C/gamma.

The validator certifies C/gamma>3000002. For every rank m<=10^1000000, elementary inequalities log(4)<2 and log(10)<3 give log(4m)<3000002. Hence this generic prescription cannot certify the inherited budget anywhere in that rank range while the stated error enclosure and norm allowance are retained. The logarithm inequalities follow, for example, from e>8/3; e<3 and pi>3 are the established elementary constant bounds used by the Fourier estimates.

This is not a statement that the actual problem needs a million-digit feature count. It rules out that particular retained-data, generic-norm prescription as a practical rank-only route. It leaves open sharper source-specific projected prime covariances, improved physical or canonical Riesz-error enclosures, different adjoint tail estimates, and methods using correlations omitted by positive Young splitting.

## Validation and scope

Generation and independent replay passed. Replay independently integrates the physical target polynomials in monomial coordinates, checks the exact Legendre/native congruences of N and E, and verifies every root-floor and directional comparison. Exact PSD checks establish positivity of both fixed allowance matrices, dominance of N+E by RC79's emitted residual upper, and consistency of the actual canonical input lower with rho P.

Inputs: RC79, RC59, RC67, RC63. All four SHA-256 hashes are recorded. RC79's native and enriched inputs, and RC63's native input, are checked against the supplied hashes.

- scripts/validate_rpb108_rc80_two_allowance_boundary.py
- certificates/rpb108_rc80_two_allowance_boundary.json
- notes/RPB108_RC80_TWO_ALLOWANCE_BOUNDARY_AND_RANK_ONLY_LIMIT_20261011.md

Replay with default repository input paths:

`python scripts/validate_rpb108_rc80_two_allowance_boundary.py --replay certificates/rpb108_rc80_two_allowance_boundary.json`

RC79's certified actual residual upper remains 417/512=0.814453125; RC80 does not change it. No actual residual lower bound, actual Riesz-error lower bound, actual rank-38 budget failure, or whole-aperture obstruction is proved. A 38-input source covariance and enlarged Weil floor remain unevaluated. No whole-aperture positivity extension, RH, F4, or Lean formalization is claimed.

## Next quantitative frontier

The productive next step is a source-specific projected residual calculation or a sharper actual Riesz approximation/error certificate, followed by recomputation of the nominal source residual. Generic scalar norm refinements and rank-only compactness are insufficient with the retained data. RC80 makes that limitation explicit without confusing failure of an upper-bound method with failure of the actual source budget.
