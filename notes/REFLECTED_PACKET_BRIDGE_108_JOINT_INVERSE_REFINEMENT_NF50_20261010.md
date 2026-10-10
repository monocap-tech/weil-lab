# RPB108 NF50 — refine the complete joint high inverse

Date:2026-10-10 UTC. Aperture:`53/50`.
Starting Native Source commit:NF49,
`2849eaa241412e2deef47e58462269112cde195b`.

NF50 appends one high direction per parity to the NF49 shared inverse bound.
Both original NF49 negative lower-bound witnesses become strictly positive
under the enlarged lower bound. New exact rational witnesses still reject
the full56-direction lower matrix in both parities. Whole positivity at1.06
remains open; the highest certified whole-aperture anchor remains1.05.

## Original objects and custody

The original NF17–NF19 compressed archives are authenticated again, including
their compressed bytes and decompressed payloads. None is regenerated or
substituted. The historical NF46 byte-identical replay, original NF47 physical
F112 floor, NF48 native finite gate, and NF49 complete signed source data are
inherited through the passed, hash-pinned records.

P, all53 T53 columns, and all eight even/seven odd inherited H columns retain
their exact physical coefficients. NF50 appends Y; the enlarged high families
have nine even/eight odd columns. Y is in F112 and is exactly physically
orthogonal to every inherited high column. It does not alter the decomposition
`f=P alpha+T53 beta+h` or discard any remaining source direction.

## Selection from the complete joint witness

Let `Xi=(R,G)` with `R=PF L P`, `G=PF L T53`, and `kappa=207/1000`.
For the old high family let

`U=(A-kappa)H`, `C=H*(A-kappa)H`, `N=C+U*U/kappa`, `W=Xi*U`.

The previous minorant is `A0=kappa I+U C^-1 U* <= A`. NF50 uses a rational
approximation to the full inverse response

`q=A0^-1 Xi z=Xi z/kappa-U N^-1 W* z/kappa^2`.

Here z is NF49's exact joint negative lower-bound witness, divided by a
rational upper bound for its original physical norm. It includes both P and
T53 coordinates. Decimal calculations and interval midpoints select a
candidate only; they do not certify its sign.

Selection evaluates q on physical Legendre degrees112..244 even and113..243
odd, down-rounds midpoint coefficients to denominator10^100, projects them
off the entire original H span using its exact rational physical Gram, and
normalizes by a rational upper norm. The original H span is contained in
these shells. Exact coefficients, the projection solve, normalization and
selection coordinates are frozen in the parity certificates.

## Complete original data for the appended direction

All added original native pairings `Q(P,Y)`, `Q(T53,Y)`, `Q(H,Y)` and `Q(Y,Y)`
are paid. All added complete physical source pairings with `PF L Y` are paid
as well, including its square. There are65 native and65 source entries even,
64 native and64 source entries odd:129 of each in total.

The complete source retains the endpoint logarithm, signed pole, regular
archimedean kernel degree320, pole approximation degree40, and13 original
prime translation cells. Analytic infinite tails use the original error

`eta=2a*4(106/125)^320/(1-106/125)+16(a/2)^41/41!`, `a=53/50`.

The new retained coordinates are enclosed by complete original source
integration. The frozen midpoint projection has a conservatively paid error
`eta ||Y||+16 max halfwidth(low_source_coordinates)`. The analytic physical
projection needs only a factor8 since `sqrt(56)<8`; the larger payment covers
both integration orders about the same frozen midpoint. The independent
validator explicitly proves this stored error covers its own source and
retained-coordinate enclosure.

Every signed source cross pays `e_i n_j+e_j n_i+e_i e_j`; no covariance is
discarded. NF49's complete Xi Gram is inherited unchanged. Native/source
high blocks and all joint crosses are enlarged together, using one shared
inverse for all56 sources.

## Enlarged minorant and independent checks

For `H+=(H,Y)`, the surplus C+ and inverse denominator N+ are independently
certified positive by rational congruence and residual proofs. The new inverse
ceiling is

`Xi* A^-1 Xi <= Xi*Xi/kappa-W+ N+^-1 W+*/kappa^2`.

Subtracting this ceiling from the original native Gram of `(P,T53)` produces
the new sufficient joint lower matrix. Both the lifted old witnesses and the
new rejecting witnesses use this same full matrix.

The producer uses moment degree1200 and outward global/cell Hankel actions.
The independent validator does not import the NF50 producer. It rebuilds the
new physical source at degree1300, integrates each original translation cell's
combined polynomial first, uses ceiling rather than floor interval centers,
and checks every added native/source entry and its physical error payment.
It independently reconstructs the T53 constraints and original physical
columns, authenticates the passed NF49 source data, and proves exact new
high orthogonality and rational final signs. Exact negative/null/positive
joint controls, mass shifts, Hankel corner controls and the signed13-cell
mixed-log identity are checked.

## Result and next exact gate

The machine-readable checkpoint records exact independent rational intervals
for the old witness values, new witness values, and inverse-reaction gains.
Both old witnesses are strictly negative under the old lower bound and
strictly positive under the enlarged lower bound. Thus the improvement clears
those specific NF49 obstructions, rather than merely reducing their width.

The following decimal enclosures round the exact independent intervals
outward. Old-witness values use its rational upper-norm normalization; the
new rejecting witnesses use their exact original physical masses.

| Independent quantity | even | odd |
| --- | --- | --- |
| Old NF49 witness, enlarged lower value | `[4.4045,4.4520] x 10^-35` | `[1.3900,1.3902] x 10^-31` |
| Old NF49 witness, inverse-reaction improvement | `[4.4917,4.5740] x 10^-35` | `[1.3928,1.3931] x 10^-31` |
| New rejecting witness, physical lower quotient | `[-1.1445 x 10^-34,-9.2813 x 10^-35]` | `[-6.7316,-6.7199] x 10^-32` |

The first nonpositive midpoint LDL pivot moves from index6 to8 even and from
index3 to6 odd. These indices locate the selected rational witnesses; the
certified signs come from exact interval quadratic values, not midpoint LDL.

The full enlarged matrix still admits a new exact rational negative
lower-bound witness in each parity. Its original physical mass and quotient
are independently certified. The negative sign rejects the selected lower
bound; it does not establish an original negative Weil vector. The negative
upper endpoint of each new quotient gives a necessary, not sufficient,
physical inverse-reaction improvement for the next refinement.

The remaining whole gate is the original shared high-condensed condition
`D-B S^-1 B* >= 0` in both parities. Refinement must target the new complete
joint sources, continue paying all omitted/infinite directions, and keep the
same original native objects. RH,F4,Lean and whole positivity at53/50 remain
open.

## Reproduction

With the three original archives under `nf24-inputs/Weil/`, run per parity:

```sh
python scripts/certify_native_joint_refinement_nf50_106.py --parity even --output notes/data/RPB108_NF50_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf50_106.py --certificate notes/data/RPB108_NF50_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF50_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD`, then run
`python scripts/summarize_native_joint_refinement_nf50_106.py`.
Private caches contain only internally generated objects under `work/`;
the original archives and frozen repository certificates remain the inputs.
