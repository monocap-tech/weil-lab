# RPB108 SI19 — exact Jensen minorants remove the odd concentration remainder penalty

**Parent:** integrated SI18 \`d7a3820790dec27630a9a6b468572bab7e6c768a\`, PR #113.  
**Front:** independent Structural Investigation of the **original CC27/RC312–313 signed** archimedean + seven-prime Weil form.  
**Status:** analytic all-degree **exact positive rank-two operator minorant** using physically supported, frequency-averaged sine features; strictly stronger **upper** bound on the original odd supported inverse Birman–Schwinger pole response. No claim of exact original inverse, whole signed Weil positivity, Stage I, F4, Lean or RH.

## 1. A structural shortcut hidden by SI17/18's Taylor remainders

Write \(\kappa=1/1000\), \(B=11/10\), and let \(A_o\) be the restriction to odd \(L^2([-B,B])\) of SI11's original supported positive operator with frequency multiplier \(a(\xi)=\max(m(\xi),\kappa)\). The original positive even pole vanishes on this sector; the negative odd pole is \(2|s\rangle\langle s|\), \(s(x)=\sinh(x/2)\).

SI18 certified two disjoint entire **original signed-positive** neighborhoods:
\[
m(\xi)>7/5=1.4 \quad\text{on } \pm[0.22,0.38],\qquad
m(\xi)>1201/1000=1.201\quad\text{on }\pm[0.73,0.79].
\]
These bounds include **every original signed prime-power term**, with exact rational all-continuum digamma and trigonometric certificates from SI13–14.

For \(c_1=3/10,\ c_2=19/25,\ r=1/125\), take the two disjoint narrower symmetric windows \(J_j^\pm=\pm[c_j-r,c_j+r]\), and put
\(\delta_1=1399/1000,\ \delta_2=6/5\).
Then the original supported odd operator obeys
\[
A_o\succeq\kappa I+\delta_1T_{J_1,o}+\delta_2T_{J_2,o},
\quad
T_{J_j,o}=2\int_{c_j-r}^{c_j+r}|h_\xi\rangle\langle h_\xi|\,d\xi,
\quad h_\xi(x)=\sin(2\pi\xi x).
\]

SI17/18 approximated each \(T_J\) by \(4r|h_c\rangle\langle h_c|\) with a **two-sided operator error \(\varepsilon\)**, deducting \(\sum_j\delta_j\varepsilon\) from the weak positive floor \(\kappa\). SI19 avoids this *entire adverse deduction*, by using the **exact frequency-averaged feature**, not the central-frequency feature.

## 2. New exact, dimension-independent Jensen/variance Loewner theorem

Define the **physically supported odd** average
\[
g_c(x):=\frac1{2r}\int_{c-r}^{c+r}\sin(2\pi\xi x)\,d\xi
=\sin(2\pi cx)\operatorname{sinc}(2\pi r x),
\quad \operatorname{sinc}z=\frac{\sin z}{z},
\]
with removable value 1 at \(z=0\). Every \(g_c\) lies entirely on the original physical interval; no unsupported frequency projection is applied to an input.

For any \(f\) in the physical odd space, **scalar Cauchy–Schwarz** implies
\[
2\int_{c-r}^{c+r}|\langle f,h_\xi\rangle|^2d\xi
\ge 4r\left|\left\langle f,\frac1{2r}\int_{c-r}^{c+r}h_\xi\,d\xi\right\rangle\right|^2.
\]
Equivalently, the positive **operator variance identity** gives
\[
\boxed{
T_{J,o}-4r|g_c\rangle\langle g_c|
=2\int_{c-r}^{c+r}|h_\xi-g_c\rangle\langle h_\xi-g_c|\,d\xi
\succeq0.
}
\]
The remainder is **exactly positive semidefinite**, rather than unknown-signed with small norm. No Taylor/Gram approximation is needed for the Loewner sign.

Therefore the entire original odd supported operator admits the rigorously positive **rank-two supported lower reference**
\[
\boxed{
A_o\succeq C_o
:=\kappa I+
\gamma_1|g_{c_1}\rangle\langle g_{c_1}|
+\gamma_2|g_{c_2}\rangle\langle g_{c_2}|,
\qquad \gamma_j=4r\delta_j.
}
\]
**The positive scalar floor remains exactly \(\kappa=0.001\)**. SI18 had to reduce its floor to approximately \(0.0008446\) to pay the Taylor operator norm error. This new theorem applies to the full odd physical Hilbert space, not a truncated test basis.

## 3. Original physically supported inverse, including correct-sign covariance

By inverse order, \(A_o^{-1}\preceq C_o^{-1}\). Let \(G:\mathbb C^2\to H_o\) synthesize the two frequency-averaged vectors, \(Ge_j=g_{c_j}\); let \(\Gamma=\mathrm{diag}(\gamma_1,\gamma_2)\), \(H=G^*G\) the original **supported physical Gram**, and \(q=G^*s\) the original odd-pole overlaps. Woodbury is exact **only for the explicit supported reference**:
\[
C_o^{-1}
=\kappa^{-1}I
-\kappa^{-2}G(\Gamma^{-1}+\kappa^{-1}H)^{-1}G^*.
\]
Thus
\[
2\langle s,A_o^{-1}s\rangle
\le 2\left[
\frac{\|s\|_2^2}{\kappa}
-\frac{1}{\kappa^2}
q^*(\Gamma^{-1}+\kappa^{-1}H)^{-1}q
\right].
\]

For the real \(2\times2\) matrix \(M=\begin{pmatrix}a&b\\ b&d\end{pmatrix}\succ0\), the correction is
\[
q^*M^{-1}q
=\frac{dq_1^2-2bq_1q_2+aq_2^2}{ad-b^2}.
\]
As in SI18, **the mixed term is adverse** since \(q_1>0,q_2<0,b<0\), so \(-2bq_1q_2<0\). The SI19 rational validator pays this sign explicitly. It does **not** substitute a physically incorrect whole-line Fourier inverse.

## 4. Exact rational control of averaged-feature Gram and source overlap

Put \(h_c(x)=\sin(2\pi cx)\). On the entire physical interval, \(|2\pi rx|\le 2(22/7)rB\), so
\[
0\le1-\operatorname{sinc}(2\pi rx)
\le\frac{(2\pi rB)^2}{6}=:\theta
<\frac1{1900}.
\]
Consequently
\[
\|g_c-h_c\|_2\le\theta\|h_c\|_2.
\]
From SI18's exact-rational trigonometric/hyperbolic enclosures and \(\|s\|_2<1/2\), \(\|h_c\|_2<7/6\), the **whole physical interval errors** satisfy
\[
\begin{split}
|\langle s,g_c\rangle-\langle s,h_c\rangle|
&\le(7/12)\theta<3/10000,\\
|\langle g_{c_i},g_{c_j}\rangle-\langle h_{c_i},h_{c_j}\rangle|
&\le(2\theta+\theta^2)(133/100)<14/10000.
\end{split}
\]
The exact-rational script regenerates SI18's *tight* non-rounded supported Gram and overlap intervals before applying these errors. It asserts the following full supported averaged-feature bounds:
\[
\begin{array}{ll}
0.5419<q_1<0.5426,& -0.1666<q_2<-0.1658,\\
1.3225<H_{11}<1.3254,&1.1909<H_{22}<1.1938,\\
-0.1442<H_{12}<-0.1413,&\|s\|_2^2<0.235648.
\end{array}
\]
All displayed decimal rationals are terminating representations of **strict Fraction inequalities**. No float approximation governs a mathematical assertion.

Let \(a_{\min},a_{\max},d_{\min},d_{\max}\) be the exact outward diagonal bounds on \(\Gamma^{-1}+\kappa^{-1}H\). Let \(b_{\min},b_{\max}\) bound the **absolute** off-diagonal. For lower correction, use
\[
N_{\min}=d_{\min}(0.5419)^2
-2b_{\max}(0.5426)(0.1666)
+a_{\min}(0.1658)^2>0,
\quad
D_{\max}=a_{\max}d_{\max}-b_{\min}^2>0.
\]
This retains the **negative adverse covariance** and the actual determinant sign. The exact conservative supported inverse upper follows:
\[
\boxed{
2\langle s,A_o^{-1}s\rangle
\le2\left[\frac{0.235648}{\kappa}
-\frac{N_{\min}}{\kappa^2D_{\max}}\right]
<18.
}
\]
This is a fully paid, **strict improvement over SI18's \(<29\) at the same original operator**. The exact rational regression prints the upper numerical enclosure from the finite arithmetic.

## 5. Strategic interpretation and SI20

SI19 removes an inefficiency in the **method of bounding the operator** rather than merely adding another positive window. It provides an exact positive concentration lower bound for *any* interval and physical carrier. This can be combined with arbitrary original signed-positive frequency intervals while retaining the original scalar floor \(\kappa\), provided all sign intervals are certified and the physical Gram is properly bounded.

It does **not** prove that the actual odd inverse pole response is less than 1 or establish positivity of the entire signed Weil form. The negative-frequency operator from SI11 remains coupled to this positive reference; full finite-dimensional Birman–Schwinger and Schur blocks are unverified. Nor is the original inverse vector \(A^{-1}s\) computed: this is a certified **upper comparison** using an explicit different operator \(C_o\).

**SI20:** exploit the Jensen variance decomposition to build a rank-three (or optimized rank-two) physically supported positive minorant without eroding \(\kappa\); test a third original signed-positive window and pay a genuine \(3\times3\) Gram/overlap matrix with correct signs. A key comparison is whether this reaches a sub-10 bound, or whether the method must shift to a genuine supported inverse response of the **complete** positive operator. The native RC signed Schur route remains independently primary.

**Reproduce:** \`python scripts/validate_rpb108_si19_odd_jensen_minorant.py\`. Uses only exact Fraction inequalities, original signed SI13/14 band proofs, SI18's rational physical trigonometric integrals, and analytic Jensen/Cauchy–Schwarz on positive Hilbert-space feature integrals. It is neither Lean formalization nor independent peer review.

**No Stage I, original global signed Weil positivity, F4 bridge, complete Lean or RH result is claimed.**
