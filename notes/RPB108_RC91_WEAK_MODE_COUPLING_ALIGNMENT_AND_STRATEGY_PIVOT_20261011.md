# RPB108 RC91 — weak-mode coupling alignment and strategy pivot

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `b0ea2c6f5e1348dc827bfd85e4b7f2500032416e` (RC90).

## Decision and result

The finite sufficient reduction does not establish a necessity to evaluate
its head densely. RC91 prioritizes a matrix Schur / weak-mode experiment
instead of another scalar transport refinement. The current exact source
covariance already permits a decisive first alignment test without new
physical integrations.

RC63's weak directions have small coupling, despite the global RC90
relative upper factor near 0.49. The complete two-dimensional weak span
in each parity, including its cross-correlation, satisfies:

| Weak span | Rank-38 projected coupling upper relative to its canonical input Gram lower | Schur penalty upper using the inherited rank-1250 complement floor |
|---|---:|---:|
| even, RC63 weak_0 and weak_1 | `5.776623910424e-14` | `5.846785334438e-13` |
| odd, RC63 weak_0 and weak_1 | `4.281982940887e-12` | `4.333990830857e-11` |

Displayed decimals are rounded upward; exact fractions are in the JSON.
The source upper is unchanged from RC90. These restrictions are obtained
by exact congruence, not by substituting the global scalar factor into the
weak block. Generation and independent bilinear replay: **PASS**.

This supports pursuing matrix-valued isolation. It does not prove that
these modes are positive: every retained RC63 weak-head interval contains
zero. Nor does it prove that these four directions contain every dangerous
mode of the complete head.

## Definitions and projection scope

Let `H_m` be the actual canonical Riesz span of physical polynomials of
degree less than `m`, and `Pi_m` its actual orthogonal projection. The
native Chebyshev and physical Legendre targets span the same polynomial
space by invertible exact basis conversion.

Let `S22` be the complete original-source map for the first 22 native
Riesz inputs. RC90 gives the actual covariance upper `G38` for

`Gamma38 = S22*(I-Pi38)S22`.

Here the star denotes the adjoint; equivalently the matrix is the canonical
Gram of the 22 projected source columns. These source vectors represent
the original Weil operator applied to the native Riesz inputs, so their
projected components give the original head/complement coupling.

Polynomial inclusion gives `H38 subset H1250`. Consequently, for every
input vector `v`,

`||(I-Pi1250)S22 v||_can^2 <= ||(I-Pi38)S22 v||_can^2`.

Thus `Gamma1250 <= Gamma38 <= G38` on the same 22 source inputs. This is
an upper bound by projection nesting, not an identification of the two
covariances. RC63's inherited complement floor is `alpha=247/2500=0.0988`
for the complement of `H1250`. RC91 never applies that floor to the larger
complement of `H38`.

## Complete weak-span congruences

For each parity, let `V` have the two fixed native coefficient columns
from RC63, labeled `weak_0` and `weak_1`. Define

`C_weak = V'G38 V`,
`M_weak_lo = V'M22_lo V`,

where `M22_lo` is RC67's actual canonical input Gram lower matrix.
The latter is positive definite, verified by exact PSD and determinant
checks. The actual weak input Gram dominates `M_weak_lo`.

The validator certifies

`C_weak <= mu M_weak_lo`

with exact rational PSD comparisons. The small matrix is scaled by `10^15`
before 40-step rational relative bisection to preserve useful precision.
Both off-diagonal entries are retained; no weak-mode orthogonality is
assumed. This proves the bound for every linear combination in each
complete two-dimensional span, not just its two basis directions.

The same covariance upper bounds the rank-1250 coupling. Therefore the
corresponding penalty upper is `C_weak/alpha`, with relative factor
`mu/alpha`, as displayed above.

## Directional head signs remain unresolved

For continuity with RC63, the following table uses its original canonical
norm lower normalization rather than the sharper block Gram reference.
It compares each actual-source covariance upper with the signed head
interval already certified there.

| Direction | Coupling upper factor | Schur penalty upper factor | Existing actual Weil Rayleigh enclosure |
|---|---:|---:|---:|
| even weak_0 | `5.82653e-17` | `5.89730e-16` | approximately `[-2.94921e-10, 2.78266e-10]` |
| even weak_1 | `1.52050e-13` | `1.53897e-12` | approximately `[-2.48516e-10, 2.36236e-10]` |
| odd weak_0 | `1.12173e-15` | `1.13536e-14` | approximately `[-1.86844e-10, 1.72921e-10]` |
| odd weak_1 | `1.08772e-11` | `1.10093e-10` | approximately `[-1.90484e-10, 2.13734e-10]` |

The table is explanatory; exact signed quadratics, norm bounds and
covariance contractions are stored in the certificate. All four available
lower bounds for `Q(v)-alpha^-1 coupling(v)` remain negative, because the
head lower enclosures themselves remain negative. This does not prove
actual negative values. In particular, the odd weak_1 penalty is still
substantial relative to its head uncertainty window.

The coupling is small precisely in these weak directions. The global
worst-case upper factor therefore loses information essential to assessing
them. RC90's scalar-family floor is not an obstruction to this different
matrix-valued strategy.

## Structural Schur objective

On the complete head `H1250`, write the original Weil block as `A`, the
head/complement coupling as `B`, and the complement operator as `D`.
The inherited floor is `D >= alpha I`. The sufficient condition

`A-alpha^-1 B*B > 0`

follows by Schur complement, since `B*D^-1B <= alpha^-1 B*B`.
It retains the relation between head weakness and coupling directions.
Using the exact complement inverse could be stronger, but is a separate
obligation.

For a certified head decomposition into weak and strong blocks, set
`T=A-alpha^-1 Gamma`. Its blocks must satisfy

`T_SS > 0`,
`T_WW-T_WS T_SS^-1 T_SW > 0`.

A positive weak diagonal or small weak-to-complement coupling alone is
insufficient: the weak/strong head cross block must also be paid. Likewise,
a strong-block theorem must cover the entire remaining complete head;
positivity of a few strong control directions is not such a theorem.

## Next targeted obligations

1. Sharpen the actual original Weil restriction to the two weak modes in each parity. This starts with six signed entries, three per 2-by-2 parity block, including exact basis and Riesz-error transport. It is not a request for a dense 1,250-feature matrix.
2. Determine whether further potentially nonpositive head modes exist outside these four directions. A structural index or strong-subspace lower theorem is needed for coverage; the four witnesses are not assumed exhaustive.
3. Certify the weak/strong cross block in the corrected Schur matrix and its strong-block inverse allowance. Retain coupling matrices and correlations throughout.

An unsuccessful positivity check from current upper/lower enclosures would
show insufficient certification. To conclude that a mode is actually
dangerous would require tighter signed values or an actual coupling lower
bound. Upper-bound failure alone cannot establish that conclusion.

The arithmetic-factorization and first-contact alternatives remain distinct
strategies. RC91 does not restart other research branches or assume a
separate aperture-1.10 finite certificate is logically necessary for a
global first-contact theorem.

## Replay and provenance

Generation contracts both weak blocks by full matrix products. Independent
replay uses the symmetric bilinear formula with diagonal terms and one
upper triangle, including cross coefficients `v_i w_j+v_j w_i`. All PSD,
Gram determinant, relative and penalty comparisons are repeated, and the
full result must equal the saved JSON.

Four hashes bind RC90, RC63, RC67 and RC59. Their source/Gram/weak-witness
provenance links are checked exactly. The actual rank-38 source upper,
rank-1250 floor, four fixed directions and normalization references remain
explicitly distinguished.

```bash
python scripts/validate_rpb108_rc91_weak_mode_coupling_alignment.py --replay certificates/rpb108_rc91_weak_mode_coupling_alignment.json
```

No matrix Schur positivity, complete weak-mode coverage, strong-block
positivity, weak/strong cross-block estimate, scalar source budget, actual
rank-38 failure, whole-aperture positivity, RH, F4 or Lean result is claimed.
