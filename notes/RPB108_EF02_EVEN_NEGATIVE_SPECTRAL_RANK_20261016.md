# RPB108 EF02 — fifteen true signed-negative EVEN packets and rank-one pole insufficiency

**Obligation:** W-EVEN-FORM (scoped; the canonical active obligation remains W-ODD-NEG).  
**Parent:** EF01, merged as PR #136 at research HEAD b9e195b30cabf965d4202e8ab330711b97f84ae0.  
**Standing:** conditional on focused exact-rational continuum and Gram replay at final PR head; analytic min–max theorem. This is a structural **method-class no-go**, not a witness against the original full even Weil form.

## 1. Exact original supported even operator, rather than a model

On the original physical carrier H_e=L²([-11/10,11/10])_even, with the original signed archimedean+seven-prime multiplier m of SI10/EF01 and κ=1/1000, put
\[
a(\xi)=\max(m(\xi),\kappa),\quad r(\xi)=(\kappa-m(\xi))_+,
\quad A_{0,e}=Z^*\mathcal F^{-1}a\mathcal FZ|_{H_e},
\quad K_e=Z^*\mathcal F^{-1}r\mathcal FZ|_{H_e}.
\]
The entire even Weil quadratic form is
\[
Q_e=A_{0,e}+2|c\rangle\langle c|-K_e,\qquad c(x)=\cosh(x/2).
\]
Here the **positive even pole** is real and favorable but rank one; the full positive supported Fourier operator A_{0,e} is not claimed finite rank and is never discarded from the original problem.

## 2. Fifteen actual signed-negative original frequency windows

Import SM04's independently replayed original signed m upper enclosures (Euler/digamma tail, all seven prime cosine intervals, and |p'|<69), not a sampled sign or toy symbol. The rational centers
\[
c_j\in\{1.90,7.26,14.42,20.04,27.32,39.08,44.70,59.12,
66.40,76.48,83.76,103.80,142.88,187.56,246.68\}
\]
have separation ≥5. Every complete interval ±[c_j−ρ,c_j+ρ], with
\(\rho=1/100\), is subdivided into four rigorously audited rational cells and satisfies \(m(\xi)<-\delta\), \(\delta=2/5\). Consequently \(r(\xi)>\delta\) throughout **both reflected bands**, without throwing away any unselected original negative-frequency contribution.

Unlike SM04's **odd sine** vectors, take the genuine even Jensen vectors
\[
g_j(x)=\frac1{2\rho}\int_{c_j-\rho}^{c_j+\rho}
\cos(2\pi\xi x)\,d\xi
=\cos(2\pi c_jx)\operatorname{sinc}(2\pi\rho x).
\]
Original even compression of the full multiplier yields the true Loewner minorant
\[
\boxed{K_e\succeq 4\rho\delta\sum_{j=1}^{15}
|g_j\rangle\langle g_j|},\qquad
\gamma=4\rho\delta=2/125.
\]
This is a physical, full-continuum operator inequality, not an assumption that the packets are Fourier eigenvectors.

## 3. Exact fifteen-vector physical cosine Gram, including all crosses

Let \(h_c(x)=\cos(2\pi cx)\). The exact physical Gram identity is
\[
\langle h_c,h_d\rangle=
\frac{\sin(2\pi B(c-d))}{2\pi(c-d)}
+\frac{\sin(2\pi B(c+d))}{2\pi(c+d)}
\quad (B=11/10);
\]
at \(c=d\) the first term is defined by continuity as \(B\).
Note the **plus sign** of the second term; reusing the odd sine Gram, which has a minus sign, is incorrect.

Define \(e=(2\pi_{\rm hi}\rho B)^2/6<1/100\). Pointwise
\(1-e\le\operatorname{sinc}(2\pi\rho x)\le1\) on the actual support.
Therefore the *true* even packet Gram \(H_{ij}=\langle g_i,g_j\rangle\)
has rigorous rational diagonal and offdiagonal enclosures
\[
H_{ii}\ge(1-e)^2\langle h_{c_i},h_{c_i}\rangle_{\rm lo},\qquad
|H_{ij}|\le|\langle h_{c_i},h_{c_j}\rangle|_{\rm up}+4Be.
\]
All fifteen diagonal rows and all 210 off-diagonal entries are charged.
The focused exact-rational validator requires the deliberately weaker inequalities
\[
\min_i H_{ii,\rm lo}>109/100,\qquad
\max_i\sum_{j\neq i}|H_{ij}|_{\rm up}<15/100,\qquad
\boxed{\lambda_{\min}(H)>93/100.}
\]
By min–max and the full original Loewner minorant,
\[
\boxed{\lambda_{15}(K_e)>
(2/125)(93/100)>3/200=0.015>\kappa=0.001.}
\]
The last stronger threshold is separately checked against the *unrounded* exact rational Gershgorin bound rather than deduced from \(93/100\), which alone would only yield 0.01488. These are eigenvalue **lower bounds for the negative part** \(K_e\), not for the complete signed \(Q_e\).

## 4. Uniform method-class obstruction, *including the positive even pole*

For any positive semidefinite T of rank≤13, the positive reference
\[
C=\kappa I+2|c\rangle\langle c|+T
\]
has non-scalar rank≤14. Because K_e has a 15-dimensional subspace where
every Rayleigh quotient exceeds \(3/200>\kappa\), there exists nonzero f
in that subspace orthogonal to c and \(\operatorname{ran}T\).
For this f, \(\langle f,Cf\rangle=\kappa\|f\|^2<
\langle f,K_e f\rangle\). Therefore
\[
\boxed{\text{For every }T\succeq0,\ \operatorname{rank}T\le13:
\quad \kappa I+2|c\rangle\langle c|+T\not\succeq K_e.}
\]
In fact the stronger general statement holds: **no** reference
\(\kappa I+T'\) with \(\operatorname{rank}T'\le14\) can dominate K_e.
This is independent of where the fourteen positive packet windows
would be placed, and shows that the positive even pole does not
transform a 13-feature-plus-floor surrogate into an all-negative-band
certificate. There are at least fifteen independent negative-frequency
directions substantially above the scalar floor.

**Crucial nonconclusion:** A_{0,e} is an actual positive
*infinite-rank supported Fourier operator*, not κI. It may absorb
K_e through structure absent in a finite positive reference.
This theorem does **NOT** show Q_e has a negative direction, does
**NOT** refute even positivity, and cannot close W-EVEN-FORM or RH.

## 5. Research disposition and next EF step

EF01's even cofinite bound and original finite inverse gate are retained.
EF02 eliminates a class of too-sparse even-pole-first certificates.
The next genuine closure route **must** employ sufficient
nontrivial original positive-frequency structure (or native RC's
correctly transported high-Schur block), then compute an actual
supported inverse/cross certificate. Repeated rank≤14 scalar-plus-feature
minorants cannot suffice for the full original negative continuum.
Do not replace this challenge with extra parity reformulations.

**Standing:** W-EVEN-FORM remains OPEN. Original entire even finite
Birman–Schwinger eigenvalue, full cross-terms, whole Weil form,
global bridge, Lean attachment and RH all remain unproved.

**Replay:** python3 scripts/validate_rpb108_ef02_even_negative_spectral_rank.py.
The focused CI checks the inherited exact original signed intervals and the
new even Gram. A passing workflow supports the stated conditional
operator certificate but is not independent mathematical peer review.
