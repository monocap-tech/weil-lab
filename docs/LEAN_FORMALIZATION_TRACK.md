# Lean Formalization Track

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
