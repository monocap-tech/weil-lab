# Lean Status

## RPB-108 — spectral operator-domain source regularity

Continues from `592eaf780c9c93b93689156b9c3a649971981fc3`.

`NeutralSourceOperatorDomain` gives a concrete spectral route to source
regularity. If the exact right-limit symbol times the carrier's L2 Fourier
transform lies in L2, its inverse Fourier transform is an actual physical
L2 core. Distributional multiplication is identified with the spectral
product using genuine a.e. representative laws. Compatibility of L2 and
tempered Fourier transforms proves exact whole-line core attachment and
pairing. Adding the actual pole and subtracting the existing exterior
candidate constructs a locally integrable representative of the actual
compact source defect, with the correct compact-test pairing. The preceding
boundary-removal theorem then derives whole compact integral-growth weak
realization when actual central source cancellation is supplied.

Actual spectral operator-domain membership and actual central cancellation
remain open witnesses. This criterion is stronger than the source form's
one-logarithm quadratic energy; no form-to-operator-domain upgrade is claimed.
No pointwise exponential growth premise or actual full-source weak identity
is assumed to construct the core. Full-symbol temperate growth is retained.
Whole-source realization and actual source-domain/quadratic/polarization/
normalized estimate witnesses remain open. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_OPERATOR_DOMAIN_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,984 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `ab3cdf9f9740142e2a4313b86f0c19eb1509d935`, run `37074199465`, job `111060294126`, source blob `2d7f07fe842550a4b2e5958e7d3a0d8c2de81250`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
EXACT L2 CORE + REGULAR ACTUAL DEFECT: CONSTRUCTED FROM SPECTRAL L2
WHOLE COMPACT REALIZATION: DERIVED FROM SPECTRAL L2 + CENTRAL CANCELLATION
ACTUAL SPECTRAL L2 MEMBERSHIP + CENTRAL SOURCE CANCELLATION: OPEN
ACTUAL SOURCE FORM-DOMAIN / QUADRATIC / POLARIZATION WITNESSES: OPEN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — regular source defect boundary removal

Continues from `48771be33f1091d4a5e89ed9bdfce08e9c795ebc`.

`NeutralSourceBoundaryRemoval` transfers mathlib's smooth compact-test
fundamental lemma to complex compact Schwartz tests on open sets. If a
locally integrable function represents the actual compact source defect,
certified exterior attachment forces it to vanish almost everywhere outside
[-a,a]. Actual central source cancellation forces it to vanish almost
everywhere in (-a,a). The two endpoints are volume-null, so the representative
vanishes almost everywhere and every compact defect is zero. This gives
whole compact weak realization for the existing integral-growth candidate.

This is a conditional reconstruction theorem. Actual central cancellation
and a locally integrable representation of the actual defect are retained
as explicit, unconstructed hypotheses. In particular, regularity is not
inferred from exterior equality or from a tempered distribution. Under this
regularity hypothesis boundary removal is proved, rather than assumed.
Whole-source realization is not yet constructed. Actual source-domain/
quadratic/polarization/normalized estimate witnesses remain open.
Full-symbol growth is retained. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_BOUNDARY_REMOVAL_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,983 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `d26dbe343dd85772593ee963d9d073af6bda9145`, run `37073137273`, job `111056978955`, source blob `5cb7d738eed3876a2acf3ca03252954be1dbbbda`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
REGULAR DEFECT BOUNDARY REMOVAL: PROVED CONDITIONALLY
WHOLE COMPACT INTEGRAL-GROWTH REALIZATION: DERIVED CONDITIONALLY
ACTUAL REGULAR DEFECT REPRESENTATION + CENTRAL CANCELLATION: OPEN
ACTUAL SOURCE-DOMAIN / QUADRATIC / POLARIZATION WITNESSES: OPEN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — compact source defect localization

Continues from `0a987d79c62dfee094fe5d5b9a515952312be424`.

`NeutralSourceDefectLocalization` defines the actual compact-test defect as
frozen corrected source action minus the concrete exterior candidate pairing.
Genuine candidate integrability proves additivity. Certified exterior
realization proves the defect vanishes on compact tests zero on (-a,a).
Consequently tests agreeing on that open window have equal defects. On a
test supported in the open window, the candidate pairing is zero and the
defect equals the actual corrected source action.

This localizes the remaining obligation; it does not cancel it. Restriction
to an open window also determines boundary jets of smooth tests, so equality
on central restrictions does not exclude boundary-supported distributions.
Next: actual central source cancellation and boundary reconstruction. Whole
compact weak realization and actual source-domain/quadratic/polarization/
normalized estimate witnesses remain open. Full-symbol growth is retained.
Threshold bookkeeping is closed; logarithmic coercivity has not started.

See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_DEFECT_LOCALIZATION_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,982 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `9ef4efd553f38279562a8433f62dc05606d0903c`, run `37071492970`, job `111051735299`, source blob `b2d5fd9bad40f5d01cd82f1b2d1b6b5aab06277b`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL COMPACT SOURCE DEFECT: LOCALIZED TO CENTRAL RESTRICTION
CENTRAL SOURCE CANCELLATION + BOUNDARY RECONSTRUCTION: OPEN
WHOLE COMPACT WEAK REALIZATION: OPEN
ACTUAL SOURCE-DOMAIN / QUADRATIC / POLARIZATION WITNESSES: OPEN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — compact exterior source realization

Continues from `b5e35610cc3c790d4deb7e03e022f97196ad0750`.
`NeutralExteriorSourceAttachment` adds the actual physical pole to the
certified exterior multiplier pairing using genuine compact-test pole
integrability. The full exterior ingredients pair integrably with compact
Schwartz tests. On exterior tests their pairing equals that of the existing
zero-continued residual candidate, because the test vanishes centrally.
The candidate therefore represents the frozen corrected source action on
every compact exterior test. Full-symbol temperate growth is retained.

Next: central cancellation and boundary reconstruction to extend this
restricted identity to arbitrary compact tests. A central or boundary-
supported distribution defect has not been excluded. Whole compact weak
realization and actual source-domain/quadratic/polarization/normalized
estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_EXTERIOR_SOURCE_ATTACHMENT_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,981 build jobs passed. All four endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `cbbee3e50dd3e4d68451b12ad874fe31887cee47`, run `37069776850`, job `111046209012`, source blob `49daf738913f8f6e4587adfe8a509dcfb90895b3`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL COMPACT EXTERIOR SOURCE REALIZATION: CONSTRUCTED
ACTUAL PHYSICAL POLE ADDITION: CONSTRUCTED
NEXT: CENTRAL CANCELLATION + BOUNDARY RECONSTRUCTION → WHOLE SOURCE
      → ACTUAL SOURCE-DOMAIN / QUADRATIC / POLARIZATION WITNESSES
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual exterior multiplier attachment

Continues from `fe9566792500d73678639ff1afbf82ac0b01cdee`.
`NeutralExteriorAttachment` consumes actual centered cancellation and scalar
carrier annihilation to prove the uncentered shifted tail tends to zero on
support-separated Schwartz tests. The certified exterior-defect identity
then identifies actual archimedean multiplier pairings with the gap function.
The exact finite prime split identifies the full right-limit fixed-cutoff
multiplier core with the concrete gap-minus-prime pairing. That pairing is
genuinely integrable. Existing full-symbol temperate growth is retained.

Exterior multiplier attachment is constructed. Next: add the physical pole
on compact tests and reconstruct the whole source, including the central
region and boundaries. Whole compact weak realization and actual source-
domain/quadratic/polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_EXTERIOR_ATTACHMENT_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,980 build jobs passed. All four endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `850bfece8cc0dbc7667a39450e9c0607122b8fbb`, run `37069105759`, job `111044051054`, source blob `10b8eee12415382b27e69bd25e210973e20f8120`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL EXTERIOR MULTIPLIER ATTACHMENT: CONSTRUCTED
FULL-SYMBOL TEMPERATE GROWTH: RETAINED
NEXT: POLE ADDITION + CENTRAL / BOUNDARY RECONSTRUCTION → WHOLE SOURCE
      → ACTUAL SOURCE-DOMAIN / QUADRATIC / POLARIZATION WITNESSES
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual centered digamma residual cancellation

Continues from `66ed85ef2dccd622e84a062489876e825912e248`.
`NeutralDigammaCancellation` maps the actual source-line Euler HasSum to
real parts, then subtracts its zero-frequency instance. The regularizing
terms cancel, leaving the reciprocal-difference series. Its actual HasSum
endpoint is the negative initial centered digamma value. Alignment with
the certified increment formula proves the represented pointwise residual
is zero and the actual centered symbol tends to zero at every frequency.

The represented residual pairing is therefore zero on every Schwartz test.
The certified dominated transfer gives zero convergence of the actual
centered action, retaining its existing full-symbol growth premise.
Next: consume the exterior-defect identity to attach the actual exterior
source. Whole source attachment, central/boundary reconstruction and actual
source-domain/quadratic/polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_CANCELLATION_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,979 build jobs passed. All seven endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `55758c60bff80e626d63d461f150f0c7613d9449`, run `37067232863`, job `111038005004`, source blob `6f1ffdfdd94ab79ce0f08ed1afa6195150e4b81d`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL CENTERED DIGAMMA RESIDUAL CANCELLATION: CONSTRUCTED
ACTUAL CENTERED ACTION ZERO LIMIT: CONSTRUCTED, FULL-SYMBOL GROWTH RETAINED
NEXT: EXTERIOR SOURCE ATTACHMENT → WHOLE SOURCE / ACTUAL SOURCE WITNESSES
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual right-half-plane digamma Euler identity

Continues from `d83104a00e91112b50b538a2b86585b26c735c21`.
`NeutralDigammaEulerIdentity` proves actual digamma holomorphy on the
right half-plane from Gamma differentiability, holomorphy of its derivative
and nonvanishing. The independent Euler candidate is holomorphic there.
Full complex positive-real equality accumulates at 1 inside this connected
domain, so analytic uniqueness identifies actual digamma with the candidate
throughout the right half-plane. Absolute summability gives the actual
complex HasSum with endpoint ψ(z)+γ.

No Gauss representation or full-symbol growth premise enters this identity.
Next: specialize the actual representation to the source line and cancel
the represented centered residual. Existing pairing transfer retains its
full-symbol growth premise. Residual cancellation, tail vanishing, exterior/
whole source attachment, central/boundary reconstruction and actual source-
domain/quadratic/polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_EULER_IDENTITY_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,978 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `42497ee96cc557201b2f87a12dee1f78e6786791`, run `37066190783`, job `111034442714`, source blob `5e236a85ccd8335f116e917e8c77cd94198ef626`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL RIGHT-HALF-PLANE DIGAMMA EULER IDENTITY: CONSTRUCTED
NEXT: SOURCE-LINE SPECIALIZATION → ACTUAL RESIDUAL CANCELLATION
      → EXTERIOR / WHOLE SOURCE ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — independent holomorphic complex Euler candidate

Continues from `b500cb88d2fbc22b25bc9cd22cb8d24d25775cc4`.
`NeutralDigammaEulerHolomorphic` defines the regularized rational terms and
Euler candidate independently of actual digamma. For 0<a≤1 and a≤Re z,
the term norm is at most (‖z-1‖/a)/(n+1)^2. This proves absolute
summability at every point of the right half-plane and supplies uniform
summable bounds on bounded open regions separated from its boundary.
The complex sum theorem gives holomorphy on each region; localization
therefore proves candidate holomorphy throughout the right half-plane.

Actual digamma identification via the full positive-real anchor and a
complex identity theorem remains next. Actual source-line residual
cancellation remains open. Existing pairing transfer retains full-symbol
growth; exterior/whole source attachment, central/boundary reconstruction
and actual source-domain/quadratic/polarization/normalized estimates remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_EULER_HOLOMORPHIC_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,977 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `c2659d1fba74be355f672b65dcaebc8a12f43aa4`, run `37064676684`, job `111029397055`, source blob `e3ae2c1ecd5d0bca73ba5b2eb9fa1d328c0a69e1`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
INDEPENDENT RIGHT-HALF-PLANE EULER CANDIDATE HOLOMORPHY: CONSTRUCTED
NEXT: ACTUAL DIGAMMA HOLOMORPHY + IDENTITY THEOREM
      → ACTUAL RESIDUAL CANCELLATION → EXTERIOR / WHOLE SOURCE ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — full complex actual digamma positive-real anchor

Continues from `bb800b705de708043a33b3d880cb8afc8edaa71a`.
`NeutralDigammaRealComplexAnchor` compares actual complex and real Gamma
derivatives by restriction to the positive real axis and uniqueness.
Actual digamma there equals the real Gamma logarithmic derivative; its
imaginary part is zero. The certified real Euler anchor therefore upgrades
to a full complex HasSum and complex Euler-series identity at every x>0.
This supplies actual complex equality, not just equality of real parts,
for the later identity-theorem step.

No full-symbol growth or Gauss representation premise enters these proofs.
Holomorphic regularized-series construction on the right half-plane, actual
complex identification there and source-line residual cancellation remain
open. The existing pairing transfer retains its full-symbol growth premise.
Exterior/whole source attachment, central/boundary reconstruction and actual
source-domain/quadratic/polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_REAL_COMPLEX_ANCHOR_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,976 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `bf973e0f991b129030d6e72371ab0317ed313ad4`, run `37063437169`, job `111025310561`, source blob `ec5ef4a4c4eaf1c21b96b3f5a979fd4764a0531f`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FULL COMPLEX ACTUAL DIGAMMA POSITIVE-REAL EULER ANCHOR: CONSTRUCTED
NEXT: HOLOMORPHIC COMPLEX EULER SERIES + IDENTITY THEOREM
      → ACTUAL RESIDUAL CANCELLATION → EXTERIOR / WHOLE SOURCE ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — independent actual digamma positive-real Euler anchor

Continues from `0bb110454c42d58f99c62ade4cc0cf2b68611344`.
`NeutralDigammaRealAnchor` proves actual Re ψ(N+x)-log N → 0 for every
positive real x, using the independent log-convex Gamma bounds. The actual
finite recurrence and the harmonic Euler-Mascheroni limit then identify
Re ψ(x) as -γ plus the regularized reciprocal series
∑' n, [1/(n+1)-1/(x+n)]. An independent summable bound proves the actual
series is absolutely summable on the positive real axis.

No full-symbol growth or Gauss representation premise enters this anchor;
no differentiation of a pointwise Gamma approximation limit is used.
Complex analytic series identification and cancellation on the actual
source line remain open. The certified pairing transfer retains its
existing full-symbol growth premise. Exterior/whole source attachment,
central/boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_REAL_ANCHOR_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,975 build jobs passed. All eight audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `5bf141ade97f784c857cd5fd9538d43dae4d013f`,
run `37061473678`, job `111018892567`, source blob
`ab7c5f233a4a2976bc3f6cca96dd529145fedff4`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL POSITIVE-REAL DIGAMMA EULER SERIES ANCHOR: CONSTRUCTED
NEXT: COMPLEX ANALYTIC SERIES IDENTIFICATION → ACTUAL RESIDUAL CANCELLATION
      → TAIL VANISHING / EXTERIOR ATTACHMENT → WHOLE SOURCE + SOURCE DOMAIN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual centered residual pairing limit

Continues from `536987d576594fd7ec9c110e8ecf26f79099dd1d`.
`NeutralDigammaPairingLimit` constructs an explicit integrable majorant
from two Schwartz multipliers and the actual carrier's global L1 norm
mass. It dominates every actual centered frequency pairing uniformly in
N. Dominated convergence passes the represented pointwise residual into
that pairing on every Schwartz test. The existing actual centered action
has exactly this Fourier integral and therefore the same residual limit.
On support-separated tests that frequency residual equals the previously
isolated physical source-attachment defect.

This transfer retains `RightLimitWeilSymbolTemperatePremise a`, the existing
full-symbol growth premise. No zero limit, smooth limiting-symbol multiplier,
or source cancellation is assumed. Actual residual cancellation, exterior/
whole source attachment, central/boundary reconstruction and actual source-
domain/quadratic/polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_PAIRING_LIMIT_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,974 build jobs passed. All seven audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `726048d7d95a6002f74e5adda6ed19737be4eb9a`,
run `37028063173`, job `110907648291`, source blob
`23afba0e8b87f3255ebd9023f9d70161c22c3a7a`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL CENTERED FREQUENCY PAIRING DOMINATION / LIMIT PASSAGE: CONSTRUCTED
ACTUAL FREQUENCY RESIDUAL = EXTERIOR SOURCE-ATTACHMENT DEFECT: CONSTRUCTED
NEXT: ACTUAL RESIDUAL CANCELLATION → TAIL VANISHING / EXTERIOR ATTACHMENT
      → WHOLE SOURCE + SOURCE DOMAIN / POLARIZATION
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual centered limit and uniform frequency envelope

Continues from `1522fd5cbe750d9bb68db255698ecd074da22dcb`.
`NeutralDigammaLimit` proves pointwise convergence of the actual centered
symbol to its initial value plus the absolutely convergent actual increment
series. The recurrence rewrites that limit as an explicit reciprocal series.
The actual displacement has the uniform-in-N bound
64(πξ)^2 S, where S = ∑' n, 1/(n+1)^3 is a fixed finite real mass.
Consequently every centered symbol is bounded by ‖centeredSymbol_0(ξ)‖
plus that same quadratic envelope, for all natural shifts including zero.
No retained full-symbol growth premise is used in these proofs.

Zero convergence is equivalent to cancellation of the explicit actual
residual. That cancellation is still open, as is integrability of the
frequency envelope in the actual Schwartz/carrier pairing and passage to
its distributional limit. Tail vanishing, exterior/whole source attachment,
central/boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_LIMIT_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,973 build jobs passed. All eight audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `808ffbd8a7fb1e3c286ac8373e2583419243d14e`,
run `37026931252`, job `110903822905`, source blob
`68e9451c4e899c659f0d61e17b49384dc260aeb4`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL CENTERED POINTWISE LIMIT / RECIPROCAL-SERIES RESIDUAL: CONSTRUCTED
UNIFORM-IN-SHIFT FREQUENCY ENVELOPE: CONSTRUCTED
NEXT: ACTUAL RESIDUAL CANCELLATION + PAIRING DOMINATION / LIMIT PASSAGE
      → TAIL VANISHING / EXTERIOR ATTACHMENT → WHOLE SOURCE + SOURCE DOMAIN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual centered digamma cubic step decay

Continues from `1ce945e7da95f500184643b674474ea4f940f63f`.
`NeutralDigammaStepDecay` proves the exact real centered reciprocal
deficit and its nonnegative cubic bound. The actual digamma recurrence
identifies each centered-symbol increment with minus that deficit.
Its norm is at most 64(πξ)^2/(N+1)^3, independently of the retained
full-symbol growth premise and without a Gauss representation premise.
The increment norm series is summable at every fixed frequency.

Increment decay does not determine the limiting value. Independent actual
Gamma derivative/series control and lawful frequency domination remain
open, as do tail vanishing, exterior/whole source identity, central/boundary
reconstruction and actual source-domain/quadratic/polarization/normalized
estimate witnesses.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_STEP_DECAY_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,972 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `5ceb3f1b15f99e10c176fec47d47b61469ff19e4`,
run `37019259247`, job `110877798396`, source blob
`ebdc030a45724aa77a9e96a9f4f847744824bded`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL CENTERED DIGAMMA CUBIC STEP BOUND / ABSOLUTE SUMMABILITY: CONSTRUCTED
NEXT: ACTUAL CENTERED LIMIT IDENTIFICATION + FREQUENCY DOMINATION
      → TAIL VANISHING / EXTERIOR ATTACHMENT → WHOLE SOURCE + SOURCE DOMAIN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — actual scalar action separation and centered digamma tail

Continues from `0ed9df1239eabbfbba06eec7509badbe07432d9b`.
`NeutralDigammaCentering` proves the generic existing multiplier law
M(m-k)f(u)=M(m)f(u)-k f(u). Actual compact carrier support makes its
distribution evaluate to zero on tests vanishing on (-a,a), with c<a.
This annihilates the carrier, not the archimedean source action.

The actual shifted symbol minus its own zero-frequency value has lawful
fixed-N temperate growth. Its action agrees exactly with the uncentered
tail on separated tests. It therefore has the same constructed source-
attachment defect limit, and its zero limit is equivalent to exterior
attachment. Scalar action separation is closed; independent centered
nonzero-frequency control and tail vanishing remain open, as do whole
source identity, central/boundary reconstruction and actual source-domain/
quadratic/polarization/normalized estimate witnesses.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_CENTERING_20261002.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,971 build jobs passed. All six audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `4c562ff72edae1571e590ca3357bbc03a0c3940f`,
run `37009813241`, job `110846577087`, source blob
`0e2c679ae105a1fc0e7cead1cb33a6e190ea3183`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL SCALAR ACTION SEPARATION / CENTERED TAIL REDUCTION: CONSTRUCTED
NEXT: INDEPENDENT CENTERED NONZERO-FREQUENCY DIGAMMA CONTROL
      → TAIL VANISHING / EXTERIOR ATTACHMENT → WHOLE SOURCE + SOURCE DOMAIN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — independent actual real-axis digamma bounds

Continues from `b2be21a14300825e897a5242665192480d85887a`.
`NeutralDigammaRealBounds` identifies the derivative of actual positive-
real log Gamma with Re ψ(x). The actual Gamma recurrence gives the exact
unit secant slope log x. Log-convexity then proves Re ψ(x)≤log x for x>0
and log(x-1)≤Re ψ(x) for x>1, independently of retained source comparison
hypotheses and without assuming a Gauss integral representation.

For N≥1 the actual shifted source symbol at zero frequency lies between
log(N-3/4)-log π and log(N+1/4)-log π. This controls its scalar value,
not the centered nonzero-frequency remainder or shifted-tail vanishing.
Exterior/whole source attachment, central/boundary reconstruction and actual
source-domain/quadratic/polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_DIGAMMA_REAL_BOUNDS_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,970 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `1d21396b8414c7524be3fa72cc80b7024136b455`,
run `36972763212`, job `110730043467`, source blob
`82d0918374ac39fb1e1799a5ebf67e27e46ab87f`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL REAL-AXIS DIGAMMA / SHIFTED ZERO-FREQUENCY BRACKET: CONSTRUCTED
NEXT: SCALAR ACTION SEPARATION + CENTERED NONZERO-FREQUENCY DIGAMMA CONTROL
      → TAIL VANISHING / EXTERIOR ATTACHMENT → WHOLE SOURCE + SOURCE DOMAIN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — exterior weak convergence and exact shifted-tail defect

Continues from `c22d1b4a18d8918c617153f1a3296ab73cfd2aee`.
`NeutralGaussExteriorWeak` proves genuine signed gap-function pairings for
every Schwartz test. For tests vanishing on (-a,a), the finite convolution
pairing error is bounded by actual carrier L1 mass times test L1 norm
times the geometric gap error. Thus its pairing converges to minus the
signed gap-function pairing.

The exact operator split now proves that the actual shifted-tail pairing
converges to actual archimedean action minus signed gap-function pairing.
Tail convergence to zero is equivalent to exterior source attachment on
the test. The limit is constructed; its vanishing remains unproved.
No new tail-vanishing premise is added. Whole residual/source identity,
central/boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_GAUSS_EXTERIOR_WEAK_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,969 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `20948ced81df10d90d34de9dea740628ead1c53e`,
run `36969430502`, job `110720096333`, source blob
`079b87d17502e6159dffee61b3fb993ab31fa735`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
EXTERIOR PHYSICAL WEAK LIMIT + EXACT SHIFTED-TAIL DEFECT LIMIT: CONSTRUCTED
NEXT: INDEPENDENT ACTUAL DIGAMMA CONTROL → TAIL VANISHING / EXTERIOR ATTACHMENT
      → WHOLE SOURCE; CENTRAL/BOUNDARY + SOURCE DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — quantitative exterior finite Gauss convergence

Continues from `d1649813180a75d93222e0fffc0f1d9e14df7fe8`.
`NeutralGaussExteriorLimit` proves a geometric kernel error uniform over
displacements beyond a positive gap. The actual finite convolution equals
its compact carrier integral with a genuinely integrable integrand.
For every x outside (-a,a), its difference from the negative signed gap
function is bounded by the actual carrier L1 mass times
exp(-2(a-c))^N / (1-exp(-2(a-c))). This bound is uniform over the exterior;
geometric decay gives actual pointwise convergence there.

The finite physical exterior limit is constructed. The actual shifted
digamma action still needs its own support-separated estimate and weak/
operator limit. Whole residual/source identity, central/boundary reconstruction
and actual source-domain/quadratic/polarization/normalized estimate witnesses
remain open. See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_GAUSS_EXTERIOR_LIMIT_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,968 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `3650789ba52f28a3c08c8f7e49c0881c9bc62e34`,
run `36964811880`, job `110706170139`, source blob
`9ec7fdf7e472a0b602482c1089a22ab7d7005eb8`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FINITE GAUSS CONVOLUTION: UNIFORM EXTERIOR ERROR + POINTWISE LIMIT CONSTRUCTED
NEXT: ACTUAL SHIFTED DIGAMMA SUPPORT-SEPARATED ESTIMATE + WEAK/OPERATOR LIMIT
      → WHOLE ARCHIMEDEAN SOURCE; CENTRAL/BOUNDARY + SOURCE DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — actual shifted digamma action and physical finite split

Continues from `3d0347e1738b2d8abc776a0eb0a5af57e22c11e3`.
`NeutralShiftedDigammaAction` lifts the proved finite recurrence to the
actual multiplier functions at t=2πξ. For every fixed N, the shifted
digamma symbol has temperate growth derived from the retained full-symbol
premise and proved finite Gauss growth; no new tail premise is introduced.
The actual archimedean action equals the shifted digamma action minus
the genuine finite physical convolution pairing on every Schwartz test.
The actual whole core also subtracts the genuine finite prime pairing.

A bound uniform in N and the support-separated weak/operator tail limit
remain open, as do whole archimedean/source attachment, central/boundary
reconstruction and actual source-domain/quadratic/polarization/normalized
estimate witnesses. See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SHIFTED_DIGAMMA_ACTION_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,967 build jobs passed. All four audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `b5539d09ef9c7661d5d512a1f24f4affc3333856`,
run `36962858435`, job `110700132811`, source blob
`3a769eee13cff80100c34b154e153d1bfe2d2d7f`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL SHIFTED DIGAMMA ACTION / FINITE PHYSICAL OPERATOR SPLIT: CONSTRUCTED
NEXT: SUPPORT-SEPARATED SHIFTED TAIL ESTIMATE + WEAK/OPERATOR LIMIT
      → WHOLE ARCHIMEDEAN SOURCE; CENTRAL/BOUNDARY + SOURCE DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — moment-derived finite Gauss multiplier attachment

Continues from `5d341dfb342fd01ff42c30899caac9f5409a3051`.
`NeutralGaussMultiplier` proves actual global integrability of every
polynomial norm moment of each Laplace kernel. A general Fourier argument
derives smoothness and uniformly bounded derivatives from these moments.
The actual finite reciprocal symbol therefore has temperate growth, with
no new symbol premise. The existing tempered Fourier-multiplier CLM on the
actual carrier equals the certified finite physical convolution pairing
on every Schwartz test.

The finite distributional multiplier attachment is constructed. The shifted
digamma tail still needs weak/operator control. Whole archimedean source
attachment, central/boundary reconstruction and actual source-domain/
quadratic/polarization/normalized estimate attachment remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_GAUSS_MULTIPLIER_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,966 build jobs passed. Four endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`c791f2def581ef83e6ea271e27dd0c0f497a2ce5`, run `36960906345`,
job `110694146452`, source blob `fd9a0350a97f5f02ce1d3eadc242cf74a83b11b7`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FINITE GAUSS TEMPERED MULTIPLIER / PHYSICAL CONVOLUTION ATTACHMENT: CONSTRUCTED
NEXT: SHIFTED DIGAMMA TAIL WEAK/OPERATOR CONTROL
      → WHOLE ARCHIMEDEAN SOURCE; CENTRAL/BOUNDARY + SOURCE DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — finite Gauss convolution and weak Fourier transfer

Continues from `542d00ae49757f9926654b5ded58988ebf9f1c89`.
`NeutralFiniteGaussConvolution` identifies the prior geometric kernel with
its finite sum of Laplace exponentials, proves its global L1 integrability,
and computes its exact finite reciprocal Fourier symbol. Its convolution
with the actual rough compact carrier is globally integrable and has the
actual product Fourier transform. On every Schwartz test the physical
pairing equals the inverse-test Fourier pairing by lawful L1 Fubini.

This is a finite weak Fourier identity, not an infinite Gauss/source
representation. Distributional multiplier packaging, shifted-tail operator
control, central/boundary reconstruction and actual source-domain/quadratic/
polarization attachment remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_FINITE_GAUSS_CONVOLUTION_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,965 build jobs passed. Seven endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`9d88d87631c8526cad40e106fe8f25e8feff1eed`, run `36958521515`,
job `110686795036`, source blob `38c6bf719c8cb5aecc4ffcb5673d14af57d0fad9`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FINITE GAUSS KERNEL / ROUGH-CARRIER CONVOLUTION / WEAK FOURIER TRANSFER: CONSTRUCTED
NEXT: DISTRIBUTIONAL MULTIPLIER PACKAGING + SHIFTED TAIL OPERATOR CONTROL
      → WHOLE ARCHIMEDEAN SOURCE; CENTRAL/BOUNDARY + SOURCE DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — normalized Laplace Fourier / Gauss reciprocal transfer

Continues from `279c732efb791a1553beae31c78ef8cd95a4fa0d`.
`NeutralLaplaceFourier` evaluates the genuinely convergent damped Fourier
integral by its two complex-exponential half-line integrals. With mathlib's
frequency t=2πξ, exp(-b|x|) transforms to 2b/(b²+t²). At b=2n+1/2 this is
exactly the real reciprocal coefficient in the finite digamma recurrence.

This attaches each finite rational term to its physical exponential.
Finite-sum/convolution weak transfer and the shifted-tail operator limit
remain open, together with central/boundary reconstruction and actual source
form-domain/polarization attachment. No whole Gauss source identity is inferred.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_LAPLACE_FOURIER_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,964 build jobs passed. Five endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`bdad467cfd28555410444825f9642a629c88f2fa`, run `36944797734`,
job `110644359699`, source blob `63ed6b78651ff2ad5c9e4f78ede851d84b4ba70d`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
NORMALIZED LAPLACE FOURIER / FINITE GAUSS RECIPROCAL TRANSFER: CONSTRUCTED
NEXT: FINITE-SUM / CONVOLUTION WEAK TRANSFER + SHIFTED TAIL OPERATOR LIMIT
      → ARCHIMEDEAN SOURCE ATTACHMENT; CENTRAL/BOUNDARY RECONSTRUCTION
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — finite digamma tail split and Gauss kernel limit

Continues from `e873b75ea172e31a55362bf39ab303c0da68bbfd`.
`NeutralFiniteGauss` derives the actual scalar digamma tail identity from
mathlib's proved recurrence. It constructs the finite geometric exponential
kernel, proves its exact remainder formula, and proves its pointwise limit
away from the singular diagonal. No Gauss identity is retained as a premise.

The pinned mathlib Digamma file explicitly lists Gauss's integral representation
as TODO. The new finite identities do not assert Fourier identification or an
operator limit. Finite resolvent/kernel Fourier transfer and control of the
shifted tail are next; source cancellation, boundary reconstruction and actual
source-domain/polarization attachment remain open.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_FINITE_GAUSS_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,963 build jobs passed. Six endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`fc66ef1e6111d637f5c538f0e4f8c48cda386aa9`, run `36942968489`,
job `110638504163`, source blob `b5ba95325f037c893d1da96866bb3fd064764978`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FINITE DIGAMMA TAIL IDENTITY / GEOMETRIC KERNEL LIMIT: CONSTRUCTED
NEXT: FINITE RESOLVENT FOURIER TRANSFER + SHIFTED TAIL OPERATOR LIMIT
      → ARCHIMEDEAN SOURCE ATTACHMENT; CENTRAL/BOUNDARY RECONSTRUCTION
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — full physical prime action and exact core split

Continues from `353d42a6aa48881be3a73aca7215881fcacba0d8`.
`NeutralWeilCoreSplit` proves the Fourier/physical identity for the full
finite prime part, on every Schwartz test, with genuine pairing convergence.
The actual fixed-cutoff multiplier core equals the archimedean multiplier
action minus that explicit physical prime integral. Archimedean temperate
growth follows from the retained full-symbol premise and proved finite-prime
growth; no additional special-function premise is assumed.

The unidentified physical multiplier component is now precisely archimedean.
Its Gauss/source attachment, central cancellation and boundary/whole-line
reconstruction remain open, together with source-domain/polarization attachment.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_CORE_SPLIT_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,962 build jobs passed. Six endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`3ddfff780beea34612ea31ef30a770b4fdfc5ca3`, run `36938066537`,
job `110622897036`, source blob `19705b44e1d3795be15b7b00646530f6e4ffd601`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FULL PHYSICAL PRIME ACTION / ACTUAL MULTIPLIER CORE SPLIT: CONSTRUCTED
NEXT: SINGULAR ARCHIMEDEAN SOURCE ATTACHMENT + CENTRAL/BOUNDARY RECONSTRUCTION
      → COMPACT WEAK REALIZATION; ACTUAL SOURCE-DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — concrete exterior residual candidate

Continues from `42324e13e69718c51b9b4408f3a8e8d1faaf6ee4`.
`NeutralExteriorResidual` constructs the actual exterior ingredients:
archimedean gap convolution minus the right-limit finite prime translations
plus the named source pole. Their zero continuation inside the enlarged
interval is locally integrable and has finite weighted norm mass for every
rate above one half. At rate one it supplies all analytic fields of
`NeutralIntegralGrowthResidual`.

Central vanishing is imposed by the explicit zero continuation. This does
not establish central cancellation of the source distribution. Exact exterior
Fourier/distribution attachment and the compact source weak identity remain
open, as does actual source-domain/polarization attachment.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_EXTERIOR_RESIDUAL_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,961 build jobs passed. Eight endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`b5b421fa5f0092fbe146229c72d599a329d8242d`, run `36936688172`,
job `110618484466`, source blob `016129d75f5368032392af46db03df752149f217`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
EXTERIOR RESIDUAL CANDIDATE / ALL ANALYTIC FIELDS: CONSTRUCTED
NEXT: EXACT EXTERIOR DISTRIBUTION + CENTRAL SOURCE CANCELLATION
      → COMPACT WEAK REALIZATION; ACTUAL SOURCE-DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual archimedean exterior function and weighted mass

Continues from `d8a521255334bd9b09abb7ce7a3b2499b093d866`.
`NeutralArchimedeanExterior` constructs a continuous bounded convolution of
the actual compact rough carrier with the gap-truncated Gauss kernel. Outside
the strict enlarged interval, truncation is inactive and the value equals the
genuinely convergent untruncated exterior integral. Its norm has finite
exponentially weighted mass for every positive rate.

The small-displacement continuation is auxiliary. No whole-line multiplier
representation or interior identification is inferred. Exterior distribution/
Fourier attachment, central reconstruction and compact source realization
remain open. See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_ARCHIMEDEAN_EXTERIOR_20261001.md).

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,960 build jobs passed. Nine endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`38f82d8b8328a7c0ce4e07e6b1476a9a2d3c9407`, run `36933467318`,
job `110608114891`, source blob `dc3e8c0e1b72769c8cdd6970c8b1131d395c24bc`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL ARCHIMEDEAN EXTERIOR FUNCTION / REGULARITY / WEIGHTED MASS: CONSTRUCTED
NEXT: EXTERIOR DISTRIBUTION ATTACHMENT / CENTRAL RESIDUAL RECONSTRUCTION
      + COMPACT SOURCE WEAK IDENTITY / ACTUAL SOURCE-DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — weighted Hermitian source identity and actual pole convergence

Continues from `e5653d51f559e9ecdcd249692a08902488748a27`.
`NeutralIntegralGrowthWeilIdentity` removes residual growth data from the
pole/Gaussian convergence proof. The actual named pole has half-rate growth;
4 ≤ R(a-c) suffices. Both residual and pole product integrability are derived
before the compact weak identity extends to the actual Hermitian Gaussian.

The compact source identity is retained explicitly in
`IntegralGrowthWeilWeakRealization`; no Gaussian identity is assumed there.
The whole archimedean function, weighted mass, and compact source witness are
not constructed. See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_WEIGHTED_WEAK_IDENTITY_20261001.md).

Certification: exact module passed 8,959 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`965b934fed9a7cca1c7ddad5d4c427c253fa3ed1`, run `36931697060`,
job `110602273298`, source blob `733587e649dadbc4fdbc8d2b97a2774813889753`.
All four audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
WEIGHTED POLE CONVERGENCE / HERMITIAN GAUSSIAN WEAK EXTENSION: CONSTRUCTED
NEXT: ACTUAL ARCHIMEDEAN FUNCTION / WEIGHTED MASS / CENTRAL CANCELLATION
      + COMPACT SOURCE WEAK IDENTITY / ACTUAL SOURCE-DOMAIN ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — integral-growth Gaussian support-gap bridge

Continues from `238f9afcfe9ae41176e95f58b33d0f6670b58301`.
`NeutralIntegralGrowthGaussian` supplies an additive residual interface with
finite exponentially weighted L1 mass and a.e. central cancellation. The
actual Hermitian Gaussian pairing genuinely converges and is bounded by
that fixed mass times the explicit support-gap collar decay and sqrt(R).

The actual physical prime shell constructs an instance with rate zero.
The compact-test weak-identity cutoff extension is independent of the old
pointwise-growth package. Full source realization and pole pairing remain
inputs; no whole residual is supplied by the shell constructor.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_INTEGRAL_GROWTH_20261001.md).

Certification: exact module passed 8,958 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`8250f691fbfcf7fbc58be23c21d4a279820d89df`, run `36930149011`,
job `110597667759`, source blob `a6c45e4a13c704a522164d0a420435bdc7858636`.
All six audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
INTEGRAL-GROWTH GAUSSIAN PAIRING BRIDGE: CONSTRUCTED
NEXT: ACTUAL ARCHIMEDEAN FUNCTION / WEIGHTED MASS / CENTRAL CANCELLATION
      + COMPACT WEAK IDENTITY / POLE PAIRING / ACTUAL SOURCE ATTACHMENT
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — actual finite-prime regularity and L1 gap pairing

Continues from `200e25ba4ce3d261841176b30372579bc5cf0782`.
`NeutralWeilPrimeRegularity` proves global L1 and local integrability of the
actual finite prime translations, their compact support enclosure, and
integrability of their norm against fixed exponential weights. The physical
shell specializes these results and has an L1 support-gap pairing bound.

Growth audit: compact L2 support does not supply the pointwise exponential
fields currently demanded of the full core/residual. The finite-prime pairing
admits an L1 route without boundedness of the carrier. The remaining bridge
must establish additional regularity or admit integral growth explicitly.
See [checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_PRIME_REGULARITY_20261001.md).

Certification: exact module passed 8,957 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`d83af4b35838e08050e82019018c2f81828d6cb4`, run `36923201866`,
job `110574045820`, source blob `7e6d285d64357e775816dfcedbc2486e44b5049f`.
All eight audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
ACTUAL FINITE-PRIME REGULARITY / INTEGRAL GROWTH: CONSTRUCTED
NEXT: ARCHIMEDEAN CORE / CENTRAL CANCELLATION / INTEGRAL-GROWTH BRIDGE
      + ACTUAL SOURCE DOMAIN / QUADRATIC IDENTITY / NORMALIZED ESTIMATES
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

## RPB-108 — explicit real source diagonal and retained shifted comparison

This pass continues from `71dddf5382d0b876b96599406a4a923950ed654e`.
`WeilDefect.Morphology.NeutralWeilSourceDiagonal` evaluates the actual
multiplier-plus-pole form's diagonal as real normalized multiplier energy
plus `2 Re(conj(Mminus) Mplus)`. Signed energy genuinely converges, and
the carrier's pole expression agrees with the real Hermitian pairing against
the previously named physical source pole.

The absolute-symbol estimate needed for mixed convergence is now derived from
the retained shifted lower/upper logarithmic comparisons. The new constructor
consumes those comparisons directly; no independent absolute-bound analytic
input is required. The mixed comparison consumes the explicit source
quadratic formula on the same retained domain.

Certification: exact module passed 8,956 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`3e285dea9d9ca673fd7f568003d10763b5e7f398`, run `36907744139`,
job `110522433582`, source blob `e1949dd4a3996e2e9445c3117aaa3459d3da36b9`.
All ten audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
NEXT: ACTUAL SOURCE DOMAIN / EXPLICIT QUADRATIC IDENTITY / NORMALIZED ESTIMATES
      + ACTUAL CORE REPRESENTATIVE / REGULARITY / GROWTH / CENTRAL CANCELLATION
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

Actual source witnesses remain unconstructed. The real diagonal identity
does not establish a regular core representative or extend the domain to
the exterior Gaussian test. WD-T40 and canonical standing are unchanged.

See [source-diagonal checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_DIAGONAL_20261001.md)
and [registered terminology](TERMINOLOGY_RPB108_SOURCE_DIAGONAL.md).


## RPB-108 — concrete source-domain mixed form

This pass continues from `275f0a21f90fbb4b939b4b621efe09a62e5fc288`.
`WeilDefect.Morphology.NeutralWeilSourceMixedForm` constructs the actual
normalized multiplier-plus-pole sesquilinear form on the retained domain.
Mixed integrals genuinely converge using retained logarithmic energy and
the explicit upper symbol bound. Lp/Fourier a.e. representative laws justify
linearity; compact-window pole moments are genuine linear maps and agree
with the actual carrier's named source moments by support.

Scoped polarization now compares the source form with this concrete form,
conditional on their same-domain diagonal identity. Actual source-domain
and diagonal attachment, the exact normalized symbol-bound attachment, and
the regular core witness with growth and central cancellation remain open.
The existing core-to-residual construction is retained, not replaced with
an inference of regularity from logarithmic quadratic energy.

~~~text
run: 36896248362 / job: 110483849939
checked-out head: d6a1a42985a22c229422d242bb5e0fb9f2dc6298
source blob: f2ce89e5e020f09de54d1864da928bd99a841cbd
Lean: 4.34.0 / mathlib: 5ed2965256430c3649e86755f9576b54eca72435
exact-module build: PASS (8955 jobs)
eight audited endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
NEXT: RETAINED SOURCE DOMAIN / CONCRETE DIAGONAL ATTACHMENT
      + ACTUAL CORE REPRESENTATIVE / REGULARITY / GROWTH / CENTRAL CANCELLATION
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

See [mixed-form checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_MIXED_FORM_20261001.md)
and [mixed-form terminology](TERMINOLOGY_RPB108_MIXED_FORM.md).

## RPB-108 — retained source domain and constructed residual certified

The recovered research base is `fe92dffc4794a519a382a2533dc4313580fa443d`.
Threshold bookkeeping remains closed. The previously stale RPB-100 overview
is repaired at [Reflected-Packet Bridge](REFLECTED_PACKET_BRIDGE.md).

The new module `WeilDefect.Morphology.NeutralWeilSourceFormDomain` certifies
complex polarization on a retained source domain and constructs the full
residual `q = r + p_h`, including its compact weak realization, from an
explicit core representative and central cancellation.

~~~text
run: 36876381132 / job: 110416765195
checked-out head: aa16a1a47ac3e8c457f30cc04f3e10610f6cdccd
source blob: f094847751d2f3fb346eb766b8a1a9e541241b57
exact-module build: PASS (8954 jobs)
four endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

The historical WD-T38 source-domain membership and carrier identification are
retained mathematical hypotheses. Their attachment to the concrete Lean lift
remains open; the new domain structure is not itself a supplied source
witness. The actual source diagonal equality, core representation,
regularity/growth and central cancellation also remain open. Scoped
polarization supplies mixed terms only on its stated domain.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
NEXT: ATTACH RETAINED WD-T38 SOURCE FORM-DOMAIN / DIAGONAL IDENTITY
      + ACTUAL CORE REPRESENTATIVE / REGULARITY / GROWTH / CENTRAL CANCELLATION
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

See [source-domain checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_FORM_DOMAIN_20261001.md)
and the additive [terminology supplement](TERMINOLOGY_RPB108_SOURCE_DOMAIN.md).

## RPB-108 strict-source action threshold delta

The source strict prime convention and the project right-limit convention are
now connected at the physical compact-test action level:

~~~math
E_a^{<=}(h;u)
=
E_a^{<}(h;u)
-
\int u\,\Theta_a^{phys}h.
~~~

The threshold physical term is the exact symmetric translation contributed by
the at-most-one prime power satisfying `log n = 2a`.

`StrictSourceCorrectedWindowPremise` can now state the remaining
finite-window attachment in the literal source convention, and its certified
`toRightLimit` adapter supplies the right-limit premise already used by the
globalization/Hermitian Gaussian stack.

~~~text
run: 36871575764
job: 110400389955
head: 3bf8577200c8ef4d1648c0613106aaf6d7706931
blob: 2e1a1d755da1414651fe088cf42a787a3df213fa
target: lake build WeilDefect.Morphology.NeutralWeilSourceThreshold
result: PASS
axiom audit: only propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

Remaining blocker:

~~~text
FINITE-WINDOW SOURCE FORM-DOMAIN
+ HERMITIAN POLARIZATION / COMPLEXIFICATION
+ ACTUAL RESIDUAL REPRESENTATION
  with local integrability, central vanishing, and exponential growth
~~~

RPB-108 remains active.  Logarithmic coercivity has not started.



## RPB-108 strict-source/right-limit threshold delta

The source strict `<` prime convention and project right-limit `≤`
convention are now explicitly separated and build-certified.

~~~text
run: 36867533110
job: 110386685114
head: db27a3a2536746060d6eb7c3dabe756b7f85b62e
target: lake build WeilDefect.Morphology.NeutralWeilSourceThreshold
blob: ae44725b1147992aa0392e130e46611e3a268bad
result: PASS
axiom audit: only propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

Certified relation:

~~~math
\Psi_a^{\le}(\xi)
=
\Psi_a^{<}(\xi)-\Theta_a(\xi),
~~~

where `Theta_a` is supported on the at-most-one equality-threshold prime
power.  The strict source symbol is also internally certified to have
temperate growth from the right-limit premise plus this finite correction.

Remaining blocker:

~~~text
FINITE-WINDOW SOURCE FORM-DOMAIN
+ HERMITIAN POLARIZATION / COMPLEXIFICATION
+ ACTUAL RESIDUAL REPRESENTATION
  (local integrability + central vanishing + exponential growth)
~~~

RPB-108 remains active.  Logarithmic coercivity has not started.



## RPB-108 source-window globalization delta

The finite prime-shell transport now permits a lawful reduction of the
remaining EXT-4 source boundary.

New certified module:

~~~text
WeilDefect/Morphology/NeutralWeilSourceWindowAttachment.lean
~~~

The base frozen action and a larger-window action satisfy, on every compact
Schwartz test,

~~~math
E_a(h;u)=E_b(h;u)+\int uP_{a,b}h.
~~~

Therefore a shell-corrected finite-window source identity is sufficient to
derive the exact all-compact-test `RightLimitWeilWeakRealizationPremise`.
The previously certified Hermitian Gaussian theorem can consume that derived
witness directly.

Certification:

~~~text
run: 36824968898
job: 110248500881
head: af0060d6acef81062a01eb06087dd3566bc800bb
target: lake build WeilDefect.Morphology.NeutralWeilSourceWindowAttachment
blob: 5be297c758f1f169be2f4eadf00996beeae3a6e4
result: PASS
axiom audit: only propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

The free-globalization draft was rejected: old-window compression cannot be
used on an arbitrary test whose support only fits a larger source window.
The finite shell is load-bearing there.

Remaining blocker:

~~~text
SOURCE QUADRATIC FORM-DOMAIN
+ POLARIZATION/COMPLEXIFICATION ON EACH FINITE WINDOW
+ STRICT-< SOURCE PRIME CUTOFF TO RIGHT-LIMIT <= THRESHOLD CORRECTION
+ ACTUAL RESIDUAL REPRESENTATION / LOCAL INTEGRABILITY / CENTRAL VANISHING /
  EXPONENTIAL-GROWTH ATTACHMENT
~~~

RPB-108 remains active.  Logarithmic coercivity has not started.

 Ledger

This file records formal verification separately from mathematical standing and P4 audit status.

## Status labels

- **LEAN-NOT-ATTEMPTED** — not yet entered into the formalization queue.
- **LEAN-IN-PROGRESS** — a Lean declaration or infrastructure exists but has not yet passed the pinned CI build.
- **LEAN-CERTIFIED** — kernel-checked under the pinned toolchain with no project `sorry`, `admit`, or `axiom`.
- **LEAN-CERTIFIED-FROM-IMPORTED-PREMISE** — Lean verifies the downstream deduction from an explicit external premise, but not the external theorem itself.
- **LEAN-BLOCKED** — direct formalization is exhausted for the current pass and an exact missing formal dependency is recorded.
- **SCOPE-ONLY** — jurisdiction rule rather than a theorem.

## Current control state

- **Formalization track:** LEAN-H1 exhausted.
- **Active phase:** none.
- **Active Lean cursor:** none.
- **Next project cursor:** RPB-108 / WD-T40 F-4 polarized EXT-4 operator realization + Hermitian Gaussian cutoff bridge.
- **Public packaging:** complete and post-WD-T40 refolded; see [Public Package Audit](PUBLIC_PACKAGE_AUDIT.md).

This section is canonical for the live queue. The certificate sections below are an append-only evidence history and may describe what was still pending at an earlier checkpoint.

## WD-T40 blocker record

### RPB-106 corrected certificate

The former RPB-104 and RPB-105 green runs remain wrong-target historical
records.  Their source obligations were subsequently repaired and certified
through the actual Gaussian assembly dependency closure.

~~~text
run:  36803460601
job:  110182696916
head: d9c0b171263862ed088620597f3d8d5ff7512278
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
target: lake build WeilDefect.Morphology.NeutralGaussianAssembly
result: PASS
~~~

Certified source blobs:

~~~text
NeutralGaussianCutoff.lean:
1cbe03541d4521026205de8475f78a733e62abe0

NeutralGaussianCutoffPairing.lean:
1accc07c182e5348212734f0b00cdf676a02b164

NeutralWeilPoleGrowth.lean:
2c1b440bb7b8c32dcde58ac5addc0fbbeab607a2

NeutralGaussianAssembly.lean:
01ce40bffd08cf73eb7d70e70f544ff479bfb4ce
~~~

The endpoint axiom audit reports only `propext`, `Classical.choice`, and
`Quot.sound`, with no `sorryAx`, for the cutoff topology theorem, both
pairing-limit theorems, the explicit exponential-pole bound, the concrete
source-pole growth instance, and the source-pole Gaussian-admissibility
constructor.

The concrete pole is the two-exponential species with growth rate `1/2`.
The final constructor is intentionally conditional on

~~~lean
RightLimitWeilWeakRealizationPremise
  c carrier residual hSymbol (neutralWeilSourcePole carrier)
~~~

so no arbitrary locally-integrable EXT-4 pole is silently identified with the
source pole.  This imported witness attachment, together with the
bilinear/Hermitian test-duality audit, is the live pre-coercivity seam.

RPB-67 completed the formalization preflight.

WD-T40 is mathematically P4-AUDIT-PASSED but is not directly certifiable from
the current project abstraction because the WD-T38 Lean interface is generic
in its physical Hilbert space and does not yet expose the concrete real-line
Fourier/distribution data consumed by the Gaussian support-gap proof.

Exact blocking stack:

~~~text
F-1  physical real-line L2 / tempered-distribution carrier lift — BUILD-CERTIFIED / audited blob 03fe8ab1b6a3190e40a91b7a467c975e0d87841d / run 36649140221
F-2  actual compact-window Weil multiplier realization — COMPLETE / NORMALIZED BUILD-CERTIFIED / t=2*pi*xi source-to-mathlib map / multiplier blob 4c24084c8a058cbb6685d54bc8226b746cabc413 / integrated run 36774149872 / explicit EXT-4 + EXT-5D premise custody unchanged
F-3  support-gap Gaussian pairing theorem — COMPLETE / BUILD-CERTIFIED AGAINST NORMALIZED F-2 / final pairing blob 54732470ab2cf2a3a99be646372fdc186225363a / integrated run 36774149872 / no new imported premise
F-4  Gaussian coercivity -> exponential Fourier weight — PRE-COERCIVITY DOMAIN BRIDGE REPAIRED THROUGH CONDITIONAL ASSEMBLY / admissibility interface BUILD-CERTIFIED / cutoff-limit constructor + pole exponential-growth integrability BUILD-CERTIFIED by RPB-101 / carrier Fourier moments + C-infinity + temperate growth BUILD-CERTIFIED by RPB-102 / exact moving filtered mode as SchwartzMap BUILD-CERTIFIED by RPB-103 / corrected compact Schwartz-cutoff + full Schwartz-topology convergence and corrected residual/pole pairing limits RE-CERTIFIED transitively by RPB-106 run 36803460601 / concrete two-exponential source-pole growth BUILD-CERTIFIED / Gaussian admissibility assembly BUILD-CERTIFIED-FROM-IMPORTED-PREMISE when EXT-4 names exactly neutralWeilSourcePole carrier / two-exponential pole quadratic algebra + Hermitian Gaussian dual test BUILD-CERTIFIED by RPB-107 / full polarized EXT-4 complex operator realization + Hermitian cutoff-limit bridge still open / coercivity not started
F-5  exponential Fourier weight -> strip holomorphy -> compact-support zero
F-6  final WD-T40 assembly from explicit EXT-4 / EXT-5 premises
~~~

Mathlib v4.34 already provides L2 Plancherel, L2/tempered-distribution Fourier
compatibility, Gaussian Fourier formulas, Fourier inversion, and complex
analytic continuation tools. The blocker is therefore project-local
integration, not absence of base Fourier mathematics.

A faithful completed formalization would be expected to carry status

~~~text
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE
~~~

unless EXT-4 and EXT-5 are themselves reconstructed in Lean.



## Declaration map

| Stable ID | Lean declaration | Status |
| --- | --- | --- |
| WD-T40 | F-1 carrier + normalized F-2 multiplier + F-3 support-gap pairing + repaired cutoff/pairing closure + concrete source-pole growth + conditional Gaussian-admissibility assembly are kernel-checked; RPB-107 additionally certifies the exact two-exponential pole quadratic factor and the conjugated Hermitian Gaussian dual test. The remaining blocker is the source-faithful polarization/complexification of EXT-4 into a compact-test operator identity and its cutoff extension to that dual test before coercivity | LEAN-BLOCKED |
| WD-T39 | WeilDefect.FullNegativeSpace + WeilDefect.fullNegativeCoeff + WeilDefect.fullCoeff + WeilDefect.fullJValue + WeilDefect.wd_t39_p3_b1_anchored_mass + WeilDefect.wd_t39_p3_b2_full_coordinate_escape_weak_zero + WeilDefect.wd_t39_p3_b3_fixed_packet_custody + WeilDefect.normEscapeSubsequence + WeilDefect.wd_t39_p3_b4_norm_escape_of_unbounded + WeilDefect.BoundedBackgroundRegime + WeilDefect.wd_t39_p3_b4_bounded_background_dichotomy + WeilDefect.BackgroundCompactnessRegime + WeilDefect.wd_t39_p3_b4_background_compactness_trichotomy + WeilDefect.wd_t39_p3_b5_fixed_selected_ray_stability + WeilDefect.wd_t39_p3_b6_fixed_full_divisor_negative_weak_limit + WeilDefect.wd_t39_p3_b7_finite_shadow_separation + WeilDefect.NoncompactDefectMorphology + WeilDefect.wd_t39_noncompact_background_morphology | LEAN-CERTIFIED |
| WD-T38 | WeilDefect.wd_t38_p3_u1_fixed_packet_critical_dichotomy + WeilDefect.wd_t38_attained_neutral_selected_coordinate_nonzero + WeilDefect.rightLimitPrimePowers + WeilDefect.wd_t38_p3_u3_right_limit_prime_decomposition + WeilDefect.wd_t38_p3_u3_right_limit_prime_support_finite + WeilDefect.wd_t38_p3_u4_logarithmic_order_neutral_carrier + WeilDefect.wd_t38_p3_u5_no_free_positive_sobolev_control + WeilDefect.wd_t38_p3_u5_finite_prime_translations_no_smoothing + WeilDefect.wd_t38_p3_u6_global_cancellation_not_termwise + WeilDefect.neutralNegativeSynthesis + WeilDefect.neutralWeilOperator + WeilDefect.wd_t38_p3_u2_negative_adjoint_identity + WeilDefect.wd_t38_p3_u2_physical_neutral_null_mode + WeilDefect.NeutralNullExtensionInterface + WeilDefect.NeutralNullExtensionInterface.persistenceGoal + WeilDefect.wd_t38_p3_u7_neutral_null_extension_reduction + WeilDefect.NeutralArithmeticMorphology + WeilDefect.wd_t38_neutral_arithmetic_morphology + WeilDefect.NeutralDefectMorphology + WeilDefect.wd_t38_attained_unit_gain_neutral_morphology | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T37 | WeilDefect.wd_t37_selected_source_zero_moment_of_wd_t26 + WeilDefect.wd_t37_selected_source_nonzero_of_wd_t26 + WeilDefect.wd_t37_p3_n1_endpoint_ray + WeilDefect.wd_t37_p3_n2_normalized_representative_blowup + WeilDefect.wd_t37_p3_n3_normalized_full_negativity + WeilDefect.wd_t37_p3_n4_zero_moment_source_far_decay + WeilDefect.wd_t37_p3_n5_far_localization + WeilDefect.wd_t37_p3_n6_weighted_next_jet_morphology + WeilDefect.wd_t37_p3_n7_no_adaptive_scalar_bypass + WeilDefect.NegativeArithmeticMorphology + WeilDefect.NegativeDefectMorphology + WeilDefect.wd_t37_fixed_packet_persistent_negative_morphology | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T36 | WeilDefect.positiveSobolevFrequencyWeight + WeilDefect.logarithmicFourierWeight_isBigO_log + WeilDefect.logarithmicFourierWeight_isLittleO_positiveSobolev + WeilDefect.positiveSobolevFrequencyWeight_not_isBigO_logarithmic + WeilDefect.wd_t36_no_uniform_positive_sobolev_coercivity_of_witness + WeilDefect.wd_t36_no_positive_sobolev_bootstrap + WeilDefect.finitePrimeTrigCorrection + WeilDefect.finitePrimeTrigBound + WeilDefect.abs_finitePrimeTrigCorrection_le + WeilDefect.finitePrimeTrigCorrection_isBigO_logarithmic + WeilDefect.logarithmicPlusFinitePrimeCorrection_isBigO + WeilDefect.wd_t36_finite_prime_translations_add_no_smoothing | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T35 | WeilDefect.logarithmicFourierWeight + WeilDefect.one_le_logarithmicFourierWeight + WeilDefect.logarithmicFourierEnergy + WeilDefect.spectralMass + WeilDefect.shiftedCompactWeilForm + WeilDefect.wd_t35_shifted_form_logarithmic_order + WeilDefect.wd_t35_compact_weil_logarithmic_form_order | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T34 | WeilDefect.activePrimePowers + WeilDefect.wd_t34_active_prime_powers_finite + WeilDefect.activePrimePowerFinset + WeilDefect.activePrimeTranslationShifts + WeilDefect.wd_t34_active_prime_translation_shifts_finite + WeilDefect.translateBy + WeilDefect.symmetricPrimeTranslation + WeilDefect.compactPrimeTranslationSum + WeilDefect.wd_t34_finite_prime_power_translations + WeilDefect.primePowerThreshold + WeilDefect.primePowerThreshold_subsingleton | LEAN-CERTIFIED |
| WD-T32 | WeilDefect.completedResponseLift + WeilDefect.iteratedDeriv_centered_power + WeilDefect.iteratedDeriv_centered_power_mul + WeilDefect.wd_t32_complementary_next_jet_identity + WeilDefect.nearComplementaryResponse + WeilDefect.weightedNearNextJetField + WeilDefect.wd_t32_weighted_near_next_jet_representation | LEAN-CERTIFIED |
| WD-T31 | WeilDefect.ZetaLogShellCountData + WeilDefect.FarShellResponseData + WeilDefect.logarithmicTail_tsum_le + WeilDefect.farShellResponse_norm_le_logarithmic_kernel + WeilDefect.wd_t31_shell_aggregation + WeilDefect.rationalResponse_zero_moment_norm_le_inverse_square + WeilDefect.farShellResponseData_of_zero_moment + WeilDefect.wd_t31_zero_moment_zero_count_far_tail | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T29 | WeilDefect.wd_t29_finite_head_approximation + WeilDefect.wd_t29_quantitative_finite_head_approximation | LEAN-CERTIFIED |
| WD-T28 | WeilDefect.ZetaZeroShellCountData + WeilDefect.NativeProblemOneResolventData + WeilDefect.NativeHilbertSchmidtCriterion + WeilDefect.NativeTraceClassCovarianceCriterion + WeilDefect.wd_t28_native_problem_one_hilbert_schmidt_actual + WeilDefect.problemOneGreenPairing_eq_dirichletEnergy + WeilDefect.problemOneColumnEnergySq_eq_dirichletEnergy + WeilDefect.wd_t28_actual_dirichlet_energy_summable | LEAN-CERTIFIED |
| WD-T27 | WeilDefect.rationalResponse + WeilDefect.residueFirstMoment + WeilDefect.rationalResponse_laurent_two + WeilDefect.rationalResponse_zero_moment_remainder_bound + WeilDefect.rationalResponse_zero_moment_remainder_isBigO + WeilDefect.rationalResponse_zero_moment_isBigO + WeilDefect.wd_t27_universal_inverse_square_far_decay + WeilDefect.wd_t27_universal_inverse_square_isBigO | LEAN-CERTIFIED |
| WD-T26 | WeilDefect.rawResiduesOfNegativePairs + WeilDefect.wd_t26_zero_moment + WeilDefect.wd_t26_coefficient_mem_rawResidues + WeilDefect.wd_t26_nonzero_raw_residue_of_nonzero_coefficient + WeilDefect.wd_t26_selected_zero_moment_residue | LEAN-CERTIFIED |
| WD-T25 | WeilDefect.problemOneDenominator + WeilDefect.problemOneL + WeilDefect.problemOneMode + WeilDefect.problemOneL_problemOneMode + WeilDefect.wd_t25_finite_problem_one_relation_trivial + WeilDefect.wd_t25_no_exact_finite_positive_compensation | LEAN-CERTIFIED |
| WD-T24 | WeilDefect.realExpMode + WeilDefect.realExpMode_ne_zero + WeilDefect.hasDerivAt_realExpMode + WeilDefect.iteratedDeriv_realExpMode + WeilDefect.iteratedDeriv_finite_exp_sum + WeilDefect.wd_t24_finite_distinct_frequency_exponential_independence | LEAN-CERTIFIED |
| WD-T23 | WeilDefect.BombieriMultiplicityNullData + WeilDefect.wd_t23_same_frequency_synthesis_factor + WeilDefect.wd_t23_same_frequency_zero_sum_null + WeilDefect.wd_t23_total_multiplicity_nullity + WeilDefect.wd_t23_single_ordinate_nullity + WeilDefect.wd_t23_single_ordinate_has_null_iff_repeated + WeilDefect.wd_t23_distinct_frequency_reduction | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T22 | WeilDefect.BombieriFiniteInertiaData + WeilDefect.wd_t22_finite_weil_inertia_saturation + WeilDefect.SimpleQuartetPacketNegative + WeilDefect.wd_t22_simple_quartet_packet_pair_count + WeilDefect.wd_t22_simple_quartet_packet_inertia + WeilDefect.wd_t22_two_simple_quartet_negative_index | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T21 | WeilDefect.quartetPairPos + WeilDefect.quartetPairNeg + WeilDefect.wd_t21_quartet_pair_pos_conjugate + WeilDefect.wd_t21_quartet_pair_neg_conjugate + WeilDefect.wd_t21_quartet_pairs_nonreal + WeilDefect.wd_t21_quartet_pairs_distinct + WeilDefect.wd_t21_simple_quartet_negative_count + WeilDefect.wd_t21_simple_quartet_pair_geometry | LEAN-CERTIFIED |
| WD-T20 | WeilDefect.wd_t20_pair_pos_eigen + WeilDefect.wd_t20_pair_neg_eigen + WeilDefect.pairEigenEquiv + WeilDefect.wd_t20_pair_diagonalization | LEAN-CERTIFIED |
| WD-T19 | WeilDefect.WDT19.analysisSpace + WeilDefect.WDT19.weak_limit_mem_physical_rightLimit + WeilDefect.WDT19.wd_t19_endpoint_representative_blowup + WeilDefect.WDT19.BoundaryAmplifies + WeilDefect.WDT19.wd_t19_boundary_amplification + WeilDefect.WDT19.wd_t19_vanishing_amplitude_normalized_blowup | LEAN-CERTIFIED |
| WD-T18 | WeilDefect.WDT18.endpointInside + WeilDefect.WDT18.endpointQuotientMap + WeilDefect.WDT18.wd_t18_endpoint_quotient_map_injective + WeilDefect.WDT18.wd_t18_endpoint_jump_negative_rank_le_quotient + WeilDefect.WDT18.wd_t18_one_dimensional_jump_rank_cap | LEAN-CERTIFIED |
| WD-T17 | WeilDefect.WDT17.weaklyTendsto_strong_of_norm_sq_tendsto + WeilDefect.WDT17.wd_t17_critical_positive_mass_le_half + WeilDefect.WDT17.wd_t17_fixed_sector_critical_dichotomy + WeilDefect.WDT17.wd_t17_neutral_branch + WeilDefect.WDT17.wd_t17_loss_branch | LEAN-CERTIFIED |
| WD-T16 | WeilDefect.WDT16.exists_weaklyTendsto_subseq_of_norm_le + WeilDefect.WDT16.wd_t16_fixed_negative_sector_compactness + WeilDefect.WDT16.wd_t16_nonpositive_limit_persists + WeilDefect.WDT16.wd_t16_uniform_negative_margin_persists + WeilDefect.WDT16.wd_t16_uniform_negative_margin_forces_endpoint_jump + WeilDefect.WDT16.wd_t16_fixed_finite_negative_sector_persistence | LEAN-CERTIFIED |
| WD-T15 | WeilDefect.WDT15.wd_t15_gap_antitone + WeilDefect.WDT15.wd_t15_right_limit_gap_duality + WeilDefect.WDT15.wd_t15_sequence_right_limit_eq + WeilDefect.WDT15.wd_t15_sequence_gap_eq_right_limit_orthogonal + WeilDefect.WDT15.wd_t15_monotone_projection_limit + WeilDefect.WDT15.wd_t15_right_limit_projection_and_gap_duality | LEAN-CERTIFIED |
| WD-T14 | WeilDefect.WDT14.wd_t14_positive_shadow_margin + WeilDefect.WDT14.wd_t14_positive_shadow_preserves_negative_margin + WeilDefect.WDT14.wd_t14_graph_shadow_admissible_iff + WeilDefect.WDT14.wd_t14_graph_admissibility_failure_example + WeilDefect.WDT14.wd_t14_finite_positive_shadows_preserve_signature_not_admissibility | LEAN-CERTIFIED |
| WD-T13 | WeilDefect.WDT13.wd_t13_complement_isUnit + WeilDefect.WDT13.wd_t13_complement_inverse_nonnegative + WeilDefect.WDT13.wd_t13_schur_correction_positive + WeilDefect.WDT13.wd_t13_schur_le_compression + WeilDefect.WDT13.wd_t13_schur_lower_bound + WeilDefect.WDT13.wd_t13_schur_isUnit + WeilDefect.WDT13.wd_t13_block_solution_exists + WeilDefect.WDT13.wd_t13_block_solution_first_component + WeilDefect.WDT13.wd_t13_direct_compression_versus_shorted_covariance | LEAN-CERTIFIED |
| WD-T12 | WeilDefect.WDT12.sequentialResidualBudget + WeilDefect.WDT12.wd_t12_sequential_budget_covariance + WeilDefect.WDT12.wd_t12_second_background_elimination + WeilDefect.WDT12.wd_t12_sequential_background_consumption | LEAN-CERTIFIED |
| WD-T11 | WeilDefect.WDT11.wd_t11_norm_one_attains_neutral + WeilDefect.WDT11.wd_t11_graphQ_diagonal + WeilDefect.WDT11.wd_t11_negative_rank_le_count + WeilDefect.WDT11.wd_t11_negative_space_strict + WeilDefect.WDT11.wd_t11_negative_space_finrank + WeilDefect.WDT11.wd_t11_negative_index_exact + WeilDefect.WDT11.wd_t11_neutral_space_finrank + WeilDefect.WDT11.wd_t11_neutral_space_graphQ_zero + WeilDefect.WDT11.wd_t11_finite_sector_singular_value_inertia | LEAN-CERTIFIED |
| WD-T10 | WeilDefect.WDT10.wd_t10_residual_budget_positive + WeilDefect.WDT10.wd_t10_residual_sqrt_sq + WeilDefect.WDT10.wd_t10_effective_covariance + WeilDefect.WDT10.wd_t10_background_covariance_elimination + WeilDefect.WDT10.wd_t10_full_defect_reduction + WeilDefect.WDT10.wd_t10_full_nonnegative_iff_effective_physical + WeilDefect.WDT10.wd_t10_full_nonnegative_iff_residual_screening + WeilDefect.WDT10.wd_t10_background_elimination_and_residual_budget | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T09 | WeilDefect.WDT09.wd_t09_full_quadratic_factorization + WeilDefect.WDT09.wd_t09_shared_defect_factorization + WeilDefect.WDT09.wd_t09_full_nonnegative_iff_joint_budget + WeilDefect.WDT09.wd_t09_separate_contractions_not_joint + WeilDefect.WDT09.wd_t09_shared_screening_budget | LEAN-CERTIFIED |
| WD-T08 | WeilDefect.WDT08.selected_adjoint_comp_injective + WeilDefect.WDT08.wd_t08_selected_negative_rank_le_finrank + WeilDefect.WDT08.wd_t08_background_null_finrank_lower + WeilDefect.WDT08.wd_t08_selected_negative_on_background_null + WeilDefect.WDT08.wd_t08_full_negative_rank_background_reduction + WeilDefect.WDT08.wd_t08_finite_selected_sector_index_cap | LEAN-CERTIFIED |
| WD-T07 | WeilDefect.wd_t07_selected_full_identity + WeilDefect.wd_t07_selected_negative_implies_full + WeilDefect.WDT07.wd_t07_full_le_selected + WeilDefect.WDT07.wd_t07_negative_rank_custody + WeilDefect.WDT07.wd_t07_full_negative_without_selected_negative + WeilDefect.WDT07.wd_t07_selected_background_monotonicity_and_custody | LEAN-CERTIFIED |
| WD-T06 | WeilDefect.WDT06.wd_t06_truncated_inner_identity + WeilDefect.WDT06.wd_t06_quadratic_mono + WeilDefect.WDT06.wd_t06_defect_mono + WeilDefect.WDT06.wd_t06_defect_le_full + WeilDefect.WDT06.wd_t06_defect_strong_tendsto + WeilDefect.WDT06.wd_t06_quadratic_tendsto + WeilDefect.WDT06.wd_t06_negative_rank_antitone + WeilDefect.WDT06.wd_t06_monotone_positive_screening | LEAN-CERTIFIED |
| WD-T05 | WeilDefect.wd_t05_rank_one_covariance + WeilDefect.WDT05.wd_t05_defect_rank_one + WeilDefect.WDT05.wd_t05_signed_factor_iff_vector + WeilDefect.WDT05.wd_t05_covariance_iff_unit_vector + WeilDefect.WDT05.wd_t05_physical_nonnegative_iff_unit_vector + WeilDefect.WDT05.wd_t05_analysis_nonnegative_iff_unit_vector + WeilDefect.WDT05.wd_t05_rank_one_specialization | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T04 | WeilDefect.WDT04.wd_t04_range_defect_no_exact_screening + WeilDefect.WDT04.wd_t04_range_defect_negative + WeilDefect.WDT04.wd_t04_over_budget_negative + WeilDefect.WDT04.wd_t04_strict_screened_lower_bound + WeilDefect.WDT04.wd_t04_attained_critical_neutral + WeilDefect.WDT04.wd_t04_nonattained_critical_positive + WeilDefect.WDT04.wd_t04_critical_approximate_neutral + WeilDefect.WDT04.wd_t04_complete_reduced_taxonomy | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T03 | WeilDefect.WDT03.wd_t03_kernel_decomposition + WeilDefect.WDT03.wd_t03_analysis_graph_iff + WeilDefect.WDT03.wd_t03_graph_signature + WeilDefect.WDT03.wd_t03_defect_factorization | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T02 | WeilDefect.WDT02.wd_t02_contractive_screening_equivalence + WeilDefect.WDT02.wd_t02_unique_reduced_solution | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE |
| WD-T01 | WeilDefect.WDT01.wd_t01_defect_inner_identity + WeilDefect.WDT01.wd_t01_nonnegative_iff + WeilDefect.WDT01.wd_t01_negative_rank_iff | LEAN-CERTIFIED |
| WD-T33 | WeilDefect.wd_t33_adaptive_cocancellation | LEAN-CERTIFIED |
| WD-T30 | WeilDefect.wd_t30_two_mode_kernel_combination + WeilDefect.wd_t30_zero_functional_preserves_every_mode | LEAN-CERTIFIED |
| WD-X01 | WeilDefect.wd_x01_partial_sum + WeilDefect.wd_x01_finite_defect_negative + WeilDefect.wd_x01_finite_defect_formula + WeilDefect.wd_x01_defect_tendsto_zero | LEAN-CERTIFIED |
| WD-X02 | WeilDefect.wdX02Weight + WeilDefect.wdX02Coord + WeilDefect.wdX02Operator + WeilDefect.wd_x02_operator_norm_eq_one + WeilDefect.wd_x02_strict_norm_loss + WeilDefect.wd_x02_no_nonzero_norm_attainer + WeilDefect.wd_x02_critical_nonattainment | LEAN-CERTIFIED |
| WD-X03 | `WeilDefect.wd_x03_individual_not_compositional` | LEAN-CERTIFIED |
| WD-X04 | `WeilDefect.wd_x04_shorted_covariance_identity` | LEAN-CERTIFIED |
| WD-X05 | WeilDefect.wdX05Delta + WeilDefect.wdX05PosAmp + WeilDefect.wdX05NegAmp + WeilDefect.wdX05Pos + WeilDefect.wdX05Neg + WeilDefect.wdX05Vector + WeilDefect.wd_x05_vector_norm_eq_one + WeilDefect.wd_x05_jvalue_formula + WeilDefect.wd_x05_jvalue_negative + WeilDefect.wd_x05_jvalue_tendsto_zero + WeilDefect.wdX05Tail + WeilDefect.wd_x05_tail_antitone + WeilDefect.wd_x05_vector_mem_tail + WeilDefect.wd_x05_tail_intersection_trivial + WeilDefect.wd_x05_moving_sectors_lose_persistent_ray | LEAN-CERTIFIED |
| WD-X06 | WeilDefect.wdX06Amp + WeilDefect.wdX06Pos + WeilDefect.wdX06Neg + WeilDefect.wdX06Vector + WeilDefect.wdX06Limit + WeilDefect.wd_x06_vector_norm_eq_one + WeilDefect.wd_x06_vector_critical + WeilDefect.wd_x06_lp_coordinate_tendsto_zero + WeilDefect.wd_x06_positive_weakly_tendsto_zero + WeilDefect.wd_x06_vector_weakly_tendsto_limit + WeilDefect.wd_x06_limit_jvalue + WeilDefect.wd_x06_positive_mass_loss_fallthrough | LEAN-CERTIFIED |
| WD-X07 | WeilDefect.wd_x07_response_identity + WeilDefect.wd_x07_real_response_formula + WeilDefect.wd_x07_scaled_response_tendsto_neg_one | LEAN-CERTIFIED |

A `LEAN-IN-PROGRESS` entry becomes `LEAN-CERTIFIED` only after the pinned CI build succeeds. `LEAN-CERTIFIED` entries in the table already have certificate evidence recorded below.

## Current formalization cursor

```math
\boxed{
\texttt{LEAN-H1 EXHAUSTED / H1-P5 COMPLETE / POST-H1 CURSOR NOT SELECTED}
}
```

No further Lean or public-package cursor is active. The certificate sections below remain append-only history.


## WD-X02 earlier failed attempt

Before certification, the implementation in `WeilDefect/Examples/CriticalNonattainment.lean` had a failed dedicated run at commit `76fde3da2385c8f43bb9ac00c04dfcbec686f00a` (GitHub Actions run `36193331699`). This is retained as historical evidence only. A later successful certificate run promoted WD-X02 to `LEAN-CERTIFIED`; see the WD-X02 certificate section below.

## First certificate evidence

The first stable-ID certifications were built at Lean commit:

```math
\boxed{
\texttt{c125114e2dd39fa3907f8690ca39d9c899468caf}.
}
```

GitHub Actions run:

```math
\boxed{
\texttt{35949414095}.
}
```

The run completed successfully with all of:

- pinned dependency resolution;
- mathlib cache fetch;
- Lake build;
- unfinished/project-axiom rejection.

Thus WD-X03 and WD-X04 satisfy the repository's LEAN-CERTIFIED rule.

At this early checkpoint, WD-T26 and WD-X07 still remained LEAN-IN-PROGRESS because their declarations covered only algebraic cores. Both were promoted by later certificate runs recorded below.

## Historical phase cursor

```math
\boxed{
\texttt{LEAN-H1-P1 / ALGEBRAIC AND FINITE-DIMENSIONAL CORE}.
}
```

This records the earlier phase checkpoint and is not the active cursor.


## WD-X01 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-X01: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.wd_x01_weight_sq_telescope;
- WeilDefect.wd_x01_partial_sum;
- WeilDefect.wd_x01_finite_defect_negative;
- WeilDefect.wd_x01_finite_defect_formula;
- WeilDefect.wd_x01_defect_tendsto_zero.

The dedicated theorem CI checked only:

```math
\texttt{WeilDefect/Examples/SpectralScreening.lean}.
```

Certificate run:

```math
\boxed{
\texttt{35952789867}
}
```

at repository head:

```math
\boxed{
\texttt{6ef0dffba1a8732d554b15ee906c64fe60bc63c7}.
}
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- Lean compilation of the WD-X01 target;
- repository unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-X07 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-X07: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.wd_x07_response_identity;
- WeilDefect.wd_x07_real_response_formula;
- WeilDefect.wd_x07_scaled_response_tendsto_neg_one.

The certificate proves the exact two-point rational identity and an explicit
sharpness witness with nonzero inverse-square leading coefficient.

The current theorem file blob

```math
\texttt{83196783b21e40eee21ca74c12b3b8094c2af391}
```

is identical to the blob checked successfully by GitHub Actions run

```math
\boxed{
\texttt{35951096357}.
}
```

That run checked repository commit

```math
\texttt{e9f158d3c8fb5b85494d08931d62cddfc8d4a534}
```

under the pinned Lean 4.34.0 / mathlib v4.34.0 environment and passed the
unfinished-proof/project-axiom gate.

A later dedicated WD-X07 rerun was also launched for redundant single-target
confirmation; certification does not depend on it because the exact current
Lean source blob is already kernel-checked.

No other stable theorem ID is promoted by this certificate.


## WD-T30 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T30: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.wd_t30_two_mode_selected_preserving;
- WeilDefect.wd_t30_both_zero_selected_preserving;
- WeilDefect.wd_t30_two_mode_kernel_combination;
- WeilDefect.wd_t30_zero_functional_preserves_every_mode.

The stable theorem is represented at the functional level:

given a complex-linear selected-response functional $C$ and two multiplier
modes $\psi_1,\psi_2$ whose selected responses are not both zero, Lean
constructs a nontrivial coefficient pair $(\beta_1,\beta_2)$ with

```math
C(\beta_1\psi_1+\beta_2\psi_2)=0.
```

The identically-zero functional branch is also formalized: every mode is
selected-preserving.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Arithmetic.Scalarization}
```

through Lake.

Certificate run:

```math
\boxed{
\texttt{35953990661}
}
```

at repository head:

```math
\boxed{
\texttt{6836f64a22544a2bd51daeb97d97bf824d339def}.
}
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T33 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T33: LEAN-CERTIFIED}.
}
```

Formal declaration:

- WeilDefect.wd_t33_adaptive_cocancellation.

The certificate formalizes the exact cutoffwise algebraic implication:

```math
N+F=P+A,
\qquad
N=A
\quad\Longrightarrow\quad
P=F.
```

This is the complete algebraic content of the audited WD-T33 co-adaptation theorem.
The analytic interpretation of $N,F,P,A$ belongs to the surrounding explicit-formula
setup and is not assumed by the Lean proof.

The current theorem file blob

```math
\texttt{d01f92d725b9ad412130424b74bea9efadcda1e1}
```

is identical to the blob included in successful full-library GitHub Actions run

```math
\boxed{
\texttt{35951096357}.
}
```

That run checked commit

```math
\texttt{e9f158d3c8fb5b85494d08931d62cddfc8d4a534}
```

with:

- pinned dependency resolution;
- mathlib cache retrieval;
- full Lake build;
- unfinished-proof/project-axiom rejection.

A later dedicated WD-T33-only CI run was also launched; certification does not depend
on it because the exact current source blob was already kernel-checked in the successful
full-library run.

No other stable theorem ID is promoted by this certificate.


## WD-T01 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T01: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.WDT01.wd_t01_coeff_identity;
- WeilDefect.WDT01.wd_t01_defect_inner_identity;
- WeilDefect.WDT01.wd_t01_nonnegative_iff;
- WeilDefect.WDT01.negativeWitness_injective_of_zero;
- WeilDefect.WDT01.wd_t01_physical_to_analysis_rank;
- WeilDefect.WDT01.wd_t01_analysis_to_physical_rank;
- WeilDefect.WDT01.wd_t01_negative_rank_iff.

The formal negative-index statement is encoded dimension-by-dimension.

For each $n$, Lean proves equivalence between:

1. an $n$-direction negative witness in the physical carrier; and
2. an $n$-direction negative witness in the closed analysis carrier.

The bridge theorem proves such a unit-sphere negative witness is injective whenever
the quadratic form vanishes at zero. Therefore these witnesses are genuine
$n$-dimensional negative directions, and equality for every finite $n$ is the
formal finite-rank-spectrum version of equality of the supremum negative indices.

The certificate also proves:

```math
[E^*h,E^*h]_J
=
\langle Dh,h\rangle,
```

in the project coefficient/operator encoding, and

```math
\mathcal A\text{ nonnegative}
\iff
D\text{ nonnegative}.
```

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.DefectIndex}.
```

Certificate run:

```math
\boxed{
\texttt{35959085940}
}
```

at repository head:

```math
\boxed{
\texttt{79218489b0a3cdeacc5ed7abe44565ee45fffca5}.
}
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T02 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T02: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations:

- WeilDefect.WDT02.physicalNonnegative_iff_covarianceLe;
- WeilDefect.WDT02.covarianceLe_iff_signed_contractive_factorization;
- WeilDefect.WDT02.reduced_neg_iff;
- WeilDefect.WDT02.signed_reduced_exists_unique;
- WeilDefect.WDT02.wd_t02_contractive_screening_equivalence;
- WeilDefect.WDT02.wd_t02_unique_reduced_solution.

The imported theorem is represented explicitly by the proposition-valued structure

```math
\texttt{WeilDefect.WDT02.DouglasUnitData}.
```

It supplies exactly the Douglas unit-majorization input:

- covariance majorization iff contractive factorization;
- existence and uniqueness of the reduced exact factor.

It is passed as a theorem premise. It is not declared as a project axiom.

Lean then verifies the full Horizon-1 convention transfer:

```math
\mathcal A\text{ nonnegative}
\iff
D\succeq0
\iff
S_-S_-^*\preceq S_+S_+^*
\iff
\exists X,\ \|X\|\le1,\ S_-=-S_+X,
```

where covariance order is encoded by its quadratic-form inequality.

Lean also verifies that the Douglas reduced solution transfers through the
project sign convention and is unique among exact signed solutions whose range
is orthogonal to $\ker S_+$.

The Douglas source theorem itself has not been reconstructed in Lean.
Accordingly this theorem must not be reported as a native LEAN-CERTIFIED result.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.Douglas}.
```

Certificate run:

```math
\boxed{
\texttt{35960549233}
}
```

at repository head:

```math
\boxed{
\texttt{5dca4d98b7062e3676399b34dfc89b383bfe1662}.
}
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T03 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T03: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations include:

- WeilDefect.WDT03.signed_reduced_of_range;
- WeilDefect.WDT03.wd_t03_kernel_decomposition;
- WeilDefect.WDT03.wd_t03_analysis_graph_iff;
- WeilDefect.WDT03.wd_t03_graph_signature;
- WeilDefect.WDT03.wd_t03_defect_factorization;
- WeilDefect.WDT03.wd_t03_reduced_graph_normal_form.

The imported theorem is isolated in the explicit proposition-valued interface
WeilDefect.WDT03.DouglasRangeData. It supplies only the Douglas
range-inclusion step giving the unique reduced exact factor.

Once the reduced signed solution X is supplied, Lean verifies internally the
orthogonal kernel decomposition, graph characterization, graph signature
identity, and defect factorization.

The coefficient direct-sum inner form is represented explicitly as

```math
\langle(a,v),(x,u)\rangle_\oplus
=
\langle a,x\rangle+\langle v,u\rangle,
```

so the formalization does not confuse Lean's ordinary product Banach norm with
the Hilbert direct-sum norm.

Dedicated theorem CI built WeilDefect.Screening.GraphNormalForm.

Certificate run:

```math
\boxed{\texttt{35962199281}}
```

at repository head:

```math
\boxed{\texttt{570dcb25de1e728bb2b135363e0b0d1ae735b5e5}}.
```

The run passed the single-module Lake build and unfinished-proof/project-axiom
gate. The Douglas source theorem itself remains unformalized.

No other stable theorem ID is promoted by this run.


## WD-T04 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T04: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations:

- WeilDefect.WDT04.wd_t04_range_defect_no_exact_screening;
- WeilDefect.WDT04.wd_t04_range_defect_negative;
- WeilDefect.WDT04.wd_t04_over_budget_negative;
- WeilDefect.WDT04.wd_t04_strict_screened_lower_bound;
- WeilDefect.WDT04.wd_t04_attained_critical_neutral;
- WeilDefect.WDT04.wd_t04_nonattained_critical_positive;
- WeilDefect.WDT04.wd_t04_critical_approximate_neutral;
- WeilDefect.WDT04.wd_t04_complete_reduced_taxonomy.

The certificate formalizes the five-way abstract screening morphology:
range defect, over-budget negative defect, strict positive screening, attained
critical neutrality, and non-attained approximate neutrality.

The range-defect negative-direction implication consumes the explicit
WeilDefect.WDT02.DouglasUnitData theorem premise.  Douglas is not introduced as
a project axiom and is not reconstructed by this certificate.  The
over-budget, strict-screening, attained-critical, and non-attained-critical
branches are checked internally once the reduced factor is given.

In particular, the non-attained critical branch does not assume operator-norm
attainment.  Lean derives arbitrarily small graph defect from the definition of
the operator norm while proving every nonzero graph vector remains strictly
positive when no nonzero adjoint vector attains norm one.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.Taxonomy}.
```

Certificate run:

```math
\boxed{\texttt{35965367830}}
```

at repository head:

```math
\boxed{\texttt{fe4ab88bbed7e5a6b1091587569ccb7713522960}}.
```

The certified theorem source blob is:

```math
\texttt{f86f72692fb4465827e4ec9f374a5a3c64f3d22a}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T05 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T05: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations:

- WeilDefect.wd_t05_rank_one_covariance;
- WeilDefect.wd_t05_rank_one_covariance_apply;
- WeilDefect.WDT05.rankOneNegative;
- WeilDefect.WDT05.wd_t05_defect_rank_one;
- WeilDefect.WDT05.wd_t05_signed_factor_iff_vector;
- WeilDefect.WDT05.wd_t05_covariance_iff_unit_vector;
- WeilDefect.WDT05.wd_t05_physical_nonnegative_iff_unit_vector;
- WeilDefect.WDT05.wd_t05_analysis_nonnegative_iff_unit_vector;
- WeilDefect.WDT05.wd_t05_rank_one_specialization.

Lean verifies natively that the one-dimensional synthesis map
$\alpha\mapsto\alpha g$ has covariance $g\otimes g$, hence

```math
D=S_+S_+^*-g\otimes g.
```

It also verifies internally that a signed contractive map
$X:\mathbb C\to K_+$ is equivalent to a single coefficient vector
$c=X(1)$ with $\|c\|\le1$, and reconstructs the converse factor from
$c$ by $\operatorname{toSpanSingleton}(c)$.

The covariance-majorization/positivity-to-factorization step is supplied by
the explicit proposition-valued Douglas premise

```math
\texttt{WeilDefect.WDT02.DouglasUnitData}.
```

Therefore the complete stable theorem is reported as
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE rather than native LEAN-CERTIFIED.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.RankOne}.
```

Certificate run:

```math
\boxed{\texttt{35966956166}}
```

at repository head:

```math
\boxed{\texttt{ef3853ef4a3892662fa59761685dfe68b1f82844}}.
```

The certified theorem source blob is:

```math
\texttt{2c37aaf3546b49cbab8be2c58ee954fd6989a965}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T06 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T06: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT06.ProjectionChainData;
- WeilDefect.WDT06.projection_inner_self;
- WeilDefect.WDT06.projection_norm_mono;
- WeilDefect.WDT06.wd_t06_truncated_inner_identity;
- WeilDefect.WDT06.wd_t06_quadratic_mono;
- WeilDefect.WDT06.wd_t06_quadratic_le_full;
- WeilDefect.WDT06.wd_t06_defect_mono;
- WeilDefect.WDT06.wd_t06_defect_le_full;
- WeilDefect.WDT06.wd_t06_defect_strong_tendsto;
- WeilDefect.WDT06.wd_t06_quadratic_tendsto;
- WeilDefect.WDT06.wd_t06_negative_rank_antitone;
- WeilDefect.WDT06.wd_t06_monotone_positive_screening.

The projection-chain interface records exactly the operator properties consumed by
the proof: self-adjointness, idempotence, nesting, contractivity, and strong
convergence to the identity.

Lean then verifies internally that

```math
D_N=S_+P_NS_+^*-S_-S_-^*
```

has quadratic form

```math
\|P_NS_+^*h\|^2-\|S_-^*h\|^2,
```

that the projected positive norms are nondecreasing under the nested
contractive projections, and hence

```math
D_N\preceq D_{N+1}\preceq D.
```

It also proves strong pointwise operator convergence

```math
D_Nh\to Dh,
```

and pointwise convergence of the corresponding quadratic forms.

Negative-index monotonicity is certified in the same dimension-by-dimension
form used by WD-T01: every $k$-dimensional negative witness for
$D_{N+1}$ is already a $k$-dimensional negative witness for $D_N$.
Thus the attainable finite negative-rank spectrum is nonincreasing under
positive-channel restoration.

No imported theorem premise is used by WD-T06.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.MonotoneScreening}.
```

Certificate run:

```math
\boxed{\texttt{35967932548}}
```

at repository head:

```math
\boxed{\texttt{6024cce8bf4f152ca21a545b93cb467e7cdadb31}}.
```

The certified theorem source blob is:

```math
\texttt{b4424d28e14466275f593e58683170d9e952b134}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T07 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T07: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.wd_t07_selected_full_identity;
- WeilDefect.wd_t07_selected_negative_implies_full;
- WeilDefect.WDT07.wd_t07_full_le_selected;
- WeilDefect.WDT07.wd_t07_negative_rank_custody;
- WeilDefect.WDT07.wd_t07_converse_failure;
- WeilDefect.WDT07.wd_t07_full_negative_without_selected_negative;
- WeilDefect.WDT07.wd_t07_selected_background_monotonicity_and_custody.

Lean verifies the exact quadratic identity

```math
q_{\rm full}(h)
=
q_M(h)-\|S_B^*h\|^2,
```

and therefore the pointwise form order

```math
q_{\rm full}(h)\le q_M(h).
```

It certifies the negative-index custody statement in finite-rank-spectrum form:
for every $k$, any $k$-dimensional negative witness for the selected
quadratic form remains a $k$-dimensional negative witness for the full
quadratic form after arbitrary negative-background aggregation.

The converse is disproved internally by an explicit one-dimensional complex
example: selected positive and negative synthesis maps are zero while the
background synthesis is the identity.  At $h=1$, the selected quadratic
value is zero but the full quadratic value is strictly negative.  Thus full
aggregate negativity does not identify the selected sector as the owner of the
defect.

No imported theorem premise is used by WD-T07.

The first dedicated attempt exposed only a simplifier gap for the adjoint of
the identity map; this was repaired explicitly using mathlib's
`ContinuousLinearMap.adjoint_id`.  No theorem statement changed.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.BackgroundCustody}.
```

Certificate run:

```math
\boxed{\texttt{35968741697}}
```

at repository head:

```math
\boxed{\texttt{48f20dfa63e5b36bd5786a0fc9fe23db9e63e21a}}.
```

The certified theorem source blob is:

```math
\texttt{8a0acaef36c3c10df5f0ec6d7a692db1b420f32a}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T08 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T08: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.WDT08.selected_adjoint_comp_injective;
- WeilDefect.WDT08.wd_t08_selected_negative_rank_le_finrank;
- WeilDefect.WDT08.backgroundNullCoords;
- WeilDefect.WDT08.wd_t08_background_null_finrank_lower;
- WeilDefect.WDT08.wd_t08_selected_negative_on_background_null;
- WeilDefect.WDT08.wd_t08_full_negative_rank_background_reduction;
- WeilDefect.WDT08.wd_t08_finite_selected_sector_index_cap.

For the selected sector, Lean proves that any k-dimensional negative witness
forces the composed adjoint map

```math
S_M^*\circ T : \mathbb C^k \to M
```

to be injective.  Finite-dimensional rank comparison therefore gives

```math
k\le \dim M.
```

This is the finite-rank-spectrum form of

```math
\operatorname{ind}_{-}(D_M)\le \dim M.
```

For the background correction, given any k-dimensional full negative witness
T, Lean forms the canonical coordinate kernel

```math
\ker(S_B^*\circ T).
```

Rank-nullity and the finite-dimensional range bound give

```math
k-\dim B
\le
\dim\ker(S_B^*\circ T).
```

On this kernel the background term vanishes identically, so the full and
selected quadratic forms agree, and Lean proves the selected form is strictly
negative on the unit sphere of that kernel.  This is exactly the
finite-dimensional kernel-slice argument underlying

```math
\operatorname{ind}_{-}(D_{\rm full})
\le
\operatorname{ind}_{-}(D_M)+\dim B.
```

The stable theorem is therefore certified in the same finite-negative-rank /
negative-subspace encoding used by the earlier index certificates.

No imported theorem premise is used by WD-T08.

The first dedicated build exposed only a normalization-through-kernel
simplification issue.  The repair replaced automation by the explicit fact
that a scalar multiple of a kernel vector remains in the kernel; no theorem
statement or mathematical hypothesis changed.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.FiniteIndexCap}.
```

Certificate run:

```math
\boxed{\texttt{36007743473}}
```

at repository head:

```math
\boxed{\texttt{c2b318997f2aaa9ca756ae66f9149ba9ac34956a}}.
```

The certified theorem source blob is:

```math
\texttt{9c61af90ab1374f65df446c558790a8b7f4dff27}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- single-module Lake build;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T09 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T09: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.WDT09.sharedDefect;
- WeilDefect.WDT09.JointBudget;
- WeilDefect.WDT09.FullNonnegative;
- WeilDefect.WDT09.adjoint_of_signed_factor;
- WeilDefect.WDT09.wd_t09_full_quadratic_factorization;
- WeilDefect.WDT09.wd_t09_shared_defect_factorization;
- WeilDefect.WDT09.wd_t09_full_nonnegative_iff_joint_budget;
- WeilDefect.WDT09.wd_t09_separate_contractions_not_joint;
- WeilDefect.WDT09.wd_t09_shared_screening_budget.

The certificate is stated on the reduced positive carrier, encoded by

```math
\ker S_+=0,
```

which is the abstract theorem's $(\ker S_+)^\perp$ target treated as its
own Hilbert carrier.

Under exact signed screening factorizations

```math
S_M=-S_+X_M,
\qquad
S_B=-S_+X_B,
```

Lean verifies the operator identity

```math
D_{\rm full}
=
S_+
\left(
I-X_MX_M^*-X_BX_B^*
\right)
S_+^*.
```

It also proves natively that full nonnegativity is equivalent to the shared
quadratic budget

```math
\|X_M^*a\|^2+\|X_B^*a\|^2
\le
\|a\|^2
\qquad
\forall a.
```

For the reverse implication from full physical nonnegativity to the global
coefficient-space budget, Lean uses

```math
\overline{\operatorname{Ran}S_+^*}
=
(\ker S_+)^\perp
=
K_+,
```

and closure of the budget inequality. Thus no Douglas factorization theorem
premise is consumed by the WD-T09 certificate.

The file imports the Douglas module only to reuse the IsContraction definition
in the explicit separate-versus-joint counterexample. It does not consume
DouglasUnitData or any imported theorem premise.

Lean also certifies that separate unit bounds are insufficient: with both
screening maps equal to the identity on $\mathbb C$, each individual map
has norm one, while the joint budget fails at $a=1$.

The first WD-T09 build exposed only local elaboration issues: theorem
visibility, rewrite order, closed-set construction, and final scalar
arithmetic. These were repaired without changing the theorem statement or
mathematical hypotheses.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.BackgroundCustody}.
```

Certificate run:

```math
\boxed{\texttt{36019357419}}
```

at repository head:

```math
\boxed{\texttt{f08c8f8a5639e1cf9d23b6381ca852c6c2e1007a}}.
```

The certified theorem source blob is:

```math
\texttt{eec7e8db876cf2504bc3cca349b68bb60d93a626}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T09-containing module;
- unfinished-proof/project-axiom rejection.

No other stable theorem ID is promoted by this run.


## WD-T10 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T10: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations include:

- WeilDefect.WDT10.residualBudget;
- WeilDefect.WDT10.wd_t10_residual_budget_positive;
- WeilDefect.WDT10.residualSqrt;
- WeilDefect.WDT10.wd_t10_residual_sqrt_selfAdjoint;
- WeilDefect.WDT10.wd_t10_residual_sqrt_sq;
- WeilDefect.WDT10.effectivePositive;
- WeilDefect.WDT10.wd_t10_effective_covariance;
- WeilDefect.WDT10.wd_t10_background_covariance_elimination;
- WeilDefect.WDT10.wd_t10_full_defect_reduction;
- WeilDefect.WDT10.wd_t10_shared_defect_inner_identity;
- WeilDefect.WDT10.wd_t10_full_nonnegative_iff_effective_physical;
- WeilDefect.WDT10.wd_t10_full_nonnegative_iff_residual_screening;
- WeilDefect.WDT10.wd_t10_background_elimination_and_residual_budget.

Assuming an exact contractive background screen

```math
S_B=-S_+X_B,
\qquad
\|X_B\|\le1,
```

Lean verifies natively that

```math
R_B=I-X_BX_B^*
```

is positive.  The canonical square root is constructed by mathlib's continuous
functional calculus,

```math
R_B^{1/2}:=\operatorname{CFC.sqrt}(R_B),
```

and Lean checks both self-adjointness and

```math
R_B^{1/2}R_B^{1/2}=R_B.
```

For

```math
S_{\rm eff}=S_+R_B^{1/2},
```

Lean then proves internally

```math
S_{\rm eff}S_{\rm eff}^*
=
S_+R_BS_+^*
=
S_+S_+^*-S_BS_B^*,
```

hence

```math
D_{\rm full}
=
S_{\rm eff}S_{\rm eff}^*-S_MS_M^*.
```

The corresponding scalar quadratic forms are identified exactly, so full
nonnegativity is reduced to physical nonnegativity of the effective
two-channel defect.

The final screening-existence clause consumes the explicit proposition-valued
premise

```math
\texttt{WeilDefect.WDT02.DouglasUnitData\ S_M\ S_eff}.
```

Downstream from that premise, Lean verifies

```math
D_{\rm full}\succeq0
\iff
\exists Y, \|Y\|\le1,\quad S_M=-S_{\rm eff}Y.
```

The CFC square-root theorems are ordinary kernel-checked mathlib library
results and are not an imported project theorem premise.  The only imported
boundary in the stable WD-T10 statement is the same Douglas factorization
interface already isolated in WD-T02.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.ResidualBudget}.
```

Certificate run:

```math
\boxed{\texttt{36021712105}}
```

at repository head:

```math
\boxed{\texttt{1e5b881fd412ce88de62564c57637702f16858c8}}.
```

The certified theorem source blob is:

```math
\texttt{1ffb6b2a80620b266798d40e68fe3329dc2cfb78}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T10 module;
- unfinished-proof/project-axiom rejection.

The first two WD-T10 compiler passes exposed only local Lean representation and
rewrite issues around adjoints, CFC square-root order hypotheses, composition
association, and scalar quadratic-form transport.  Those repairs did not alter
the theorem statement or mathematical hypotheses.

No other stable theorem ID is promoted by this run.


## WD-T11 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T11: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT11.wd_t11_norm_activeScreen;
- WeilDefect.WDT11.wd_t11_norm_activeAdjoint;
- WeilDefect.WDT11.wd_t11_norm_one_attains_neutral;
- WeilDefect.WDT11.wd_t11_graphQ_eigenvector;
- WeilDefect.WDT11.wd_t11_graphQ_diagonal;
- WeilDefect.WDT11.wd_t11_negative_rank_le_count;
- WeilDefect.WDT11.wd_t11_negative_space_strict;
- WeilDefect.WDT11.wd_t11_negative_space_finrank;
- WeilDefect.WDT11.wd_t11_negative_rank_count_exists;
- WeilDefect.WDT11.wd_t11_negative_index_exact;
- WeilDefect.WDT11.wd_t11_neutral_space_finrank;
- WeilDefect.WDT11.wd_t11_neutral_space_graphQ_zero;
- WeilDefect.WDT11.wd_t11_finite_sector_singular_value_inertia.

The certificate formalizes finite-sector singular-value inertia on the canonical
active carrier. Lean proves that the number of singular values strictly greater
than one is the exact maximal finite negative rank, that the singular values
equal to one give the neutral-space dimension, and that operator norm one is
attained by an actual nonzero neutral graph direction.

No imported project theorem premise is consumed by WD-T11.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.FiniteSectorInertia}.
```

Certificate run:

```math
\boxed{\texttt{36032799794}}
```

at repository head:

```math
\boxed{\texttt{44a2634f87604dc7d8d82ec36db8ba379e1b64aa}}.
```

The certified theorem source blob is:

```math
\texttt{5404514d874c1cdc710045cab7819601d0a6994f}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T11 module;
- unfinished-proof/project-axiom rejection.

The certification repair passes changed proof engineering only; no stable theorem
statement or mathematical hypothesis was weakened.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T12 / WD-B6 — SEQUENTIAL ELIMINATION}
}
```


## WD-T12 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T12: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.WDT12.sequentialResidualBudget;
- WeilDefect.WDT12.wd_t12_sequential_budget_covariance;
- WeilDefect.WDT12.wd_t12_second_background_elimination;
- WeilDefect.WDT12.wd_t12_sequential_background_consumption.

The certificate formalizes sequential background consumption under the exact
residual-factorization hypothesis. After the first contractive screen, the
second background is required to factor through the first effective positive
synthesis. Lean verifies that the twice-consumed covariance is both

```math
S_+
\left(
R_1-R_1^{1/2}Y_2Y_2^*R_1^{1/2}
\right)
S_+^*
```

and

```math
S_1(I-Y_2Y_2^*)S_1^*.
```

No imported project theorem premise is consumed by WD-T12. The proof reuses
the native algebraic WD-T10 residual-budget lemmas and does not invoke a
Douglas premise.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.SequentialElimination}.
```

Certificate run:

```math
\boxed{\texttt{36057422878}}
```

at repository head:

```math
\boxed{\texttt{cbbaf45442ec5f6cae5cb4e639882a3f2e2c6304}}.
```

The certified theorem source blob is:

```math
\texttt{482eee655471c74e6e87733b3441b2bd26990ab9}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T12 module;
- unfinished-proof/project-axiom rejection.

WD-T12 compiled successfully on the first formal pass.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T13 / WD-B7 — DIRECT COMPRESSION VERSUS SHORTED COVARIANCE}
}
```

The audited WD-T13 hypothesis is the corrected uniformly positive setting
$K\succeq mI$, which guarantees bounded invertibility of the complementary
block.


## WD-T13 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T13: LEAN-CERTIFIED}.
}
```

The certificate uses the corrected uniformly positive hypothesis

```math
K\succeq mI,
\qquad m>0,
```

for the self-adjoint block operator. The Hilbert direct-sum lower bound is
encoded explicitly in `WeilDefect.WDT13.BlockUniformlyPositive`.

Formal declarations include:

- WeilDefect.WDT13.wd_t13_complement_lower_bound;
- WeilDefect.WDT13.wd_t13_complement_isUnit;
- WeilDefect.WDT13.wd_t13_complement_inverse_nonnegative;
- WeilDefect.WDT13.wd_t13_schur_correction_positive;
- WeilDefect.WDT13.wd_t13_schur_le_compression;
- WeilDefect.WDT13.wd_t13_schur_lower_bound;
- WeilDefect.WDT13.wd_t13_schur_isUnit;
- WeilDefect.WDT13.wd_t13_block_solution_exists;
- WeilDefect.WDT13.wd_t13_block_solution_first_component;
- WeilDefect.WDT13.wd_t13_direct_compression_versus_shorted_covariance.

Lean derives bounded invertibility of the complementary block from the uniform
lower bound; it is not assumed. For

```math
H_W=A-BC^{-1}B^*,
```

Lean proves

```math
H_W\preceq A
```

and a uniform lower bound on $H_W$, hence bounded invertibility of
$H_W$.

The inverse-compression identity is kernel-checked in its equivalent block
solution form: every solution of

```math
Ax+By=w,
\qquad
B^*x+Cy=0
```

has

```math
x=H_W^{-1}w,
```

and such a solution is constructed for every $w$. This is the coordinate
form of $P_WK^{-1}|_W=H_W^{-1}$.

No imported project theorem premise is consumed by WD-T13.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.ShortedCovariance}.
```

Certificate run:

```math
\boxed{\texttt{36059475701}}
```

at repository head:

```math
\boxed{\texttt{b2af38e06332be4d68a57a159fdf4ca547e372cd}}.
```

The certified theorem source blob is:

```math
\texttt{a0c3ee14272f34dff041601b5abdfaeca7841e8b}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T13 module;
- unfinished-proof/project-axiom rejection.

The certification retained the corrected uniformly positive hypothesis from the
P4 audit; no theorem statement or mathematical hypothesis was weakened.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T14 / WD-B8 — FINITE POSITIVE SHADOWS PRESERVE SIGNATURE BUT NOT ADMISSIBILITY}
}
```


## WD-T14 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T14: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.WDT14.shadowMargin;
- WeilDefect.WDT14.wd_t14_positive_shadow_margin;
- WeilDefect.WDT14.wd_t14_positive_shadow_preserves_negative_margin;
- WeilDefect.WDT14.wd_t14_graph_shadow_admissible_iff;
- WeilDefect.WDT14.wd_t14_graph_admissibility_failure_example;
- WeilDefect.WDT14.wd_t14_finite_positive_shadows_preserve_signature_not_admissibility.

For every orthogonal positive-coordinate projection $P_U$, Lean certifies

```math
\|u\|^2-\|P_Ua\|^2
\ge
\|u\|^2-\|a\|^2.
```

Hence positive truncation preserves, and can only strengthen, a positive
negative margin.

For graph vectors $u=-X^*a$, Lean also proves the exact admissibility
criterion

```math
u=-X^*P_Ua
\iff
X^*(a-P_Ua)=0.
```

An explicit $\mathbb C$ counterexample with $X=2I$, $a=1$,
$u=-2$, and zero positive projection has margin $3>0$ before and after
the signature shadow while the projected pair is not graph-admissible.

Thus the stable distinction between signature shadow and admissible analysis
vector is kernel-checked.

No imported project theorem premise is consumed by WD-T14.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Screening.FinitePositiveShadows}.
```

Certificate run:

```math
\boxed{\texttt{36062388096}}
```

at repository head:

```math
\boxed{\texttt{adcdc167eb274af899a1a53dfb86b76c5bc442ae}}.
```

The certified theorem source blob is:

```math
\texttt{ed287dfd0dbe7e47cdbb074c0fda64bcd0bc6e41}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T14 module;
- unfinished-proof/project-axiom rejection.

The only repair residue was normalization of the concrete scaled-identity
adjoint in the counterexample; no theorem statement or hypothesis changed.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T15 / WD-C1+WD-C2 — RIGHT-LIMIT PROJECTION CONVERGENCE AND GAP-SPACE DUALITY}
}
```


## WD-T15 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T15: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT15.rightLimit;
- WeilDefect.WDT15.gapLimit;
- WeilDefect.WDT15.wd_t15_gap_antitone;
- WeilDefect.WDT15.wd_t15_right_limit_gap_duality;
- WeilDefect.WDT15.wd_t15_sequence_right_limit_eq;
- WeilDefect.WDT15.wd_t15_sequence_gap_eq_right_limit_orthogonal;
- WeilDefect.WDT15.wd_t15_monotone_projection_limit;
- WeilDefect.WDT15.wd_t15_right_limit_projection_and_gap_duality.

The certificate represents the right-limit analysis space as the
`ClosedSubmodule` infimum

```math
A_{c+}=\bigcap_{t>c}A_t
```

and the limiting gap as the closed-submodule supremum

```math
G_{c+}
=
\overline{\operatorname{span}\bigcup_{t>c}A_t^\perp}.
```

Lean proves the gap duality

```math
A_{c+}=G_{c+}^{\perp}.
```

For every antitone real sequence $t_n\downarrow c$ from the right and every
vector $x$, Lean also proves

```math
P_{A_{t_n}}x\to P_{A_{c+}}x.
```

The P4 audit records that the sequential formulation suffices for the
real-parameter strong-limit statement.

No imported project theorem premise is consumed by WD-T15.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Filtration.RightLimit}.
```

Certificate run:

```math
\boxed{\texttt{36070010269}}
```

at repository head:

```math
\boxed{\texttt{ee1efb86924caa501e0bfaa4ab8a1478736c64d8}}.
```

The certified theorem source blob is:

```math
\texttt{2df4a12993a7fdad3695deb5e68e7ae526b8ebee}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T15 module;
- unfinished-proof/project-axiom rejection.

Repair work changed Lean representation only; no theorem statement or
mathematical hypothesis was weakened.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T16 / WD-C3+WD-C5 — FIXED FINITE NEGATIVE-SECTOR PERSISTENCE}
}
```


## WD-T16 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T16: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT16.exists_weaklyTendsto_subseq_of_norm_le;
- WeilDefect.WDT16.weaklyTendsto_norm_sq_le_of_tendsto;
- WeilDefect.WDT16.wd_t16_fixed_negative_sector_compactness;
- WeilDefect.WDT16.wd_t16_nonpositive_limit_persists;
- WeilDefect.WDT16.wd_t16_uniform_negative_margin_persists;
- WeilDefect.WDT16.wd_t16_uniform_negative_margin_forces_endpoint_jump;
- WeilDefect.WDT16.wd_t16_fixed_finite_negative_sector_persistence.

The coefficient Hilbert space is represented by the actual $L^2$-product
$K_+\oplus M$, with $M$ finite-dimensional.

Lean natively extracts a weakly convergent subsequence of the positive
coordinates without assuming global separability: it localizes to the
separable closed span of the sequence, passes through the Fréchet–Riesz
isometry, applies sequential Banach–Alaoglu in the weak dual, and lifts the
result back to the ambient Hilbert space.

Finite-dimensional compactness gives strong convergence of the negative
coordinate. The assembled weak limit lies in the WD-T15 right-limit space.

For normalized signatures

```math
J(a_n,u_n)\to q_*\le0,
```

Lean proves

```math
\boxed{
\exists,0\ne y\in A_{c+},
\qquad
J(y)\le q_*.
}
```

For a uniform margin $\kappa>0$,

```math
J(a_n,u_n)\le-\kappa,
```

Lean proves

```math
\boxed{
\exists,0\ne y\in A_{c+},
\qquad
J(y)\le-\kappa.
}
```

If the endpoint $A_c$ is $J$-nonnegative, the produced vector is also
certified to lie in

```math
A_{c+}\setminus A_c.
```

No imported project theorem premise is consumed by WD-T16.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Filtration.FiniteNegativeSector}.
```

Certificate run:

```math
\boxed{\texttt{36078296999}}
```

at repository head:

```math
\boxed{\texttt{6c8bd4b57eb18c583d426c767beca21f06307f69}}.
```

The certified theorem source blob is:

```math
\texttt{f7f2a50f8183ba1a617ce1cf97855461bbbbda5f}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T16 module;
- unfinished-proof/project-axiom rejection.

The final audited WD-C3 nonpositive-limit theorem was added before promotion;
the certificate does not merely cover the compactness core.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T17 / WD-C4 — FIXED-SECTOR CRITICAL DICHOTOMY}
}
```


## WD-T17 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T17: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT17.weaklyTendsto_strong_of_norm_sq_tendsto;
- WeilDefect.WDT17.NeutralCriticalBranch;
- WeilDefect.WDT17.NegativeFallthroughBranch;
- WeilDefect.WDT17.wd_t17_critical_positive_mass_le_half;
- WeilDefect.WDT17.wd_t17_fixed_sector_critical_dichotomy;
- WeilDefect.WDT17.wd_t17_neutral_branch;
- WeilDefect.WDT17.wd_t17_loss_branch.

For a unit-normalized critical sequence in a fixed finite negative sector,

```math
J(y_n)\to0,
```

Lean proves

```math
\|a_n\|^2\to\frac12,
\qquad
\|u_n\|^2\to\frac12.
```

After the WD-T16 compactness extraction, the nonzero right-limit vector
$y=(a,u)$ satisfies exactly one of two alternatives:

1. $\|a\|^2=1/2$, hence $J(y)=0$, weak convergence of the positive
   coordinate upgrades to strong convergence, and the full coefficient
   subsequence converges strongly to $y$;
2. $\|a\|^2<1/2$, hence $J(y)<0$.

The assembled theorem proves both exhaustivity and mutual exclusion of these
branches.

No imported project theorem premise is consumed by WD-T17.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Filtration.CriticalDichotomy}.
```

Certificate run:

```math
\boxed{\texttt{36081480092}}
```

at repository head:

```math
\boxed{\texttt{ed92f76a62c26ab48f35f7637c07bdf9568dccab}}.
```

The certified theorem source blob is:

```math
\texttt{7102a25b28f7a8cf72e805f845bad23daf535aa2}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T17 module;
- unfinished-proof/project-axiom rejection.

Repair work changed only Lean normalization and coercion details; no theorem
statement or mathematical hypothesis was weakened.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T18 / WD-C6 — ENDPOINT-JUMP QUOTIENT BOUNDS NEW RIGHT-LIMIT NEGATIVE INDEX}
}
```


## WD-T18 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T18: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT18.endpointInside;
- WeilDefect.WDT18.endpointQuotientMap;
- WeilDefect.WDT18.wd_t18_endpoint_quotient_map_injective;
- WeilDefect.WDT18.wd_t18_endpoint_jump_negative_rank_le_quotient;
- WeilDefect.WDT18.wd_t18_one_dimensional_jump_rank_cap.

For closed endpoint/right-limit spaces $A_0\subseteq A_+$, Lean formalizes
the endpoint quotient $A_+/A_0$. Any finite-dimensional strictly negative
witness in $A_+$ injects into that quotient when the endpoint is
nonnegative. Hence every such witness rank is bounded by the quotient
dimension; in particular a one-dimensional jump caps the finite negative rank
at one.

No imported project theorem premise is consumed by WD-T18.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Filtration.EndpointJump}.
```

Certificate run:

```math
\boxed{\texttt{36082262379}}
```

at repository head:

```math
\boxed{\texttt{f02683ec35aa1d61ee056512f2a9977e081a7990}}.
```

The certified theorem source blob is:

```math
\texttt{d7743465cac328c8aa6236fb12942117b8e67a7e}.
```

The run passed pinned dependency resolution, mathlib cache retrieval, the
direct Lake build, and unfinished-proof/project-axiom rejection.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T19 / WD-C7+WD-C8+WD-C9 — NEW ENDPOINT VECTORS FORCE BOUNDARY AMPLIFICATION / REPRESENTATIVE BLOW-UP}
}
```


## WD-T19 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T19: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.WDT19.analysisSpace;
- WeilDefect.WDT19.weaklyTendsto_of_tendsto;
- WeilDefect.WDT19.weaklyTendsto_map;
- WeilDefect.WDT19.weaklyTendsto_unique;
- WeilDefect.WDT19.weak_limit_mem_physical_rightLimit;
- WeilDefect.WDT19.wd_t19_endpoint_representative_blowup;
- WeilDefect.WDT19.BoundaryAmplifies;
- WeilDefect.WDT19.wd_t19_boundary_amplification;
- WeilDefect.WDT19.wd_t19_vanishing_amplitude_normalized_blowup.

For a common bounded physical map $T$ and right-continuous nested physical
spaces, Lean proves that any new endpoint vector requires representative norm
blow-up, upgrades that statement to the full local boundary-amplification
predicate, and certifies the reciprocal-growth identity for vanishing-amplitude
normalized representatives.

No imported project theorem premise is consumed by WD-T19.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.Filtration.RepresentativeBlowup}.
```

Certificate run:

```math
\boxed{\texttt{36083158273}}
```

at repository head:

```math
\boxed{\texttt{33f5a187baf7e195c19e179bb3b6b9befb7a0700}}.
```

The certified theorem source blob is:

```math
\texttt{6645820485d46afe8566e1812de0e301fb290ba2}.
```

The run passed pinned dependency resolution, mathlib cache retrieval, the
direct Lake build, and unfinished-proof/project-axiom rejection.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T20 / ZW1-T1 — CANONICAL CONJUGATE-PAIR DIAGONALIZATION INTO POSITIVE/NEGATIVE WEIL CHANNELS}
}
```


## WD-T20 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T20: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.wd_t20_pair_pos_eigen;
- WeilDefect.wd_t20_pair_neg_eigen;
- WeilDefect.pairEigenEquiv;
- WeilDefect.wd_t20_pair_diagonalization.

For one distinct nonreal conjugate pair, Lean represents conjugation as a
two-coordinate swap and proves that the symmetric and antisymmetric channels
are the $+1$ and $-1$ eigendirections. The complex-linear
`pairEigenEquiv` identifies raw pair coefficients with positive/negative
channel coordinates, in which the involution is exactly

```math
(a,b)\mapsto(a,-b).
```

The formal source uses unnormalized representatives $(1,1)$ and
$(1,-1)$; these span the same canonical eigendirections as the normalized
$1/\sqrt2$ convention.

WD-T20 is pair-level algebra after reduction to a distinct conjugate-pair
coordinate. The separate same-frequency multiplicity quotient remains WD-T23.

No imported project theorem premise is consumed by WD-T20.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.PairGeometry}.
```

Certificate run:

```math
\boxed{\texttt{36087496196}}
```

at repository head:

```math
\boxed{\texttt{9b8142168cb5e4a5bd53e4d6e903abec211465d4}}.
```

The certified theorem source blob is:

```math
\texttt{a15e6eb544f9154836644d1a82a607f10639cbb3}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T20 module;
- unfinished-proof/project-axiom rejection.

The theorem source required no repair during this certification cursor.

Next theorem cursor:

```math
\boxed{
\texttt{WD-T21 / ZW1-T2 — ONE SIMPLE ZETA QUARTET CONTRIBUTES TWO NEGATIVE PAIR COORDINATES}
}
```


## WD-T21 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T21: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.quartetPairPos;
- WeilDefect.quartetPairNeg;
- WeilDefect.wd_t21_quartet_pair_pos_conjugate;
- WeilDefect.wd_t21_quartet_pair_neg_conjugate;
- WeilDefect.wd_t21_quartet_pairs_nonreal;
- WeilDefect.wd_t21_quartet_pairs_distinct;
- WeilDefect.wd_t21_simple_quartet_negative_count;
- WeilDefect.wd_t21_simple_quartet_pair_geometry.

Under the simple off-critical nondegeneracy assumptions

```math
T\ne0,
\qquad
\delta\ne0,
```

Lean certifies that the Bombieri ordinate coordinates

```math
\{T+i\delta,T-i\delta\}
```

and

```math
\{-T+i\delta,-T-i\delta\}
```

are two distinct nonreal complex-conjugate pairs.

Combining this with WD-T20's pair diagonalization, one simple quartet has
exactly two canonical negative pair coordinates. The formal coordinate type
is `Fin 2`, with cardinality two.

WD-T21 is only the coefficient-space count. Equality with the finite Weil
matrix negative spectral index remains WD-T22 and uses Bombieri's imported
finite-inertia theorem.

No imported project theorem premise is consumed by WD-T21.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.PairGeometry}.
```

Certificate run:

```math
\boxed{\texttt{36088674422}}
```

at repository head:

```math
\boxed{\texttt{e8e1c6b9e1f9f9f566d6398b296d7b30b827ef3d}}.
```

The certified theorem source blob is:

```math
\texttt{427fbe49617add15010ba812c6140e07a7b9507f}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T21 module;
- unfinished-proof/project-axiom rejection.

The only compiler repair was the pinned complex-conjugation API name; no
mathematical statement was weakened.

## WD-T22 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T22: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations:

- WeilDefect.BombieriFiniteInertiaData;
- WeilDefect.wd_t22_finite_weil_inertia_saturation;
- WeilDefect.SimpleQuartetPacketNegative;
- WeilDefect.wd_t22_simple_quartet_packet_pair_count;
- WeilDefect.wd_t22_simple_quartet_packet_inertia;
- WeilDefect.wd_t22_two_simple_quartet_negative_index.

The pinned Bombieri finite-inertia theorem (Theorem 8, p. 213) is represented
explicitly by the proposition-valued premise

```math
\texttt{BombieriFiniteInertiaData}.
```

It supplies exactly the imported equality between the finite Weil matrix's
negative spectral index and the number of distinct nonreal conjugate pairs.
It is passed as a theorem premise and is not declared as a project axiom.

Lean then verifies the packet specialization internally.  Using WD-T21's
two negative pair coordinates per simple quartet, a packet of $q$ simple
disjoint quartets has pair-coordinate cardinality

```math
2q.
```

Therefore the imported Bombieri equality specializes to

```math
\operatorname{ind}_{-}=2q,
```

and for the audited two-quartet packet:

```math
\boxed{
\operatorname{ind}_{-}=4.
}
```

The Bombieri source theorem itself has not been reconstructed in Lean, so this
result must not be reported as a native LEAN-CERTIFIED theorem.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.PairGeometry}.
```

Certificate run:

```math
\boxed{\texttt{36089403584}}
```

at repository head:

```math
\boxed{\texttt{83914d302ba9201983c5e0b0d4404b727714acbd}}.
```

The certified theorem source blob is:

```math
\texttt{91bc6efce70e05a3ec1d320ec8ee1e99abc6be3d}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T22 target module;
- unfinished-proof/project-axiom rejection.

No stable theorem statement or mathematical hypothesis was weakened.

## WD-T23 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T23: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations:

- WeilDefect.BombieriMultiplicityNullData;
- WeilDefect.wd_t23_same_frequency_synthesis_factor;
- WeilDefect.wd_t23_same_frequency_zero_sum_null;
- WeilDefect.wd_t23_total_multiplicity_nullity;
- WeilDefect.wd_t23_single_ordinate_nullity;
- WeilDefect.wd_t23_single_ordinate_has_null_iff_repeated;
- WeilDefect.wd_t23_distinct_frequency_reduction.

The direct coefficient mechanism is proved natively.  For duplicate
same-frequency coordinates with common physical shape $g$, Lean verifies

```math
\sum_i x_i g
=
\left(\sum_i x_i\right)g.
```

Hence every zero-sum duplicate coefficient combination is an exact
synthesis-null direction.

The exact nullity count is the imported part.  Bombieri Lemma 10 and its proof
continuation are represented by the explicit proposition-valued premise

```math
\texttt{BombieriMultiplicityNullData}.
```

For distinct ordinates of raw multiplicities $m_j$, it supplies exactly

```math
\operatorname{nullity}
=
\sum_j (m_j-1).
```

For one ordinate of multiplicity $m$, Lean specializes this to

```math
\operatorname{nullity}=m-1
```

and proves that a nontrivial multiplicity-null sector occurs exactly when
$m>1$.

Thus multiplicity-null directions are formally separated from the active
distinct-frequency channel before independent negative-index counting.  The
Bombieri source theorem itself is not reconstructed in Lean and is not a
project axiom.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.PairGeometry}.
```

Certificate run:

```math
\boxed{\texttt{36089684621}}
```

at repository head:

```math
\boxed{\texttt{a16b63021e91639beb59bfc387946531aa1fdd83}}.
```

The certified theorem source blob is:

```math
\texttt{853b2de7d7df4a435059d7f5cb3ae0fe89a5baeb}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T23 target module;
- unfinished-proof/project-axiom rejection.

No stable theorem statement or mathematical hypothesis was weakened.

## WD-T24 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T24: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.realExpMode;
- WeilDefect.realExpMode_ne_zero;
- WeilDefect.hasDerivAt_realExpMode;
- WeilDefect.iteratedDeriv_realExpMode;
- WeilDefect.contDiffAt_const_mul_realExpMode;
- WeilDefect.iteratedDeriv_finite_exp_sum;
- WeilDefect.wd_t24_finite_distinct_frequency_exponential_independence.

For distinct complex frequencies $\lambda_i$, Lean certifies that if

```math
\sum_i c_i e^{\lambda_i x}=0
```

throughout a nonempty real interval, then every coefficient $c_i$ is zero.

The proof is fully internal.  It chooses an interior point $x_0$, differentiates
the local zero relation through orders $0,\dots,n-1$, and obtains

```math
\sum_i
\bigl(c_i e^{\lambda_i x_0}\bigr)\lambda_i^k
=
0.
```

Mathlib's Vandermonde nonsingularity theorem then forces all weighted
coefficients to vanish.  Since the complex exponential is never zero, every
$c_i$ vanishes.

No analytic-continuation theorem and no imported project theorem premise is
needed.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.FiniteExponentialIndependence}.
```

Certificate run:

```math
\boxed{\texttt{36093132364}}
```

at repository head:

```math
\boxed{\texttt{79882bdc976581db62bbc783d52f8bb4ac01e214}}.
```

The certified theorem source blob is:

```math
\texttt{7244cb18dd652c02619f6b56061443e00097df5f}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T24 target module;
- unfinished-proof/project-axiom rejection.

The repair passes resolved Lean parser and real/complex module-instance
ambiguities only; no theorem statement or mathematical hypothesis was weakened.

## WD-T25 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T25: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.problemOneDenominator;
- WeilDefect.problemOneL;
- WeilDefect.problemOneL_realExpMode;
- WeilDefect.problemOneMode;
- WeilDefect.problemOneDenominator_half;
- WeilDefect.problemOneDenominator_neg_half;
- WeilDefect.problemOneL_problemOneMode;
- WeilDefect.problemOneL_const_mul_problemOneMode;
- WeilDefect.problemOneL_fin_sum;
- WeilDefect.wd_t25_finite_problem_one_relation_trivial;
- WeilDefect.wd_t25_no_exact_finite_positive_compensation.

Lean represents the Problem-1 differential operator as

```math
L=-\frac{d^2}{dx^2}+\frac14.
```

For an exponential mode $e^{\lambda x}$, it certifies

```math
L e^{\lambda x}
=
\left(\frac14-\lambda^2\right)e^{\lambda x}.
```

A Green-preconditioned Problem-1 coordinate is represented as one reciprocal
particular solution plus arbitrary boundary-homogeneous terms at frequencies
$\pm 1/2$.  Lean proves that the two boundary terms are killed by $L$, and
that a reciprocal coefficient satisfying

```math
q\left(\frac14-\lambda^2\right)=1
```

is mapped back to the raw exponential mode.

Consequently, any finite exact relation among distinct-frequency
Green-preconditioned coordinates on a nonempty interval is sent by $L$ to a
finite distinct-frequency exponential relation.  WD-T24 then forces every
coefficient to vanish.

The anchored corollary therefore proves that if one selected channel has a
nonzero coefficient, no finite family of distinct-frequency compensating
channels can cancel it exactly on a nontrivial interval.

No imported project theorem premise is consumed by WD-T25.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.ProblemOneIndependence}.
```

Certificate run:

```math
\boxed{\texttt{36093665687}}
```

at repository head:

```math
\boxed{\texttt{ae100c2bfd4fddcc45296f52e0b38d844344477d}}.
```

The certified theorem source blob is:

```math
\texttt{a799e0931c557a977b8163fc21940defa366fdee}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T25 target module;
- rebuilding and rechecking the WD-T24 dependency;
- unfinished-proof/project-axiom rejection.

The single repair pass changed Lean representation only; no theorem statement
or mathematical hypothesis was weakened.

## WD-T26 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T26: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.rawResiduesOfNegativePairs;
- WeilDefect.wd_t26_zero_moment;
- WeilDefect.wd_t26_coefficient_mem_rawResidues;
- WeilDefect.wd_t26_nonzero_raw_residue_of_nonzero_coefficient;
- WeilDefect.wd_t26_selected_zero_moment_residue.

For a finite list of selected negative pair coefficients

```math
(\alpha_1,\dots,\alpha_m),
```

the raw residue map is represented as

```math
(\alpha_1,-\alpha_1,\dots,\alpha_m,-\alpha_m).
```

Lean certifies the zero-moment identity

```math
\sum_j v_j=0
```

by pairwise antisymmetry.

The nondegeneracy half is also certified: if at least one selected negative
coefficient is nonzero, then at least one raw residue is nonzero.  The custody
bridge is direct: each coefficient $\alpha$ occurs verbatim as one of the
two raw residues $(\alpha,-\alpha)$.

Thus the associated raw residue vector has zero total residue and cannot
collapse to the zero residue vector when the selected negative coefficient
vector is genuinely nonzero.

No imported project theorem premise, prime-side input, pole term, or
archimedean input is consumed by WD-T26.

Dedicated theorem CI built:

```math
\texttt{WeilDefect.PairGeometry}.
```

Certificate run:

```math
\boxed{\texttt{36095464414}}
```

at repository head:

```math
\boxed{\texttt{a02e9176ca3f6dd071ab9b43226d025efb5f7592}}.
```

The certified WD-T26 source commit is:

```math
\texttt{61110e7fc77722dbfa0a1459f101d98ae90efff8}.
```

The certified theorem source blob is:

```math
\texttt{5361e8384880fcd799fbd62151b65be7a11f3cf8}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T26 target module;
- unfinished-proof/project-axiom rejection.

No stable theorem statement or mathematical hypothesis was weakened.

## WD-T27 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T27: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.rationalResponse;
- WeilDefect.residueFirstMoment;
- WeilDefect.residueSecondMomentNorm;
- WeilDefect.inv_sub_laurent_two;
- WeilDefect.weighted_inv_sub_laurent_two;
- WeilDefect.rationalResponse_laurent_two;
- WeilDefect.rationalResponse_zero_moment_expansion;
- WeilDefect.rationalResponse_remainder_term_bound;
- WeilDefect.rationalResponse_zero_moment_remainder_bound;
- WeilDefect.residueRadius;
- WeilDefect.norm_le_residueRadius;
- WeilDefect.rationalResponse_zero_moment_remainder_isBigO;
- WeilDefect.rationalResponse_zero_moment_isBigO;
- WeilDefect.wd_t27_universal_inverse_square_far_decay;
- WeilDefect.wd_t27_universal_inverse_square_isBigO.

For a finite residue vector $v$ at locations $\rho_i$, Lean certifies the
exact Laurent decomposition

```math
R_v(z)
=
\frac{\sum_i v_i}{z}
+
\frac{M_1(v)}{z^2}
+
\sum_i
\frac{v_i\rho_i^2}{z^2(z-\rho_i)},
```

where

```math
M_1(v)=\sum_i \rho_i v_i.
```

Under the WD-T26 zero-moment condition

```math
\sum_i v_i=0,
```

the inverse-linear term disappears exactly.

Lean then proves the quantitative far-field bound: whenever

```math
2\|\rho_i\|\le \|z\|
```

for every selected pole,

```math
\left\|
R_v(z)-\frac{M_1(v)}{z^2}
\right\|
\le
\frac{
2\sum_i \|v_i\|\|\rho_i\|^2
}{
\|z\|^3
}.
```

Thus the precise first-moment refinement is kernel-checked, with no hidden
uniformity beyond the fixed finite packet.

The same module also certifies the literal Landau statements on the complex
cobounded filter:

```math
R_v(z)-\frac{M_1(v)}{z^2}
=
O(\|z\|^{-3}),
```

and

```math
\boxed{
R_v(z)=O(\|z\|^{-2}).
}
```

No imported project theorem premise is consumed by WD-T27.

The quantitative core first passed in CI run:

```math
\texttt{36096310211}.
```

The final certificate including the literal Landau corollaries is:

```math
\boxed{\texttt{36097347267}}
```

at repository head:

```math
\boxed{\texttt{3990122ea425e7bb84b6093cd5e1b5a791c11e8c}}.
```

The certified theorem source blob is:

```math
\texttt{aed1edaa7734adb0a1ede11aac2683053a1345da}.
```

The final run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T27 target module;
- rebuilding and checking the WD-T26 dependency;
- unfinished-proof/project-axiom rejection.

The repair passes affected only finite-sum normalization, Bornology scope, and
triangle-inequality elaboration.  No theorem statement or mathematical
hypothesis was weakened.

## WD-T28 criterion-layer certificate evidence

Stable ID remains:

```math
\boxed{
\text{WD-T28: LEAN-IN-PROGRESS}.
}
```

The Hilbert--Schmidt **criterion layer** is kernel-checked.

Formal declarations include:

- WeilDefect.ZetaShellIndex;
- WeilDefect.ZetaZeroShellCountData;
- WeilDefect.NativeProblemOneResolventData;
- WeilDefect.NativeHilbertSchmidtCriterion;
- WeilDefect.NativeTraceClassCovarianceCriterion;
- WeilDefect.nativeShellEnergy;
- WeilDefect.summable_shifted_rpow_neg_three_halves;
- WeilDefect.nativeShellEnergy_le_three_halves;
- WeilDefect.nativeShellEnergy_summable;
- WeilDefect.wd_t28_native_basis_square_summable;
- WeilDefect.wd_t28_native_problem_one_hilbert_schmidt.

The pinned Mathlib version does not expose a native Hilbert--Schmidt or
trace-class operator type.  Accordingly WD-T28 is represented at the standard
$\ell^2$-basis criterion level:

```math
\sum_\gamma
\|E_t e_\gamma\|_{H^{-1}_L}^2
<
\infty.
```

The zero-count input is explicit.  The Titchmarsh
$O(\log T)$ unit-shell estimate is packaged through its elementary weaker
consequence

```math
\#\Gamma_n
\ll
(n+1)^{1/2},
```

which is sufficient for summability.

The native column estimate is also explicit:

```math
\|E_t e_\gamma\|_{H^{-1}_L}^2
\le
A(n+1)^{-2}
```

for a coordinate in unit shell $n$.

Lean then verifies internally that one shell contributes at most

```math
AC(n+1)^{-3/2},
```

and proves summability via the $p$-series with exponent $3/2$.
The Sigma-type shell decomposition then yields summability over all zero
coordinates.

At the criterion level Lean therefore verifies both:

```math
\text{Hilbert--Schmidt basis-square summability},
```

and the corresponding covariance trace-sum criterion.

Dedicated criterion CI built:

```math
\texttt{WeilDefect.NativeHilbertSchmidt}.
```

Certificate run:

```math
\boxed{\texttt{36100254156}}
```

at repository head:

```math
\boxed{\texttt{b919ea890dfb83236cdb6ec0de625b5e59fd9e24}}.
```

The checked theorem source blob is:

```math
\texttt{d94c9020fdd9c3acadf0e143735b21bb12bd8598}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of the WD-T28 criterion module;
- rebuilding the finite Problem-1 dependencies;
- unfinished-proof/project-axiom rejection.

### WD-T28 resolvent-realization certificate

The previously abstract native-column premise has now been discharged by an
explicit compact-window Dirichlet construction.

Additional formal declarations include:

- WeilDefect.problemOneFreq;
- WeilDefect.problemOneGreenDenom;
- WeilDefect.problemOneGreenQ;
- WeilDefect.dirichletRightReal;
- WeilDefect.dirichletLeftReal;
- WeilDefect.dirichletRightBasis;
- WeilDefect.dirichletLeftBasis;
- WeilDefect.problemOneL_dirichletRightBasis;
- WeilDefect.problemOneL_dirichletLeftBasis;
- WeilDefect.problemOneGreenQ_shell_bound;
- WeilDefect.norm_problemOne_source_le;
- WeilDefect.dirichletProblemOneColumn;
- WeilDefect.dirichletProblemOneColumn_pos;
- WeilDefect.dirichletProblemOneColumn_neg;
- WeilDefect.problemOneL_dirichletProblemOneColumn;
- WeilDefect.norm_dirichletProblemOneColumn_le;
- WeilDefect.problemOneGreenPairing;
- WeilDefect.problemOneColumnEnergySq;
- WeilDefect.problemOneColumnEnergySq_le;
- WeilDefect.ActualProblemOneShellData;
- WeilDefect.actualProblemOneEnergySq;
- WeilDefect.nativeProblemOneResolventData_of_actual;
- WeilDefect.wd_t28_native_problem_one_hilbert_schmidt_actual.

For fixed $t>0$, the explicit Green column is

```math
F_\gamma(x)
=
q_\gamma e^{-i\gamma x}
-q_\gamma e^{-i\gamma t}h_+(x)
-q_\gamma e^{i\gamma t}h_-(x),
```

where

```math
q_\gamma
=
\left(\frac14+\gamma^2\right)^{-1}
```

and $h_\pm$ are the canonical hyperbolic-sine Dirichlet interpolation
functions.

Lean certifies

```math
F_\gamma(\pm t)=0
```

and

```math
\left(-\partial_x^2+\frac14\right)F_\gamma
=
e^{-i\gamma x}.
```

Inside the fixed zeta strip

```math
|\Im\gamma|\le\frac12,
```

Lean proves the compact-window source and boundary-correction bounds and the
shell-height reciprocal estimate

```math
\|q_\gamma\|
\le
(n+1)^{-2}
```

whenever the coordinate is assigned to a shell satisfying

```math
n+1\le |\Re\gamma|.
```

Consequently the Green pairing obeys the explicit bound

```math
\left|
\int_{-t}^{t}
\overline{e^{-i\gamma x}}\,F_\gamma(x)\,dx
\right|
\le
6t\,e^t\,\|q_\gamma\|,
```

which supplies the inverse-square column-energy estimate consumed by the
already-certified shell-summability theorem.

The direct resolvent target passed in:

```math
\boxed{\texttt{36106100832}}
```

at repository head:

```math
\boxed{\texttt{b4f66285b0060afce5af47310e98cbb5fef41cc9}}.
```

The checked resolvent source blob is:

```math
\texttt{2564a66892ed3c623249d621d54a556bcec8857b}.
```

This run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of $\texttt{WeilDefect.DirichletResolvent}$;
- rebuilding the WD-T28 criterion dependencies;
- unfinished-proof/project-axiom rejection.

The former abstract premise

```math
\texttt{NativeProblemOneResolventData}
```

is therefore internally realized for the explicit shell data by

```math
\texttt{nativeProblemOneResolventData_of_actual}.
```

### Remaining WD-T28 semantic obligation

WD-T28 remains

```math
\boxed{\text{LEAN-IN-PROGRESS}}
```

for one narrower reason.

The current scalar

```math
\texttt{problemOneColumnEnergySq}
```

is defined as the norm of the Green pairing.  The mathematical native
$H^{-1}_L$ statement additionally identifies the pairing itself with the
positive Dirichlet energy:

```math
\boxed{
\langle f_\gamma,Gf_\gamma\rangle
=
\int_{-t}^{t}
\left(
|F_\gamma'(x)|^2
+
\frac14|F_\gamma(x)|^2
\right)\,dx
\ge0.
}
```

The next kernel obligation is therefore no longer the resolvent estimate.
It is only this integration-by-parts positivity/energy identification.

Cursor at this checkpoint:

```math
\boxed{
\texttt{WD-T28 / ENERGY IDENTIFICATION — GREEN PAIRING = POSITIVE }H^{-1}_L\texttt{ ENERGY}
}
```


## WD-T28 final certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T28: LEAN-CERTIFIED}.
}
```

The remaining semantic obligation was the native Green-pairing / positive
Dirichlet-energy identification. Lean now certifies the chain

```math
\langle f_\gamma,Gf_\gamma\rangle
=
\int_{-t}^{t}
\left(
|F_\gamma'(x)|^2+\frac14|F_\gamma(x)|^2
\right)\,dx
\ge 0,
```

together with the real/complex cast and the identification of
`problemOneColumnEnergySq` with the positive Dirichlet energy.

Final declarations include:

- WeilDefect.problemOneDirichletEnergy;
- WeilDefect.problemOneDirichletEnergyComplex;
- WeilDefect.dirichlet_second_derivative_pairing;
- WeilDefect.problemOneDirichletEnergyComplex_eq_ofReal;
- WeilDefect.problemOneDirichletEnergy_nonneg;
- WeilDefect.problemOneGreenPairing_eq_dirichletEnergyComplex;
- WeilDefect.problemOneGreenPairing_eq_dirichletEnergy;
- WeilDefect.problemOneColumnEnergySq_eq_dirichletEnergy;
- WeilDefect.actualProblemOneEnergySq_eq_dirichletEnergy;
- WeilDefect.wd_t28_actual_dirichlet_energy_summable.

The final cast repair was proof-engineering only: after `push_cast`, the goal
was reflexive and is closed by `rfl`. No mathematical statement or hypothesis
was weakened.

The final WD-T28 dependency was rebuilt successfully as part of the WD-T29
certificate run:

```math
\boxed{\texttt{36149246351}}
```

at repository head:

```math
\boxed{\texttt{766ddd2297e5d884a532e09379b7c2e6ad82db86}}.
```

The final Dirichlet-energy source blob is:

```math
\texttt{68c53704d15038b6365a9835d79b7c6d4a3d548b}.
```


## WD-T29 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T29: LEAN-CERTIFIED}.
}
```

Formal declarations:

- WeilDefect.wd_t29_finite_head_approximation;
- WeilDefect.wd_t29_quantitative_finite_head_approximation.

Lean formalizes the exact necessary-condition mechanism. If

```math
y=S_{\le G}x_{\le G}+S_{>G}x_{>G},
\qquad
\|x_{>G}\|\le 1,
```

then

```math
\operatorname{dist}
\bigl(y,\operatorname{Ran}S_{\le G}\bigr)
\le
\|S_{>G}\|.
```

Any quantitative operator-tail bound
$\|S_{>G}\|\le\varepsilon_G$ therefore transfers immediately to the
same finite-head approximation rate.

Certificate run:

```math
\boxed{\texttt{36149246351}}
```

at repository head:

```math
\boxed{\texttt{766ddd2297e5d884a532e09379b7c2e6ad82db86}}.
```

The WD-T29 source blob is:

```math
\texttt{1f0222e44d03a9b23d0ae3900c3f884893f2eaa1}.
```

The run passed:

- pinned dependency resolution;
- mathlib cache retrieval;
- direct Lake build of `WeilDefect.FiniteHeadApproximation`;
- rebuilding the WD-T28 Dirichlet-energy dependency;
- unfinished-proof/project-axiom rejection.

WD-T30 is already independently Lean-certified.

## WD-T31 analytic tail-kernel subpass

The analytic summation core of WD-T31 is now kernel-checked. Lean certifies the
nonnegative antitone kernel

```math
k(x)=\frac{1+\log x}{x^2},
```

its exact improper integral

```math
\int_R^\infty k(x)\,dx
=
\frac{\log R+2}{R},
```

and the discrete shifted-tail estimate

```math
\sum_{n\ge R+1} k(n)
\le
\frac{\log R+2}{R}.
```

Formal declarations include:

- WeilDefect.logarithmicTailKernel;
- WeilDefect.logarithmicTailKernel_nonneg;
- WeilDefect.logarithmicTailKernel_antitoneOn;
- WeilDefect.logarithmicTailKernel_integrableOn_Ioi;
- WeilDefect.integral_logarithmicTailKernel_Ioi;
- WeilDefect.logarithmicTail_tsum_le.

This subpass passed pinned CI in:

```math
\boxed{\texttt{36155524899}}
```

at repository head:

```math
\boxed{\texttt{ddb689c21d9278c05dc792f08b44d7d7e6feed01}}.
```

The checked source blob is:

```math
\texttt{439db969240a2534e15709c9bf27c998421acb12}.
```

The shell aggregation and WD-T27 bridge are now complete.

## WD-T31 final certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T31: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Additional declarations include:

- WeilDefect.FarShellIndex;
- WeilDefect.ZetaLogShellCountData;
- WeilDefect.FarShellResponseData;
- WeilDefect.farShellResponse;
- WeilDefect.logarithmicTailKernel_summable_nat;
- WeilDefect.logarithmicTailKernel_shift_summable;
- WeilDefect.farShellResponse_norm_le_logarithmic_kernel;
- WeilDefect.wd_t31_shell_aggregation;
- WeilDefect.zeroMomentResponseConstant;
- WeilDefect.rationalResponse_zero_moment_norm_le_inverse_square;
- WeilDefect.zeroMomentShellTerm;
- WeilDefect.farShellResponseData_of_zero_moment;
- WeilDefect.wd_t31_zero_moment_zero_count_far_tail.

The final theorem consumes the selected zero-moment law directly. WD-T27 gives
the pointwise inverse-square response bound on each sufficiently far
complementary zero; a uniformly bounded multiplier preserves that rate; the
imported logarithmic unit-shell zero-count premise supplies the shell
multiplicity bound. Lean then proves

```math
\left\|
\sum_{n\ge R}\mathcal S_n
\right\|
\le
AC\,\frac{\log R+2}{R},
```

with the constants explicitly assembled from the multiplier bound, selected
residue moments, and shell-count constant.

The imported part is exactly the source-pinned logarithmic unit-shell zero
count represented by $\texttt{ZetaLogShellCountData}$. It is not introduced
as a project axiom.

The generic shell aggregation first passed in CI run:

```math
\boxed{\texttt{36159321679}}.
```

The final zero-moment bridge and full WD-T31 target passed in:

```math
\boxed{\texttt{36160324368}}
```

at repository head:

```math
\boxed{\texttt{2e36689aba0b8825c6ed553ca04849fa6fd3f511}}.
```

The final theorem source blob is:

```math
\texttt{d0461bbf09d2928f43807abc8e347c36883f231b}.
```

The final run passed pinned dependency resolution, mathlib cache retrieval,
the dedicated $\texttt{WeilDefect.Arithmetic.FarTail}$ build, and
unfinished-proof/project-axiom rejection.

WD-T31 is therefore closed.

## WD-T32 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T32: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.completedResponseLift;
- WeilDefect.iteratedDeriv_centered_power;
- WeilDefect.iteratedDeriv_centered_power_mul;
- WeilDefect.wd_t32_complementary_next_jet_identity;
- WeilDefect.nearComplementaryResponse;
- WeilDefect.weightedNearNextJetField;
- WeilDefect.wd_t32_weighted_near_next_jet_representation.

For a local multiplicity factorization

```math
\Xi(z)=(z-\mu)^m g(z),
\qquad g(\mu)\ne0,
```

Lean proves directly from the pinned iterated-derivative shift and Leibniz
rules that

```math
\Xi^{(m)}(\mu)=m!\,g(\mu),
```

and, for the completed lift $H=\Xi R$,

```math
H^{(m)}(\mu)=m!\,g(\mu)R(\mu).
```

The nonzero local factor therefore gives the exact quotient identity

```math
R(\mu)
=
\frac{H^{(m)}(\mu)}{\Xi^{(m)}(\mu)}.
```

Lean then substitutes this identity termwise over an arbitrary finite
complementary packet, certifying the ZW2-T4 weighted near next-jet
representation.

No project axiom or imported theorem premise is consumed by WD-T32. The local
factorization, smoothness, and nonvanishing conditions appear explicitly as
the mathematical hypotheses of the theorem.

Dedicated theorem CI passed in:

```math
\boxed{\texttt{36167018245}}
```

at repository head:

```math
\boxed{\texttt{c8d35dfef95e7e9989ca07faa5dbd531332c22ff}}.
```

The certified theorem source blob is:

```math
\texttt{df0d86d7c86f7b6ae8ae142f6a5018bacb65a0b6}.
```

The run passed pinned dependency resolution, mathlib cache retrieval, direct
Lake build of $\texttt{WeilDefect.Arithmetic.NextJet}$, and
unfinished-proof/project-axiom rejection.

WD-T33 is already independently Lean-certified.

## WD-T34 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T34: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.activePrimePowers;
- WeilDefect.wd_t34_active_prime_powers_finite;
- WeilDefect.activePrimePowerFinset;
- WeilDefect.mem_activePrimePowerFinset;
- WeilDefect.activePrimeTranslationShifts;
- WeilDefect.wd_t34_active_prime_translation_shifts_finite;
- WeilDefect.translateBy;
- WeilDefect.symmetricPrimeTranslation;
- WeilDefect.compactPrimeTranslationSum;
- WeilDefect.wd_t34_finite_prime_power_translations;
- WeilDefect.primePowerThreshold;
- WeilDefect.primePowerThreshold_subsingleton.

Lean first certifies directly that, for every fixed real support radius
$c$, the compact-window threshold condition

```math
\log n<2c
```

selects only finitely many natural prime powers.  The proof exponentiates the
support inequality and places every active index in one finite natural
interval.

The corresponding physical arithmetic shifts

```math
\{\pm\log n:
n\text{ prime-power active at }c\}
```

are therefore a finite set.  The module packages the arithmetic contribution
as an actual finite sum of scalar-weighted symmetric translations.

The exact threshold set

```math
\{n:
n\text{ prime power},\ \log n=2c\}
```

is also certified to be subsingleton, so a fixed support boundary can contain
at most one natural prime-power threshold event.

The identification of this threshold set as the prime part of the
compact-window Weil formula remains the source-pinned specialization recorded
in the theorem ledger; no external theorem is introduced as a project axiom
inside the Lean module.

The core theorem build first passed in:

```math
\boxed{\texttt{36168682600}}.
```

After correcting the finite operator helper so its arithmetic coefficient acts
by scalar multiplication, the final certificate run passed in:

```math
\boxed{\texttt{36168986069}}
```

at repository head:

```math
\boxed{\texttt{3bb1f99e923b0b80729144bb2eb8e374c7f15ade}}.
```

The final WD-T34 source blob is:

```math
\texttt{ed91ac08a670ae1405cb994b05d06065f5452b5b}.
```

The run passed pinned dependency resolution, mathlib cache retrieval, direct
Lake build of $\texttt{WeilDefect.Arithmetic.PrimeSupport}$, and
unfinished-proof/project-axiom rejection.

WD-T34 is therefore closed.

## WD-T35 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T35: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations include:

- WeilDefect.logarithmicFourierWeight;
- WeilDefect.one_le_logarithmicFourierWeight;
- WeilDefect.logarithmicFourierEnergy;
- WeilDefect.spectralMass;
- WeilDefect.shiftedCompactWeilForm;
- WeilDefect.wd_t35_shifted_form_logarithmic_order;
- WeilDefect.wd_t35_compact_weil_logarithmic_form_order.

The canonical Fourier weight is represented exactly as

```math
w(t)=\log(e+|t|),
```

and Lean certifies $w(t)\ge1$ everywhere.

For a nonnegative spectral density, the imported compact-window specialization
is isolated into explicit hypotheses:

1. the shifted symbol comparison
   ```math
   a\,w(t)\le \Psi_c(t)+C\le b\,w(t);
   ```
2. the shifted geometric-form identity;
3. a nonnegative pole/evaluation contribution bounded by
   $K\|F\|_2^2$.

The symbol comparison is the source-pinned consequence of the digamma
asymptotic together with WD-T34 finite prime support. The geometric identity
is the source-pinned compact-window Weil formula. Neither is installed as a
project axiom.

Lean proves internally that spectral mass is bounded by logarithmic Fourier
energy, absorbs the pole term, and obtains the two-sided estimate

```math
a
\int_{\mathbb R}
\log(e+|t|)\,|F(t)|^2\,dt
\le
Q_c(f)+C\|f\|_2^2
```

and

```math
Q_c(f)+C\|f\|_2^2
\le
(b+K)
\int_{\mathbb R}
\log(e+|t|)\,|F(t)|^2\,dt.
```

All integration is explicitly against Lebesgue volume; no ambient measure
instance is left implicit.

Dedicated theorem CI passed in:

```math
\boxed{\texttt{36171526106}}
```

at repository head:

```math
\boxed{\texttt{37b89dd60cfe1963abc58c04c6113319fea383c1}}.
```

The certified WD-T35 source blob is:

```math
\texttt{ae932d4f3f7e4d6d06dbd778a5708927172238dc}.
```

The final run passed pinned dependency resolution, mathlib cache retrieval,
direct Lake build of $\texttt{WeilDefect.Arithmetic.LogarithmicForm}$,
rebuilding WD-T34, and unfinished-proof/project-axiom rejection.

WD-T35 is therefore closed.

## WD-T36 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T36: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations include:

- WeilDefect.positiveSobolevFrequencyWeight;
- WeilDefect.logarithmicFourierWeight_isBigO_log;
- WeilDefect.logarithmicFourierWeight_isLittleO_positiveSobolev;
- WeilDefect.positiveSobolevFrequencyWeight_not_isBigO_logarithmic;
- WeilDefect.wd_t36_no_uniform_positive_sobolev_coercivity_of_witness;
- WeilDefect.wd_t36_no_positive_sobolev_bootstrap;
- WeilDefect.finitePrimeTrigCorrection;
- WeilDefect.finitePrimeTrigBound;
- WeilDefect.finitePrimeTrigBound_nonneg;
- WeilDefect.abs_finitePrimeTrigCorrection_le;
- WeilDefect.finitePrimeTrigCorrection_isBigO_logarithmic;
- WeilDefect.logarithmicPlusFinitePrimeCorrection_isBigO;
- WeilDefect.wd_t36_finite_prime_translations_add_no_smoothing.

For every $\varepsilon>0$, Lean certifies the asymptotic separation

```math
\log(e+|N|)
=
o\!\left(N^{2\varepsilon}\right),
```

in the precise Landau sense needed for the squared positive-Sobolev frequency
weight. Consequently,

```math
N^{2\varepsilon}
\not=
O\!\left(\log(e+|N|)\right).
```

The witness-transfer theorem then proves that any fixed-support oscillatory
family satisfying the canonical growth inputs

```math
\text{shifted Weil-form energy}
=
O(\log(e+N))
```

and

```math
N^{2\varepsilon}
=
O(\text{Sobolev energy})
```

cannot obey a uniform positive-Sobolev coercive estimate.

The concrete compact-support construction
$f_N(x)=\phi(x)\cos(Nx)$, together with its Fourier concentration
asymptotics, is not separately rebuilt in the current Lean corpus. Those
standard witness asymptotics are therefore the explicit premise represented
by the transfer theorem, which is why WD-T36 receives the
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE label rather than an unconditional
physical-space certification.

The finite-arithmetic clause is kernel-checked internally. For every fixed
WD-T34 active prime set and coefficient family, Lean defines the finite cosine
correction

```math
P_c(t)
=
\sum_{n\in S_c}
a_n\cos(t\log n)
```

and proves

```math
|P_c(t)|
\le
\sum_{n\in S_c}|a_n|.
```

Hence

```math
P_c
=
O\!\left(\log(e+|t|)\right)
```

and even

```math
\log(e+|t|)+P_c(t)
=
O\!\left(\log(e+|t|)\right).
```

Thus the finitely many prime translations do not raise the principal order and
cannot repair the positive-Sobolev mismatch.

The core asymptotic obstruction first passed in CI run:

```math
\boxed{\texttt{36176761127}}.
```

The completed WD-T36 target, including the finite-prime order-zero clause,
passed in:

```math
\boxed{\texttt{36177620078}}
```

at repository head:

```math
\boxed{\texttt{ad575eded95f8b50e05aca512611f4f6db9cc190}}.
```

The final WD-T36 source blob is:

```math
\texttt{57153cd26db57d683b5603913e9c1ace42ca8035}.
```

The final run passed pinned dependency resolution, mathlib cache retrieval,
direct Lake build of $\texttt{WeilDefect.Arithmetic.NoSobolevBootstrap}$,
the WD-T34/WD-T35 dependencies, and unfinished-proof/project-axiom rejection.

WD-T36 is therefore closed.

## WD-T37 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T37: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations include:

- WeilDefect.SelectedSourceData;
- WeilDefect.wd_t37_selected_source_zero_moment_of_wd_t26;
- WeilDefect.wd_t37_selected_source_nonzero_of_wd_t26;
- WeilDefect.wd_t37_p3_n1_endpoint_ray;
- WeilDefect.wd_t37_p3_n2_normalized_representative_blowup;
- WeilDefect.wd_t37_p3_n3_normalized_full_negativity;
- WeilDefect.wd_t37_p3_n4_zero_moment_source_far_decay;
- WeilDefect.wd_t37_p3_n5_far_localization;
- WeilDefect.wd_t37_p3_n6_weighted_next_jet_morphology;
- WeilDefect.wd_t37_p3_n7_no_adaptive_scalar_bypass;
- WeilDefect.NegativeArithmeticMorphology;
- WeilDefect.NegativeDefectMorphology;
- WeilDefect.wd_t37_fixed_packet_persistent_negative_morphology.

Lean now packages the complete conditional negative morphology from persistent
selected negativity through endpoint persistence, normalized representative
blow-up, full-Weil negativity, selected raw-residue formation, inverse-square
far decay, quantitative far localization, weighted completed-Xi next-jet
morphology, and no adaptive scalar bypass.

The final residue-custody repair is load-bearing. SelectedSourceData no longer
stores a free zero-moment proof. The composite constructor instead receives
the negative-pair coefficient specialization and requires the exact identity

```math
\operatorname{List.ofFn}(v)
=
\operatorname{rawResiduesOfNegativePairs}(x).
```

Lean derives both zero moment and source nontriviality from the certified
WD-T26 raw-residue lemmas before WD-T27 or WD-T31 can be applied. The output
package retains this equality and the nonzero pair-coefficient witness, so the
source cannot be replaced by an unrelated zero-moment look-alike.

The only imported analytic-number-theory premise inherited by the arithmetic
localization is the logarithmic unit-shell zero-count interface
$\texttt{ZetaLogShellCountData}$ already isolated in WD-T31. No imported
result is installed as a project axiom.

The composite intentionally contains no actual-zeta exclusion field. Its exact
formal stop remains

```math
\boxed{\texttt{AZ-NEXTJET-LOC}}.
```

The data-valued endpoint-package repair first passed pinned CI in:

```math
\boxed{\texttt{36182014916}}.
```

The completed residue-custody target passed in:

```math
\boxed{\texttt{36182444478}}
```

at repository head:

```math
\boxed{\texttt{144bef98b0f66dd7f6f82eb523c06c8eec85479e}}.
```

The certified WD-T37 source blob is:

```math
\texttt{ff0bae40f6aba4c04a8d3fd75a8fe309f8ea79ae}.
```

The final run passed pinned dependency resolution, mathlib cache retrieval,
direct Lake build of $\texttt{WeilDefect.Morphology.Negative}$, and
unfinished-proof/project-axiom rejection.

WD-T37 is therefore closed.

## WD-T38 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T38: LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

Formal declarations include:

- WeilDefect.wd_t38_p3_u1_fixed_packet_critical_dichotomy;
- WeilDefect.wd_t38_attained_neutral_selected_coordinate_nonzero;
- WeilDefect.rightLimitPrimePowers;
- WeilDefect.wd_t38_p3_u3_right_limit_prime_decomposition;
- WeilDefect.wd_t38_p3_u3_right_limit_prime_support_finite;
- WeilDefect.wd_t38_p3_u4_logarithmic_order_neutral_carrier;
- WeilDefect.wd_t38_p3_u5_no_free_positive_sobolev_control;
- WeilDefect.wd_t38_p3_u5_finite_prime_translations_no_smoothing;
- WeilDefect.wd_t38_p3_u6_global_cancellation_not_termwise;
- WeilDefect.neutralNegativeSynthesis;
- WeilDefect.neutralWeilOperator;
- WeilDefect.wd_t38_p3_u2_negative_adjoint_identity;
- WeilDefect.wd_t38_p3_u2_physical_neutral_null_mode;
- WeilDefect.NeutralNullExtensionInterface;
- WeilDefect.NeutralNullExtensionInterface.persistenceGoal;
- WeilDefect.wd_t38_p3_u7_neutral_null_extension_reduction;
- WeilDefect.NeutralArithmeticMorphology;
- WeilDefect.wd_t38_neutral_arithmetic_morphology;
- WeilDefect.NeutralDefectMorphology;
- WeilDefect.wd_t38_attained_unit_gain_neutral_morphology.

The composite preserves the audited attained-neutral branch distinction from
WD-T17. In particular, the retained selected coordinate is explicitly proved
nonzero from the neutral branch equations rather than left as an implicit
custody fact.

For the finite-exception realization, Lean proves

```math
C^\ast C u=u,\qquad Cu=P^\ast k,\qquad N=-PC
```

implies

```math
N^\ast k=-u
```

and therefore

```math
(PP^\ast-NN^\ast)k=0,
\qquad k\ne0.
```

The arithmetic continuation is threshold-aware. Lean defines the strict
right-limit prime support by

```math
\{n:\operatorname{IsPrimePow}(n),\ \log n\le 2c\}
```

and proves it is exactly the endpoint strict-active set
$\log n<2c$ union the equality-threshold set. The latter is subsingleton, so
the strict-right correction is finite and contains at most one natural prime
power.

The logarithmic-order and no-bootstrap clauses are transferred from WD-T35 and
WD-T36 with their hypotheses preserved. Consequently WD-T38 inherits the
source-pinned compact-window formula/symbol-comparison premise from WD-T35,
which is why the composite receives
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE rather than an unconditional label.

The global-cancellation scope theorem remains purely logical: a zero total
cancellation does not imply termwise vanishing. No prime, pole, or
archimedean term is separately forced to vanish.

Most importantly, the null-extension endpoint is represented as a typed open
interface. It records:

- the nonzero zero-extended fixed vector;
- distinct endpoint and strict-right operators;
- the endpoint interior null equation;
- equality of endpoint/right-limit operators only under the explicit
  no-threshold carrier-identification premise;
- finite right-limit prime support and subsingleton threshold support.

The unresolved statement

```math
\texttt{NeutralNullExtensionInterface.persistenceGoal}
```

is deliberately a proposition attached to the returned data, not a field
proved by WD-T38. Thus no support-rigidity or unique-continuation theorem is
silently imported upstream.

The assembled composite first passed pinned CI in:

```math
\boxed{\texttt{36187216321}}
```

at repository head:

```math
\boxed{\texttt{ec71653408d8254844039f851cab429d5c32ebb9}}.
```

The final selected-coordinate custody refinement passed in:

```math
\boxed{\texttt{36187705896}}
```

at repository head:

```math
\boxed{\texttt{1d09fa5c85b1a5970376db5adcda0c1b0872da75}}.
```

The certified WD-T38 source blob is:

```math
\texttt{2f6f05486f61fd8be18d444f9ef1e2bde5ae1abd}.
```

The final run passed pinned dependency resolution, mathlib cache retrieval,
direct Lake build of $\texttt{WeilDefect.Morphology.Neutral}$, and
unfinished-proof/project-axiom rejection.

WD-T38 is therefore closed.

## WD-T39 certificate evidence

Stable ID:

```math
\boxed{
\text{WD-T39: LEAN-CERTIFIED}.
}
```

Formal declarations include:

- WeilDefect.FullNegativeSpace;
- WeilDefect.fullNegativeCoeff;
- WeilDefect.fullCoeff;
- WeilDefect.fullJValue;
- WeilDefect.wd_t39_p3_b1_anchored_mass;
- WeilDefect.FullCoordinateExhaustion;
- WeilDefect.wd_t39_p3_b2_full_coordinate_escape_weak_zero;
- WeilDefect.wd_t39_p3_b3_fixed_packet_custody;
- WeilDefect.normEscapeSubsequence;
- WeilDefect.wd_t39_p3_b4_norm_escape_of_unbounded;
- WeilDefect.BoundedBackgroundRegime;
- WeilDefect.wd_t39_p3_b4_bounded_background_dichotomy;
- WeilDefect.BackgroundCompactnessRegime;
- WeilDefect.wd_t39_p3_b4_background_compactness_trichotomy;
- WeilDefect.wd_t39_p3_b5_fixed_selected_ray_stability;
- WeilDefect.wd_t39_p3_b6_fixed_full_divisor_negative_weak_limit;
- WeilDefect.wd_t39_p3_b7_finite_shadow_separation;
- WeilDefect.NoncompactDefectMorphology;
- WeilDefect.wd_t39_noncompact_background_morphology.

The full-carrier escape theorem uses a self-adjoint finite-coordinate exhaustion
converging strongly to the identity. If every fixed full-coordinate block
vanishes on a uniformly bounded sequence, Lean proves that the entire
coefficient sequence converges weakly to zero. The exhaustion is explicitly
on the full carrier, preserving composite correction B-1.

For one fixed finite selected packet, any frequently retained positive amount
of selected negative norm admits a strongly convergent subsequence with
nonzero selected limit. Thus the moving/full-carrier escape species is kept
separate from fixed-packet custody.

For the unselected background, Lean certifies the complete subsequential
classification:

```math
\boxed{
\text{norm escape}
\;\vee\;
\text{bounded weak/tail escape}
\;\vee\;
\text{strong background compactness}.
}
```

The norm-escape arm is constructed explicitly from failure of every uniform
norm bound. In the bounded case, weak compactness plus a convergent norm-square
subsequence gives either positive weak norm loss or, at equality, strong
convergence.

The fixed selected negative ray remains nonzero and strictly negative after
any bounded background weak limit. In the strong-background regime the entire
negative sector converges strongly, while the positive coordinate is retained
only weakly unless an additional positive-coordinate compactness hypothesis is
supplied. This preserves composite correction B-2.

Finite positive shadows preserve the algebraic selected negative margin but
retain a separate graph-admissibility condition, so no background compactness
is inferred from a finite positive projection.

WD-T39 introduces no imported analytic-number-theory premise and no new
RH-facing interface. The assembled universal morphology packages the audited
branch theorems separately rather than asserting that one sequence
simultaneously realizes incompatible compactness species.

The complete core/trichotomy checkpoint passed pinned CI in:

```math
\boxed{\texttt{36190887350}}.
```

The final assembled WD-T39 target passed in:

```math
\boxed{\texttt{36191325215}}
```

at repository head:

```math
\boxed{\texttt{9f883eef5ec8cee9c8fd092576a5e0fff3326872}}.
```

The certified WD-T39 source blob is:

```math
\texttt{f5b029598b0b80c5fc8ef292a858bb63d9c3a076}.
```

The final run passed pinned dependency resolution, mathlib cache retrieval,
direct Lake build of $\texttt{WeilDefect.Morphology.Noncompact}$, and
unfinished-proof/project-axiom rejection.

WD-T39 is therefore closed. The next unfinished stable formalization cursor is:

```math
\boxed{
\texttt{WD-X02 / CRITICAL SCREENING WITHOUT AN ATTAINED NEUTRAL VECTOR}
}
```


## WD-X02 certificate evidence

Stable ID:

```math
\boxed{\text{WD-X02: LEAN-CERTIFIED}.}
```

Lean certifies an explicit diagonal $\ell^2(\mathbb N;\mathbb C)$ realization
of the same critical nonattainment geometry as the canonical
$L^2(0,1)$ multiplication-by-$t$ witness in the audit document.

The coordinate gains are

```math
r_n=1-\frac1{n+2},
\qquad
0\le r_n<1,
\qquad
r_n\to1.
```

The induced coordinatewise operator $X$ satisfies

```math
\boxed{\|X\|=1}
```

while every nonzero vector obeys

```math
\boxed{\|Xf\|<\|f\|}.
```

Thus the critical operator norm is not attained by any nonzero vector.
At the same time the standard basis vectors are unit vectors and satisfy

```math
\|Xe_n\|=r_n\to1,
```

so the associated critical defect can be made arbitrarily small without an
actual neutral vector.

This is exactly the sharpness role required by WD-X02:

```math
\|X\|=1
\not\Rightarrow
\text{norm attainment / actual neutrality}
```

in infinite dimension.

Certificate run:

```math
\boxed{\texttt{36193606439}}
```

at repository head:

```math
\boxed{\texttt{e29b843f20125f4a43152459b9c77a4bb60f8f1b}}.
```

The certified source blob is:

```math
\texttt{eb98e663282551b1dfede47f148132d93051d079}.
```

The run passed pinned dependency resolution, direct Lake build of
$\texttt{WeilDefect.Examples.CriticalNonattainment}$, and the
unfinished-proof/project-axiom rejection gate.

WD-X02 is therefore closed. The next unfinished stable example cursor is:

```math
\boxed{\texttt{WD-X05 / MOVING SECTORS CAN LOSE EVERY PERSISTENT RAY}}
```


## WD-X05 certificate evidence

Stable ID:

```math
\boxed{\text{WD-X05: LEAN-CERTIFIED}.}
```

Lean certifies an explicit moving-sector witness on
$\ell^2(\mathbb N)\oplus\ell^2(\mathbb N)$. For

```math
\delta_n=\frac1{n+2},
```

the positive and negative amplitudes are chosen with squared norms

```math
\|a_n\|^2=\frac{1-\delta_n}{2},
\qquad
\|u_n\|^2=\frac{1+\delta_n}{2}.
```

Hence every coefficient vector is normalized,

```math
\boxed{\|y_n\|=1},
```

while its Krein signature is exactly

```math
\boxed{[y_n,y_n]_J=-\delta_n<0},
\qquad
[y_n,y_n]_J\to0.
```

The moving-sector custody is encoded by nested coordinate-tail predicates
$\texttt{wdX05Tail}\,N$. Lean proves

```math
N\le k \Longrightarrow y_k\in \texttt{wdX05Tail}\,N
```

and, crucially,

```math
\boxed{
\left(\forall N,\ y\in\texttt{wdX05Tail}\,N\right)
\Longrightarrow y=0.
}
```

Thus stagewise finite-dimensional negative directions can move through
infinitely many coordinates while the total nested intersection loses every
nonzero persistent ray. This is the exact sharpness role of WD-X05 for the
fixed-sector hypothesis in WD-T16/WD-T17 and for the moving/full-coordinate
escape side of WD-T39.

Certificate run:

```math
\boxed{\texttt{36196053927}}
```

at theorem head:

```math
\boxed{\texttt{a1fe7296738e48065c1e393723bf22b251c9728e}}.
```

Certified source blob:

```math
\texttt{e51c450d99e35d59e56ffc5803dc48ad9654302b}.
```

The run passed pinned dependency resolution, direct Lake build of
$\texttt{WeilDefect.Examples.MovingSectors}$, and the
unfinished-proof/project-axiom rejection gate.

WD-X05 is therefore closed. The next unfinished stable example cursor is:

```math
\boxed{
\texttt{WD-X06 / POSITIVE-COORDINATE MASS LOSS STRENGTHENS CRITICALITY TO NEGATIVITY}
}
```


## WD-X06 certificate evidence

Stable ID:

```math
\boxed{\text{WD-X06: LEAN-CERTIFIED}.}
```

Lean certifies the critical weak-fall-through witness on
$\ell^2(\mathbb N)\oplus\mathbb C$.

For

```math
y_n=\left(\frac1{\sqrt2}e_n,\frac1{\sqrt2}\right),
```

the formal witness satisfies

```math
\boxed{\|y_n\|=1}
\qquad
\boxed{[y_n,y_n]_J=0}
```

for every $n$. Lean also proves the standard-basis weak convergence

```math
e_n\rightharpoonup0
```

directly from the $\ell^2$ coordinate square-summability identity. Therefore

```math
y_n\rightharpoonup
y=\left(0,\frac1{\sqrt2}\right).
```

The limit has exact signature

```math
\boxed{[y,y]_J=-\frac12<0}.
```

Thus WD-X06 formally realizes the negative-fall-through branch of WD-T17:
positive-coordinate mass can disappear under weak convergence while the
selected negative coordinate remains fixed, strengthening criticality to
strict negativity.

Certificate run:

```math
\boxed{\texttt{36196899652}}
```

at theorem head:

```math
\boxed{\texttt{39353ab8185c99959481c334aa67d42c88e8f859}}.
```

Certified source blob:

```math
\texttt{746b1d4716e72a0f607c38c8412d61771d9acae2}.
```

The run passed pinned dependency resolution, direct Lake build of
$\texttt{WeilDefect.Examples.WeakCriticalFallthrough}$, and the
unfinished-proof/project-axiom rejection gate.

WD-X06 is therefore closed.

All stable Horizon-1 theorem/example rows now have durable final Lean states.
Accordingly:

```math
\boxed{\texttt{LEAN-H1 EXHAUSTED}}
```

The next project cursor is recorded, but no H1-P5 work has been started:

```math
\boxed{\texttt{H1-P5.0 / PUBLIC PACKAGE ARCHITECTURE}}
```


---

## RPB-68 carrier-lift delta

The source layer for F-1 now exists in

~~~text
WeilDefect/Morphology/NeutralFourierCarrier.lean
~~~

and is imported by WeilDefect.lean.

Implemented source components:

- concrete real-line L2 representative;
- compact-support field in [-c,c];
- adapter back to NeutralNullExtensionInterface;
- nonzero transfer to the concrete L2 mode;
- coercion to tempered distributions;
- L2/tempered-distribution Fourier compatibility;
- semantic strict residual vanishing via Distribution.IsVanishingOn.

A temporary validation PR attempted to compile the new module, but GitHub
Actions run 36638336287 failed before exposing job steps or compiler logs.
Therefore the carrier is source-implemented but not yet build-certified.

WD-T40 remains LEAN-BLOCKED.



---

## RPB-69 build-gate blocker

Two independent temporary validation PRs attempted to compile

~~~text
WeilDefect.Morphology.NeutralFourierCarrier
~~~

without merging validation-only workflow changes into the research branch.

Both GitHub Actions jobs failed before runner allocation.

Observed job state in both cases:

~~~text
runner_id:          0
runner_name:        ""
runner_group_id:    0
runner_group_name:  ""
steps:              []
~~~

Therefore no checkout, toolchain setup, lake invocation, or Lean compiler
process occurred.

The F-1 carrier source is not certified and is not diagnosed as failing to
compile.

Current status:

~~~text
F-1:
    SOURCE IMPLEMENTED
    BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED

WD-T40:
    LEAN-BLOCKED
~~~

The next cursor is RPB-70 / WD-T40 carrier build infrastructure recovery.



---

## RPB-70 infrastructure-recovery delta

Three hosted validation routes now fail before runner allocation:

~~~text
ubuntu-latest / research-base
ubuntu-latest / main-base
ubuntu-slim / main-base
~~~

All three report runner_id 0, empty runner name, and zero steps.

The local execution environment has no Lean/Lake toolchain and cannot resolve external hosts, so it cannot install Elan/mathlib.

A deterministic repository check now exists at scripts/check_neutral_fourier_carrier.sh.

F-1 remains source-implemented and build-uncertified. F-2 remains unopened.

Next cursor: RPB-71 / WD-T40 carrier static elaboration audit.


---

## RPB-71 static API audit delta

The F-1 carrier source was checked declaration-by-declaration against pinned Lean/mathlib v4.34.0.

Static result:

~~~text
Lp / MemLp.toLp signatures: PASS
Lp -> tempered-distribution coercion: PASS
L2 Fourier instance: PASS
tempered Fourier instance: PASS
fourier_toTemperedDistribution_eq: PASS
Distribution.IsVanishingOn / mono direction: PASS
~~~

Four elaboration-hardening edits are now present: explicit volume, explicit residual set arguments, explicit Fourier coercions, and a direct unfold/exact adapter proof.

No declaration-shape mismatch remains. Build certification is still infrastructure-blocked, so F-1 is not Lean-certified and F-2 remains unopened.

Next cursor: RPB-72 / WD-T40 carrier typeclass synthesis audit.


---

## RPB-72 typeclass synthesis delta

Every implicit instance required by the F-1 carrier was traced through pinned mathlib v4.34.0.

Resolved statically: ENNReal p=2 fact, real inner-product and finite-dimensional structure, real measurable/Borel/second-countable structure, canonical volume/Haar measure, temperate growth of volume, local finiteness, complex inner-product/completeness, and both L2 and tempered Fourier instances.

No local instance shim was added because the required classes are already globally registered.

Current F-1 state: SOURCE IMPLEMENTED / STATIC API PASS / TYPECLASS STATIC PASS / BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED.

F-2 remains NOT STARTED.

Next cursor: RPB-73 / WD-T40 carrier proof-term elaboration audit.


---

## RPB-73 proof-term elaboration delta

The F-1 carrier proof bodies were audited line-by-line against pinned Lean/mathlib idioms.

Static result: PASS. The adapter target is explicit, nonzero transfer uses equality composition, Fourier compatibility uses an explicit change plus the pinned theorem, and residual monotonicity is a direct theorem application with named sets. No metavariable holes, simpa dependence, or rewrite-driven proof state remains.

Current F-1 state: SOURCE IMPLEMENTED / STATIC API PASS / TYPECLASS STATIC PASS / PROOF-TERM STATIC PASS / BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED.

F-2 remains NOT STARTED.

Next cursor: RPB-74 / WD-T40 F-1 static closure and build handoff.


---

## RPB-74 F-1 static closure delta

The audited F-1 source is frozen at Git blob `93f05eceb07ffda593181d0e9293caa0a05705ac`.

The deterministic handoff script `scripts/check_neutral_fourier_carrier.sh` now verifies the frozen blob, root import, exact module build, and unfinished-proof/project-axiom scan before reporting success.

Current F-1 state: SOURCE IMPLEMENTED / STATIC API PASS / TYPECLASS STATIC PASS / PROOF-TERM STATIC PASS / STATIC LINE EXHAUSTED / BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED.

No further static audit is live unless the frozen source changes or a real compiler diagnostic appears. F-2 remains NOT STARTED.

Next cursor: RPB-75 / WD-T40 F-1 build execution gate.


---

## RPB-75 build gate delta

The exact frozen F-1 handoff was attempted from a fresh validation branch based on the current RPB-74 research head.

Run 36645302165 again failed before runner allocation with runner_id 0 and zero steps. The local environment still has no Lean/Lake/Elan toolchain.

No compiler process ran. The frozen carrier and handoff script are unchanged. F-1 remains build-uncertified and F-2 remains NOT STARTED.

Next cursor: RPB-76 / WD-T40 F-1 build gate recheck.


---

## RPB-76 build gate delta

The exact frozen-handoff job from run 36645302165 was rerun.

Attempt 2 again failed before runner allocation with runner_id 0, empty runner name, and zero steps. No checkout, handoff script, Lake, or Lean process executed.

The frozen carrier blob and canonical handoff script are unchanged. F-1 remains statically exhausted and build-uncertified. F-2 remains NOT STARTED.

Next cursor: RPB-77 / WD-T40 F-1 build gate recheck.


---

## RPB-77 build gate delta

The exact frozen-handoff job from run 36645302165 was rerun as attempt 3.

Attempt 3 again failed before runner allocation with runner_id 0, empty runner name, and zero steps. The local environment still has no lean/lake/elan binary.

No Lean process ran. The frozen carrier and canonical handoff are unchanged. F-1 remains statically exhausted and build-uncertified. F-2 remains NOT STARTED.

Next cursor: RPB-78 / WD-T40 F-1 build gate recheck.


---

## RPB-78 F-1 build certification delta

GitHub-hosted runner access was restored and the exact audited F-1 carrier reached Lean.

Two compiler-level issues were resolved: the file required a `noncomputable section` because `Real.measureSpace` is noncomputable, and that unnamed section then required a matching plain `end` before `end WeilDefect`.

Certified carrier blob:

~~~text
03fe8ab1b6a3190e40a91b7a467c975e0d87841d
~~~

Successful validation evidence:

~~~text
run: 36649140221
job: 109679039673
runner_id: 1000001147
head: 5e2e9a1a3edad1f57e7afb0f357b822b92dc9099
~~~

The exact module build and repository-wide unfinished-proof/project-axiom scan both passed.

F-1 is therefore BUILD-CERTIFIED. WD-T40 remains LEAN-BLOCKED because F-2 through F-6 remain open.

Next cursor: RPB-79 / WD-T40 actual Weil multiplier realization.


---

## RPB-101 Gaussian-admissibility build certification delta

The RPB-100 source layer was compiled directly through:

~~~text
lake build WeilDefect.Morphology.NeutralGaussianAdmissibility
~~~

The first compiler run exposed one elaboration-only defect at the compact
central interval: Lean could not infer the endpoints hidden behind
`isCompact_Icc`.

The repair gave the local statement its intended explicit type:

~~~lean
have hpoleInt :
    IntegrableOn pole (Set.Icc (-residual.a) residual.a) volume :=
  hpole.pole_locallyIntegrable.integrableOn_isCompact isCompact_Icc
~~~

No mathematical hypothesis or theorem statement changed.

Successful validation evidence:

~~~text
run:  36780605398
job:  110109603982
head: 83a3635a294b7c16f9d382dbb87eee6532d9871b
blob: dfcfb49e443a00a6bea91c6bed15daed88ff0282
~~~

The exact module build and repository-wide unfinished-proof/project-axiom
rejection gate both passed.

Current F-4 state:

~~~text
CUTOFF-LIMIT CONSTRUCTOR: BUILD-CERTIFIED
POLE × MOVING-GAUSSIAN INTEGRABILITY FROM EXPONENTIAL GROWTH: BUILD-CERTIFIED
ACTUAL MOVING FILTERED MODE AS SCHWARTZMAP: OPEN
ACTUAL COMPACT SCHWARTZ CUTOFF PACKAGE: OPEN
RESIDUAL/POLE CUTOFF CONVERGENCE: OPEN
ACTUAL EXT-4 POLE GROWTH INSTANTIATION: OPEN
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

Next cursor:

~~~text
RPB-102 / WD-T40 F-4 ACTUAL MOVING-FILTERED-MODE SCHWARTZ REALIZATION
~~~


---

## RPB-102 moving-mode Schwartz carrier-side reduction delta

A new source module now records the carrier-side part of the moving-mode
Schwartz problem:

~~~text
WeilDefect/Morphology/NeutralGaussianSchwartz.lean
~~~

Build-certified declarations:

~~~text
neutralPhysicalRepresentative_polynomialNorm_integrable
neutralPhysicalRepresentative_polynomialSmul_integrable
neutralPhysicalRepresentative_fourier_contDiff
neutralPhysicalRepresentative_fourier_hasTemperateGrowth
~~~

The first two declarations prove every polynomial norm/scalar moment of the
compactly supported F-1 representative is integrable.  No differentiability
of the representative is required.

Pinned mathlib's Fourier-derivative API then proves that the ordinary Fourier
transform of the representative is C-infinity.  The derivative formulas plus
the L1 norm bound for the Fourier integral give uniform bounds on every
derivative, hence:

~~~text
Function.HasTemperateGrowth (𝓕 carrier.h)
~~~

with polynomial degree zero sufficient for each derivative.

Successful validation evidence:

~~~text
carrier moment + Fourier smoothness:
    run:  36794685260
    job:  110155298721
    head: 2c9b74e74590d1766f681ac2155bdc418f9845d0

temperate-growth extension:
    run:  36795139285
    job:  110156751629
    head: eedbd92800e750711c02e7a5c30b97f50f75d85c
    blob: 4bb1fec7270d25fc8a9b899b8d3f204e12b342b1
~~~

Both exact module builds and unfinished-proof/project-axiom rejection gates
passed.

The carrier therefore contributes no remaining smoothness assumption to the
F-4 Schwartz seam.

Current remaining seam:

~~~text
1. bundle the positive-R Gaussian seed as SchwartzMap ℝ ℂ;
2. impose the exact project Fourier normalization / modulation / scaling;
3. multiply the seed by the certified temperate multiplier 𝓕 h;
4. inverse Fourier transform;
5. identify the resulting SchwartzMap pointwise with
   movingGaussianFilteredMode Ck R carrier.
~~~

Next cursor:

~~~text
RPB-103 / WD-T40 F-4 GAUSSIAN SCHWARTZ SEED + MOVING-MODE FOURIER IDENTIFICATION
~~~

Do not add a smoothness premise on carrier.h.  Compact cutoff convergence and
logarithmic coercivity remain downstream.


---

## RPB-103 moving-filtered-mode Schwartz closure delta

Two modules now close the actual moving-mode Schwartz obligation:

~~~text
WeilDefect/Morphology/NeutralGaussianSchwartzSeed.lean
WeilDefect/Morphology/NeutralGaussianFilteredSchwartz.lean
~~~

The seed module constructs the standard real Gaussian as a Schwartz function,
rescales it to the project width `exp(-R x^2 / 4)`, complexifies it, and
multiplies by the exact oscillatory phase `exp(i R x)`.  The resulting
`movingGaussianPhysicalKernelSchwartz` is pointwise equal to the existing
physical kernel.

The filtered module multiplies the Schwartz Fourier transform of that kernel
by the RPB-102 temperate multiplier `𝓕 carrier.h`, then applies inverse
Fourier transform.  Fourier/convolution compatibility and ordinary inversion
identify the bundled result with the whole-line physical convolution, and
compact support of `carrier.h` reduces that integral to the original F-3
definition.

Certified endpoint:

~~~lean
movingGaussianFilteredModeSchwartz_apply
~~~

with pointwise identity:

~~~text
movingGaussianFilteredModeSchwartz Ck R hR carrier x
  = movingGaussianFilteredMode Ck R carrier x
~~~

for `R > 0`.

Final custody-safe validation:

~~~text
run:  36799159760
job:  110169382060
head: 105afd4f4fdb215e138af4af642ff2acfa165512

seed blob:
5874ebc61f915e4612fa6ee02bec033a418b0d6a

filtered blob:
c639b2f5df08d2365cf9dc0c6933a60ed72dbebe
~~~

The full exact-module build and unfinished-proof/project-axiom rejection gate
both passed.

RPB-100 burden A is therefore closed.

Remaining pre-coercivity burdens:

~~~text
B. compactly supported Schwartz cutoffs converging in Schwartz topology
C. residual pairing convergence along those cutoffs
D. pole pairing convergence along those cutoffs
E. actual EXT-4 pole exponential-growth instantiation
~~~

Next cursor:

~~~text
RPB-104 / WD-T40 F-4 COMPACT SCHWARTZ CUTOFF CONSTRUCTION + SCHWARTZ-TOPOLOGY CONVERGENCE
~~~

Logarithmic coercivity remains unopened.


---

## RPB-104 compact Schwartz cutoff convergence delta

The actual moving filtered mode now has an explicit compactly supported
Schwartz approximation sequence.

New module:

~~~text
WeilDefect/Morphology/NeutralGaussianCutoff.lean
~~~

The construction uses a fixed `ContDiffBump` with inner radius 1 and outer
radius 2 and rescales it by `R^{-1}`.

Core declarations:

~~~text
neutralGaussianCutoffScalar
neutralGaussianSchwartzCutoff
neutralGaussianSchwartzCutoff_compact
neutralGaussianSchwartzCutoff_seminorm_le
neutralGaussianSchwartzCutoff_tendsto
movingGaussianFilteredModeCompactCutoff
movingGaussianFilteredModeCompactCutoff_compact
movingGaussianFilteredModeCompactCutoff_tendsto
~~~

For every Schwartz function `f`, the cutoff error satisfies an explicit
seminorm estimate of order `O(1/R)`.  Taking `R=N+1` gives convergence in
the complete Schwartz topology, not merely pointwise or in an Lp norm.

Applied to the RPB-103 moving filtered mode, Lean certifies:

~~~text
each cutoff term: compactly supported
cutoff sequence:  tends to movingGaussianFilteredModeSchwartz
                  in Schwartz topology
~~~

Successful validation evidence:

~~~text
run:  36800396833
job:  110173193606
head: 8e8cf915220bf5bff355d4df006b3c18b926a780
blob: e8f5319b0b8a8b2a1c840e8630f53f2c7dce08da
~~~

The exact module build and repository-wide unfinished-proof/project-axiom
rejection gate both passed.

RPB-100 burden B is therefore closed.

Remaining pre-coercivity burdens:

~~~text
C. residual pairing convergence along cutoffs
D. pole pairing convergence along cutoffs
E. actual EXT-4 pole exponential-growth instantiation
~~~

Next cursor:

~~~text
RPB-105 / WD-T40 F-4 RESIDUAL + POLE CUTOFF PAIRING CONVERGENCE
~~~

Logarithmic coercivity remains unopened.


---

## RPB-105 cutoff pairing convergence delta

New module:

~~~text
WeilDefect/Morphology/NeutralGaussianCutoffPairing.lean
~~~

The source first upgrades the existing exterior residual pairing
integrability to whole-line integrability by combining the exterior result
with the certified a.e. central vanishing of the residual.

It then proves a general dominated-convergence theorem for the RPB-104
cutoff operator:

~~~lean
neutralGaussianSchwartzCutoff_pairing_tendsto
~~~

The argument uses only:

~~~text
0 <= cutoff <= 1
each fixed x is eventually inside the cutoff-one region
integrability of the uncut pairing
~~~

Specializations:

~~~text
movingGaussianFilteredModeCompactCutoff_residual_pairing_tendsto
movingGaussianFilteredModeCompactCutoff_pole_pairing_tendsto
~~~

The residual specialization is unconditional under the existing F-3
large-R hypotheses.

The pole specialization is conditional exactly on:

~~~text
NeutralPoleExponentialGrowthData pole
~~~

and uses the RPB-100 whole-line pole-pairing integrability theorem.

Successful validation evidence:

~~~text
run:  36801083567
job:  110175352895
head: 646adabb7d5423b4eafbd388150a6d0cd0cba2f8
blob: ea80c81d5d31768c68a6ea0ec69c68bed0cab806
~~~

The exact module build and repository-wide unfinished-proof/project-axiom
rejection gate both passed.

RPB-100 burden C is closed.  Burden D is closed conditional only on burden E.

Remaining pre-coercivity burden:

~~~text
E. actual EXT-4 pole exponential-growth instantiation
~~~

Once E is certified, the already-proved cutoff package fields can be assembled
into the actual `RightLimitWeilGaussianCutoffPremise`, after which RPB-100
derives the Gaussian weak identity internally.

Next cursor:

~~~text
RPB-106 / WD-T40 F-4 ACTUAL EXT-4 POLE EXPONENTIAL-GROWTH INSTANTIATION
~~~

Logarithmic coercivity remains unopened.


## RPB-107 source-pole attachment and test-duality audit

RPB-107 separates two issues that had been compressed into the former
"concrete EXT-4 attachment" cursor.

The new module

~~~text
WeilDefect/Morphology/NeutralGaussianDualityAudit.lean
~~~

is build-certified under the pinned toolchain:

~~~text
run:  36807944842
job:  110196386366
head: 52c22e7dd49ac50f8ea228b046db5faf5b2362de
blob: e9d4fde62ea2bbd8e7c586b134e81e58103b9085
target: lake build WeilDefect.Morphology.NeutralGaussianDualityAudit
result: PASS (8948 jobs)
unfinished/project-axiom rejection gate: PASS
~~~

Certified declarations include:

~~~text
conjugateSchwartz
movingGaussianFilteredModeDualTest
neutralWeilPoleMoment_eq_integral
neutralWeilPoleMoment_integrable_global
neutralWeilSourcePole_pairing_eq
complex_bilinear_phase_I
complex_hermitian_phase_I
~~~

The source-pole theorem gives exactly

~~~math
\int h(x)p_h(x)\,dx
=
2M_{-1/2}(h)M_{1/2}(h),
~~~

so the RPB-106 two-exponential pole is attached at the quadratic-algebra
level to the two evaluation factors in the pinned compact-window formula.

The duality audit also proves that the present unconjugated complex pairing
has bilinear phase scaling: a common phase \(i\) changes its sign.  By
contrast, the conjugated test

~~~math
G_R^\vee(x)=\overline{G_R(x)}
~~~

has Hermitian phase invariance.  This is the test species required before the
weak identity can be interpreted as the Fourier energy containing
\(|\widehat h|^2\).

The pinned EXT-4 source gives a quadratic form.  The current
`RightLimitWeilWeakRealizationPremise` is a stronger polarized complex
operator identity against arbitrary compact complex Schwartz tests.  RPB-107
does not manufacture that strengthening from the source.  The exact remaining
formal seam is therefore polarization/complexification plus cutoff passage for
the Hermitian Gaussian dual test.

Next cursor:

~~~text
RPB-108 / WD-T40 F-4
POLARIZED EXT-4 OPERATOR REALIZATION
+ HERMITIAN GAUSSIAN CUTOFF BRIDGE
~~~

Logarithmic coercivity remains unopened.
