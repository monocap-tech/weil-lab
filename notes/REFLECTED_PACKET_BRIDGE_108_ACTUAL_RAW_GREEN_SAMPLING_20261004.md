# RPB-108 — raw actual-divisor sampling of Green synthesis (2026-10-04 UTC)

Parent research head: `10c426cff9afdf3c503fa84570b468bb830b91cd`.

## Definitions before use

Raw window evaluation E(a,z,f) is the integral of f(x)exp(i*z*x) over [-a,a].
The input G is the already constructed actual full-divisor Green synthesis,
with actual lp² coefficient family v. Its global weak derivative D is the
constructed gradient synthesis. The sampled ordinate is the actual divisor
ordinate gamma(q), with Re(gamma)=Im(rho) and |Im(gamma)|<1/2.
These are raw exponential evaluations of G, rather than pairings with a
Green-smoothed test column.

## Concrete source-sampling advance

Integration by parts for each endpoint-corrected Dirichlet Green column,
whose endpoint values are zero, gives
i*z*E(a,z,G_column)=-E(a,z,D_column).
Continuity of raw evaluation as a physical L² pairing transports this
identity through the actual convergent value and gradient series.

The compact raw exponential columns obey
||column(a,z)||²<=2*a*exp(a/2)² throughout the closed ordinate strip.
Thus E(a,z,D) has squared norm bounded by that constant times ||D||².
At actual height h>=1, |gamma|>=h and the derivative identity imply
|E(a,gamma,G)|²<=8*a*exp(a/2)²*||D||²/(1+h)².
The exceptional actual divisor window h<=1 is finite. The certified
inverse-square weight proves raw square sampling converges over every
analytic multiplicity copy. Mixed raw evaluations of two actual syntheses
are absolutely summable by the square-sampling bounds.

The decay is derived from the actual gradient. No supplied sample-decay
premise, shell count, enumeration, RH, or retained spectral-domain premise is used.

## Retained-witness boundary

The original WD-T38 record permits independently named density/Q and
abstract P/C operators. Its existing zero-density reindex audit preserves
physical/null data while changing the named density. Accordingly those
fields do not identify the retained physical mode with the actual synthesis,
or its null equation with the concrete multiplier-plus-pole form.
This chunk adds a genuine raw zero-side convergence witness for the constructed
actual carrier; it does not infer the missing identity from that record.

## Validation

Exact candidate `029075a4d5fa0dca6e4c7c0b63e6846541d92b03` passed [run 37170307358](https://github.com/monocap-tech/weil-lab/actions/runs/37170307358), job `111341779278`: isolated module 9,025 jobs; full `lake build WeilDefect` 9,058 jobs. All eight theorem audits report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed. Certified source and import are promoted separately from the validation workflow and dependency manifest.

## Next cursor and residue

Next: attach the mixed raw actual-divisor pairings to their explicit-formula
transport on this actual supported H¹ synthesis class; recover the retained
coefficient/source dictionary and same-vector identity.
Extension to the entire logarithmic form domain remains a separate obligation.

WD-T38 source/null attachment, central cancellation, background completion
and F-4 remain open. Sharp local unit-band counts remain open. Earlier residue
is preserved. SOURCE stays off the critical path; threshold remains closed.
Retained-mode spectral L²/operator-domain membership is unproved and unassumed.
RH remains open.
