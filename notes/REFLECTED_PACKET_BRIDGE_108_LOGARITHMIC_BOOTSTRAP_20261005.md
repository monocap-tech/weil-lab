# RPB108: every finite logarithmic order from actual full weak-nullity

Base: a7d14ef13f2b83ddfbd21dcc32939a84202318f4.
Definitions: docs/TERMINOLOGY_RPB108_LOGARITHMIC_BOOTSTRAP.md.

## Derived result

Fix a>0. Every actual full mixed weak-null vector h in D_a belongs, after zero extension, to X_k for every integer k>=0, where

    ||h||_(X_k)^2 = integral w(xi)^(2k)|Fourier(h)(xi)|^2 dxi,
    w(xi)=log(exp(1)+abs(xi)).

These regularity properties are conclusions of the null equation, not premises. Constants are uniform on the weak-null space for fixed a. No positivity, H1, boundary trace, enlarged vanishing interval or nonzero null existence is assumed. For its moving Gaussian mass, for every N>0,

    M_R = O_a,N((log R)^(-N)) ||h||_2^2.

The constants depend on N. This is not exponential decay in R, does not supply the strict-gap F4 entry, and does not exclude an endpoint.

## Actual source equation and the initial domain

Let P=P_a be multiplication by 1_[-a,a]. Separate the actual frozen multiplier as m_a=m0-t_a, where

    m0(xi)=Re psi(1/4+i*pi*xi)-log(pi),
    T_a h=sum_(log n<=2a) Lambda(n)/sqrt(n)
                 [h(. -log n)+h(. +log n)].

The frozen set includes threshold equalities. T_a has norm at most S_a=2 sum Lambda(n)/sqrt(n) on every X_k, since each translation is a Fourier phase. Let p_h(x)=M_-(h)exp(x/2)+M_+(h)exp(-x/2).

The preceding actual boundary regularity theorem has already derived m_a Fourier(h) in L2 without a multiplier-domain assumption. Since T_a is bounded on L2, m0 Fourier(h) is also in L2. Full mixed weak-nullity therefore yields the legitimate L2 identity

    P m0(D)h = P T_a h - P p_h,   Ph=h.

It is the full mixed equation that gives this identity; zero diagonal in an indefinite form or a selected-only retained record does not suffice. We retain the existing finite global envelope |m0-w|<=C0.

## Explicit derivative bound for the actual quarter-line multiplier

The trigamma series psi'(z)=sum_(n>=0)(n+z)^(-2) is NIST DLMF 5.15.1: https://dlmf.nist.gov/5.15.E1 . It gives

    |m0'(x)|<=pi sum_(n>=0) 1/[(n+1/4)^2+pi^2 x^2].

For 0<=x<=1 the sum is at most 16+sum_(n>=1) n^(-2)<=18, using the integral test. With pi<4 this is at most 72. For x>=1, retain the n=0 bound 1/(pi^2 x^2), and bound the decreasing n>=1 tail by integral_0^infinity dt/(t^2+pi^2 x^2)=1/(2x). With 3<pi<4 this gives at most (7/3)/x<3/x. Thus on the whole real line

    |m0'(x)|<=144/(1+|x|).

The multiplier is even. Writing r=1+|xi|, t=1+|eta|, integration on positive magnitudes gives

    |m0(xi)-m0(eta)|<=144 |log(r/t)|.

This also covers opposite frequency signs; when their magnitudes agree the difference is zero.

## Weighted Schur estimate, without a support gap

The Fourier kernel of P is sin(2*pi*a*(xi-eta))/(pi*(xi-eta)). Define

    J_k = integral_0^infinity |log z|/(|1-z|sqrt(z))
                                (1+|log z|)^k dz.

It is finite for every integer k>=0. Substitution z=exp(v) gives

    J_k=integral_R |v|/[2 sinh(|v|/2)] (1+|v|)^k dv.

On |v|<=1 the first factor is at most one. On |v|>=1 it is at most 2|v|exp(-|v|/2), since exp(1)>2. Integrating the latter majorant over the larger half-line [0,infinity) gives the explicit integer ceiling

    J_k <= U_k,
    U_k=2^(k+1)+4 sum_(j=0)^k binom(k,j) 2^(j+2)(j+1)!.

Here integral_0^infinity v^(j+1)exp(-v/2)dv=2^(j+2)(j+1)!, proved by integration by parts. This is a universal bound, not sampled quadrature.

The weight w, viewed as log(exp(1)-1+r), has derivative at most one with respect to log r and is at least one. Consequently

    |w(xi)-w(eta)|<=|log(r/t)|,
    w(xi)/w(eta)<=1+|log(r/t)|,

and the reciprocal ratio satisfies the same bound.

The conjugated commutator [m0(D),P] has absolute kernel bounded by

    48 |log(r/t)|/|r-t| (1+|log(r/t)|)^k,

using pi>3 and |xi-eta|>=||xi|-|eta||. Apply weighted Schur with weight (1+|xi|)^(-1/2). Splitting the eta integral into its two signs, replacing each magnitude variable t>=1 by t>0, and putting t=r z bounds each Schur integral by 96 J_k. The column integral has the identical bound because the reciprocal w ratio obeys the same inequality. Hence

    ||[m0(D),P]||_(X_k -> X_k) <= D_k=96 U_k.

The apparent 0/0 at equal magnitudes is interpreted by its continuous limit, or ignored on a measure-zero set. The numerator cancels the diagonal singularity. Kernel domination and weighted Cauchy-Schwarz justify the estimate.

## The support indicator itself preserves every finite logarithmic order

This fact must be proved rather than presumed. On Fourier test functions,

    w(D)^k P w(D)^(-k) = P + [w(D)^k,P] w(D)^(-k).

For k>=1, the elementary power difference inequality gives

    |w(xi)^k-w(eta)^k|/w(eta)^k
       <= k |log(r/t)| (1+|log(r/t)|)^(k-1).

The same Schur calculation bounds the additional term by (2k/pi)J_(k-1)<=k U_(k-1). Since P is an orthogonal projection on physical L2,

    ||P||_(X_k -> X_k)<=A_k=1+k U_(k-1), k>=1;
    A_0=1.

Approximation by Fourier test functions proves these operator identities and bounded extensions on X_k. The constants are uniform in a; dependence on a enters the prime and pole terms below.

## Pole term at every logarithmic order

Set H=||h||_2. Cauchy-Schwarz gives |M_pm(h)|<=sqrt(2a)exp(a/2)H. On [-a,a], |p_h|<=2sqrt(2a)exp(a)H and |p_h'|<=sqrt(2a)exp(a)H. The zero extension Pp_h therefore has

    ||Pp_h||_1<=b_a H, b_a=4a sqrt(2a)exp(a),
    total variation(Pp_h)<=v_a H,
    v_a=(4+2a)sqrt(2a)exp(a).

Its Fourier transform is bounded by min(b_a, v_a/(2*pi*|xi|))H, by integration by parts including the two jumps. Using w<2 on |xi|<=1 and w<=2+log|xi| on |xi|>=1 gives

    ||Pp_h||_(X_k)<=F_(a,k) H,
    F_(a,k)^2=2*2^(2k)b_a^2
       +(v_a^2/18) sum_(j=0)^(2k) binom(2k,j)2^(2k-j)j!.

Only this smooth pole profile has endpoint values in the proof; no trace of h is taken.

## Bootstrap using the full mixed equation

For Ph=h the commutator identity and the L2 interior equation give, as distributions,

    m0(D)h = P T_a h - Pp_h + [m0(D),P]h.

Suppose h belongs to X_k. All three terms on the right then belong to X_k by the proved bounds. Thus m0 Fourier(h) belongs to weighted L2 with weight w^(2k). The global envelope w<=|m0|+C0 implies h belongs to X_(k+1), with

    ||h||_(X_(k+1))
       <=(C0+A_k S_a+D_k)||h||_(X_k)+F_(a,k)H.

The distribution identity is rigorous even before this next domain conclusion: h in X_k makes m0(D)h belong to X_(k-1) for k>=1; P is bounded there, and approximation gives the commutator identity there. For k=0 the preceding boundary regularity theorem supplies the initial L2 multiplier domain. No circular domain premise is introduced.

Start L_(a,0)=1 and recursively set

    L_(a,k+1)=(C0+A_k S_a+D_k)L_(a,k)+F_(a,k).

Induction proves ||h||_(X_k)<=L_(a,k)H for every finite k. This is a quantitative analytic recurrence, not an assertion of uniform control as k tends to infinity.

## Gaussian consequence and the remaining gap

Keep the actual beta_R=exp(-(2*pi*xi-R)^2/R). For R>4*pi split frequencies at |2*pi*xi-R|=R/2. On the central band w>=log(R/(4*pi)); off it beta_R<=exp(-R/4). Therefore for every integer k>=0,

    M_R <= [L_(a,k)^2/(log(R/(4*pi)))^(2k)
             +exp(-R/4)] H^2.

Given N choose a fixed k with 2k>=N. This proves every inverse logarithmic power rate. Unlike the preceding physical-norm boundary concentration vectors, these vectors satisfy the actual full mixed null equation; it is that equation that permits indefinite repetition of the regularity step.

All finite logarithmic moments do not imply a positive Sobolev exponent or exponential Fourier decay. The constants grow with k; no optimization in k, quasianalyticity, exponential signed Gaussian upper bound or null exclusion follows from the estimates established here. The earlier boundary scaling obstruction remains valid for arbitrary carrier vectors. This theorem does not attach an abstract retained selected witness to an actual full weak-null vector.

## Validation and standing

The reproducible integer certificate audits U_k, A_k, D_k and pole moment factorials for orders 0 through 12, the derivative budget constants, and a rejected control that drops the Schur tail. It validates constants and recurrences; the infinite-order induction, Fourier operator identities and Schur proof are analytic and are not mechanically or Lean verified. The trigamma series input was checked against the primary NIST DLMF source above.

Numerical aperture frontier: 81/100. Global endpoint exclusion, retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms, CI and historical notes unchanged.
