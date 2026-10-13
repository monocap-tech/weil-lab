# RPB108: explicit archimedean envelope and finite-certificate cost

Base: research cea15d5997d2b8313dc744c87c1f823d793b482f.

## Result

The generic finite-form certificate no longer needs an unspecified archimedean constant. In the actual project normalization,
\[
|\operatorname{arch}(2\pi\xi)-\log(e+|\xi|)|
\le4+\log(1+4\pi e)<10.
\tag{1}
\]
A simple full correction bound is therefore
\[
\|C_a\|\le\overline c_a:=10+12ae^a.
\tag{2}
\]
Explicit T and N below guarantee any requested native operator error epsilon in (0,1).

The resulting sufficient sizes are extremely large. This is a rigorous analytic construction, not a practical numerical solver or a completed sign computation.

## Terminology before use

**Explicit archimedean envelope:** a stated uniform constant bounding the actual digamma symbol's difference from the canonical logarithmic weight.

**Sufficient certificate size:** a chosen T,N proving the requested error; not a lower bound on all possible approximations.

**Certificate cost audit:** evaluation of how large this particular sufficient construction is, without equating theoretical existence with implementability.

## Direct Euler sum-integral estimate

For Re z=s>0, the already used digamma Euler series gives
\[
\psi(z)=\lim_{m\to\infty}
\left(\log m-\sum_{n=0}^{m-1}\frac1{n+z}\right).
\]
This follows by writing the finite Euler sum as H_m minus the reciprocal sum and using H_m-log m -> gamma.

Put f(t)=1/(t+z). On each unit interval,
\[
f(n)-f(t)=\int_n^t\frac{du}{(u+z)^2}.
\]
Hence, for E_m=sum f(n)-integral_0^m f(t)dt,
\[
|E_m|\le\int_0^m\frac{du}{|u+z|^2}
\le\int_0^\infty\frac{du}{(u+s)^2}
=\frac1s.
\]
The errors have an absolutely convergent limit by the same estimate. On the right half-plane the principal logarithm gives
integral_0^m f=log(m+z)-log z. Since log m-log(m+z) -> 0,
\[
|\psi(z)-\log z|\le\frac1{\Re z}.
\tag{3}
\]
No digamma asymptotic remainder is imported.

## Exact project normalization

The actual archimedean multiplier is
\[
\operatorname{arch}(2\pi\xi)
=\Re\psi(1/4+i\pi\xi)-\log\pi.
\]
At z=1/4+i pi xi, (3) bounds its difference from log|z|-log pi by 4.

Put t=|xi| and q=1/(4pi). The remaining logarithmic difference is
\[
\log\frac{\sqrt{q^2+t^2}}{e+t}.
\]
The ratio is at most one since sqrt(q^2+t^2)<=q+t<=e+t. It is at least q/(e+q): for t<=q use numerator>=q, and for t>=q use numerator>=t and t/(e+t)>=q/(e+q).

Thus its absolute logarithm is at most log(1+4pi e), proving (1). For the coarse rational envelope 10, use pi<4, 2<e<3:
1+4pi e<49<64<e^6, hence log(1+4pi e)<6.

This explicit value can replace C0 in the existing positive-seed and finite-approximation estimates. It does not certify a maximal positivity aperture.

## Explicit finite prime and pole bound

The actual correction estimate was
\[
\|C_a\|\le C_0+
2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+4ae^a.
\]
Since Lambda(n)<=log n<=2a and the sum is included in n<=M=floor(e^(2a)),
\[
2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
\le4a\sum_{n=1}^{M}n^{-1/2}
\le8a\sqrt M\le8ae^a.
\]
The middle bound follows by comparison with the decreasing integral; including n=1 only overestimates because Lambda(1)=0. This proves (2), retaining the actual pole estimate.

No numerical prime list or zero data is required for this deliberately coarse bound.

## Completely specified approximation sizes

Fix desired error 0<epsilon<1. Set
\[
\theta=\min\{1/2,\epsilon/(3\overline c_a)\},
\qquad T=\exp(4/\theta^2),\qquad L=2\pi aT.
\]
Choose an integer k>=1 such that
\[
k\ge2eL,\qquad
k\ge\frac{L+\log(2\sqrt{4aT}/\theta)}{\log2},
\quad N=k-1.
\tag{4}
\]
Taking the ceiling of the maximum of these three requirements suffices.

The Fourier tail in the preceding certificate is at most theta/2 since log(e+T)>=4/theta^2. Also
\[
k!\ge(k/e)^k,
\]
which follows by integrating log t from 1 to k. Therefore
\[
\sqrt{4aT}e^L\frac{L^k}{k!}
\le\sqrt{4aT}e^L(eL/k)^k
\le\sqrt{4aT}e^L2^{-k}
\le\theta/2.
\]
Thus eta_TN<=theta and
\[
\|A-A_{TN}\|\le\overline c_a\theta(2+\theta)
\le3\overline c_a\theta\le\epsilon.
\tag{5}
\]
Every constant and sufficient cutoff in this analytic bound is now specified.

Finite Gram/native entries still require evaluation or rigorous enclosure. Specifying the tail does not compute those entries or their spectral signs.

## Cost audit and limits

For the illustrative a=1/2 and epsilon=1/4, cbar=10+6 sqrt(e), and the above choice gives
\[
\log_{10}T=
\frac{4(12\overline c_a)^2}{\log10},
\]
approximately 99,000. The finite degree in (4) is at least proportional to this enormous T.

The decimal figure is illustrative floating-point arithmetic, not a formal numerical certificate or an eigenvalue computation. The exact displayed formula is the proved sufficient size.

This quantifies why the generic Fourier-tail/Taylor construction should not be treated as ready for direct matrix computation. The slow logarithmic tail and global Taylor bound are highly conservative. It is not proved that a native-adapted method must pay this cost; this is not a complexity lower bound for the problem.

A practical certificate would need sharper native correction estimates, a better finite basis, stronger control of the relevant near-null range, or another approximation strategy. Implementing this sufficient construction blindly would not be a justified next computational step.

## Remaining input and validation

The finite certificate theorem is analytically explicit, but no actual finite matrix sign or endpoint exclusion has been obtained. Better constants cannot by themselves settle the global null question. The signed endpoint-to-Gaussian upper estimate remains independent.

Self-contained proof from the Euler series already in the actual dictionary and elementary integral/factorial estimates. No new external input, actual negative vector, endpoint, RH conclusion, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At cea15d5, all constants in the generic finite-form tail certificate are explicit. The Euler digamma sum compared directly with its integral proves |psi(z)-log z|<=1/Re z on the right half-plane. With the actual symbol Re psi(1/4+i pi xi)-log pi, this gives |arch(2pi xi)-log(e+|xi|)|<=4+log(1+4pi e)<10. The full bounded physical correction therefore has norm <=cbar_a=10+12a exp(a), using a crude finite prime-power bound and the actual pole estimate. For desired operator error eps in (0,1), choose theta=min(1/2,eps/(3cbar_a)), T=exp(4/theta^2), and k=N+1 above both 2e(2pi aT) and [2pi aT+log(2sqrt(4aT)/theta)]/log2. These choices prove eta<=theta and actual native error<=eps. The cost is explicitly enormous: even the illustrative a=1/2, eps=1/4 construction selects T with about 99,000 decimal digits. This is a cost of this coarse sufficient construction, not a lower bound for all methods. The finite certificate is rigorous but not a practical numerical solver; native-specific sharper estimates or a different approximation remain needed before implementation. No numerical sign, endpoint, RH conclusion, new Lean or CI result; FULL TRANSPORT CLOSED remains open.
