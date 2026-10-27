# Original arch mixed block: shared scalar moments and complete kernel error

Parent: PR #339, source 2e6647dcce1f05e0cbb41051baa5c7b6a94fb8ec.
Canonical manifest inspected: W-ODD-NEG remains OPEN. No governance change.

## New complete error term

Keep the original physical U=JD and W=(I-P_J470)FC, with exact U*W=0.
The inherited physical-shift identity is

    M_arch = - integral_0^L k(s) A(s) ds,
    A(s)=U*C_s W, L=11/5, k(s)=exp(s/2)/sinh(s).

The accepted full physical frame bound gives ||U||,||W|| <= sqrt(101/100),
and C_s is a physical compression of symmetric translations, hence
||A(s)|| <= 101/100. The original small-shift proof supplies A(s)=O(s).
Thus the singular 1/s part below is integrable in these EXACT coordinates.

Put g(s)=s*k(s). This is analytic for |s|<pi, with g(0)=1.
NIST DLMF 4.36.1 gives sinh(z)/z = product_n(1+z^2/(n*pi)^2).
On |z|=3, the product triangle inequality and the same identity at z=3i give

    |sinh(z)/z| >= sin(3)/3,
    |g(z)| <= 3 exp(3/2)/sin(3) < 128.

The strict last bound is checked by exact Taylor inequalities:
sin(3)>7/50 and exp(3/2)<9/2. Radius 3 is below pi; no singularity
is crossed. Source: https://dlmf.nist.gov/4.36.E1 .
Cauchy bounds for the exact Taylor polynomial P_N, N=384, therefore yield

    |g(s)-P_N(s)| <= 128 (s/3)^(N+1)/(1-s/3), 0<=s<=L.

Consequently the COMPLETE original mixed operator kernel replacement obeys

    ||M_arch + integral_0^L P_N(s) A(s)/s ds||
       <= (101/100) * 128 * (11/15)^(N+1) / ((1-11/15)*(N+1))
       < 2^-170.

This holds for all 470 source and 14 feature coefficients together, in JD/W
coordinates. It does not require source Taylor approximations or midpoint
sampling. It is not an entrywise bound multiplied by dimension later.
The builder computes all 385 coefficients by exact formal division using
(sinh(s)/s)*g(s)=exp(s/2). Replay verifies them through the independent
identity ((exp(2s)-1)/(2s))*g(s)=exp(3s/2).

## Shared moments and finite polynomial reduction

For j>=1 define mu_j = integral_0^L k(s)*(s/L)^j ds. All source pairs share
these scalar moments. If P_N(s)=sum c_n s^n, then the retained exact center is

    mu_j^N = sum_(n=0)^N c_n L^n/(j+n),
    |mu_j-mu_j^N| <= 128*(11/15)^(N+1)/((1-11/15)*(N+j+1)).

The artifact retains j=1,...,128. Each value and its individual radius is
replayed with stdlib Fractions. These are scalar moments of the ORIGINAL
kernel, not samples of it. Local build and independent replay take seconds.

For odd polynomials f,g on [-B,B], the physical correlation on [0,2B] is

    A_fg(s) = integral_(-B)^(B-s) g(x) f(x+s) dx.

It is a polynomial of degree at most deg(f)+deg(g)+1. The half from the
symmetric translation and the factor from odd reflection have already
cancelled; there is NO additional factor 2. For exactly orthogonal f,g,
A_fg(0)=0, so if A_fg(L*t)=sum_(j>=1) a_j t^j, the arch mixed entry equals
-sum a_j mu_j, with error <=sum |a_j| radius_j. The utility implements
this finite binomial formula, tests the original B=11/10 orthogonal pair
f=x, g=x^3-3B^2*x/5, its boundary cusp, reversal symmetry, and the vanishing
full constant-kernel integral for odd functions. The 128 moments support
polynomial pairs of degree at most 63. This is a utility scope, NOT a claim
that degree 63 approximates the actual trial frame.

## Cost decision and remaining dependency

No more full-source shift nodes are needed to build a universal scalar
moment table: its cost is independent of 470x14 and of native projection
precision. A finite polynomial correlation then contracts against the same
table. This avoids a proposed many-node matrix quadrature as a prerequisite
for this route; it does NOT prove that the polynomial route is cheaper in
its entirety. Naive high-degree overlap assembly can itself be expensive.

Before a full original matrix run, certify the needed degree and physical /
arch form error for the ACTUAL normalized U and W. The accepted dyadic D
must be regenerated with its fingerprint checked, and the exact real
projection enclosure must be retained. Approximate polynomial functions
will generally lose exact U*W=0: one must explicitly correct their constant
correlation or use the full identity term. Dropping the constant while
integrating a 1/s kernel would be invalid. Kernel approximation error alone
does not bound this source approximation error. Likewise a polynomial
coefficient l1 norm may be large; scalar moment radii must be propagated
through the actual coefficients. These are required dependencies, not
assumed cancellations.

Do not launch a large source-polynomial calculation before that degree and
cost estimate. The actual original arch mixed matrix, full Astar projection,
matched forcing, inverse response and W-ODD-NEG remain UNCOMPUTED / OPEN.
This result certifies one complete kernel-error term and a reusable scalar
integration reduction; it is not a completed quadrature certificate.
Inherited Fourier/domain review, arithmetic CI and analytic proof standing
remain separate. Even/CC27/Weil/RH remain OPEN. Draft/unmerged.
