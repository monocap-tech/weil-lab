# RPB108: one-sided Gaussian decay and the exact upper-bound obstruction

Base: research e1615858981c7ca33b8605c604e554b7dc94559d.

## Minimal theorem

Let h be a complex L2 vector supported in [-c,c], with c finite, and write
\[
F(\xi)=\widehat h(\xi),\qquad
M_R=\int_{\mathbb R}
 e^{-(2\pi\xi-R)^2/R}|F(\xi)|^2\,d\xi,\quad R\ge1.
\]
If, for some positive delta and finite C,R0,
\[
M_R\le C e^{-\delta R}\qquad(R\ge R_0),
\tag{1}
\]
then h=0.

No symmetry, reality, zeta-zero assumption, source positivity, retained membership or operator-domain assumption is needed. The theorem uses only the positive-frequency Gaussian sweep. In particular, the negative-frequency half-line need not satisfy any additional decay estimate.

For a nonzero compactly supported h, M_R>0 for every R and
\[
\limsup_{R\to\infty}\frac{\log M_R}{R}=0.
\tag{2}
\]
Thus Gaussian mass can decay faster than powers without having a strictly negative exponential limsup.

## Terminology before use

**One-sided exponential Fourier mass** means
\[
\int_0^\infty e^{\kappa\xi}|F(\xi)|^2\,d\xi<\infty
\]
for some kappa>0. It is an averaged L2 property, not a pointwise bound.

**Eventual exponential Gaussian upper bound** means (1) for every sufficiently large real R. Sparse estimates along a subsequence do not instantiate it.

**Endpoint-null-to-upper-estimate input** means a theorem deriving an eventual upper estimate on the genuine frozen action from the lawful actual endpoint-null premises for the same vector. It does not mean assuming larger-window nullity or replacing the action by a different residual.

## Logarithmic integral lemma: direct proof

Compact support makes h integrable. Its Fourier transform extends to an entire function
\[
F(z)=\int_{-c}^c h(x)e^{-2\pi i z x}\,dx.
\]
For Im z>=0, the function
\[
Q(z)=e^{2\pi i c z}F(z)
=\int_{-c}^c h(x)e^{-2\pi i z(x-c)}\,dx
\]
is bounded by ||h||_1, since x-c<=0. On the real line |Q|=|F|.

Suppose h is nonzero. Fourier injectivity makes Q nonzero, so choose z0=x0+i y0 in the upper half-plane with Q(z0)!=0. Put B=max(1,||h||_1) and map the disk to that half-plane by
\[
\phi(w)=x_0+i y_0\frac{1+w}{1-w}.
\]
The holomorphic function H(w)=Q(phi(w))/B satisfies |H|<=1 and H(0)!=0. Jensen's inequality for its logarithmic mean gives
\[
\frac1{2\pi}\int_0^{2\pi}
 -\log|H(r e^{i\theta})|\,d\theta
 \le-\log|H(0)|,\qquad 0<r<1.
\]
Zeros on an integration circle are harmless logarithmic singularities; the mean formula, or its limiting version, applies.

The integrands are nonnegative. At every boundary point except w=1, phi approaches a finite real number and Q is continuous there. Fatou and the boundary change of variables therefore give
\[
\int_{\mathbb R}
 \frac{y_0}{\pi((t-x_0)^2+y_0^2)}
 \left[-\log\frac{|F(t)|}{B}\right]dt<\infty.
\]
The Poisson weight is comparable, above and below, with (1+t^2)^(-1). Hence
\[
\int_{\mathbb R}
 \frac{-\log(|F(t)|/B)}{1+t^2}\,dt<\infty.
\tag{3}
\]
The nonnegative integrand is allowed the value infinity at zeros; isolated zeros do not invalidate integrability.

This is the relevant Paley-Wiener logarithmic obstruction. For literature context, Bhowmik, J. Aust. Math. Soc. 109 (2020), Theorem 1.2 recalls the half-line logarithmic-integral criterion:
https://doi.org/10.1017/S1446788719000077
The proof above supplies the exact lemma used here; no decay theorem is imported without proof.

## One-sided exponential Fourier mass forces zero

Suppose the one-sided exponential Fourier mass is finite, with value E. For integers n>=0,
\[
J_n:=\int_n^{n+1}|F(t)|^2dt\le E e^{-\kappa n}.
\]
If E=0, F vanishes on the positive half-line and h=0 immediately. Otherwise, assuming h nonzero, concavity of log on the interval of length one gives
\[
\int_n^{n+1}\log\frac{|F(t)|}{B}\,dt
 \le\frac12\log\frac{J_n}{B^2}
 \le\frac12\log\frac{E}{B^2}-\frac{\kappa n}{2}.
\]
Jensen may first be applied to |F|^2+epsilon and then epsilon decreased to zero. Formula (3) ensures the resulting negative logarithm is integrable on each compact interval.

Writing v(t)=-log(|F(t)|/B)>=0, for all sufficiently large n,
\[
\int_n^{n+1}v(t)\,dt\ge\frac{\kappa n}{4}.
\]
Consequently
\[
\int_0^\infty\frac{v(t)}{1+t^2}\,dt
 \ge\sum_{n\ \mathrm{large}}
 \frac{\kappa n}{4(1+(n+1)^2)}=\infty.
\]
This contradicts (3). Thus one-sided exponential Fourier mass implies h=0. The argument applies to arbitrary complex h.

## The moving Gaussian supplies that mass

Assume (1) and choose 0<epsilon<delta. Then
\[
I:=\int_{R_0'}^\infty e^{\epsilon R}M_R\,dR<\infty,
\qquad R_0'=\max(1,R_0).
\]
By nonnegative Tonelli,
\[
I=\int_{\mathbb R}|F(\xi)|^2
 \left[\int_{R_0'}^\infty
 e^{\epsilon R-(2\pi\xi-R)^2/R}\,dR\right]d\xi.
\]
For t=2pi xi>=R0', restrict the inner integral to R in [t,t+1]. On this interval,
\[
\frac{(t-R)^2}{R}\le1,\qquad e^{\epsilon R}\ge e^{\epsilon t}.
\]
Its length is one. Thus
\[
I\ge e^{-1}\int_{R_0'/(2\pi)}^\infty
 e^{2\pi\epsilon\xi}|F(\xi)|^2\,d\xi.
\]
The remaining bounded positive-frequency interval has finite weighted mass by Plancherel. This proves one-sided exponential Fourier mass and therefore h=0.

For nonzero h, beta_R>0 gives M_R>0 and beta_R<=1 gives M_R<=||h||_2^2. These imply the limsup in (2) is at most zero. A strictly negative limsup would imply (1), contrary to the theorem. This proves (2).

## Consequence for the genuine native action

Assume now h has finite logarithmic Fourier energy and use the actual fixed-cutoff frozen action from the preceding moving-Gaussian coercivity theorem. Put g_R=K_R*h with the exact project normalization. That theorem proves
\[
\Re\mathcal A_a(h;\overline{g_R})
 \ge(\log R-C'_a)M_R
 -D_{a,c}(1+\log R)e^{-R/4}\|h\|_2^2.
\tag{4}
\]

If, for some delta>0, finite C and finite p>=0, the genuine action also obeys
\[
\Re\mathcal A_a(h;\overline{g_R})
 \le C(1+R)^p e^{-\delta R}
\qquad(R\ \mathrm{sufficiently\ large}),
\tag{5}
\]
then h=0. In particular an absolute-value upper estimate suffices, but is stronger than necessary.

Indeed take 0<eta<min(delta,1/4), and R large enough that log R-C'_a>=1. Combining (4) and (5), then absorbing their polynomial and logarithmic prefactors into the strictly larger exponential rates, gives
\[
M_R\le C_\eta e^{-\eta R}.
\]
The minimal theorem applies.

Equivalently, for every nonzero supported logarithmic h, every delta>0, p>=0, C>=0 and R0, some R>=R0 violates (5). This is a precise obstruction to an unconditional exponential residual-action estimate on the actual nonzero carrier.

## Scope and the remaining independent input

The conclusion is not that an endpoint-null-to-upper-estimate theorem is logically forbidden. Such a theorem, if independently proved, would combine with (4) and the result above to exclude nonzero endpoint null modes. That is a legitimate proof-by-contradiction route.

What is forbidden is treating (5) as an ordinary universal estimate for a genuine nonzero compactly supported vector, or obtaining it merely by changing representations. The theorem proves that this estimate already has null-exclusion strength when restricted to the endpoint-null class.

The existing strict-gap residual bound still demands central vanishing on a larger window. Earlier translation and finite-nullity results rule out that vanishing for a nonzero same vector. We have not derived (5) from the remaining lawful endpoint-null premises, and have not constructed or asserted an actual endpoint null mode.

This chunk closes the analytic implication from an eventual exponential Gaussian upper bound to zero. It avoids a separate two-sided decay or strip-holomorphy stage. It does not close F4 transport or FULL TRANSPORT CLOSED, and it adds no source/null assumptions.

## Validation and cursor

Analytic verification: direct disk Jensen/Fatou, explicit unit-interval logarithmic estimate, nonnegative Tonelli with the exact Gaussian normalization, and the preceding native action lower bound. No Lean source or workflow changes. No new CI result is claimed; certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At e161585, the actual moving-Gaussian mass M_R cannot have an eventual exponential upper bound for any nonzero compactly supported complex L2 vector. A bounded upper-half-plane Fourier function and Jensen/Fatou give finite weighted negative logarithm; one-sided exponentially weighted Fourier L2 mass contradicts it. Tonelli on R in [2pi xi,2pi xi+1] converts exponential M_R decay to that forbidden one-sided mass. Combining this with the proved actual Gaussian lower bound shows that even an eventual polynomial-times-exponential upper bound on the real genuine frozen action forces h=0. This closes the analytic Gaussian-upper-bound-to-zero implication without a two-sided or even-real hypothesis. It does not derive the upper bound from actual endpoint nullity. The remaining independent input is exactly a lawful same-vector endpoint-null-to-upper-estimate theorem (or a different null-exclusion argument); the old strict-gap central-null interface remains obstructed. No actual endpoint null mode, residual regularity, RH conclusion or new Lean/CI result is asserted. FULL TRANSPORT CLOSED remains open.
