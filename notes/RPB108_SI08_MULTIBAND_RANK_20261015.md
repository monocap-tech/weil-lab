# RPB108 SI08 — support-preserving multi-band negative-operator compression

**Parent:** SI07 integrated at \`9f8d7242eb7e4cd1863b4770e910eb555102e3aa\`.  
**Carrier:** Original CC27/RC312–313 archimedean plus seven signed prime translates, with the explicit signed even/odd poles.  
**Front:** Independent structural investigation, not a replacement of RC original signed Schur-covariance certification.  
**Standing:** A rigorous *rank–operator-error frontier* for the full physically supported negative component. It does **not** prove the original signed Weil form nonnegative or close Stage I, F4, Lean or RH.

## 1. Input: actual SI07 certified cover, not a continuous worst-case band

SI06 proved \(m(\xi)>0\) for \(|\xi|\ge896\) for the original signed archimedean-plus-prime Fourier multiplier
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
-2\!\sum_{n\in\{2,3,4,5,7,8,9\}}\!\frac{\Lambda(n)}{\sqrt n}
\cos(2\pi\xi\log n).
\]
SI07's rational interval verifier certified that the negative part \(m_-=\max(0,-m)\) is supported in a symmetric union of 107 rational connected interval clusters on each half-line (including possibly the endpoints); their total width on both signs is \(243/8=30.375\), versus the earlier blanket width \(1792\). The same SI07 certificate gives
\[
M_-:=\int_{\mathbb R}m_-(\xi)\,d\xi
\le37.59565259375<38,\qquad \operatorname{tr}K_-=2BM_-\le82.71043570625<83
\]
with physical \(B=11/10\) and
\(K_-=Z^*\mathcal F^{-1}m_-\mathcal FZ\succeq0\).
SI08 reconstructs *all* accepted-positive and unresolved rational leaves by the exact same SI06/SI07 signed-source interval routines; it does not attempt to infer the support from finite sampling or merely from a plot.

## 2. New native support-preserving multi-band approximation lemma

For every certified positive-frequency cluster \(I_j=[a_j,b_j]\), set \(c_j=(a_j+b_j)/2\), \(w_j=b_j-a_j\). Retain its reflected partner \(-I_j\), with center \(-c_j\). Let \(\phi_\xi(x)=\mathbf1_{[-B,B]}(x)e^{2\pi i\xi x}\), a vector of physical \(L^2([-B,B])\). The negative physical operator admits the *positive trace-class integral* identity
\[
K_-=\int_{\mathbb R}m_-(\xi)|\phi_\xi\rangle\langle\phi_\xi|\,d\xi.
\]
Fix \(0<\varepsilon<1\). For each cluster let \(p_j\) be any positive integer obeying
\[
\frac{[(22/7)Bw_j]^{p_j}}{p_j!}<\varepsilon.
\]
Define the **physically supported modulated-polynomial span**
\[
V_{\varepsilon}=\operatorname{span}
\left\{\mathbf1_{[-B,B]}e^{\pm2\pi ic_jx}x^k:
1\le j\le107,\ \ 0\le k<p_j\right\}
+\operatorname{span}\{\sinh(x/2)\}.
\]
All basis functions have compact physical support; this construction does **not** Fourier-project the physical input onto an unbounded-support band.

For each frequency \(\xi\) in the corresponding signed cluster, the Taylor polynomial
\[
\mathbf1_{[-B,B]}e^{2\pi i c_jx}\sum_{k=0}^{p_j-1}
\frac{(2\pi i(\xi-c_j)x)^k}{k!}\in V_\varepsilon
\]
approximates \(\phi_\xi\) uniformly in \(L^2([-B,B])\):
\[
\operatorname{dist}(\phi_\xi,V_\varepsilon)
\le\sqrt{2B}\,\varepsilon.
\]
Here the **real-phase Taylor integral remainder** satisfies
\[
\left|e^{it}-\sum_{k=0}^{p-1}\frac{(it)^k}{k!}\right|
\le |t|^p/p!,
\qquad t\in\mathbb R,
\]
without an unnecessary \(e^{|t|}\) factor. On the entire interval \(I_j\),
\(|t|=|2\pi(\xi-c_j)x|\le\pi B w_j<(22/7)Bw_j\).
Let \(P_\varepsilon\) be the *physical \(L^2\) orthogonal projection* onto \(V_\varepsilon\). Since best approximation is at least as good as Taylor:
\[
\|(1-P_\varepsilon)\phi_\xi\|_2
\le\sqrt{2B}\varepsilon\quad(m_-(\xi)>0).
\]

The rank-one operator inequality
\[
\||u\rangle\langle u|-|v\rangle\langle v|\|
\le(\|u\|+\|v\|)\|u-v\|
\]
and \(\|\phi_\xi\|=\sqrt{2B}\), \(\|P\phi_\xi\|\le\sqrt{2B}\), give the **uniform full physical operator-norm bound**
\[
\boxed{
\|K_--P_\varepsilon K_-P_\varepsilon\|
\le4B M_-\varepsilon
<2^8\varepsilon.}
\]
No unrepresented frequency region is omitted. Both original negative odd-pole and positive even-pole forms stay explicit: the negative odd pole \(2|\sinh(x/2)\rangle\langle\sinh(x/2)|\) lies *exactly inside* \(V_\varepsilon\), so its compression has **zero error**. The resulting entire negative-source approximant is positive semidefinite and has
\[
\boxed{\operatorname{rank}\le2\sum_{j=1}^{107}p_j+1.}
\]

This is an **existence theorem with constructive explicit generators**; the validator checks rational Taylor orders and bounds but does not numerically orthonormalize or invert the potentially ill-conditioned modulated-polynomial Gram matrix. Converting the bound into a finite signed Schur certificate requires additional algebra and may be expensive.

## 3. Certified dimension/error frontier

The SI08 exact-Fraction validator rebuilds the 107 actual signed-source cluster lengths and computes the *minimum sufficient local Taylor orders under the conservative \(\pi<22/7\) bound* for target \(\varepsilon=2^{-b}\), \(b=40,64,80,96\). The resulting rigorous inequalities are
\[
\boxed{
\|K_{\rm negative}
-P_bK_{\rm negative}P_b\|<2^{-(b-8)},
\quad
\operatorname{rank}P_b
\le 2\sum_jp_j(b)+1.
}
\]
The exact rational validator and CI provide the following explicit frontier:

| Local Taylor error | Certified PSD rank (including exact odd pole) | Maximum local polynomial order | Entire negative-operator norm error |
|---|---:|---:|---:|
| \(2^{-40}\) | \(2503\) | 28 | \(<2^{-32}\) |
| \(2^{-64}\) | \(3541\) | 36 | \(<2^{-56}\) |
| \(2^{-80}\) | \(4165\) | 41 | \(<2^{-72}\) |
| \(2^{-96}\) | \(4757\) | 45 | \(<2^{-88}\) |

All 107 positive-frequency clusters, their reflected counterparts, the complete original signed Fourier uncertainty and the exact negative odd pole are accounted for. These ranks are **sufficient upper bounds on the dimension of an explicit span**, not proven minimal ranks or numerical eigencounts. The \(2^{-80}\) choice cuts the sufficient rank from 9473 to 4165 (approximately 56%) at the expense of relaxing SI06's much stronger \(2^{-1000}\) operator-error guarantee. The rank 4165 remains ~13.8 times RC314's 301-dimensional potential-negative-sector count.

This comparison is a **rank/error tradeoff**, not simultaneous domination: SI06's bound of rank 9,473 achieved error \(<2^{-1000}\), far stronger precision. SI08 reduces the rank when a more modest, still rigorous operator tolerance is sufficient.

## 4. Relation to RC Stage I and structural strategy

The original full signed form is
\[
Q_{\rm Weil}(f)
=Q_+(f)-\langle f,K_{\rm negative}f\rangle,
\qquad Q_+\ge0,
\]
on the relevant supported polynomial core. The approximation implies the **valid lower comparison**
\[
Q_{\rm Weil}(f)\ge Q_+(f)
-\langle f,P_bK_{\rm negative}P_b f\rangle
-2^{-(b-8)}\|f\|_{L^2}^2.
\]
It does **not** imply positivity of this lower bound. The rank bound is on a physically negative trace-class operator; it is *not* the number of possible negative eigenvalues of the full Weil form. RC314 has already localized the latter to a much smaller (301-dimensional) subspace by a different argument.

The correct decision test is whether support-preserving band adaptation can approach RC's native 301/317 dimensions at the **positive spectral margins actually needed**. Failure at the chosen tolerances is a structural efficiency result, not a refutation of the Weil program.

## 5. Next: SI09

Optimize the **rank/error/mass budget** of the cover. Consider merging nearby bands when that decreases \(p_j\)-sum, using the actual certified local weight integrals rather than a single \(\varepsilon\), and deriving a stable interval-rational Gram compression. The price of merging is larger phase radius, so only compare concrete fully paid operator errors. Alternatively test weighted Slepian/prolate concentration to beat the local Taylor span. Continue RC independently; no automatic shift of the main proof front.

## Reproduction

\`\`\`bash
python scripts/validate_rpb108_si08_multiband_rank.py
\`\`\`

The validator uses SI06's original signed rational phase/cosine machinery, SI07's exact adaptive support reconstruction, and Fraction-based Taylor bound search. Analytic input includes Plancherel, Rodrigues/Taylor integral remainder, Hilbert-space orthogonal projection and trace-class Bochner integration. CI replay checks the finite algebra but is not a Lean formalization or independent mathematical peer review.
