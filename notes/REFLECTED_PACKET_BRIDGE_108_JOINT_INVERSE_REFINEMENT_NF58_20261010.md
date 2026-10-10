# RPB108 NF58 — refine the unresolved even probe and odd rejection

Client date: 2026-10-09, America/Los_Angeles. Artifact suffixes and ledger
`date_UTC` retain 2026-10-10 UTC provenance. Aperture: `53/50`.
Starting NF57 commit: `bd860a44481a58425f858aaf86cb61b3e192e2ec`.
Branch: `research/rpb108-phase-geometry-localization`.

NF58 appends one physical high direction per parity while preserving the
recovered original archives, P, T53 and every inherited high column. Its even
target is the first frozen NF57 sign-probe direction, whose certified
lower-matrix enclosure spans zero. Its odd target is NF57's exact certified
rejecting witness. The even target is not reclassified as a negative witness.
Both target records, their original physical masses and their provenance are
authenticated independently.

Target values and gains use the recorded rational upper bound on the
original target's physical norm. A rejecting witness's physical quotient
instead divides its quadratic value by its exact original physical mass
squared. Neither normalization changes a certified sign.

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
checked. The high families grow to seventeen even and sixteen odd columns.

The original domain remains `f=P alpha+T53 beta+h`, `h in F112`. NF47's
unshifted physical floor controls every remaining infinite high direction.
All 56 original joint sources and the original complete Xi/native Grams stay
fixed. Added data include every original signed native and source cross:

| New certified pairings | even | odd | total |
| --- | ---: | ---: | ---: |
| `Q(P,Y), Q(T53,Y), Q(H,Y), Q(Y,Y)` | 73 | 72 | 145 |
| Complete physical source pairings | 73 | 72 | 145 |

## Analytic payments and independent validation

The producer uses an 800-digit grid and degree-1700 moments; the independent
validator uses 900 digits and degree 1800. Both retain the unchanged, pinned
NF53 precision primitive with explicit atanh, Machin pi and
Euler–Maclaurin tails. Historical 500-digit source intervals are promoted
exactly; NF53–NF57 appended sources are reconstructed at the current grid
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

The validator does not import the NF58 producer. It uses the larger moment
cutoff and integrates each original cell's combined polynomial first. It
checks all new native/source entries, physical error payments, exact high
orthogonality, target physical masses, enlarged inverse proofs and witness
signs. The routes share the precision primitive but use distinct grids and
native/source assembly routes. Signed/null rank-one, negative/null/positive
joint, physical mass, Hankel corner and mixed-log cell controls are included.

NF58 retains NF57's degree-436/435 response shell and uses degree
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

## Certified results and quantified remaining gap

Both independent validators and the aggregate checkpoint return `PASS`.
All 145 added native pairings and 145 complete physical source pairings
are covered. The following intervals are rounded outward; exact rational
endpoints remain in the validation records. Target values and gains use
the recorded rational upper norm described above.

| Independent result | even NF57 probe | odd NF57 witness |
| --- | ---: | ---: |
| Old lower value | `[-8.98612, 8.55193] e-33` | `[-2.05108, -1.98546] e-30` |
| Correlated inverse-reaction gain | `[0.178183, 0.178387] e-33` | `[6.55789, 6.55793] e-30` |
| New intersected lower value | `[-8.80793, 8.73032] e-33` | `[4.50682, 4.57247] e-30` |
| Fixed target resolved positive | no | yes |
| Complete joint lower-matrix status | `UNRESOLVED` | `JOINT_LOWER_BOUND_REJECTED` |

The even gain is strictly positive, but its new enclosure still spans zero.
The old enclosure width is about `1.753804 e-32`; the guaranteed correlated
gain is about 1.016% of that width. The ledger stores the exact old width,
gain-to-width ratio and new width. These quantities describe the recorded
enclosure gap; they do not identify its sole cause, predict convergence,
or certify the actual original form's sign.

Lifting this fixed target's recorded lower endpoint would require an
additional guaranteed correlated gain strictly greater than approximately
`8.807929808823024 e-33`, or a tighter valid enclosure. The ledger retains
the exact endpoint budget. This is sufficient for this recorded enclosure,
not a necessary gain for the actual form or a sufficient condition for
the complete matrix.

The complete even producer matrix still first reaches a nonpositive
midpoint LDL pivot at index 15. A separate pass examines all 56 midpoint
pivots and freezes 14 rational candidates with denominator `10^120`.
Exact interval quadratic evaluation, including each original physical
mass, leaves all 14 enclosures spanning zero. The candidate count changed
from NF57's 15 to 14; midpoint selection and this count do not certify
positivity of the entire matrix.

The complete odd matrix has a new exact rational rejecting witness at
midpoint pivot index 16. Independent reconstruction certifies its original
physical quotient inside `[-2.90024, -1.62149] e-31`. This rejects the
sufficient lower bound, not the original Weil form. The exact witness,
physical mass and signed quotient remain in the certificate and validation.

The next gate must address the quantified even gap through tighter valid
complete source/inverse enclosures or further certified response directions,
resolve the new odd rejecting direction, and establish the original complete
Schur inequality in both parities. Whole aperture `53/50` (1.06) remains
open; the highest certified whole-aperture anchor remains `21/20` (1.05).
RH, F4, Lean and all-aperture closure remain open. No original archive,
historical script, certificate or frozen vector was edited.

## Reproduction

With authenticated originals in `nf24-inputs/Weil/`, run in fresh processes:

```sh
python scripts/certify_native_joint_refinement_nf58_106.py --parity even --output notes/data/RPB108_NF58_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf58_106.py --certificate notes/data/RPB108_NF58_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF58_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD`, then run
`python scripts/probe_native_joint_sign_nf58_106.py` followed by
`python scripts/summarize_native_joint_refinement_nf58_106.py`.

