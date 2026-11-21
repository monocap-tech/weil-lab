# PI015 — Exact two-toolchain source resolution and finite Gamma multiplier bridge

**PI### Potential Interface**, stacked on PI014 PR #830 → PI013 #828 → PI012 #824 → PI011 #823 → PI010 #821 → PI009 #820 → PI008 #818 → PI007 #816 and preceding PI stages. Canonical registry: issue #792. **No NF###, IV### or CP### branch, theorem, numerical certificate or workflow modified.**

**Status:** source-ref resolution and exact mathematical finite-symbol bridge; new **Lean proof candidates** in two separately pinned compiler environments; exact Fraction algebra PASS. **NO PI015 Lean compiler/axiom PASS, no valid cross-compiler import theorem, no original IV011 signed Gamma transport, no independent Masullo operator trace, no global Weil positivity or RH/GRH.**

## 1. PI014's apparent mismatch is a genuine two-version boundary

Actual inspected Git and source refs, not guessed release mapping:

| Source | Lean toolchain | Mathlib declared ref | Git commit of Mathlib ref |
|---|---|---|---|
| Weil-Lab PI branch | leanprover/lean4:v4.34.0 | v4.34.0 | 5ed2965256430c3649e86755f9576b54eca72435 |
| Zeta23 upstream | leanprover/lean4:v4.33.0-rc2 | 51e6992efd06126df61a496bebf8f49482a4e129 | 51e6992efd06126df61a496bebf8f49482a4e129 |

GitHub's actual \`mathlib4\` tag \`refs/tags/v4.33.0-rc2\` resolves to **51e6992efd06126df61a496bebf8f49482a4e129**; \`refs/tags/v4.34.0\` resolves to **5ed2965256430c3649e86755f9576b54eca72435**. They are distinct commit objects. The Zeta23 repo's pinned compiler \`v4.33.0-rc2\` matches the older ref, and its \`zeta23/lake-manifest.json\` also resolves to exactly the older SHA.

Authenticated upstream source custody, **read from the GitHub repository**:
- root Git commit: \`anthropics/formal-math@16a5ce41304fcdaea4e0be7c132e1c361dc26da5\` (source snapshot, 2026-10-27);
- \`zeta23/lean-toolchain\` Git blob \`c084c7fbe586b0276863b66f16d2955a43bc3fc6\`;
- \`zeta23/lakefile.toml\` Git blob \`43d9da33fb523dce999b070df74e7cdd03381e2b\`;
- \`zeta23/lake-manifest.json\` Git blob \`af9ef405e4e292f2e0176b12b6cb66f547575314\`;
- \`zeta23/Zeta23/Defs.lean\` Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`;
- \`zeta23/Zeta23/ExplicitFormula.lean\` Git blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`;
- \`zeta23/Zeta23/GammaFacts/Series.lean\` Git blob \`2c6cf90050c2e6d5cbef0745d0445e3a8d02394a\`.

Authenticated original PI branch source:
- root \`lean-toolchain\` Git blob \`664e12dc06fe1ec82414cccb8e8f8e34d33d9f3f\`, v4.34.0;
- root \`lakefile.toml\` Git blob \`e567c529fc39eff8a175b3361a2831763e5dcc2c\`, requiring Mathlib tag v4.34.0;
- true PI007, PI008 and PI014 imported source Git blobs in \`docs/PI015_DUAL_SOURCE_LOCK.json\`.

The **distinct Git commits and Lean compiler versions are genuine**, not merely a spelling difference between a tag and a commit. They do **not** imply different mathematical Fourier definitions or invalidate accepted source results in independently pinned branches. A direct \`.olean\` import between these compiler ecosystems has NOT been established.

## 2. Two real, separate Lean theorem targets: do NOT counterfeit source imports

### 2a. Original upstream Lean environment

\`compat/pi015/PI015ExternalPaperFT.lean\` imports **the real upstream \`Zeta23.Defs\`**, not a substitute \`namespace Zeta23\` defined inside Weil-Lab. It is designed to be compiled in a checkout of the exact upstream \`zeta23/\` subproject using the original Lean v4.33.0-rc2 and Mathlib commit. It proposes:

\[
\boxed{
\texttt{Zeta23.paperFT}\ f\ z=
\int_\mathbb R f(u)\operatorname{Complex.exp}(i z u)\,du.
}
\tag{PI015-upstream-definition}
\]

Two no-sorry Lean candidate theorems unfold the imported \`paperFT\` at complex and real frequencies. These are deliberately source-exact \`rfl\` obligations. Once independently compiled, they certify only the actual source definition and positive forward Fourier sign, not any PI007 kernel nor the archimedean inverse transform.

### 2b. Weil-Lab local Lean v4.34.0 environment

\`WeilDefect/Arithmetic/PI015FiniteGammaSymbolBridge.lean\` imports **actual** local \`PI008FiniteDigammaSymbol\` and \`PI014KernelCharacterBridge\`. Define the finite harmonic sum
\[
H_N=\sum_{n<N}\frac1{n+1}.
\]
From the authentic PI008 finite symbol
\[
\Omega_N(r)=
-\gamma-\log\pi+
\sum_{n<N}\left(\frac1{n+1}-
\frac{n+1/4}{(n+1/4)^2+(r/2)^2}\right)
\]
and the PI014 *local-model* Fourier comparison, the exact finite algebra is
\[
\boxed{\Omega_N(r)=H_N-\gamma-\log\pi-\mathcal F_{+,{\rm local}}K_N(r).}
\tag{PI015-local-symbol}
\]
The new source-typed Lean **candidates** are:
- \`pi015FiniteHarmonic_zero\` and \`pi015FiniteHarmonic_succ\`;
- \`pi015FiniteSymbol_split\`: literal PI008 real multiplier equals harmonic minus gamma/logpi minus rational sum;
- \`pi015FiniteSymbol_eq_localFourier\`: same identity embedded in ℂ, with actual PI014 local finite transform;
- \`pi015FiniteSymbol_scalar\`: multiplication by an arbitrary complex scalar does not discard the harmonic/gamma/logπ contribution.

All five names have \`#print axioms\`. **None is yet kernel accepted.** Multiplication by a scalar alone is *not* the missing \(h(0)\) inverse-Fourier pairing.

## 3. Exact symbolic preflight: no floating-point or erased contacts

\`scripts/pi015_finite_symbol_preflight.py\` checks the finite multiplier with exact \`fractions.Fraction\` for N=0..100 and seven signed rational frequencies. It represents the transcendental constants in a **formal three-coordinate basis** (1, EulerGamma, log(pi)), so neither constant can cancel accidentally.

Independent equivalent execution:
- **707** exact finite-symbol cases PASS;
- **2,828** scalar-contact coefficient instances (four h0 choices per frequency) PASS;
- the N=0 symbol remains **−EulerGamma−log(pi)**, even though there are no finite Fourier atoms.

These are algebraic checks. They do not prove source-correct inverse Fourier integration or diagonal trace extension.

## 4. Source-lock and CI contract; do not invent one Lean environment

\`docs/PI015_DUAL_SOURCE_LOCK.json\` fixes the root upstream Git commit, full source Git blob SHA, BOTH actual Lean/Mathlib versions and Git tag resolutions.

\`scripts/pi015_dual_source_lean_audit.py\` fails closed unless:
- actual input source bytes match those **exact** Git blobs;
- the local \`.lake/packages/mathlib\` git HEAD is the **exact** resolved v4.34.0 tag SHA;
- in upstream mode the upstream root checkout SHA is the pinned commit, upstream source and manifest bytes match, and its \`.lake/packages/mathlib\` HEAD equals **51e6992…**;
- actual direct Lean source evaluation produced the complete expected five (local) or two (upstream) named \`#print axioms\` receipts;
- nonempty compiled \`.olean\` exists and only \`propext\`, \`Classical.choice\`, \`Quot.sound\` are used;
- source commit and \`.olean\` SHA256 are recorded.

\`.github/workflows/pi015-dual-toolchain-zeta23-source.yml\` provides **two independent jobs**, one building the real upstream Zeta23.Defs with Lean 4.33.0-rc2 and one building the local PI015 finite symbol with Lean 4.34.0. The workflow is **manual-only** to avoid adding more automatically queued heavyweight jobs while PI009–PI013 pending CI remains unresolved.

**Dispatch limitation:** GitHub's workflow_dispatch may require a workflow to already exist on the default branch. Do not claim PI015 CI ran, or that it can be dispatched directly from an unmerged draft PR, until GitHub actually accepts a dispatch and reports a completed run with artifacts. Even **both** job PASS results certify distinct source facts, not an imported cross-toolchain theorem.

## 5. Important obstruction: two separate receipts are not a bridge

The following inference is invalid:

> "The local model has the same printed integrand as upstream paperFT, and both projects compile independently; therefore PI007's K_N is already an actual imported Zeta23.paperFT theorem in the Weil-Lab proof environment."

To close the actual external-source gate, the original Zeta23 source and PI007/PI008/PI014 declarations must be **co-resident in one fully pinned compatible Lean environment**, with compiled common imports and a genuine theorem. This may be achieved through a controlled port with exact source-diff receipts, or through a carefully version-reconciled companion; it may not be achieved by copying a theorem's name or pretending the existing cross-version \`.olean\` objects can be shared.

This is a testable **source-admissibility gate**. Its failure would falsify a claimed formal transport, not the classical finite Fourier identity.

## 6. PI016 next and unconditional limitations

1. Recover real PI009–PI014 direct compiler results; repair specific Lean errors on the existing candidates before enlarging the CI queue. Keep numerical NF, extension IV, and spectral CP independent.
2. After the compiler backlog, actually build the two pinned PI015 environments with logs, source/blob hashes and strict axioms.
3. Choose and verify a single common source graph for the authentic Zeta23 \`paperFT\` and the literal PI007/PI008 kernel or provide an exact audited port; do not infer this from two separate toolchains.
4. Only then formalize the finite inverse pairing for compact smooth h with **the full contact coefficient**
\[
A_N(h)=\big(H_N-\gamma-\log\pi\big)h(0)-
\int_\mathbb R h(u)K_N(u)\,du,
\]
with exact inverse factor \(1/(2\pi)\). For nonzero diagonal h, dropping the harmonic contact term is mathematically false.
5. Once the finite pairing and PI007 physical/PI008 frequency tails are Lean accepted, attach to the actual original IV011 \`neutralIV011OriginalMixedArch\` in a **separate IV-based PI companion**, preserving source SHA and strict axiom custody.
6. Independently determine whether Masullo's nuclear trace operator has the same excluded-diagonal contact extension. PI006's orthogonal/disjoint-support information-loss obstruction remains; the signed Weil global positivity and RH/GRH are still OPEN.

**PI015 falsifiable result:** the upstream/source toolchain mismatch is an exact two-version fact, and a source-locked dual-build path is specified without conflating algebraic dictionary, Lean import or spectral operator equivalence.
