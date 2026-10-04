# RPB108: actual symbol growth and the boundary-removal central gate

Base: research 291257bf0bc9d3405553e13a9b605d7e92b15dcf.

## Result

The actual right-limit native multiplier has temperate growth at every fixed cutoff, by a direct derivative argument from the already certified digamma Euler series. This supplies the analytic content of RightLimitWeilSymbolTemperatePremise without imposing physical operator-domain membership on a witness.

With that genuine symbol, the frozen compact action and native mixed form agree:
\[
\mathcal A_a(h;u)=Q_a(\overline u,h)
\]
for compact smooth tests supported in (-a,a).

Consequently, for an actual logarithmic vector h supported in [-c,c], c<a, the central-cancellation hypothesis used by the current boundary-removal theorem forces h=0. The desired nonzero same-vector instantiation is obstructed. This distinguishes a valid conditional assembly theorem from a realizable nonzero input to it.

## Uniform digamma derivative bounds from existing Euler custody

The certified module NeutralDigammaEulerIdentity proves, for Re z>0,
\[
\psi(z)=-\gamma+\sum_{n=0}^\infty
 \left(\frac1{n+1}-\frac1{n+z}\right).
\]
On compact subsets of the right half-plane, each original term is
\[
\frac{z-1}{(n+1)(n+z)},
\]
so the series converges locally normally. For every k>=1 the differentiated terms are
\[
(-1)^{k+1}k!(n+z)^{-k-1}.
\]
They converge uniformly on Re z>=1/4 by the Weierstrass bound
\[
k!(n+1/4)^{-k-1}.
\]
Termwise holomorphic differentiation is therefore justified, locally normally at every order; it is not inferred from the zeroth-order asymptotic.

On the quarter line z=1/4+i pi xi,
\[
|\psi^{(k)}(z)|
 \le k!\sum_{n=0}^\infty(n+1/4)^{-k-1}
 \le k!(4^{k+1}+2).
\]
The last bound separates n=0 and uses
sum_{n>=1}n^{-k-1}<=sum_{n>=1}n^{-2}<=2.

The actual archimedean function is
\[
\alpha(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi.
\]
It is smooth, with
\[
|\alpha^{(k)}(\xi)|
 \le\pi^k k!(4^{k+1}+2),\qquad k>=1.
\tag{1}
\]
These are uniform bounds on all real frequencies. They are sufficient polynomial bounds; decay of polygamma is unnecessary.

At order zero the already certified archimedean/log comparison gives
\[
|\alpha(\xi)|\le C+\log(e+|\xi|)
 \le C+e+|\xi|.
\tag{2}
\]
For fixed a, the threshold-corrected prime set is finite. The k-th derivative of each cosine term is bounded by
\[
|\operatorname{coefficient}(n)|\,|2\pi\log n|^k.
\]
Together (1), (2) and finite summation prove smoothness and polynomial control of every iterated derivative of
\[
m_a(\xi)=\operatorname{rightLimitCompactWeilSymbolMathlib}(a,\xi).
\]
On the one-dimensional real domain, ordinary derivative bounds also control the corresponding iterated Fréchet derivatives. This proves Function.HasTemperateGrowth of the actual complex-valued symbol analytically, hence the stated symbol premise. No new external polygamma input is used.

This is not yet a new Lean constructor for that premise. The existing Euler and zeroth-order lemmas are certified; the all-order differentiation and bound argument here is analytic.

## Exact frozen/native compact-test dictionary

Let h be supported in [-c,c], with finite logarithmic energy, and let u be a compact smooth test supported in (-a,a), where c<=a. Set g=conjugate(u). Both g,h are lawful in D_a.

The repository uses the positive physical compact transform and the mathlib Fourier convention exp(-2pi i x xi). The native multiplier pairing is
\[
\int\overline{\widehat g(\xi)}m_a(\xi)\widehat h(\xi)\,d\xi.
\]
Since
\[
\widehat{\overline u}(\xi)=\overline{\widehat u(-\xi)},
\]
this equals the bilinear pairing
\[
\int\widehat u(-\xi)m_a(\xi)\widehat h(\xi)\,d\xi.
\tag{3}
\]

The actual symbol is real and even, by the certified digamma conjugation and cosine dictionaries. The distributional multiplier transpose, applied to the actual L2 distribution of h, gives precisely (3), by bilinear Plancherel. More explicitly its test multiplier is Fourier(m_a inverseFourier(u)), and
\[
\int h(x)\operatorname{Fourier}(v)(x)\,dx
 =\int\widehat h(\xi)v(\xi)\,d\xi,
\qquad v=m_a\operatorname{inverseFourier}(u).
\]
Since inverseFourier(u)(xi)=Fourier(u)(-xi), this is exactly (3). No change to the physical exponent convention is made.

All operations are genuine: temperate growth makes the Schwartz multiplication branch lawful; m_a times inverseFourier(u) is Schwartz. Its pairing with h is absolutely integrable by L2 Cauchy-Schwarz. Equivalently the spectral integral (3) converges absolutely because u is Schwartz and m_a has logarithmic growth. We do not assume m_a Fourier(h) is L2. The distributional and form domains are not confused.

For the physical pole,
\[
\operatorname{pole}_h(x)
 =M_-(h)e^{x/2}+M_+(h)e^{-x/2}.
\]
Thus
\[
\int u(x)\operatorname{pole}_h(x)\,dx
 =\overline{M_-(g)}M_+(h)+
   \overline{M_+(g)}M_-(h),
\]
exactly the native complex mixed cross-moment term. Both compact pole products are integrable. Adding this to (3) proves
\[
\operatorname{frozenWeilCompactAction}(h,a,u)=Q_a(g,h).
\tag{4}
\]
The physical carrier must contain this same h and its actual tempered L2 distribution; the identity does not identify an independently named carrier with h by fiat.

## What the existing central gate actually requires

NeutralSourceBoundaryRemoval, theorem
neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation,
requires c<a and
\[
\mathcal A_a(h;u)=0
\]
for every compact Schwartz u with support strictly inside (-a,a), as well as a regular defect representative.

By (4), this central hypothesis gives Q_a(g,h)=0 for every compact smooth g supported in (-a,a). These tests are dense in D_a in logarithmic energy by the previously proved inward-dilation/convolution theorem. Continuity of the native mixed form yields
\[
Q_a(g,h)=0\quad\hbox{for every }g\in D_a.
\tag{5}
\]
Conversely (5) gives the central compact-test hypothesis immediately.

Because h is supported in the strictly smaller window [-c,c], the native translation/finite-nullity theorem applies and proves h=0. Thus, for this actual carrier,
\[
\text{strict support margin + central frozen cancellation}
 \quad\Longrightarrow\quad h=0.
\]

Regularity of the defect cannot remove this contradiction for a proposed nonzero input. The central hypothesis alone already forces zero. Nor can a finite selected null equation supply it: the finite selected-forcing record proves the exact extra forcing, and the strict-margin selected obstruction.

## F4 implication

The existing boundary-removal theorem remains correct as a conditional theorem. Its central hypothesis is simply unavailable for the nonzero actual same-vector witness under the current strict-margin contract. Supplying more source representations or proving the symbol premise does not make that nonzero input possible.

The actual symbol premise is now analytically discharged, and the frozen/native convention ambiguity is resolved. The remaining obstruction is mathematical: the input demands full native weak-nullity on a window strictly larger than the vector's support.

A revised route would need a different conclusion or witness construction that does not require this impossible input, while preserving whatever custody its eventual argument consumes. This record does not propose or instantiate that new route. It does not prove RH and does not establish FULL TRANSPORT CLOSED.

## Validation and cursor

Analytic proof from the existing certified right-half-plane Euler identity, native log envelope and Fourier/pole definitions, plus the recent analytic carrier-density and null-extension theorems. No new external source. No Lean source/workflow changes or new CI claim. Existing certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 291257b, the certified right-half-plane digamma Euler series supplies uniform positive-order derivative bounds on the quarter line: |d^k arch(2pi xi)/d xi^k|<=pi^k k!(4^(k+1)+2), k>=1. Together with the native logarithmic bound and finite cosine derivatives this proves actual RightLimitWeilSymbolTemperatePremise analytically for every cutoff, without an operator-domain premise for h. Bilinear Plancherel and the exact complex pole cross moments prove frozenWeilCompactAction_a(h;u)=Q_a(conj u,h) on compact central tests. Thus the existing boundary-removal central hypothesis for a supported actual logarithmic vector with strict support margin c<a is equivalent by test density to full native weak-nullity on D_a, and forces h=0 by the proved translation/finite-nullity obstruction. Consequently the current nonzero same-vector boundary-removal/F4 entry contract cannot be instantiated; it is not merely awaiting another representation theorem. No alternative F4 transport or RH contradiction is constructed. Analytic only; Lean unchanged; FULL TRANSPORT CLOSED and F4 entry remain open.
