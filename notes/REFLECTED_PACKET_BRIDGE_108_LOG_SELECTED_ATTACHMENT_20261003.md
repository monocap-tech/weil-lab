# RPB-108 — actual selected source columns on the logarithmic carrier

Continues from `9d8c80a5391f98c10ea7ef37053af630259cc465`.
This pass certifies the compact exponential analysis component of the written
native coefficient dictionary. It does not assert an identification of the
current generic WD-T38 synthesis, compensator, or physical null vector.

## Concrete columns and analysis

The retained convention is `e_z(x)=exp(-i*z*x)`.
The new module `NeutralLogSelectedSourceAttachment.lean` constructs its actual
compact-window L2 column, with support `[-a,a]`, for every complex ordinate.
No spectral-domain premise is used.

`neutralWindowEvaluation a z f` is the compact window integral
`∫ f(x)*exp(i*z*x) dx`. It is not point evaluation of the L2 Fourier transform
of an arbitrary representative.

The first-antilinear L2 pairing is certified exactly:
`inner(e_z,f)=neutralWindowEvaluation a (conj z) f`.
Applying the already concrete physical inclusion adjoint constructs the
actual Riesz source vector in the complete logarithmic Hilbert carrier.
Its pairing gives the same physical window integral. Thus the selected
analysis functional is an actual continuous linear map on that form carrier,
rather than an assumed source identification.

This Riesz source vector uses the logarithmic Hilbert norm. It is not claimed
to equal a native Dirichlet Green column. The written Green/background
completion transport and current WD-T38 source identification remain separate
obligations.

## Pair convention and actual selected block

The positive/negative pair source vectors are the sum/difference of the
actual conjugate-ordinate source vectors, scaled by `1/sqrt(2)`.
Their exact mixed analysis identities are certified.

Conjugating the ordinate fixes the positive source and negates the negative
source. The constructed negative pair energy operator is a rank-one operator;
its exact mixed pairing is the product of the corresponding actual analysis
coordinates. Its diagonal is exactly the squared norm of its actual analysis.
The two source signs cancel, so the operator is unchanged by
the convention swap. No negative input coordinate or compensator is silently
relabelled.

This block represents the selected negative energy. It is not the full
Weil form, a strictly positive background, or an endpoint null theorem.
No multiplicity quotient, infinite actual-zeta sampling bound, closed
background range, or effective background isometry is newly certified here.

## Witness standing

**Proved:** actual compact complex exponential L2 columns; the correct
conjugate-ordinate adjoint integral; concrete logarithmic Riesz source
vectors and continuous analysis; actual pair formulas and conjugation
signs; selected rank-one mixed identity and convention invariance.

**Retained/written:** native multiplicity and Green dictionary, global
actual-zeta sampling, retained strictly positive effective background and
its form completion. Their realization as the generic current WD-T38
`P,C,k,extend` has not been proved.

**Open:** current carrier logarithmic-energy custody and source/quadratic/null
identification; fixed physical enlarged central cancellation. The complete
form carrier and actual multiplier-plus-pole operator from prior checkpoints
remain certified, but constructing these selected source columns alone does
not identify WD-T38's independent source fields.

**Spectral L2:** not derived from WD-T38 and not assumed. These compact
column constructions require only physical L2 and its actual supported
logarithmic reconstruction. They do not upgrade one-log energy to
squared-multiplier L2.

Upon actual enlarged central cancellation, consume the already certified
inner-collar/locally-integrable regular defect, boundary removal, and whole
compact weak realization immediately. Exterior/digamma/boundary work is
not reopened.

Next cursor: concrete effective background completion and current native
source-vector identification, followed by the actual enlarged mixed null law.
Threshold bookkeeping CLOSED; F-4 NOT STARTED; WD-T40/RH unchanged.

## Validation

Certified validation head: `9e845d60e4ab2e3150b4e0d76e3e9f99fecddd67`.
Run: `37128544369`; job: `111218776545`.
Whole-root `lake build WeilDefect`: 9,026 jobs succeeded.
Eleven axiom audits contain only `propext`, `Classical.choice`, and `Quot.sound`.
The unfinished/project-axiom declaration gate passed.
New module blob: `edef77b3479b2908a1bfd46b3b8df035786979b6`.
Root import blob: `b840b5acd8cdc50f7a86f3bc1278ca4708af03ad`.
The validation-only workflow is excluded from research promotion.
