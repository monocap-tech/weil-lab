# RPB108 SI06 — certified original signed negative-frequency localization and smaller finite-rank compression

**Front:** Structural Investigation, independent of RC high-inverse Schur work.  
**Parent:** SI05 merged at \`f5b1f41d3c5fb8147a7db277a166cbb4463f3abe\`. RC330 already merged separately and must not be overwritten.  
**Source:** original CC27/RC312–313 signed archimedean–prime multiplier and signed pole, SI04–SI05 physical Fourier-to-Legendre negative operator.  
**Standing:** rigorous all-frequency positivity in the high band, an actual negative-frequency witness, and a smaller fully paid finite-rank approximation. No full Weil positivity, 3D Schur certificate, Stage I, F4, Lean, RH closure.

## 1. New signed support theorem

On \(I=[-B,B]\), \(B=11/10\), define the original frequency multiplier (RC312–313 Fourier convention)
\[
m(\xi)=\operatorname{Re}\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}c_n\cos(2\pi\xi\log n),
\quad c_{p^k}=\frac{\log p}{\sqrt{p^k}}.
\]

**New theorem:**
\[
\boxed{m(\xi)>0\text{ for every real }|\xi|\ge896.}
\]
The negative part \(m_-=\max\{-m,0\}\) is therefore supported inside the strict finite band \((-896,896)\), improving SI04's \((-2048,2048)\).

An independently certified **actual negative** signed Fourier value occurs at the rational frequency \(\xi=88291/100=882.91\):
\[
\boxed{m(882.91)<-0.08<0.}
\]
This means some negative multiplier persists below 896; this work makes **no claim** that the negative set is a single interval or that 896 is optimal.

## 2. Proof on the infinite high-frequency half-line

Set \(a=1/4\), \(y=\pi|\xi|\) and \(g_y(t)=y^2/((t+a)((t+a)^2+y^2))\). Euler's digamma series gives
\[
a_{\rm arch}(\xi)=\psi(a)-\log\pi+\sum_{k\ge0}g_y(k).
\]
Each \(g_y(t)\) is nonnegative, decreasing in \(t\ge0\) and increasing in \(y>0\). Thus for \(K=128\),
\[
\sum_{k\ge0}g_y(k)\ge
\sum_{k=0}^{127}g_{y_0}(k)
+\int_{128}^{\infty}g_{y_0}(t)dt
>\sum_{k=0}^{127}g_{y_0}(k)
+\log\frac{y_0}{128+1/4},
\quad y_0=\frac{333}{106}|\xi|_{\min}.
\]
The original identity \(\psi(1/4)=-\gamma-\pi/2-3\log2\) plus rigorous
\(\gamma<29/50,\ \pi<22/7,\ \log2<347/500,\ \log\pi<573/500\)
produces a **rational** all-\(\xi\ge1200\) bound. The certified seven-prime upper scalar is \(2C<70751/10000\), with *correct original base-prime coefficients*, and the exact validator establishes
\[
a_{\rm arch}(1200)\ge A_{1200}>2C.
\]
Consequently \(m(\xi)\ge a_{\rm arch}(\xi)-2C>0\) on the entire infinite half-line \(|\xi|\ge1200\). This does **not** substitute SI03's supported-operator 4.103149 bound into an unbounded-frequency pointwise assertion.

## 3. Fully rigorous interval check on 896..1200

Each integer cell \([j,j+1]\), \(j=896,\ldots,1199\), has an analytically monotone archimedean lower bound \(A_j\), computed with \(K=128\) positive digamma terms and the exactly enclosed \(\log(y/(K+1/4))\).

The signed prime trigonometric polynomial \(p(\xi)=-2\sum c_n\cos(2\pi\xi\log n)\) has the **uniform all-real derivative bound**
\[
|p'(\xi)|\le4\pi\sum_n c_n\log n<69
\]
proved in exact rational intervals.

For every adaptive dyadic subinterval \([l,r]\subset[j,j+1]\) with rational midpoint \(x\), the validator encloses \(p(x)\) using:
- Machin's formula \(\pi=16\arctan(1/5)-4\arctan(1/239)\), with rigorously signed alternating-series error;
- 128-term rational \(\operatorname{atanh}\) logarithms with geometric tail;
- exact outward integer-square-root bounds for all seven \(c_n\);
- phase reduction modulo \(2\pi\) with all angular/logarithmic uncertainty charged;
- a signed integer fixed-point 18th-degree-in-\(t^2\) cosine Taylor recurrence scaled by \(10^{40}\). Its truncation error is bounded by \((22/7)^{38}/38!<10^{-22}\). Each fixed-point recurrence operation incurs <one integer unit of error; the accumulated Taylor rounding error is conservatively below \(10^5/10^{40}\). Phase uncertainty is <\(10^{-15}\). A total cosine enclosure \(\pm10^{-13}\) dominates all three errors.

A subinterval is **accepted only if**
\[
\boxed{A_j+p_{\rm lower}(x)-\frac{69}{2}(r-l)>0.}
\]
The last term covers every frequency between the sample point and endpoints, so this is not a floating-point grid or a finite sampling inference.

**Actual run:** 2,535 accepted dyadic leaves, maximal dyadic depth 7, with all interval lower certificates positive; the smallest outward rational margin exceeds \(0.00369\). Together with the infinite-half-line argument and evenness of the multiplier, this certifies the whole set \(|\xi|\ge896\).

## 4. Independently certified negative witness

For \(\xi=88291/100\), reverse the digamma tail estimate: since \(g_y(t)\) is decreasing,
\[
\sum_{k=128}^\infty g_y(k)
\le\int_{127}^\infty g_y(t)dt
=\frac12\log\left(1+\frac{y^2}{(127+1/4)^2}\right).
\]
Use \(y\le (22/7)(88291/100)\), the rigorous lower constant
\(\gamma>57/100,\ \pi>333/106,\ \log2>69/100\),
and a certified lower rational bound on \(\log\pi\). Add an **upper** enclosure for the full signed seven-prime trigonometric polynomial. The exact rational validator obtains
\[
m(882.91)<-0.08419<-0.08.
\]
The witness is not an RH counterexample or a negative Weil quadratic direction: an isolated negative value of the uncompressed Fourier multiplier does not prove negativity of the form on **compactly supported inputs**.

## 5. SI05 finite-rank compression improves by more than a factor of two

On physical \(L^2([-B,B])\), let \(K_-=Z^*\mathcal F^{-1}m_-\mathcal FZ\). Retain the negative odd-pole \(2|s\rangle\langle s|\) exactly, as in SI05. In SI05's Rodrigues/Legendre projection proof, use the new frequency bandwidth \(\Omega=896\) and \(N=9472\) Legendre modes.

The plane-wave phase satisfies
\[
|z|=|2\pi B\xi|\le 2\cdot\frac{22}{7}\cdot B\cdot896.
\]
With \(e<11/4\), exact rational arithmetic proves
\[
\frac{(11/4)|z|}{2N}<\frac9{10},\qquad
q=(9/10)^2=\frac{81}{100},\quad q^4<\frac12.
\]
Consequently, for all \(|\xi|\le896\),
\[
\|(I-\Pi_N)\phi_\xi\|_2^2
\le2Bq^N\left(\frac{2N+1}{1-q}+\frac{2q}{(1-q)^2}\right)
<2^{18}2^{-2368}=2^{-2350}.
\]
The total negative frequency mass satisfies \(\int m_-<2(896)13<2^{15}\). The exact SI05 rank-one integral argument therefore gives
\[
\boxed{\|K_- -\Pi_NK_-\Pi_N\|<2^{-1158}<2^{-1000}.}
\]
Retaining the original negative odd pole exactly yields a **positive semidefinite negative-operator approximant with rank at most**
\[
\boxed{9473\quad\text{versus SI05's }20481.}
\]
This is a rigorous sufficient rank, *not* an optimal or necessary rank and not positivity of the full Weil operator.

## 6. Strategic outcome and next frontier

This **more than halves** the SI05 sufficient rank with a strictly tighter remainder estimate, but even 9,473 is over 31 times RC314's currently certified 301 potentially nonpositive directions. It is not yet competitive with the native RC330 and continuing high inverse/Schur chain.

**SI07:** determine whether a *support-preserving, weighted time-frequency localization* can reduce the effective dimension below the native 301-direction benchmark, or whether the SI Fourier-only route should be retained as a useful but secondary structural theorem. Optimize negative-set intervals instead of treating the entire 896 band uniformly; avoid assuming disjoint Fourier intervals preserve original physical support.

**Reproduction:** \`python scripts/validate_rpb108_si06_negative_band.py\` uses only Python's standard library \`Fraction\`, exact integer arithmetic, and integer square roots. GitHub Actions structural CI runs all SI validators.

No Stage I/F4/Lean/RH claim is made.
