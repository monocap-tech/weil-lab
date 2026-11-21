# PI011 — Assemble the source-positive whole-line Fourier atom from actual Mathlib integrals

**Lane:** PI### Potential Interface. Stacked PI010 → PI009 #820 → PI008 #818 → PI007 #816 → PI006 #812 → PI005 #809 → PI004 #804 → PI003 #801 → PI002 #798 → PI001 #793. The PI registry is GitHub issue #792. **NF### numerical/Lean custody, IV### Phase IV support-extension Lean work, and CP### finite-compression compatibility work remain untouched.**

**Status:** mathematically complete decomposition and directly specified, no-sorry Lean theorem *candidates* for the actual whole-real-line source-positive Fourier exponential. **No CI/olean/axiom PASS is claimed until new direct-target Actions receipts have completed.** Rational complex simplification and the full original IV011 Gamma inverse transform remain separate open Lean theorems. Neither Masullo's operator trace nor diagonal positivity has been proved.

## 1. Actual source audit

The PI010 parent branch contains \`WeilDefect/Arithmetic/PI010FourierHalflineAtom.lean\`, invoking the **real pinned Mathlib v4.34.0** theorems:
- \`integrableOn_exp_mul_complex_Ioi\`, \`integral_exp_mul_complex_Ioi\` on positive half-lines for complex exponent with negative real part;
- \`integrableOn_exp_mul_complex_Iic\`, \`integral_exp_mul_complex_Iic\` on negative half-lines for complex exponent with positive real part.

Primary Mathlib source:
https://github.com/leanprover-community/mathlib4/blob/v4.34.0/Mathlib/Analysis/SpecialFunctions/ImproperIntegrals.lean

PI011 additionally located the **exact existing integral decomposition**
\[
\texttt{integral\_Iic\_add\_Ioi}
\]
in:
https://github.com/leanprover-community/mathlib4/blob/v4.34.0/Mathlib/MeasureTheory/Integral/IntervalIntegral/Basic.lean

Its genuine hypothesis is integrability of the same function on \((-\infty,b]\) and \((b,\infty)\); it then states
\[
\int_{(-\infty,b]}f+\int_{(b,\infty)}f=\int_{\mathbb R}f.
\]
This is the specific missing compiler-level *assembly lemma* from PI010. It is not a guessed measure-theoretic equality.

Original Fourier convention remains \(\exp(+iru)\):
- \`Zeta23.paperFT\` upstream \`Zeta23/Defs.lean\`, blob \`8024700cbfefb54d763b487afa84c03fef58a550\`.
- Original \`Zeta23.EF.gammaBracket\` upstream \`Zeta23/ExplicitFormula.lean\`, blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`.
- Authentic original IV011 mixed source blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\` lives on the **separate IV source stack**, not on PI's branch.

## 2. Exact full-line mathematical identity

For \(\alpha>0\) and \(r\in\mathbb R\), put
\[
z_+ =-\alpha+ir,\qquad z_-=\alpha+ir,
\qquad
F_{\alpha,r}(u)=e^{-\alpha|u|+iru}.
\]
For \(u>0\), \(F=e^{z_+u}\); for \(u\le0\), \(F=e^{z_-u}\). Each half is absolutely integrable by \(\Re z_+<0,\ \Re z_->0\). The actual pinned Mathlib half-line results give
\[
\begin{aligned}
I_+ &= \int_{(0,\infty)} e^{z_+u}\,du=-1/z_+=1/(\alpha-ir),\\
I_- &= \int_{(-\infty,0]} e^{z_-u}\,du=1/z_-=1/(\alpha+ir).
\end{aligned}
\]

The source \`integral_Iic_add_Ioi\`, together with a pointwise piecewise identity at \(u=0\), yields
\[
\boxed{
\int_\mathbb R F_{\alpha,r}(u)\,du
=-\frac1{-\alpha+ir}+\frac1{\alpha+ir}.
}
\tag{PI011-full}
\]
The remaining simple *complex rational* calculation is
\[
-\frac1{-\alpha+ir}+\frac1{\alpha+ir}
=\boxed{\frac{2\alpha}{\alpha^2+r^2}}.
\tag{PI011-rational}
\]
The denominator is strictly positive because \(\alpha>0\), so no singularity arises. At \(\alpha=2n+\frac12\) it reproduces PI008's true rational digamma atom
\[
\frac{2\alpha}{\alpha^2+r^2}
=\frac{n+1/4}{(n+1/4)^2+(r/2)^2}.
\]
This is an **analytical identity**, not a PI011 Lean acceptance report. The PI010 independent Fraction preflight checked that rational algebra at 768 parameter pairs; exact mathematics is not the same as kernel acceptance.

## 3. New true-target Lean candidate module

\`WeilDefect/Arithmetic/PI011WholeLineFourierAtom.lean\` imports the actual \`WeilDefect.Arithmetic.PI010FourierHalflineAtom\` source module and \`Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic\`. Its named candidate declarations are:

1. \`pi011Piecewise_integrableOn_Iic\`: genuine integrability inherited from the pinned Mathlib complex negative-half-line theorem.
2. \`pi011Piecewise_integrableOn_Ioi\`: genuine integrability inherited from the pinned Mathlib positive-half-line theorem.
3. \`pi011Piecewise_whole_integral\`: genuine whole-line integral assembled via \`integral_Iic_add_Ioi\` and both exact PI010 half-line evaluations.
4. \`pi011Physical_eq_piecewise\`: identifies the **single physical** \(e^{-\alpha|u|+iru}\) kernel with the two formulas, including at \(u=0\).
5. \`pi011Physical_whole_integral\`: transfers the whole-real-line integral to the authentic damped source-positive physical kernel, yielding the sum of two complex fractions.

All five have \`#print axioms\`. None has \`sorry\`, a project axiom, an unproved equality to a rational digamma atom, or an unverified import of IV011. **Compiler status is pending; any tactic/elaboration failure must be repaired on the actual source before designation PASS.**

## 4. CI and strict axiom custody

New \`.github/workflows/pi011-wholeline-atom-lean.yml\`:
- uses only the pinned Lean 4.34.0 and Mathlib 4.34.0;
- builds **both actual targets** \`WeilDefect.Arithmetic.PI010FourierHalflineAtom\` and \`WeilDefect.Arithmetic.PI011WholeLineFourierAtom\`;
- requires nonempty original \`.olean\` files for both;
- invokes direct \`lake env lean\` for PI010 and PI011 source, not merely generic historical tests;
- runs PI010's prior fail-closed compiler/axiom audit and PI011's new \`scripts/pi011_strict_wholeline_lean_audit.py\`, requiring the exact five names and only \`propext\`, \`Classical.choice\`, and \`Quot.sound\`;
- records actual checked-out commit and both imported dependency/source blob IDs and \`.olean\` SHA256 hashes; uploads source identity, build logs, axiom logs and objects on failure or success.

A queue entry is not a compiler receipt. Even a successful generic Lean CI cannot substitute for this exact module coverage. If a compiler error appears, PI012 must repair it without fudging theorem statements or labeling an unverified candidate kernel accepted.

## 5. Specific remaining proof and projection gates

**PI012 first:** recover actual PI009/PI010/PI011 Actions conclusions and logs, repair any Lean errors and prove (PI011-rational) with complex denominator nonvanishing; attach a genuine compiled theorem
\[
\int_\mathbb R e^{-\alpha|u|+iru}\,du=\frac{2\alpha}{\alpha^2+r^2}
\]
and source-normalized PI008 rational atom equality. Only a genuine \`.olean\` and accepted axiom audit count.

**PI013 next:** for smooth compact h, formalize the *finite* Fourier inversion against each atom and check the \(1/(2\pi)\) factor and sign. The exact PI007 physical kernel and PI008 frequency-tail arguments supply analytical proofs; Lean transport has not passed.

**Separate IV-based PI companion:** bind the formal finite and limiting identities into literal \`neutralIV011OriginalMixedArch\`, using IV source SHA and the genuine physical Schwartz correlation, without changing NF/IV compilation/certification agendas.

**Spectral/diagonal stop line:** Masullo's global trace theorem and its operator extension to \(h(0)\neq0\) remain unverified. PI006 proved that orthogonal mixed-test agreements cannot determine a full positive Hermitian form without a separately fixed contact/mass normalization. Source-matching Gamma atoms alone do not resolve that obstruction, prove RH or provide full Weil positivity.

**PI011 conclusion:** genuine pinned formal ingredients for the whole-line *integral* have been attached as new Lean candidates, with dedicated fail-closed acceptance infrastructure. No current PI011 Lean PASS is asserted.
