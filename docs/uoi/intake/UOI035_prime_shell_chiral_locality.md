# Weil-Lab — UOI035: chiral symmetry and boundary localization of the first extended prime shell

**Status:** new analytic deduction, checked against pinned source definitions; **NOT** a new Lean kernel certificate, and **NOT** a statement of universal signed Weil positivity or RH. No GitHub workflow or research branch is changed by this note.

**Pinned source:** `monocap-tech/weil-lab`, commit `614ba879f7389fdb620c474adaee273b00eac71c`.

- `WeilDefect/Morphology/NeutralWeilFrozenExtension.lean` (Git blob `9499aed94305708e559f2e8acbd63ee086f62c04`) defines `frozenWeilPrimeShell`, `frozenWeilPrimeShellSymbol`, and the physical shell `frozenWeilPrimeShellPhysical` with symmetric translations and coefficient `compactWindowPrimeCoefficient n / 2`.
- `WeilDefect/Morphology/NeutralWeilPrimeShellTranslation.lean` (Git blob `628f979cb0e7b33d22c1a1144ae9e5c25560d257`) contains the Fourier-character/cosine identity and exact weak Schwartz pairing of the Fourier multiplier with the physical translation shell; this source statement is **not** a full source/native original signed-Weil-form identification.
- `WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean` (Git blob `d5aa1095b2fe64933ad8db64732d232631d3d3b7`) defines the mixed physical correlation `C_a(f,g;t)` with the **first slot conjugated**, so the associated Hilbert form must retain the same slot convention.

## 1. Setup: first new shell of the support extension

Fix `a = 1`, `b = 6/5`, the Hilbert space `H_b = L²([-b,b]; ℂ)` (functions zero-extended to the line), and the exact shell `N = {8, 9, 11}`. Write `t_n = log n` and `c_n = Λ(n)/√n > 0` for `n∈N`, matching the pinned physical coefficients. Define the bounded self-adjoint *isolated new-prime operator*

\[
 (Bf)(x) = {\bf1}_{[-b,b]}(x)\sum_{n\in N}\frac{c_n}{2}\left[f(x-t_n)+f(x+t_n)\right].
\]

Each compressed translation has norm at most one, so

\[
 \|B\|\le K=\sum_{n\in N} c_n,\qquad
 t_{\min}=\log8\approx 2.07944154168 > b=1.2,
 \quad t_{\max}=\log11\approx 2.3978952728<2b=2.4.
\]

This is the *prime-shell correction* only, not the full operator for the pole, Gamma, and prime contributions of the original signed form.

## 2. Exact chiral anticommutation

Define the sign involution `S` on `H_b` by `(Sf)(x)=sgn(x) f(x)` (the value at zero is immaterial in L²). Then `S²=I` and `S*=S`.

**Theorem (analytic).** `SBS = -B`.

**Proof.** If both `x` and `x-t_n` lie in `[-b,b]`, then

\[
 x\ge t_n-b>0,\qquad x-t_n\le b-t_n<0.
\]

Therefore they have opposite signs. Likewise, if both `x` and `x+t_n` lie in the window, then `x<0<x+t_n`. Multiplication by `sgn(x)` at the output and `sgn(x\pm t_n)` at the input introduces a factor `-1` for every nonvanishing shifted term, giving `S B S=-B`. This holds almost everywhere, as required for L². ∎

**Consequences:** `spec(B)=-spec(B)` because conjugation by the unitary involution `S` preserves the spectrum. In particular, a nonzero `B` has positive and negative spectral directions. With the orthogonal splitting into negative and positive half-windows, `B` has the purely off-diagonal form

\[
 B=\begin{pmatrix}0&T^*\\ T&0\end{pmatrix},
\]

not a positive diagonal graph Laplacian. `S` itself depends on the chosen central split, but **existence of an anticommuting unitary involution and central spectral symmetry** are preserved by unitary equivalence.

## 3. Exact boundary localization and sharper edge norm

Put

\[
 r=t_{\min}-b=\log8-\tfrac65\approx0.87944154168,
 \quad E={\bf1}_{[-b,-r]\cup[r,b]}.
\]

If `|x|<r`, then `|x\pm t_n|>b` for all `n∈N`; hence `(Bf)(x)=0`. Because `B` is self-adjoint, it also annihilates every input supported in `[-r,r]` (up to measure-zero endpoints). Thus **exactly**

\[
 \boxed{B=EBE},\qquad
 |\langle f,Bg\rangle|\le K\|Ef\|_2\|Eg\|_2.
\]

The new shell is blind to the entire central core, not merely to old-old pairings. It only measures energy in the two end strips of the larger window. Note that `r< a=1`, so these strips include both the outer part of the old window and the newly acquired support collars.

## 4. Nonzero positive/negative witnesses **entirely in the new collars**

Let `t=log8`, `δ=1/100`. The intervals

\[
 I_- = (-t/2-\delta,-t/2+\delta),\qquad I_+=I_-+t
\]

lie strictly within `(-6/5,-1)` and `(1,6/5)`, respectively, because `1+δ<t/2<6/5-δ`. Also `2δ<log(9/8)`, so no prime shifts of 9 or 11 can connect these narrow intervals.

Choose any nonzero **real** `φ∈C_c^∞(I_-)`, and `ψ(x)=φ(x-t)`, with `J=||φ||²₂>0`. Both `φ` and `ψ` vanish on the entire old window `[-1,1]`. Set `h_β=φ+βψ` for `|β|=1`. There is no overlap except the precise `n=8` cross-translation. Direct expansion with the first slot conjugated yields

\[
 \boxed{\langle h_\beta,Bh_\beta\rangle = c_8J\operatorname{Re}\beta},
 \quad c_8=\frac{\log2}{\sqrt8}>0,
 \quad \|h_\beta\|_2^2=2J.
\]

Consequently `h_+`, `h_-`, and `h_i` yield strictly positive, strictly negative, and zero prime-shell quadratic values, **all within the new complement** `H_b\ominus H_a`. In fact,

\[
 \sup\operatorname{spec}(B)\ge c_8/2\approx0.1225322679,\quad
 \inf\operatorname{spec}(B)\le -c_8/2.
\]

This is stronger than merely saying `P_a B P_a=0` or bounding leakage from old vectors: `Q_a B Q_a` itself has both signs, where `Q_a=I-P_a`.

## 5. Implication for extension positivity and cross-projection comparisons

Any complete support-extension argument must control the new-new block of the **entire signed operator**, not only the old-old compression and old-new mixed leakage. The isolated prime shell contributes an indefinite block on the new collars; the original pole/Gamma/other terms may compensate, but that requires an independent quantitative theorem. None follows from `P_a B P_a=0`.

**Falsifiable compatibility test.** If an independent arithmetic or spectral candidate `B'` is claimed to represent this *isolated* physical prime shell by a genuine unitary intertwiner `U`, it must satisfy `B'=UBU*`. Necessarily it is nonzero, has centrally symmetric spectrum, has positive and negative quadratic directions, and supports an anticommuting involution `S'=USU*`. A nonzero positive-semidefinite-only proposal for `B'` therefore cannot be unitarily equivalent to this shell. Preserving the *localized edge projector* `E` is a stronger assertion requiring `U E U*=E'`; without a matching support filtration on the other side, the coordinate edge bound cannot simply be declared intrinsic.

**Boundaries / unpaid hypotheses:** This tests only an explicitly defined finite physical translation shell. It does **not** prove the entire original signed Schwartz Weil form equals the native bounded operator on all of `H_b`. That full domain/core identification, all additional Gamma/pole terms, support-independent positivity, and RH remain open. The analytic proofs above have **not** been translated to Lean or kernel-audited, and no new numerical gates are promoted.
