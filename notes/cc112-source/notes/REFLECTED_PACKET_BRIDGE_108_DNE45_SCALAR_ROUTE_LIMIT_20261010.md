# RPB108 DNE45: a certified limit of the fixed scalar route

Parent: DNE44, `bb7220c07aa66c2fea00bbc36452a59130ee3fb1`, on
`research/rpb108-direct-null-exclusion`. Terminology was registered before
load-bearing computation in `docs/TERMINOLOGY_RPB108_DNE45_SCALAR_ROUTE_LIMIT.md`.
Prior reports and certificates are immutable.

DNE45 proves that improving only the global prime operator norm estimate,
while retaining the inherited arch-minus-pole input, cannot make either
complete DNE44 44-column sufficient comparison positive. This is a limit
of that certificate route. It is not an original negative direction or
an obstruction to RH.

## Exact result

Let N44 be the original native matrix and G44 the original projected
source Gram in each parity. The packet is (T4 S, X[0:40]). Define
lambda = max_v (v*G44 v)/(v*N44 v). N44 is positive by a re-audited
rational congruence certificate. The saved certificate gives an exact
rational trial lower bound and a full congruence positive certificate
for hi N44 - G44, hence lo <= lambda < hi.

| Parity | Lower bound, decimal display | Exact rational upper bound | Width |
| --- | ---: | ---: | ---: |
| Even | 0.7463624055881617 | 74636241/100000000 | < 1e-8 |
| Odd | 0.6199376939988428 | 6199377/10000000 | < 1e-8 |

Lower endpoints are stored as exact rational numbers; displayed decimals
are illustrative. NumPy proposes trials only. All proof decisions are
exact interval inequalities. The upper thresholds have **not** been
established as lower bounds for the original infinite high operator.

For the global clipped prime operator P, take w=P^17 1. DNE43's authenticated,
independently audited bands enclose w and Pw. DNE45 integrates their products
on all 8,899 common bands. Cut lengths have independently evaluated rational
logarithm enclosures. The saved intervals enclose <w,Pw> and <w,w>.
Their quotient proves, after a strict downward rounding,

    ||P|| > r = 107944751/50000000 = 2.15889502.

The strictness is an exact check against the unrounded Rayleigh lower
endpoint. P is symmetric and preserves nonnegative functions; it need
not be positive semidefinite for this norm lower bound.

Keep the fixed inherited arch-minus-pole lower input

    alpha = 693087810933/250000000000 = 2.772351243732.

Every valid global prime norm upper bound beta must satisfy beta >= ||P|| > r.
Consequently the fixed-input subtraction route can certify a lower floor
alpha-beta strictly below

    alpha-r = 153364055933/250000000000 = 0.613456223732.

This ceiling lies strictly below both exact trial lower bounds. The
certificate also pays both trial budgets (alpha-r) v*N44 v - v*G44 v,
and the independent audit verifies that each upper endpoint is negative.
Thus no choice of a better positive weight, nor even an optimal global
norm upper estimate, closes either full 44-column comparison using this
fixed alpha. This does not bound the actual high floor from above:
alpha is a lower input, **not an upper bound on the true arch term**.
With the same global subtraction form, closing each parity necessarily
requires increasing the arch input by more than approximately
0.132906181856 (even) or 0.006481470267 (odd); exact necessary lower
amounts are saved in the certificate. These are necessary, not sufficient.

## What remains certified

DNE44 remains the positivity state: 85 retained directions (42 even,
43 odd), including the entire previous 72-direction span, coupled to the
whole infinite F112 high space with original high floor 603/1000. The
physical guard remains 1e-38. Of the 112 retained dimensions, 27 remain
uncovered: 24 outside the computed packet and three inside it (two even,
one odd). DNE45 computes no new original source integrals and evaluates
no actual high inverse. Whole-aperture positivity, first-contact exclusion,
RH, and Lean remain open.

## Validation and custody

Run from the repository root:

```sh
python scripts/certify_dne45_scalar_route_limit.py --output notes/data/RPB108_DNE45_SCALAR_ROUTE_LIMIT_20261010.json.gz.b64
python scripts/validate_dne45_scalar_route_limit.py notes/data/RPB108_DNE45_SCALAR_ROUTE_LIMIT_20261010.json.gz.b64 --output notes/data/RPB108_DNE45_SCALAR_ROUTE_VALIDATION_20261010.json
```

The validator uses independent exact endpoint matrix algebra. It rechecks
both inherited native congruences, both new full-packet target congruences,
the trial quadratic enclosures, band coverage and exact integral sums,
Rayleigh arithmetic, strict ceiling failures, decoded input hashes, and
scope flags. It authenticates DNE43's passing band-recurrence audit and
DNE44's passing source/subspace audits rather than counting their checks
as newly executed. The independent validation passes 50,340 newly executed exact rational
checks. Custody records byte hashes and reproducible script dependencies.

## Direction for continuation

The remaining three comparison directions require a certificate that
changes a substantive input: stronger arch control, a restricted or
correlated prime estimate, or directional high inverse response. For the
last option, use DNE44's exact positive embedding B and negative comparison
embedding D. With C = G/k - Z*L P_F L_F^(-1) P_F L Z >= 0 and k=603/1000,
the original finite Schur matrix is H/k+C. In the (B,D) basis, closure
requires F-E* A^(-1) E > 0, where A=B*(H/k+C)B, E=B*(H/k+C)D,
and F=D*(H/k+C)D. A credit on D alone does not pay the mixed E block.
Those response bounds remain to be computed and certified. A basis change
alone cannot remove DNE44's already certified comparison inertia.
