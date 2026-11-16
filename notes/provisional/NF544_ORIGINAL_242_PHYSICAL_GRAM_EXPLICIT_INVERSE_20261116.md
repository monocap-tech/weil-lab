# NF544 — Construct finite 242-column Gram inverse in the exact original physical logarithmic carrier

**2026-11-16 PT, draft stacked on NF543 #571. Compiler acceptance pending.** Original NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, original selected 242 moment directions (including the sinh-pole mode), `B=11/10`, `δ=1/500`, full actual divisor multiplicity and the original physical (L²) source unchanged. No RH claim; no main merge.

## 1. Compiler custody from NF542/NF543

NF540 quadratic Fourier-moment admission PASS at [#43891499088](https://github.com/monocap-tech/weil-lab/actions/runs/43891499088), NF541 derivative-witness bridge PASS at [#43891499147](https://github.com/monocap-tech/weil-lab/actions/runs/43891499147). NF542 prior run [#43891501533](https://github.com/monocap-tech/weil-lab/actions/runs/43891501533) FAILED at two `ContDiff ℝ ∞` parser locations; NF543 fixed syntax to `ContDiff ℝ ⊤`. Latest NF543-branch NF542/NF543 focused checks had not yet completed at the time of writing. Any further compiler errors must be repaired before promoting NF542, NF543, or NF544.

## 2. Original 242-column weighted Gram reduction

Let (E=(-11/10,-11/10+1/500)\cup(11/10-1/500,11/10)). The mathematical candidate remains the *actual* NF523/NF528 source family (j_0,\ldots,j_{241}), including its genuine sinh-pole direction, and a fixed even nonnegative (χ\in C_c^\infty(E)) positive on a nonempty collar interval. Set (b_j=χj_j\in C_c^\infty(E)), and (M: L²(\mathbb R;\mathbb C)\to\mathbb C^{242}), (M_i(f)=\int \overline{j_i}f). Neither (χ) nor (j_j) is replaced with numerical polynomial controls.

The new Lean module **constructs**, for an explicitly supplied indexed family of Schwartz columns (b_j), the linear synthesis

```
B(c) = ∑_{j : Fin 242} c_j • b_j
G(c) = M (B(c).toLp 2 volume)
```

using the genuine Mathlib `Pi.basisFun` and `Basis.constr` APIs. The entries of `G` are precisely the original physical weighted moments once (M) and (b_j) are instantiated with the authentic data; there is no independent hypothetical inverse operator.

The source-specific Gram positivity gate is stated sharply as

```
∀ c ≠ 0, 0 < Re (∑ i, conj(c_i) * G(c)_i).
```

For the authentic real odd analytic (j_i), the analytic argument is positivity of (\int χ|\sum c_i j_i|²) for nonzero (c): this relies on nontrivial analyticity, independence and positive support of (χ), which are **not yet formalized for the actual (j_i)**. It would be invalid to silently infer this from a six-polynomial control Gram or a different source.

**New finite-dimensional deduction from actual-positive Gram hypothesis:**

```
G positive definite  =>  G injective  =>  G bijective
=> E = LinearEquiv.ofBijective G ...
=> R = B ∘ E.symm
=> M (R d).toLp = d   for every d ∈ ℂ^242.
```

The finite-dimensional injective/surjective implication is an established Mathlib theorem. Support is handled by finite sum of the supplied strictly E-supported columns, so every R d remains in the EXACT same collars.

With this constructed R, the previous NF543 exact-moment log-carrier theorem yields

```
∀ original ell : L² and strict-E Schwartz g,
∃ k : NeutralLogHilbertCarrier (11/10),
  neutralLogPhysical k.val = [g + R(M ell - M[g])]L²
  ∧ M [g + R(M ell - M[g])]L² = M ell.
```

This *eliminates the abstract right-inverse R hypothesis* of NF543. It **does not eliminate** the genuine source-specific Gram positivity, actual selected function construction, (C_c^\infty) original approximant construction, or full true P/N graph convergence hypotheses.

## 3. Lean implementation

New `WeilDefect/Arithmetic/ActualZetaOriginalCollar242GramInverse.lean` contains: exact `Pi.basisFun` indexed 242-bump synthesis; physical Gram endomorphism; Hermitian strict-positivity-to-injectivity lemma; finite-dimensional Gram linear equivalence; explicit right-inverse; proof of the right-inverse equation; finite supported synthesis; strict original collar support of R; and complete conditional original-log-carrier plus exactly all-242-moments entry theorem.

An independent pinned compiler workflow `nf544-original-242-gram-inverse.yml` compiles the entire NF542→NF543→NF544 dependency chain and rejects proof placeholders. **All NF544 Lean source is pending actual compiler acceptance**.

## 4. Required source-specific promotion steps

1. Implement original `j_i` including sinh pole as actual functions in Lean; certify real analyticity and linear independence of this **exact** 242-dimensional family on every nonempty strict collar interval, not merely in the larger aperture.
2. Construct the genuine even smooth supported (χ) and (b_j=χj_j); verify Schwartz membership and exact E support.
3. Identify the physical complex-linear `M_i(f)` with the source's actual 242 selected (L²) moment functionals; prove `G` is exactly (\int χ\,\overline{j_i}j_j).
4. Establish `Re ∑ \overline c_i (Gc)_i >0` from original analytic independence and the positive mass region.
5. Attach actual NF528 (g_s), complete all-multiplicity true divisor (P/N) graph convergence and finite-rank correction continuity.
6. Discharge NF527 genuine gamma+prime n=9+both poles uniform 1/10 coercivity in Lean, NF539 full original signed graph formula. W_ODD_NEG and RH remain OPEN.

**Disposition:** The *formal inverse construction* now follows from one explicitly isolated source-specific Gram-positivity premise, instead of an assumed right inverse. Without proving that premise for the original 242 (j_i), this is not yet an unconditional source-specific certificate or an RH sign proof.
