# RPB108 NF22 — Original archimedean physical source reconstructed and squared rigorously on e0/e1

Date: 2026-10-09 UTC / 2026-10-08 Pacific. Independent branch research/rpb108-phase-geometry-localization. Start source head de3f69bd4121aa586b480222405a480f1edf0f17 (NF21) and live Coupled mathematical head CC58 ff5a90f8ea83d9a7891d1755bb42074d91922c77, read-only. All older native and source certificates remain unmodified. CC58 already independently replayed the NF21 prime/pole SOURCE-square; NF22 therefore computes the MISSING archimedean physical source, not that existing sector again.

**New A-class original arch source theorem at a=53/50:** An explicit degree-320 rational Taylor reconstruction of the actual log-archimedean physical operator action on the first two normalized supported Legendre modes has rigorously bounded physical L2 errors <10^-19, preserving the genuine endpoint logarithms. The archimedean physical SOURCE squares (not native Q diagonals) are rigorously enclosed by

\[
\boxed{7.082144075590 < \|L_{\rm arch}e_0\|_{L^2}^2 < 7.082144075591,}
\tag{NF22.1}
\]

\[
\boxed{1.083143528165 < \|L_{\rm arch}e_1\|_{L^2}^2 < 1.083143528166.}
\tag{NF22.2}
\]

This is a new actual original-source sector certificate, complementary to NF21's fully signed prime+pole SOURCE-square on e0/e1. It does NOT enclose the complete arch–prime or arch–pole SOURCE cross terms, the combined complete source squares or the full E112 compensated residual Gram P2.

## 1. Exact original archimedean action and the endpoint-log cancellation

The CC56 original physical archimedean operator formula is

\[
(L_{\rm arch}p)(x)=a_0p(x)
+\int_{-a}^a j(|x-y|)[p(x)-p(y)]\,dy
+p(x)[J(a-x)+J(a+x)],
\]
where
\[
j(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
J(t)=\int_t^\infty j(s)\,ds
 =\operatorname{atanh}(e^{-t/2})+\arctan(e^{-t/2}),
\]
and \(a_0=\psi(1/4)-\log\pi=-\gamma-\pi/2-3\log2-\log\pi\).
Put \(F(t)=\int_0^t s\,j(s)\,ds\) and \(a=53/50\).
For \(e_0=1/\sqrt{2a}\) and \(e_1=\sqrt{3/(2a)}\,x/a\), the original action is EXACTLY

\[
L_{\rm arch}e_0(x)=\frac{U(x)}{\sqrt{2a}},\qquad
L_{\rm arch}e_1(x)=\frac{\sqrt{3/(2a)}}{a}
   [xU(x)+F(a+x)-F(a-x)],
\tag{NF22.3}
\]

where \(U(x)=a_0+J(a-x)+J(a+x)\). The odd integral-difference term is essential: it is the original inside-support polynomial-difference contribution and cannot be omitted.

The exact generating function
\[
h(z)=z j(z)=\frac{z e^{z/2}}{2\sinh z}
     =\sum_{k\ge0}h_k z^k,\qquad h_0=1/2,
\]
has RATIONAL Taylor coefficients determined by
\[
2h_n+\sum_{k=1}^{\lfloor n/2\rfloor}
\frac{2h_{n-2k}}{(2k+1)!}
=\frac{1}{2^n n!}.
\tag{NF22.4}
\]
The first coefficients \(h_1=1/4,h_2=-1/48,h_3=-1/32\) were checked independently.

Since \(J'(t)=-j(t)\), the exact local analytic primitive of its regular part and the polynomial-difference primitive are
\[
J(t)=-\frac12\log t+\log2+\frac\pi4
          -\sum_{k\ge1}\frac{h_k}{k}t^k,
\quad
F(t)=\frac t2+\sum_{k\ge1}\frac{h_k}{k+1}t^{k+1}.
\]

Combining \(a_0+2(\log2+\pi/4)\) gives the useful exact cancellation
\[
\boxed{
U(x)=-\gamma-\log(2\pi)-\frac12\log(a^2-x^2)
      -\sum_{k\ge1}\frac{h_k}{k}
         [(a-x)^k+(a+x)^k].
}
\tag{NF22.5}
\]
Thus the singular endpoint logarithm is explicit; only the ANALYTIC regular function is approximated by a rational polynomial. This avoids making a false uniform pointwise boundedness assertion near \(x=\pm a\).

## 2. Uniform Cauchy remainder for the entire target aperture

On the complex circle \(|z|=5/2<\pi\), the generating function h(z) is holomorphic and obeys \(|h(z)|<10\). Indeed, if \(|\Re z|\ge1/2\), \(|\sinh z|\ge\sinh(1/2)>1/2\); otherwise \(\sqrt6<|\Im z|\le5/2\) and \(|\sinh z|\ge|\sin(\Im z)|>\frac12\). Also \(|e^{z/2}|\le e^{5/4}<4\), so \(|z e^{z/2}/(2\sinh z)|<10\).

The target support width is \(2a=53/25\), and its ratio to this circle is \(\rho=106/125\). Cauchy's coefficient estimates imply for the degree-320 regular kernel polynomial \(r_{320}(t)=\sum_{k=1}^{320}h_k t^{k-1}\),

\[
\boxed{
\sup_{0\le t\le2a}\left|
 j(t)-\frac1{2t}-r_{320}(t)\right|
\le\frac{4\rho^{320}}{1-\rho}
<3.213\times10^{-22}<10^{-20}.
}
\tag{NF22.6}
\]

Integrating the regular error into the J and F functions and using normalized physical Legendre functions yields

\[
\|L_{\rm arch}e_0-L_{\rm arch,320}e_0\|_2
 \le 4a\epsilon<10^{-19},
\]
\[
\|L_{\rm arch}e_1-L_{\rm arch,320}e_1\|_2
 \le 8a\sqrt3\,\epsilon<14a\epsilon<10^{-19},
\]
where \(\epsilon=4\rho^{320}/(1-\rho)\).
These are true native original physical source errors, not nominal floating-point tolerances. All bounds use exact rational comparisons.

## 3. Rigorous original arch-source squared norms

The polynomial part of (NF22.5) is even and F(a+x)-F(a-x) is odd. NF22 integrates their exact rational coefficient products against the COMPLETE physical interval analytically. For \(M_m=\int_{-a}^a x^{2m}dx=2a^{2m+1}/(2m+1)\), let \(Z=\log(2a)\), \(H_m=\sum_{k=1}^{m+1}(2k-1)^{-1}\), and \(H_m^{(2)}=\sum_{k=1}^{m+1}(2k-1)^{-2}\). The EXACT logarithmic endpoint moments are

\[
\int_{-a}^a x^{2m}\log(a^2-x^2)\,dx
=2M_m(Z-H_m),
\]
\[
\int_{-a}^a x^{2m}\log^2(a^2-x^2)\,dx
=M_m\left(4(Z-H_m)^2-\frac{\pi^2}{3}+4H_m^{(2)}\right).
\tag{NF22.7}
\]

These integrals incorporate the singular endpoint exactly; no endpoint samples or guessed discarded strips occur. Euler's constant is enclosed by the exact harmonic/Euler–Maclaurin formula at n=100 with 20 Bernoulli corrections and its bounded next term. Pi uses Machin arctangents; logarithms use monotone rational atanh enclosures with outward endpoint rounding. Every polynomial coefficient, antiderivative and moment sum is rational before substituting those enclosed constants.

The rational-interval integrator computes the two source-square intervals for \(L_{\rm arch,320}e_j\), then pays the above physical source L2 errors by
\[
|\|L_{\rm arch}e_j\|_2^2-\|L_{\rm arch,320}e_j\|_2^2|
\le \delta_j(8+\delta_j)
\]
since both approximant and true source L2 norms are <4. This establishes (NF22.1)–(NF22.2), with the unrounded enclosures having widths about2.18e-20 even and7.63e-20 odd.

Reproducible exact sources:
- [320-degree full-cap regular source and Cauchy proof checks](../scripts/certify_native_arch_source_uniform_nf22_106.py).
- [Independent exact polynomial/logarithm moment and arch SOURCE-square producer](../scripts/certify_native_arch_source_square_nf22_106.py).
- [Machine-readable NF22 certificate and scope](data/RPB108_NF22_ARCH_SOURCE_LOW2_CERTIFICATE_20261009.json).

The two exact mathematical calculations ran locally, with the uniform series certificate using only exact rational comparisons and the squared-norm certificate additionally enclosing pi, Euler gamma and logarithms outward. No GitHub Actions or Lean replay is claimed.

## 4. Complete original source pilot — NUMERICAL diagnostics only

The complete source on e0/e1 is
\[
s_j=L_{\rm arch}e_j+L_{\rm prime}e_j+L_{\rm pole}e_j.
\]
A separate [NON-CERTIFYING full source integration diagnostic](../scripts/diagnose_native_complete_source_low2_nf22_106.py) evaluates the 13 prime-translation support cells with independent SciPy integration. It reports:

| SOURCE-square/cross term | Even e0 | Odd e1 |
|---|---: | ---: |
| Rigorous arch square, numerical midpoint | 7.082144 | 1.083144 |
| Rigorous NF21 prime square, numerical midpoint | 4.249294 | 2.322359 |
| Rigorous NF21 pole square, numerical midpoint | 21.678748 | 0.176303 |
| Rigorous NF21 twice prime-pole cross, numerical midpoint | -18.683476 | -1.217839 |
| **UNPROVED numerically: twice arch-prime cross** | +10.024385 | -2.767819 |
| **UNPROVED numerically: twice arch-pole cross** | -24.267433 | +0.741994 |
| **UNPROVED complete combined source square** | **0.0836618** | **0.3381412** |

The direct source/native pairing numerically reproduces NF17's actual original Q(e0,e0)=0.040152084275421 and Q(e1,e1)=0.144011672856334 with deviations below 2e-15. This strongly supports correct normalization, original signed pole conventions and absence of a missing local arch constant, but remains a numerical CROSSCHECK and is not promoted to an exact source-square theorem.

The marked cross terms are LARGE. The combined source-square is considerably smaller than the sum of individually rigorous sectors. This empirically supports NF20/CC58's insistence on compensated-source cancellation BEFORE squaring. It does not itself upper-bound the complete physical-source estimator at any near-critical E112 direction.

## 5. NF23 next gate and classification

**Closed at NF22:** exact original physical arch source expressions for low e0/e1; uniform entire-cap rational kernel approximation; rigorous arch SOURCE-square bounds. Combining with NF21, all three separate SOURCE-square diagonal sectors on e0/e1 are certified (arch, prime and pole), and the prime–pole covariance is certified.

**Open:** RIGOROUS arch–prime and arch–pole physical SOURCE cross enclosures, combined full original e0/e1 source squares, then 58-column compensated physical source Gram D/P2 per parity and ultimately its source-aligned inverse response. The numerical combined values in section4 are not certificates.

**NF23 objective:** Integrate the remaining arch–prime and arch–pole SOURCE cross terms on each of the 13 original translation cells. Exploit (NF22.5)'s explicit endpoint logarithm and exact regular polynomial to produce outward rational integrals, paying the <=1e-19 arch source L2 error after multiplication by the already certified NF21 prime/pole source norm. First certify complete e0/e1 source squares, then attempt a near-critical NF18 rational vector and the first compensated residual P2 entry. A failure of the crude physical residual Gram sign remains inconclusive, not an actual negative Weil vector.

Highest internally certified WHOLE original aperture remains a=21/20 (CC18), not a=53/50. CC58 concurrent compensated form-source analysis and previous CC57 graph-gap control remain independent and unchanged. No global RH/F4, old-gap-independent collective frame, full transport or Lean theorem is claimed.
