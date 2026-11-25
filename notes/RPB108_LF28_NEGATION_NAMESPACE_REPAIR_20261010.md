# RPB108 LF28 — Negation transport namespace repair

## Change

Qualify all three reflection measure-preservation calls as
`Measure.measurePreserving_neg`. The pinned Mathlib source declares the
multiplicative original `measurePreserving_inv` inside `namespace Measure`,
with its additive negation counterpart generated in the same namespace.
This corrects the shared reflection dependency in the left physical-tail L2
transport and both left exterior kernel transport proofs.

## Validation evidence

LF27 commit `6289689e3f4e3555191aa2031b66312dde8ad188`, run
38106362945, job 114372645685, compiled the endpoint squared-log/tail L2
module again. ExteriorSplit reported only two unknown identifiers
`measurePreserving_neg`; CapL2 reported only one identical error.
CapExtension remained downstream and unbuilt. The full-root and unfinished
trusted-declaration steps were skipped after these target failures.

LF28 is submitted for fresh cumulative kernel checking; lack of additional
diagnostics in LF27 is not a compilation certificate for either failed module.
No theorem premise or mathematical conclusion is changed, and no unfinished
proof or axiom is introduced.

## Next cursor

After cumulative checking, complete the actual complex jump integral for a
zero-extended trial from internal cap integration and the two exterior tail
identities. Mixture exchange, physical weak action and spectral source identity
remain open. No new aperture positivity, F4 or RH claim.
