# RPB108 NF53 — discharge the extended-shell precision barrier

Client date: 2026-10-09, America/Los_Angeles. Artifact suffixes and ledger
`date_UTC` retain the computation's 2026-10-10 UTC provenance.
Aperture: `53/50`. Starting NF52 commit:
`19c11a4f9f8f03b039fcb30a8addf4d96029c53c`.
Branch: `research/rpb108-phase-geometry-localization`.

NF53 certifies the extended degree-308/307 shell that NF52 could not enclose
at its 500-digit grid. It appends one physical high direction per parity,
preserving the recovered original archives, P, T53, and every inherited high
column. Both NF52 joint lower-bound witnesses become strictly positive under
the enlarged bound. New exact witnesses still reject the full joint bound;
original whole positivity at 1.06 remains open.

## Fixed physical domain and complete data

The candidate responds to the complete NF52 joint witness through the shared
minorant inverse `A0^-1 Xi`, with `Xi=(R,G)`, `R=PF LP`, `G=PF LT53`, and
`kappa=207/1000`. It uses Legendre degrees 112..308 even and 113..307 odd.
Response midpoint coordinates are down-rounded to denominator `10^100`,
projected off all inherited H columns using their exact physical Gram, and
divided by a rational upper norm. This selects a frozen exact polynomial;
the sign proofs separately certify it. Decimal midpoint inverses used for
selection do not supply positivity evidence.

The high families grow from eleven to twelve even columns and from ten to
eleven odd columns. Exact physical orthogonality to every inherited high
column is checked. The domain remains `f=P alpha+T53 beta+h`, `h in F112`;
the infinite remainder is controlled by the original NF47 physical floor.

| Newly certified pairings | even | odd | total |
| --- | ---: | ---: | ---: |
| Original native `Q(P,Y), Q(T53,Y), Q(H,Y), Q(Y,Y)` | 68 | 67 | 135 |
| Complete physical source pairings | 68 | 67 | 135 |

All 56 original joint sources, their Xi Gram, and inherited physical errors
remain unchanged. Complete source profiles retain the endpoint logarithm,
signed pole, degree-320 regular kernel, degree-40 pole approximation, and
all 13 original prime translation cells. With `a=53/50`, the uniform infinite
analytic payment remains

`eta=2a*4(106/125)^320/(1-106/125)+16(a/2)^41/41!`.

Native crosses pay `eta ||Y|| ||v||`. The frozen retained midpoint projection
pays `eta ||Y||+16 max halfwidth(low_source_coordinates)`; the independent
validator verifies coverage of its own coordinate enclosure. Every source
covariance pays `e_i n_j+e_j n_i+e_i e_j` with certified physical errors and
approximant norm upper bounds. No infinite source direction is discarded.

## Precision upgrade with exact custody

Simply increasing the integer grid would leave the finite analytic constants
too uncertain. The scoped precision module therefore upgrades the grid,
finite series cutoffs, explicit tails, and grid-dependent caches together.
The producer uses an 800-digit grid and moment degree 1300; the independent
validator uses 900 digits and moment degree 1400.

Before changing the grid, every inherited 500-digit source-profile interval
integer is multiplied by `10^300` or `10^400`. Its exact rational endpoints
and uncertainty remain identical. Historical certificate matrix endpoints
are likewise preserved as rational intervals. Old physical errors and norms
remain valid for the same analytic approximants. The new candidate's source
and all of its added entries are freshly reconstructed at the higher grid.

The producer/validator use respectively 1400/1600 outward atanh terms,
650/750 terms in the explicit-tail Machin pi formula, and 400/450
Euler–Maclaurin terms at harmonic endpoints 800/900 for Euler's constant.
The Bernoulli next-term remainder is paid. Basis, log2 and native-log caches
are cleared when the grid changes. Moment cache keys bind parity, cutoff,
precision and the precision-module hash; independent action keys also bind
the validator and certificate. Original archive inputs are never regenerated
or replaced by analytic caches.

The former raw source-square enclosure explosion is resolved: the new
source-square values are narrowly enclosed near 17.41573 even and 14.57557
odd, and both enlarged surplus and inverse-denominator positivity proofs
pass. These decimals describe the enclosure scale; exact rational endpoints
and residual/congruence proofs are in the certificates and validation reports.

## Shared inverse and independent witness checks

For the enlarged family, set `U=(A-kappa)H`, `C=H*(A-kappa)H`,
`N=C+U*U/kappa`, and `W=Xi*U`. Positive C and N establish

`Xi* A^-1 Xi <= Xi*Xi/kappa-W N^-1 W*/kappa^2`.

Subtracting this ceiling from the original native Gram of `(P,T53)` gives a
sufficient 56-direction joint lower matrix. The independent validator does
not import the NF53 producer. It reconstructs the source, integrates each
original prime cell's combined polynomial first, checks all 135 native and
135 source entries, authenticates the inherited chain and original floor,
and verifies the shared inverse, exact physical masses and witness signs.
The two evaluations share the explicit precision primitive; they use distinct
grids, moment cutoffs and native/source assembly routes.

The correlated rank-one gain from NF52 remains independently checked. For
`N+=[[N,t],[t*,s]]`, `W+=[W,w]`, and `delta=s-t* N^-1 t > 0`, it is

`(w-W N^-1 t)(w-W N^-1 t)*/(kappa^2 delta)`.

The common Xi Gram cancels exactly. Signed and null rank-one controls, joint
negative/null/positive controls, physical mass shifts, Hankel corner controls,
and the 13-cell mixed-log identity are verified. The old witness's direct new
value is intersected with its old value plus correlated gain. Both resulting
lower endpoints are strictly positive.

The following decimal enclosures round the exact independent intervals
outward. Each old witness is normalized using its original physical mass.

| Normalized NF52 witness | even | odd |
| --- | --- | --- |
| Correlated inverse-reaction gain | `[7.9677,7.9756] x 10^-35` | `[7.4781,7.4783] x 10^-31` |
| Refined lower value | `[7.2299,7.8415] x 10^-35` | `[6.4237,6.4264] x 10^-31` |

The enlarged joint lower matrices still admit new exact rational rejecting
witnesses in both parities. Their coefficients, original physical masses,
negative physical quotient intervals, and necessary next improvement bounds
are explicit in the records. A negative sufficient lower-bound value does
not establish a negative original Weil vector. Clearing two inherited
witnesses does not prove positivity of the complete matrix.

The aggregate ledger authenticates the compressed and decompressed SHA-256
hashes of all three recovered original archives again. NF48's byte-identical
literal NF46 replay and NF47's original unshifted floor remain the anchors.
This checkpoint is additive; historical scripts, inputs and vectors remain
unchanged.

## Remaining original gate and reproduction

The remaining gate is the complete original `D-B S^-1 B* >= 0` in both
parities, with the same high inverse for all original 56 sources. Whole
positivity at `53/50`, RH, F4 and Lean remain open. The highest certified
whole-aperture anchor remains `21/20`.

With the authenticated originals in `nf24-inputs/Weil/`, run per parity:

```sh
python scripts/certify_native_joint_refinement_nf53_106.py --parity even --output notes/data/RPB108_NF53_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf53_106.py --certificate notes/data/RPB108_NF53_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF53_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD` in fresh processes, then run
`python scripts/summarize_native_joint_refinement_nf53_106.py`.

