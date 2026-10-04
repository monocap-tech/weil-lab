# RPB-108 — actual full-divisor Green sampling (2026-10-04 UTC)

Parent research head: `da7a2ebdb60748dbbaaee15c598f43f05d6a334f`.

## Definitions before use

The actual divisor coordinate q is an actual open-strip zeta zero rho,
together with one analytic multiplicity copy. Its Bombieri ordinate gamma
satisfies Re(gamma)=Im(rho) and |Im(gamma)|<1/2.
The Green coefficient Q(gamma) is (1/4+gamma²)⁻¹.
The actual Green column is the physical L² class of the compact, endpoint-corrected
Dirichlet Green column on [-a,a], for a>0.
The actual Green coefficient space is lp² indexed by all divisor copies.
Its synthesis is the convergent sum of coefficient times actual Green column.

## Concrete convergence

At absolute height h>=1, the strip denominator bound gives |Q|<=h⁻²,
hence |Q|²<=16/(1+h)^4. The exceptional actual divisor window h<=1 is finite.
The previously certified quartic weight therefore proves unconditional
square summability of the actual Green coefficients.

The concrete pointwise column bound gives
||G(a,q)||²<=18*a*exp(a/2)²*|Q(gamma(q))|².
Thus actual columns are square summable over every multiplicity copy.
Cauchy–Schwarz yields square-summable Green samples for every physical L² input,
and absolutely convergent mixed sample pairings.
The canonical log-carrier samples inherit the same conclusion through the
already constructed physical inclusion and its adjoint.
The existing source-pairing theorem identifies them with the concrete
Green-column integral against neutralLogPhysical f.val.

Every lp² family on the actual divisor synthesizes an absolutely convergent
physical L² vector, with HasSum and same-vector inner-product identities.
No externally stipulated shell count, enumeration, simplicity assumption,
RH, or spectral-domain membership is used.

## Boundary and next cursor

This certifies Green-smoothed sampling and Green value synthesis.
The Green correction and reciprocal denominator are part of the tested
object. The result does not prove raw exponential/window-transform decay,
bounded unregularized sampling on the whole canonical logarithmic form domain,
or gradient/energy synthesis convergence.
Next: derive the stronger inverse-square divisor tail by dyadic bands and
attach actual gradient/energy convergence; retain raw test decay as a separate
source-attachment obligation.

WD-T38 source/null attachment, central cancellation, background completion
and F-4 remain open. SOURCE is off the critical path; threshold remains closed.
Retained-mode spectral L²/operator-domain membership is unproved and unassumed.
RH remains open.

## Validation

Exact candidate `1fd137394b34c7562e63c21a8896809832e2603c` passed [run 37167951376](https://github.com/monocap-tech/weil-lab/actions/runs/37167951376), job `111335525272`: isolated module 9,014 jobs; full `lake build WeilDefect` 9,054 jobs. All eleven theorem audits report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed. The certified source and import are promoted separately from the validation workflow and dependency manifest.
