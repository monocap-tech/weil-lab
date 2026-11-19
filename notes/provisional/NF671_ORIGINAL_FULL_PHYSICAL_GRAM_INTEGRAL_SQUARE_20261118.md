# NF671 — exact original 242-generator physical Gram square, PSD and authentic Schur remainder

## Accepted sources

- NF667 full exact original 15-source physical coercivity at **10^-60**, full original-source Lean PASS and standard-axiom audit, workflow **44455028120**.
- NF668 full source-specific original 15-source physical strict positivity, no-kernel and injectivity, complete Lean PASS and axiom audit, workflow **44457538220**.
- NF669 complete exact original **15+227 index split**, physical A/B/C dictionary, and generic Schur square completion, full Lean PASS and axiom audit, workflow **44459126587** (generic and original-source jobs).
- NF670 full original 242-source quadratic transport and genuine original cross-block Riesz response have been authored; dedicated NF670 workflow **44460719268** was still queued at last inspection. They remain **compiler pending**, and thus all dependent NF671 source theorems also remain pending.

## NF671 new generic integral theorem

`WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramIntegralSquare.lean` defines for any finite continuous real source family `g:Fin n→ℝ→ℝ`:

`IntegralGram(g,a,b)_ij = ∫_(a..b) g_i(t)g_j(t)dt`,

`G_c(t)=Σ_i c_i g_i(t)`.

It proves the exact equality

`Σ_ij IntegralGram_ij c_i c_j = ∫_(a..b) G_c(t)^2 dt`

using finite-sum linearity and interval-integrable continuity, and establishes that the matrix is positive semidefinite whenever `a≤b`. This does not assume source linear independence and does not establish a strictly positive lower eigenvalue bound.

New generic proof candidates are independently tested by the `generic-integral-square-psd` CI job.

## NF671 original 242 physical source attachment

`WeilDefect/Generated/NF671/OriginalPhysicalFullGramPSD.lean` connects the generic identity to the **actual NF606** unweighted interval-integral matrix:

`H_ij = ∫_(−11/10..11/10) j_i(t)j_j(t) dt`.

It proves that all 242 unchanged original selected real generators are continuous (the first 241 authentic oscillators and the unchanged `sinh(t/2)` pole at index 241), identifies the actual H entrywise/definitionally with the generic Gram, and proposes the exact 242-dimensional identity

`Q_H(z)=∫_(−11/10..11/10)(Σ_{i:Fin242} z_i*j_i(t))²dt ≥0`

for **every** real original 242-source coefficient vector. This is genuine physical Gram PSD; no finite numerical interval certificate, approximation or generic nonnegativity hypothesis is substituted.

## NF671 direct original 227-source Schur equality

Using the original A/B/C block and the exact Riesz response from NF670, define the assembled coefficient vector

`z_y := Assemble(−U(y), y) : Fin242→ℝ`.

The proposed theorem `nf671ActualPhysicalSchur_eq_integral_square` identifies the genuine 227-source Schur remainder with an explicit original physical interval integral of the square of the *orthogonalized original source combination*:

`S(y)=Q_C(y)−Q_A(U(y))=Q_H(z_y)=∫_(−11/10..11/10)(Σ_k z_y(k) j_k(t))²dt`.

Hence `S(y)≥0` follows from the elementary square-integral sign, with **no** new C positivity assumption, rounding, full 242 inverse or Schur numerical witness. This also verifies the physical 15+227 block PSD qualitatively and splits the NF670 full square-completion identity into two nonnegative contributions.

This is **not** strict coercivity. Neither `S(y)≥ c‖y‖²` for a known `c>0` nor unique invertibility of full H is asserted. Nor does physical H PSD imply the signed Weil-form positivity or the Riemann hypothesis.

## Certification and scope

The new `.github/workflows/nf671-original-integral-square.yml` runs (1) generic finite continuous Gram interval-square equality + PSD + axiom audit; (2) pinned original NF631/NF632/NF621/NF648 artifact rebuild through the full NF665 15-source certificate and NF669/NF670 actual source bridges, followed by the source-specific full 242 physical square identity, actual 227 Schur exact square equality/nonnegativity, and strict standard-axiom whitelist.

New NF671 statements are **Lean proof candidates until the complete corresponding CI job and standard-axiom audit PASS**. If NF670 upstream fails, NF671 must be repaired only after the exact upstream compiler defect is diagnosed; an imported file cannot be declared valid merely because it exists.

## Next — NF672

Investigate **strict** original 242-source physical Gram nondegeneracy, connecting the already established NF569 real-source global analytic independence (when compiler accepted) to vanishing integral squares on a nonempty interval. This can potentially close qualitative positive definiteness of all 242 original sources, without yet supplying the much stronger **quantitative** coercivity lower bound required by physical solver enclosures. The original 242-generator positivity and global signed Weil positivity are distinct problems.
