# RPB108: fresh matched aperture 19/20, finite/source stage

Use the actual window I=(-19/20,19/20) and physical orthonormal basis
sqrt((2n+1)/(2a)) P_n(x/a), n=0,...,83. The prime-power terms are
2,3,4,5, with amplitude Lambda(n)/sqrt(n); Lambda(4)=log(2).

The native constructor uses L=4a=19/5, exponential ceiling 45, kernel
ceiling 19/4, exponential order 260 and 250 Bernoulli pairs. The fresh
source constructor uses its independently checked ceiling 9/4, order 90,
100 alternating Bernoulli pairs and complete coefficient rounding error.
The nine-panel ordering and all active translations are recomputed at a.

The combined prime operator T is the bounded self-adjoint sum of the eight
signed supported translations. It has a nonnegative kernel; this is not a
claim that T is positive semidefinite. For even depth d, the positive-kernel
Schur row-mass bound gives ||T||^d=||T^d||<=sup(T^d 1). Every intermediate
prefix must remain in I. The fresh sixth- and tenth-power bounds are
937/500 and 919/500, respectively. A rejected smaller row-mass ceiling is
not an operator-norm lower bound.

For the 84-moment complement use inner cutoff 13 and outer cutoff 141/10.
The former outer cutoff 71/5 lies outside the proved positive Bessel region
at this aperture. Both complete 48-degree masses and infinite tails are
freshly audited. The outer single-band lower bound is negative; it is stored
only as an algebraic intermediate, with no positive single-band claim.
The two-band lower bound is 0.6593030884750124..., and replacing the
separated prime loss with the fresh tenth-power bound gives
0.7982182322149314...>399/500. The logarithmic complement bound remains 9/100.

Finite native positivity, source approximation, partial panel accumulation,
complete residual Gram and corrected whole-domain positivity are distinct
states. Two saved Gram panels do not give a complete Gram or a Schur sign.
The certified whole-domain frontier remains 47/50. No global endpoint
exclusion, retained packet attachment, F4 closure or Lean formalization is
claimed here.
