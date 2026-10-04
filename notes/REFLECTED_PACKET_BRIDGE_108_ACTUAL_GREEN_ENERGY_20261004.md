# RPB-108 — actual inverse-square tails and Green energy (2026-10-04 UTC)

Parent research head: `8bfd58180ac97ede31e6f3fd397d185c144f7d18`.

## Definitions before use

An actual divisor coordinate q contains an actual open-strip zeta zero rho and
one of its analytic multiplicity copies. Its height is h=abs(Im rho).
The dyadic band n is the set with Nat.log 2 (floor(h)+1)=n.
It lies below height 2^(n+1), and 2^n<=1+h.
The quadratic height weight is 1/(1+h)^2.
The actual gradient column is the physical L² class of the compact derivative
of the endpoint-corrected Dirichlet Green column.
The actual gradient synthesis is the sum of lp² actual-divisor coefficients
times those concrete gradient columns.

## Proof

The existing cumulative bound N(T)<=K(T+1)log(T+2) implies dyadic
cardinality <=6K(n+2)2^n. This does not assert sharp unit-band logarithmic density.
Each quadratic weight is <=2^(-2n) on band n. The band total is therefore
bounded by 6K(n+2)2^(-n), a summable polynomial times geometric series.
The nonnegative partition theorem gives full actual-divisor inverse-square
summability, counting every multiplicity copy without an enumeration.

For h>=1, |Q(gamma)|<=1/h²<=4/(1+h)²; the actual low-height exception set is finite.
Thus reciprocal Green coefficients are absolutely summable.
The existing concrete Green energy estimate and actual open-strip
nonresonance identify the energy with gradient norm squared plus one quarter
of value norm squared. These energies are summable over the actual divisor.
Consequently the actual gradient columns are square summable.

Every lp² coefficient family on the actual divisor has convergent gradient
synthesis in physical L², with HasSum and same-vector inner-product identities.
No externally stipulated shell count, simplicity, RH, or retained-mode
spectral-domain membership is used.

## Validation

Exact candidate `754179202aeaf6b5964d94cec2f3bbec439c0c1c` passed [run 37169148911](https://github.com/monocap-tech/weil-lab/actions/runs/37169148911), job `111338364233`: isolated module 9,016 jobs; full `lake build WeilDefect` 9,056 jobs. All fourteen theorem audits report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed. Certified source and imports are promoted separately from the validation workflow and dependency manifest.

## Next cursor and residue

Next: attach the synthesized value/gradient pair by its weak derivative
identity and support to the canonical supported logarithmic form domain.
Then return to the retained WD-T38 source/null witness on that same domain.
Convergence of the two component series alone does not identify their weak
derivative relation, their form-domain membership, or the retained witness.

Raw exponential/window-transform decay, sharp unit-band counts, and
unregularized sampling on the whole logarithmic form domain remain open.
WD-T38 source/null attachment, central cancellation, background completion
and F-4 remain open. Earlier residue is preserved. SOURCE remains off the
critical path; threshold remains closed. Retained-mode spectral L²/operator
domain membership is unproved and unassumed. RH remains open.
