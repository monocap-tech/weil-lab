# SM28 — Genuine original positive-frequency continuum: infinite Legendre towers and a complete physical residual bound on thirteen certified bands

**W-ODD-NEG canonical · October 18, 2026 · stacked on SM27 draft PR #208 (SM27 focused Actions PASSED).** This checkpoint produces a **new analytic original-operator signed-positive continuum module**: it retains *all* frequency degrees inside thirteen actual SM14 whole-real signed-positive intervals, proves their discarded Jensen variance is strictly positive on every nonzero original supported odd test function, constructs the first two exact orthogonal original physical frequency moments, and rigorously bounds the **entire infinite positive-frequency tower tail after degree one** in operator norm. This is not an entire-frequency odd Weil positivity theorem. All PS36 O1/O2 complete-original-operator gates, even E1–E4, whole signed Weil, CC27 D-Riesz, RH stay OPEN. Independent infinite-dimensional mathematical audit remains required.

## 1. Recover source information lost by finite Jensen means

On the actual original odd carrier \(H_o=L^2([-B,B])_{\mathrm{odd}}\), \(B=11/10\), put \(h_\xi(x)=\sin(2\pi \xi x)\). Original signed seven-prime positive multiplier \(w_+(\xi)=(m(\xi)-\kappa)_+\) with \(\kappa=1/1000\) gives
\[
A_o=\kappa I+2\int_0^\infty w_+(\xi)|h_\xi\rangle\langle h_\xi|\,d\xi,
\qquad A_*=A_o-2|s\rangle\langle s|,\quad s(x)=\sinh(x/2).
\]
The integral is understood as the original closed quadratic form; on any **finite selected real-frequency window** it is a bounded positive operator. SM14 certified **thirteen true positive bands**
\[
J_j=[c_j-r,c_j+r],\quad c_j=\frac{n_j}{50},
\quad r=\frac3{200},
\]
with \((n_j,\delta_j)=
(703,4),(705,4),(707,4),(709,3),(711,2),(713,1),
(728,1),(730,2),(732,3),(734,3),(736,3),(738,3),(740,2)\).
Every point of every real interval satisfies the **original full-seven-prime signed inequality** \(w_+(\xi)>\delta_j\), not merely its midpoint. These thirteen intervals have disjoint interiors, lie outside the original SM12 C33 windows and the SI29 B14 frequency windows, and do not double count a single Fourier-integral contribution.

Define the **full continuum** signed-positive physical band response
\[
\boxed{T_j=2\delta_j\int_{J_j}|h_\xi\rangle\langle h_\xi|\,d\xi\succeq0.}
\]
Because the actual positive signed frequency bands are disjoint from SI29's genuine protected 14-source positive windows, the **pole-conditioned, genuinely ORIGINAL** full-carrier Loewner minorant is
\[
\boxed{A_*\succeq B_{14}+\sum_{j=1}^{13}T_j\succeq B_{14}
\succeq\kappa_*I,\qquad \kappa_*=\frac{33621}{10^9}>0.}
\]
This retains the actual negative odd pole exactly once, already inside \(B_{14}=\kappa I+P_{14}-2|s\rangle\langle s|\). Unlike a 13-dimensional Jensen correction, **each true \(T_j\) has infinite rank on the original supported odd carrier**. This is a strict enlargement of the rank-14 method class ruled out in SM26, although it does not by itself pass the entire odd negative-cap comparison.

## 2. Exact infinite orthogonal original frequency decomposition

Let \(P_n\) be the standard Legendre polynomial, normalized by
\(\int_{-1}^1P_n(t)P_m(t)\,dt=2\delta_{nm}/(2n+1)\).
For each original \(J_j\), define the **actual physical vectors**
\[
q_{jn}(x)=\frac12\int_{-1}^1P_n(t)\,h_{c_j+rt}(x)\,dt\in H_o.
\]
Hilbert-valued Parseval, applied to the **whole true supported** continuous sine family, gives an operator-norm convergent positive series
\[
\boxed{
T_j=4r\delta_j\sum_{n=0}^\infty(2n+1)|q_{jn}\rangle\langle q_{jn}|.
}
\]
This identity includes every frequency covariance term inside its interval; it does **not** approximate the continuous multiplier by point frequencies.

The first two genuinely original physical moments are
\[
q_{j0}(x)=\sin(2\pi c_jx)\operatorname{sinc}(2\pi rx),
\]
\[
q_{j1}(x)=\cos(2\pi c_jx)\,
\frac{\sin t-t\cos t}{t^2},\qquad t=2\pi r x,
\]
with continuous \(q_{j1}(0)=0\). The latter is the **exact odd first-frequency moment**, not the derivative of a fabricated finite packet. The exact two-mode finite positive lower is
\[
\boxed{T_j^{[2]}
=4r\delta_j\bigl(|q_{j0}\rangle\langle q_{j0}|
+3|q_{j1}\rangle\langle q_{j1}|\bigr)\preceq T_j.}
\]
Equivalently, with \(v_{j1}=(3/r)q_{j1}\),
\(T_j^{[2]}=4r\delta_j|q_{j0}\rangle\langle q_{j0}|
+(4r^3\delta_j/3)|v_{j1}\rangle\langle v_{j1}|\).

**Crucial strictness:** for every nonzero actual odd \(f\in H_o\), the positive-frequency transform \(F_f(\xi)=\langle f,h_\xi\rangle\) extends to an entire function of \(\xi\), is odd and tends to zero on the real line by Riemann–Lebesgue. If
\(\langle f,(T_j-T_j^{[2]})f\rangle=0\), then \(F_f\) agrees a.e. on \(J_j\) with a degree-one polynomial, hence identically with that polynomial by analytic continuation. Real-line decay forces this polynomial to vanish; Fourier uniqueness forces \(f=0\), contradiction. Therefore
\[
\boxed{\langle f,(T_j-T_j^{[2]})f\rangle>0
\qquad\forall f\in H_o\setminus\{0\}.}
\]
More generally every finite Legendre truncation retains a strictly positive **infinite-rank** remainder. Because these operators are compact, this strict positivity is **not** a uniform coercive \(L^2\) floor. Do not infer \(\lambda_{\min}>0\) on the infinite odd carrier.

## 3. NEW certified whole-infinite-tail original operator-norm upper

Write \(Q_{j,p}=\sum_{n=0}^{p-1}4r\delta_j(2n+1)|q_{jn}\rangle\langle q_{jn}|\) and \(R_{j,p}=T_j-Q_{j,p}\succeq0\). The Hilbert-valued Legendre projection is the best \(L^2([-1,1];H_o)\) degree-<p approximation. Apply the **actual original sine** Taylor polynomial in \(t\) about zero:
\[
\left|\sin(2\pi(c_j+rt)x)
-\sum_{n=0}^{p-1}\frac{t^n}{n!}
\left.\partial_t^n\sin(2\pi(c_j+rt)x)\right|_{t=0}\right|
\le \frac{(2\pi rB)^p}{p!}
\quad(|t|\le1, |x|\le B).
\]
The genuine original two-dimensional \(t,x\) integral consequently gives
\[
\boxed{
0\preceq R_{j,p}\preceq
\frac{8B\delta_j r}{(p!)^2}
(2\pi rB)^{2p}I
}
\]
on **every** original physically supported odd profile. This is a uniform infinite-rank **remainder norm upper**, not a claim of its positive coercive lower.

The exact SM14 rational geometry has \(\sum_j\delta_j=35\). With original upper \(\pi<22/7\), \(B=11/10\), \(r=3/200\), verify
\[
\frac{2\cdot22}{7}\,rB<\frac18,
\qquad
\boxed{
0\preceq R_{13,\ge2}:=\sum_{j=1}^{13}(T_j-T_j^{[2]})
\prec\frac{3}{10000}I.
}
\]
The strict scalar \(3/10000\) has an **exact Fraction** proof:
\(8B r(\sum\delta_j)(1/8)^4/(2!)^2<3/10000\). (This is a norm upper, not a matrix-eigenvalue certificate.)

Thus **all** the physically supported original positive continuum of these thirteen windows can be resolved into **26 exact orthogonal-frequency physical vectors** and an independently accounted, positive, strictly positive-on-nonzero, infinite-rank remainder of norm \(<3\cdot10^{-4}\). Define
\[
B_{40}=B_{14}+\sum_j T_j^{[2]},\quad
\boxed{B_{40}\preceq B_{40}+R_{13,\ge2}
\preceq A_*,\quad B_{40}\succeq\kappa_*I.}
\]
\(B_{40}\) denotes at most 14+26 feature directions, not a claim those forty are linearly independent, and the source **odd pole remains exactly inside \(B_{14}\)**. The **actual signed-positive frequency continuum outside these thirteen bands** is still not paid by this minorant; do not confuse a complete-13-band expansion with the complete-positive-half-line operator.

A strong monotone-inverse corollary on the original full odd carrier is
\[
A_*^{-1}\preceq(B_{40}+R_{13,\ge2})^{-1}
\preceq B_{40}^{-1}
\preceq\kappa_*^{-1}I.
\]
This is a full-carrier **operator order**, not a evaluated 890-source inverse. In particular the strict positive remainder could improve the true inverse while a finite-dimensional reference remains inadequate. The positive tail upper **cannot** be subtracted as though it were a beneficial lower bound; only the exact positive tail identity justifies retaining it in \(B_{40}+R\).

## 4. Keep complete-operator odd acceptance explicit

The genuine original negative-frequency Taylor cap remains
\(K_{\neg,o}\preceq UDU^*+\eta I\), with all 890 original columns, all 107 original covariance blocks, complete cross terms and \(\eta<302/10^{12}\). The necessary **full** PS36 O1/O2 sufficient gate, for the new continuum-enriched *lower* reference, is
\[
\boxed{
S^{(40+\mathrm{tail})}_{890}
=
D^{-1}-U^*(B_{40}+R_{13,\ge2}-\eta I)^{-1}U
\succeq0.
}
\]
Its true original pole-conditioning and reference floor ensure the inverse is well-defined because \(\kappa_*>\eta\). The **correct** reference has 13 entire positive bands, not merely 26 discrete center packets; the remaining positive half-line response in \(A_*\) can only improve the original true gate, but its exact supported inversion remains unknown.

**SM28 does not establish the positivity of this 890-source operator.** It proves the exact continuum-preserving decomposition, strict original tail positivity, and a rigorous small *upper* on the tail; these are preconditioning tools, not O1/O2 closure. SM27's C33 negative 890-source surrogate shows feature count alone is insufficient; the expanded B40 may or may not pass. Neither statement is a true original odd negative eigenvalue.

**SM29 actionable:** construct the complete original 890-column *signed* Gram versus all 40 exact physical sources (SI29 fourteen + thirteen Legendre degree 0/1 pairs), including original pole conditioning, actual \(\eta\)-shift and all block offdiagonals, and/or develop an operator-valued positive-continuum residual lower useful for the entire original Schur. Evaluate the 890×890 residual spectrum with rigorous low/high blocks, not per-column scalar tests; if finite B40 fails, compare with the true strict-positive infinite-rank R, not an unjustified scalar uplift. The complete original O1/O2 odd, even E1–E4, full Weil, CC27 D-Riesz and RH all remain OPEN.

**Acceptance replay:** \`python3 scripts/validate_rpb108_sm28_positive_continuum_legendre_tower.py\`. Exact rational source geometry, full SM14/SM15 whole-real signed-frequency checks, Legendre Taylor-tail constants, original SI29 odd pole baseline and SM10 complete cap all validated. Infinite-dimensional Fourier analytic continuation/Legendre Parseval and operator order arguments need independent mathematical audit; CI alone is not such review.
