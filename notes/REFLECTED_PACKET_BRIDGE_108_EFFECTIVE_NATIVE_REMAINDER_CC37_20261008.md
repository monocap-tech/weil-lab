# RPB108 CC37: effective full native remainder norm at the certified cap

Date: 2026-10-08 UTC. Parent: 76adf52044de54a6991080b4bb40f9e53935a9ce.
Definitions: [effective native remainder](../docs/TERMINOLOGY_RPB108_EFFECTIVE_NATIVE_REMAINDER.md).
Result: |r_arch(xi)|<8 on the entire real line, and ||R_B||<20 for
B<=21/20. These are deliberately conservative rigorous envelopes.

## Global archimedean constant

Primary identity: NIST DLMF 5.9.13,
https://dlmf.nist.gov/5.9.E13 . For Re z>0,

    psi(z)-log z=-int_0^infinity k(u) exp(-uz) du,
    k(u)=1/(1-exp(-u))-1/u.

The elementary inequalities 1-exp(-u)<=u and exp(u)-1>=u imply
0<=k(u)<=1 for u>0. Therefore on Re z=1/4,

    |psi(z)-log z|<=int_0^infinity exp(-u/4)du=4.        (1)

Put x=|xi|, b=1/(4*pi). The difference of the two real logarithms is

    log|1/4+i*pi*xi|-log pi-log(e+x)
       =log(sqrt(x^2+b^2)/(e+x)).                      (2)

The ratio is at most one. Cauchy-Schwarz gives

    (e+x)^2<=(e^2+b^2)(1+x^2/b^2),
    sqrt(x^2+b^2)/(e+x)>=b/sqrt(e^2+b^2)
                               >1/(4*pi*e+1).

Using pi<22/7, e<3 and e>8/3, we have

    4*pi*e+1<271/7<(8/3)^4<e^4.

Thus the absolute value of (2) is less than four. Combining with
(1) proves the uniform rigorous bound |r_arch(xi)|<8, including low
frequency and both infinite tails. No floating sample or asymptotic
cutoff supplies this bound. It is not a claimed optimal supremum.

## Complete cap arithmetic

For B<=21/20, the exact rational exponential enclosure below proves
exp(21/20)<3, hence exp(2B)<9. Every possible active prime power is
among 2,3,4,5,7,8. Bounding all six is safe even when a smaller cap
has not yet activated some of them. Lambda(6)=0; none is omitted.

Use the strict rational bounds

    log2<7/10, log3<11/10, log5<81/50, log7<39/20,
    sqrt2>7/5, sqrt3>17/10, sqrt5>11/5,
    sqrt7>13/5, sqrt8>14/5, sqrt4=2.

The sum of their coefficient upper bounds is

    S= (7/10)/(7/5)+(11/10)/(17/10)+(7/10)/2
       +(81/50)/(11/5)+(39/20)/(13/5)+(7/10)/(14/5)
      =12093/3740.

Also exp B<3 implies exp(-B)>1/3 and
4 sinh B=2(exp B-exp(-B))<16/3. CC33's full native bound therefore
becomes

    ||R_B|| < 8+2S+16/3 =111079/5610 <20.              (3)

The factor two retains both prime translations, and the pole bound
retains both cross terms without changing their signs in the form.
Only absolute operator norms are estimated here; the actual signed
form and complete positive inverse remain those of CC33--CC36.

All transcendental enclosures used for the cap coefficients are
certified by rational exponential series. For x>=0 and N=20,
the partial sum is a lower bound for exp x. If x/(N+2)<1, an upper
bound is that sum plus the first omitted term divided by
1-x/(N+2). Successive remaining terms have ratio at most x/(N+2).
This certifies exp(21/20)<3 and exp(log-bound)>2,3,5,7, respectively.
The square-root bounds are checked by exact rational squaring.
The classical pi<22/7 is used as an analytic input, not re-proved
by the finite validator.

## What becomes effective, and what does not

CC34 now yields on this cap

    ||h||_2^2 >= (1/U_B^2-delta)/20

for a normalized critical lift with delta<1/U_B^2. The unknown source
observability constant U_B is still retained. No number is assigned
to an actual source defect or eigenvector.

IP7's finite-cap native sufficient Schur gate may use r_B=20:

    eta<1/20 and lambda_min(E Q_B E)>400eta/(1-20eta).

This substitution supplies one actual arithmetic constant that IP7
left unevaluated. It does not compute its finite projection, physical
tail eta or native finite matrix, and does not make the gate pass.
Larger caps still admit the general effective bound
8+2 sum_(log n<=2B)Lambda(n)/sqrt(n)+4sinh B; no uniform-in-B
bound is claimed. Absolute estimates do not provide CC35's missing
transverse or longitudinal defect suppression.

The validator adds 13 exact rational enclosure checks and replays
CC36's 25,972, total25,985. The digamma inequality is an analytic
deduction from the primary integral, not finite covariance data or Lean.

Original positivity remains certified through21/20, even0/odd0,
physical margin1/(3*10^63). RH/F4, original outward suppression,
retained attachment, reusable continuation and Lean closure remain open.
All concurrent handoffs are preserved; other fronts remain paused.
