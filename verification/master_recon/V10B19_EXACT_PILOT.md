# V10B19 — exact polynomial/logarithm action pilot

**Status: exact rational arithmetic PASS; conditional on analytical attachment.**
No native Lean adoption, no global positivity conclusion.

The V10B18 bank was frozen as new dyadic coefficients with denominator 2^48,
16 supported polynomial trials of degree <=159 and 16 retained-load subtractions.
The full replay archive (including coefficients, exact polynomial/log moment generator,
independent congruence checker and analytic derivation) has SHA256
38059a234a781bbe5d9d15513520c6aa1418ebb64f8b8ee6cba6e518b4d805d7.
The parent manifest authenticated 15/15 files. Exact replay from integer coefficients
reproduced exact_result.json hash afb474cb569b08dff1782e5a19430b0436a3a77bfcb7b2211547017e7a460903.
See v10b19_terminal_congruence.py for the independent terminal matrix replay.

## Literal physical action to attach

At t=1/4, L=1/2, z=(x+t)/L, p supported by zero extension, use the digamma
integral for Re(s)>0 and translations tau_r. The Archimedean action is

D f = (-gamma-log pi) f + integral_0^infty
  [2 exp(-2r) f-exp(-r/2)(tau_r f+tau_-r f)]/(1-exp(-2r)) dr.

For supported polynomials, L2 translation differences are O(sqrt(r)) near
zero, permitting a Bochner limit; at infinity the integrand decays
exponentially. Fourier transformation gives Re psi(1/4-i pi u)-log pi.
Integration by parts also gives Fourier decay O(1/|u|), so the supported
polynomial lies in the logarithmic carrier. Both attachments need Lean.

Split k(r)=exp(r/2)/(2 sinh r)=1/(2r)+h(r). The constant integrals on
(0,L) and (L,infty) cancel to -log(2L)=0. With T(z^j)=H_j z^j,
q(z)=p(1-z), Kp(z)=integral_0^z L h(Ls)p(z-s) ds, the restricted action is

A p(z)=(-gamma-log pi)p(z)-p(z)(log z+log(1-z))/2
       +(Tp(z)+Tq(1-z))/2-Kp(z)-Kq(1-z)
       + exp(x/2) integral exp(-y/2)f(y)dy
       + exp(-x/2) integral exp(y/2)f(y)dy.

The prime term vanishes at this radius. T follows from a finite geometric sum;
K uses beta integrals j!k!/(j+k+1)!.

## Enclosures

On |r|=1, |sinh(r)/r-1|<1/4 and |exp(r/2)-1|<3/4 imply |h(r)|<1.
Cauchy estimates yield a degree-28 kernel remainder <=2^-28 on [0,1/2].
Pi uses Machin brackets; logs use atanh-series bounds; gamma uses
H_4096-log(4097) <= gamma <= H_4096-log(4096).
The normalized deflated pole load P15 plus higher odd Legendre terms
has coefficient ratio <=1/(64*(2j+1)*(2j+3)) < 1/65000 for j>=15,
from the positive spherical modified Bessel series. Degree-33 truncation
and 16-term inner series give uniform error <10^-25. The exact deflated
load is the retained subtraction in the receiver. Coverage follows from
strict row diagonal dominance after the full high-pole-load reserve.

For n=k+1 and l=log z+log(1-z), the exact moments of z^k times 1,l,l^2 are
1/n, -1/n^2-H_n/n, and
2/n^3+(H_n^2+H_n^(2))/n+2*(H_n/n^2-(zeta(2)-H_n^(2))/n).
These require beta derivative or log series attachments. Pi midpoint error
in the residual Gram has a separate 10^-16 spectral reserve.

The exact replay checks column physical norms <=1 and ||V||<=4; action
error <=0.000488300; residual synthesis norm <1/50. Hence the energy
reserve is 4e, residual Gram reserve 2e/50+e^2+10^-16. With c=1/8 and
log 2>2/3 the inverse-response factor is <12. Entrywise downward rounding
is NOT a PSD bound: the full spectral rounding reserve 16/2^48 is used.

Results:
- exact constraint dominance margin >1.0675 (conditional pole-load identity)
- combined error reserve <0.002190442
- 16/16 exact positive LDL pivots after reserves and 1/100 I
- minimum pivot >0.04
- conditional lower margin 1/100

The analytic formula and exact endpoint moments still need native attachment
to the literal arithmetic form. The V10B17 tail and V10B18 receiving
theorems remain subject to native audit. No new Lean declarations or runner
were activated for this arithmetic-only stage. Arithmetic ADOPT 0.
