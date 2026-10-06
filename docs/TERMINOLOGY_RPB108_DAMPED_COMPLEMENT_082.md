# RPB108 terminology: damped actual complement at 41/50

Introduced with `REFLECTED_PACKET_BRIDGE_108_DAMPED_COMPLEMENT_082_20261006.md`. The physical basis, actual native form and full residual Gram retain their existing conventions.

- **Spherical Bessel function j_n:** the regular solution of x^2 j_n''+2x j_n'+(x^2-n(n+1))j_n=0, normalized by j_n(x)~x^n/(2n+1)!! at zero.
- **Normalized Bessel tail F_n:** (2n+1)!! j_n(x)/x^n, with F_n(0)=1. For n>=1 and 0<=x<=sqrt(n(n+1)), it is positive and bounded above by exp(-x^2/[2(2n+3)]).
- **Physical plane-wave tail:** the W_k projection of exp(2*pi*i*t*u) on [-a,a]. Its squared norm is 2a*sum_{n>=k}(2n+1)j_n(2*pi*a*t)^2.
- **Existing undamped mass bound B(a,k,T):** 4aT*(2a*(22/7)*T)^(2k)/[(2k+1)!!]^2 divided by 1-(2a*(22/7)*T)^2/[(2k+1)(2k+3)]. Its geometric ratio must be below one.
- **Damped finite block:** degrees k through k+N-1. This pass uses a=41/50, k=84, N=16, T=67/5 and frequency split q=87/100.
- **Squared-tail damping exponent z:** (2a*pi_lower*q*T)^2/[2(k+N-1)+3]. It applies to the finite block on qT<=|t|<=T, after verifying (2a*pi_upper*T)^2<k(k+1).
- **Rational attenuation E:** an outward upper bound for 1/sum_{j=0}^{60}z^j/j!, hence for exp(-z). The damped integrated mass bound is B(a,k,qT)+E*B(a,k,T)+B(a,k+N,T).
- **New actual complement c:** 3/5 at the fixed aperture 41/50, with inverse factor beta=5/3. The prior beta=2 estimator and its negative direction remain historical certificates.
- **Refined corrected margin tau:** the certified positive margin for Q84-(5/3)Rhat84-((5/3)delta+tau)I using the complete pinned Gram and its actual source error.
- **Full-domain coefficients:** with lift bound J, mu=tau*c/[tau+c(1+J^2)] and kappa=mu/[10(mu+23)]. They bound the full native physical and logarithmic energies at this aperture.

The new tail inequality is proved analytically in the companion note. Finite series and rational controls validate its numerical application; they do not mechanically formalize the differential-equation argument. Global endpoint exclusion, historical packet attachment, F4 and FULL TRANSPORT CLOSED remain open.
