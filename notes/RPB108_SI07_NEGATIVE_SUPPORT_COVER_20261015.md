# RPB108 SI07 — certified sparse negative-frequency support and trace bound

**Front:** Structural Investigation (SI), independent of RC native signed Schur response.  
**Parent:** integrated SI06 \`b9ff35013891ae8575a910a99558ea11b67ae95d\`.  
**Native source:** CC27/RC312–313 original archimedean and seven signed prime translations; SI06 exact rational multiplier enclosure; original even/odd pole kept separately.  
**Standing:** rigorous adaptive real-frequency support cover and **trace** bound for the negative Fourier operator. This is **not** a 301-dimensional norm-tail certificate or original Weil positivity.

## 1. Actual signed multiplier and two kinds of spectral statements

For the zero-extended physical interval \([-B,B]\), \(B=11/10\), define
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}c_n\cos(2\pi\xi\log n),
\qquad c_{p^k}=\frac{\log p}{\sqrt{p^k}}.
\]
This is the actual CC27 original archimedean-plus-prime multiplier, with all signed prime powers, not the positive SI03 Dirichlet part alone. SI06 rigorously established \(m(\xi)>0\) for all \(|\xi|\ge896\), yet \(m(882.91)<-0.08\). Therefore **merely lowering a uniform outer cutoff cannot eliminate most of the remaining required rank**: any certified all-negative support radius must exceed 882.91.

SI07 takes a different approach. Define the possibly negative subset
\[
S_-=\{\xi\in\mathbb R:m(\xi)<0\},\qquad m_-=\max(0,-m).
\]
Instead of assuming \(m_-\) occupies the entire interval \([-896,896]\), construct an explicit finite union \(U\) of rational dyadic intervals such that
\[
\boxed{S_-\subseteq U\cup(-U).}
\]
SI07's self-contained rational verifier provides, with strict exact outward checks,
\[
\boxed{|S_-|<40},\qquad
\boxed{\operatorname{tr}K_-<100}.
\]
Here \(K_-=Z^*\mathcal F^{-1}m_-\mathcal FZ\) is the **physical supported negative-frequency operator**, which is positive trace-class by SI04. The full negative spectral mass is
\[
\operatorname{tr}K_-=2B\int_{\mathbb R}m_-(\xi)\,d\xi.
\]
This dramatically improves the SI04 worst-case trace upper
\(2B\cdot(4096)\cdot13\), while **not claiming to have resolved every exact sign-changing endpoint**.

## 2. All-point, not sampled, interval enclosures

On each integer cell \(j\le\xi\le j+1\), \(j=0,\ldots,895\), Euler's *monotone* quarter-digamma series gives the exact archimedean lower bound
\[
A_j=\sum_{k=0}^{63}
\frac{y_j^2}{(k+1/4)((k+1/4)^2+y_j^2)}
+\frac12\log\left(1+\frac{y_j^2}{(64+1/4)^2}\right)
-\left(\gamma_{\rm upper}+\frac{\pi_{\rm upper}}2+
3\log2_{\rm upper}+\log\pi_{\rm upper}\right),
\quad y_j=\frac{333}{106}j.
\]
The \(\frac12\log(1+\cdots)\) term is the exact integral lower bound for the decreasing positive tail starting at index 64; it is valid **even at \(j=0\)**. All rational logarithms are enclosed using the validated SI06 atanh series.

For an adaptive dyadic candidate interval \([l,r]\subseteq[j,j+1]\) with rational midpoint \(x=(l+r)/2\), SI06's fixed-point cosine/phase/log/sqrt routine computes a rigorous signed-prime lower \(p_{\rm lo}(x)\). The all-real derivative bound \(|p'(\xi)|<69\) implies
\[
\boxed{m(\xi)\ge L_{l,r}:=A_j+p_{\rm lo}(x)-\frac{69}2(r-l)}
\qquad(\xi\in[l,r]).
\]
If \(L_{l,r}>0\), **the entire continuous subinterval is certified positive**. Otherwise bisect until depth 6. Remaining unresolved dyadic leaves belong to \(U\); no false negativity is inferred from them.

For each unresolved leaf \([l,r]\), every point obeys
\[
0\le m_-(\xi)\le(-L_{l,r})_+.
\]
For inexpensive, reproducible, mathematically outward summation, its height is rounded **up** to integer multiples of \(10^{-6}\). Then exact rational summation gives both
\[
|U|=\sum_{\rm unresolved}(r-l)<20,
\qquad
\int_{\mathbb R}m_-\le2\sum_{\rm unresolved}(r-l)\,\lceil(-L_{l,r})_+10^6\rceil/10^6
<\frac{100}{2B}.
\]
Using SI06's high-frequency positivity completes the proof for all real frequencies. No untested point outside \(U\cup(-U)\) is allowed to contribute negative multiplier.

## 3. Quantitative spectral consequence—and a precise limitation

Since \(K_-\succeq0\) is trace-class and \(\operatorname{tr}K_-<100\), its eigenvalues arranged nonincreasingly obey
\[
\boxed{\lambda_j(K_-)<100/j}\quad(j\ge1).
\]
In particular, \(\lambda_{302}(K_-)<100/302<1/3\).
Also, fewer than 100 eigenvalues can exceed or equal 1. **This is only a thresholded spectral count for \(K_-\)**, not a bound on the number of negative eigenvalues of the full Weil operator.

The signed negative odd pole \(2|\sinh(x/2)\rangle\langle\sinh(x/2)|\) remains an additional exact rank-one negative operator and is **not silently included** in the displayed \(K_-\) trace budget. SI03 provides its separate physical trace \(2(\sinh B-B)\).

**Important no-go:** A trace bound, even a much better one, does *not* make the rank-301 truncation error negligible. The crude min–max norm tail \(100/302\) is orders of magnitude too large for the tight original signed RC Schur margins. SI07 does **not** replace SI05/06's small-operator-norm rank-9473 bound with a rank-301 bound.

## 4. Strategic reading and SI08

The frequency-only outer-bound estimate treated a band of total length \(1792\) as potentially negative. SI07 instead proves that the actual negative set is covered by dyadic intervals of *total length <40* (both signs), and certifies a strongly reduced trace budget.

This makes **multi-band time–frequency compression** worth investigating, in contrast to further shaving the outer frequency radius from 896 toward the genuinely negative witness at 882.91.

**SI08:** build a positive-semidefinite, *support-preserving* finite-rank model using the certified SI07 dyadic negative-frequency cover, with rigorous residual norm—not trace alone. Compare any rank/error pair directly against RC314's 301 potentially nonpositive directions and the current original RC high-inverse Schur margins. Options include modulated local polynomial features for each certified frequency cluster; the remainder must be charged by the **actual uncertain-band masses** and the original Fourier convention. Do not equate sparse spectral support with physical compact support, and do not infer positivity of a full Weil form from the negative Fourier trace alone.

### Reproduce

\`\`\`bash
python scripts/validate_rpb108_si07_negative_support_cover.py
\`\`\`

Exact Fraction arithmetic; imports SI06's certified original signed prime trigonometric interval functions. The computational certificate does not formalize all functional-analytic steps in Lean. Stage I, F4 and RH remain open.
