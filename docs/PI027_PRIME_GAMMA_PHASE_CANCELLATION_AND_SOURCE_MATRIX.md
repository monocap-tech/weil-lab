# PI027 — Two-channel prime/Gamma phase calibration, an exact n=3 cancellation separation, and the source spectral response matrix

**Independent Weil-Lab PI### Potential Interface | ANALYTIC-FIRST.** Parent branch: \`research/pi026-original-weil-phase-law-and-source-ratio\`. Canonical registry: issue #792. **No PR, Lean file, new GitHub Actions workflow, compiler dispatch, or NF/IV/CP mutation.** This stage adds exactly one analytic memo and one exact-arithmetic script. NF remains compiler-active; PI/IV/CP analytic-first.

**Main new classical theorem:** a genuine Schwartz autocorrelation family has full original signed Weil phase response
\[
\boxed{
W_a(h_\beta)=W(C_m)+[B_m(a)-P_m(a)]\,\mathrm{Re}\,\beta
}
\tag{PI027-phase}
\]
with separately source-identified archimedean \(B_m(a)>0\) and finite genuine von-Mangoldt prime \(P_m(a)\) channels. At a prime-free \(\log(9/4)\), \(P_m=0\) and the phase coefficient is positive. At \(a=\log3\), the single n=3 prime contribution \((\log3/\sqrt3)J_m\) strictly dominates the archimedean amplitude; the full phase coefficient is \(< -2J_m/9\). By continuity there is **at least one separation**
\[
\boxed{a_m^*\in(\log(27/10),\log3)}
\tag{PI027-crossover}
\]
with \(P_m(a_m^*)=B_m(a_m^*)>0\): a live original arithmetic interaction cancels the original Gamma phase response EXACTLY and all unit complex phases have the same complete original signed Weil evaluation. No global positivity or RH follows.

The result is not a bare graph observation. It preserves the original complex correlation orientation, source sign \(+\)pole \(-\)prime \(+\) Gamma, prime coefficients, and complex off-critical shifted Mellin test transform. It provides a falsifiable original arithmetic/Gamma normalization and information contract for spectral approaches. The independence of Masullo's unfinished Chapter13 trace claim remains explicit.

## 1. Exact source ledger, no generic formula substitutions

**Actual IV original arithmetic source reopened:** \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\` at independent IV024 \`research/iv024-original-prime-graph-ci-custody\`, Git blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`. Its literal original test is
\[
h_{s,t}(u)=\int_{\mathbb R}t(x)\overline{s(x-u)}\,dx,
\]
and its source \`neutralIV011OriginalMixed_arithmeticSplit\` gives
\[
\boxed{
W(h)=L_+(h)+L_-(h)
-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
  [h(+\log n)+h(-\log n)]
+A_\Gamma(h),
}
\tag{PI027-source}
\]
where \(L_\pm(h)=\operatorname{Zeta23.paperFT}(h)(\pm i/2)\), and
\[
A_\Gamma(h)=\frac1{2\pi}\int_{\mathbb R}
\operatorname{Zeta23.paperFT}(h)(r)
\bigl(\operatorname{Zeta23.EF.gammaBracket}(r)\bigr)dr.
\]
All exact signs and \(1/(2\pi)\) are from this SOURCE. For h with h(0)=0, PI007–PI018's established *classical* physical expression is
\[
A_\Gamma(h)=-\int_\mathbb R h(u)K(u)du,
\quad K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}},\ u\ne0.
\]
For h(0)≠0, PI018's compensated version is required and cannot be replaced by the divergent naive integral.

**Actual independent Masullo PDF re-opened with page-image inspection:** Alessandro Maria Masullo, *The Music of the Primes* (November 2026), https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf .
Printed p.519, Thm. 12.5.1.1 (PDF index 518), states the original full-divisor trace on \(\varphi(C_F^1)=0\) with canonical real factor \(1/2\), complex \(1/(2\pi)\) and finite \(\log(q_v)/\mu_v(O_v^\times)\).
Printed p.522, Thm. 13.3.1.1 (index 521), instead claims a critical-line-only spectral sum with \(N_{\rm spec}(c)=\min(N(c),[F:\mathbb Q])\) on a distinct Mellin moment domain and prints bare Tamagawa real/complex PV terms. Its surrounding "Theorem ??" and "Insert statement" text remains unfinished.
Appendix Theorem B.4.4.7 at printed p.623 (index 622) independently shows canonical coefficients \(1/M_v\), with \(M_v=2\) for a real place, \(2\pi\) for complex. **No authentic Chapter13 correction or proof was verified by PI027.**
For \(F=\mathbb Q\), the finite coefficient denominator \(\mu_p(\mathbb Z_p^\times)=1\), so the real place is the relevant displayed normalization discrepancy. See PI022–PI026 for the full source/Haar audit. None of these manuscript theorems is newly Lean-certified or independently validated.

## 2. One fixed genuine Schwartz bump, two distinct source arithmetic channels

Fix the EXACT width \(d=\log(10/9)>0\). Choose nonzero real \(\rho\ge0\) in \(C_c^\infty((0,d))\). For m≥1 put
\[
\lambda_j=2j+\frac12,\qquad
\phi_m=\partial_x\prod_{j=0}^{m-1}
   (\partial_x^2-\lambda_j^2)\rho,\quad
J_m=\int_\mathbb R|\phi_m(x)|^2dx>0.
\]
For any real separation a>d set \(\psi_{m,a}(x)=\phi_m(x-a)\), and for every |\(\beta\)|=1 define
\[
s_{\beta,m,a}=(\phi_m+\beta\psi_{m,a})/\sqrt2,\quad
C_m(v)=\int\phi_m(x)\phi_m(x-v)dx,\quad
h_{\beta,m,a}(u)=\int s_{\beta,m,a}(x)
\overline{s_{\beta,m,a}(x-u)}dx.
\]
Both bumps are disjoint, and each \(s_{\beta,m,a}\) is a genuine compact Schwartz test of the same support/mass \(J_m\) at **fixed a** for every unit beta. Exact **original IV** conjugation orientation:
\[
\boxed{
h_{\beta,m,a}(u)=C_m(u)
+\frac{\bar\beta}{2}C_m(u+a)
+\frac{\beta}{2}C_m(u-a),\quad h_{\beta,m,a}(0)=J_m.
}
\tag{PI027-correlation}
\]
All \(C_m\) supports lie inside \((-d,d)\). For a>d, the three correlation components are disjoint; all original prime samples from the central C_m vanish as \(d<\log2\).

Let \(S_m(z)=\int\phi_m(x)e^{zx}dx\) and \(R(z)=\int\rho(x)e^{zx}dx\). Integration by parts:
\[
\boxed{S_m(z)=-z\prod_{j<m}(z^2-\lambda_j^2)R(z).}
\]
Hence \(S_m(0)=S_m(\pm1/2)=0\), even for complex beta and ANY separation a. Therefore for each diagonal h:
\[
\boxed{
\int h_{\beta,m,a}=0,\quad
\int h_{\beta,m,a}(u)e^{\pm u/2}du=0,
}
\tag{PI027-pole-null}
\]
so **both** original literal \(\operatorname{paperFT}(h)(\pm i/2)\) pole terms vanish exactly. Each h also satisfies Masullo Chapter13's STATED \(F=\mathbb Q\) radial moment restriction; it does NOT satisfy Chapter12's h(0)=0. Their difference \(D_a=h_{1,m,a}-h_{-1,m,a}\) satisfies BOTH domains with zero contact. The exact norm-radial lift and compact Haar mass 1 are established from the genuine source in PI025.

## 3. Derive and separate the two source phase channels

For \(a>d\), every original prime sample \(n\ge2\) obeys \(\log n>d\), and \(\log n+a>d\), hence
\[
h_{\beta,m,a}(\log n)+h_{\beta,m,a}(-\log n)
=\mathrm{Re}\beta\,C_m(\log n-a).
\]
Therefore the literal original von-Mangoldt component is
\[
\boxed{
\operatorname{Prime}(h_{\beta,m,a})
=\mathrm{Re}\beta\,P_m(a),\qquad
P_m(a):=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 C_m(\log n-a).
}
\tag{PI027-prime}
\]
Only FINITELY many n contribute at every fixed a because supp C_m⊂(-d,d). This is an exact source-coefficient formula; a signed overlap graph alone would NOT give the amplitudes \(C_m(\log n-a)\).

Since K and C_m are even and the shifted terms lie away from 0, PI018's compensated Gamma distribution gives
\[
A_\Gamma(h_{\beta,m,a})
=A_\Gamma(C_m)-\mathrm{Re}\beta\,I_m(a),\quad
I_m(a)=\int_\mathbb R C_m(v)K(a+v)dv.
\]
For a>d, the physical source kernel expansion, \(R(\pm\lambda_n)>0\) for real λ, and \(S_m(\lambda)S_m(-\lambda)\le0\) imply
\[
\begin{aligned}
I_m(a)
&=-\sum_{n=m}^\infty e^{-\lambda_n a}
 \lambda_n^2\prod_{j<m}(\lambda_n^2-\lambda_j^2)^2
 R(\lambda_n)R(-\lambda_n)<0,\\
\boxed{
B_m(a):=-I_m(a)
=\sum_{n=m}^\infty e^{-\lambda_n a}
 \lambda_n^2\prod_{j<m}(\lambda_n^2-\lambda_j^2)^2
 R(\lambda_n)R(-\lambda_n)>0.
}
\end{aligned}
\tag{PI027-Gamma}
\]
Absolute convergence follows from the actual compact spatial support and a>d. B_m(a) is continuous (indeed real analytic) for a>d. P_m(a) is a locally finite sum of smooth compact correlations, hence continuous. **No RH or spectral trace assumption** is needed.

The full SOURCE \(\text{pole}-\text{prime}+\Gamma\) thus gives
\[
\boxed{
W_a(h_{\beta,m,a})
=W(C_m)+\bigl(B_m(a)-P_m(a)\bigr)\mathrm{Re}\beta.
}
\tag{PI027-FULL}
\]
The baseline W(C_m) is NOT asserted to be positive. This is an exact relative phase law and does not imply negative diagonals or any global Weil positivity.

## 4. Three source-exact anchor windows and an elementary, UNIFORM prime-dominance bound

### Gamma-only anchor \(a_g=\log(9/4)\)

The translated correlation windows are
\[
\pm[\log(81/40),\log(5/2)]
\subset\pm(\log2,\log3),
\]
so NO integer ≥2, hence no prime power, is sampled. Thus
\[
\boxed{P_m(a_g)=0,\quad \Theta_m(a_g)=B_m(a_g)>0.}
\tag{PI027-gap}
\]

### First live prime \(a_3=\log3\)

Now the translated support window is
\[
\pm[\log(27/10),\log(10/3)]
\subset\pm(\log2,\log4).
\]
The ONLY integer n≥2 in this positive window is n=3, and \(C_m(0)=J_m\). Therefore
\[
\boxed{P_m(a_3)=\frac{\Lambda(3)}{\sqrt3}J_m
=\frac{\log3}{\sqrt3}J_m>0.}
\tag{PI027-prime3}
\]

To bound the Gamma amplitude without ANY numerical estimate of rho, write
\(I_m(a)=\iint\phi_m(x)\phi_m(y)K(a+x-y)dxdy\).
Since supp φ_m is contained in an interval of length d and K decreases strictly on (0,∞), for a>d:
\[
\boxed{
0<B_m(a)\le |I_m(a)|\le
K(a-d)\bigl(\int|\phi_m|\bigr)^2
\le dK(a-d)J_m.
}
\tag{PI027-universal-B}
\]
The last inequality is Cauchy–Schwarz, using the support measure at most d.

Prove the elementary inequalities **analytically**:
\(d=\log(1+1/9)<1/9\);
\(a_3-d=\log(27/10)>\log2\);
\(K(\log2)=2\sqrt2/3<1\);
\(\log3=\int_1^3dt/t>2/3\);
and \(\sqrt3<2\). Thus
\[
B_m(a_3)<\frac{J_m}{9},
\qquad
P_m(a_3)>\frac{J_m}{3},
\]
so
\[
\boxed{
\Theta_m(a_3):=B_m(a_3)-P_m(a_3)<-\frac{2J_m}{9},\quad
W_{a_3}(h_1)-W_{a_3}(h_{-1})<-\frac{4J_m}{9}.
}
\tag{PI027-strict3}
\]
This bound holds UNIFORMLY for every order m≥1 and every such \(\rho\); it is not a sample fit or a claim that either complete diagonal value is negative.

### Original n=9 source anchor \(a_9=\log9\)

The window \((\log(81/10),\log10)\) contains just the integer n=9, with true original von-Mangoldt coefficient
\(\Lambda(9)/\sqrt9=\log3/3\). Thus
\[
P_m(a_9)=\frac{\log3}{3}J_m.
\]
Since \(a_9-d>\log8\), \(K(\log8)=16\sqrt2/63<1/2\), \(d<1/9\), and \(\log3>2/3\),
\[
\boxed{B_m(a_9)<\frac{J_m}{18},\quad
P_m(a_9)>\frac{2J_m}{9},\quad
\Theta_m(a_9)<-\frac{J_m}{6}.}
\tag{PI027-strict9}
\]
In particular \(W_{a_9}(h_1)-W_{a_9}(h_{-1})<-J_m/3\). This is an independent n=9 check with the **actual IV original arithmetic weight**, not an invented normalization.

## 5. Main new crossover existence theorem inside the FIRST prime interaction

Set \(a_0=\log(27/10)=\log3-d\). The translated support at \(a_0\) only touches the n=3 sample at its outer boundary \(u=\log3\). Because \(C_m\) is smooth with support compact INSIDE (-d,d), \(C_m(d)=0\); no other integer prime-power sample enters this window. Thus
\[
P_m(a_0)=0,\quad
\Theta_m(a_0)=B_m(a_0)>0.
\]
At \(a_3=\log3\), Section 4 proves \(\Theta_m(a_3)<-2J_m/9<0\). Since \(\Theta_m\) is continuous on \([a_0,a_3]\), the intermediate value theorem gives
\[
\boxed{\exists a_m^*\in(\log(27/10),\log3):
\ \Theta_m(a_m^*)=0.}
\tag{PI027-crossover}
\]

Furthermore, throughout this open interval the ONLY possible original prime contribution is n=3:
\[
P_m(a)=\frac{\log3}{\sqrt3}C_m(\log3-a).
\]
At the root,
\[
\boxed{
0<B_m(a_m^*)=P_m(a_m^*)
=\frac{\log3}{\sqrt3}C_m(\log3-a_m^*).
}
\tag{PI027-live-cancel}
\]
Hence the n=3 correlation sample is genuinely nonzero and positive at the root; a SUPPORT GRAPH can see the active edge, but not the cancellation.

For EVERY unit phase beta, the full original signed Weil value satisfies
\[
\boxed{W_{a_m^*}(h_\beta)=W(C_m).}
\tag{PI027-phase-flat}
\]
The Gamma term and the prime term each depend nontrivially on Re beta, but their original SIGNED sum is phase-flat. **This does not say the full Weil value vanishes or is positive**; only its relative phase coefficient vanishes.

This crossover is *existential*, not an effective numerical location of \(a_m^*\); no smooth rho was fixed to evaluate it. It holds for **every** real nonnegative nonzero rho of the stated compact class and every m≥1, with a possibly different root. The root is not asserted to be unique. It uses real analysis and actual source constants, not unproved zeta-zero data.

## 6. Exactly source-shifted COMPLEX spectral fingerprint, without assuming a trace theorem

Let the SOURCE positive angular Fourier transform be
\[
\Phi_m(z)=\int\phi_m(x)e^{izx}dx=S_m(iz),\quad z\in\mathbb C.
\]
Directly from the ORIGINAL oriented correlation, with beta of unit modulus,
\[
\boxed{
\widehat{h_{\beta,m,a}}(z)
=\Phi_m(z)\Phi_m(-z)\,
\frac{(1+\beta e^{iaz})(1+\bar\beta e^{-iaz})}{2}.
}
\tag{PI027-entire-transform}
\]
This is entire in z and has the genuine source \(+iru\) Fourier sign. For REAL t, \(\Phi_m(-t)=\overline{\Phi_m(t)}\), so
\[
\boxed{
\widehat h_{\beta,m,a}(t)
=|\Phi_m(t)|^2\bigl(1+\mathrm{Re}(\beta e^{iat})\bigr)\ge0.
}
\tag{PI027-critical-line}
\]
The pointwise nonnegative expression on real t is the standard Fourier positivity of an autocorrelation. It does **not** imply positive original W, which uses a signed complex zero divisor and arch/primes/poles.

At a nontrivial zeta zero \(\rho=\sigma+i\gamma\), the two Masullo source forms use the shift \(c|\cdot|^{-1/2}\); on this radial family the correct Fourier argument is
\[
\boxed{z_\rho=\gamma-i(\sigma-\tfrac12).}
\]
Then \(e^{iaz_\rho}=e^{a(\sigma-1/2)}e^{ia\gamma}\). If σ≠1/2 the frequency is NONREAL and the two exponential factors in (PI027-entire-transform) are **NOT** conjugate; the real-axis modulus-square formula must NOT be used at offcritical zeros. This is why a finite spectral zero count, support graph or phase-blind Hermitian mass cannot replace the original complex spectral test map.

The source Chapter12 full zero series and Chapter13 capped critical-only series are distinct and separately unverified on the same geometric functional. Nothing here asserts either as an accepted independent trace.

## 7. Exact two-channel source-normalization matrix on theorem-admissible differences

Define \(D_a=h_{1,m,a}-h_{-1,m,a}=C_m(u+a)+C_m(u-a)\). This smooth compact difference is supported away from u=0 and satisfies
\(D_a(0)=0,\int D_a=0,\int D_a e^{\pm u/2}=0\).
It is admissible for both **stated norm-radial test-domain conditions**, although the Chapter13 theorem itself remains unproved.

The three original source channels on D_a are:
\[
\operatorname{Pole}(D_a)=0,\quad
\operatorname{Prime}(D_a)=2P_m(a),\quad
A_\Gamma(D_a)=2B_m(a)>0.
\]
For the literal printed Masullo real-place Tamagawa PV on off-identity D, \(\mathsf R_\mu(D_a)=2\int D_aK=-4B_m(a)\). Their displayed local coefficients therefore give this exact comparison:

| Source formula | Pole | Prime/geometric finite | Real local | Signed total or required zero side |
|:--|:--|:--|:--|:--|
| Actual IV signed Weil | 0 | \(-2P_m(a)\) | \(+2B_m(a)\) (Gamma) | \(W(D_a)=2[B_m-P_m]\) |
| Masullo Ch12 printed, **IF trace identity holds** | 0 | \(+2P_m(a)\) on geometric side | \(\tfrac12\mathsf R_\mu=-2B_m(a)\) | \(Z_{12,I}(D_a)=2[B_m-P_m]\) |
| Masullo Ch13 printed, **IF its different identity holds** | 0 | \(+2P_m(a)\) on geometric side | \(\mathsf R_\mu=-4B_m(a)\) | \(Z_{13,\rm cap}(D_a)=4B_m-2P_m\) |

Thus the exact **conditional** required spectral defect on any source-matched D_a is
\[
\boxed{Z_{13,\rm cap}(D_a)-Z_{12,I}(D_a)=2B_m(a)>0.}
\tag{PI027-spectral-defect}
\]
Crucially, the difference does NOT depend on the prime sample P_m; it measures the manuscript's **distributed real-place factor-two** seam, not a contact correction. The values at the source anchors must be kept distinct:

- At \(\log(9/4)\), \(P=0\): \(Z_{12}=2B>0\) and \(Z_{13}=4B>0\).
- At \(\log3\), \(P=(\log3/\sqrt3)J_m\): \(Z_{12}< -4J_m/9\) and \(Z_{13}< -2J_m/9\).
- At \(\log9\), \(P=(\log3/3)J_m\): \(Z_{12}< -J_m/3\) and \(Z_{13}< -2J_m/9\).
- At the EXACT phase-flat crossing \(a_m^*\), \(P=B>0\):
\[
\boxed{W(D_{a_m^*})=Z_{12,I}(D_{a_m^*})=0,\qquad
Z_{13,\rm cap}(D_{a_m^*})=2B_m(a_m^*)>0}
\tag{PI027-source-falsifier}
\]
**ONLY IF the printed source trace formulas each hold under a truly common Q test/Haar/zero-strip/cutoff dictionary.** These are not computed spectral sums, and the source's full strip I is not assumed to equal all nontrivial zeros without proof. If an authenticated Chapter13 correction restores the canonical \(1/2\) real multiplier, these particular printed spectral predictions change; such a correction must be pinned and its theorem still proved independently.

The last line is a particularly clean *conditional* test: original full Weil and the Chapter12 zero divisor would vanish on the smooth phase-difference, whereas Chapter13's displayed critical-only/capped zero side would be forced to a nonzero positive value. A mass-contact, pole-moment or original prime-coefficient edit cannot erase their geometric difference, since those terms are source-matched on D and contact/pole vanish.

**Do not infer RH from the mismatch.** PI021's infinite spectral rigidity requires a whole **unbounded** translation half-line with a common identity, while the precise first-prime crossover and all-prime-free controls occur only in bounded windows. PI023–PI024 separately established a conditional boundary-pole obstruction under much stronger global source-matching assumptions. Neither result authorizes declaring the actual manuscript's intended corrected theorem false or proved.

## 8. Exact arithmetic regression and PI028 handoff

The **only** new executable file, \`scripts/pi027_prime_gamma_phase_source_matrix_exact.py\`, checks with \`fractions.Fraction\`:
- exact q=9/4, q=3, q=9 prime support windows and the left edge q=27/10 of the n3 overlap;
- squared rational inequalities \(K(\log2)^2=8/9<1\), \(K(\log8)^2=512/3969<1/4\), plus the rational consequences of the analytic log inequalities \(\log(10/9)<1/9\), \(\log3>2/3\);
- strict phase-coefficient margin bounds \(\Theta_3<-2J_m/9\), \(\Theta_9<-J_m/6\);
- **800** positive Gamma mode rational checks across m=1,…,8 for q=9/4 and q=9; and **28** exact formal source/conditional-Ch12/13 matrix checks, including the phase-flat root \((P=B>0)\).
Independent equivalent Python Fraction execution **PASS**. This is a regression for correct arithmetic and channel algebra, not a proof of the intermediate value theorem or of an actual smooth test integral; those are mathematical proofs in Sections 2–5. No CI/Lean, zeta zero roster, operator trace or RH claim.

**PI028, ANALYTIC-FIRST only:**
1. Explore stability and transversality of the crossover: under what additional conditions on rho does \(\Theta_m'(a_m^*)\ne0\)? Prove or refute uniqueness of a cancellation crossing inside the first prime window without assuming positivity of the signed bump correlation off center. Do not assert uniqueness from the IVT existence theorem.
2. Give a quantitative *root localization* for at least one fixed explicit \(C_c^\infty\) rho with interval-certified estimates, **without creating new GitHub Actions or treating external approximations as Lean certificates**. If effective localization is impossible with available interval tools, retain the analytic existence statement.
3. Compare the original IV exact signed n3/n9 prime coefficient against CP's actual spectral-test projection, preserving full complex offcritical \(\widehat h(z_\rho)\). A zero count or phase-blind support graph is not enough.
4. Require an authentic Chapter13 revision/proof and exact canonical Haar factors before claiming Masullo spectral identification. Keep NF compiler-active and PI/IV/CP analytic-first.

**PI027 verdict:** actual source Gamma and prime channels produce **opposite relative-phase signs** on carefully controlled smooth Schwartz diagonals. There is necessarily a live first-prime exact cancellation separation, and the two printed Masullo spectral formulas require a visibly different zero-side response there. This is a falsifiable, source-conserving compatibility probe, not a solution of global Weil positivity or RH.
