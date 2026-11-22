# Weil-Lab — UOI037: the intrinsic pole radical, explicit pole-neutral prime witnesses, and stronger local Weil margin

**Status, 2026-11-21:** Analytic theorem and exact-rational consistency checks only. No new Lean kernel compilation, no new numerical HD/A gate acceptance, no PR/workflow/CI action, and no claim of full-space original Weil positivity or RH. Historical HD/A frontier stays **708/968**.

## Source custody and meanings

The exact original source is `monocap-tech/weil-lab` commit `614ba879f7389fdb620c474adaee273b00eac71c`.

- `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean`, blob `f2ce89e5e020f09de54d1864da928bd99a841cbd`, defines the *linear* window moments `sourceWindowMoment a (±1/2)` and the Hermitian crossed source pole form `conj(m_-(f)) m_+(g)+conj(m_+(f))m_-(g)`.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean`, blob `21e2efc93cbaf7f227b81d9fd9784613c0a2905d`, proves `neutralNF600SmoothWeil_split` with the source sign `Gamma - Re Prime + Re Pole` **for the special old NF543 collars only**. Its exact *literal algebraic expansion* applies analytically to our newly supported correlations, but that wider Lean identity is **not compiled**.
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`, blob `eacb18946673c62f9c39bf02bccf01f3f2cff06e`, states the signed Gamma inequality for arbitrary Schwartz tests, using high-frequency lower `11/10`, global lower `-28/5`, and band `[-5,5]`.
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean`, blob `5ed0be00fdfefe2f0b21223858c36e3870cda5f7`, fixes the *complete* von Mangoldt contribution with both `±log n` correlations; and `WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean`, blob `d5aa1095b2fe64933ad8db64732d232631d3d3b7`, fixes the first-slot-conjugated convention.
- Parent local analytical note `UOI036_microcollar_full_weil_coercivity.md` supplies the exact microcollar geometry and general (non-pole-neutral) lower `W(f) ≥ (4/5 - log2/sqrt8) ||f||²` with a conservative pole penalty. The present note cancels that penalty **exactly** on a canonical subspace.

## 1. The pole radical is exactly a codimension-two intrinsic subspace

Write `t=log 8`, `δ=1/1000`, and

\[
I_-=(-t/2-\delta,-t/2+\delta),\quad
I_+=(t/2-\delta,t/2+\delta),\quad D=I_-\cup I_+.
\]

The intervals are disjoint, contained in `(-11/10,-1) ∪ (1,11/10)`, hence also in the extension from radius `1` to `6/5`. Let

\[
V=C_c^\infty(D;\mathbb C),\qquad
m_\pm(f)=\int_{\mathbb R} f(x)e^{\pm x/2}\,dx.
\]

Define the **original crossed pole form**, with the source's conjugate-first convention:

\[
p(f,g)=\overline{m_-(f)}m_+(g)+\overline{m_+(f)}m_-(g).
\]

Then:

1. The complex-linear map `M: V → C²`, `M(f)=(m_-(f),m_+(f))`, is **surjective**. Indeed, take nonnegative nonzero real smooth bumps `u` and `v` respectively supported in `I_-` and `I_+`. Their moments `m_-(u), m_-(v)` are strictly positive, and
   `m_+(h)/m_-(h)` is a weighted average of `e^x` with weight `h(x)e^{-x/2}`. Since every `x` of `supp u` is strictly smaller than every `x` of `supp v`, their ratios differ. Thus their two moment vectors are linearly independent.
2. On `C²`, the pole form has Hermitian matrix `H=[[0,1],[1,0]]`, hence **rank two, signature `(1,1)`** and eigenvalues `+1,-1` in the moment coordinates. Its pullback to `V` has radical

\[
\boxed{\operatorname{Rad}(p)=\ker m_-\cap\ker m_+ =: N,\qquad \operatorname{codim}_{\mathbb C}N=2.}
\]

The quotient form on `V/N` is nondegenerate with signature `(1,1)`. These are **intrinsic form invariants**. The chosen coordinates `m_±` or the literal physical boundary intervals are *not* themselves intrinsic to an arbitrary spectral projection.

*Important distinction:* `p(f,f)=0` is **weaker** than `f∈N`. For example, a nonzero moment vector `(1,i)` has zero diagonal pole quadratic value but is not in the form radical: there exists `g` with `p(f,g)≠0`. The radical requires **all** mixed pairings to vanish.

## 2. Explicit infinite-dimensional pole-neutral bump construction

Take any nonzero real `η∈C_c^∞(I_-)` and define

\[
\boxed{\phi=(\partial_x^2-\tfrac14)\eta.}
\]

For `σ=±1/2`, integrate twice by parts (all boundary terms vanish):

\[
m_\sigma(\phi)=\int e^{\sigma x}(\eta''-\tfrac14\eta)dx
=(\sigma^2-\tfrac14)\int e^{\sigma x}\eta(x)dx=0.
\]

Also `φ≠0`: a compactly supported solution of `η''=η/4` is zero by uniqueness for the initial-value problem outside the support. The differential operator is injective on `C_c^∞(I_-)`, so its image is infinite dimensional. Complex-linear combinations remain pole neutral.

Let `ψ(x)=φ(x-t)` (`t=log 8`). Then `ψ∈C_c^∞(I_+)`, and

\[
m_\sigma(\psi)=e^{\sigma t}m_\sigma(\phi)=0.
\]

For every `β∈C` define `f_β=φ+βψ`. **Both original pole moments vanish identically for every phase**:

\[
\boxed{m_\pm(f_\beta)=0,\qquad p(f_\beta,g)=0\quad\text{for every }g\in V.}
\]

So `f_β∈N` is in the **mixed-form radical**, not merely the diagonal zero cone.

## 3. Exact prime phase law survives the pole cancellation

Let `J=||φ||₂²>0` and `κ=Λ(8)/√8=log2/√8`. The support difference sets are contained in `(-2δ,2δ)` or neighborhoods of `±t` of halfwidth `2δ`. Since `log2>2δ`, `log(8/7)>2δ`, and `log(9/8)>2δ`, the original complete prime sum has precisely one potentially nonzero term, `n=8`.

For `|β|=1`, `||f_β||₂²=2J`. With the original correlation `C(u)=∫ f(x) overline{f(x-u)} dx`,

\[
C_{f_\beta}(t)=\beta J,\qquad C_{f_\beta}(-t)=\overline\beta J,
\]

and therefore the **entire literal prime term** equals

\[
\boxed{P(f_\beta)=\kappa(C(t)+C(-t))=2\kappa J\operatorname{Re}\beta.}
\]

Thus `β=+1,-1,i` yield **positive, negative, and zero original prime contributions** even though *all* original pole cross terms vanish and the support and L² mass stay fixed. The UOI035 half-weighted physical shell `B` has `⟨fβ,Bfβ⟩=κ J Re β`; the literal prime is **twice** that number.

## 4. Stronger positive **full signed literal** Weil bound on the entire pole radical

For any `f∈N` (`N⊂V`), write `M_f=||f||₂²`. The two intervals have total length `4δ`, hence `||f||₁²≤4δM_f`. The Fourier low-band `[-5,5]` has length ten, so

\[
\int_{-5}^{5}|\widehat f(\xi)|^2\,d\xi\le 40\delta M_f.
\]

Using the pinned **signed** Gamma lower bounds,

\[
\Gamma(f)\ge(\tfrac{11}{10}-\tfrac{67}{10}\cdot40\delta)M_f
=(\tfrac{11}{10}-268\delta)M_f.
\]

The genuine prime contribution is bounded by `|P(f)|≤κM_f`, and `p(f,f)=0` **exactly**. Therefore the original literal explicit-formula expression (analytic, as the new-collar source identity awaits Lean generalization) obeys

\[
\boxed{W(f)=\Gamma(f)-\operatorname{Re}P(f)
\ge (\tfrac{11}{10}-268\delta-\kappa)\,||f||_2^2\quad(f\in N).}
\]

At `δ=1/1000`, `11/10−268δ=104/125`, so

\[
\boxed{W(f)\ge(\tfrac{104}{125}-\tfrac{\log2}{\sqrt8})||f||_2^2
\approx 0.58693546413\,||f||_2^2.}
\]

For an **entirely rational certificate**, `exp(7/10) > 1+7/10+(7/10)²/2+(7/10)³/6 = 12013/6000 > 2`, so `log2<7/10`. Also `sqrt8>14/5`, hence `κ< (7/10)/(14/5)=1/4`. It follows that

\[
\boxed{W(f)\ge \tfrac{291}{500}||f||_2^2,\qquad
W(f)>\tfrac{291}{500}||f||_2^2\quad\text{when }f\ne0.}
\]

This is stronger than UOI036's `4/5−κ≈0.554935` margin by **exactly `4/125=0.032`** in the lower-bound budget, because the pole penalty has been removed. This is not a statement about all functions on the enlarged support, let alone unrestricted support.

For variable sufficiently small `δ` respecting the same separation geometry, a sufficient positive range for the pole-neutral subspace is

\[
\delta<(\tfrac{11}{10}-\kappa)/268,
\]

and a sufficient margin of at least `1/2` is `δ≤(3/5−κ)/268`. The specific `δ=1/1000` satisfies both.

## 5. Falsifiable cross-projection dictionary

Let `T:V→V'` be a complex-linear **isomorphism onto its image** into a proposed independent arithmetic/spectral construction. Suppose its target has a Hermitian pole pairing `p'` with

\[
 p'(Tf,Tg)=p(f,g)\quad\text{for all }f,g\in V.
\]

Then necessarily

\[
\boxed{T(N)=\operatorname{Rad}(p'|_{T(V)}),\quad
\operatorname{rank}(p'|_{T(V)})=2,
\quad\operatorname{sig}(p'|_{T(V)})=(1,1).}
\]

Proof: the image-space quotient forms are isomorphic. Thus **the pole radical and its two nondegenerate signature directions** are form-intrinsic, whereas the coordinate pair `(m_-,m_+)`, the support intervals, and the chosen sign involution from UOI035 depend on extra structure. A map preserving only total `W`, or only the prime interaction graph, is **not thereby shown** to preserve `p`. A candidate projection with a positive-semidefinite-only pole pairing on `T(V)`, or a pole pairing with trivial radical, fails the stated componentwise compatibility test.

**Exact support-extension stability of the moment nullspace.** For any window radius `r ≥ 11/10`, the two pinned source moments `sourceWindowMoment r (±1/2)` of a function supported in `D` equal the full-line moments `m_±`. Consequently, zero extension from the `11/10` window into the `6/5` window preserves `N` and all its pole mixed pairings *exactly*, without any error budget. This is an admissibility statement about the **pole term and compact support**, not the unproved full source-to-native signed-Weil-form transfer.

**Exact support-extension stability of the moment nullspace.** For any window radius `r ≥ 11/10`, the two pinned source moments `sourceWindowMoment r (±1/2)` of a function supported in `D` equal the full-line moments `m_±`. Consequently, zero extension from the `11/10` window into the `6/5` window preserves `N` and all its pole mixed pairings *exactly*, without any error budget. This is an admissibility statement about the **pole term and compact support**, not the unproved full source-to-native signed-Weil-form transfer.

For compatibility with the entire original Weil form one additionally needs the source-to-native literal identity on the relevant full core, support-domain admissibility of `T`, the exact Gamma and prime dictionaries, and preservation of the complete mixed signed form. None has been established here.

## 6. Lean handoff: smallest genuine obligation, not another workflow

1. **First** finish the already running UOI030 real Lean compiler gate. Do not overlap it with an unrelated heavy job.
2. For UOI037, reuse pinned `sourceWindowMoment` and `sourceDomainPoleForm` to show the moment functional of `(D²−1/4)η` vanishes (two integrations by parts). Formalize the support-preserving translation of this cancellation.
3. Prove `m_-`,`m_+` independent on the two microcollars, using positive bumps with disjoint ordered supports; obtain `codim N=2` and radical identity for the **mixed pole pairing**.
4. Generalize `neutralNF600SmoothWeil_split` from **old NF543 collars** to `C_c^∞(D)` while retaining the exact original `Gamma−Prime+Pole` normalization. Verify only `n=8` in the literal von Mangoldt sum and retain `2B` as prime normalization.
5. Apply the already sourced universal Gamma bracket estimates and the exact `vol(D)=4δ` inequality. Publish standard-only Lean/axiom receipts only after real kernel compilation; no premature formal theorem status.

**No universal signed Weil positivity, no independent-projection equivalence, and no RH result follow from this narrow subspace theorem.**