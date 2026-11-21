# PI020 — Prime-, pole-, and contact-null overlap test with strictly nonzero original Gamma response

**PI### Potential Interface, ANALYTIC-FIRST / NO NEW ACTIONS.** Research branch \`research/pi020-prime-pole-null-overlap-gamma-witness\` stacked solely on PI019 \`research/pi019-analytic-trace-domain-and-phase-cancellation\` and preceding PI work. NF numerical compiler recovery is separate. IV and CP remain analytic-first. There is **no new PR, workflow, Lean theorem candidate or compiler job**.

**Main result (classical mathematics):** an explicit nonzero \(D\in C_c^\infty(\mathbb R;\mathbb R)\) is constructible with
\[
\boxed{
D(0)=0,\quad \int D=0,\quad
\int D(u)e^{\pm u/2}\,du=0,\quad
D(\pm\log p^k)=0\ \ \forall p,k\ge1,
\qquad A_\Gamma(D)>0.
}
\tag{PI020-main}
\]
Here \(A_\Gamma\) is the EXACT PI018 original source-normalized archimedean Gamma distribution. The first four vanishings are independent of its **strictly positive** response. The test is also a difference of two legitimate smooth autocorrelations of equal mass, whose INDIVIDUAL diagonal tests have zero ordinary Mellin moment and both pole Mellin moments. This is a stronger discriminating interface test than phase information alone.

**Source/certification boundary:** The source identification of the original Weil-Lab Gamma distribution and the classical PI007–PI008 Fourier limits is as in PI018; the new witness is an elementary smooth-function and Laplace-transform theorem, not a Lean kernel acceptance or proof of Masullo Chapter 13. Its support is intentionally in a prime-power gap, NOT the frozen original IV collar. No claim is made that IV's original support-restricted positivity theorem applies to this new physical test.

## 1. Directly checked original manuscript distinction

Re-opened the actual 940-page Masullo *The Music of the Primes*, November 2026:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

**Printed p.519 (PDF index 518), Theorem 12.5.1.1:** The source explicitly assumes \(\varphi(C_F^1)=0\) and gives an all-zero-divisor spectral sum with multiplicity \(N(c)\) and the **shifted Mellin character** \(c|\cdot|_F^{-1/2}\), plus pole and local geometric integrals. Do not suppress the Mellin shift or pretend all zeros are on the critical line.

**Printed p.522 (PDF index 521), Theorem 13.3.1.1:** The source instead assumes moment vanishing (13.3.1.2), places a critical-line restriction \(\sigma(c)=1/2\) on the spectral sum and replaces \(N(c)\) by \(N_{\rm spec}(c)=\min(N(c),[F:\mathbb Q])\). Its displayed spectral term also uses \(c|\cdot|^{-1/2}\). For \(F=\mathbb Q\), \(N_{\rm spec}(c)=\min(N(c),1)\). This is **not the same divisor** as Theorem 12.5.1.1. The statement is accompanied by the footnote "Correct statement", the immediately following Theorem 13.3.1.2 says "Insert statement", and the printed outline says to state/prove the main theorems. **There is no Chapter 13 proof on this page establishing that the critical-line/capped divisor expression is equivalent to Chapter 12 on a different test hyperplane.**

These are SOURCE FACTS, not a claim the unproved Chapter 13 theorem is false. The shift \(c|\cdot|^{-1/2}\) is present on BOTH spectral formulas; the true unresolved difference concerns the divisor, multiplicities, and test domain. This corrects any misleading impression from a bare \(M(\varphi)(c)\) shorthand.

## 2. Select a compact support gap excluding every prime power

Fix exact rational endpoints
\[
q=\frac94,\quad a=\log q,\quad d=\log\frac{10}{9}.
\]
They satisfy
\[
2<\frac q{10/9}=\frac{81}{40}<q<
q\frac{10}{9}=\frac52<3,\qquad 0<d<a.
\]
Choose any nonzero nonnegative real \(\rho\in C_c^\infty((0,d))\). Set
\[
\boxed{\phi(x)=\left(\frac{d^3}{dx^3}-\frac14\frac d{dx}\right)\rho(x),\qquad
\psi(x)=\phi(x-a).}
\tag{PI020-bump}
\]
The differential polynomial is not the zero operator on nonzero compact smooth \(\rho\), so \(\phi\neq0\). Its translated supports are disjoint since d<a.

Let
\[
J=\|\phi\|_2^2>0,\quad
C(u)=\int_\mathbb R\phi(x)\phi(x-u)dx,\quad
s_\beta=\frac{\phi+\beta\psi}{\sqrt2},\quad
h_\beta(u)=\int s_\beta(x)\overline{s_\beta(x-u)}dx,
\quad \beta\in\{1,-1,i,-i\}.
\]
The actual Weil-Lab correlation convention agrees with this formula. Each hβ is smooth and compact and hβ(0)=J. For β∈{±1}, the *real-phase* difference is
\[
\boxed{D=h_1-h_{-1}=C(u+a)+C(u-a).}
\tag{PI020-difference}
\]
The support of C lies in [-d,d]. Hence D is supported in
\[
[-a-d,-a+d]\ \cup\ [a-d,a+d]
=\pm[\log(81/40),\log(5/2)].
\]
These intervals lie strictly between \(\pm\log 2\) and \(\pm\log3\), avoiding \(0\) and **every** logarithmic prime-power support \(\pm\log(p^k)\), p prime, k≥1 (indeed every \(\pm\log n\) for integer n≥2). Thus
\[
\boxed{D(0)=0,\quad D(\pm\log p^k)=0\ \forall p,k.}
\]
The hβ themselves have in addition a central bump C supported in (-d,d) with d<log2. This also contains **no nontrivial prime-power logarithm**. Consequently **each individual diagonal hβ is prime-sample-null**, not just its phase difference. All assertions concern the original arithmetic prime-sampling distribution, not a source theorem that Masullo's entire finite-place orbital kernels reduce to these samples without paying a separate dictionary.

## 3. Exact moment annihilator kills Ch.13's radial condition AND both pole terms

Define the bilateral Laplace moment
\[
R(z)=\int_\mathbb R \rho(x)e^{zx}dx.
\]
For every real z, R(z)>0 because \(\rho\ge0\), nonzero. Integrating by parts three times gives
\[
\boxed{
S(z):=\int_\mathbb R\phi(x)e^{zx}dx
=-z\left(z^2-\frac14\right)R(z).}
\tag{PI020-S}
\]
Thus S(z)=0 at **z=0 and z=±1/2**.

Since \(C\) is the correlation of real φ,
\[
\int_\mathbb R C(u)e^{zu}du=S(z)S(-z).
\]
The two-bump difference has entire Mellin/Laplace transform
\[
\boxed{
\mathcal L_D(z)=
2\cosh(az)S(z)S(-z)
=-2z^2\left(z^2-\frac14\right)^2
\cosh(az)R(z)R(-z).
}
\tag{PI020-Mellin}
\]

In particular,
\[
\boxed{\mathcal L_D(0)=\mathcal L_D(\tfrac12)
=\mathcal L_D(-\tfrac12)=0.}
\]
The vanishing at z=0 pays exactly the **F=Q norm-radial** Chapter 13 k=0 moment condition, PROVIDED the ordinary compact-fiber Haar disintegration and source test lift are matched. The values z=±1/2 are precisely the two pole moment functionals displayed in Chapter 12's (12.5.1.3) under the same norm-radial convention. The zero at z=0 is actually of order ≥2; the zeros at z=±1/2 are also of order ≥2, because both S(z) and S(-z) vanish there.

For each individual autocorrelation hβ, the transform is a product of the two weighted transforms of sβ. Since S(0)=S(±1/2)=0, both individual diagonals satisfy
\[
\boxed{
\int h_\beta=0,\qquad
\int h_\beta(u)e^{\pm u/2}du=0,\qquad
h_\beta(0)=J>0
}
\tag{PI020-diagonal}
\]
for all |β|=1. This gives genuine smooth, prime- and pole-sample-null **diagonal candidates in Chapter 13's stated moment hyperplane**, while their real-phase difference D lies simultaneously in Chapter 12's h(0)=0 domain.

**No equivalence between Ch.12 and Ch.13 is assumed** by using these domains. The exact Chapter 13 source statement is unproved/unfinished and has a different divisor.

## 4. Despite all null conditions, the original real Gamma form detects D STRICTLY

Take the actual PI007/PI018 physical Gamma kernel
\[
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}
=\sum_{n=0}^\infty e^{-\lambda_n|u|},
\qquad \lambda_n=2n+\frac12.
\]
All translated supports of D lie away from zero, so \(\int D K\) is absolutely convergent without contact subtraction. Because C and K are even,
\[
A_\Gamma(D)=-\int_\mathbb R D(u)K(u)du
=-2I_a,\qquad I_a=\int C(v)K(a+v)dv.
\]
For a>d, a+v>0 on supp C. The absolutely convergent exponential expansion yields
\[
\begin{aligned}
I_a
&=\sum_{n=0}^\infty e^{-\lambda_n a}S(-\lambda_n)S(\lambda_n)\\
&=-\sum_{n=0}^\infty
e^{-\lambda_n a}\lambda_n^2
\left(\lambda_n^2-\frac14\right)^2
R(\lambda_n)R(-\lambda_n).
\end{aligned}
\tag{PI020-I}
\]
The n=0 term vanishes exactly because \(\lambda_0=1/2\), a deliberately annihilated pole exponent. **EVERY n≥1 summand in -I_a is strictly positive**. Convergence is exponential because \(\rho\) is supported within length d<a. Therefore
\[
\boxed{\displaystyle
A_\Gamma(D)=
2\sum_{n=1}^\infty
e^{-\lambda_n a}\lambda_n^2
\left(\lambda_n^2-\frac14\right)^2
R(\lambda_n)R(-\lambda_n)>0.
}
\tag{PI020-GAMMA}
\]
At n=1, \(\lambda_1=5/2\) and \(e^{-\lambda_1 a}=(9/4)^{-5/2}=(2/3)^5=32/243\). The exact coefficient is
\[
\lambda_1^2(\lambda_1^2-\tfrac14)^2
e^{-\lambda_1 a}
=\frac{25}{4}\cdot36\cdot\frac{32}{243}
=\frac{800}{27}.
\]
So the first term alone produces the **strict quantitative bound**
\[
\boxed{
A_\Gamma(D)\ge
\frac{1600}{27}\,
R(-5/2)R(5/2)>0.}
\tag{PI020-BOUND}
\]
This is an exact analytic result for bona fide smooth compact tests. It is **not** a finite combinatorial graph calculation, quadrature, or an unverified spectral-operator value.

The exact local kernel value \(K(\log(9/4))=54/65\) is useful for source sanity, but by itself does not prove the strict sign, because C changes sign. The Laplace-product factorization above supplies the sign.

## 5. New information-theoretic NO-GO for insufficient cross-projection invariants

Let E contain smooth compact tests above and define the source data map
\[
\mathcal I(h)=\Big(
h(0),\ \int h,\ \int he^{u/2},\
\int he^{-u/2},\
\{h(\pm\log p^k)\}_{p,k}
\Big).
\]
Then \(\mathcal I(D)=0=\mathcal I(0)\), yet
\[
\boxed{A_\Gamma(D)>0=A_\Gamma(0).}
\tag{PI020-no-go}
\]

**Rigorous conclusion:** NO functional of only these data, even a nonlinear one \(F(\mathcal I(h))\), can reconstruct the full original Gamma pairing for all smooth compact h; it would assign the same output to D and to the zero function. This strictly strengthens support-graph-only insufficiency by explicitly retaining every prime-power point sample, the original contact evaluation and both pole Mellin moments, and the zero total Mellin moment.

It does **not** say that the full original Weil explicit formula is inconsistent: a genuine spectral zero-sum pairing (or full continuous archimedean input) could and must distinguish D from zero. Nor does it imply any spectral projection is false. It identifies one necessary piece of information that cannot be compressed away.

**Interpretation for IV and CP:** a candidate universal invariant must preserve some *nonlocal/test-shape-sensitive* archimedean information, or a genuine spectral evaluation supplying it, in addition to prime samples, phase edges, and finite moment data. Even a complex-valued full prime-interaction graph would see **no** samples on this D; that graph cannot recover its nonzero Gamma response by itself.

## 6. Explicit spectral fingerprint on the actual overlap subspace

Write the Riemann zero parameter as \(c=|\cdot|^{\sigma+i t}\) on the norm-radial, compact-fiber-trivial part for F=Q. Both printed sources use the shifted test transform
\[
\mathcal M_D(c|\cdot|^{-1/2})
=\mathcal L_D(\sigma-\tfrac12+i t).
\]
At a critical-line zero \(\sigma=1/2\), this becomes
\[
\boxed{
\mathcal L_D(it)
=2\cos(at)|S(it)|^2
=2\cos(at)\,
t^2(t^2+\tfrac14)^2
|\widehat\rho(t)|^2.}
\tag{PI020-critical}
\]
The Fourier sign does not change the *real even* cosine expression. This is a **phase-sensitive spectral fingerprint** of the identical original source test D, not a guessed spectral measure.

Consequently the precisely formulated unresolved overlap defect between the two source formulas is
\[
\begin{aligned}
\Delta_{\rm zero}(D)=&
\sum_{\sigma(c)\ne1/2}N(c)\,
\mathcal L_D(\sigma(c)-1/2+i\,t(c))\\
&+\sum_{\sigma(c)=1/2}
\bigl[N(c)-\min(N(c),1)\bigr]\,
\mathcal L_D(i\,t(c)).
\end{aligned}
\tag{PI020-defect}
\]
Here only compact-fiber-trivial characters survive the radial Q integration (with authentic Haar normalization). Both formulas must be interpreted using their original spectral regularization/source convergence; for Schwartz-frequency transforms of compact smooth h the usual zeta zero sums converge absolutely after standard zero-count estimates, but this is not an independently certified Masullo theorem.

**Necessary conditional compatibility:** if Ch.12 and Ch.13 indeed represent the SAME continuous global functional on the overlap test D with the SAME pole/prime/Haar normalizations, then
\[
\boxed{\Delta_{\rm zero}(D)=0.}
\tag{PI020-compatibility}
\]
No extra \(c\,D(0)\), \(d\int D\), \(e_\pm\int De^{\pm u/2}\), or \(\sum_{p,k}w_{p,k}D(\pm\log p^k)\) can repair a discrepancy: every one is exactly zero on D.

This is a **conditional spectral matching equation**, NOT an unconditional result that every zero is on the critical line or simple. The Chapter 13 theorem and the source-to-original-IV finite-part normalization are still missing. With distinct test spaces and different divisors, formal hyperplane gluing does NOT pay the spectral equivalence automatically.

On the two individual diagonal tests h±, however, Chapter 13's claimed critical-line spectral side (if valid and suitably normalized) would involve the nonnegative weights \(|\widehat{s_\pm}(t)|^2\). The difference has spectral density \(2\cos(at)|S(it)|^2\). It is thus possible to use a matched *diagonal* formula and its *contact-free difference* as two complementary source checks, with no prime or pole contamination. Neither is yet an actually evaluated, independently certified spectral sum.

## 7. Independent exact fraction preflight: no Actions, no Lean

The analytic-only \`scripts/pi020_prime_pole_moment_null_exact_preflight.py\` verifies:
- exact prime-power exclusion \(2<81/40<9/4<5/2<3\), using \(e^d=10/9\) (no approximate logarithms);
- the exact differential annihilator polynomial vanishes at \(0,1/2,-1/2\);
- \(\lambda_0=1/2\) yields zero Gamma coefficient, and all **500** checked later Gamma coefficients are positive fractions;
- the first nonvanishing Gamma coefficient is **800/27** in -I_a and **1600/27** in A_gamma(D).

Actual mathematics proves positivity for ALL n≥1 from the square polynomial and positivity of \(R(\pm\lambda_n)\); the finite Fraction regression checks implementation and constants only. No numerical integration or unproved Masullo spectral trace is promoted.

No PR, automatic GitHub Actions workflow, new Lean source or dispatch is part of PI020. Keep NF's compiler runs intact.

## 8. PI021 analytic-only next obligations

1. **Source-level signed local dictionary:** compare the literal Masullo (12.5.1.1) real-place integrals with the genuine Zeta23/IV original archimedean Gamma convention on this specific D; settle every factor 2π, Haar mass, sign and \(|g|^{1/2}\) before equating A_gamma with the manuscript geometric side.
2. **Independent overlap spectral evaluation:** derive both manuscript zero sums with the correct shifted Mellin parameter and zero multiplicity for the same D; inspect whether the Chapter 13 statement has an actual proof or is still an unsupported rewritten claim. Its critical-line/capped divisor cannot silently replace the full zero divisor.
3. **Spectral phase inequality:** if Ch.13 is valid, identify the exact cosine-weighted zero sum on the two individual diagonal autocorrelations and see whether the predicted signed contrast agrees with the positive \(\Gamma\) response. This is a *conditional test*, not a proof of RH.
4. **No-go transport:** use the genuinely zero prime/pole/contact/moment data but positive A_gamma(D) to reject any CP/IV cross-projection proposal that compresses the original Weil functional to these data only. Do not reject a proposal that retains the full spectral test transform or another equivalent continuous source carrier.
5. Maintain ANALYTIC-FIRST without creating more Actions jobs. No global positivity, RH or cross-projection equality is established.

**PI020 conclusion:** there is an explicit fully smooth source test whose prime, pole, identity-contact and total-Mellin-moment data ALL vanish, yet whose genuine Gamma distribution is strictly positive with an exact lower bound. This exposes an unavoidable information requirement of any true spectral/arithmetic interface and yields an exact overlap test on which no scalar normalization repair is possible.
