# RPB108 NF61 — inverse refinement of the frozen NF60 targets

NF61 starts from NF60 commit `db69f427046cc6eff5a615ca1d1c32dbae963042`
on `research/rpb108-phase-geometry-localization`. Both independent parity
validators pass. A single physical high direction is added in each parity,
with 149 new original native pairings and 149 new complete source covariances
independently checked in total. Both frozen targets have strictly positive
correlated inverse-reaction gain. Neither frozen target becomes positive;
both remain certified negative for the current minorant. Whole aperture
`1.06` remains open.

## Certified target results

The exact targets are NF60's frozen normalized vectors, originally recorded
by NF59 from NF58. The physical P3/T53 frame, all 56 signed target coordinates
and NF60's direct complete-source norm intervals are unchanged. Decimal
interval endpoints below are rounded outward; the checkpoint and validation
reports contain exact fractions.

| Parity | High dimension | NF60 target minorant | NF61 correlated gain | Best NF61 target minorant | Scalar status |
| --- | --- | --- | --- | --- | --- |
| Even | 18 → 19 | `[-5.5040106E-35, -3.6037102E-35]` | `[6.6502208E-37, 6.8062065E-37]` | `[-5.4375084E-35, -3.5356481E-35]` | NEGATIVE |
| Odd | 17 → 18 | `[-1.2752105E-31, -1.2669723E-31]` | `[1.5786415E-32, 1.5788766E-32]` | `[-1.1173463E-31, -1.1090847E-31]` | NEGATIVE |

The full entrywise joint-matrix classifications are recorded separately in
the checkpoint. A positive scalar target certifies only that direction of
the sufficient minorant. A negative scalar target rejects this minorant in
that direction. Neither is an actual negative original Weil form claim.

## Construction and independent proof

The original unshifted F112 operator retains the certified floor
`kappa = 207/1000`. The original archives and P3/T53 physical columns stay
fixed. Select from the remaining inverse response using NF60's directly
combined complete projected source. Use the established degree shell
112–436 even / 113–435 odd, midpoint down-rounding to denominator `10^100`,
exact physical projection off every old high direction, and rational upper
norm normalization. The selected coefficients are frozen before proof.
Midpoint selection is not sign evidence.

The producer reconstructs the new native and complete source pairings at
800 digits with degree-1700 moments. The independent validator does not
import the NF61 producer. It uses 900 digits and degree-1800 moments,
reconstructs the exact physical orthogonality and target normalization, and
integrates the prime-cell polynomial plus common polynomial together in
each cell. The endpoint logarithm, signed pole, regular N320 profile, all
13 prime cells, signed mixed terms, log square, projection errors, and
regular/pole infinite tails remain paid.

Certify positivity of the enlarged surplus and inverse denominator. For
the enlarged inverse denominator, a block inverse yields the target gain
`|z* (w - W N^-1 t)|^2 / (kappa^2 (s - t* N^-1 t))`.
The common source Gram cancels exactly; it is not subtracted as two
independently uncertain quantities. Both signed residuals and Schur
denominators certify a strictly positive gain.

Carry NF60's tighter complete-source norm interval forward unchanged.
Contract the enlarged high source cross against the fixed target before
the inverse quadratic. Intersect this grouped direct-source enclosure with
the NF60 old target interval plus correlated gain, and with the new full
entrywise target enclosure. The final intersection is nonempty and all
original analytic errors remain present.

## Remaining frontier

Exact remaining endpoint budgets are in the checkpoint. Rounded budgets
for the recorded fixed targets are:

- even: necessary additional gain strictly greater than 3.5356481E-35, sufficient endpoint gain strictly greater than 5.4375084E-35
- odd: necessary additional gain strictly greater than 1.1090847E-31, sufficient endpoint gain strictly greater than 1.1173463E-31

These are scalar target budgets, not sufficient conditions for positivity
of the full 56-dimensional joint gate. Where a target remains negative,
the next refinement must improve the physical inverse minorant. Where a
target is positive, the remaining signed joint directions and full matrix
gate still require certification. Historical witnesses and classifications
remain preserved.

All three original archives pass compressed and decompressed SHA-256 checks.
All 302 locally recovered historical scripts, notes and data files matched
the NF60 committed tree before these additions. Publication preserves every
parent blob and adds paths only. NF46's original byte-identical replay and
NF47's original physical floor remain intact. The certified whole-aperture
anchor is `21/20 = 1.05`; whole `53/50 = 1.06`, RH, F4, Lean and all-aperture
positivity remain open.

## Reproduction

Run from the repository root with authenticated originals in
`nf24-inputs/Weil/`. Use a fresh Python process for each parity.

```bash
python scripts/certify_native_joint_refinement_nf61_106.py --parity even --output notes/data/RPB108_NF61_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/certify_native_joint_refinement_nf61_106.py --parity odd --output notes/data/RPB108_NF61_ODD_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf61_106.py --certificate notes/data/RPB108_NF61_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF61_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
python scripts/validate_native_joint_refinement_nf61_106.py --certificate notes/data/RPB108_NF61_ODD_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF61_ODD_JOINT_REFINEMENT_VALIDATION_20261010.json
python scripts/summarize_native_joint_refinement_nf61_106.py
```

See `docs/TERMINOLOGY_RPB108_JOINT_REFINEMENT_NF61.md` for selection,
correlated gain, direct-source retention and the distinction between gates.
