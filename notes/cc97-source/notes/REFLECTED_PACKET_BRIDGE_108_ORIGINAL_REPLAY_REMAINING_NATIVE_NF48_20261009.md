# RPB108 NF48 — original NF46 replay and remaining native transport

Date: 2026-10-09 (America/Los_Angeles). Aperture: `53/50`.
Parent checkpoint: NF47, `4b1cba2a490545758c4c9d4cadd7af1d9c5d5926`.
Original NF46 checkpoint: `6658ff2837838ab00b9b9c605fdd200d473c3293`.

## Scope and custody

This additive checkpoint recovers the three original NF17–NF19 Library inputs,
executes the unchanged historical NF46 selection, certification and independent
validation, and certifies the finite native part of the remaining-53 transport.
It retains NF37's exact three joined physical columns in each parity and NF47's
exact remaining frame. No source archive or physical vector is regenerated or
substituted. Historical scripts, notes and certificate bytes remain unchanged.

The supplied gzip bytes were installed in `nf24-inputs/Weil/` only after **all
three** decompressed JSON SHA-256 hashes matched the original loader:

| Original archive | Decompressed SHA-256 |
| --- | --- |
| `native112_N720_K620.json.gz` | `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81` |
| `native_boundary_columns_112_113.json.gz` | `da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee` |
| `native_boundary_114_115.json.gz` | `0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad` |

The original archives remain untracked. The replay manifest records both their
compressed and decompressed hashes and each fresh output's SHA-256. It closes
NF47's missing-input replay blocker without rewriting that historical record.
Final replay and independent-validation statuses are recorded in the data
files accompanying this note.

All three literal NF46 stages are **PASS_BYTE_IDENTICAL**: selection,
certification and independent validation. The NF48 replay record is **PASS**
and embeds the unchanged runner's historical NF47-labelled report. Its fresh
output hashes match the frozen NF46 files. This fully closes the original
missing-input replay blocker.

The freshly reproduced NF46 joined condensed margin is approximately
`[7.489332906151752e-23, 7.609234379592e-23]`, with the exact historical
certificate bytes preserved. NF47 discharges its original high-floor
hypothesis; the remaining transport condition below is separate.

## Exact native remaining block

Let `E` be the original 56-dimensional retained physical space per parity.
Let `P=(x,w,u)` be the unchanged joined physical columns, whose retained
projections are exactly mutually orthogonal. NF47 defines

`T53 = E intersect span(x,w,u)^perp`.

The producer uses the original rational two-constraint frame and imposes its
third constraint exactly. The independent validator reconstructs the frame
from the original retained coefficients, solves the two pivot coordinates,
and imposes the third constraint independently. It checks the frozen column
identities and exact frame conditions through the NF47 independent checks.

Every original signed interval in

`C53 = Q(T53,T53)`, `B0 = Q(T53,P)`

is paid. There are 1,431 symmetric native entries and 159 signed joined
couplings per parity: 2,862 and 318 entries respectively across both parities.
The certificate stores complete C53 interval matrices and displays B0
transposed, with three rows and 53 columns. Sparse frame expansion uses the
original signed `full` native intervals, including the original boundary
entries. It does not use a selected spectral replacement or diagonal estimate.

The frame is nonorthonormal. Its exact physical Gram is `M=T53* T53`.
The positive physical inverse trace is bounded by an outward rational interval
for `tr(C53^-1 M)`. Its upper endpoint `t` proves the physical native gap
`Q(g,g) >= (1/t) ||g||^2` on T53. Numerically the producer lower bounds are:

| Parity | Native physical gap lower bound | Finite joined last Schur margin |
| --- | ---: | ---: |
| even | approximately `1.210013983675892e-16` | `[3.4881095841054166e-22, 3.488325027179946e-22]` |
| odd | approximately `2.7057281915718575e-14` | `[2.8526222188174533e-19, 2.8526232230186314e-19]` |

These decimal displays are informational. Exact rational endpoints and all
inverse verification bounds are in the certificate and independent report.

## Signed source and finite reaction payments

For each frozen physical P column the original retained-source reconstruction
has a physical error `epsilon_i`. Every signed B0 entry pays
`epsilon_i ||T_j||`. The 56 retained-coordinate interval half-widths are paid
by a physical source ball

`r_i = epsilon_i + 8 max_k halfwidth(source_ik)`.

The factor 8 exceeds sqrt(56). Let `b_i` be the midpoint retained-source
coordinates projected into the T53 frame. The signed midpoint reaction is

`H_ij = b_i* C53^-1 b_j`.

With `e_i=r_i sqrt(t)` and `n_i=sqrt(upper(H_ii))`, the physical ball payment is

`e_i n_j + e_j n_i + e_i e_j`.

This pays the source errors in the inverse metric, using the exact physical
Gram through the inverse trace. It preserves the signed midpoint cross before
adding the symmetric error interval. The resulting reaction encloses the
original `B0* C53^-1 B0`.

The finite Schur matrix

`Q(P,P) - B0* C53^-1 B0`

is positive in both parities. Together with C53 positivity, this proves
positivity on the entire finite graph `span(P)+T53`, whose physical retained
projection covers all 56 retained coordinates. Arbitrary infinite high vectors
are not part of this graph.

## Independent validation

The NF48 validator does not import the NF48 producer. It independently expands
the original entries in reverse summation order with its own outward rational
interval implementation. Decimal Gaussian elimination chooses a rational
inverse candidate; no Decimal sign is accepted as a proof. An independently
constructed, column-solved unit-LDL congruence proves positive definiteness by
a rational Gershgorin lower bound. A rational residual norm below one bounds
the inverse entry error.

The validator reconstructs the physical Gram and original retained sources,
pays their physical source balls, checks agreement of the stored intervals,
and separately proves positive finite sequential Schur pivots. The report also
runs NF47's exact negative, null and positive block controls and whole-mass
shift controls. Original archive hashes and the NF47 certificate hash are
checked before these calculations.

The final independent report is **PASS** in both parities. Its independently
paid last-pivot lower endpoints are approximately `3.488186634743419e-22`
(even) and `2.852622541615889e-19` (odd).

## What remains for the original whole form

NF47's original unshifted high restriction `A=Q|F112` has the unconditional
physical floor `207/1000`. NF46 certifies the unchanged fixed joined Schur
packet after high condensation. Neither fact alone closes the remaining
transport. Define the complete original sources `R=PF L P`, `G=PF L T53` and
use the **same** infinite high inverse in all three blocks:

`S=Q(P,P)-R* A^-1 R`,

`D=C53-G* A^-1 G`,

`B=B0-G* A^-1 R`.

The remaining whole-domain condition is `D-B S^-1 B* >= 0` in both parities.
NF48 closes C53 and B0. The complete signed source data `G*G`, `G*R`, and
`G*U` for the existing high minorants, together with their reconstruction
errors and infinite remainders, still require certification and assembly.
Per parity the first two require 1,431 symmetric entries and 159 signed
entries; the existing high-minorant cross has 424 even / 371 odd entries.

Subtracting a fixed-packet high response from the separately finite-condensed
matrix is not justified: the G cross corrections and remaining high block
must be assembled before the final Schur gate. The positive finite result
does not pay omitted arbitrary high directions.

Whole-aperture original Weil positivity at `53/50`, RH, F4, all-aperture
continuation and Lean closure remain open. The highest certified whole-aperture
anchor remains `21/20`. No other investigation branch is restarted or changed.

## Reproduction

From the repository root, with the three authenticated originals installed:

```sh
python scripts/replay_native_frozen_nf46_nf47_106.py --inputs nf24-inputs/Weil --replay-selection
python scripts/certify_native_remaining_native_nf48_106.py --output notes/data/RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64
python scripts/validate_native_remaining_native_nf48_106.py --certificate notes/data/RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64 --output notes/data/RPB108_NF48_REMAINING_NATIVE_VALIDATION_20261009.json
```

The certificate is deterministic gzip (mtime zero) encoded as base64 text.
The independent report pins both its encoded and decompressed JSON SHA-256.
All 151 recovered NF10–NF46 files and the seven NF47 files were verified
against their pinned Git blob SHA values and remained unchanged.
