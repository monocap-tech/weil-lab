# Weil-Lab — UOI039: odd prime-power cycles and a uniform signed margin on arbitrarily large sparse supports

**Status:** New **analytic** proposition and exact rational arithmetic audit, **not Lean kernel certified**. No changes to GitHub, compiler lanes, NF gate registry, or source declarations. In particular, this is *not* a monotone support-extension theorem, full-support positivity, independent spectral equivalence, or RH.

## Source alignment and provenance

Pinned original research source: `monocap-tech/weil-lab` at `614ba879f7389fdb620c474adaee273b00eac71c`.

- `WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean`, blob `0034976fe2f1e5fa9d411108736160542eb94293`, **defines** `Zeta23.EF.literatureRHS k = pole - prime + archimedean` in the original convention. Its `EF_lit` zero-side assertion is a **hypothesis field**, not a mathematical theorem to infer from the definition.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean`, blob `21e2efc93cbaf7f227b81d9fd9784613c0a2905d`, supplies the compiled-source *old-NF543-collar-specific* `neutralNF600SmoothWeil_split`. We do **not** claim it proves the widened identity for the new supports.
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`, blob `eacb18946673c62f9c39bf02bccf01f3f2cff06e`, contains the general complex-Schwartz signed Gamma inequality
  `Gamma(f) >= (11/10)||f||² - (67/10) ∫_{-5}^{5} |fhat(ξ)|² dξ`, with mathlib's Fourier sign `exp(-2πi ξx)`.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean`, blob `5ed0be00fdfefe2f0b21223858c36e3870cda5f7`, fixes the genuine **full** prime term `P(f)=Σ_{n≥2} [Λ(n)/√n](C_f(log n)+C_f(-log n))`, with first-slot-conjugated correlation.
- `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean`, blob `f2ce89e5e020f09de54d1864da928bd99a841cbd`, fixes the two pole moments `m_±(f)=∫f(x)e^{±x/2}dx` and the Hermitian mixed pole form.
- Analytic predecessor UOI038, local file `UOI038_local_pole_cancellation_fourier_flatness.md`, studied just two tiny symmetric collars, their separate moment annihilators, and the compressed two-vertex prime operator.

The new proposition works directly with the *literal finite-support expression*

`W_lit(f) := Gamma(f) - Re P(f) + Re Q(f)`, with `Q(f)=conj(m_-(f))m_+(f)+conj(m_+(f))m_-(f)`.

Its exact identification with `Zeta23.EF.literatureRHS (neutralWindowCorrelation ... f f)` **for the growing supports constructed below** is an uncompiled formal transfer obligation. It does not assert the zero-side Weil criterion, a full native form equality, or RH.

## 1. Sparse new-support collars at unbounded radii

Set `t=log8`, and for every integer `m>=2`, let

`delta_m = 1 / (1000 * 8^(m-2))`,

`c_j = (j+1/2)*t` for `0<=j<m`,

`I_j = (c_j-delta_m,c_j+delta_m)`, `D_m = union_{j=0}^{m-1} I_j`.

The intervals are disjoint. They all lie in `(1, infinity)` because `t/2>1+1/1000`; for an exact verification, the series `log2=2(1/3+(1/3)^3/3+...)` yields `log2>56/81`, hence `t/2=(3/2)log2>28/27>1001/1000`. Thus they do not occupy the original support `[-1,1]`. Their rightmost endpoint increases without bound with `m`. The total measure is

`|D_m|=2m delta_m <= 1/250`.

The last inequality follows from `m<=2*8^(m-2)` for every `m>=2`, proved by induction. Note **the supports are not nested**: `delta_m` shrinks with `m`. Thus this is a family of arbitrarily large *support radii*, not positivity transported along inclusions `D_m ⊆ D_(m+1)`.

Define one-collar closed subspaces

`K_j = {u ∈ L²(I_j; C): ∫_{I_j}u=0, ∫_{I_j}u(x)e^{x/2}dx=0, ∫_{I_j}u(x)e^{-x/2}dx=0}`

and `K_m = K_0 ⊕ ... ⊕ K_(m-1) ⊂ L²(D_m)`.

All three linear functionals exist continuously, and `K_j` is infinite-dimensional (indeed codimension three, since `1,e^{x/2},e^{-x/2}` are linearly independent on an open interval). Translation carries the same local constraints between collars; in particular the isometric identifications of the collars identify `K_m` with `K_base^m`. The subspace contains infinitely many compactly supported complex Schwartz tests. One explicit generator on any interval is

`u = d/dx (d²/dx² - 1/4) eta`, `eta ∈ C_c^∞(I_j)`;

all three moments vanish by integration by parts. The differential operator is injective on compactly supported smooth functions, so these witnesses span an infinite-dimensional subspace. Since each pole moment vanishes on each collar, `Q(f,g)=0` for **every** `f∈K_m` and every test `g` on the full form domain, not only on the diagonal.

## 2. Exact prime arithmetic: an entire weighted Toeplitz graph

Let `r=1/sqrt8`, and for integers `d>=1`, `kappa_d=Lambda(8^d)/sqrt(8^d)=(log2)r^d`. These are the genuine von Mangoldt coefficients: `8^d=2^(3d)` is a prime power, and `Lambda(8^d)=log2`.

For two different collars `I_j,I_k`, the possible positive differences `x-y` lie within `2delta_m` of `|j-k|t=log(8^|j-k|)`. No `log n` for an integer `n>=2` other than `n=8^|j-k|` can lie in that range. A uniform separation proof is:

- For any integer `q>=8`, the closest other integer log to `log q` differs by at least `log(1+1/q)`; the lower neighbor is farther.
- For `1<=d<=m-1`, `log(1+8^(-d)) >= [8/9] * 8^(-(m-1))` (use `log(1+x)>=x/(1+x)`, `x<=1/8`).
- But `2delta_m = [16/1000]*8^(-(m-1))`, strictly smaller. Within a single collar `2delta_m<=1/500<log2`, so no `n>=2` contributes on a diagonal block.

Therefore, under `L²(D_m) ≅ L²((-delta_m,delta_m))^m` by translation, the **compressed full literal prime quadratic operator** (not the half-weight UOI035 operator) is exactly

`A_m ⊗ I`, where `(A_m)_(jk) = 0` if `j=k`, and `(A_m)_(jk)=(log2)r^|j-k|` if `j ≠ k`.

In particular `P(f)=<f,(A_m ⊗ I) f>` with conjugate-first inner product, so there is **no missing factor two**: each unordered edge appears twice in the real correlation sum. UOI035's half-weight physical operator would be `A_m/2` after this compression. The subspace `K_m` is invariant under `A_m ⊗ I` because all collar-local annihilation constraints are preserved by translation.

A simple row-sum (Schur) bound, uniform in `m`, is

`||A_m|| <= 2 (log2) ∑_{d>=1} r^d = 2(log2) r/(1-r) = 2 log2/(sqrt8-1) ≈ 0.758189562142.`

An exact rational upper certificate uses `log2 < 139/200` (positive fourth-order Taylor lower bound for `exp(139/200)>2`) and `sqrt8 > 707/250` (because `(707/250)^2<8`). Thus `r<250/707`, whence

`||A_m|| < 2*(139/200)*(250/457) = 695/914 ≈ 0.760393873085`.

This is independent of the number of collars.

## 3. A genuine odd cycle at three collars destroys chirality

For `m=2`, the compressed literal prime matrix is `[[0,kappa_1],[kappa_1,0]]` and has eigenvalues `±kappa_1`, reproducing the two-collar phase symmetry (with a factor-two adjustment relative to UOI035's half-weight shell).

For `m=3`, however,

`A_3 = [[0,kappa_1,kappa_2],[kappa_1,0,kappa_1],[kappa_2,kappa_1,0]]`.

The edges `0↔1` and `1↔2` come from the genuine `n=8` prime power; the closing edge `0↔2` comes from the genuine `n=64` prime power. All three edges are nonzero. They form an **odd triangle**, not a bipartite graph. The exact invariant is

`trace(A_3^3)=6*kappa_1^2*kappa_2 >0`, and `det(A_3)=2*kappa_1^2*kappa_2 >0`.

Consequently the `3×3` prime matrix cannot have a spectrum symmetric about zero. Its three eigenvalues are exactly

`-kappa_2`, and `(kappa_2 ± sqrt(kappa_2²+8*kappa_1²))/2`.

The associated operator `A_3 ⊗ I_(K_base)` has each of these eigenvalues with infinite multiplicity, so it too lacks any global sign-reversing unitary involution. **This is not a contradiction of UOI035**: UOI035 established chirality for the *new shell between radii 1 and 6/5*; here we consider a much larger support and the **entire original prime contribution** after compression. Two-collar chirality is not preserved as new arithmetic edges enter.

## 4. Gamma domination survives the odd cycle — uniformly in collar count

Let `f∈K_m ∩ C_c^∞(D_m; C)` and `M=||f||²_2`. The zero *ordinary* integral on each collar permits the subtraction `e^{-2πi ξ(x-c_j)}-1` from each local Fourier integral. For `|ξ|<=5`, `|q|=|2πξ|<32`, and all real `y`,

`|e^{-iqy}-1| <= |q||y| <= 32 delta_m`.

Summing all collars and applying Cauchy–Schwarz over their **total** measure gives

`sup_{|ξ|<=5} |fhat(ξ)| <= (32 delta_m) sqrt(2m delta_m) ||f||₂`, hence

`∫_{-5}^{5}|fhat(ξ)|²dξ <= 20m delta_m (32 delta_m)² M`

`<= (20/500)*(32/1000)² M = (16/390625) M`.

Apply the original **signed** Gamma lower bound, the exact pole annihilation and the prime norm bound:

`Gamma(f) >= [11/10 - (67/10)*(16/390625)] M`

`|Re P(f)| <= ||A_m|| M < (695/914) M`

`Re Q(f) = 0`.

Therefore the original *literal signed expression* satisfies the **uniform, all-m, infinite-dimensional** estimate

`W_lit(f) >= [11/10 - 695/914 - 536/1953125] M`

`= (302880048/892578125) M > (1/3) M`.

In particular,

**For every `m>=2`, every smooth test in `K_m` has `W_lit(f) >= (1/3)||f||²`, despite support radii tending to infinity and a non-bipartite arithmetic prime interaction graph already at `m=3`.**

The constants are deliberately conservative. Imposing three ordinary local moments `∫(x-c_j)^k f=0` for `k=0,1,2`, as well as both pole moments, improves the Fourier band bound to

`∫_{-5}^{5}|fhat|² <= 20m delta_m (32 delta_m)^6/(3!)² * M`, permitting the lower estimate to approach `11/10 - ||A_m||` as local moment order grows. All these higher-order local nullspaces remain infinite-dimensional, but become **more restricted**, not less.

## 5. What this does and does not transfer

The genuine, coordinate-independent observations are: the Hermitian pole radical, the spectrum of each *fully specified compressed prime form*, the nonzero three-cycle odd spectral moment on the finite collar index, and the complete literal signed margin on the specified form domain. The *locations and shapes* of the collars, the local ordinary-moment filtration, and the collar identification underlying `A_m⊗I` are additional structure.

**Falsifiable compatibility test:** A cross-projection model claiming to preserve the literal prime operator on the three-collar domain must reproduce the non-bipartite triangle and its asymmetric prime spectrum. A target insisting on spectral `±` symmetry of every prime compression already fails at `m=3`. Reproducing the prime graph alone does not supply the signed Gamma lower bound or the pole/source/native transfer.

**Crucial limits:**

1. The growing regions `D_m` are **not nested**, so the uniform `1/3` margin is **not** a positive extension theorem for all vectors of an expanding support domain. It is a uniform positive *sparse-family* result at unbounded radii.
2. Each `K_m` is finite-codimensional in `L²(D_m)` (three constraints per collar), so these results do not sign the complementary directions, where negative interactions may occur.
3. We have shown analytically the literal `Gamma - Prime + Pole` expression; direct **Lean formalization** of the general literal correlation-to-full-source identity on these new supports remains open. Nor does this identify the entire native source domain.
4. The zero-side explicit formula and global Weil positivity/RH do not follow; they require their own missing source and admissibility hypotheses.

## 6. Next small formalization obligations (do not start a heavy CI job here)

- **UOI030 compiler result is now available:** Actions run `44953767601` completed SUCCESS. Direct `lake build WeilDefect.Research.UOI030CorrelationFourierFactorization` succeeded, the job checked for a nonempty `.olean`, and `lake env lean` reported only `[propext, Classical.choice, Quot.sound]` for its two named theorems. These are **UOI030** compiler receipts, not UOI039 certification; a separate independent artifact archive review is still required before any formal promotion. Avoid overlapping new heavy jobs.
- Prove the general `Zeta23.EF.literatureRHS` decomposition for a compact smooth `f` on **arbitrary** support (rather than invoke old-NF543-only `neutralNF600SmoothWeil_split`). Keep original prime coefficient, Gamma normalization and pole cross terms.
- In pinned Lean, define the three local linear functionals and show they annihilate `D(D²-1/4)η` by source-matched integration by parts; prove support and translation laws.
- Prove the spacing lemma for `log n` against the `8`-power ladder, the exact compressed Toeplitz prime form and its Schur bound. Establish the three-vertex cycle by `trace(A₃³)>0` **without** assuming an existing chiral involution.
- Apply the existing general signed Gamma theorem and the one-moment low-band estimate. Run direct Lean kernel compile, verify `.olean` and all named axioms before claiming any new formal result.

**Independent arithmetic companion:** `check_uoi039.py`, using Python's exact `Fraction` for all inequality budgets. Numerical finite examples are sanity checks only. No GitHub or CI task was launched.