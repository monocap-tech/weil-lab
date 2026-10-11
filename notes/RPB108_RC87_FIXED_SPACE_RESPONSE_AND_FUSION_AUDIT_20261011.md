# RPB108 RC87 — fixed-space response gain and continuous fusion audit

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `bb7467784cd19031a1f1de19713f741e33b27706` (RC86).

## Result

RC87 closes two narrowly defined refinement routes:

1. The maximum canonical response-error reduction from any correction in the existing 64-mode polynomial trial space is at most `10^-36 M22` in the even block and `10^-37 M22` in the odd block. For the nominal midpoint metric, the corresponding capture gain is at most `10^-78 M22` in either block.
2. Every continuous convex blend of the retained RC82 source covariance upper and the RC86 candidate fails the next lower factor on the existing 12-step dyadic certificate grid, separately in both parity blocks. This is proved for all blend weights, not merely sampled weights.

The retained actual rank-38 projected source upper is unchanged:
`2061/4096 = 0.503173828125` times the original 22-input canonical Gram
lower matrix. Head rank 38, source inputs 22, and trial dimension 64 remain
unchanged. Generation and independent replay: **PASS**.

These results concern the strength of specified upper-bound constructions.
They do not prove actual leakage is large, positivity fails, or the scalar
source gate is impossible by other methods.

## Fixed-space nominal normal equations

Let `H` be the center of the complete RC83 64-by-22 physical source-pairing
table, `G` the RC67 nominal canonical metric center, and `Z` the unchanged
RC83 rational response. Set

`d = H-GZ`.

For a trial response `W`, the nominal capture functional is

`C(W) = H'W + W'H - W'GW`.

For every 64-by-22 correction `T`, exact square completion gives

`C(Z+T)-C(Z) = d'T + T'd - T'GT`
` = d'G^-1d - (T-G^-1d)'G(T-G^-1d)`.

Thus the maximal gain is exactly `d'G^-1d`. RC67's actual metric lower
bound implies `G >= D`, with `D` the physical Legendre mass matrix, so

`d'G^-1d <= d'D^-1d`.

The validator calculates the normal-equation solution, checks `G T=d`,
and checks this Loewner comparison with exact rational arithmetic. The
recorded upper matrix is rounded upward on the `10^-100` grid. Its
relative bound against `M22` is `10^-78` in each parity. This is a
rounding-scale correction to an already stationary response.

## Actual metric and physical nominal source

The conclusion is not restricted to the midpoint metric. Let
`S = i*F_nom`, `e=S-Z`, and `P_W` be the actual canonical orthogonal
projection onto the entire 64-mode polynomial trial space `W64`.
For every correction `T` in that space,

`Gram_can(e)-Gram_can(e-T)`
` = Gram_can(P_W e)-Gram_can(T-P_W e)`
` <= Gram_can(P_W e)`.

RC86's certified orthogonality-defect matrix `Omega` bounds the last Gram.
RC87 reconstructs it independently from the pairing intervals and metric
uncertainty. If `R_H` is the entrywise pairing radius and `delta_G` the
metric mass error, then

`Omega = 3[d'D^-1d + box(R_H'D^-1R_H) + delta_G^2 Z'DZ]`,

with upward Loewner rounding on the `10^-60` grid. Here `box(K)` is the
diagonal matrix of row sums of the nonnegative-entry matrix `K`.
The validator checks the actual metric lower enclosure is at least `D`,
verifies nonnegative entries of `R_H'D^-1R_H`, and requires exact equality
with RC86's `Omega`.

| Parity | Nominal midpoint maximum capture gain upper | Actual-metric nominal-source maximum response-error reduction upper |
|---|---:|---:|
| even | `10^-78 M22` | `10^-36 M22` |
| odd | `10^-78 M22` | `10^-37 M22` |

The actual-source transfer uncertainty is not removed by this statement.
It bounds corrections to the response to the physical nominal source,
using the actual canonical metric. Nor does stationarity imply that every
possible projected-source attachment certificate has been optimized:
a different response can change conservative intermediate bounds even
when it cannot materially reduce the true unprojected response error.

## All continuous convex source fusions

Let `A` be the retained RC82 actual projected-source covariance upper and
`B` the RC86 candidate upper. Both bound the same actual rank-38 projected
source Gram, so every

`C(theta)=(1-theta)A+theta B`, `0 <= theta <= 1`,

is also a valid upper matrix. Parity weights can be chosen independently.
RC87 uses fixed integer native input directions `v` selected by numerical
exploration, then verifies all evidence with exact fractions. The numerical
selection is not part of the proof.

For each direction, compute exact ratios

`r_A = v'Av/(v'M22 v)`, `r_B = v'Bv/(v'M22 v)`.

The same direction gives

`v'C(theta)v/(v'M22 v) = (1-theta)r_A+theta r_B`
` >= min(r_A,r_B)`.

Therefore any scalar factor `lambda` satisfying `C(theta) <= lambda M22`
must be at least this minimum, for every continuous blend weight.

| Parity | Universal factor lower bound for these upper matrices, approximately | Next lower dyadic factor | Retained factor |
|---|---:|---:|---:|
| even | 0.5031277681876338 | `2060/4096 = 0.5029296875` | `2061/4096` |
| odd | 0.4597643360637354 | `1883/4096 = 0.459716796875` | `1884/4096 = 471/1024` |

Both exact witness margins over the next lower factor are strictly
positive. No blend, including weights arbitrarily near either endpoint,
can certify that next grid value. The certificate stores the integer
directions, all three quadratic forms, exact ratios and strict margins.
This does not exclude improvements smaller than one grid step or fusion
methods other than scalar convex combinations.

The witness lower factors also exceed RC63's inherited scalar Schur
source-budget strict ceiling
`42711336886890003319091/2500000000000000000000000000000000`,
approximately `1.7084534755e-11`. Thus this entire convex upper-enclosure
family cannot meet that sufficient gate. This comparison is about the
family's upper factors, not a lower bound for the actual projected source
Gram. The inherited complement floor and the scalar method's sufficiency
conditions remain unchanged.

## Replay and provenance

Generation bounds the normal-equation gain by `d'D^-1d`. Replay also
computes the capture functional at `Z+G^-1d` and verifies exact equality
of its gain with `d'G^-1d`, checking all 64-by-22 normal equations. The
continuous-fusion witnesses are replayed through diagonal and doubled
upper-triangular quadratic sums, independently of the matrix-product
contractions used in generation. All Loewner and strict scalar comparisons
are repeated, and the complete result must equal the saved JSON.

The five input SHA-256 hashes are checked together with RC86-to-RC83,
RC86-to-RC67, RC86-to-RC82, RC83-to-RC67 and RC82-to-RC63 provenance links.

```bash
python scripts/validate_rpb108_rc87_fixed_space_response_and_fusion_audit.py --replay certificates/rpb108_rc87_fixed_space_response_and_fusion_audit.json
```

## Frontier implication and scope

Further material reduction of the true canonical response error requires
changing the trial space or the source being approximated. The scalar
convex fusion of these two completed source certificates cannot reduce the
retained dyadic factors. Improvements to the actual projection/source
attachment, stronger complement transport, or a different sufficient gate
remain distinct possibilities; RC87 does not eliminate them.

No new source covariance, positive Weil or complement floor, scalar source
budget certification, actual rank-38 failure, whole-aperture positivity,
RH, F4 or Lean result is asserted.
