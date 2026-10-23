# W-ODD-NEG — Original 470 physical sources in the strong multiplier domain

**Date:** October 23, 2026. **Scope:** an analytic SOURCE-DOMAIN consequence of SM35 source geometry and SM41 multiplier growth, *conditional on the original supported Fourier operator/form realization*. This does not close that independent realization/interface audit, MG07, signed odd, even, CC27, the Weil criterion, or RH.

## Exact physical source family

SM35's exceptional synthesis \(J:\mathbb R^{470}\to H_o\) consists of 469 odd zero-extended supported generators \(f_{c,k}(x)=x^k\sin(2\pi c x)\) for even \(k\), or \(x^k\cos(2\pi c x)\) for odd \(k\), at the 107 distinct original rational cluster centers, together with \(s(x)=\sinh(x/2)\). Each is supported on \([-B,B]\), \(B=11/10\), and belongs to \(W^{1,1}(-B,B)\). Their zero extensions can have boundary jumps; no global \(W^{1,1}(\mathbb R)\) or twice-differentiable zero-extension hypothesis is made.

With the Fourier convention \(\widehat f(\xi)=\int f(x)e^{-2\pi i\xi x}dx\), integration by parts inside \([-B,B]\), explicitly retaining both boundary terms, gives for \(\xi\ne0\):
\[
 |\widehat f(\xi)|\le
 \frac{|f(B)|+|f(-B)|+\int_{-B}^B|f'(x)|dx}{2\pi|\xi|}.
\]
For each polynomial generator, bounding the derivative and using \(\pi>3\) gives the exact rational envelope
\[
 |\widehat{f_{c,k}}(\xi)|\le \frac{C_{c,k}}{|\xi|},\qquad
 C_{c,k}=\frac{1+\mathbf1_{k>0}}3 B^k+
               \frac{2cB^{k+1}}{k+1}.
\]
For the true supported pole, let \(y=B/2=11/20<1\). The positive-series bound \(\sinh y\le y/(1-y^2)\) gives, accounting for both endpoint values and the derivative's full \(L^1\) norm,
\[
 |\widehat{s}(\xi)|\le\frac{C_s}{|\xi|},\qquad
 C_s=\frac23\frac{y}{1-y^2}=\frac{440}{837}.
\]

## Complete high-frequency original positive multiplier bound

SM41's inherited original odd positive multiplier bound is
\(0<a_o(\xi)\le17+\log|\xi|\) for \(|\xi|\ge1\). Integration by the substitution \(u=\log t\) gives
\[
 \int_{|\xi|\ge1}\frac{(17+\log|\xi|)^2}{\xi^2}d\xi
 =2\int_0^\infty e^{-u}(17+u)^2du
 =650.
\]
Let \(C=(C_{c,k},C_s)\in\mathbb Q_{>0}^{470}\). For every actual coefficient vector \(z\), triangle and coefficient Cauchy give
\[
 |\widehat{Jz}(\xi)|\le\frac{\|C\|_2\|z\|_2}{|\xi|}.
\]
Consequently the **entire untruncated original high-frequency multiplier action** obeys the finite rational 470-dimensional coefficient-space Loewner estimate
\[
 \boxed{\int_{|\xi|\ge1}a_o(\xi)^2
               |\widehat{Jz}(\xi)|^2d\xi
      \le650\|C\|_2^2\|z\|_2^2.}
\]
This is a rigorous (under SM41) whole-source high-tail bound, **not** a useful quantified MG07 residual estimate: absolute values destroy frequency/source cancellation. Its full-line multiplier-action norm is an upper bound for the corresponding compressed supported operator-action norm, not an identity for that compression.

The original digamma-plus-seven-prime multiplier is continuous and bounded on the compact \([-1,1]\), and each \(Jz\in L^2\). Therefore \(a_o\widehat{Jz}\in L^2(\mathbb R)\). Under the standard closed supported positive Fourier-form construction, this condition is sufficient for \(Jz\in\operatorname{Dom}(A_o)\): the functional \(g\mapsto\int a_o\widehat{Jz}\overline{\widehat g}\) is bounded in the \(H_o\) norm and represented by compression of the whole-line multiplier action. The rank-one pole \(2|s\rangle\langle s|\) is bounded, so \(\operatorname{Dom}(A_\star)=\operatorname{Dom}(A_o)\). Thus all 470 actual generators are strong-domain admissible in this precise operator realization.

**Still open:** independent identification of the project's claimed original Weil/odd form with that Fourier-form realization, and the complete same-trial actual 470×470 \(G_0\), \(N_{0,\mathrm{cap}}\) and \(D_B\) matrices with rational Loewner control. Neither signed odd positivity nor RH follows.

**Replay:** \`python scripts/validate_rpb108_odd470_strong_domain_tail.py\`. Rational geometry/envelope computations are checked; the analytic integration-by-parts and operator-representation argument still require human proof review.
