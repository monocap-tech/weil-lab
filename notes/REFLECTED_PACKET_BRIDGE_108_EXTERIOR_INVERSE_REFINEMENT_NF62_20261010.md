# RPB108 NF62 — exterior inverse-response audit

NF62 starts from NF61 commit `a119005c56e3ea39d80f228e5dff57e0297aab96`
on `research/rpb108-phase-geometry-localization`. Both independent validators
pass, with 151 new native pairings and 151 new complete source covariances
checked. One physical direction from the exterior degree shell is added
per parity. Strict positive gain is certified in 2 of two parities;
the frozen target minorant remains certified negative in 0 of two.
Whole aperture `1.06` remains open.

## Certified target results

Targets are exactly the normalized vectors retained by NF60 and NF61,
originally frozen by NF59 from NF58. The original P3/T53 frame and all 56
signed target coordinates are unchanged. Decimal endpoints below are
rounded outward; reports contain exact rational intervals.

| Parity | High dimension | NF61 target minorant | Exterior correlated gain | Best NF62 target minorant | Scalar status |
| --- | --- | --- | --- | --- | --- |
| Even | 19 → 20 | `[-5.4375084E-35, -3.5356481E-35]` | `[8.4087347E-34, 8.4111598E-34]` | `[7.8649839E-34, 8.0575950E-34]` | POSITIVE |
| Odd | 18 → 19 | `[-1.1173463E-31, -1.1090847E-31]` | `[1.8700974E-30, 1.8701084E-30]` | `[1.7583628E-30, 1.7591999E-30]` | POSITIVE |

Strictness is recorded separately from nonnegativity. If a gain interval
starts at zero, the actual gain has not been proved zero. Scalar minorant
signs do not establish a negative original Weil form or full joint-matrix
positivity. The full entrywise classifications are retained separately.

## Exterior construction and proof

Select only even degrees 438–500 or odd degrees 437–499. Every inherited
high column is supported at degrees at most 436, so the new direction is
exactly physically orthogonal by disjoint support. Down-round the remaining
inverse response's midpoint coordinates to denominator `10^100` and use a
rational norm upper bound. The recorded old-high projection coefficients
are all zero. Selection is distinct from sign evidence.

The response uses NF60's complete directly combined target source and
NF61's current high minorant under the original unshifted F112 floor
`kappa = 207/1000`. Every old physical column, source error, source norm and
signed native/source cross is preserved. The new native and complete
source entries are independently reconstructed and paid.

The frozen selection remains at 800 digits. The final proof uses a
1000-digit, degree-1700 producer route and an independent 1100-digit,
degree-1800 cell-first route. Historical interval enclosures are promoted
exactly and all historical physical errors remain unchanged. The independent validator does
not import the NF62 producer. The new regular N320 source polynomial has
degree at most 820, so its square requires moment degree 1640. The scripts
check this capacity explicitly. Endpoint logarithms, log square, signed
pole degree40, all 13 prime translation cells, signed mixed products,
projection errors and regular/pole infinite tails remain enclosed.

Certify the enlarged surplus and inverse-denominator positive proofs.
Evaluate the correlated block-inverse target gain from its signed residual
and strictly positive Schur denominator. The common source Gram cancels
exactly. A residual interval containing zero permits a nonnegative gain
certificate without a false strictness claim.

Carry NF60's direct complete-source norm enclosure forward unchanged.
Contract the enlarged high cross against the fixed target before the
inverse quadratic. Intersect that grouped target enclosure with NF61's
best interval plus the correlated gain and the new full entrywise target
interval. The final intersection is checked as nonempty.

The initial 800-digit exterior norm enclosures were too wide to certify
the enlarged inverse denominator (even roughly ±3.3e62; odd ±1.5e60).
No certificate was issued from those runs. The final arithmetic upgrade
keeps the selected physical coefficients fixed and rebuilds only new
analytic source/moment calculations, with explicit finite-series tails.

## Remaining frontier

Rounded endpoint budgets for these frozen targets are:

- even: target already strictly positive; no additional target gain is required
- odd: target already strictly positive; no additional target gain is required

Residual probe counts independently checked: even: 14 candidates, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO; odd: 14 candidates, SPAN_ZERO, SPAN_ZERO, CERTIFIED_NEGATIVE_LOWER_MATRIX_PROBE, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO, SPAN_ZERO

Odd residual pivot 26 has physical quotient [-1.6107186e-29, -4.7731754e-30]
(outward rounded), an exact interval strictly below zero, rejecting the
current sufficient lower matrix; it does not establish a negative original
Weil form. The other 27 residual probes span zero. The producer and validator
midpoint LDL classifications remain UNRESOLVED; the additional exact probe
audit strengthens the odd classification to REJECTED_BY_CERTIFIED_NEGATIVE_PROBE.

The next gate is to refine the certified negative odd residual and resolve
the first span-zero even residual using complete direct-source and inverse
enclosures, then certify the entire original Schur gate.

These are target budgets, not sufficient conditions for the full joint
positive gate. NF62 tests one exterior response direction in each parity;
it does not certify every exterior direction or an infinite high-tail
inverse. Every remaining signed joint direction and the complete original
whole-form gate still need closure. A negative target requires a stronger
physical inverse minorant; tighter enclosures alone cannot lift it.

All three original archives pass compressed and decompressed SHA-256 checks.
All 312 locally recovered historical scripts, notes and data files matched
NF61's committed tree before additions, and publication preserves every
parent blob. NF46's original byte-identical replay and NF47's original
physical F112 floor remain intact. The certified whole-aperture anchor
remains `21/20 = 1.05`. Whole `53/50 = 1.06`, RH, F4, Lean and all-aperture
positivity remain open.

## Reproduction

Run from the repository root with authenticated originals under
`nf24-inputs/Weil/`. Use a fresh Python process per parity.

```bash
mkdir -p work/nf62/even work/nf62/odd
cp notes/data/RPB108_NF62_EVEN_FROZEN_EXTERIOR_SELECTION_20261010.json work/nf62/even/selected_high.json
cp notes/data/RPB108_NF62_ODD_FROZEN_EXTERIOR_SELECTION_20261010.json work/nf62/odd/selected_high.json
python scripts/certify_native_joint_refinement_nf62_106.py --parity even --output notes/data/RPB108_NF62_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/certify_native_joint_refinement_nf62_106.py --parity odd --output notes/data/RPB108_NF62_ODD_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf62_106.py --certificate notes/data/RPB108_NF62_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF62_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
python scripts/validate_native_joint_refinement_nf62_106.py --certificate notes/data/RPB108_NF62_ODD_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF62_ODD_JOINT_REFINEMENT_VALIDATION_20261010.json
python scripts/probe_native_joint_sign_nf62_106.py --parity even
python scripts/probe_native_joint_sign_nf62_106.py --parity odd
python scripts/summarize_native_joint_refinement_nf62_106.py
```

See `docs/TERMINOLOGY_RPB108_EXTERIOR_REFINEMENT_NF62.md` for exterior
support, moment capacity, correlated-gain strictness and gate scope.
