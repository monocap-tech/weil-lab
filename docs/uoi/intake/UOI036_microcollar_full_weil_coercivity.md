# Weil-Lab — UOI036: exact narrow-collar Gamma compensation for the original signed explicit-formula expression

**Status (2026-11-21):** new **analytic** restricted-support theorem with reproducible rational/numeric checks; **NOT** a new Lean kernel certificate, no new source-domain/native whole-carrier identification, no universal signed Weil positivity, and no RH claim. The original numerical HD/A frontier remains 708/968; no GitHub CI action is submitted by this report.

## Pinned source custody and normalization

Repository `monocap-tech/weil-lab`, source SHA `614ba879f7389fdb620c474adaee273b00eac71c`:

1. `WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean`, blob `21e2efc93cbaf7f227b81d9fd9784613c0a2905d`, theorem `neutralNF600SmoothWeil_split`: for the **previously fixed NF543 collars**, the literal original Weil explicit-formula RHS has the signs **Gamma – Prime + Pole**. Extending the *same literal identity* to the new narrow support through a window-representative lemma is an **uncompiled** proof obligation; the algebraic identity itself is the one used analytically below.
2. `WeilDefect/Arithmetic/ActualZetaOriginalCollarGammaLower.lean`, blob `fbdcffbaa30f0abcf134ed7c515ffc0fbe4e2c07`: `neutralNF599GammaLower`, `neutralNF599GammaHigh` establish the real Gamma bracket bounds at all frequencies and on |ξ|≥5. `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`, blob `eacb18946673c62f9c39bf02bccf01f3f2cff06e`, derives their signed form for arbitrary complex Schwartz inputs (Lean source status must be checked separately).
3. `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean`, blob `5ed0be00fdfefe2f0b21223858c36e3870cda5f7`, defines the literal prime term as **Σ(Λ(n)/√n)(C(log n)+C(−log n))**; `WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean`, blob `d5aa1095b2fe64933ad8db64732d232631d3d3b7`, fixes the conjugated first source slot of `C`.
4. `WeilDefect/Arithmetic/ActualZetaOriginalCollarPoleBound.lean`, blob `2cdf9d321af47f659579b73a3abb10514e500ab2`, and `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean`, blob `f2ce89e5e020f09de54d1864da928bd99a841cbd`, give the two cross-moments `M_±(f)=∫ e^{±x/2} f(x)dx`, and the pole form `conj(M_-) M_+ + conj(M_+) M_-`.
5. `WeilDefect/Morphology/NeutralWeilFrozenExtension.lean`, blob `9499aed94305708e559f2e8acbd63ee086f62c04`, defines the half-weighted physical prime shell `B`; see parent UOI035 report for `SBS=-B` and `B=EBE` at radii `(a,b)=(1,6/5)`.

## Theorem: narrow two-collar full **literal** signed coercivity (analytic)

Put `t=log 8`, `δ=1/1000`, `a=1`, `b=6/5`, and the intermediate evaluation window `b₀=11/10`. Set

\[
 I_-=(-t/2-\delta,-t/2+\delta),\qquad
 I_+=(t/2-\delta,t/2+\delta),\quad D=I_-\cup I_+.
\]

The two intervals are in `(-b₀,-a)` and `(a,b₀)`, respectively (indeed `t/2≈1.03972077084`). Let `f∈C_c^∞(D;ℂ)` and `M=‖f‖²₂`. Evaluate the literal original signed explicit-formula RHS on the exact compact correlation `C_{b₀}(f,f)`, equivalently `C_b(f,f)` because `f` is supported in both windows. Denote this real value by `W(f)`, with the pinned source convention `W=Γ−Re(P)+Re(Q)`.

**Claim:**

\[
\boxed{
 W(f)\ge \left(\frac45-\frac{\log2}{\sqrt8}\right)M
 \ \approx 0.55493546413\,M\ \ge \frac12 M.}
\]

The *coefficient* in the middle is strictly greater than `1/2`, so `W(f)>M/2` when `f≠0`; for `f=0` both sides are zero. Thus the literal RHS is uniformly positive on an **infinite-dimensional complex smooth test subspace contained entirely in the new support complement** `H_{6/5} ⊖ H_1`.

### Proof (all three original terms, including normalization)

**A. Support geometry and physical uncertainty.** Both intervals have length `2δ`, so `vol(D)=4δ=1/250`. Cauchy–Schwarz yields

\[\|f\|_1^2\le (1/250)\|f\|_2^2 = M/250.\]

The full-support window restriction is exact: the physical representative is zero outside `D`, so `C_{b₀}(f,f)=C_b(f,f)=∫ f(x)\overline{f(x-u)}dx` pointwise for every shift `u`. There is **no claim** that all compact physical vectors belong to a completed source-domain carrier.

**B. Genuine signed Gamma lower bound.** Set `ρ(ξ)=|\mathcal F f(ξ)|²`, in the pinned negative-exponent `2π` convention. Plancherel gives `∫ρ=M`, and the unitary Fourier L¹ bound gives

\[
L:=\int_{-5}^5\rho(\xi)d\xi \le 10\|f\|_1² \le M/25.
\]

The pinned Gamma bracket satisfies `γ(ξ)≥−28/5` everywhere and `γ(ξ)≥11/10` for `|ξ|≥5`. Therefore

\[
\Gamma(f)\ge\frac{11}{10}M-\frac{67}{10}L
\ge\Big(\frac{11}{10}-\frac{67}{250}\Big)M
=\boxed{\frac{104}{125}M}.
\]

This uses the **signed**, not absolute-value, original Gamma multiplier. No critical-line or RH assumption is needed for these inequalities.

**C. Both original pole moments.** Since `|x|<11/10` on `D`, `e^{|x|/2}<e^{11/20}<2`. Hence

\[
|M_+(f)|,\ |M_-(f)|\le 2\|f\|_1,
\qquad |Q(f)|=2|\operatorname{Re}(\overline{M_-}M_+)|
\le8\|f\|_1² \le \boxed{\frac4{125}M}.
\]

This is the exact **crossed pole**, not a diagonal-square substitute. As a form of two bounded functionals, it has rank at most two on the compact window; no claim that Gamma is compact follows.

**D. Every genuine von Mangoldt prime interaction.** If the correlation `C(u)` is nonzero, the source points lie either in the same tiny interval, forcing `|u|<2δ`, or in opposite intervals, forcing `||u|-t|<2δ`. For `n≥2`, `log n≥log2>2δ`. Also the nearest integers to 8 are separated by more than `2δ` in logarithmic distance: `log(8/7)>2δ` and `log(9/8)>2δ`. Consequently **all** `n≠8` contributions vanish, even without first restricting to prime powers.

With `c₈=Λ(8)/√8=log2/√8`, and the first input conjugated in the L² inner-product convention,

\[
P(f)=c_8\big(C(t)+C(-t)\big)=2c_8\operatorname{Re}C(t),
\qquad |\operatorname{Re}P(f)|\le c_8 M,
\]

where the last inequality follows by `2|⟨f_-,T_{-t}f_+⟩|≤‖f_-‖²₂+‖f_+‖²₂=M`.

**Normalization warning:** For the physical operator `B` from UOI035, whose shift coefficients are `c_n/2`, **the literal prime contribution is `P(f)=2⟨f,Bf⟩`**, not `⟨f,Bf⟩`. Our margin uses the entire `c₈ M` as worst-case prime loss, so it does **not** undercount the prime term.

**E. Combine the genuine signed pieces.** The explicit-formula algebra gives

\[
W(f)=\Gamma(f)-\operatorname{Re}P(f)+\operatorname{Re}Q(f)
\ge\left(\frac{104}{125}-c_8-\frac4{125}\right)M
=\left(\frac45-c_8\right)M.
\]

For a rationally verifiable strict `>1/2` bound, note `log2<3/4` (because `e^{3/4}>1+3/4+(3/4)^2/2+(3/4)^3/6>2`) and `√8>5/2`. Hence `c₈<(3/4)/(5/2)=3/10`, and `(4/5-c₈)>1/2`. This completes the **analytic** proof. □

## Why this changes the interpretation of UOI035

UOI035 showed that the **isolated** new-prime correction `B` is chiral and indefinite even on new-new vectors. Here, however, the complete literal expression is positive with a substantial *uniform* margin on an infinite-dimensional family of the very same new-collar vectors. These statements are compatible because the signed Gamma multiplier supplies a positive contribution that outweighs the worst-case prime and pole losses.

For a variable sufficiently small halfwidth `δ` satisfying the same strict geometric separation, the same argument yields the **capacity budget**

\[
\boxed{W(f)\ge\left(\frac{11}{10}-c_8-300\delta\right)\|f\|_2^2,\qquad f\in C_c^\infty(D_\delta;\mathbb C).}
\]

A sufficient positive range is `δ < (11/10−c₈)/300≈0.00284978` (plus the wider geometric separation constraints). This is a support-**measure** tax, not merely a radius penalty.

A further compatibility consequence is that the pole correction, being finite-rank, cannot by itself compensate the negative `−2B` direction on an infinite-dimensional matched-pair subspace. A candidate spectral projection that retains only `−2B` plus compact corrections **cannot be unitarily identified with this positive literal form** on the whole microcollar subspace. The full Gamma response or another equally substantive noncompact contribution must be represented. This is a **conditional comparison of model forms**, not an identification of the complete original Schwartz source domain with a bounded `H_b` operator.

## Remaining certification obligations and research direction

1. Formally generalize the pinned `neutralNF600SmoothWeil_split` / `neutralNF600LiteralArch_eq` from the **original NF543 special collars** to **every Schwartz test supported in `D`**, using physical representative equality and the unchanged `literatureRHS` definition. The existing source theorem for the old collars must **not** be misquoted as already proving this new support case.
2. Formalize the exact correlation support restriction and isolate **only `n=8`** in the complete prime sum, explicitly proving the von Mangoldt coefficient `Λ(8)=log2` and its full `2B` normalization.
3. Reuse the pinned universal signed Gamma bracket bounds, the Fourier L¹ estimate for a set of volume `1/250`, and the two original cross-pole moments. Obtain the **exact rational** `104/125`, `4/125`, and final `4/5−c₈` margin, with real compiler transcript and standard-only axioms.
4. Only **after** this literal theorem is proven, ask whether the selected native/cross-projection form preserves this entire positive microcollar **form**, not just the chiral prime shell. This requires a domain-respecting isometry, original full-form identity, and an extension-compatible support filtration; these are **not supplied**.

Local arithmetic check: `UOI036_microcollar_checks.py` (exact `fractions.Fraction` budget checks plus numerical geometry and complex-phase tests). This is **not** Lean, and no CI job or new HD/A gate acceptance is claimed.
