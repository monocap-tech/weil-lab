# Lean Formalization Track

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

## RPB-108 — strict-source action threshold correction certified

The source strict `<` and project right-limit `<=` conventions are now
connected at the physical action level.

Certified additions to `NeutralWeilSourceThreshold.lean` include

~~~text
rightLimitThresholdPrimePhysical
rightLimitThresholdPrime_pairing_integrable
rightLimitThresholdPrime_fourier_physical_pairing
strictSourceWeilMultiplierCore
strictSourceCompactAction
frozenWeilCompactAction_eq_strictSource_sub_threshold
StrictSourceCorrectedWindowPremise
StrictSourceCorrectedWindowPremise.toRightLimit
~~~

with

~~~math
E_a^{<=}(h;u)
=
E_a^{<}(h;u)
-
\int u\,\Theta_a^{phys}h.
~~~

The remaining source premise can therefore be stated literally with the
pinned strict prime cutoff and converted internally to the right-limit window
premise already consumed downstream.

~~~text
run: 36871575764 / job: 110400389955
head: 3bf8577200c8ef4d1648c0613106aaf6d7706931
target: lake build WeilDefect.Morphology.NeutralWeilSourceThreshold
blob: 2e1a1d755da1414651fe088cf42a787a3df213fa
build: PASS (8953 jobs)
three endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration gate: PASS
~~~

The threshold convention is no longer part of the open source boundary.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
NEXT: FINITE-WINDOW SOURCE FORM-DOMAIN + HERMITIAN POLARIZATION/COMPLEXIFICATION + ACTUAL RESIDUAL REPRESENTATION
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — strict-source/right-limit threshold correction certified

The pinned source's strict prime convention and the project's equality-retaining
right-limit convention are now separate build-certified objects.

New module:

~~~text
WeilDefect/Morphology/NeutralWeilSourceThreshold.lean
~~~

Lean proves that the correction Finset is exactly the at-most-one set of prime
powers satisfying `log n = 2a`, and certifies

~~~math
\Psi_a^{\le}
=
\Psi_a^{<}-\Theta_a.
~~~

Away from a threshold the symbols coincide.  The finite threshold term has
temperate growth, so the strict source symbol inherits temperate growth from
the existing right-limit symbol premise with no additional external
special-function input.

~~~text
run: 36867533110 / job: 110386685114
checked-out head: db27a3a2536746060d6eb7c3dabe756b7f85b62e
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
target: lake build WeilDefect.Morphology.NeutralWeilSourceThreshold
source blob: ae44725b1147992aa0392e130e46611e3a268bad
build: PASS (8953 jobs)
four audited endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration rejection gate: PASS
~~~

The remaining RPB-108 source frontier is no longer threshold bookkeeping:

~~~text
NEXT:
FINITE-WINDOW SOURCE FORM-DOMAIN
+ HERMITIAN POLARIZATION / COMPLEXIFICATION
+ ACTUAL WHOLE-LINE RESIDUAL REPRESENTATIVE ATTACHMENT

LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — shell-corrected source-window globalization certified

The all-compact frozen weak-realization premise is no longer the minimal
external source boundary.  The new certified module
`NeutralWeilSourceWindowAttachment.lean` proves that it follows from a
shell-corrected identity on each sufficiently large finite source window.

A free support globalization was explicitly rejected: `E_b` compresses to
`E_a` without correction only for tests already supported in the old
window.  For arbitrary compact tests the exact certified relation is

~~~math
E_a(h;u)=E_b(h;u)+\int u(x)P_{a,b}h(x)\,dx.
~~~

The new finite-window premise carries that shell term explicitly and then
globalizes to the existing `RightLimitWeilWeakRealizationPremise`.

~~~text
run: 36824968898 / job: 110248500881
checked-out head: af0060d6acef81062a01eb06087dd3566bc800bb
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
target: lake build WeilDefect.Morphology.NeutralWeilSourceWindowAttachment
source blob: 5be297c758f1f169be2f4eadf00996beeae3a6e4
build: PASS (8952 jobs)
four audited endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration rejection gate: PASS
~~~

The earlier green run `36823900387` built an unrelated inherited target and
is explicitly not a certificate.

The source reconstruction frontier is now finite-window:
form-domain inclusion, polarization/complexification of the source quadratic
identity, the strict-cutoff/right-limit equality-threshold correction, and
attachment of the actual residual with its retained regularity/growth fields.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
NEXT: SOURCE QUADRATIC FORM-DOMAIN + THRESHOLD-CORRECTED LOCAL RESIDUAL ATTACHMENT
HERMITIAN GAUSSIAN BRIDGE: READY DOWNSTREAM
LOGARITHMIC COERCIVITY: NOT STARTED
~~~


## RPB-108 — Fourier/physical shell certified; source attachment continues

The [prime-shell translation certificate](../notes/REFLECTED_PACKET_BRIDGE_108_PRIME_SHELL_TRANSLATION_20260930.md)
closes the previously missing Fourier/physical connection. The finite cosine
shell multiplier now equals the physical symmetric-translation shell in its
pairing with every complex Schwartz test. Genuine pairing integrability is
proved without adding smoothness to the compact L2 carrier.

~~~text
run: 36818895703 / job: 110229945734
checked-out head: bf38f197440a0fd1ea11b699813547672dad3b34
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
target: lake build WeilDefect.Morphology.NeutralWeilPrimeShellTranslation
source blob: 628f979cb0e7b33d22c1a1144ae9e5c25560d257
build and declaration gate: PASS
all nine endpoint axiom closures: propext, Classical.choice, Quot.sound
~~~

Combined with the existing radius correction and shell support theorem, this
proves equality of the two internally defined frozen actions on compact tests
supported in the old open window. It does not identify those actions with the
external source form or construct the supplied residual witness.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FOURIER/PHYSICAL PRIME-SHELL IDENTIFICATION: CERTIFIED
INTERNAL FROZEN-ACTION COMPRESSION EQUALITY: CERTIFIED
NEXT: SOURCE FORM-DOMAIN / POLARIZED COMPRESSION ATTACHMENT
THEN: ACTUAL RESIDUAL REPRESENTATION WITH RETAINED DOMAIN/GROWTH CONDITIONS
HERMITIAN GAUSSIAN CUTOFF BRIDGE: CERTIFIED CONDITIONAL
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

Do not restart the Gaussian or cosine/translation constructions. Imported
hypotheses remain explicit parameters. The full EXT-4 attachment remains open;
earlier handoffs below are preserved as history, not current instructions.

## RPB-108 — frozen-cutoff action and radius-correction continuation

The [frozen-extension continuation certificate](../notes/REFLECTED_PACKET_BRIDGE_108_FROZEN_EXTENSION_20260930.md)
records the exact source and build evidence for this subpass. The selected
compact-test action now holds the prime cutoff fixed independently of the
test support. Its pole pairing is integrable. The difference between two
cutoff radii is explicitly the finite added-prime-shell multiplier, with the
source-to-mathlib frequency normalization retained.

The separately defined physical shell vanishes on the old open window when
`c <= a`. Its identification with the Fourier shell multiplier still needs
its own translation/Fourier proof. Do not treat these separately certified
identities as an already certified source-compression theorem.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
FROZEN COMPACT-TEST ACTION + EXACT MULTIPLIER RADIUS CORRECTION: CONSTRUCTED
PHYSICAL ADDED-SHELL VANISHING ON THE OLD WINDOW: PROVED
NEXT: FOURIER/PHYSICAL SHELL IDENTIFICATION + SOURCE COMPRESSION
THEN: ACTUAL RESIDUAL REPRESENTATION WITH RETAINED DOMAIN/GROWTH CONDITIONS
HERMITIAN GAUSSIAN CUTOFF BRIDGE: CERTIFIED CONDITIONAL
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

The `frozenWeilCompactAction_represents_iff` equivalence characterizes the
remaining residual attachment; it is not a construction of that witness.
Definitions are registered in the additive [RPB-108 terminology supplement](TERMINOLOGY_RPB108_FROZEN_EXTENSION.md).
No Gaussian seed, Schwartz realization, or cutoff-limit proof is restarted.
The earlier certificates and handoffs below remain historical records.

## RPB-108 — certified Hermitian bridge; source attachment remains open

**Effective live state:** the Hermitian Gaussian cutoff bridge, scoped real
polarization/complexification algebra, and the correct conjugate cross-moment
pole pairing are now build-certified. The full EXT-4 source-operator
attachment is not yet discharged; RPB-108 remains active.

~~~text
run:  36813420117
job:  110213211667
checked-out head: db57718d34c7e064744ba8e7b6eca21be0b6592a
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
target: lake build WeilDefect.Morphology.NeutralGaussianHermitianBridge
source blob: b32fc8623b6c3e69efd3c0e82019997bf76a1e92
build: PASS
all eight inspected endpoint axiom closures: propext, Classical.choice, Quot.sound
declaration rejection gate: PASS
~~~

The existing bilinear distribution interface is valid. The corrected energy
test is the conjugated Gaussian, and its weak identity is now derived by
compact cutoffs under the exact existing compact weak witness. No additional
Gaussian identity is assumed.

The source's fixed-window quadratic formula can be polarized within its
form domain, but this does not automatically extend the fixed-cutoff operator
to all compact tests on the whole line. Define that frozen-cutoff extension,
identify its compression with the polarized source form, and attach the
actual residual representative. Preserve the form-domain, growth, threshold,
and Fourier-normalization conditions explicitly.

~~~text
RPB-108 / WD-T40 F-4
CONTINUE: FROZEN-CUTOFF EXT-4 EXTENSION + ACTUAL RESIDUAL WITNESS ATTACHMENT
HERMITIAN GAUSSIAN CUTOFF BRIDGE: CERTIFIED CONDITIONAL
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

The [final RPB-108 certificate](../notes/REFLECTED_PACKET_BRIDGE_108_CERTIFICATE_20260930.md)
supersedes the build-pending status of the [implementation checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_20260930.md).
The general `LEAN_STATUS.md` queue remains RPB-108. Do not restart the
Gaussian seed, moving-mode Schwartz realization, or the generic cutoff
convergence proofs. Do not mark the whole source attachment closed from the
conditional bridge certificate. Earlier handoffs below are historical.

## RPB-107 duality audit and live handoff

RPB-107 is build-certified under pinned Lean 4.34.0 / mathlib
5ed2965256430c3649e86755f9576b54eca72435.

~~~text
run:  36807944842
job:  110196386366
head: 52c22e7dd49ac50f8ea228b046db5faf5b2362de
target: lake build WeilDefect.Morphology.NeutralGaussianDualityAudit
result: PASS
blob: e9d4fde62ea2bbd8e7c586b134e81e58103b9085
~~~

The exact two-exponential source pole now reproduces the source quadratic pole
factor through a certified whole-line pairing identity.  The same pass
constructs the conjugated moving Gaussian as a Schwartz test and certifies the
phase distinction between the existing complex-bilinear pairing and the
Hermitian pairing required by the Fourier energy.

This does not reconstruct EXT-4.  The pinned source presents a quadratic form,
whereas the existing Lean compact weak-realization premise asserts a polarized
complex operator identity against every compact complex Schwartz test.  The
remaining task is to derive that polarization/complexification explicitly and
then pass it to the Hermitian Gaussian dual test by compact cutoffs.

The next live cursor is:

~~~text
RPB-108 / WD-T40 F-4
POLARIZED EXT-4 OPERATOR REALIZATION
+ HERMITIAN GAUSSIAN CUTOFF BRIDGE
~~~

Do not begin logarithmic coercivity until the Hermitian compact-test identity
and its Gaussian cutoff limit are certified.


## RPB-106 certification correction and live handoff

**Repair complete.** Correct-target validation run `36803460601` / job
`110182696916` checked out
`d9c0b171263862ed088620597f3d8d5ff7512278` and directly built
`WeilDefect.Morphology.NeutralGaussianAssembly`. The build transitively
compiled the repaired RPB-104 cutoff module, repaired RPB-105 pairing module,
the concrete two-exponential pole-growth module, and the Gaussian assembly.
The six endpoint declarations audited by `#print axioms` contain only
`propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` appears.
This is the actual certificate for the repaired 104/105 dependency closure;
the original wrong-target green runs remain historical and are not
retroactively reclassified.

The concrete source-pole growth and conditional Gaussian-admissibility
assembly are therefore certified.  The assembly still requires an explicit
compact EXT-4 witness whose pole is exactly
`neutralWeilSourcePole carrier`; EXT-4 itself has not been reconstructed in
Lean.  The next live cursor is:

~~~text
RPB-107 / WD-T40 F-4
CONCRETE EXT-4 POLE ATTACHMENT + TEST-DUALITY AUDIT
~~~

Do not enter logarithmic coercivity until the imported compact identity is
attached to the named pole and the bilinear/Hermitian test convention is
audited.

The effective post-RPB-105 state and next cursor are recorded in [RPB-106 — certification repair and source-pole assembly](../notes/REFLECTED_PACKET_BRIDGE_106_20260930.md). That record supersedes the RPB-104/105 certificate claims in the historical snapshot below and in `LEAN_STATUS.md`.

The original RPB-104 and RPB-105 green runs built `WeilDefect.Examples.WeakCriticalFallthrough`, not the named cutoff modules. Their statuses are preserved as run history, but their claimed certification scope is withdrawn. Repaired source must be associated with its own correct-target run and exact blobs; no later success retroactively changes what those original runs checked.

For all subsequent certificates, read the actual build command and compiler trace, record the checked-out commit, pinned dependency revision and target blobs, and inspect the endpoint's transitive axioms. A green run on an unrelated target is not a certificate. Gaussian admissibility remains distinct from logarithmic coercivity, and the imported EXT-4 witness must identify the very pole supplied to the assembly constructor.

The LEAN-H1 material and pre-RPB-106 post-Horizon snapshot below are retained for provenance. They are not the current RPB cursor.

## LEAN-H1 — Certification before H1-P5 — EXHAUSTED

This track preempted H1-P5 until its exhaustion condition was met.

LEAN-H1 is exhausted under the current Horizon-1 theorem inventory. The subsequent H1-P5 public-package phase is also complete; see [Public Package Audit](PUBLIC_PACKAGE_AUDIT.md).

This page is the **control surface** for the completed formalization track. Certificate evidence and historical run records belong in [Lean Status](LEAN_STATUS.md); this page records the phase structure, exhaustion rule, and current post-LEAN handoff.

## Toolchain

Pinned baseline:

```math
\boxed{
\text{Lean 4.34.0}
\qquad
\text{mathlib v4.34.0}.
}
```

The project uses:

- `lean-toolchain`;
- `lakefile.toml`;
- the `WeilDefect` Lean namespace;
- GitHub Actions build verification.

## Certification rule

A theorem is **LEAN-CERTIFIED** only if:

1. its Lean declaration exists in the repository;
2. the declaration contains no `sorry`, `admit`, or project `axiom`;
3. the pinned Lean/mathlib build succeeds in CI;
4. the theorem-ID-to-declaration map is recorded durably.

A proof downstream from an imported external theorem is not called a full Lean certification of that external theorem.

Instead the status is:

```math
\boxed{
\text{LEAN-CERTIFIED-FROM-IMPORTED-PREMISE}.
}
```

The imported premise itself remains separately unformalized until its source theorem is reconstructed in Lean.

## Phases

### LEAN-H1-P0 — Infrastructure and vertical pilot — COMPLETE

- initialize Lake/mathlib project;
- pin toolchain;
- establish CI;
- prohibit `sorry`, `admit`, and project `axiom`;
- certify a small vertical slice of algebraic theorem/example statements.

### LEAN-H1-P1 — Algebraic and finite-dimensional core — COMPLETE

Primary targets:

- WD-T05;
- WD-T07;
- WD-T09;
- WD-T14;
- WD-T20;
- WD-T21;
- WD-T26;
- WD-T27;
- WD-X01 through WD-X07.

### LEAN-H1-P2 — Operator screening core

Targets:

- WD-T01 through WD-T13 excluding statements already discharged;
- Douglas-dependent theorems formalized downstream from an explicit imported-premise interface until Douglas itself is reconstructed or mapped to an existing mathlib theorem.

### LEAN-H1-P3 — Filtration and persistence core

Targets:

- WD-T15 through WD-T19;
- weak/strong convergence;
- endpoint intersection spaces;
- quotient/index arguments;
- boundary amplification.

### LEAN-H1-P4 — Zeta-Weil specialization

Targets:

- WD-T20 through WD-T36;
- imported analytic results represented as explicit premises where their source proofs have not yet been formalized;
- no hidden project axioms.

### LEAN-H1-P5 — Composite morphology

Targets:

- WD-T37 through WD-T39;
- certify the deductions from already certified internal theorems and explicit external premises;
- preserve every P4.3 branch/custody correction.

### LEAN-H1-P6 — Imported-source reconstruction frontier

Attempt direct Lean reconstruction of load-bearing external results where feasible:

- Douglas factorization if not already available in mathlib;
- Bombieri finite inertia/multiplicity;
- zeta zero counting;
- compact-window explicit formula;
- special-function asymptotics.

This phase may terminate with exact formalization blockers if reconstructing an external analytic theorem requires a corpus far larger than this project.

## Exhaustion condition

LEAN-H1 is exhausted only when every stable Horizon-1 theorem/example has one of the following durable states:

```math
\boxed{
\begin{array}{l}
\text{LEAN-CERTIFIED},\\
\text{LEAN-CERTIFIED-FROM-IMPORTED-PREMISE},\\
\text{LEAN-BLOCKED with an exact formal dependency/blocker},\\
\text{SCOPE-ONLY}.
\end{array}
}
```

A theorem may not remain merely “not attempted.”

Only after this exhaustion condition is met does the project resume:

```math
\boxed{
\texttt{H1-P5.0 / PUBLIC PACKAGE ARCHITECTURE}.
}
```

## Historical pre-RPB-106 control snapshot

- **LEAN-H1:** EXHAUSTED.
- **H1-P5:** COMPLETE.
- **Active Lean phase:** none.
- **Active Lean cursor:** none.
- **Next project cursor:** RPB-106 / WD-T40 F-4 actual EXT-4 pole exponential-growth instantiation.

```math
\boxed{
\texttt{LEAN-H1 EXHAUSTED / H1-P5 COMPLETE / HORIZON 1 COMPLETE}
}
```

WD-X06 is `LEAN-CERTIFIED`, LEAN-H1 is exhausted, and H1-P5.0 through H1-P5.5 are complete. Horizon 1 is complete. The historical LEAN-H1 track remains exhausted. Post-Horizon theorem WD-T40 is now LEAN-BLOCKED after RPB-67: a faithful certificate requires a new physical real-line Fourier/distribution carrier layer. The F-1 physical Fourier carrier is now build-certified under pinned Lean 4.34.0 / mathlib v4.34.0 (run 36649140221, carrier blob 03fe8ab1b6a3190e40a91b7a467c975e0d87841d). The remaining WD-T40 formalization frontier begins at F-2, the actual compact-window Weil multiplier realization. The exact strict-right scalar symbol is build-certified by RPB-80 (run 36677931966, blob fe0b84a5c7a1d8d7acfe57ce2674c36d8e386202). RPB-81 then found that the full pole-restored residual is not lawfully typed as tempered because the promoted theorem allows fixed exponential growth. RPB-100 implemented the cutoff-limit constructor that derives the Gaussian weak identity and the exponential-pole Gaussian integrability layer. RPB-101 then build-certified that source layer after one elaboration-only repair making the compact central interval explicit (run 36780605398; blob dfcfb49e443a00a6bea91c6bed15daed88ff0282). RPB-102 proves from compact support alone that every polynomial moment of the physical representative is integrable and that its ordinary Fourier transform is C-infinity with temperate growth (runs 36794685260 and 36795139285; blob 4bb1fec7270d25fc8a9b899b8d3f204e12b342b1). RPB-103 then build-certified the exact Gaussian Schwartz seed and the complete moving-filtered-mode Schwartz realization, including pointwise equality with the existing F-3 convolution (run 36799159760; filtered blob c639b2f5df08d2365cf9dc0c6933a60ed72dbebe). RPB-104 then build-certified an explicit compactly supported Schwartz cutoff sequence for the actual moving filtered mode, together with full Schwartz-topology convergence (run 36800396833; blob e8f5319b0b8a8b2a1c840e8630f53f2c7dce08da). RPB-105 then build-certified both ordinary-integral cutoff pairing limits by dominated convergence; the pole limit is conditional only on the explicit `NeutralPoleExponentialGrowthData` carrier (run 36801083567; blob ea80c81d5d31768c68a6ea0ec69c68bed0cab806). The next research cursor is RPB-106 / WD-T40 F-4 actual EXT-4 pole exponential-growth instantiation. See [Lean Status](LEAN_STATUS.md) for the declaration map and certificate evidence and [Public Package Audit](PUBLIC_PACKAGE_AUDIT.md) for package closure.


---

## Post-Horizon WD-T40 formalization frontier

RPB-67 determined that mathlib v4.34 has the required base Fourier/Gaussian
infrastructure, but the current WeilDefect Lean abstraction is too high-level
to state WD-T40 faithfully.

The physical real-line carrier bridge F-1 is now build-certified. The next missing bridge connects that carrier to:

- L2 Fourier data;
- compact support;
- tempered-distribution residuals;
- the actual compact-window Weil multiplier.

The strict-right scalar symbol layer of F-2 is build-certified.

RPB-81 corrected the target carrier: the scalar multiplier core remains
tempered, but the full pole-restored residual requires a broader physical
exponential-growth carrier.

The corrected exponential-growth residual carrier and compact-test
weak-realization target interface are now build-certified.

The exact scalar symbol's imported temperate-growth premise interface and the
conditional canonical tempered multiplier core are now build-certified.

The actual EXT-4 weak-realization bridge is now build-certified, and F-2 is
complete conditional on the explicit imported EXT-4 / EXT-5D premises.

F-3 remains open.  The strict collar geometry and exterior pointwise Gaussian
domination are now build-certified; the actual filtered-mode convolution
envelope and Gaussian tail integration remain open.

The actual moving-Gaussian kernel, compact-support convolution, and corrected
exterior filtered-mode envelope are now build-certified.

The residual's fixed exponential growth is now reduced by a build-certified
completion layer to an integrable exterior Gaussian tail while retaining an
explicit exponentially small collar factor in the moving parameter.

The source-frequency to mathlib-frequency repair t = 2*pi*xi is now
build-certified through the full F-3 pairing stack.

The next cursor is:

~~~text
RPB-98 / WD-T40 F-4 GAUSSIAN-ADMISSIBILITY WEAK-REALIZATION BRIDGE
~~~

The noncompact moving-Gaussian domain seam is now represented by a
build-certified admissibility interface.  The interface itself is typed and
kernel-checked; its cutoff/growth discharge from the current carrier remains
open.

The Gaussian weak identity is now an internal consequence of compact-test EXT-4 plus a cutoff package, and exponential pole growth is sufficient for whole-line pole pairing integrability in source. The actual cutoff package and actual pole-growth instantiation remain open.

The next cursor is:

~~~text
RPB-106 / WD-T40 F-4 ACTUAL EXT-4 POLE EXPONENTIAL-GROWTH INSTANTIATION
~~~

The RPB-100 Gaussian-admissibility source layer is now build-certified. RPB-102 closes the carrier-side regularity burden: compact support alone makes every polynomial moment integrable, and the Fourier transform of the carrier is smooth and temperate. The actual moving filtered mode is build-certified as a SchwartzMap and pointwise identified with the existing physical convolution. An explicit compactly supported Schwartz cutoff sequence now converges to it in the full Schwartz topology. Residual cutoff convergence is closed, and pole cutoff convergence is closed conditional on the explicit pole-growth carrier. The only remaining RPB-100 Gaussian-admissibility burden is actual EXT-4 pole-growth instantiation. The logarithmic coercivity inequality and F-5 strip holomorphy remain closed.
