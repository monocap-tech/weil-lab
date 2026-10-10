# RPB108 NF60 — direct combined-source refinement

NF60 starts from NF59 commit `a8f814c8c1a40dc6e6aba7166b47793198f94ad8`
on `research/rpb108-phase-geometry-localization`. Both independent scalar
validations pass. The previously unresolved even target now certifies a
negative value of the current physical high minorant. The odd target also
retains a strictly negative minorant value. Neither result is a negative
original Weil form, and whole aperture `1.06` remains open.

## Certified result

The targets are exactly the normalized NF58 joint vectors frozen by NF59.
The displayed decimal intervals are rounded outward for readability; the
certificates and validation reports contain exact rational endpoints.

| Parity | Previous NF59 best interval | NF60 best interval | Direct-source width / previous source width |
| --- | --- | --- | --- |
| Even | `[-2.112666e-33, 2.021588e-33]` | `[-5.504011e-35, -3.603710e-35]` | `0.003652846` |
| Odd | `[-1.392642e-31, -1.149540e-31]` | `[-1.275211e-31, -1.266972e-31]` | `0.027716647` |

The complete scalar source enclosure is about 274 times narrower for even
and 36 times narrower for odd. This resolves the sign uncertainty of the
fixed even target by exposing a remaining shortfall in the minorant. NF59's
historical full-matrix labels and its other sign probes remain intact.
NF60 establishes a scalar counterdirection for that same physical high
minorant in each parity.

## Calculation and independent audit

For `phi = P alpha + T53 beta`, merge all equal orthonormal basis indices
using exact rational coefficients before computing its complete source.
The independent validator reconstructs this merge and checks its exact
physical mass against the inherited witness and normalization. No target
or high column is selected, rescaled or replaced in NF60.

The producer uses the established 800-digit, degree-1700 moment route. The
independent validator uses the 900-digit, degree-1800 cell-first route and
does not import the NF60 producer. Both retain the endpoint logarithm,
signed pole, regular degree-320 profile, signed mixed terms, logarithm
square, all 13 prime translation cells and the analytic infinite tails.

Freeze the producer's low midpoint polynomial. The independent route
rebuilds the complete source and its low native integrals about this same
polynomial, and verifies that the frozen projected-source error covers its
own required error. For the approximant `r`, the paid source norm interval
uses `2 e ||r||_upper + e^2`. The certified norm is intersected with the
previous common-Gram scalar interval for the same actual `Xi z`.

Retain the original floor `kappa = 207/1000`, NF59's 18 even / 17 odd high
columns, its complete signed source/native crosses and its independently
certified grouped inverse correction. Reevaluate
`Q(phi) - ||Xi z||^2/kappa + correction`, then intersect with the previous
NF59 scalar target interval. This refines the enclosure of the same
minorant. It does not change the minorant or the actual inverse operator.

An initial width-accounting assertion omitted outward rounding in division
by `kappa`. The final validator accounts for the rounded source ceiling;
both final reports pass the exact component-width identity. The failed
development runs produced no public validation report.

## Remaining gate

To make the recorded target strictly positive, an additional certified
inverse-reaction gain is necessarily greater than `3.603710e-35` for even
and `1.266972e-31` for odd. A gain exceeding the negative lower endpoint
(`5.504011e-35` / `1.275211e-31`, rounded upward here) is sufficient for
these particular recorded scalar intervals. These are target budgets,
not sufficient conditions for positivity of the complete joint matrix.
The checkpoint stores both budgets as exact fractions.

The next source frontier must improve the physical inverse minorant in
these frozen counterdirections or certify a stronger inverse construction.
Further enclosure tightening alone cannot turn these negative minorant
values into a positive certificate. Every other signed transport/native
cross and the full joint positive gate still need closure.

All three original frozen archives pass both compressed and decompressed
SHA-256 checks. Before NF60 additions, all 292 locally recovered historical
scripts, notes and data files matched the NF59 Git tree. Publication adds
new paths only and preserves the complete parent tree. The original NF46
byte-identical replay and NF47 original unshifted F112 floor remain valid.
The highest certified whole-aperture anchor remains `21/20 = 1.05`.
Whole `53/50 = 1.06`, RH, F4, Lean and all-aperture closure remain open.

## Reproduction

Run from the repository root with the three authenticated original archives
in `nf24-inputs/Weil/`. Run each parity in a fresh Python process because
the inherited precision configuration is process-local.

```bash
python scripts/certify_native_combined_target_source_nf60_106.py --parity even --output notes/data/RPB108_NF60_EVEN_COMBINED_TARGET_SOURCE_CERTIFICATE_20261010.json
python scripts/certify_native_combined_target_source_nf60_106.py --parity odd --output notes/data/RPB108_NF60_ODD_COMBINED_TARGET_SOURCE_CERTIFICATE_20261010.json
python scripts/validate_native_combined_target_source_nf60_106.py --certificate notes/data/RPB108_NF60_EVEN_COMBINED_TARGET_SOURCE_CERTIFICATE_20261010.json --output notes/data/RPB108_NF60_EVEN_COMBINED_TARGET_SOURCE_VALIDATION_20261010.json
python scripts/validate_native_combined_target_source_nf60_106.py --certificate notes/data/RPB108_NF60_ODD_COMBINED_TARGET_SOURCE_CERTIFICATE_20261010.json --output notes/data/RPB108_NF60_ODD_COMBINED_TARGET_SOURCE_VALIDATION_20261010.json
python scripts/summarize_native_combined_target_source_nf60_106.py
```

See `docs/TERMINOLOGY_RPB108_COMBINED_SOURCE_NF60.md` for the source norm,
projection payment and scalar minorant terminology.
