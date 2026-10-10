# RPB108 NF51 — recover NF50 and refine its complete joint witnesses

Date: 2026-10-10 UTC. Aperture: `53/50`.
Recovered Native Source head: `c576e34dc445b029f1846119e83a8146fc9706df` (NF50).
Branch: `research/rpb108-phase-geometry-localization`.

NF51 appends one high physical direction per parity, selected from the full
NF50 joint witness. Both NF50 rejecting witnesses become strictly positive
under the new sufficient lower matrix. New exact rational witnesses still
reject the complete 56-direction bound in both parities. Whole positivity at
1.06 remains open; the highest certified whole-aperture anchor remains 1.05.

## Recovered and fixed objects

The three original NF17–NF19 frozen archives remain byte-identical to the
recovered Library originals. The aggregate ledger verifies both compressed
hashes and the required decompressed SHA-256 values. No archive is regenerated
or substituted. The passed NF48 literal NF46 replay and NF47 original
unshifted physical floor `A >= (207/1000) I` remain the authenticated anchors.

NF51 preserves every P column, every T53 column, all NF49 high columns, and
both appended NF50 high polynomials. The new high families have ten even and
nine odd columns. Each new Y is in F112 and is exactly physically orthogonal
to the full inherited high family, including NF50's appended direction.

The complete Xi Gram from NF49 remains unchanged, with `Xi=(R,G)`,
`R=PF L P` and `G=PF L T53`. NF50's native/source high matrices and all joint
crosses are inherited together through its passed certificate and validation
hashes. The validator follows that authentication chain back through NF49.

## Full joint response and new source data

For the inherited family H, let `U=(A-kappa)H`,
`C=H*(A-kappa)H`, `N=C+U*U/kappa`, `W=Xi*U`, `kappa=207/1000`.
The selected response approximates

`q=A0^-1 Xi z=Xi z/kappa-U N^-1 W* z/kappa^2`,

where z is NF50's complete rational joint witness, divided by a rational
upper bound for its original physical norm. Selection includes both P and
T53; it does not replace the remaining transport by a joined-only source.

Response coordinates use physical Legendre degrees 112..244 even and
113..243 odd. Midpoints are down-rounded to denominator 10^100, projected
off every inherited high polynomial through an exact rational physical Gram
solve, and normalized by a rational upper norm. Selection is only candidate
generation. All signs below use paid original data and exact rational values.

For each new Y, NF51 certifies the signed original native pairings and complete
physical source pairings against P, T53, all inherited H, and Y itself:

| Added certified data | even | odd | total |
| --- | ---: | ---: | ---: |
| Original native pairings | 66 | 65 | 131 |
| Complete physical source pairings | 66 | 65 | 131 |

The endpoint logarithm, signed pole, degree-320 regular archimedean kernel,
degree-40 pole approximation, and all 13 original prime translation cells
remain in each complete source. Infinite analytic remainders use

`eta=2a*4(106/125)^320/(1-106/125)+16(a/2)^41/41!`, `a=53/50`.

Native entries pay `eta ||Y|| ||v||`. The frozen retained midpoint projection
pays `eta ||Y||+16 max halfwidth(low_source_coordinates)`; the independent
validator proves this covers its own retained enclosure. Signed source
crosses pay `e_i n_j+e_j n_i+e_i e_j`. No covariance or infinite tail is dropped.

## Shared inverse and independent proof

For `H+=(H,Y)`, both enlarged C+ and N+ are independently certified positive.
The original form has the sufficient joint lower bound obtained by subtracting

`Xi*Xi/kappa-W+ N+^-1 W+*/kappa^2`

from its original native Gram on `(P,T53)`. Every block uses that same shared
inverse. The NF48 finite native gate is not combined with an unrelated high
response bound.

The producer integrates at moment degree 1200. The independent validator
does not import the NF51 producer, rebuilds the new source at degree 1300,
and integrates each original translation cell's combined polynomial first.
Ceiling-centered Hankel enclosures and independent rational inverse/congruence
proofs check all added data, the complete assembled matrix, physical errors,
exact high orthogonality, witness masses and final signs. The passed NF50
degree-1300 analytic moments are reusable because moment construction depends
on parity and cutoff, not the new polynomial. Private caches contain only
internally generated data; original archives and frozen certificates remain
the inputs. Action caches bind the certificate as well as the validator.

Exact negative/null/positive joint controls, physical mass shifts, Hankel
endpoint-corner controls and the signed 13-cell mixed-log identity pass.
Floating arithmetic chooses inverse and witness candidates only.

## Result and next gate

The checkpoint ledger records the exact independent intervals for both old
NF50 witnesses before and after refinement and their inverse-reaction gains.
Both old values have negative upper endpoints; both new values have positive
lower endpoints. This clears those specific obstructions to the lower bound.

The first nonpositive midpoint LDL pivot moves from index 8 to 9 even and
from index 6 to 9 odd. New frozen rational witnesses independently have
strictly negative values under the enlarged lower matrix. Their coefficients,
exact original physical masses and negative physical quotients are in the
parity certificates and validation reports. Midpoint LDL only locates these
candidates; exact interval quadratic values certify their signs.

A negative value under this sufficient lower matrix rejects the selected
minorant proof. It does not establish a negative original Weil vector. The
remaining original gate is still `D-B S^-1 B* >= 0` in both parities, with the
same high inverse acting on all original 56 sources. The negative upper
quotient of each new witness determines a necessary, not sufficient, physical
inverse-reaction improvement for the next refinement. RH, F4, Lean and whole
positivity at `53/50` remain open.

## Reproduction

With the authenticated originals under `nf24-inputs/Weil/`, run each parity:

```sh
python scripts/certify_native_joint_refinement_nf51_106.py --parity even --output notes/data/RPB108_NF51_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64
python scripts/validate_native_joint_refinement_nf51_106.py --certificate notes/data/RPB108_NF51_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64 --output notes/data/RPB108_NF51_EVEN_JOINT_REFINEMENT_VALIDATION_20261010.json
```

Repeat with `odd` and `ODD`, then run
`python scripts/summarize_native_joint_refinement_nf51_106.py`.
