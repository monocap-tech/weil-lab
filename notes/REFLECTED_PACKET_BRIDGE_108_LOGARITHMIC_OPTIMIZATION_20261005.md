# RPB108: explicit optimization of the actual logarithmic bootstrap

Base: cc9302665923e060a5d5b56c032dd5990727eabf.
Definitions: docs/TERMINOLOGY_RPB108_LOGARITHMIC_OPTIMIZATION.md.

## Result

For every actual full mixed weak-null vector h at fixed a>0, the preceding logarithmic bootstrap gives an explicit optimized Gaussian estimate. Put

    t=log log(R/(4*pi)),
    Z_a=3266+C0+35 S_a+2b_a+v_a,
    b_a=4a sqrt(2a)exp(a),
    v_a=(4+2a)sqrt(2a)exp(a).

Here C0>=0 is the existing global envelope constant |m0-w|<=C0 and S_a is the exact frozen finite-prime translation budget. If

    t>=max(128,4 log Z_a),

then

    M_R <= [exp(-t^2/[16 log(t+2)])+exp(-R/4)] ||h||_2^2.

This is an asymptotic quantitative consequence of full mixed nullity. The threshold is very large; it does not improve the numerical positivity aperture. No nonzero null vector or endpoint is asserted to exist.

## Compressing the order constants

Use the definitions U_k, A_k, D_k and F_(a,k) at the base commit. Their universal formulas imply

    U_k<=34*2^k*(k+1)!,
    A_k<=35*2^k*(k+1)!,
    D_k<=3264*2^k*(k+1)!.

For the first bound, rewrite the sum as

    sum_(j=0)^k binom(k,j)2^j(j+1)!
      =2^k k! sum_(l=0)^k (k-l+1)/(2^l l!)
      <=2^k(k+1)! exp(1/2)<2^(k+1)(k+1)!.

Inserting its factor 16 in U_k, and bounding the remaining 2^(k+1) by 2*2^k(k+1)!, gives 34. The A_k estimate follows from 1+k U_(k-1) for k>=1 and A_0=1. The D_k estimate is 96 times the U_k estimate. The inequalities exp(1)<3 and exp(1/2)<2 follow from the elementary factorial series bound; no numerical asymptotic is being assumed.

The pole moment sum has a similar exact rewrite:

    sum_(j=0)^(2k) binom(2k,j)2^(2k-j)j!
      =(2k)! sum_(l=0)^(2k)2^l/l!<9(2k)!.

The central binomial inequality (2k)!<=4^k(k!)^2 then gives

    F_(a,k)^2<=4^k(k!)^2 [2b_a^2+v_a^2/2],
    F_(a,k)<=(2b_a+v_a)2^k k!.

The square root inequality in the last step holds since b_a,v_a>=0.

## A single all-order envelope

Let L_(a,k) be the previously derived recursive bound for ||h||_(X_k)/||h||_2. Define B_0=1 and

    B_(k+1)=Z_a 2^k(k+1)! B_k.

Since Z_a>=2, B_k>=1. The preceding coefficient and pole estimates, together with the original recurrence, prove by induction L_(a,k)<=B_k. Explicitly,

    B_k=Z_a^k 2^(k(k-1)/2) product_(j=1)^k j!.

For k>=1, j!<=k^j gives

    log B_k <= k log Z_a + k^2 log(2k).

This is deliberately a ceiling, not a sharp asymptotic. It accounts for the inhomogeneous pole term and all prime contributions; none is discarded to improve the rate.

## Lawful order choice

The prior frequency split yields, with ell_R=log(R/(4*pi)),

    M_R/||h||_2^2 <= B_k^2/ell_R^(2k)+exp(-R/4).

Choose the integer order

    k=floor(t/[8 log(t+2)]),   t=log ell_R.

For t>=128, log(t+2)<=t/16: at t=128 use log(130)<8, and its difference has positive derivative thereafter. Hence t/[8 log(t+2)]>=2 and

    t/[16 log(t+2)]<=k<=t/[8 log(t+2)].

Also 2k<=t+2, so log(2k)<=log(t+2). If t>=4 log Z_a, these inequalities imply

    log(B_k^2/ell_R^(2k))
       <=2k log Z_a+2k^2 log(2k)-2kt
       <=kt/2+kt/4-2kt
       <=-kt
       <=-t^2/[16 log(t+2)].

This proves the stated bound with no interchange of an infinite sum and a Gaussian limit. The all-finite-order theorem supplies the particular integer k chosen for each R. The threshold condition is essential; choosing a growing order without paying for the constants would be invalid.

## Rate meaning and remaining work

For every fixed N, t^2/log(t+2) eventually exceeds N t, recovering every inverse logarithmic power rate. But the negative exponent is o(log R), so the displayed envelope itself is weaker than every fixed inverse power R^(-delta), delta>0. It is much weaker than exp(-cR). This compares the established bounds; it does not prove a lower bound for the actual Gaussian mass, nor rule out better decay from additional information.

Thus optimization of the published constant hierarchy does not provide the exponential signed boundary estimate, endpoint exclusion or F4 entry. The first-contact and retained selected-witness attachment problems are unchanged. Stronger control must come from information beyond this bound, such as a sharper weak-null estimate or an independently valid endpoint argument. No same-vector null extension is presumed.

## Validation and standing

The exact integer/rational certificate audits the factorial ceilings at orders 0 through 64. It independently constructs the product envelope by recurrence and closed product for a stated test budget. Rational logarithm intervals validate the floor and signed exponent at four t values under the threshold conditions. A negative control with an oversized budget violating t>=4 log Z is rejected. These tests check constants and order selection; the universal induction and asymptotic proof above remain analytic, not mechanically or Lean checked.

The certificate reproduced byte for byte. Numerical positivity frontier remains 81/100. Global endpoint exclusion, retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms, CI and historical notes unchanged.
