# RPB108 — DNE19: floor-only raw-background strategy boundary

Definitions: [DNE19 terminology](../docs/TERMINOLOGY_RPB108_DNE19_FLOOR_BOUNDARY.md).
Parent: DNE18, e955e684fb2c88545f39621bf4095882ef63ca55.
Read-only Phase head: 1b227864aa6398e59922fde470f371fb9b72dc11 (NF28).
Read-only Coupled head: ae03e419ef9b975ee219806873c755b4d3149982 (CC71).
Aperture a=53/50. Only the DNE branch is modified.

## Result

The original DNE17 high floor kappa=11/25 does NOT close the coarse
collective estimator on NF28's unlifted retained response w. Its diagonal
is strictly negative in both parities. This remains an estimator
rejection, not a negative original Weil vector or actual Schur sign.

More decisively, no improvement of the global prime norm bound ALONE
can close that raw-background test while retaining DNE17's fixed
archimedean-minus-pole budget L=2.772351243732.

| Certified quantity | Even | Odd |
| --- | ---: | ---: |
| Necessary floor threshold, strict lower | 0.69827 | 0.80553 |
| Coarse w diagonal upper at kappa=0.44 | -2.7617e-37 | -2.2502e-33 |
| Necessary source-square reduction at fixed native energy | >36.98% | >45.37% |
| Necessary fixed-budget L if using a global norm subtraction | >2.82242 | >2.92968 |

The common floor ceiling of this specified subtraction family is less
than 0.648204. The complete two-direction coarse matrix therefore fails
already on w; its remaining mixed entries cannot repair positivity.
The full unchanged unlifted background matrix also cannot pass, because
it contains this explicit retained direction. A basis change of the
same trial space only applies congruence and cannot repair this failure.

This does not prohibit improving the archimedean bound, using compressed
prime estimates, changing high lifts, or resolving actual inverse response.
In particular, it is NOT an upper bound on the actual F112 spectral floor.

## Exact global-prime witness

Use the same complete six-prime clipped physical operator P as DNE17.
For f=P1, self-adjointness gives

    ||P|| >= <P1,P^2 1>/<P1,P1>
           = <1,P^3 1>/<1,P^2 1>.

The first expression is integrated exactly over the union of the
13-band P1 and 39-band P^2 1 step functions. Every cut remains symbolic
plus/minus a+log(q), with q rational. The frozen DNE17 producer verifies
all ordering and clipping decisions with outward rational logarithm
and square-root enclosures; no rounded support or sampling is accepted.

An independent combinatorial computation enumerates all 12 signed prime
steps at lengths two and three. Intersecting the support constraints at
EVERY prefix leaves 82 and 464 surviving words. Summing their amplitude
products times exact interval-domain lengths independently encloses the
denominator and numerator. Both computations overlap on each moment and
on their ratio.

The certified Rayleigh lower bound exceeds 2.124147. Full exact rational
intervals are in the certificates; approximately it is 2.124147562285916.
Thus any global norm upper bound U must satisfy U >= this witness, and
any floor supplied using the fixed L obeys

    kappa <= L-U <= L-Rayleigh_lower < 0.648204.

NF28's source-square/energy ratios are above this ceiling in both
parities. Even the ceiling itself gives a strictly negative sufficient
w diagonal after interval payment. This rejects the entire specified
fixed-budget/global-norm subtraction family, not merely DNE17's selected
positive step weight or precision.

## Dependency and validation boundaries

The NF28 complete source Gram and original two-direction native energy
are authenticated byte-exact inputs from the read-only Phase head.
DNE19 does not replay their expensive full signed source construction or
the raw E112 archive. The source input records the same authenticated
target, high trial, NF26 certificate, NF27 response and raw-native hashes.
DNE19's numerical statements are exact rational consequences of those
intervals, plus its fresh prime Rayleigh witness.

The frozen DNE17 producer is copied byte-exact. Primary 60-digit/220-term
and replay 80-digit/320-term rational enclosures each pass 623 explicitly
counted assertions, with 21 separate replay comparisons. Higher precision
nests the two physical moment intervals and strengthens the barrier.
These counts exclude the inherited producer's internal assertions.

Three exact two-block controls cross positive, null and negative Schur
signs. Three shifts of the whole rank-one null form have exact positive
ground levels. A positive actual matrix [[1,0.7],[0.7,1]] is rejected by
the deliberately coarser 0.44 floor, checking that estimator failure is
not reported as actual negativity. These controls are algebraic and are
not countermodels to complete Weil identities.

Reproduce with the published scripts adjacent to their frozen helper:

```sh
python3 scripts/certify_dne19_floor_boundary.py notes/data/RPB108_DNE19_NF28_INPUT_20261009.json --output /tmp/dne19.json
DNE17_GRID_DIGITS=80 DNE17_LOG_TERMS=320 python3 scripts/certify_dne19_floor_boundary.py notes/data/RPB108_DNE19_NF28_INPUT_20261009.json --output /tmp/dne19_replay.json
python3 scripts/validate_dne19_replay.py /tmp/dne19.json /tmp/dne19_replay.json /tmp/dne19_validation.json
```

## Board state and next interface

DNE18's positive four-dimensional retained plane plus the ENTIRE F112
complement remains certified, with common physical gap 10^-35. DNE19
adds no new positive retained dimensions and removes no established result.

CC71 now supplies complete original finite116 positivity and 110 frozen
source-aware background lifts. Its complete-source Gram is not yet
certified. A finite116 gap cannot be transferred to the remaining
infinite complement without paying that source reaction.

The next collective route should preserve the frozen lifts' original
energy and physical mass matrices and certify their COMPLETE residual
source Gram, then test the resulting joint seed/background matrix with
the DNE17 floor or a justified sharper response estimate. Raw-W source
precision and global prime-weight optimization alone are not sufficient
under the budget fixed here. A new archimedean estimate is another route,
not ruled out by this checkpoint.

The authenticated raw E112 archive remains needed for independent native
replay, although CC71's published certificates now provide a finite
collective dependency. Its availability is not inferred from failed
Library searches. This turn makes no additional Library search.

Whole 1.06 positivity, complete infinite-high retained Schur sign, global
actual null exclusion, cap-uniform leakage, RH/F4, full transport and
Lean closure remain open. Historical text and all other branches are untouched.
