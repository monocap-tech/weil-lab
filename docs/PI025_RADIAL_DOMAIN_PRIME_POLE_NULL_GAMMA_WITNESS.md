# PI025 — Source-exact Q radial test domain, prime/pole-null smooth witnesses and arbitrary finite Gamma-mode annihilation

**Weil-Lab PI### Potential Interface. ANALYTIC-FIRST.** Parent: \`research/pi024-analytic-completed-divisor-gamma-pole-ladder\`. PI registry #792. This stage adds **one mathematical memo and one exact-Fraction preflight script only**. **NO new pull request, Lean theorem file, GitHub Actions workflow or dispatch.** NF numerical certification remains compiler-active. PI, IV and CP remain analytic-first.

**New unconditional classical result:** an explicit smooth, compact, real test \(D\neq0\), which is the difference of two genuine diagonal autocorrelations of equal mass, annihilates (a) the Chapter 12 norm-one/contact evaluation, (b) the Chapter 13 \(F=\mathbb Q\) total Mellin moment, (c) BOTH explicit pole Mellin evaluations, and (d) EVERY prime-power logarithmic point sample. Yet its original PI018 Gamma distribution is STRICTLY POSITIVE with an exact lower bound. A generalized differential annihilator can kill any prescribed FINITE initial segment of real Gamma Laplace atoms and still leave a strictly positive Gamma response. Thus prime, pole, contact and finitely many arch mode data are insufficient to reconstruct the original Gamma distribution.

**Crucial contextual boundary:** PI022–PI024 identified a literal real-place canonical/Tamagawa **factor-two mismatch** between Masullo Chapters 12 and 13 and a conditional Gamma Laplace-pole no-go against using the two printed identities simultaneously. PI025 does NOT assume their geometric sides are identical or the Chapter 13 claim is valid. It supplies genuine prime- and pole-null source tests and independently checks the radial group/test-space dictionary. Its new compact *prime-gap* family is NOT an unbounded translation half-line, so PI021's full-halfline spectral rigidity cannot be applied merely from data on this bounded gap.

## 1. Primary source: an actual F=Q norm split and exact Haar disintegration

Directly re-read the original 940-page November 2026 Masullo PDF:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

- **Printed p.546 (PDF index 545), equation (A.2.2.3) and Lemma A.2.2.1:** the source supplies a genuine topological group isomorphism
\[
\boxed{C_\mathbb Q\cong\mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times},}
\tag{PI025-Q-split}
\]
and a canonical continuous multiplicative section \(s_\mathbb Q\) of the idelic norm. In particular the norm-one fiber is the compact profinite group \(C_\mathbb Q^1\cong\widehat{\mathbb Z}^{\,\times}\).
- **Printed p.547 (PDF index 546), Lemmas A.2.2.4 / A.2.2.9:** compatible sections and the direct product \(\mathbb R_{>0}\times \mathrm{GL}_1(\mathbb A_F)^1\) on ideles are explicitly described; it is not a guessed scalar projection.
- **Printed p.561 (PDF index 560), §A.3.3.1:** under the section, the local/global Tamagawa product measure disintegrates as
\[
d\bar\mu_{C_F}=(dt/t)\otimes d\bar\mu_1\quad
\text{on }\mathbb R_{>0}\times C_F^1.
\tag{PI025-Haar}
\]
- **Printed p.560 (PDF index 559), formula (A.3.2.1):** for \(F=\mathbb Q\), \(r_1=1,r_2=0,h=1,R=1,|\!d_F\!|=1,w_F=2\), hence the compact fiber has the explicitly normalized Haar mass
\[
\boxed{\bar\mu_1(C_\mathbb Q^1)=1.}
\tag{PI025-fiber-mass}
\]
- **Printed pp.62–63 (PDF indices 61–62), §2.1.1.3–§2.1.2:** Schwartz–Bruhat tests on \(\mathbb R\times\) compact profinite groups include compactly supported smooth functions in the real coordinate and constant (therefore locally constant) functions on the compact fiber. For \(h\in C_c^\infty(\mathbb R;\mathbb C)\), the norm-radial lift
\[
\boxed{\varphi_h(t,k)=h(\log t),\quad
(t,k)\in\mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times}}
\tag{PI025-radial}
\]
is a genuine smooth compactly supported test on \(C_\mathbb Q\), not merely a formal expression. Its support is the product of the compact \(e^{\operatorname{supp}h}\) and the compact fiber. The source uses \(\mathcal D(C_F)\) for this test class; the induced compact-support/smoothness claim follows from the actual split. No source-specific unproved operator theorem is needed for this elementary test membership.

### The TWO literal theorem domains follow exactly on this radial subspace

**Chapter 12, Theorem 12.5.1.1, printed p.519 (PDF index 518):** it assumes \(\varphi(C_F^1)=0\). At \(t=1\) the radial lift is the constant \(h(0)\) on the compact fiber, so
\[
\boxed{\varphi_h|_{C_\mathbb Q^1}\equiv0\iff h(0)=0.}
\tag{PI025-Ch12}
\]

**Chapter 13, Theorem 13.3.1.1, printed p.522 (PDF index 521):** its proposed moment restriction (13.3.1.2) applies to every unitary \(\chi\) and \(0\le k\le[F:\mathbb Q]-1\). For Q only \(k=0\). Every unitary character of the split group is
\[
\chi(t,k)=t^{i x_0(\chi)}\xi(k),
\]
where \(\xi\) is a unitary character of the compact group. The source's moment is
\[
\begin{aligned}
\left.\int_{0}^{\infty}t^{s+i x_0(\chi)}
\left(\int_{C_\mathbb Q^1}h(\log t)\xi(k)d\bar\mu_1(k)\right)
\frac{dt}{t}\right|_{s=-i x_0(\chi)}.
\end{aligned}
\]
If \(\xi\neq1\), its compact-fiber integral vanishes by Haar character orthogonality. If \(\xi=1\), the compact-fiber integral has normalized value \(h(\log t)\), the \(t\)-phase cancels at the source evaluation, and \(u=\log t\) gives
\[
\boxed{
\text{ALL Chapter 13 moment conditions on radial Q tests}
\iff \int_{\mathbb R}h(u)\,du=0.}
\tag{PI025-Ch13}
\]
The converse follows by taking the trivial character. This is an **exact elementary source-domain reduction**, not a proof of the **different** Chapter 13 trace equality. It also exhibits the independence of the two hyperplanes \(\ker h(0)\) and \(\ker\int h\) in the genuine source test class. The author-stated Chapter 13 theorem still has critical-line-only capped multiplicities and visibly incomplete adjacent proof text; nothing here authenticates that theorem.

## 2. Genuine smooth phase probes in the COMPLETE prime-power gap (2,3)

Choose exact rational values
\[
\boxed{q=9/4,\quad a=\log q,\quad d=\log(10/9).}
\]
They obey
\[
\boxed{
2<81/40=q e^{-d}<q<q e^d=5/2<3,\quad d<a.}
\tag{PI025-prime-gap}
\]
Take nonzero nonnegative \(\rho\in C_c^\infty((0,d);\mathbb R)\). For the basic \(m=1\) case define
\[
\phi=\rho'''-\frac14\rho',\quad \psi(x)=\phi(x-a),\quad
s_\beta=(\phi+\beta\psi)/\sqrt2,\quad
h_\beta(u)=\int s_\beta(x)\overline{s_\beta(x-u)}dx.
\]
Every hβ is a genuine smooth compactly supported complex autocorrelation and \(h_\beta(0)=J=\|\phi\|_2^2>0\). Let \(C(v)=\int\phi(x)\phi(x-v)dx\) and
\[
\boxed{D=h_1-h_{-1}=C(u+a)+C(u-a).}
\tag{PI025-D}
\]

Because supp C is in [-d,d], the supports of the shifted parts of D lie in the two intervals
\[
\pm[\log(81/40),\log(5/2)]\subset
\pm(\log2,\log3).
\]
Thus D is identically zero on a neighborhood of the identity and at ALL logarithmic prime powers:
\[
\boxed{D(0)=0,\quad D(\pm\log p^k)=0\quad\forall p,k\ge1.}
\tag{PI025-prime-null}
\]
The *individual* hβ have an additional central C bump supported in [-d,d], with d<log2; they likewise vanish at every nontrivial logarithmic prime-power sample, despite hβ(0)=J>0. The information is exact at all primes, not a finite sample of the n=9 graph.

This support window is intentionally **not** the frozen original IV physical collar; no IV local margin or pre-certified support transfer is being silently extended.

## 3. Simultaneously annihilate the total Mellin moment and BOTH poles

For real or complex z define
\[
R(z)=\int\rho(x)e^{zx}dx,\quad
S(z)=\int\phi(x)e^{zx}dx
=-z(z^2-\tfrac14)R(z).
\tag{PI025-annihilator}
\]
Integration by parts is justified by smooth compact support. For all real z, \(R(z)>0\), and \(S(0)=S(\pm1/2)=0\). The entire bilateral Laplace transform of D is exactly
\[
\boxed{\mathcal L_D(z)=
2\cosh(az)\,S(z)S(-z)
=-2z^2(z^2-\tfrac14)^2\cosh(az)R(z)R(-z).}
\tag{PI025-transform}
\]
Therefore
\[
\boxed{
\int D=0,\quad
\int D(u)e^{u/2}du=0,\quad
\int D(u)e^{-u/2}du=0.}
\tag{PI025-moments}
\]
The values at ±1/2 correspond to the **two pole Mellin evaluations displayed in the actual Chapter 12 (12.5.1.3)** after the exact radial lift. These vanish for each individual hβ too, as each \(s_\beta\) inherits S(0)=S(±1/2)=0. In particular, every hβ belongs to Chapter 13's *stated* moment domain and has nonzero diagonal hβ(0)=J, while D lies in the **intersection** of the Chapter 12 and Chapter 13 source test domains.

This is a rigorous *test-space* result; it does not establish Masullo's Chapter 13 trace theorem, an independent operator or a source-normalized spectral equality.

## 4. The original real Gamma distribution is nevertheless STRICTLY nonzero

The PI007/PI018 original physical kernel is
\[
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}
=\sum_{n\ge0}e^{-\lambda_n|u|},\quad
\lambda_n=2n+\tfrac12.
\]
All D support is away from zero, so the source PI018 Gamma distribution has no contact term:
\[
A_\Gamma(D)=-\int_{\mathbb R}D(u)K(u)du.
\]
Since K and C are even, set \(I_a=\int C(v)K(a+v)dv\) and obtain
\[
\begin{aligned}
A_\Gamma(D)&=-2I_a\\
&=2\sum_{n\ge0}e^{-\lambda_n a}\lambda_n^2
(\lambda_n^2-\tfrac14)^2R(\lambda_n)R(-\lambda_n).
\end{aligned}
\tag{PI025-Gamma}
\]
The n=0 term is EXACTLY zero because \(\lambda_0=1/2\), an annihilated pole exponent. For every n≥1 the coefficient is STRICTLY positive, and the series converges absolutely since a>d. Hence
\[
\boxed{A_\Gamma(D)\ge
\frac{1600}{27}R(5/2)R(-5/2)>0,}
\tag{PI025-Gamma-bound}
\]
because the n=1 coefficient in \(I_a\) is \(800/27\) at \(a=\log(9/4)\).

This is a classical analytic calculation for legitimate smooth tests, **not** a Gaussian-delta surrogate, a finite-precision quadrature or an independent evaluation of a spectral operator. The local kernel value \(K(a)=54/65\) is an exact consistency check, not an adequate substitute for the Laplace-product sign proof.

### Strengthening: annul ANY FINITE initial segment of Gamma atoms

For any integer m≥1, set
\[
\boxed{
\phi_m=
\partial_x\prod_{j=0}^{m-1}(\partial_x^2-\lambda_j^2)\rho,
\qquad \lambda_j=2j+\tfrac12.}
\tag{PI025-mode-annihilator}
\]
Form \(s_{\beta,m},h_{\beta,m},D_m\) with the SAME separated supports. Every D_m has all the prior source-domain, pole, contact and prime-sample vanishings, while
\[
S_m(z)=\int\phi_m(x)e^{zx}dx=
-z\prod_{j=0}^{m-1}(z^2-\lambda_j^2)R(z).
\]
For n<m, \(S_m(\pm\lambda_n)=0\); for n≥m,
\[
S_m(\lambda_n)S_m(-\lambda_n)
=-\lambda_n^2\prod_{j<m}(\lambda_n^2-\lambda_j^2)^2
R(\lambda_n)R(-\lambda_n)<0.
\]
Thus
\[
\boxed{\displaystyle
A_\Gamma(D_m)=
2\sum_{n=m}^{\infty}
e^{-\lambda_n a}\lambda_n^2
\prod_{j<m}(\lambda_n^2-\lambda_j^2)^2
R(\lambda_n)R(-\lambda_n)>0.}
\tag{PI025-tail-survives}
\]
This proof requires no zero-location assumption and no knowledge of a Masullo trace. It shows that removing any FIXED FINITE collection of the initial Gamma atoms, including the n=0 boundary pole emphasized in PI023, does **not** erase the nonzero distributed Gamma response. PI024 already analyzed the full unmatched Gamma pole ladder under an all-translation source-comparison hypothesis; this finite-annihilator result is a complementary **explicit prime-/pole-null smooth test** construction. It does not supersede or conflate the half-line pole argument.

## 5. Exact information-obstruction theorem and its limitation

Define the invariant candidate
\[
\mathcal I(h)=\Big(h(0),\int h,
\int h e^{u/2},\int h e^{-u/2},
\{h(+\log p^k),h(-\log p^k)\}_{p,k}\Big).
\]
For any m≥1 the nonzero D_m satisfies \(\mathcal I(D_m)=\mathcal I(0)=0\), while \(A_\Gamma(D_m)>A_\Gamma(0)=0\). Thus:
\[
\boxed{
\text{There is NO map }F\text{ (even nonlinear) with }
A_\Gamma(h)=F(\mathcal I(h))
\text{ for every smooth compact }h.}
\tag{PI025-no-go}
\]
The proof uses two tests with IDENTICAL \(\mathcal I\) data and DIFFERENT Gamma values. It is a strict loss-of-information counterexample, stronger than support-graph-only or prime-phase-only limitations.

This does NOT contradict an actual complete Weil explicit formula, because the **full zero-divisor spectral test transform**, continuous archimedean kernel or an equivalent retained carrier can distinguish D_m from zero. It is also NOT a proof that a CP or IV proposal retaining more information fails.

### The literal Chapter 12-vs-13 factor TWO must NOT be overlooked

PI022–PI024 authenticated from the actual manuscript that the Chapter 12 real local coefficient is 1/2 of Tamagawa PV and the Chapter 13 display omits the 1/2, while Appendix B specifies the canonical factor. For the off-identity D_m, the unweighted real local integral is \(2\int D_mK\), and the Chapter 12 canonical term is \(\int D_mK\). Therefore the literal printed geometric difference is
\[
\boxed{
\mathsf A_{13,\infty}(D_m)
-\mathsf A_{12,\infty}(D_m)
=\int D_mK=-A_\Gamma(D_m)<0.
}
\tag{PI025-literal-residual}
\]
Both Mellin pole evaluations and every original prime-power sample of D_m vanish. Hence **this one explicit witness isolates a nonzero real-place residual from ALL those other original channels**, even on the proposed Chapter 12/13 domain intersection.

If the two PRINTED formula statements were independently valid on D_m with exactly the same test lift, canonical/Tamagawa convention and zero-index dictionary, the necessary spectral difference would be the **NONZERO** residual above, not zero. If an author-supplied correction restores Chapter 13's 1/2 factor, this particular geometric residual disappears, but proving the revised critical-line/capped trace theorem remains an independent and potentially very deep problem. No corrected version of the manuscript was observed here, and neither theorem was independently verified in this stage.

**The bounded-gap / half-line distinction matters.** Since a fixed positive width prime-free interval cannot extend through all sufficiently large a (prime power logs recur), PI021's infinite spectral uniqueness on a whole translation HALF-LINE does not apply to the prime-NULL witness family alone. The **all-translation** argument of PI023–PI024 needs the separately hypothesized matching of nonzero prime terms. These are two different admissible experiments; do not combine their assumptions silently.

## 6. Exact preflight and source custody

The executable analytic-only script
\`scripts/pi025_prime_gap_pole_moment_gamma_ladder_exact.py\`
checks, using Python \`fractions.Fraction\` and NO floating-point numerical quadrature:

- Exact prime gap \(2<81/40<9/4<5/2<3\), support separation and \(K(\log(9/4))=54/65\);
- polynomial Mellin annihilation at 0 and ±1/2, for m=1,…,8;
- cancellation of the first m Gamma atoms, and **280** strictly positive retained coefficients for n=m,…,m+34;
- the exact basic lower coefficient \(1600/27\) times the two positive Laplace moments of rho.

**Independent arithmetic execution: PASS.** The infinite series convergence and positivity are proved by the mathematical argument; the finite regression cannot replace that proof. No Lean/CI acceptance, zero evaluation, independent spectral-operator normalization or RH claim is made.

Source primary: The Music of the Primes (November 2026), pp.62–63, 519–522, 546–547, 560–561, 619–620, and corrected Appendix B.4.4.7 at printed p.623. Original PI007/PI008/PI018 physical Gamma source and PI022–PI024 normalization audit are retained. **No PR/Actions workflow/Lean added by PI025.** NF numerical certification unaffected.

## 7. PI026 analytic-only handoff

1. **Source exact diagram:** write and check the commutative diagram between \(\mathcal D(C_\mathbb Q)\), the canonical norm-radial lift, all local place restrictions, the true Haar normalization and the original signed Weil functional. Clarify whether the sum of local terms can be expressed entirely through prime samples and the real Gamma distribution on the full radial domain.
2. **Test the new family on both claimed source theorems, separately:** Chapter 12 full-divisor formula on D_m (zero contact) and Chapter 13 proposed capped critical-line formula on the individual h_{\beta,m} (zero Mellin moment but NONzero h(0)). Carry the factor-of-two discrepancy explicitly until a verified correction exists.
3. **Source-corrected pole ladder:** explain how a finite collection of boundary/trivial-zero terms is annihilated by the chosen \(\phi_m\), leaving an independently nonzero Gamma tail. Do not assume a finite source correction repairs the entire Gamma distribution.
4. **Inter-projection information contract:** IV and CP candidate invariants must be able to distinguish D_m from zero despite matching ALL prime, pole, contact and moment samples. Preserve the full spectral test transform or equivalent phase/arch carrier.
5. Continue ANALYTIC ONLY on PI/IV/CP and NF compiler-active; no whole Weil positivity, Masullo operator trace equivalence or RH/GRH result is claimed.

**PI025 verdict:** the exact F=Q radial test-domain dictionary can be grounded in the source's actual group decomposition and Haar product formula. On that genuine test domain, a specifically engineered smooth prime-/pole-/contact-null overlap test still excites a strictly positive original real Gamma functional, even after annihilating any finite initial Gamma atom set. The persistent missing source obligation is the unproved and apparently mis-normalized Chapter 13 trace statement, not this finite contact algebra.
