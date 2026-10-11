# RPB108 RC90 — continuous source balance and fixed-enclosure floor

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `e79f7b5546ac46b4860f21e755db406c6db826cd` (RC89).

## Result

RC90 replaces the coarse final Young-parameter search with two fixed
rational parameters selected by numerical exploration and certified by
exact fractions. It also brackets the global best relative factor over
all positive scalar Young parameters for the unchanged RC89 component
matrices. The retained actual projected-source upper decreases from
`251/512 = 0.490234375` to
`269336301191/549755813888 = 0.4899198778566642...`.

| Parity | Rational Young parameter | Certified family lower, approximately | Certified source upper, approximately | Certified upper/lower gap |
|---|---:|---:|---:|---:|
| even | `265289494/10^9` | 0.4899198778557595 | 0.4899198778566642 | less than `9.05e-13` |
| odd | `284355267/10^9` | 0.4473514308264781 | 0.4473514308265294 | less than `5.14e-14` |

The retained factor decreases by approximately **0.0641524%**. The larger
result is the boundary certificate: further rebalancing of this fixed
family cannot yield a material decrease. Even zero transfer allowance
leaves a nominal-upper-matrix directional factor above **0.306** in the
even block and **0.271** in the odd block, far above the inherited scalar
gate. This is a limitation of these enclosure matrices, not a lower bound
on actual source leakage.

The head rank is 38, source inputs 22, and polynomial trial dimension 64.
No physical source, Riesz trial or component covariance changes.
Generation and independent replay: **PASS**.

## Fixed family and the actual-source upper

Let `N` be RC89's nominal projected-source covariance upper and `E` its
complete actual-source transfer covariance upper. Both are fixed 22-by-22
PSD matrices with exact parity preservation. RC89 supplies the proof
that, for every positive parity parameter `t_p`,

`Gamma38 <= A(t)=(1+t_p)N+(1+1/t_p)E`,

with upward Loewner rounding on the `10^-24` grid. `Gamma38` is the actual
rank-38 projected original-source Gram. All original Riesz and physical
source approximation uncertainties remain included in `E`.

The reference input matrix is the unchanged RC67 actual original
22-input canonical Gram **lower** matrix `M22`. Thus proving
`A(t) <= lambda M22` is a sufficient relative bound against the full
actual input Gram. The optimization and lower witnesses below use this
fixed reference lower matrix; they do not determine a generalized
eigenvalue against the unknown full actual input Gram.

At the two recorded rational parameters, the validator constructs the
full parity-preserving source upper and checks its PSD property. Exact
40-step rational bisection then certifies each relative upper factor.
Replay repeats the comparisons after native-to-Legendre congruence.

The new upper improves the reported scalar factors in both parities.
A whole Loewner improvement over RC89's final matrix is **not** certified:
changing Young parameters trades matrix directions even when the worst
relative factor decreases. RC89's prior upper remains valid.

## Continuous-family lower witnesses

In each parity choose the recorded fixed integer native direction `v`.
All proof quantities are exact:

`a=v'Nv/(v'M22 v)`, `b=v'Ev/(v'M22 v)`.

Both are positive. For every `t>0`,

`v'A(t)v/(v'M22 v) = a+b+at+b/t`
` >= a+b+2 sqrt(ab)`.

The inequality follows from `(sqrt(at)-sqrt(b/t))^2 >= 0`.
Upward matrix rounding can only increase this quadratic, so the same
lower applies to the rounded family. If `A(t) <= lambda M22`, then
`lambda` must exceed this directional lower bound.

The validator computes an exact square-root floor on the
`10^-30` grid using integer square root and verifies
`r^2 <= ab < (r+10^-30)^2`. The recorded lower is `a+b+2r`.
No floating value is used as proof evidence. Numerical exploration only
selected the integer directions and rational parameters.

The certified source upper bounds the infimum over the family from above;
the directional witness bounds it from below. Their exact rational
difference is below `10^-12` in both parity sectors. This proves a global
near-optimum for this particular family over **all** positive parameters,
not merely over a sampled grid. It does not optimize other source
attachment methods or projection spaces.

## Zero-transfer limit and sensitivity

To expose the remaining term, consider an idealized transfer amplitude
`alpha`, replacing `E` by `alpha^2 E` while keeping `N` fixed. The same
direction proves, for every positive parameter,

`lambda >= a+alpha^2 b+2 alpha sqrt(ab)`.

The certificate records exact lower values for amplitudes `0`, `1/4`,
`1/2` and `1`. Values with `alpha<1` are hypothetical sensitivity probes;
they are not valid improved certificates for the unchanged actual source.

At `alpha=0`, the continuous-family infimum still has the directional
lower `a`:

| Parity | Nominal-upper-matrix directional factor, approximately | Ratio to inherited scalar gate, approximately |
|---|---:|---:|
| even | 0.306016788706724 | `1.7912e10` |
| odd | 0.271193010965569 | `1.5874e10` |

RC63's inherited strict scalar source-budget ceiling is
`42711336886890003319091/2500000000000000000000000000000000`,
approximately `1.7084534755e-11`. Exact comparisons show that reducing
`E` alone, even ideally to zero, cannot make this fixed `N` satisfy that
sufficient gate through positive scalar Young balancing.

The witness is a lower bound for the **nominal upper matrix**, not the
true nominal or actual source Gram. It does not prove the actual source
has these factors. A sharper source-specific transport bound or covariance
calculation can change `N`; a different positivity criterion can change
the required sufficient gate. Neither is excluded by RC90.

## Replay and provenance

Generation evaluates directional quadratics by matrix contraction.
Independent replay uses diagonal terms and doubled upper-triangular sums,
rebuilds the final covariance through a separate expression, verifies the
integer-square-root enclosure, and repeats the exact PSD and relative
comparisons after native-to-Legendre congruence. The full replay result
must equal the saved JSON.

Four input hashes bind RC89, RC67, RC59 and RC63. RC89's links to RC67 and
RC59, and RC63's link to RC59, are checked. The fixed rank, source input
count, dimension, component positivity and parity zeros are checked.

```bash
python scripts/validate_rpb108_rc90_continuous_source_balance_and_method_floor.py --replay certificates/rpb108_rc90_continuous_source_balance_and_method_floor.json
```

## Frontier implication and scope

Scalar balancing of the current two component matrices is now exhausted
at the certified precision. Material progress toward the inherited gate
must change the nominal source enclosure as well as address transfer, or
use another sufficient criterion. Source-specific complement transport,
physical subtraction/covariance refinement and head enrichment remain
separate possible changes; their outcomes are not assumed here.

The scalar source budget remains open. No actual rank-38 budget failure,
38-input original source covariance, enlarged Weil or complement floor,
whole-aperture positivity, RH, F4 or Lean formalization is asserted.
