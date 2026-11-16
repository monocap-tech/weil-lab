# NF535 — Original two-collar C² smooth test to genuine physical L², a.e. and complete-zeta EF

**2026-11-15 PT · branch research/nf535-repair-multiplicity-bridge-and-smooth-ae · draft PR #563.**
Original NF494 U400 source SHA256 remains \`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181\`. No original U400 replay, no new 242 moment selection, no fake zero enumeration. All authentic multiplicity copies persist.

## 1. Actual NF533 compiler failure and repair

Focused NF533 Actions #43807515763 completed **FAILURE**, and its *first new* failing module was \`ActualZetaSmoothLiteralFormulaAutomatic.lean\` line 25. The code \`convert hEF using 1\` tried to prove that the repository zero-point type \`NeutralActualZetaZeroPoint\` was literally equal to the \`Zeta23\` carrier subtype. Their equivalence was already proved as \`neutralActualZetaLiteraturePointEquiv\`, and equality of the index types is not the correct proof obligation.

NF535 correctly pushes the summability assertion through \`neutralActualZetaLiteraturePointEquiv.summable_iff\`, creating a source-indexed \`Summable\` theorem *before* any \`convert\` on the summand. The remaining comparison uses the already-proved exact actual multiplicity and ordinate dictionaries. This is an index transport correction; none of the zeta zeros, multiplicities or normalizations is changed.

**This NF535 patch is a candidate until the focused CI succeeds**. The previously compiled NF529 bounded source-graph closure and NF532 generic physical-window zero-side literal EF (with explicit C² and summability hypotheses) remain certified from past successful focused runs.

## 2. New actual L² construction for STRICT ORIGINAL two-collar smooth tests

The actual \(B=11/10,\delta=1/500\) physical support subset is introduced directly as
\[
E=(-B,-B+\delta)\cup(B-\delta,B)\subset[-B,B].
\]
This is the *same* original endpoint geometry of NF523/NF527; the definition contains no redefined U400 physical source.

For **any** \(\psi\in C_c^2(\mathbb R)\) satisfying \(\psi(x)=0\) for \(x\notin E\), the new Lean module \`ActualZetaOriginalCollarSmoothL2.lean\` proves at the source level that there EXISTS \(g\in RealComplexL2\) with
\[
(1_{[-B,B]})\,g=_{\mathrm{a.e.}}\psi .
\]
Construction: \(\psi\) is in \(\mathrm{MemLp}(\psi,2,\mathrm{volume})\) by \`Continuous.memLp_of_hasCompactSupport\); form \`g=MemLp.toLp ψ\`; use the genuine \`MemLp.coeFn_toLp\` a.e.-identity and the strict support-in-window implication. Crucially, this **does not** assert the arbitrary chosen representative of \(g\) is pointwise C². No Green span or abstract source synthesis is used.

The next statement composes this exact a.e.-source identification with NF534's \`neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond\` and NF533's \`neutralActualZetaWindowCorrelation_literature_of_contDiff\`. Once all targeted modules compile, for that *same* \(g\), and **every** physical \(f\in L²\):
\[
\sum_{q\in\mathcal D_\zeta}
\overline{F_f(\overline{z_q})}F_g(z_q)
=\operatorname{Zeta23.EF.literatureRHS}(C_{f,g}).
\]
The zero-divisor sum carries all genuine integer multiplicities. The right side retains the imported gamma, actual primes and two pole terms. No additional independent divisor absolute-summability hypothesis survives if NF533 compiles.

This is an **existential physical smooth-test formula**, not the original singular endpoint vector. It does not yet give the uniform NF527 one-tenth coercivity inequality or show graph convergence of the full original \(\ell_U\).

## 3. Focused compiler acceptance gates

The dedicated \`.github/workflows/nf529-source-graph-closure.yml\` has been extended to compile, in order:
1. \`ActualZetaSourceQuadraticClosure\` (prior Lean PASS);
2. \`ActualZetaSmoothLiteralFormula\` (prior Lean PASS);
3. \`ActualZetaSmoothLiteralFormulaAutomatic\` (NF533 failed, NF535 repaired, PENDING);
4. \`ActualZetaSmoothCorrelationRegularity\` (NF534 a.e. regularity, PENDING);
5. \`ActualZetaOriginalCollarSmoothL2\` (**new NF535**, PENDING).

The check also scans all five target source files for unsupported Lean \`sorry\`, \`admit\` or \`axiom\`. At the time of this note the new focused pull-request workflow was **QUEUED**; there is NO accepted compile receipt for items 3–5. In particular, do not label the original collar admissibility compiler-certified at this stage unless the actual GitHub check later succeeds.

## 4. Remaining critical path

- Verify and, if necessary, repair the NF535 exact Lean compiler output, including the two earlier NF534 regularity lemmas.
- Formalize the NF527 **full true archimedean digamma lower**, actual \(n=9\) prime-only support term and both poles to derive \(Q(f)\ge\frac1{10}\|f\|_{L²}²\) for each genuine strict smooth two-collar test. This remains ANALYTIC.
- Prove on the full actual Hilbert source graph (not only constructed Green packets) that the *same* physical-test zero-side sum coincides with the normalized P/N quadratic. This generalization remains OPEN; avoid assuming it from the Green-only theorem.
- Formalize NF524/NF528 original \(\ell_U\) source graph convergence and original nonzero margin, and pass the compiled closure theorem to its exact-original physical carrier. ANALYTIC.
- The original exact-242-moment collar correction is a separate provenance claim (NF528), not a prerequisite for positivity of one carrier.

**NF535 disposition: substantive authentic L² test embedding and exact source-index repair, formal CI PENDING.** No assertion of a new RH or global W_ODD_NEG theorem.
