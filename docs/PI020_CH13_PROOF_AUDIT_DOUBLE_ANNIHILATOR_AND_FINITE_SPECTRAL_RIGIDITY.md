# PI020 — Chapter 13 proof audit, double-annihilator spectral defect, and finite-divisor phase rigidity

**Weil-Lab independent PI### Potential Interface, ANALYTIC ONLY.** Stacked on \`research/pi019-analytic-trace-domain-and-phase-cancellation\`. Source status at creation: **no new Lean files, no GitHub Actions workflow, no pull request**. Existing PI compiler backlog stays frozen; NF numerical CI independently remains active; IV and CP maintain their own analytic investigations.

**Central result:** the *claimed* Chapter 13 critical-line/capped-multiplicity trace formula has NO displayed proof of its divisor replacement in Chapter 13. Its agreement with Chapter 12 on the overlap of their test domains would require a precise spectral-defect identity. PI020 exhibits a genuine family of smooth compact tests in that overlap, proves a **finite-divisor spectral rigidity lemma** for phase-opposed pairs, and states exactly what is missing for the actual infinite zeta divisor. **No proof of Chapter 13, RH, spectral equivalence, or global Weil positivity is claimed.**

## 1. Primary-source audit: the missing step is mathematically substantial

Direct visual and text review of Alessandro Maria Masullo, *The Music of the Primes*, November 2026 manuscript, https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf :

- **Theorem 12.5.1.1, printed pp.519–520 (PDF indices 518–519)**: assumes \(\varphi(C_F^1)=0\), and its spectral sum uses **the actual full zero multiplicity \(N(c)\)** over zeros in a specified vertical strip \(\Omega(C_F)_I\); the geometric expression has two pole Mellin evaluations and the real, complex and nonarchimedean local terms. The displayed proof on p.520 cites the global kernel/source results of preceding chapters and concludes that very identity. It **does not itself exhibit a capped, critical-line-only spectral equality on a different test domain**.
- **Theorem 13.3.1.1, printed p.522 (PDF index 521)**: states a different result on a subspace of functions annihilated by \(0\le k\le[F:\mathbb Q]-1\) Mellin-moment evaluations. It defines \(N_{\rm spec}(c)=\min(N(c),[F:\mathbb Q])\), and the spectral sum is **restricted to \(\sigma(c)=1/2\)**. Its geometric side has the two pole terms and local real/finite contributions, with the author's stated convergence and functional identity. This is not a restatement of Theorem 12.5.1.1.
- **Proof audit:** Chapter 13 consists, at the relevant point, of this statement and no displayed derivation. The very next sentence invokes **"Theorem ??"**, and Theorem 13.3.1.2 has the visible footnotes **"Insert statement"** and **"State and prove the Main Theorems"**. Chapter 14 (printed p.528) discusses an expected multiplicity bound and includes a visible editorial instruction **"Correct this subsection"**. Thus the file contains a **source-claimed theorem, not a completed proof of the full/capped/critical spectral replacement**. This observation is not a proof the theorem is false; it is a clear unresolved justification obligation.
- **Scope warning:** the Chapter 12 sum is over a specified vertical strip. A comparison with *every* nontrivial zeta zero requires an allowed strip containing them and verification that all other source terms and the zero-indexing conventions match. Do not silently enlarge \(I\).

Original Weil-Lab source anchors (not newly claimed compiler accepted): PI007 finite arch kernel, PI008 digamma symbol, PI018 compensated full-test Gamma distribution and PI019 smooth phase-correlation tests. PI019 mathematical memo Git blob \`6848cc451ebdb882ca5e710dfb73bc756ac366b9\`.

## 2. The exact common-domain test and source zero-divisor defect

Specialize to \(F=\mathbb Q\) and norm-radial functions
\(\varphi_h(g)=h(\log|g|_\mathbb Q)\).
**Subject to the actual Haar disintegration and \(\mathcal D(C_\mathbb Q)\) membership**, the two source vanishing conditions reduce to
\[
E_e=\{h\in C_c^\infty(\mathbb R;\mathbb C):h(0)=0\},
\qquad
E_m=\{h:\int_\mathbb R h(u)\,du=0\}.
\]
The overlap \(E_{em}=E_e\cap E_m\) is codimension **two** in the full smooth compact radial test space.

With the source's Mellin and positive Fourier conventions, put
\[
\widehat h(z)=\int_\mathbb R h(u)e^{izu}\,du.
\]
For a zero \(\rho=\beta+i\gamma\) of \(\zeta\), define its shifted Fourier argument
\[
z_\rho=\gamma-i(\beta-\tfrac12)
\quad\Longrightarrow\quad
\int h(u)e^{(\rho-\tfrac12)u}du=\widehat h(z_\rho).
\]
On the critical line \(\beta=1/2\), this reduces to the *real* Fourier argument \(\gamma\). Let \(m(\rho)\) denote its full multiplicity.

Provided the source theorem's zero-strip covers the zeros being compared and both sums define actual continuous linear functionals, the difference between its **full** and **critical/capped** spectral expressions is
\[
\boxed{
\mathfrak B(h)=
\sum_{\substack{\rho\ \mathrm{nontrivial}\\\beta\ne1/2}}
m(\rho)\,\widehat h(z_\rho)
+
\sum_{\substack{\rho\ \mathrm{nontrivial}\\\beta=1/2}}
\bigl(m(\rho)-\min(m(\rho),1)\bigr)\widehat h(\gamma).
}
\tag{PI020-defect}
\]
This formula is a mathematical **source-dictionary candidate**, not an independently verified identification of all author-specific spectral cutoff factors. A source-accurate comparison must still check the actual \(\Omega(C_F)_I\) indexing and zero-character multiplicity conventions.

**Necessary overlap identity:** if Theorems 12.5.1.1 and 13.3.1.1 both hold, with the SAME pole/prime/arch side and Haar/cutoff normalization, then
\[
\boxed{\mathfrak B(h)=0\quad\text{for every }h\in E_{em}.}
\tag{PI020-overlap}
\]
The two scalar corrections \(c\,h(0)\) and \(d\,\int h\) vanish identically on \(E_{em}\) and therefore CANNOT repair a counterexample to (PI020-overlap).

No off-critical zeta zero or multiple noncentral zero is asserted to exist. Equally, no theorem removing either possibility has been proved here. Those are precisely the difficult spectral possibilities the two source formulas distinguish.

## 3. Exact smooth phase witness and its ENTIRE spectral transform

Choose \(\rho_0\in C_c^\infty(\mathbb R;\mathbb R_{\ge0})\), nonzero, and put \(\phi=\rho_0'\). Choose \(a>\operatorname{diam}(\operatorname{supp}\rho_0)\) and \(\psi(x)=\phi(x-a)\). Define four genuine smooth autocorrelation pairs from
\[
s_\beta=\frac{\phi+\beta\psi}{\sqrt2},
\quad\beta\in\{1,-1,i,-i\},\qquad
h_\beta(u)=\int s_\beta(x)\overline{s_\beta(x-u)}dx.
\]
Let \(C(u)=\int\phi(x)\phi(x-u)dx\).
Then
\[
\begin{aligned}
D_e(u)&:=h_1(u)-h_{-1}(u)=C(u+a)+C(u-a),\\
D_o(u)&:=h_i(u)-h_{-i}(u)=i\bigl(C(u-a)-C(u+a)\bigr).
\end{aligned}
\tag{PI020-phase}
\]
Because \(\int\phi=0\), \(\int C=(\int\phi)^2=0\). By separation, \(C(\pm a)=0\). Thus BOTH tests satisfy
\[
\boxed{D_e(0)=D_o(0)=0,\qquad \int D_e=\int D_o=0.}
\tag{PI020-admissible}
\]
Each is a legitimate \(C_c^\infty\) function. Under the verified norm-radial test-space dictionary these lie in BOTH manuscript subspaces. Unlike the PI018 auxiliary Lipschitz compensator, neither test has a smoothness defect.

Define the entire Paley–Wiener transform
\[
R(z)=\int_\mathbb R\rho_0(x)e^{izx}dx,\qquad
\widehat C(z)=z^2 R(z)R(-z).
\]
The sign follows from \(\widehat{\rho_0'}(z)=-iz R(z)\).
Translation yields the exact entire identities
\[
\boxed{
\widehat{D_e}(z)=
2z^2\cos(az)R(z)R(-z),\qquad
\widehat{D_o}(z)=
i\bigl(e^{iaz}-e^{-iaz}\bigr)z^2R(z)R(-z)
=-2z^2\sin(az)R(z)R(-z).
}
\tag{PI020-witness}
\]

**Central blindness is explicit:** \(\widehat{D_e}\) vanishes to at least second order at \(z=0\); \(\widehat{D_o}\) to at least third order. Thus no finite collection of these exact phase tests detects a discrepancy supported only at the central argument \(z=0\). This respects the manuscript's separate discussion of central-zero multiplicities; do not claim central simplicity from these tests.

**Noncentral sensitivity:** for any specified \(z\ne0\) in a FINITE set, choose a sufficiently narrow nonnegative bump \(\rho_0\) that \(R(z)R(-z)\ne0\); this follows by normalizing its mass and shrinking its support, yielding \(R(z)\to1\). The even/odd translation factors together cannot vanish at the same \(z\) since \((e^{iaz}+e^{-iaz})\) and \(i(e^{iaz}-e^{-iaz})\) cannot both be zero.

At the original old n=9 offset \(a=\log9\), a genuine smooth \(D_e\) has the archimedean Gamma response \(A(D_e)>0\) by PI019's derivative-bump Laplace sign calculation. That *single* arch response is NOT the whole prime-plus-poles spectral defect \(\mathfrak B(D_e)\); original IV's prime n9 phase term must be accounted for independently.

## 4. New finite-divisor spectral rigidity theorem (genuine proof, no RH assumed)

This is a strictly **finite-dimensional mathematical lemma**.

Fix finitely many **distinct noncentral** complex spectral arguments \(z_1,\ldots,z_M\ne0\) and coefficients \(b_1,\ldots,b_M\in\mathbb C\). Define
\[
B(h)=\sum_{j=1}^M b_j\,\widehat h(z_j).
\]
Choose a real nonnegative smooth bump \(\rho_0\) with small enough support that \(R(\pm z_j)\ne0\) for every j. For all translations \(a\) in an arbitrary nonempty open interval with \(a>\operatorname{diam}\operatorname{supp}\rho_0\), build the two smooth phase-difference tests \(D_e(a),D_o(a)\).

**Theorem PI020-FINITE-RIGIDITY.** If
\[
B(D_e(a))=B(D_o(a))=0
\quad\text{for every such }a,
\]
then \(b_1=\cdots=b_M=0\).

**Proof.** Set \(t_j=b_jz_j^2R(z_j)R(-z_j)\). The even and odd hypotheses say
\[
\sum_jt_j(e^{iaz_j}+e^{-iaz_j})=0,\quad
\sum_jt_j i(e^{iaz_j}-e^{-iaz_j})=0.
\]
Adding/subtracting them isolates
\[
\sum_jt_je^{iaz_j}=0
\quad\text{and}\quad
\sum_jt_je^{-iaz_j}=0.
\]
Distinct complex exponentials are linearly independent on any nonempty open interval: evaluate successive derivatives at one interior point to obtain an invertible Vandermonde system. Thus \(t_j=0\) for all j. Because \(z_j\ne0\) and \(R(\pm z_j)\ne0\), each \(b_j=0\). QED.

**This is a new concrete preservation/obstruction law for finite spectral projections:** agreement on BOTH phase families across a real translation interval forces equality of all *noncentral* finite spectral coefficients, not just equality up to \(c\,h(0)\) or a support graph. No zero location hypothesis is used.

**Important limit:** the actual zeta divisor is INFINITE. PI020-FINITE-RIGIDITY cannot be applied termwise to an infinite formal spectral difference without proving the correct convergence/analytic continuation and exponential-series uniqueness on the varying support family. Establishing that infinite-divisor uniqueness is a genuinely difficult missing hypothesis, possibly as strong as the zero-location/multiplicity issue. Do not promote the finite theorem to global zero-divisor equality, RH or simplicity.

## 5. General annihilator theorem: what the overlap does NOT see

On \(E=C_c^\infty(\mathbb R;\mathbb C)\), let \(e(h)=h(0)\), \(m(h)=\int h\). They are linearly independent. The source intersection is \(E_{em}=\ker e\cap\ker m\).

**Double-annihilator lemma:** a complex-linear functional \(B:E\to\mathbb C\) vanishes on \(E_{em}\) **if and only if**
\[
\boxed{B(h)=c\,h(0)+d\int h(u)du}
\tag{PI020-annihilator}
\]
for uniquely determined constants \(c,d\in\mathbb C\).

Proof: choose a contact-normalized smooth \(f\) with \(f(0)=1,\int f=0\) (normalize the derivative-bump autocorrelation) and a smooth \(g\) supported away from 0 with \(g(0)=0,\int g=1\). Write every h as
\(h=[h-e(h)f-m(h)g]+e(h)f+m(h)g\), with first term in the intersection. Hence \(B(h)=B(f)e(h)+B(g)m(h)\).

**Two limitations:**
1. Even a successful match of Chapter 12/13 on the ENTIRE intersection does not by itself exclude a \(c\,h(0)+d\int h\) distributional discrepancy on the full E. It only identifies the defect modulo these two scalar functionals.
2. If a *finite* spectral divisor difference defines B, the much stronger analytic argument of Section 4 eliminates all noncentral finite spectral modes; in distribution language, a finite sum of nonconstant exponentials cannot equal a contact delta plus a constant. That argument still needs a separate infinite-divisor upgrade for actual zeta zeros.

The PI019 transversality *gluing* theorem remains correct **conditionally**: if both entire source functionals are genuinely defined on their respective hyperplanes and agree on their overlap, there is a unique linear gluing on E. It does not say two different spectral divisors already agree, nor that the resulting gluing is a positive self-adjoint trace operator.

## 6. Falsifiable source spectral compatibility conjecture PI020-X

**Given:** (i) correct \(F=\mathbb Q\) norm-radial Haar/test-space identification; (ii) a permitted common zero strip and full zero multiplicity; (iii) independently proved Chapter 12 and Chapter 13 trace identities with the SAME actual global pole/prime/arch geometric functional, rather than an author-labeled theorem without a proof; (iv) sufficient zero-series convergence and spectral-distribution uniqueness to exchange sums with the whole \(a\)-family of smooth tests.

**Require:**
\[
\boxed{
\mathfrak B(D_e(a))=\mathfrak B(D_o(a))=0
\quad\text{for all }a>\operatorname{diam}\operatorname{supp}\rho_0.
}
\tag{PI020-X}
\]
This is the precise, phase-bearing, double-contact-free source preservation law. The infinite-divisor statement remains a **CONJECTURAL COMPATIBILITY GATE**, not a proved equality.

**Falsifiers:** a valid source-level evaluation of either difference yielding a nonzero result after ALL original arithmetic places and poles are accounted for; a proven failure of Chapter 13's source trace theorem under its actual hypotheses; or an authenticated discrepancy in either norm lift, zero-strip indexing, multiplicity weight or cutoff normalization. Such a failure cannot be fixed by adding \(c\,h(0)\) or \(d\int h\) because both vanish on the tests.

**Positive conditional consequence, not a proof:** on moment-zero autocorrelations \(h_{s,s}\), the Chapter 13 capped critical-line spectral side would take the form
\[
\sum_{\gamma:\,\zeta(1/2+i\gamma)=0}
 \min(m_\gamma,1)\,|\widehat s(\gamma)|^2\ge0.
\]
If this sum is genuinely proved equal to the ORIGINAL globally normalized signed Weil form on those h, it would imply nontrivial restricted Weil positivity. That conclusion needs the full source proof, not just the visibility of a formally positive sum. It does not establish RH, and the restriction \(m(h)=0\) must not be confused with the complete Weil positivity criterion.

## 7. Independently checked exact finite regressions, no compiler/Actions work

\`scripts/pi020_double_annihilator_fourier_witness.py\` uses \`fractions.Fraction\` only for (a) the *formal narrow-bump limit* of the exact smooth entire transform, and (b) the dual-basis double-annihilator law.

At \(a=\log9\), in the **formal delta limit only** (not an admissible test),
\[
\widehat D_e(ik)=-k^2(9^k+9^{-k}),\qquad
\widehat D_o(ik)=ik^2(9^k-9^{-k}),\quad k\in\mathbb N.
\]
For k=1 this is **−82/9** and **\(i\,80/9\)**. For k=2 it is **−26248/81** and **\(i\,26240/81\)**. These check the noncentral sign/coefficient and the central z=0 blindness without floating-point oscillatory fitting. They do NOT assert an actual zeta zero at any such argument.

Independent equivalent Fraction execution **PASS** for **250** noncentral even and **250** noncentral odd mode checks and **1,024** dual-functional intersection identities. No actual zeta zeros were evaluated. The finite-rigidity lemma's proof is mathematical and not replaced by the script.

**NO new PR, .lean file, Actions workflow, or CI run** is created for PI020; only this memo and the exact script are committed on the analytic branch. NF compiler certification remains independent; IV/CP/PI analytic-first.

## 8. Next PI021 analytic-only gate

1. Audit the source's exact hypothesis under which Theorem 12.5.1.1 is claimed to imply Theorem 13.3.1.1. Demand an explicit proof of **full divisor → critical-only capped divisor** on the moment-zero domain, not a citation to the Chapter 12 identity with different hypotheses.
2. Test whether the source's zero spectral series defines a distribution of sufficient growth for the **infinite** counterpart to PI020-FINITE-RIGIDITY. If only a cutoff equality can be shown, track its boundary/renormalization term explicitly before passing to infinite limits.
3. Preserve \(\widehat D_e,\widehat D_o\) with arbitrary translation \(a\) and a narrow nonnegative bump as **phase-bearing continuous spectral probes**. Do not mistake a single \(a=\log9\) comparison for the full family or use the original IV024 support graph outside its fixed window.
4. If the Chapter 12/13 overlap equality survives a true source proof, test an actual zero-Mellin-moment diagonal autocorrelation to calibrate the remaining contact constant against PI018. If not, report the exact source obstruction. The PI006 one-contact ambiguity and PI019 double-domain gluing remain conditional.
5. Compare to IV original n=9 signed phase amplitudes and CP genuine finite zero roster only through a **test-level, convention-preserving** dictionary. Neither a support graph nor a finite zero count can replace the infinite divisor trace/cutoff theorem.

**PI020 conclusion:** the critical obstacle is not a missing scalar renormalization but the unproved replacement of a full zero divisor by a critical-line, capped-multiplicity divisor on a different test class. We now have explicit smooth double-admissible phase probes and a rigorous finite-spectral injectivity mechanism; upgrading that mechanism to the actual infinite source trace remains open. No RH/GRH or full Weil positivity claim.
