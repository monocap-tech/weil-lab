# RPB108: additive quartic Bessel damping argument

Definitions: [quartic damping registry](../docs/TERMINOLOGY_RPB108_QUARTIC_DAMPING.md). This strengthens the existing quadratic damping note; it does not replace historical results.

The spherical-Bessel differential equation and regular series are recorded in NIST DLMF [10.47.1](https://dlmf.nist.gov/10.47.E1) and [10.53.1](https://dlmf.nist.gov/10.53.E1). The estimate below is derived here. The previous [positive-region proof](REFLECTED_PACKET_BRIDGE_108_DAMPED_COMPLEMENT_082_20261006.md) proves positivity of j_n on 0<x<=sqrt(n(n+1)), n>=1, by applying w_n''=(n(n+1)/x^2-1)w_n to w_n=x*j_n. It proves F_n=(2n+1)!!j_n/x^n positive and decreasing, with -F_n'/F_n>=x/(2n+3).

Put p=2n+2, A=1/(p+1), and y=-F_n'/F_n. Substitution into F_n''+p*F_n'/x+F_n=0 gives

\[
y'+(p/x)y=1+y^2.
\]

The regular origin series gives y=O(x), so the boundary term x^p*y vanishes at zero. Multiplying by x^p and integrating yields

\[
y(x)=x^{-p}\int_0^x t^p(1+y(t)^2)\,dt
\ge Ax+\frac{A^2}{p+3}x^3.
\]

Here the integrand bound uses the already proved y(t)>=A*t, which is nonnegative throughout the positive region. Integrating y=-d(log F_n)/dx from zero gives the stronger squared bound

\[
F_n(x)^2\le
\exp\left[-\frac{x^2}{2n+3}
-\frac{x^4}{2(2n+3)^2(2n+5)}\right].
\]

No new Bessel zero or positivity assumption is introduced. The squared quartic coefficient is obtained by integrating 2*A^2*x^3/(p+3); it is not an empirical fit.

For z,w>=0 and 0<s<=1, log(s)<=(s^2-1)/2 and log(s)<=(s^4-1)/4 imply

\[
e^{-zs^2-ws^4}\le e^{-z-w}s^{-2z-4w}.
\]

Consequently, if r=2n+1-2z-4w>0,

\[
\int_0^1 s^{2n}e^{-zs^2-ws^4}\,ds\le\frac{e^{-z-w}}r.
\]

Apply this to the actual plane-wave projection norm 2a*sum_(n>=k)(2n+1)*j_n(2*pi*a*t)^2. For Y=2*pi*a*T, use Y_upper for powers and the rate, Y_lower for the damping exponent, and the reciprocal of the positive 81-term exponential Taylor sum as an outward upper bound on exp(-z_lower-w_lower). The high-endpoint rate is no larger than the low-endpoint rate, so this replacement only increases the mass bound. Explicitly check both Y_upper^2<k(k+1) and every positive rate. Sum degrees k through k+47 and add the existing complete undamped bound from k+48 onward. Thus every infinite-tail degree remains included.

This proves the new helper's integrated mass bound. At each chosen fixed aperture and cutoff, the original actual prime chains, signed pole allowance, archimedean low floor, high-frequency bound and independent logarithmic complement must still be checked. A complement improvement alone does not certify the full-domain corrected sign.
