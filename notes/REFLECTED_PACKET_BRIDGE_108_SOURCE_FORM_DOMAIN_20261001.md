# RPB-108 — retained source domain and represented-core residual construction

**Date:** 2026-10-01 (America/Los_Angeles)  
**Recovered research head:** `fe92dffc4794a519a382a2533dc4313580fa443d`  
**Status:** SCOPED POLARIZATION AND REPRESENTED-CORE RESIDUAL CONSTRUCTION BUILD-CERTIFIED / ACTUAL SOURCE ATTACHMENT OPEN / THRESHOLD BOOKKEEPING CLOSED / COERCIVITY NOT STARTED.

## Recovery and custody

The live branch is `monocap-tech/weil-lab@research/reflected-packet-bridge`.
Its RPB-108 threshold-action checkpoint, rather than the stale RPB-100
overview, is the recovered pointer. The latest threshold action certificate
is run `36871575764`, job `110400389955`, source blob
`2e1a1d755da1414651fe088cf42a787a3df213fa`.

The already certified Hermitian cutoff, frozen action, Fourier/physical shell,
source-window globalization and strict-source threshold conversion are retained.
No Gaussian construction or threshold investigation is reopened.

## Source-domain audit

Zhu, arXiv:2608.24827v2, equations (2)-(3), Section 2 and Lemma 6.1, was
re-read at https://arxiv.org/html/2608.24827v2. The diagonal formula is scoped
to its admissible finite-window class. Lemma 6.1 supplies the parity and
real/imaginary decomposition. It is not an identification of every compact
L2 vector with a finite-energy form-domain element.

The code audit is decisive about what is currently available:
`NeutralPhysicalFourierCarrier` supplies an L2 representative and compact
support. Its `NeutralNullExtensionInterface` has abstract bounded operators
and restrictions; it has no identification with the source logarithmic form
or with a multiplier-core function representative. Smoothness of the ordinary
Fourier transform, already certified from compact support, does not itself
assert weighted Fourier decay.

The new `NeutralSourceFormDomainAttachment` keeps a complex L2 submodule, its
specified a.e. support window, logarithmic-energy integrability of its
members, and membership of the actual carrier explicit. It defines the
required custody data; no instance for the actual source has been constructed.
It also does not identify this domain with an operator domain: finite
logarithmic quadratic energy alone is not a theorem of pointwise residual
regularity or of an L2 multiplier output.

The historical WD-T38 statement already includes source form-domain
membership and identification of its algebraic null equation with that same
compact-window form (`docs/NEUTRAL_DEFECT_MORPHOLOGY.md`, Sections 2 and the
composite hypothesis list). The open membership row below means formal
attachment of that retained hypothesis to the concrete L2 lift. It does not
ask for a new theorem deriving source membership from arbitrary compact L2
data, and it does not strengthen WD-T38's mathematical assumptions.

## Scoped complex polarization

`sourceFormDomain_polarization` proves the antilinear-first identity for
complex sesquilinear forms:

~~~math
4B(x,y)=Q(x+y)-Q(x-y)-iQ(x+iy)+iQ(x-iy).
~~~

`sourceFormDomain_eq_of_diagonal` applies it on a retained complex submodule.
Thus source and multiplier forms with identical diagonals on that same domain
have identical mixed terms there. No Hermitian symmetry assumption is needed
for this algebraic identity. No exterior test or rough ambient vector is
admitted through polarization alone.

The actual source diagonal equality and the realization of the corresponding
multiplier/pole form as a sesquilinear form on this domain remain open.

## Constructed full residual

`NeutralWeilCoreFunctionRepresentation` isolates the actual function `r`
representing the fixed-cutoff multiplier core on every compact Schwartz test.
Its local integrability and exponential bounds are explicit obligations.

Given this core and central a.e. cancellation of `r + p_h`, the definition
`neutralWeilResidualFromCore` constructs

~~~math
q=r+p_h,
\qquad C_q=C_r+C_p,
\qquad \kappa_q=\max(\kappa_r,\kappa_p).
~~~

Local integrability follows by addition, growth by the triangle inequality
and the already certified pole bound, and central vanishing is attached to
this specific sum. `neutralWeilResidualFromCore_weakRealization` derives the
full EXT-4 compact identity using genuine integrability of both products.

This reduces the full-residual packaging burden to an explicit core function
representation and central cancellation. It does not prove that the actual
multiplier has such a representative; regular distributions with this growth
remain a restriction on the inputs, not a property of all tempered
distributions. The existing conditional Gaussian theorem can consume the
constructed residual without a new Gaussian weak-identity premise.

## Validation

Validation branch: `validation/rpb108-source-domain`, draft PR #30.
The validation-only workflow checks out the exact PR head, builds
`WeilDefect.Morphology.NeutralWeilSourceFormDomain`, records its source blob,
inspects the four new endpoint axiom closures and rejects unfinished trusted
declarations. Only source, root import, terminology and control artifacts are
eligible for research promotion; the workflow is excluded.

The local Lean installation encountered a runtime application-location error
before source elaboration. It provides no source-build evidence. Validation
therefore uses the established GitHub-hosted runner.

Final direct build certificate:

~~~text
run: 36876381132
job: 110416765195
checked-out head: aa16a1a47ac3e8c457f30cc04f3e10610f6cdccd
module: WeilDefect.Morphology.NeutralWeilSourceFormDomain
source blob: f094847751d2f3fb346eb766b8a1a9e541241b57
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
build: PASS (8954 jobs)
four endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

Runner evidence:
https://github.com/monocap-tech/weil-lab/actions/runs/36876381132/job/110416765195

The first full run, `36875376150`, reached the new module and exposed a
simplifier recursion caused by expanding complex conjugation into a form
that rewrote back to itself, plus an unclosed definitional radius equality.
The corrected run removed the looping rewrites and closed that equality by
`rfl`. No theorem statement or analytic hypothesis changed. The earlier run
`36875134627` was superseded by the source-window custody update.

This certificate covers the exact module and its transitive imports, not a
separate build of the root aggregate. The research root import is added for
normal discoverability. Imported source conditions remain parameters even
though the endpoint axiom closures contain no project axiom or `sorryAx`.

## Continuation

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
Threshold bookkeeping: CLOSED
Actual carrier membership in retained source form domain: OPEN
Source diagonal/multiplier-form identification on that domain: OPEN
Scoped complex polarization: BUILD-CERTIFIED
Full residual construction from represented core: BUILD-CERTIFIED
Actual core representation + regularity/growth + central cancellation: OPEN
Logarithmic Gaussian coercivity: NOT STARTED
~~~

The next pass must attach the retained WD-T38 source hypotheses and establish
the core representation inputs for the actual carrier. It
must not treat the new structures as supplied witnesses or infer a regular
residual from the existence of the frozen compact-test action.
