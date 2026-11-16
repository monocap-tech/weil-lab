# NF538 — Universal actual full-source quadratic ↔ literal zeta divisor, with Lean compiler repair

**2026-11-15 PT · Draft PR #566 · formal target source committed, focused Lean check PENDING.**

Source custody is unchanged: original NF494 U400 SHA256 \`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181\`; original 242 selected moment identities unchanged; divisor copy index exactly \`NeutralActualZetaDivisorCoordinate = Σ ρ, Fin (mult ρ)\`. No original U400 coefficient replay and no RH, global positivity or W_ODD_NEG assertion.

## I. Precise upstream CI audit and correction

NF535 dedicated run [43810306286](https://github.com/monocap-tech/weil-lab/actions/runs/43810306286) completed **FAILURE**, but the target progression is essential:
- \`lake build WeilDefect.Arithmetic.ActualZetaSourceQuadraticClosure\` **PASS** (previous NF529).
- \`lake build WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormula\` **PASS** (previous NF532).
- \`lake build WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormulaAutomatic\` **PASS** (NF535's corrected zero-index equivalence; fixes NF533's original typed-index failure).
- \`lake build WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity\` **FAILURE** at two actual Lean elaboration errors: (a) \`HasCompactSupport.intro isCompact_Icc\` leaves the compact interval bounds metavariables unsolved; (b) a line-broken leading-dot convolution lemma name is misparsed, \`.contDiff_convolution_right\`.

NF538 repairs both directly in \`WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean\` by specifying \`(K := Set.Icc (-a) a)\` in \`HasCompactSupport.intro\`, and invoking the concrete \`(...).contDiff_convolution_right\`. **Recompile is pending**, so do not claim those two repairs have passed until new CI succeeds. NF535's subsequent original-collar L² module was skipped by the failed workflow.

NF536 and NF537 standalone focused checks were queued at latest inspection. Their new Lean proofs remain unaccepted. To prevent the NF534 smooth branch from blocking the independent universal result, the new NF538 universal module imports ONLY previously compiled source-closure and the now-compiled NF533 automatic divisor EF, and the focused workflow compiles it **before** the outstanding NF534 branch.

## II. Complete original source graph, not Green restricted

The original \`NeutralActualZetaSourceDomain a\` is the closed submodule whose triple \((f,P,N)\) includes \(f\in\mathrm{NeutralLogHilbertCarrier}(a)\) and both complete authentic \(\ell^2\) source sequences. The graph equations are exactly the source pair evaluations at every genuine \(\zeta\) zero copy.

Let \(\phi=\mathrm{neutralLogPhysical}(f)\), \(F(z)=\int_{-a}^a \phi(x)e^{izx}\,dx\), and
\[
  A_q=F(\overline{z_q}),\qquad B_q=F(z_q),\qquad
  P_q=\frac{A_q+B_q}{\sqrt2},\quad
  N_q=\frac{A_q-B_q}{\sqrt2}.
\]
The graph already has \(P,N\in\ell^2(D_\zeta)\). Hence \(A=(P+N)/\sqrt2\) and \(B=(P-N)/\sqrt2\) are **automatically** in \(\ell^2(D_\zeta)\). No extra smoothness or zeta-zero count is used here. The actual all-divisor sum \(\sum_q\overline A_q B_q\) is thus absolutely convergent by Hilbert-space Cauchy–Schwarz for EVERY element of the complete source graph.

The authentic original source normalization is a second \(c=1/\sqrt2\) per channel. The source quadratic is
\[
 Q(f,P,N)=\|cP\|_2^2-\|cN\|_2^2
  =\frac12(\|P\|_2^2-\|N\|_2^2).
\]
Hilbert polarization yields
\[
 \boxed{Q(f,P,N)=\operatorname{Re}\langle A,B\rangle_{\ell^2}
       =\operatorname{Re}\sum_{q\in D_\zeta}\overline{F(\overline{z_q})}F(z_q)} .
\]
This algebra is **universal on the original full source graph**, without requiring oddness, Green synthesis/density or RH. This is a mathematically proven two-by-two identity; the new Lean proof target below must compile to become a formal certificate.

If the *actual* physical correlation \(C_{\phi,\phi}\) is \(C^2\), the imported \`Zeta23.WeilEF.EF_lit_zeta\` and the authentic complex-window correlation transformation give the literal identity
\[
 \boxed{Q(f,P,N)=\operatorname{Re}\mathrm{Zeta23.EF.literatureRHS}(C_{\phi,\phi})} .
\]
The RHS includes both pole contributions, actual primes, gamma/archimedean term. No RH assumption appears, but **C² regularity is a genuine hypothesis** and not asserted for the original singular endpoint carrier.

## III. New Lean source and exact architecture

\`WeilDefect/Arithmetic/ActualZetaFullGraphRawDivisorQuadratic.lean\` includes no \`sorry\`, \`admit\` or \`axiom\`; it is a new **uncompiled theorem candidate** with:

1. The exact complex scalar identity \(\mathrm{neutralActualZetaSourceNormalization}^2=1/2\).
2. The two authentic full-graph inverse raw sample \(\ell^2\) vectors built from the original complete positive/negative source coordinates (not artificial Fourier samples).
3. Coordinatewise equality of both inverses to the actual physical window evaluations \(F(\overline{z_q})\) and \(F(z_q)\), using \`neutralActualZetaSourceAnalysis_sampling\` and \`neutralLogPositivePairSource_inner\` / \`neutralLogNegativePairSource_inner\`.
4. A scalar-independent Hilbert polarization lemma for \(Q=\operatorname{Re}\langle A,B\rangle\).
5. **\`neutralActualZetaSourceQuadratic_fullGraph_rawDivisor\`**, the universal full graph = actual all-divisor mixed sum identity, by \`lp.inner_eq_tsum\`.
6. **\`neutralActualZetaSourceQuadratic_fullGraph_literature_of_contDiff\`**, the genuine imported literal zeta EF on the same full graph vector with physical autocorrelation \`ContDiff ℝ 2\`.

The Lake workflow adds \`lake build WeilDefect.Arithmetic.ActualZetaFullGraphRawDivisorQuadratic\` immediately after the NF533 automatically summable EF, **ahead of** the unresolved NF534 smooth-correlation module and unrelated NF536/NF537 new source files. This isolates the original full graph universal theorem's compiler acceptance from the separate smooth-test pathway.

Focused run for this PR: [NF538 source-graph CI](https://github.com/monocap-tech/weil-lab/actions/runs/43816455341). At note creation it is QUEUED. No universal Lean PASS may be asserted at this point.

## IV. Strict mathematical gates still open

- **NF538 formal universal graph identity:** source written, compiler unverified until CI.
- **NF534 a.e. C² convolution and NF535 original-collar L² embedding:** compiler patches committed NF538, CI pending; NF535 did not compile its dependent original-collar module.
- **Original \(C_c^\infty(E)\) physical test -> logarithmic Hilbert carrier:** an \(L²\) embedding alone is insufficient; weighted Fourier logarithmic energy must be formalized, and an a.e.-representative physical custody theorem supplied.
- **Real odd smooth test Fourier symmetry and raw source ℓ²:** NF536/NF537 candidate route, full Lean compilation pending.
- **NF527 actual two-collar universal gamma / true \(n=9\) prime / pole lower bound \(Q\ge0.1\|\cdot\|_2^2\):** analytically developed, not Lean source-certified.
- **Original NF523/NF524/NF528 exact \(\ell_U\) full two-source graph smoothing/limit and nonzero physical margin:** analytic, uncompiled.
- **Original 242 selected moment Gram/provenance:** separate OPEN, not necessary for the direct one-carrier sign path.
- Full odd/even coercivity, W_ODD_NEG, RH: OPEN.

**NF538 disposition:** universal authentic full-graph zeta identity reduced to a direct standalone Lean target; prior NF533 automatic summability compiler PASS confirmed; NF534 precise diagnostics patched; NF538 dedicated Lean acceptance PENDING. No RH claim.
