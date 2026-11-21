# PI002 — Exact norm/Mellin dictionary, Q-Haar volume, and a genuinely prime-active mixed trace test

**Lane:** PI### Potential Interface, stacked only on PI001 #793, under PI registry #792. **Independent of** CP001 #790, IV020 #788 and NF750 #789. Existing Lean phases continue without interruption.

**Status:** mathematical source-domain/transform derivations + independent exact rational geometry/moment sanity checker. **Not** a Lean theorem, accepted Masullo trace proof, or equality between complete Weil and trace formulas. **No RH/GRH.**

## 0. Primary source custody (not inferred)

Alessandro Maria Masullo, *The Music of the Primes*, release PDF:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

- **Chapter 1, p. 28 (PDF index 27)**: test assumptions (1) \(\varphi\in\mathcal D(C_F)\), smooth and compactly supported, and (2) \(\varphi(C_F^1)=0\); defines Mellin \(M(\varphi)(c)=\int_{C_F}\varphi(g)c(g)d\bar\mu(g)\); local geometric terms and zero side shown.
- **Theorem 12.5.1.1, pp. 519–520 (PDF index 518–519)**: repeats \(\varphi\in\mathcal D(C_F)\) and \(\varphi(C_F^1)=0\), with zero terms \(M(\varphi)(c|\cdot|_F^{-1/2})\). It is a manuscript assertion, not independently certified. The zero sum is written with a specified relative strip \(I\); it is **not automatically** the full zero-divisor functional on all nontrivial zeros.
- **Definition A.3.2.1, p. 560 (PDF index 559)**: \(\bar\mu_1(C_F^1)=2^{r_1}(2\pi)^{r_2}h_F R_F/(|d_F|^{1/2}w_F)\). The usual \(\mathbb Q\) invariants \(r_1=1,r_2=0,h=1,R=1,d=1,w=2\) give precisely \(\boxed{\bar\mu_1(C_{\mathbb Q}^1)=1}\).
- **A.3.3, p. 561 (PDF index 560)**: continuous section to the idelic norm, product decomposition and Haar factor \(dt/t\otimes\bar\mu_1\) (at the idelic/group quotient level). This justifies disintegration in the trivial-character class-group sector; it is not a generic permission to disregard normalization for other fields.

For independent check of the compact norm-one class group/topological splitting: K.S. Kedlaya, *Idèles and class groups*, https://kskedlaya.org/cft/sec_ideles.html , and H. W. Lenstra, *The Idèle Class Group*, https://websites.math.leidenuniv.nl/algebra/Lenstra-Idele.pdf .

## 1. Exact norm pullback and admissibility

Let \(s,t\in C_c^\infty(\mathbb R;\mathbb C)\) be genuine physical Schwartz tests. Fix the original PI001 orientation
\[
h_{s,t}(u)=\int_{\mathbb R}t(x)\,\overline{s(x-u)}\,dx.
\]
This is a smooth compactly supported correlation. Its support lies in \(\operatorname{supp}(t)-\operatorname{supp}(s)\). Write \(\ell(g)=\log|g|_{\mathbb Q}\) and define \(\Phi_{s,t}=h_{s,t}\circ\ell\) on \(C_{\mathbb Q}\).

- **Norm-one gate:** \(\ell(C_{\mathbb Q}^1)=0\), so \(\Phi|_{C_{\mathbb Q}^1}=h_{s,t}(0)=\int t\bar s\). Hence vanishing is equivalent to \(\langle t,s\rangle_{L^2}=0\).
- **Full test domain, as a mathematical deduction from classical structure:** the norm-one class group \(C_{\mathbb Q}^1\) is compact; a continuous norm section identifies \(C_{\mathbb Q}\simeq C_{\mathbb Q}^1\times\mathbb R_{>0}\). The inverse image of the compact support \(\exp(\operatorname{supp}h)\) is compact. In these coordinates \(\Phi(k,e^u)=h(u)\): constant (hence locally constant/smooth in the totally disconnected compact kernel variable) and smooth in \(u\). Thus \(\Phi\in\mathcal D(C_{\mathbb Q})\) under the smooth-compact support convention used in Theorem 12.5.1.1. **A matching Lean implementation of the author's exact Bruhat test-space definition is not supplied; do not promote this pen-and-paper proof to formal certification.**
- **Isotypic restriction:** \(\Phi\) is invariant under \(C_{\mathbb Q}^1\) and so pairs only with characters trivial on that subgroup. More generally, for any character \(\chi\) whose restriction to \(C_{\mathbb Q}^1\) is nontrivial, its compact-fiber integral against \(\Phi\) vanishes by character orthogonality. No claim about arbitrary Dirichlet or Hecke characters.

## 2. Actual Q Tamagawa Haar/Mellin calculation

Use Masullo's \(\bar\mu\) on \(C_{\mathbb Q}\), the multiplicative quotient measure \(dt/t\), and the norm-one fiber measure \(\bar\mu_1\) with **volume one**. By disintegration:
\[
M(\Phi_{s,t})(|\cdot|_{\mathbb Q}^{z})
 =\int_{C_{\mathbb Q}}\Phi_{s,t}(g)|g|_{\mathbb Q}^{z}\,d\bar\mu(g)
 =\int_0^\infty h_{s,t}(\log v)v^z\,\frac{dv}{v}
 =\int_{\mathbb R}h_{s,t}(u)e^{zu}\,du.
\]
Define the bilateral Laplace transform \(H_f(z)=\int_{\mathbb R}f(x)e^{zx}\,dx\). By absolutely justified Fubini and \(y=x-u\):
\[
\begin{aligned}
\int_{\mathbb R}e^{zu}h_{s,t}(u)\,du
 &=\int_{\mathbb R^2}t(x)\overline{s(y)}e^{z(x-y)}dxdy\\
 &=H_t(z)\overline{H_s(-\overline z)}.
\end{aligned}
\]
Thus the **exact analytical identity** (no RH assumption) is
\[
\boxed{M(\Phi_{s,t})(|\cdot|^z)=H_t(z)\overline{H_s(-\bar z)}}.
\]

For the relative-center zero parameter \(z=\rho-\tfrac12\), Masullo's Theorem 12.5.1.1 uses
\[
M(\Phi)(|\cdot|^{\rho-1/2})
=H_t(\rho-1/2)\overline{H_s(1/2-\bar\rho)}.
\]
This is the reflected centered zero-side **summand** from CP001 in compatible conventions; this fact does **not** identify Masullo's spectral strip sum, multiplicity conventions and operator trace with the complete original divisor functional.

His **two polar evaluations** transform exactly into
\[
M(\Phi)(|\cdot|^{\pm 1/2})
 =H_t(\pm1/2)\overline{H_s(\mp1/2)}.
\]
Their sum matches the usual Hermitian-polarized pole pairing. Matching the *whole* Gamma/digamma and local p-adic geometric distribution is still open.

## 3. Critical improvement over PI001: choose a prime-active mixed test

PI001 used the old–new disjoint pair. It belongs to the domain gate, but its genuine mixed prime term is zero by construction; it is therefore a weak test of the arithmetic leg of a trace dictionary.

PI002 instead freezes an *old–old off-diagonal* pair still disjoint at zero but with a genuine n=9 overlap:

\[
c_-=-1099/1000,\quad c_+=1099/1000,\quad a=1/2000,
\]
\[
s=b_{c_-,a},\quad t=b_{c_+,a},\quad
b_{c,a}(x)=\begin{cases}
\exp(1-a^2/(a^2-(x-c)^2)),&|x-c|<a,\\
0,&\text{otherwise}.
\end{cases}
\]

Both are genuine nonnegative \(C_c^\infty\) bumps inside the two original strict collars, and their supports are disjoint. Hence \(h_{s,t}(0)=0\) and \(\Phi_{s,t}\) is trace-domain admissible by sections 1–2.

But the center difference \(c_+-c_- =1099/500\) obeys
\[
0<1099/500-\log 9<1/1000=2a.
\]
Therefore the translated supports meet in an interval of **strictly positive length** at \(u=\log9\), and the integrand is strictly positive there. Thus
\[
\boxed{h_{s,t}(\log9)>0}
\]
while \(h_{s,t}(-\log9)=0\). For all other original active \(2\le n<10\), both signed shifts miss this pair's support difference. The genuine source coefficient is \(\Lambda(9)/\sqrt9 =\log3/3>0\); its exact placement/sign in the complete mixed Weil/trace expression must be checked, not assumed.

This **nonzero n=9 mixed term is the first falsifiable coefficient-level arithmetic target**. It tests the local geometric prime-power term instead of merely agreeing where the prime term is identically zero.

The script \`scripts/pi002_mellin_haar_n9_preflight.py\` verifies the rational logarithmic inequalities using rigorous atanh tails; it also validates the formal Taylor moments of the Laplace-correlation identity on independent compactly supported polynomial surrogate tests. Surrogates are NOT the actual smooth source bumps and this computation is not a Lean proof.

## 4. What is now established, and what still fails

**Analytic deductions verified from primary source + standard classical facts:**
- the \(\mathbb Q\) Tamagawa norm-one fiber has volume one in Masullo's convention;
- the norm pullback of any compact smooth \(h\) has compact support and the right smoothness under the classical idele-class splitting;
- \(\Phi(C_{\mathbb Q}^1)=0\iff h(0)=0\);
- Mellin of the norm pullback is the exact reflected Laplace product for both polar and centered-zero arguments;
- the proposed old–old real nonnegative smooth pair is domain-admissible yet has a strictly nonzero \(n=9\) correlation.

**Unverified mathematical/interface obligations:**
1. Directly match a **single local p=3, exponent 2** geometric term in Masullo's Theorem 12.5.1.1 to the original Weil von Mangoldt coefficient \(\log 3/3\) times the chosen \(h(\log9)\), including Haar, signs, factors of 2 and whether the author's \(\varphi(g)\) versus \(\varphi(g^{-1})\) orientation matches this ordered pair.
2. Match all \(\Gamma\)/digamma local distributions and all genuine pole constants in the **complete** mixed source identity; apparent agreement of Mellin pole evaluations is not the whole formula.
3. Compare the author's specified relative spectral strip \(I\), counting multiplicity \(N(c)\), and subsequent chapter 13 \(N_{\rm spec}\) truncation against the full-multiplicity Weil sum. No all-zero equality is implied without a strip exhaustion/tail theorem.
4. Source-accurate Lean theorem stating full \(\mathcal D(C_\mathbb Q)\) membership, Mellin normalization and the n=9 amplitude; if the required imported idele/Masullo definitions are not formalized, keep this as an analytical PI result rather than fake a theorem.
5. The diagonal obstruction from PI001 remains: for nonzero \(t\), \(h_{t,t}(0)=\|t\|_2^2>0\). No positivity or operator isometry follows from these mixed pairings.
6. PI-C1 of PI001 (old/new mixed trace equality) is still unproved; PI002 adds a **strictly stronger coefficient test** (old-old \(n=9\) interface), not a claim the earlier conjecture has been settled.

## 5. PI003 gate and falsification plan

**PI003 — first local arithmetic coefficient audit**: choose exactly the above \(s,t\), read Masullo's explicit \(F=\mathbb Q\), \(p=3\) local geometric term, and calculate both sides with the same positive \(\log9\) correlation. Compare complete \(\pm\log n\) terms (only \(n=9\) survives) and coefficient \(\log3/3\) exactly. Freeze the author's \(\varphi\) vs \(\varphi\circ\mathrm{inv}\) convention. A rigorous mismatch after normalization falsifies the naive local dictionary.

Only after the local coefficient matches should PI investigate full archimedean/poles, full spectral multiplicity/tail, diagonal corrections, then an explicit bridge into Alpöge's arithmetic source and CP001's generalized finite compression.

**Guardrails:** no global Weil positivity, no purported accepted trace formula, no Lean PASS, no RH/GRH, no change to independent NF/IV/CP work.
