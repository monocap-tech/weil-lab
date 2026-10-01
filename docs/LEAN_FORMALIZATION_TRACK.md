# Lean Formalization Track

## RPB-106 certification correction and live handoff

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
