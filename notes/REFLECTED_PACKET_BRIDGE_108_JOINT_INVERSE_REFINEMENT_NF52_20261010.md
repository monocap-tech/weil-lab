# RPB108 NF52 — refine the complete NF51 joint witnesses

Date: 2026-10-10 UTC. Aperture: `53/50`.
Starting Native Source commit: `f9b3495c7f9e7c96f1a71cae16ee223de1575461` (NF51).
Branch: `research/rpb108-phase-geometry-localization`.

NF52 appends one high physical direction per parity to NF51's shared high
inverse bound. The original inputs, P, T53, and every inherited high column
remain fixed. The complete original high-condensed gate, rather than finite
native positivity alone, determines whole positivity.

## Selection and fixed domain

Write `Xi=(R,G)`, `R=PF L P`, `G=PF L T53`, `kappa=207/1000`,
`U=(A-kappa)H`, `C=H*(A-kappa)H`, `N=C+U*U/kappa`, and `W=Xi*U`.
Each final candidate uses a rational approximation to

`q=A0^-1 Xi z=Xi z/kappa-U N^-1 W* z/kappa^2`.

Here z is NF51's full joint negative lower-bound witness, divided by a rational
upper bound for its original physical norm. Selection includes all of its
P and T53 coordinates. Midpoint response coordinates on Legendre degrees
112..244 even and 113..243 odd are down-rounded to denominator `10^100`,
projected off every inherited H column using an exact rational physical Gram,
and normalized by a rational upper norm. Selection supplies a fixed polynomial;
it does not supply a sign proof.

The new high families have eleven even and ten odd columns. Exact physical
orthogonality to the full old family is verified, including the directions
appended in NF50 and NF51. The original decomposition
`f=P alpha+T53 beta+h`, `h in F112`, remains unchanged. No infinite high
direction is discarded.

## Added original data and infinite payments

All original signed native pairings `Q(P,Y)`, `Q(T53,Y)`, `Q(H,Y)`, `Q(Y,Y)`
and all corresponding complete physical source pairings are certified:

| Added pairings | even | odd | total |
| --- | ---: | ---: | ---: |
| Original native | 67 | 66 | 133 |
| Complete physical source | 67 | 66 | 133 |

The source profiles retain the analytic endpoint logarithm, signed pole,
degree-320 regular archimedean kernel, degree-40 pole approximation and all
13 original prime translation cells. Infinite analytic remainders use

`eta=2a*4(106/125)^320/(1-106/125)+16(a/2)^41/41!`, `a=53/50`.

Native crosses pay `eta ||Y|| ||v||`. The frozen retained midpoint projection
pays `eta ||Y||+16 max halfwidth(low_source_coordinates)`; the validator
proves this error covers its own retained coordinate enclosure. Each signed
source covariance pays `e_i n_j+e_j n_i+e_i e_j`. Inherited source errors and
approximant norms remain authenticated through the passed NF51/NF50/NF49
records. The original complete Xi Gram from NF49 is unchanged.

For `H+=(H,Y)`, the enlarged high native/source blocks and all joint crosses
are assembled together. Positive surplus C+ and inverse denominator N+ give
the shared original inverse ceiling

`Xi* A^-1 Xi <= Xi*Xi/kappa-W+ N+^-1 W+*/kappa^2`.

Subtracting this ceiling from the original native Gram of `(P,T53)` gives
one sufficient 56-direction joint lower matrix per parity. A negative value
under this lower matrix rejects the selected bound; it does not establish
a negative original Weil vector.

## Independent validation and custody

The producer uses moment degree 1200. The independent validator does not
import the NF52 producer. It rebuilds the new physical source with degree-1300
analytic moments, integrates each original translation cell's combined
polynomial first, and uses ceiling-centered Hankel intervals. It checks all
added native/source pairings, physical error payments, exact orthogonality,
the complete shared inverse, rational congruence/residual positivity proofs,
and exact witness quadratic values and original physical masses.

Passed analytic moments are reusable because they depend on parity and
cutoff, not the new polynomial. Private caches contain only internally
generated objects; action keys also bind the validator and certificate.
Original input archives are not generated from caches or substituted by them.
Exact negative/null/positive joint controls, physical mass shifts, Hankel
corner controls and the signed 13-cell mixed-log identity are checked.

The aggregate ledger rechecks compressed bytes and the required decompressed
SHA-256 hashes of all three recovered originals. The NF48 literal NF46 replay,
NF47 original unshifted physical floor, and all historical coefficients remain
the authenticated anchors. The branch update adds new records without editing
those inputs or prior checkpoints.

## Correlated rank-one inverse gain

NF52 adds an independent correlated gain check. Partition the enlarged
inverse denominator as `N+=[[N,t],[t*,s]]` and the joint surplus crosses as
`W+=[W,w]`. Then `delta=s-t* N^-1 t > 0`, and the exact inverse-reaction
improvement is

`(w-W N^-1 t)(w-W N^-1 t)*/(kappa^2 delta)`.

For the fixed old witness z, its scalar gain is the square of the signed
residual `z*(w-W N^-1 t)`, divided by `kappa^2 delta`. This cancels the common
Xi Gram exactly. Subtracting separately enclosed reaction matrices pays that
same Gram's uncertainty twice and can leave a positive gain unresolved.
The validator independently certifies the positive denominator and strictly
positive gain, checks signed and null exact rank-one controls, and intersects
the correlated old-value-plus-gain enclosure with the direct new value.

## Exact result and remaining gate

Both inherited NF51 witnesses have strictly positive certified correlated
inverse-reaction improvements. Their final values and the complete joint
matrix status remain explicit in the independent reports and checkpoint.
Both old NF51 witnesses remain strictly negative under the refined lower
bound. New rejecting witnesses include exact coefficients, original physical
masses and certified physical quotients. The following decimal enclosures
round the exact independent correlated intervals outward:

| Normalized NF51 witness | even | odd |
| --- | --- | --- |
| Correlated inverse-reaction gain | `[3.0499,3.0708] x 10^-36` | `[1.5157,1.5159] x 10^-31` |
| Refined lower value | `[-5.8202 x 10^-36,-2.8829 x 10^-37]` | `[-1.5168,-1.4994] x 10^-32` |

An attempted extension to degree 308 at the same 500-digit grid failed to
certify positivity of the inverse denominator: its raw source-square
intervals became too wide. This is an enclosure failure, not a negative
original source norm. The final certificates retain the validated degree-244
polynomials and their complete physical source payments. Further extension
requires greater precision or a better-conditioned representation, together
with fresh certification of every added native/source entry. Original input
archives and historical vectors remain fixed throughout.

The remaining original whole gate is `D-B S^-1 B* >= 0` in both parities,
using the same high inverse for all original 56 sources. Whole positivity at
`53/50` remains open; the highest certified whole-aperture anchor is `21/20`.
RH, F4 and Lean remain open.

## Reproduction

With the authenticated originals in `nf24-inputs/Weil/`, run per parity:

```sh
python scripts/certify_native_joint_refinement_nf52_106.py --parity even --output notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf52_106.py --certificate notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD`, then run
`python scripts/summarize_native_joint_refinement_nf52_106.py`.
