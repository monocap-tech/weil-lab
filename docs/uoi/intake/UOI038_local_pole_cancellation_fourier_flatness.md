# Weil-Lab — UOI038: local pole cancellation forces quadratic Fourier flatness and a stronger full-form margin

**Status (2026-11-21): analytic theorem, rational arithmetic checked, no new Lean compiler success, no GitHub/CI changes, and no statement of full-space Weil positivity or RH.** Historical original HD/A accepted frontier stays **708/968** pending independent updates from the separate NF track. This document advances the analytic UOI037 construction; it is not itself a Lean theorem.

## Original source identity and conventions

Pinned research source: `monocap-tech/weil-lab` commit `614ba879f7389fdb620c474adaee273b00eac71c`.

- `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean` (Git blob `f2ce89e5e020f09de54d1864da928bd99a841cbd`): the two original linear moments `m_±(f) = ∫ f(x)e^{±x/2} dx`; pole crossed Hermitian form `conj(m_-(f))m_+(g)+conj(m_+(f))m_-(g)`.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean` (Git blob `5ed0be00fdfefe2f0b21223858c36e3870cda5f7`): genuine original `P(f) = Σ_{n≥2} Λ(n)/√n [C_f(log n)+C_f(-log n)]`, with first-slot conjugated correlation convention.
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean` (Git blob `eacb18946673c62f9c39bf02bccf01f3f2cff06e`): uniform signed Gamma lower bound `Gamma(f) ≥ (11/10)||f||²-(67/10)∫_{-5}^5 |f̂(ξ)|²dξ` for complex Schwartz input.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean` (Git blob `21e2efc93cbaf7f227b81d9fd9784613c0a2905d`): source sign `W = Gamma − Re P + Re Q` for the *old NF543 collar support only*. Applying this exact literal explicit-formula algebra to the new collars is analytically justified from the definitions but remains an **uncompiled generalization obligation**.
- `WeilDefect/Morphology/NeutralWeilFrozenExtension.lean` (Git blob `9499aed94305708e559f2e8acbd63ee086f62c04`): isolated half-weighted physical prime shell `B = (1/2)Σ_n (Λ(n)/√n)(T_{log n}+T_{−log n})` under projection to the larger window, not the full Weil operator.

Previous local source-grounded analytic notes: UOI035 (new-shell chirality), UOI036 (two narrow-collar full-form estimate), and UOI037 (intrinsic pole radical and the explicit `(D²−1/4)` bump construction).

## 1. Define the *stronger* local pole-neutral subspace

Set `t = log 8`, `δ = 1/1000` and

`I_- = (−t/2−δ, −t/2+δ)`, `I_+ = (t/2−δ, t/2+δ)`, `D = I_- ∪ I_+`.

These tiny intervals are entirely in the new support `[-6/5,6/5] \ [-1,1]` and inside `[-11/10,11/10]`. Let `H_±=L²(I_±;ℂ)` and

`K_±={f∈H_± : ∫_{I_±} f(x)e^{x/2}dx = ∫_{I_±} f(x)e^{−x/2}dx = 0}`,

`K=K_- ⊕ K_+ ⊂ L²(D)`.

Each `K_±` is closed and of complex codimension two in `H_±`, so `K` is infinite-dimensional. **Do not confuse it with UOI037's larger full pole radical** `N = ker m_+∩ker m_-` on `L²(D)`, which has codimension two: here `K⊂N` has codimension four, because *each collar separately* cancels both moments. The stronger cancellation is exactly what permits the improved Fourier estimate.

Explicit witnesses abound: for any `η∈C_c^∞(I_-)`, `(∂²−1/4)η∈K_-` by two integrations by parts; its translate `T_t(∂²−1/4)η∈K_+`. Nonzero `η` gives a nonzero resulting function. These smooth witnesses form an infinite-dimensional subspace `K∩C_c^∞(D)`.

## 2. New theorem — second-order low-frequency cancellation

Use the pinned Fourier convention `f̂(ξ)=∫_ℝ f(x)e^{−2πi ξx}dx`. Fix one of the two collar centers `c=±t/2` and write `f_c(y)=f(c+y)` for `|y|<δ`. Both individual moment identities give

`∫ f_c(y)cosh(y/2)dy = 0`, and `∫ f_c(y)sinh(y/2)dy = 0`.

For any real `q`, introduce the *exact two-moment interpolation remainder*

`R_q(y) = e^{−iqy} − cosh(y/2) + 2iq sinh(y/2)`.

Because the two interpolating terms integrate to zero against `f_c`, the Fourier transform of each collar component satisfies exactly

`f̂_c(ξ) = e^{−2πi ξc} ∫ f_c(y)R_{2πξ}(y)dy`.

There is no approximation in this equality. Its crucial property is

`R_q(0)=R'_q(0)=0`.

Also

`R''_q(y) = −q² e^{−iqy} − (1/4)cosh(y/2) + (iq/2)sinh(y/2)`.

For `|ξ|≤5` we have `|q|≤10π<32`. For `|y|≤δ=1/1000`, elementary bounds `cosh(δ/2)<2` and `sinh(δ/2)<δ` yield

`|R''_q(y)| < 32² + 2/4 + (32/2)δ < 1025`.

Taylor's formula with integral remainder, valid for complex `R_q`, then gives

`|R_q(y)| ≤ (1025/2)y² ≤ (1025/2)δ²`.

Summing both collar integrals and using Cauchy–Schwarz on `D`, whose measure is `4δ`, proves the **uniform, dimension-independent Fourier estimate**

\[
\boxed{\sup_{|\xi|\le5}|\widehat f(\xi)|\le 1025\delta^{5/2}\|f\|_2\quad (f\in K).}
\]

Consequently

\[
\boxed{\int_{-5}^5|\widehat f(\xi)|^2d\xi \le 10\cdot1025^2\delta^5\|f\|_2^2
=\frac{1681}{160000000000}\|f\|_2^2.}
\]

This replaces UOI037's generic estimate `≤40δ||f||²`: for individual pole-neutral collars the low-frequency *mass* is `O(δ^5)`, not `O(δ)`. The statement is analytically valid for all `L²` functions in `K` because each supported collar is also `L¹` and its moments exist; smoothness is needed for the eventual original Schwartz test theorem, not for this Fourier estimate.

The same interpolation is interpretable as **two prescribed complex-frequency zeros** of the entire compact-support transform (at `ξ=±i/(4π)` for this Fourier convention), separately on each collar. Those zeros are coordinate-specific representations of the original pole annihilator; they are not automatically preserved by an arbitrary change of spectral projection.

## 3. Exact compressed prime shell, including its infinite multiplicity

Let `Π_D` project `L²([-6/5,6/5])` onto `L²(D)` by multiplying by `1_D`. Let `κ = Λ(8)/√8 = log2/√8>0`. The only shift that links the two tiny collars is `t=log8`: no same-side nontrivial prime shift intersects a collar, and `|log(9/8)|>2δ`, `|log(11/8)|>2δ` exclude the other first-new-shell terms.

Under the decomposition `L²(D)=H_- ⊕ H_+` and the unitary translation `T:H_-→H_+`, `(Tu)(x)=u(x−t)`, the **compression** of the shell from UOI035 is

\[
\boxed{\Pi_D B\Pi_D=\frac\kappa2
\begin{pmatrix}0&T^{-1}\\T&0\end{pmatrix}.}
\]

This is an identity of operators on `L²(D)`, **not** a claim that the uncompressed `B` has no output outside `D`: the `n=9,11` shifts can produce such output in the full `[-6/5,6/5]` window.

Translation scales each pole moment by `e^{±t/2}`, hence maps `K_-` onto `K_+`; therefore the displayed compressed operator preserves `K`. Its restriction has exact eigenvalues `+κ/2` and `−κ/2`, each of **infinite multiplicity**, via `(u,Tu)` and `(u,−Tu)` with `u∈K_-`. Equivalently, the literal prime quadratic `P=2⟨f,Bf⟩` has eigenvalues `+κ` and `−κ` on this compressed subspace. Pole cancellation does not erase arithmetic phase competition.

## 4. Stronger *full literal* signed Weil margin

For smooth `f∈K∩C_c^∞(D)`, use the unchanged literal source convention

`W(f) = Gamma(f) − Re P(f) + Re Q(f)`.

The pole contribution `Q(f)` is zero **exactly** because both moments vanish. The complete original prime sum on `D` reduces to `n=8` and satisfies `|Re P(f)|≤κ||f||²` with the full original coefficient (not the half-weight `B` coefficient). The pinned signed Gamma inequality and the new low-band estimate give

\[
\begin{aligned}
W(f)&\ge\left(\frac{11}{10}-\kappa -\frac{67}{10}\cdot10\cdot1025^2\delta^5\right)\|f\|_2^2\\
&=\boxed{\left(\frac{11}{10}-\frac{\log2}{\sqrt8}-\frac{112627}{1600000000000}\right)\|f\|_2^2}.
\end{aligned}
\]

The numeric coefficient is approximately **0.854935393741**, as compared with UOI037's `0.58693546413` from a generic L¹ estimate. This is a *subspace-strengthened* lower bound, not an improved bound on all UOI037 full-radical vectors `N`.

There is also an entirely rational lower certificate, with no floating-point dependence. The positive Taylor polynomial of `exp(139/200)` through degree four is greater than two, hence `log2<139/200`; since `(14/5)²<8`, we have `sqrt8>14/5`, so `κ<139/560`. The exact arithmetic inequality

\[
\frac{11}{10}-\frac{139}{560}-\frac{112627}{1600000000000}
=\frac{9539999211611}{11200000000000}>\frac{17}{20}
\]

proves the clean consequence

\[
\boxed{W(f)\ge\frac{17}{20}\|f\|_2^2\quad\text{for all smooth }f\in K.}
\]

For nonzero `f` the sharp inequalities used above actually give `W(f)>(17/20)||f||²`. This is an **infinite-dimensional, phase-sensitive new-support family** where the pole mixed form is identically zero and the entire literal original signed expression is uniformly coercive. It is neither a support-independent result nor global Weil positivity/RH.

## 5. Cross-projection compatibility: a more discriminating test

UOI037 identified the intrinsic pole radical `N` and its rank-two `(1,1)` quotient. UOI038 adds a **filtration-dependent subspace** `K⊂N` where both pole moments vanish in each collar separately, and where an explicitly compressed prime operator has two infinite-multiplicity signs, while the **full** form obeys `W≥0.85||f||²`.

A proposed unitary cross-projection dictionary should therefore specify which of the following it actually preserves:

1. The pole mixed pairing `p` and hence its full radical `N` (intrinsic to the pairing).
2. The two-collar support splitting and the stronger local radical `K` (depends on the support filtration).
3. The source-normalized compressed prime operator and its `±κ/2` spectrum on `K` (requires exact arithmetic interaction, not only an unsigned interaction graph).
4. The complete original signed form `W` and its `17/20` lower margin on `K` (requires Gamma and the literal original source/native bridge, not just pole-plus-prime preservation).

A construction may pass (1) while failing (2)–(4). Thus this is a **falsifiable conditional compatibility dictionary**, not an asserted equivalence between constructions.

## 6. Outstanding formal and mathematical obligations

- First preserve the already-running UOI030 real compiler path; do not create a competing broad CI job for UOI038.
- In Lean, generalize the old-collar-specific literal `Gamma−Prime+Pole` identity to Schwartz functions supported in `D`. The imported old theorem is not a proof for these new collars.
- Prove per-collar vanishing of `sourceWindowMoment` for `(D²−1/4)η`; then formalize the two-moment interpolation lemma and `O(δ⁵)` low-band energy bound using only pinned Mathlib Fourier and Schwartz definitions.
- Prove the projected prime-shell matrix identity on `L²(D)`, preserving `P=2⟨f,Bf⟩`; distinguish it explicitly from a spectral identity for uncompressed `B`.
- Verify exact rational bounds and only claim Lean certification after a direct compiler transcript, `.olean` proof, and standard-only named axiom audit. No new HD/A gates follow from this analytical finding.

**Reproducible independent arithmetic check**: `check_uoi038.py`, using Python standard-library `fractions.Fraction`; it validates constants and geometry and samples the interpolation remainder numerically. The analytic proof above, not sampled data, is the basis of the estimate.
