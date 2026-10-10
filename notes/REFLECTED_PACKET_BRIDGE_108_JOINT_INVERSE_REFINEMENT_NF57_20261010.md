# RPB108 NF57 — refine the unresolved even probe and odd rejection

Client date: 2026-10-09, America/Los_Angeles. Artifact suffixes and ledger
`date_UTC` retain 2026-10-10 UTC provenance. Aperture: `53/50`.
Starting NF56 commit: `b7bb22586ea8dc398813c5f80e84dbe8ebee9b15`.
Branch: `research/rpb108-phase-geometry-localization`.

NF57 appends one physical high direction per parity while preserving the
recovered original archives, P, T53 and every inherited high column. Its even
target is the first frozen NF56 sign-probe direction, whose certified
lower-matrix enclosure spans zero. Its odd target is NF56's exact certified
rejecting witness. The even target is not reclassified as a negative witness.
Both target records, their original physical masses and their provenance are
authenticated independently.

## Complete response and fixed domain

With `Xi=(R,G)`, `R=PF LP`, `G=PF LT53`, and `kappa=207/1000`, selection uses
the complete joint minorant-inverse response to each physically normalized
target. For `U=(A-kappa)H`, `C=H*(A-kappa)H`, `N=C+U*U/kappa`, `W=Xi*U`,
the response is

`A0^-1 Xi z=Xi z/kappa-U N^-1 W* z/kappa^2`.

Coordinates on degrees 112..436 even and 113..435 odd are down-rounded to
denominator `10^100`, projected off all inherited H columns using an exact
rational physical Gram, and divided by a rational upper norm. These frozen
coefficients select a physical polynomial; midpoint computations do not
supply sign evidence. Exact orthogonality and normalization are independently
checked. The high families grow to sixteen even and fifteen odd columns.

The original domain remains `f=P alpha+T53 beta+h`, `h in F112`. NF47's
unshifted physical floor controls every remaining infinite high direction.
All 56 original joint sources and the original complete Xi/native Grams stay
fixed. Added data include every original signed native and source cross:

| New certified pairings | even | odd | total |
| --- | ---: | ---: | ---: |
| `Q(P,Y), Q(T53,Y), Q(H,Y), Q(Y,Y)` | 72 | 71 | 143 |
| Complete physical source pairings | 72 | 71 | 143 |

## Analytic payments and independent validation

The producer uses an 800-digit grid and degree-1700 moments; the independent
validator uses 900 digits and degree 1800. Both retain the unchanged, pinned
NF53 precision primitive with explicit atanh, Machin pi and
Euler–Maclaurin tails. Historical 500-digit source intervals are promoted
exactly; NF53–NF56 appended sources are reconstructed at the current grid
with their frozen retained midpoint projections. Inherited matrix endpoints,
physical errors and norm bounds remain unchanged.

Previously certified analytic moments are reused only at the same parity,
cutoff, precision and precision-module hash. New source caches bind the
fixed polynomial; independent action keys also bind the validator and
certificate. Original inputs are never regenerated or replaced by caches.

Complete profiles retain the endpoint logarithm, signed pole, degree-320
regular kernel, degree-40 pole approximation and all 13 original prime cells.
With `a=53/50`, the infinite analytic payment remains

`eta=2a*4(106/125)^320/(1-106/125)+16(a/2)^41/41!`.

Native crosses pay `eta ||Y|| ||v||`. The retained midpoint projection pays
`eta ||Y||+16 max halfwidth(low_source_coordinates)` and must cover the
independent coordinate enclosure. Every source covariance pays
`e_i n_j+e_j n_i+e_i e_j` using certified physical errors and norm bounds.
No endpoint logarithm, signed pole, original prime cell, cross covariance or
infinite remainder is omitted.

The validator does not import the NF57 producer. It uses the larger moment
cutoff and integrates each original cell's combined polynomial first. It
checks all new native/source entries, physical error payments, exact high
orthogonality, target physical masses, enlarged inverse proofs and witness
signs. The routes share the precision primitive but use distinct grids and
native/source assembly routes. Signed/null rank-one, negative/null/positive
joint, physical mass, Hankel corner and mixed-log cell controls are included.

NF57 expands the degree-436/435 response shell from NF56 degrees 372/371, and uses degree
1700/1800 moment cutoffs. The regular polynomial source square can reach
degree 1512. Every pairing for the newly selected polynomials is freshly
certified; all inherited physical columns remain fixed.

## Shared inverse, target gain and remaining gate

Positive enlarged surplus C and inverse denominator N establish

`Xi* A^-1 Xi <= Xi*Xi/kappa-W N^-1 W*/kappa^2`.

Subtracting that ceiling from the original `(P,T53)` native Gram gives a
sufficient 56-direction joint lower matrix per parity. A negative value
under this lower matrix rejects that bound; it does not establish a negative
original Weil vector. A span-zero enclosure leaves the tested sign unresolved.

The independent correlated gain cancels the common Xi Gram exactly. For
`N+=[[N,t],[t*,s]]`, `W+=[W,w]`, `delta=s-t* N^-1 t > 0`, it is

`(w-W N^-1 t)(w-W N^-1 t)*/(kappa^2 delta)`.

Each target's directly enclosed new value is intersected with its old value
plus this correlated gain. Even's old value is checked to span zero; odd's
old upper endpoint is checked to be negative. Positive gain and positive
target value are separate conclusions from complete matrix positivity.

The aggregate ledger reauthenticates compressed and decompressed hashes of
all three recovered original archives. NF48's byte-identical literal NF46
replay, NF47's unshifted physical floor and all historical vectors remain
the anchors. This checkpoint adds new files without editing historical
records. The original whole gate remains `D-B S^-1 B* >= 0` in both parities
with the same high inverse for all original 56 sources.

## Certified results and remaining obstruction

Both independent validators and the aggregate checkpoint return `PASS`.
All 143 added native pairings and 143 complete physical source pairings
are covered. The following intervals are rounded outward; exact rational
endpoints remain in the validation records. Target values and gains use
the fixed target's original physical normalization.

| Independent result | even NF56 probe | odd NF56 witness |
| --- | ---: | ---: |
| Old lower value | `[-6.51505, 5.28603] e-33` | `[-0.227978, -0.0342720] e-30` |
| Correlated inverse-reaction gain | `[5.89420, 5.89490] e-33` | `[7.01673, 7.01676] e-30` |
| New intersected lower value | `[-0.620845, 11.18093] e-33` | `[6.78875, 6.98249] e-30` |
| Fixed target resolved positive | no | yes |
| Complete joint lower-matrix status | `UNRESOLVED` | `JOINT_LOWER_BOUND_REJECTED` |

The even gain is strictly positive, but the certified new enclosure still
spans zero. Its recorded lower endpoint would require an additional
guaranteed correlated gain strictly greater than approximately
`6.208441174004043 e-34`, or a tighter valid enclosure, to certify this
fixed target positive. The ledger retains the exact endpoint budget.
This is sufficient for this target's recorded enclosure; it is neither a
necessary gain for the actual form nor sufficient for the complete matrix.

The complete even producer matrix first reaches a nonpositive midpoint LDL
pivot at index 15, compared with index 13 in NF56. This midpoint progression
is not a sign proof. A separate pass examines all 56 midpoint pivots and
freezes 15 rational candidates with denominator `10^120`. Exact interval
quadratic evaluation, including each original physical mass, leaves all 15
enclosures spanning zero. None is a certified negative original-form vector.

The complete odd matrix has a new exact rational rejecting witness at
midpoint pivot index 15. Independent reconstruction certifies its original
physical quotient inside `[-2.05738, -1.97915] e-30`. This rejects the
sufficient lower bound, not the original Weil form. The exact witness,
physical mass and signed quotient remain in the certificate and validation.

The next gate must resolve the remaining complete even signs and the new
odd rejecting direction, then establish the original complete Schur
inequality in both parities. Whole aperture `53/50` (1.06) remains open;
the highest certified whole-aperture anchor remains `21/20` (1.05).
RH, F4, Lean and all-aperture closure remain open. No original archive,
historical script, certificate or frozen vector was edited.

## Reproduction

With authenticated originals in `nf24-inputs/Weil/`, run in fresh processes:

```sh
python scripts/certify_native_joint_refinement_nf57_106.py --parity even --output notes/data/RPB108_NF57_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf57_106.py --certificate notes/data/RPB108_NF57_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF57_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD`, then run
`python scripts/probe_native_joint_sign_nf57_106.py` followed by
`python scripts/summarize_native_joint_refinement_nf57_106.py`.

