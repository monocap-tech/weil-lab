# PI010 — Genuine Mathlib complex half-line Fourier-atom pilot and compiler custody

**Independent PI### Potential Interface** continuation of PI009 #820 → PI008 #818 → PI007 #816, with earlier PI001–PI006 retained. PI registry #792. No changes to unrelated NF### Phase III numerical custody, IV### Phase IV source/extension certificates or CP### invariant/compression research.

**Status:** actual pinned Mathlib *library theorems* identified; five new PI010 Lean theorem **candidates** written; independent exact rational algebraic sanity pass (768 parameter pairs); **PI010 compiler/olean/axiom result pending**. The full-real-line Fourier atom remains an explicit proof obligation, not an accepted Lean theorem. No Masullo trace, diagonal operator, positivity or RH claim.

## 1. Compiler ledger: prior PI009 has not cleared

At inspection, the dedicated PI009 GitHub Actions run #44858094682 was **queued**, with its build job #136704899901 also queued. The generic earlier PI007 and PI008 Lean workflow runs #44856739800 and #44857500784 were also **queued**. No actual compiler-accepted object or standard-axiom receipt could be recovered. Do NOT relabel a queued run as Lean PASS.

The PI009 discovery remains essential: generic .github/workflows/lean.yml compiles only the historical WeilDefect.Examples.WeakCriticalFallthrough target and does NOT import the PI007/PI008 pilot modules. PI009 added a dedicated exact two-target workflow. PI010 gives the **new half-line atom module its own dedicated CI** rather than assuming the generic or PI009 checks include it.

## 2. New pinned Mathlib fact: the needed improper integral is already formalized

The repo pins leanprover/lean4:v4.34.0 and mathlib v4.34.0. Inspecting that **exact tag**:

https://github.com/leanprover-community/mathlib4/blob/v4.34.0/Mathlib/Analysis/SpecialFunctions/ImproperIntegrals.lean

The library has:

\[
\begin{aligned}
&\texttt{integral\_exp\_mul\_complex\_Ioi}:
\quad \Re z<0\ \Longrightarrow\
 \int_{(c,\infty)}e^{zu}du=-e^{zc}/z,\\
&\texttt{integral\_exp\_mul\_complex\_Iic}:
\quad \Re z>0\ \Longrightarrow\
 \int_{(-\infty,c]}e^{zu}du=e^{zc}/z.
\end{aligned}
\]

Its neighboring \`integrableOn_exp_mul_complex_Ioi\` and \`integrableOn_exp_mul_complex_Iic\` supply the actual half-line integrability facts. These are **real Mathlib source theorems**, not speculative theorem names or unproved Gamma/Masullo imports.

Define coefficients for \(\alpha>0,\ r\in\mathbb R\),
\[
z_+=-\alpha+ir,\qquad z_-=\alpha+ir.
\]
Then \(\Re z_+<0\), \(\Re z_->0\), and the exact half-line integrals are
\[
\boxed{
I_+(\alpha,r):=\int_0^\infty e^{z_+u}du=\frac1{\alpha-ir},
\qquad
I_-(\alpha,r):=\int_{-\infty}^0 e^{z_-u}du=\frac1{\alpha+ir}.
}
\tag{PI010-halves}
\]

The elementary complex rational identity,
\[
\frac1{\alpha-ir}+\frac1{\alpha+ir}
=\frac{2\alpha}{\alpha^2+r^2},
\tag{PI010-rational}
\]
is valid for every \(\alpha>0\), avoiding poles by \(\alpha^2+r^2>0\). At \(\alpha=2n+\frac12=2(n+\frac14)\), it is *exactly* PI008's genuine finite digamma term:
\[
\frac{2\alpha}{\alpha^2+r^2}
=\frac{n+1/4}{(n+1/4)^2+(r/2)^2}
=\operatorname{pi008GammaRationalAtom}(n,r).
\]
The original Zeta23 paper Fourier transform uses \(e^{+iru}\), **not** the standard negative-sign Fourier convention. This is why z_± have +ir in both halves.

## 3. New actual Lean candidates and precise limits

The file \`WeilDefect/Arithmetic/PI010FourierHalflineAtom.lean\` imports the **real** pinned \`Mathlib.Analysis.SpecialFunctions.ImproperIntegrals\` module and states five named theorems:

- \`pi010PositiveExponent_re\`, \`pi010NegativeExponent_re\`: exact real parts of the two complex coefficients;
- \`pi010PositiveHalflineIntegral\`, \`pi010NegativeHalflineIntegral\`: source-correct actual half-line integrals, each proved by invoking the real Mathlib improper integral theorem with verified real-part sign;
- \`pi010HalflineIntegralPair\`: adds the two actual half-line integrals, without pretending their sum already equals the integral over all ℝ.

All five declarations include \`#print axioms\`. There are no assumed/new project axioms and no sorry in this candidate. **The source was committed, not kernel compiled at the time of drafting.** Only a completed CI run with .olean + exact direct source axiom logs can upgrade their status.

\`.github/workflows/pi010-direct-halfline-lean.yml\` explicitly builds \`WeilDefect.Arithmetic.PI010FourierHalflineAtom\`, requires its nonempty compiled .olean, invokes \`lake env lean\` on the exact source, and runs \`scripts/pi010_strict_halfline_audit.py\`, which fails closed on missing/extra/duplicate axiom records, nonstandard axioms, source mismatches, incomplete proof tokens, wrong pinned Mathlib version or missing object. This CI runs independently of the overloaded NF/IV tracks.

## 4. Independent non-Lean check and what it tests

\`scripts/pi010_halfline_rational_preflight.py\` uses only exact \`Fraction\` arithmetic. For 128 finite levels \(n=0,\dots,127\) and six rational frequency keys, it verifies both reciprocal real/imaginary parts, complete cancellation of imaginary components and the exact equality with PI008's rational atom, **768 parameter pairs PASS**. These checks verify neither complex integral convergence nor the Lean theorem files; those must be obtained from actual source/CI.

## 5. Exact remaining PI011 source-assembly gate

Even if all five pilot lemmas compile, there are three genuine further mathematical/Lean steps:

1. **Whole-real-line splitting and integrability** for the *single* source-positive Fourier kernel
   \[
   u\longmapsto e^{-\alpha|u|}e^{iru}.
   \]
   On u>0 it is \(e^{z_+u}\), and on u≤0 it is \(e^{z_-u}\). Prove the real split \(Iic\,0\cup Ioi\,0=\mathbb R\), a.e. domain identities, and integrability on both halves. Then combine the exact Mathlib half-line lemmas and prove rational simplification (PI010-rational) in Lean:
   \[
   \boxed{\int_{\mathbb R}e^{-\alpha|u|}e^{iru}\,du
   =2\alpha/(\alpha^2+r^2).}
   \]
2. **Genuine finite Fourier-inversion theorem** for compact C∞ h and all n<N, checking the \(1/(2\pi)\) factor, integrability/Fubini, and sign. This closes the PI007 finite arch identity in source Lean, not merely by a list of identities in prose.
3. **Limit and original IV011 source attachment**: formally apply PI008's controlled frequency-tail and PI007's physical-tail to the actual \`neutralIV011OriginalMixedArch\`, whose source lives on the separate IV### stack. This requires a **separate explicitly IV-based PI companion** with pinned source SHAs. Do not pull uncompiled IV statements into the PI-only branch. No independent Masullo operator-trace theorem follows from this dictionary.

**Stop criteria:** any Lean failure or nonstandard axiom is reported as a failed candidate; a completed pilot only certifies its own names, not the full source arch bridge. The central unresolved spectral question remains **Masullo's independent trace/operator contact normalization on the excluded h(0)≠0 diagonal domain**.

## 6. Handoff

**PI011**: first recover the actual PI009 and PI010 direct CI outcomes, repair real failures, then aim for full-real-line Fourier atom and ratio theorem with strict .olean/axiom receipt. Only once the source theorem is accepted should PI012 attempt the finite Gamma inverse and IV011 companion.

No global Weil positivity, GRH/RH, or proof-method equivalence is claimed.
