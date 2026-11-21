# PI024 — The missing archimedean spectral term is a full Gamma pole ladder, not a single boundary zero

**Weil-Lab PI### Potential Interface | ANALYTIC-ONLY | 2026-11-20.**
Parent: \`research/pi023-analytic-canonical-haar-and-boundary-pole-obstruction\`.
PI registry: #792. **No pull request, Lean module, Actions workflow or compiler run.**
NF remains the compiler-active certification lane; IV/CP/PI are analytic-first.

## 1. Source verdict and corrected page custody

Directly reopened and inspected **page images**, not only previous PI summaries, of Alessandro Maria Masullo, *The Music of the Primes*, 940-page public manuscript released November 20, 2026:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

The external independent formalization \`mccorvie/riemann-masullo/paper/README.md\` records an **unmodified release mirror** with SHA256 \`e039d3f6cf0a4b14f03c7edb85097752dd65c0a2fe543c76fe992be234f97bf5\`. This digest is attested for the mirror; we did **not** independently hash the current WordPress download bytes. The accessible WordPress primary remains the same 940-page November edition in the inspected sections. A search of Vakil's announcement and primary manuscript references identified **no authenticated, dated author erratum or corrected Chapter 13 manuscript**. This is a limited search result, not a claim that no private revision exists. Do not silently incorporate a hypothesized editorial fix.

Primary page receipts, with PDF zero-index in parentheses:
- **p.123 (122), Proposition 3.2.1.3 and equation (3.2.1.4)**: defines the **completed** idelic Hecke \(L(s,\chi)\), with \(\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\), as distinguished from the finite Euler \(L_f(s,\chi)\). It has simple poles at \(s=0,1\) on the trivial-character component and zeros only in the **open** critical strip \(0<\Re s<1\). The functional equation has a nowhere-vanishing factor; negative-even *finite* zeta trivial zeros are canceled by Gamma poles.
- **p.124 (123), Definition 3.2.1.4**: separately names the finite \(L_f\), whose trivial zero divisor is not the completed \(L\) zero divisor.
- **p.370 (369), §7.4.3**: explicitly says the reciprocal archimedean Gamma factor has zeros at the trivial zeros of \(L_f\) with matching multiplicities. This independently confirms the completed/finite divisor distinction already implicit in Chapter 3.
- **p.519 (518), Theorem 12.5.1.1**: the full completed \(L(c)\) zero sum over \(\Omega(C_F)_I=\{c:\sigma(c)\in1/2+I\}\), with real canonical conversion \(1/2\), complex \(1/(2\pi)\), and finite \(\log q_v/\mu_v(O_v^\times)\). For \(F=\mathbb Q\) the zero arguments are among the zeros of the completed \(\Lambda(s)\); taking a narrower strip can omit zeros but cannot add boundary/trivial zeros.
- **p.520 (519), proof (12.5.1.4)**: explicitly introduces \(I=[-\alpha,\alpha]\) and writes the geometric kernel trace as the completed \(L(c)\) zero sum on that strip. \(\alpha\) is a strip parameter; no extra zero at \(s=0\) is introduced by this notation.
- **p.522 (521), Theorem 13.3.1.1**: a critical-line-only, multiplicity-capped \(\min(N(c),[F:\mathbb Q])\) sum, with bare real/complex PV integrals and \(\log q_v\) finite factors. The surrounding chapter contains unfilled proof references; the full-divisor-to-capped-critical-line step remains unauthenticated.
- **p.619 (618) and p.620 (619), Appendix B.4.3–B.4.4**: the source emphasizes canonical \(d\mu_{\rm can}=d\mu_v/2\) at a real place, \(d\mu_v/(2\pi)\) at a complex place, and the finite unit-volume conversion; footnote 16 explicitly asks to recheck factors of \(2\) and \(2\pi\). The local PV definition is relative to the displayed \(d\mu_v\), with no seen Chapter-13-only redefinition.
- **CORRECTION TO PI023 CUSTODY:** Theorem **B.4.4.7** and equation (B.4.4.16) are on **printed p.623, PDF index 622**, NOT p.624. The latter contains proof material and remarks. Page 623's own footnote 24 says the right side should be double-checked, so this appendix display is source evidence for the author's normalization, not an independently verified theorem.

The original first-party announcement dated November 20 says the draft was released for checking while corrections were being incorporated. The external \`mccorvie/riemann-masullo\` formalization's README and ERRATA document ongoing prerequisite work and no completed verification of Chapter 12/13; its early-paper errata are NOT a validated correction of these trace formulas.

## 2. The source divisor has NO boundary or trivial zero at the missing Gamma positions

For the trivial character over \(\mathbb Q\),
\[
\boxed{\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).}
\tag{PI024-completed}
\]
The author's spectral sum is indexed by **zeros of this completed \(L\)**, rather than all zeros of the uncompleted \(\zeta_f\). The difference is decisive:

| Gamma index \(n\) | Source Gamma pole \(s=-2n\) | Finite \(\zeta_f(s)\) | Completed \(\Lambda(s)\) | Shift \(w=s-\tfrac12\) |
|---|---|---|---|---|
| \(n=0\) | \(s=0\) | \(\zeta(0)=-1/2\ne0\) | Simple **pole**, not a zero | \(w=-1/2\) |
| \(n\ge1\) | \(s=-2n\) | Simple **trivial zero** | Gamma pole and finite zero **cancel**, no completed zero | \(w=-2n-1/2\) |

Indeed
\[
\frac{\Lambda'}{\Lambda}(s)=
\frac{\zeta'}{\zeta}(s)+\frac12\psi(s/2)-\frac12\log\pi.
\tag{PI024-log-derivative}
\]
At \(s=-2n,\ n\ge1\), the log-derivative residues \(+1\) from \(\zeta_f\) and \(-1\) from \(\Gamma(s/2)\) cancel. At \(s=0\), only the Gamma pole remains (and it is represented by the completed-function **pole** and explicit Mellin pole terms, not by a completed zero).

Thus **none of the shifted Gamma lattice**
\[
\boxed{\{-\tfrac12,-\tfrac52,-\tfrac92,\ldots\}
 =\{-2n-\tfrac12:n\ge0\}}
\tag{PI024-lattice}
\]
belongs to the zero divisor of the source completed \(L\). Any relative vertical strip selects a subset of actual completed zeros and cannot create one of these excluded positions.

This resolves PI023's outstanding *zero indexing* question for the \(F=\mathbb Q\) trivial-character component in the public manuscript. It does NOT prove the Chapter 12/13 trace identities correct, and it does not classify arbitrary Hecke characters for general \(F\).

## 3. Strengthen PI023: the ENTIRE infinite boundary-pole ladder obstructs a finite correction

Retain all the **explicitly conditional** PI023 hypotheses: both literally printed Chapter 12 and Chapter 13 formulas are valid on the SAME \(F=\mathbb Q\) norm-radial test lift for every separated smooth phase test, with exactly matched global pole, prime, Haar, cutoff, and Mellin conventions, and their spectral difference contains ONLY the stated completed nontrivial \(L\)-zero divisors with adequate normal convergence. These assumptions, especially the unproved Chapter 13 assertion and source normalization, are **NOT established**.

Take the PI019 smooth derivative-bump construction \(\rho_0\in C_c^\infty(\mathbb R;\mathbb R_{\ge0})\setminus\{0\}\), \(\phi=\rho_0'\), and let the real translation \(a>d=\operatorname{diam}\operatorname{supp}\rho_0\). Both even and odd phase tests satisfy \(D(0)=\int D=0\) and are supported away from the identity. Under the literal printed normalization, PI022's real-place residual is \(\int D K\), where
\[
K(u)=\sum_{n\ge0}e^{-(2n+1/2)|u|}.
\]
The PI023 paired-phase algebra isolates the positive-translation spectral function \(G(a)\) and requires
\[
\boxed{
G(a)=
-\sum_{n=0}^\infty \lambda_n^2P_n^-P_n^+e^{-\lambda_n a},
\quad
\lambda_n=2n+\tfrac12,\quad
P_n^\pm=\int\rho_0(x)e^{\pm\lambda_nx}dx>0.
}
\tag{PI024-literal-source-implication}
\]

Shift \(a=A+t,\ A>d\), and take the Laplace transform. Because the source-zero weights are absolutely summable after Schwartz smoothing and obey a bounded-imaginary-strip condition, their meromorphic transform has poles only at shifted **completed zero frequencies**. The RHS instead has the meromorphic transform
\[
\boxed{
-\sum_{n=0}^\infty
\frac{\lambda_n^2P_n^-P_n^+e^{-\lambda_n A}}
{s+\lambda_n}.
}
\tag{PI024-arch-Laplace}
\]
It converges normally away from \(-\lambda_n\): the support-diameter condition bounds \(P_n^-P_n^+\) by an exponential of \(\lambda_n d\), dominated by \(e^{-\lambda_n A}\).

At **EVERY** \(s=-\lambda_n\) this transform has strictly nonzero residue
\[
\boxed{
r_n=-\lambda_n^2P_n^-P_n^+e^{-\lambda_n A}<0,\qquad n\ge0.
}
\tag{PI024-all-residues}
\]
By Section 2, the completed \(L\)-zero spectrum has **NO pole at ANY of those positions**, not just PI023's \(s=-1/2\).

**Refined conditional no-go:** the literal common-source trace assumptions cannot simultaneously hold on all separated phase translations. A correction by a **single** boundary pole at \(s=-1/2\), or by any **finite set** of exceptional spectral pole/contact terms, still cannot account for the infinitely many uncanceled nonzero residues \(s=-5/2,-9/2,\ldots\).

The ladder is the shifted footprint of the **uncompleted finite-zeta trivial-zero/Gamma-pole cancellation**. This is a source-preservation dictionary, NOT permission to insert the trivial-zero divisor into the completed \(L\) sum: on an arbitrary two-sided compact test the raw uncompleted-trivial-zero Mellin sum does not necessarily converge without an independently specified one-sided kernel, contour or regularization. The exact sign/weight match for the smoothed phase experiment must be derived, not copied from a list of zeros.

## 4. Consequences for the possible source repairs

**(A) Restoring canonical Haar conversion factors.** Chapter 12 and Appendix B.4.4.7 both print canonical conversions; Chapter 13 does not. Explicitly changing Chapter 13's measure or multiplying its real/complex/finite terms by the correct factors removes the distributed local mismatch and hence the Gamma pole ladder in THIS difference. That would only restore the *possibility* of PI021's conditional overlap-zero identity; it does NOT prove the critical-line/capped spectral theorem, which still has substantial zero-location/multiplicity content.

**(B) Completed-versus-finite spectral correction.** To keep Chapter 13's unweighted geometry, an independent source theorem would have to identify a *whole archimedean/trivial-zero ladder* or equivalent regularized Gamma term in the spectral difference. Simply supplying a completed-zeta zero at \(s=0\) is impossible: the completed \(\Lambda\) has a pole there; the negative-even finite zeta zeros are canceled in \(\Lambda\). Any reintroduction requires a consciously different spectral divisor and a separate proof of its analytic kernel and pole subtraction.

**(C) Separate source lift, pole, cutoff or local conventions.** If Chapter 13 uses genuinely different data despite the printed notation, derive the exact mapping for the test classes and every place, rather than relabeling its PV after the fact. On off-identity test functions, a principal-value/contact change cannot multiply ordinary integrals by 2. A finite adjustment of the two completed poles at \(s=0,1\) can at most affect \(s=\pm1/2\) in the shifted Laplace picture, not the negative-even Gamma ladder at \(s=-5/2,-9/2,\ldots\).

These are **alternatives to investigate**, not corrections established by the author. The public text does not supply a verified fix, and its own appendix proof has editorial cautions.

## 5. Direct exact arithmetic, independent of spectral claims

\`scripts/pi024_completed_divisor_ladder_exact_preflight.py\` was **executed independently on exact Python Fraction arithmetic**. It uses a signed two-atom SURROGATE of PI019's smooth derivative bump, not an admissible smooth spectral test. Put \(a=\log9\), \(\phi_{\rm model}=\delta_0-\delta_{\log4}\), and \(C_{\rm model}=2\delta_0-\delta_{\log4}-\delta_{-\log4}\). Then
\[
\begin{aligned}
I_N(a)
 &=2K_N(\log9)-K_N(\log36)-K_N(\log(9/4))\\
 &=\sum_{n<N}(2-4^{\lambda_n}-4^{-\lambda_n})9^{-\lambda_n}.
\end{aligned}
\]
The coefficient of each \(e^{-\lambda_n a}\) is negative. At \(a=\log9\), the first two coefficients are **\(-1/6\)** and **\(-961/7776\)**, with shifted poles **\(-1/2\)** and **\(-5/2\)**. The script verified:

- **80** exact Gamma index/pole/finite-to-completed log-derivative cancellation positions;
- **81** exact truncated physical signed-kernel identities (N=0,…,80);
- all 80 model residues strictly negative; a single \(s=-1/2\) boundary adjustment leaves 79 further nonzero model poles.

These checks are algebraic consistency tests only. The smooth \(\rho_0\) pole nonvanishing is separately proved in Section 3. The script neither enumerates true zeta zeros nor compiles Lean or tests Masullo's operator.

## 6. Primary-source and formalization custody limitations

- The **public November 20 manuscript** remains an unfinished proof proposal, not an accepted trace theorem. The official release notice invited verification; no authenticated public erratum was located in the limited search.
- \`mccorvie/riemann-masullo\` has an ongoing independent Lean formalization and source errata, but explicitly says Chapters 10–12 have not been formalized and no specialist reviewed its ERRATA; it cannot certify the Chapter 13 divisor replacement or settle the Weil-Lab PI seam.
- The original global source Theorem B.4.4.7 is quoted with its precise printed page and its own **footnote requesting a double-check**. Correcting a PI023 page number does not prove the source theorem.
- **No inference to RH, GRH, full signed Weil positivity, equality of Masullo's trace operator to our physical form, or an IV/CP cross-projection equivalence is made**. PI021's unconditional half-line rigidity theorem remains separate from the unproved premise that two differently normalized printed trace formulas agree.

## 7. PI025 analytic-only handoff

1. Establish the *literal* source moment-domain and norm-radial Haar dictionary rigorously on the **entire** family \(D_e(a),D_o(a)\), not just one \(a=\log9\), including its cutoff and pole conventions. Resolve whether Chapter 13 is an incomplete statement or uses another source definition.
2. Distinguish completed \(L\) zeros, finite \(L_f\) trivial zeros, and the two global completed-function poles in every proposed spectral/pole/arch identity. Do **not** insert a trivial-zero ladder without a matching analytic regularization.
3. Reconcile Chapter 13 with the **canonical normalized** Appendix B.4.4.7 original explicit formula, with real \(1/2\), complex \(1/(2\pi)\) and finite unit-volume factors; inspect any genuine later author erratum by date and immutable source SHA.
4. Only when the normalized geometric sides have actually been reconciled test PI021's spectral half-line rigidity; if a residual remains, preserve the full Gamma pole ladder and expose its exact source.
5. Continue analytic first in PI, IV and CP; NF stays compiler-active. Do not create Actions, PR fan-out or Lean candidates in PI025 until an actual decisive source proof becomes available.

**PI024 verdict:** in the literal manuscript the missing real-place discrepancy carries an **infinite Gamma pole ladder** whose positions are not zeros of the source's completed Hecke \(L\). This strengthens PI023's *conditional* no-go and precisely locates the completed-versus-finite divisor seam. It does not prove or disprove an author-intended corrected theorem or solve RH.
