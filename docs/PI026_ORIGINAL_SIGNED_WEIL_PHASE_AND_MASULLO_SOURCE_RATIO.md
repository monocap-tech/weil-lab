# PI026 — Full original signed Weil phase law on prime/pole-null diagonal tests; exact Chapter 12/13 1:2 spectral source ratio

**Independent Weil-Lab PI### Potential Interface | ANALYTIC-FIRST | NO ACTIONS/LEAN.**
Parent branch \`research/pi025-radial-domain-prime-pole-null-gamma-witness\` and original PI001–PI025 sources retained. Issue #792 is the PI registry. Only this analytic memo and \`scripts/pi026_original_signed_weil_phase_exact.py\` are committed. **No PR, new Lean theorem candidates, workflow, CI job, or dispatch.** NF remains compiler-active; IV and CP remain analytic-first.

**Main CLASSICAL result.** Within a TRUE smooth compact autocorrelation family, the original Zeta23/IV source-signed Weil functional has a STRICT real phase harmonic even though **every prime-power sample, both pole Mellin moments, total Mellin moment, L² mass, identity contact, and the underlying physical support are constant**:
\[
\boxed{
W_{\rm orig}(h_\beta)=W_{\rm orig}(C_m)+B_m\,\operatorname{Re}(\beta),
\quad |\beta|=1,\qquad B_m>0.
}
\tag{PI026-main}
\]
Thus the genuine diagonal tests \(h_1,h_{-1}\), not just their difference, are a counterexample to any cross-projection map using only the phase-blind list of source data above. At m=1,
\[
\boxed{W_{\rm orig}(h_1)-W_{\rm orig}(h_{-1})
=2B_1\ge \frac{1600}{27}R(5/2)R(-5/2)>0.}
\tag{PI026-bound}
\]
This establishes neither positivity for every original Schwartz test nor RH.

**Printed-source comparison (separate CONDITIONAL result).** If Masullo's genuine Chapter 12 **full-zero** and Chapter 13 **critical-only capped** trace identities are valid on the same radial Q phase-difference test, with original source Haar, pole and prime conventions and a common zero indexing dictionary, the **two LITERALLY PRINTED expressions** require
\[
\boxed{
Z_{12}(D_m)=W_{\rm orig}(D_m)=2B_m,\qquad
Z_{13}(D_m)=2W_{\rm orig}(D_m)=4B_m.
}
\tag{PI026-source-ratio}
\]
The factor two comes from Chapter 13's **unweighted real Tamagawa** place versus Chapter 12's **canonical 1/2**; the same source manuscript Appendix B supplies the canonical conversion. These are *necessary predictions conditional on both author-stated formulas*, NOT actual independent spectral sum evaluations and NOT an equality or contradiction already certified in Lean. The incomplete Chapter 13 proof and the completed/full divisor gap remain open.

## 1. Source reopened and exact signs (not a reconstructed generic explicit formula)

### Actual original signed Weil/Zeta23 branch

Directly reopened \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\` from \`research/iv024-original-prime-graph-ci-custody\`, Git blob
\`14d8f01ce34f764900eccc68399d7323b4f4a25c\`.
It provides these literal three-input components for the original complex physical Schwartz correlation \(h_{s,t}(u)=\int t(x)\overline{s(x-u)}dx\):

- \`neutralIV011OriginalMixedPole\`: genuine \`Zeta23.paperFT h (Complex.I/2) + Zeta23.paperFT h (-Complex.I/2)\`.
- \`neutralIV011OriginalMixedPrime\`: \(\sum_{n\ge1}\Lambda(n)/\sqrt n\,[h(+\log n)+h(-\log n)]\), with genuine \`ArithmeticFunction.vonMangoldt\` and no invented support-graph-only approximation.
- \`neutralIV011OriginalMixedArch\`: \((1/(2\pi))\int_{\mathbb R}\operatorname{Zeta23.paperFT}(h)(r)\operatorname{Zeta23.EF.gammaBracket}(r)dr\).
- \`neutralIV011OriginalMixed_arithmeticSplit\`: the **exact original sign** \(\boxed{W_{\rm orig}(h)=\text{pole}-\text{prime}+\text{Gamma}}\). The source also proves a sharp actual Schwartz-support correlation dictionary. Compiler acceptance of this individual branch/module is NOT newly asserted; the *classical* exact definitions are the source of this stage.

The original Gamma distribution on general compact smooth h was derived classically in PI018:
\[
A_\Gamma(h)=-(\gamma+\log\pi)h(0)-
\int_{\mathbb R}\left(h(u)-h(0)e^{-3|u|/2}\right)K(u)du,\quad
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}.
\tag{PI026-Gamma}
\]
This retains the source's \((1/2\pi)\) forward Fourier normalization and contact payment; it does not pretend that a divergent \(\int hK\) is legal at h(0)≠0. The auxiliary \(e^{-3|u|/2}\) is *only* a Lipschitz compensation anchor, not a Masullo smooth source test.

### Actual Masullo November 2026 source

Reopened and visually inspected the original 940-page Masullo *The Music of the Primes* (https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf), not just summaries:

- printed p.519/PDF index 518: Theorem 12.5.1.1 assumes \(\varphi(C_F^1)=0\), prints the real-place **\(1/2\)**, complex **\(1/(2\pi)\)**, finite **\(\log(q_v)/\mu_v(O_v^\times)\)** coefficients, and a full zero-divisor sum \(-\sum_{c,I}N(c)M(\varphi)(c|\cdot|_F^{-1/2})\) with specified relative strip \(I\). Printed p.520/PDF index 519 gives a proof claiming that formula by global kernel comparison.
- printed p.522/PDF index 521: Theorem 13.3.1.1 states a distinct Mellin-moment domain, **critical-line-only** sum with **\(N_{\rm spec}(c)=\min(N(c),[F:\mathbb Q])\)**, and local principal-value integrals printed **without** the Chapter 12 canonical factors. Theorem 13.3.1.2 below contains "Insert statement", and the chapter invokes "Theorem ??" and asks to state/prove the main theorems. This is a manuscript assertion with a missing displayed proof, not independent theorem certification.
- printed p.546/PDF index 545: the source exhibits \(C_\mathbb Q\cong\mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times}\) and its norm section; printed p.561/PDF index 560: compatible Haar \(dt/t\otimes d\bar\mu_1\). The source Q fiber normalization \(\bar\mu_1(C_\mathbb Q^1)=1\) was audited in PI025.
- printed p.623/PDF index 622: Theorem B.4.4.7 prints the canonical \(1/M_v\) factor, \(M_v=2\) at a real place and \(2\pi\) at a complex place; the manuscript's separate author factor-check caveat was authenticated in PI022–PI024. No authenticated subsequent corrected Chapter 13 text was substituted.

**Scope:** The source's actual full zero divisor may be in a restricted strip \(I\); Chapter 13's summation/character indexing and cutoff terms are not independently reconciled. Do not silently change either sum into the *same* complete nontrivial Riemann zero divisor or assume RH/multiplicity one.

## 2. Prime- and pole-null SOURCE-CONCRETE smooth diagonal family

Fix
\[
q=\frac94,\quad a=\log q,\quad d=\log(10/9),\qquad
2<\frac{81}{40}=qe^{-d}<q<qe^d=\frac52<3.
\]
Choose any nonzero real \(\rho\ge0\) in \(C_c^\infty((0,d))\). For an integer \(m\ge1\), define
\[
\lambda_j=2j+\tfrac12,\qquad
\phi_m=\partial_x\prod_{j=0}^{m-1}(\partial_x^2-\lambda_j^2)\rho,
\quad\psi_m(x)=\phi_m(x-a).
\]
The two real bumps are disjoint, nonzero and have equal mass \(J_m=\|\phi_m\|_2^2>0\). For a unit complex phase \(\beta\in\mathbb C,\ |\beta|=1\), put
\[
s_{\beta,m}(x)=\frac{\phi_m(x)+\beta\psi_m(x)}{\sqrt2},\quad
h_{\beta,m}(u)=\int_{\mathbb R}s_{\beta,m}(x)\,
\overline{s_{\beta,m}(x-u)}dx.
\]
Every \(s_{\beta,m}\) is a **genuine compactly supported Schwartz test** (not a formal delta or the Lipschitz PI018 anchor). It has the SAME physical support and L² mass \(J_m\) for every \(|\beta|=1\). Let \(C_m(u)=\int\phi_m(x)\phi_m(x-u)dx\), a real even smooth compact autocorrelation. Exact expansion in the **literal** original IV orientation is
\[
\boxed{h_{\beta,m}(u)=
C_m(u)+\tfrac{\bar\beta}{2}C_m(u+a)
+\tfrac{\beta}{2}C_m(u-a).}
\tag{PI026-correlation}
\]
Thus \(h_{\beta,m}(0)=J_m\) for every beta. Each support lies in the same three disjoint physical intervals near \(0,\pm a\), independent of phase.

For the compact fiber-normalized Q radial lift \(\varphi_h(t,k)=h(\log t)\), verified in PI025, the Chapter 12 vanishing-on-\(C_\mathbb Q^1\) condition is \(h(0)=0\), and the Chapter 13 **STATED** F=Q Mellin-moment condition is \(\int h=0\). The individual \(h_{\beta,m}\) have NONZERO h(0), so they are not tests of the headline Chapter 12 theorem; they do lie in the Chapter 13 *stated domain* as a **test-space fact**, not an already validated theorem.

### EVERY original finite-place arithmetic prime sample vanishes for the individual tests

The central support of \(C_m\) is contained in \([-d,d]\), with \(d<\log2\). The two translated supports are contained in
\[
\pm[a-d,a+d]
=\pm[\log(81/40),\log(5/2)]
\subset\pm(\log2,\log3).
\]
For every integer \(n\ge2\), \(\log n\) is either \(\log2\) or at least \(\log3\), or equals another integer log outside the gap. Therefore
\[
\boxed{h_{\beta,m}(\pm\log n)=0\quad(n\ge2),}
\tag{PI026-primes}
\]
including ALL prime powers \(\Lambda(n)\ne0\). The \(n=1\) term has \(\Lambda(1)=0\). Hence the literal source \`neutralIV011OriginalMixedPrime\` is exactly zero for each beta and every m≥1, with no finite cutoff approximation and no use of a support interaction graph as a surrogate for the complex amplitudes.

### BOTH original source poles vanish for each diagonal

Let \(R(z)=\int\rho(x)e^{zx}dx\), \(S_m(z)=\int\phi_m(x)e^{zx}dx\), so
\[
S_m(z)=-z\prod_{j<m}(z^2-\lambda_j^2)R(z).
\tag{PI026-S}
\]
The two-point correlation has Laplace moment \(\int h_{\beta,m}(u)e^{zu}du
=\frac12 S_m(z)S_m(-z)(2+\beta e^{az}+\bar\beta e^{-az})\).
Because \(S_m(0)=S_m(\pm1/2)=0\), every beta has
\[
\boxed{
\int h_{\beta,m}=0,\quad
\operatorname{Zeta23.paperFT}(h_{\beta,m})(+i/2)=
\operatorname{Zeta23.paperFT}(h_{\beta,m})(-i/2)=0.
}
\tag{PI026-poles}
\]
The \(+i/2\) Fourier argument means \(e^{-u/2}\), the \(-i/2\) argument means \(e^{u/2}\). This retains the genuine source's positive Fourier sign.

Therefore, on the full source signed form, for each beta **individually**,
\[
\boxed{W_{\rm orig}(h_{\beta,m})=A_\Gamma(h_{\beta,m}).}
\tag{PI026-source-split}
\]
No Masullo theorem is invoked to get this identity: it uses the original arithmetic split and actual zero prime/pole components. A source-checked Lean import/compiler receipt remains an independent certification obligation.

## 3. Exact full-form REAL phase law and strictly positive amplitude

The infinite physical Gamma kernel is even, \(K(u)>0\) for \(u\ne0\). The central smooth C_m carries the same contact \(C_m(0)=J_m\) as every h_beta. Using the PI018 **fully compensated** Gamma distribution, all beta-independent terms group into \(W_{\rm orig}(C_m)=A_\Gamma(C_m)\). The shifted cross terms are supported away from zero, so their ordinary integrals converge and the source gamma sign is negative.

Define
\[
I_{a,m}:=\int_{\mathbb R}C_m(v)K(a+v)dv.
\]
The kernel and C_m are even, hence both shifted cross integrals equal \(I_{a,m}\). Therefore
\[
W_{\rm orig}(h_{\beta,m})
=W_{\rm orig}(C_m)-\operatorname{Re}(\beta)I_{a,m}.
\]
Put \(B_m=-I_{a,m}\). Since \(a>d\), expand the **actual** PI007 physical kernel into the absolutely convergent source exponentials \(\lambda_n=2n+1/2\):
\[
\begin{aligned}
I_{a,m}
&=\sum_{n\ge0}e^{-\lambda_n a}S_m(-\lambda_n)S_m(\lambda_n)\\
&=-\sum_{n=m}^{\infty}
e^{-\lambda_n a}\lambda_n^2
\prod_{j<m}(\lambda_n^2-\lambda_j^2)^2
R(\lambda_n)R(-\lambda_n).
\end{aligned}
\]
For real \(\lambda\), \(R(\pm\lambda)>0\) because rho is nonzero nonnegative; all surviving coefficients are strictly positive, and convergence is exponential due to \(a>d\). Thus
\[
\boxed{\displaystyle
B_m=\sum_{n=m}^\infty
e^{-\lambda_n a}\lambda_n^2
\prod_{j<m}(\lambda_n^2-\lambda_j^2)^2
R(\lambda_n)R(-\lambda_n)>0,
}
\tag{PI026-amplitude}
\]
and
\[
\boxed{
W_{\rm orig}(h_{\beta,m})
=W_{\rm orig}(C_m)+B_m\operatorname{Re}\beta.
}
\tag{PI026-phase}
\]
At m=1, n=1 has coefficient \(\tfrac{800}{27}\), giving
\[
\boxed{B_1\ge\tfrac{800}{27}R(-5/2)R(5/2)>0.}
\]
With \(\beta=e^{i\theta}\), the complete original signed Weil quadratic form has the **exact first cosine harmonic**
\[
\boxed{W_{\rm orig}(h_{e^{i\theta},m})
=W_{\rm orig}(C_m)+B_m\cos\theta.}
\tag{PI026-cosine}
\]
In particular
\[
\begin{aligned}
W_{\rm orig}(h_{1,m})-W_{\rm orig}(h_{-1,m})&=2B_m>0,\\
W_{\rm orig}(h_{i,m})-W_{\rm orig}(h_{-i,m})&=0,\\
W_{\rm orig}(h_{i,m})&=W_{\rm orig}(C_m).
\end{aligned}
\]
This is a **relative comparison**, NOT a claim that \(W_{\rm orig}(C_m)\) or every diagonal value is nonnegative. The fact that these particular original diagonal tests are phase-sensitive does not establish original global Weil positivity.

## 4. Strict phase-blind no-go **on the autocorrelation cone itself**

Consider the data carried by a putative phase-insensitive cross-projection invariant:
\[
\mathcal I(h_{\beta,m})=
\left(
\operatorname{supp}s_{\beta,m},\,
\|s_{\beta,m}\|_2^2,\,
h_{\beta,m}(0),\,
\int h_{\beta,m},\,
\int h_{\beta,m}e^{\pm u/2},\,
\{h_{\beta,m}(\pm\log n)\}_{n\ge2}
\right).
\]
All these data are **identical** for every unit beta, including beta=1 and beta=-1. But their full original Weil evaluations differ by strictly \(2B_m>0\).

Hence there is **NO FUNCTION**, even nonlinear, of just this data tuple that reproduces the original Weil form on all genuine smooth compact Schwartz autocorrelations:
\[
\boxed{
\not\exists F:\quad
W_{\rm orig}(h)=F(\mathcal I(h))
\quad\text{for every such diagonal }h.
}
\tag{PI026-cone-no-go}
\]
This is stronger than PI025's original comparison \(D_m\) vs the zero test: it works **within the positive autocorrelation cone**. The real relative phase (or an equivalent continuous Gamma/spectral carrier) must survive a faithful cross-projection map. A signed prime-interaction graph alone is even less information than the full null data tuple and cannot recover the strictly varying phase law.

**Precision:** The no-go forbids compression to precisely the listed data. It does not forbid a spectral projection retaining the entire test transform, a suitable off-diagonal density, or an intrinsically richer phase-sensitive invariant.

## 5. Literal Masullo Chapter12/Chapter13 spectral ratio under explicit, UNPAID trace hypotheses

Let
\[
D_m=h_{1,m}-h_{-1,m}
=C_m(u+a)+C_m(u-a).
\]
Then \(D_m(0)=\int D_m=\int D_m e^{\pm u/2}=0\), and \(D_m(\pm\log n)=0\) at every original prime sample. It is smooth, supported away from zero, and belongs to both Q radial source **test domains**, independently of whether either claimed trace is valid. From the proven original source phase law:
\[
\boxed{W_{\rm orig}(D_m)=A_\Gamma(D_m)=2B_m>0,\qquad
\int_{\mathbb R}D_m(u)K(u)du=-2B_m.}
\tag{PI026-D}
\]

**Chapter 12 literal local-geometric equation, conditional on its theorem and source lift.** Printed equation (12.5.1.1–3) has canonically normalized real coefficient \(1/2\) before the Tamagawa PV, while all pole moments and finite prime samples on D_m vanish. Since supp(D_m) excludes 0, this PV is an ordinary integral:
\[
\frac12 R_\mu(D_m)=\int D_m K=-2B_m,\quad
R_\mu(D_m)=2\int D_mK.
\]
The printed Chapter 12 formula is \(\text{local geometric}=\text{poles}-Z_{12,I}\). Therefore it **would require**
\[
\boxed{Z_{12,I}(D_m)=-\int D_mK
=2B_m=W_{\rm orig}(D_m).}
\tag{PI026-Z12}
\]

**Chapter 13 literal local-geometric equation, conditional on its differently stated theorem.** Printed equation (13.3.1.3–5) has real Tamagawa PV coefficient \(1\) rather than \(1/2\). The source's claimed critical-line capped divisor is \(N_{\rm spec}(c)=\min(N(c),[F:\mathbb Q])\), so here \(N_{\rm spec}=\min(N,1)\); it does NOT become the full Chapter 12 divisor by assertion. With poles and finite primes zero, the literal displayed Chapter 13 formula is \(Z_{13,\rm cap}=\text{poles}-\text{local geometric}\). It **would require**
\[
\boxed{Z_{13,\rm cap}(D_m)=-2\int D_mK
=4B_m=2W_{\rm orig}(D_m).}
\tag{PI026-Z13}
\]
Thus the two printed source spectra would necessarily satisfy the **strict** arithmetic source ratio
\[
\boxed{Z_{13,\rm cap}(D_m)=2Z_{12,I}(D_m)>0,\quad
Z_{12,I}(D_m)-Z_{13,\rm cap}(D_m)=-2B_m.}
\tag{PI026-ratio}
\]

**This is not an independently proved evaluation of either zeta-zero series.** Neither manuscript statement has been newly verified, Chapter13's displayed proof remains unfinished, and the zero strip/capped divisor cannot be silently identified. It is a **falsifiable source compatibility condition** for anyone proposing that BOTH printed identities hold with a common unaltered Haar/test dictionary.

**Contact terms cannot repair the mismatch.** On D_m, h(0)=0, ∫h=0, both pole Mellin moments=0, and all prime-power samples are zero, so no combination of \(\delta_0\), constant-total-mass, pole-moment or original prime-sample corrections changes the \(-2B_m\) residual. The only legitimate repairs would change the real geometric normalization, carry an additional continuous/spectral term, or alter another independently documented source hypothesis. PI022–PI024 identified canonical Haar as the most direct *editorial* candidate; **no corrected Chapter13 theorem has been authenticated**.

**Crucial distinction:** PI021's half-line Laplace spectral rigidity applies only if a source-matched overlap equality holds for an **entire unbounded translation family**. The prime-free support gap used here is BOUNDED in a, so one cannot borrow PI021 to conclude any zero is on or off the critical line. PI023–PI024's boundary/gamma-ladder conditional no-go uses a separately stronger all-translation assumption and is preserved as its own investigation.

## 6. Exact rational preflight, no new Actions or compiler

\`scripts/pi026_original_signed_weil_phase_exact.py\` uses \`fractions.Fraction\` to verify:
- all-prime-power support gap: \(2<81/40<9/4<5/2<3\);
- the source kernel point \(K(\log(9/4))=54/65\) and \(\lambda_0\)-pole/moment root;
- for 8 annihilator orders m=1,…,8, **400** exact surviving strictly positive rational Gamma coefficients;
- **240** exact \(W_0+B\,\mathrm{Re}\beta\) identities over ten rational unit-circle phases and three arbitrary base values per m, including real-phase contrast, imaginary-phase invariance, and the **conditional** \(Z_{12}=2B, Z_{13}=4B\) source algebra.
- m=1 n=1 exact coefficient \(800/27\) and doubled difference \(1600/27\).

**Independent equivalent exact-arithmetic execution PASS: 400 coefficient checks and 240 phase checks.** This verifies rational algebra; the classical smooth-function construction and infinite-series positivity are proved mathematically in §§2–3, not by the finite script. No direct zeta-zero sum, independent Masullo operator trace, Lean compiler build, full original IV011 kernel audit or RH claim is supplied.

## 7. PI027 analytic-only next

1. **Source-local functional test:** build an explicit exact source normalization matrix for the original IV signed \(W=\text{pole}-\text{prime}+\text{Gamma}\), Masullo Ch12 \(\text{real}/2\), and Ch13 \(\text{real}\), including the prime coefficient and both polar evaluations on radial Q test space. Choose at least one source-test family with NONzero prime samples alongside PI026's all-zero prime samples to detect independent arithmetic sign mistakes.
2. **Spectral phase carrier:** derive the actually source-shifted Mellin transform of \(h_{\beta,m}\) at a general zero \(\rho=\sigma+i\gamma\), keeping the full complex off-critical test transform, and test whether a proposed CP spectral invariant retains \(B_m\) from the phase-varying true diagonal tests. No zero-sum equality may be assumed.
3. **Source correction fork:** if an author-supplied Chapter13 revision is found, freeze its bytes/date and redo the local coefficient and zero-divisor comparison; otherwise retain the literal factor-two compatibility equation and the PI023–PI024 gamma-pole no-go.
4. Continue PI, IV, CP **analytic-first** with no new automatic workflows. NF remains the only compiler-priority lane.

**PI026 verdict:** a rigorously constructed family of actual Schwartz **diagonals**, indistinguishable by the prime/pole/contact/total-moment/support/mass data, has a strictly varying FULL ORIGINAL signed Weil evaluation \(W_0+B_m\cos\theta\). The literal printed Masullo 12/13 spectral formulations would demand a strict 1:2 source ratio on their common test difference, not equality. The missing source normalization/proof is a real mathematical obligation, not a formalization backlog issue. No full Weil positivity, RH, or certified cross-projection equivalence follows.
