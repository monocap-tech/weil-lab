# PI014 — Literal finite physical kernel × positive paper Fourier character; external Zeta23 import contract

**Distinct PI### Potential Interface lane** on PI013 #828 → PI012 #824 → PI011 #823 → PI010 #821 → PI009 #820 → PI008 #818 → PI007 #816 and PI001–PI006. PI custody registry issue #792. **NF### Phase III, IV### Phase IV and CP### original spectral/compression work are unchanged.**

**Stage:** exact classical identity with local source-typed no-sorry Lean proof candidates, independent Fraction regression PASS, and a **verified external source-dependency mismatch**. **NO PI014 Lean kernel PASS** and no external Zeta23 module imported or compiled. Masullo's operator trace, diagonal contact agreement, global Weil positivity, RH and GRH remain OPEN.

## 1. Exact source reinspection and newly isolated dependency issue

Actual PI branch source:
- Weil-Lab file WeilDefect/Arithmetic/PI007FiniteGammaKernel.lean, \`pi007FiniteGammaKernel N u = ∑ n in range N, Real.exp(-(2*n+1/2)*|u|)\`; Git blob 598fe925b129fcf8eb7d5fd5b94e7849a9e82ef9.
- Weil-Lab file WeilDefect/Arithmetic/PI013FiniteFourierSum.lean, \`pi013FiniteDampedFourier N r u = ∑ n in range N, pi011PhysicalFourierAtom (pi013GammaDamping n) r u\` and a finite Bochner integral candidate \`pi013FiniteFourierIntegral\`; Git blob f483941d92b4b0ec7a4e4be4ad9b471356aac432.
- Weil-Lab file WeilDefect/Arithmetic/PI013GammaAtomCast.lean, exact damping \`pi013GammaDamping n = 2*(n+1/4)\`; blob 016385a2b3bf93e94a515dfe67d1de4401a49cca.

**Authentic upstream**:
https://github.com/anthropics/formal-math/blob/main/zeta23/Zeta23/Defs.lean
Git blob **8024700cbfefb54d763b487afa84c03fef58a550**, literal definition:
\[
\texttt{Zeta23.paperFT f z} := \int_{\mathbb R}f(u)\operatorname{Complex.exp}(i z u)\,du.
\]
In particular the angular Fourier **sign is positive**, with no \(2\pi\) factor on the *forward* transform.

**New dependency audit:** Weil-Lab PI branch's \`lakefile.toml\` (blob e567c529fc39eff8a175b3361a2831763e5dcc2c) declares only Mathlib \`rev = "v4.34.0"\` and **does not declare a package named Zeta23**. The directly probed root module paths \`Zeta23/Defs.lean\`, \`Zeta23/ExplicitFormula.lean\`, \`Zeta23/GammaFacts/Series.lean\`, and \`Zeta23.lean\` were absent in this branch. The external upstream \`zeta23/lakefile.toml\` (Git blob **43d9da33fb523dce999b070df74e7cdd03381e2b**) pins Mathlib \`rev = "51e6992efd06126df61a496bebf8f49482a4e129"\`, not the PI branch's textual \`v4.34.0\`.

**Precise consequence:** the local PI branch cannot truthfully claim \`Zeta23.paperFT\` is an actually imported, compiled source constant **without an explicit dependency resolution** and compiled bridge. The mathlib revisions are textually different; their effective compatibility/commit identity has not been established. This is an *unpaid source-provenance hypothesis*, not a mathematical contradiction, and is not solved by inventing a local definition under the Zeta23 namespace.

Historical original IV011 uses the literal source name \`Zeta23.EF.literatureRHS\`; this PI014 audit does **not** invalidate any independently accepted IV/Lean source certificate or prove what upstream package was compiled in that separate IV lineage. Each relevant branch must produce its own source-manifest custody.

## 2. Source-identical finite physical Fourier identity

Define
\[
\alpha_n=2n+\tfrac12,\quad
K_N(u)=\sum_{n=0}^{N-1}e^{-\alpha_n|u|},\quad
\chi_r(u)=e^{iru}.
\]
For every real r,u and N,
\[
\begin{aligned}
K_N(u)\chi_r(u)
&=\sum_{n<N}e^{-\alpha_n|u|}e^{iru}\\
&=\sum_{n<N}e^{-\alpha_n|u|+iru}\\
&=\operatorname{pi013FiniteDampedFourier}(N,r,u).
\end{aligned}
\tag{PI014-pointwise}
\]
This is exact finite-sum algebra with complex exponential addition and real/complex coercions, not a claim about the external Zeta23 import.

PI013's previous **source-typed finite Bochner integral candidate** then gives the exact classical identity
\[
\boxed{
\underbrace{\int_{\mathbb R}K_N(u)e^{iru}\,du}_{\mathcal F_+K_N(r)}
=\sum_{n<N}\frac{n+1/4}{(n+1/4)^2+(r/2)^2}.
}
\tag{PI014-forward}
\]
There is **no \(1/(2\pi)\)** on the forward transform. The source's inverse normalization remains an independent finite Gamma-pairing obligation.

## 3. New three-theorem Lean pilot, with source boundary preserved

\`WeilDefect/Arithmetic/PI014KernelCharacterBridge.lean\` imports the **actual** local PI007 and PI013 modules, rather than defining replacement data, and proposes:

1. \`pi014PhysicalAtom_factor\`: genuine PI011 exponential = physical real exponential (complex cast) × exact original-positive angular Fourier character.
2. \`pi014FiniteDamped_eq_kernelCharacter\`: finite sum of actual PI011 exponentials = **literal PI007** finite physical kernel (complex cast) times angular character, pointwise.
3. \`pi014PaperFTModel_finite\`: integral of that literal PI007 kernel × literal-formula character equals the PI013 sum of literal PI008 Gamma rational atoms, using \`pi013FiniteFourierIntegral\` for the integral.

**Terminology:** \`pi014PaperFTModel\` is a *local formula comparison*, not the actual imported \`Zeta23.paperFT\`. This name is deliberately outside the Zeta23 namespace; PI014 must not misrepresent an unimported external constant as accepted. All three theorem statements are zero-sorry **compiler candidates**, with no actual PI014 \`.olean\`/axiom receipt at commit time. Failure of any tactic, coercion or imported PI009–PI013 proof is a legitimate formal blocker.

The future external Lean theorem must import the actual Zeta23 source after pin reconciliation, and prove, for all N and r,
\[
\boxed{
\texttt{Zeta23.paperFT}
  \left(\lambda u.\,\uparrow(\texttt{pi007FiniteGammaKernel}\ N\ u)\right)
  (r:\mathbb C)
=\sum_{n<N}\uparrow(\texttt{pi008GammaRationalAtom}\ n\ r).
}
\tag{PI014-external-gate}
\]
Since the external definition applies \(\int f(u)\operatorname{exp}(i(r:\mathbb C)u)\,du\), this would follow by unfolding the **actual imported** \`paperFT\` and applying the accepted local candidate with correct equality of exponential arguments. Until those imports and source SHA pass, (PI014-external-gate) is **OPEN**, even if the local model theorem compiles.

## 4. Audits and falsifiability

- \`scripts/pi014_exact_preflight.py\` independently executed with exact Python Fractions: **1,792** rational frequency atom checks; **56** finite-sum identities; **240** physical kernel checkpoints for square norm q = 4,9,16,25,36,49. **PASS**. These do not prove the complex integrals nor Lean.
- \`scripts/pi014_zeta23_source_gate.py\` optionally ingests authentic raw upstream Defs.lean and lakefile.toml, verifies the **literal Git blob SHA for both**, and checks the exact paperFT definition plus Mathlib revision declarations. It fails closed in \`--require-matched-mathlib\` mode, because the source pins have not been reconciled. **Source bytes were inspected through GitHub tools; the optional local byte-audit execution is NOT presented as run at PR creation.**
- \`scripts/pi014_strict_local_kernel_audit.py\`: on an actually compiled local PI014 module and all eight transitive PI007–PI013 local source objects, demands the exact three \`#print axioms\` records and only \`propext\`, \`Classical.choice\`, \`Quot.sound\`, preserving source blob hashes and physical compiled-object SHA256. Its PASS is explicitly scoped to the *local* comparison and cannot certify external Zeta23 imports.
- Workflow \`.github/workflows/pi014-kernel-character-lean.yml\` is **manual-only** (workflow_dispatch), to avoid further consuming an already backed-up Actions queue. When dispatched it checks the upstream source byte identity, runs the exact rational preflight, builds the actual PI014 target and checks transitive objects and strict axiom receipts. No Actions or Lean PASS is inferred from merely committing this workflow.

## 5. Finite Gamma and contact term remain unpaid

PI013 and PI014 prepare the genuine finite Gamma multiplier identity,
\[
\Omega_N(r)=H_N-\gamma-\log\pi-\mathcal F_+K_N(r).
\]
For compact smooth h, the finite source Gamma pairing is
\[
A_N(h)=\frac1{2\pi}\int_{\mathbb R}\operatorname{paperFT}(h)(r)\Omega_N(r)\,dr
=(H_N-\gamma-\log\pi)h(0)-\int_{\mathbb R}h(u)K_N(u)\,du.
\]
This identity is **classically** obtained with an inverse Fourier \(1/(2\pi)\) and proper Schwartz/integrability/Fubini hypotheses, but **is not a PI014 compiled Lean theorem**. Its harmonic contact term cannot be dropped on a diagonal h(0)>0 test.

To attach its \(N\to\infty\) limit to actual original IV011 \`neutralIV011OriginalMixedArch\`, an explicitly **IV-based** PI companion is required, preserving original physical Schwartz correlations, source SHAs, actual \`.olean\` status and standard-only axiom audits. Nothing in the local finite comparison creates a Masullo spectral operator trace on tests outside \(\varphi(C_\mathbb Q^1)=0\).

## 6. Next PI015 action

1. Recover actual PI009–PI013 direct build failures/completions; repair them based on compiler logs, do not relabel queued Jobs.
2. Independently reconcile the Zeta23 upstream Mathlib pin with the repository source graph, or provide a **separate pinned vendored/import bridge** with exact source SHA, source verification, direct build and standard axioms. The bridge must not rewrite the original \`paperFT\` definition or inflate prior certifications.
3. Once actual Zeta23 import is viable, prove (PI014-external-gate) as a source-named Lean theorem.
4. Formalize finite inverse Fourier pairing with exact \(1/(2\pi)\) and the **nonzero diagonal contact term**, then separate PI007/PI008 tails and original IV011 transport. Independent Masullo diagonal operator normalization remains an additional hypothesis.

**Falsifier:** Any source-exact sign, normalization, import, contact or multiplicity mismatch must be recorded as an explicit failed interface gate. No global Weil positivity, full spectral isometry or RH/GRH follows from this finite projection.
