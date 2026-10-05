# RPB108: first certified actual Schur correction

## Terminology and theorem

An **actual Schur diagonal** is S(e,e)=Q(e)-Q(z_e), with the exact coercive-complement solution z_e, rather than the raw restriction Q(e). **Endpoint-log separation** isolates the explicit logarithmic singularities of the actual polynomial source before bounding its projected tail.

At a=1/2, let E and F be the established 64-dimensional physical Legendre low space and its complement in the logarithmic carrier. For e=1 on [-1/2,1/2], the actual corrected Schur diagonal satisfies

S(e,e) > 194/3125 > 3/50.

This certifies one corrected direction, including the entire uncomputed infinite complement correction. It does not certify the sign of the full 64-dimensional Schur matrix or the full Weil form.

## Decompose the actual source

The previous actual interior source constructor gives

q_1(x)=c(x)+8sinh(1/4)cosh(x/2)
 -(log 2/sqrt 2) 1_(|x|>=log 2-1/2).

Here c(x)=psi(1/4)-log pi+J(x+1/2)+J(1/2-x), and J(d)=atanh(exp(-d/2))+atan(exp(-d/2)). Set H(d)=J(d)+(1/2)log d. Then q_1 is the sum of a constant, the endpoint-log part

L(x)=-(1/2)[log(x+1/2)+log(1/2-x)],

the smooth part h(x)=H(x+1/2)+H(1/2-x)+8sinh(1/4)cosh(x/2), and the prime step part. The constant has no complement projection. All pieces use the same actual source.

## Endpoint-log tail bound

The physical orthonormal basis is v_n(x)=sqrt(2n+1)P_n(2x). For n>=1, direct Legendre integration gives

integral_0^1 log t P_n(2t-1)dt = (-1)^(n+1)/[n(n+1)],
integral_0^1 log(1-t)P_n(2t-1)dt = -1/[n(n+1)].

These follow by integrating the Legendre differential equation against log t or log(1-t); its weighted endpoint term vanishes, and the resulting polynomial boundary integral is exact. Therefore the coefficient of L is zero for odd n and sqrt(2n+1)/[n(n+1)] for even n>=2. Physical polynomial completeness follows from uniform polynomial approximation on the compact interval; no logarithmic or graph density is assumed.

Its squared complement norm is bounded by

sum_(n>=64) (2n+1)/[n^2(n+1)^2]
 =sum_(n>=64)[1/n^2-1/(n+1)^2]=1/64^2.

Thus ||P_F^(physical)L||<=1/64.

## Smooth tail bound

Since J'(d)=-K(d) and K(d)=exp(d/2)/(2sinh d),

H'(d)=[sinh d/d-exp(d/2)]/[2d(sinh d/d)].

For 0<d<=1, exp(d/2)-1<d and sinh d/d-1<d^2. The latter follows by the positive series and sinh 1-1<1. Consequently |H'(d)|<=1, including the continuous endpoint limit. The pole derivative is at most 4sinh(1/4)^2<1. Hence |h'|<=3.

The Legendre differential operator on this physical interval has eigenvalues n(n+1) and derivative energy integral (1/4-x^2)|h'|^2 dx. Integration by parts and Bessel's inequality give

||P_F^(physical)h||^2 <= [integral (1/4-x^2)|h'|^2 dx]/(64*65)
 <=3/[2*64*65] <1/50^2.

This is a tail estimate for a specific smooth physical function, not a full-carrier coercivity assumption.

## Exact prime-step projection

Put r=2log 2-1 and c=log 2/sqrt 2. For the step c 1_(|2x|>=r), its squared physical norm is c^2(1-r). Its coefficient at n=0 is c(1-r), its odd coefficients vanish, and its even coefficients n>=2 are

c [P_(n-1)(r)-P_(n+1)(r)]/sqrt(2n+1).

This follows from the exact antiderivative (P_(n+1)-P_(n-1))/(2n+1). Subtracting the squared first 64 coefficients from the full squared norm gives its exact squared complement norm. The rational log/sqrt enclosures and interval Legendre recurrence enclose this quantity between the exact endpoints recorded in `notes/data/RPB108_CONSTANT_SCHUR_CERTIFICATE_20261005.json`. Its upper endpoint is less than 1/800, hence its norm is less than 1/28. No endpoint quadrature is used.

## Coupling and Schur certificate

The triangle inequality now gives

||P_F^(physical)q_1|| < 1/64+1/50+1/28 < 9/125.

Apply the established exact residual theorem with approximate lift Z=0. The actual complement correction obeys

0<=Q(z_1)<=5||P_F^(physical)q_1||^2 <81/3125.

The prior rational finite matrix certificate proves Q(1)>11/125; its first pivot is precisely this raw diagonal because the constant basis vector is physically normalized at a=1/2. Therefore

S(1,1)=Q(1)-Q(z_1)>11/125-81/3125=194/3125>3/50.

This is the claimed actual corrected sign, independent of the earlier exploratory quadrature. `scripts/certify_native_constant_schur.py` reproduces all rational arithmetic, recomputes the prior finite certificate, and verifies the exact inequalities. The analytic log-tail and derivative arguments supply its stated bounds. Floating pilot signs are not inputs.

## Remaining obstruction

This removes the infinite-complement uncertainty for one actual Schur diagonal. Positive diagonal entries do not imply a positive matrix: mixed entries and the other 63 directions still matter. No scalar conclusion is promoted to the full Schur sign, WD-T10 global contraction, endpoint exclusion or RH. The same-vector corrected source is 1-z_1, but no explicit numerical z_1 is asserted.

The missing fixed-aperture task remains rigorous coupled matrix/residual enclosures for all sources. Endpoint-log separation and exact prime-step projection now provide an alternative to uncertified endpoint quadrature for part of that task. F4 entry and FULL TRANSPORT CLOSED remain open; Lean source and certified checkpoint are unchanged.
