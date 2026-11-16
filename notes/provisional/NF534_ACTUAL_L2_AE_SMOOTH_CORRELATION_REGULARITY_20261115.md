# NF534 — True compact smooth correlation from an a.e. physical L² representative

**2026-11-15 PT. FORMAL PROOF SOURCE COMMITTED; DEDICATED LEAN CI OPEN.** The original NF494 U400 checksum is unchanged (\`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181\`), the genuine 242 selected moments are unchanged, and every authentic zeta multiplicity copy remains included. No original source coefficient replay, signed original source numerical acceptance, RH or W_ODD_NEG claim.

## New proof target and why the naive smoothness proof is insufficient

The genuine Weil-Lab physical correlation is defined on \`RealComplexL2\`, *not* on an independently invented smooth-test type:
\[
W_a f=(1_{[-a,a]})f,\qquad C_{f,g}(t)=\int_\mathbb R W_a g(s)\overline{W_a f(s-t)}\,ds .
\]
The canonical L² representative is only a.e. defined. Even when a physical test originates in \(C_c^\infty\), pointwise \(\operatorname{ContDiff} \,W_a g\) does NOT follow from smoothness of an a.e.-equal test function. A theorem demanding pointwise smoothness of the arbitrary canonical representative would leave a genuine transfer gap.

NF534 first proves the exact real-bilinear convolution identity in the existing physical coordinates:
\[
C_{f,g}= W_a g\star_{\mathbb R} (t\mapsto\overline{W_a f(-t)}).
\]
The reflected first window has compact support, and its integrability follows from the actual L² compact-window estimate. No Green synthesis or zero approximation is involved.

**The main NEW theorem candidate** is:
\[
\begin{gathered}
\psi\in C_c^2(\mathbb R),\quad
W_a g=_{\rm a.e.}\psi,\quad f,g\in L^2
\\
\Longrightarrow C_{f,g}\in C^2(\mathbb R).
\end{gathered}
\]
Importantly, only **one** input needs an a.e.-equal compact smooth representative, and the *other* is arbitrary L². Proof uses Mathlib \`convolution_congr\` for the a.e.-equal second window, followed by \`HasCompactSupport.contDiff_convolution_left\`. This is a.e.-invariant and does not smuggle pointwise smoothness into an L² quotient.

Given the NF533 automatically summable multiplicity-correct direct explicit-formula lemma, the formal target then yields
\[
\sum_{q\in\mathcal D_\zeta}
\overline{F_f(\overline{z_q})}F_g(z_q)
=
Zeta23.EF.literatureRHS(C_{f,g})
\]
under exactly the hypotheses above. Both poles, the genuine prime sum and the complete gamma bracket are preserved. The only newly needed test input is \(\psi\in C_c^2\) with the genuine physical-window a.e. identification. The old separate all-copy divisor-summability assumption is removed by NF533 **if its own Lean compilation passes**.

## Exact Lean modules and gates

New \`WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean\` contains:

1. \`neutralWindowCorrelation_eq_realBilinearConvolution\`: the actual window correlation written as a real-bilinear convolution (not an invented smooth scalar).
2. \`neutralWindowReflectedRepresentative_hasCompactSupport\`: uniform compact support of the reflected first L² window.
3. \`neutralWindowCorrelation_contDiff_of_windowRepresentative_contDiff\`: a stronger pointwise representative criterion, retained only as an auxiliary.
4. **\`neutralWindowCorrelation_contDiff_of_ae_smoothSecond\`**: the a.e.-invariant true-L² smooth representative criterion described above.
5. **\`neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond\`**: direct application of true-zero, all-multiplicity literal EF via NF533.

A dedicated Lake CI now builds this new module after NF533. No new \`sorry\`, \`axiom\` or \`admit\` is intentionally added. **At the time of this note, NF533 and NF534 focused checks are still pending, so none of the new theorems 4–5 is claimed Lean-certified.** NF532 had already compiled the generic EF with explicit regularity and summability hypotheses and NF529 had compiled the full graph closure transfer.

## Remaining obligations to reach the ORIGINAL \(\ell_U\) carrier sign

- **NF533**: automatic exact-multiplicity divisor summability under C² (written; compilation pending).
- **NF534**: genuine correlation C² via an a.e. smooth second window (written; compilation pending).
- **NF535 candidate**: construct actual \`RealComplexL2\` class from strict \(\psi\in C_c^\infty(E)\) and prove \(W_a g =_{\rm a.e.}\psi\); this is the required source-exact smooth-test embedding, with no arbitrary representative pointwise assumption.
- **NF527**: compile the two-collar true gamma/digamma + n=9 prime + pole support-only \(Q\ge(1/10)\|\cdot\|_2^2\). Still analytic.
- **NF524/NF528**: compile full all-copy two-source graph approximation of the exact original endpoint-log \(\ell_U\) and original nonzero premise. Still analytic.
- Global odd/even positivity, Green density, W_ODD_NEG and RH: OPEN.

**NF535 priority**: inspect the actual NF533/NF534 CI compiler logs and repair, then prove the concrete strict smooth collar test's a.e. L² window identification. Do not conflate a.e. and pointwise smoothness.