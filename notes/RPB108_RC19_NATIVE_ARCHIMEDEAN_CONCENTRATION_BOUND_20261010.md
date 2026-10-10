# RPB108 RC19 — native archimedean concentration bound

2026-10-10. Independent route consolidation.
Parent: 05600c92b9198282c354f14b7c8628d58cef8871 (RC18).
Only research/rpb108-route-consolidation is written.

## Result and computational scope

Using the ACTUAL digamma multiplier rather than the generic negative
remainder allowance proves

    A_Q >= (1/10)I_D -(153/10)C_exp(10)

at cap B=11/10, where C_T is RC18's canonical low-frequency concentration
operator. Its spectral head above theta=1/306 has finite rank below
30 million, and its entire original-form complement has floor 1/20.

For that head, an actual head floor >=1/4000 and actual source cross norm
<=1/400 would give a paid Schur reserve >=1/8000.
Neither actual bound is supplied here. No spectral head is instantiated.
Thirty million is a conservative rank upper bound, not an observed rank;
a dense matrix at that bound remains computationally prohibitive.

The native multiplier lowers the analytic concentration rank envelope
from RC18's 12 trillion to 30 million. These are upper-bound envelopes for
different projections and acceptance conditions, not actual rank ratios
or an assertion that the finite positivity problem is solved.

## Native definitions and custody

On the supported logarithmic carrier D_B let i:D_B -> L2(-B,B) be
the physical inclusion, ||i||<=1, and

    w(xi)=log(e+|xi|),
    ||h||_D^2=integral w(xi)|Fourier(i h)(xi)|^2 dxi.

Fourier convention: exp(-2pi i xi x).
The original native form is the Fourier multiplier

    a_arch(xi)=Re psi(1/4+i*pi*xi)-log pi,

plus negative prime translations with coefficients Lambda(n)/sqrt(n)
and the cross-paired pole moments. The bounded canonical operator is
A_Q=I+i^*R_B i; full Q is not a bounded physical L2 operator.

CC27 blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482 at CC119
5df347d3808ac3282864a657b7380e0f54bf4daa supplies the native identity.
RC17 supplies exact pole eigenvalues and coefficient bounds at B=11/10.
The seven active prime powers are 2,3,4,5,7,8,9.

The external special-function input is the Euler series
[NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6), checked 2026-10-10.
All lower-envelope, tail and Schur estimates below are fresh deductions
from that series and the pinned native identity.

## Euler-series lower bounds for the actual multiplier

Put a=1/4 and y>=0. The Euler series gives

    Re psi(a+i y)
      =lim_(N->infinity) [log N -sum_(n=0)^(N-1)
                         (n+a)/((n+a)^2+y^2)].

Here H_N-gamma-log N tends to zero. The elementary integral comparison
for H_N gives gamma<=1.

Subtracting the absolutely convergent real Euler series at y=0 gives

    Re psi(a+i y)-psi(a)
      =sum_(n>=0) y^2/[(n+a)((n+a)^2+y^2)] >=0.

Also psi(a)=-gamma-1/a+sum_(n>=1) a/[n(n+a)] >=-5.
With inherited pi<22/7 and a fresh rational exp(6/5)>22/7,

    a_arch(xi)>=-5-log pi >-31/5                     (1)

for all real xi.

For y>=a define f(t)=(t+a)/((t+a)^2+y^2).
Its maximum on t>=0 is 1/(2y), attained at t=y-a.
It rises from f(0) to that maximum and then decreases to zero, so

    integral_0^infinity |f'(t)|dt=1/y-f(0)<=1/y.

For each integer n, the fundamental theorem of calculus gives

    |f(n)-integral_n^(n+1) f(t)dt|
      <=integral_n^(n+1)|f'(t)|dt.

Summing controls the full sum/integral discrepancy by 1/y.
Since

    integral_0^N f(t)dt
      =(1/2)log[((N+a)^2+y^2)/(a^2+y^2)],

the Euler-series limit implies

    Re psi(a+i y) >=(1/2)log(a^2+y^2)-1/y
                   >=log y-1/y.                    (2)

This is a proved inequality, not an uncontrolled asymptotic expansion.
For x=|xi|>=exp(10), y=pi*x>=a. Using pi>1 in (2),

    a_arch(xi)>=log x-1/(pi*x)>=log x-1/x.           (3)

The elementary pi>1 and inherited pi<22/7 are analytic inputs;
their proofs are not part of the rational validator.

## Full prime and signed pole budget

RC17 gives

    sum c_n <12093/3740+11/30,
    negative pole norm <179/310.

Zero-extended translations are contractions, so their full negative
allowance is twice the coefficient sum. The complete nonarchimedean
part therefore has lower bound -8I in physical L2, since

    2(12093/3740+11/30)+179/310 <8.                   (4)

Both translation orientations and both pole moments are retained.
The positive pole component can be dropped in this LOWER estimate.
It is still retained in the actual source residual and head.

Thus the actual Q obeys

    Q(h,h)>=integral [a_arch(xi)-8]|Fourier(i h)(xi)|^2 dxi.

## A native canonical floor with only low-band subtraction

Let alpha=1/10 and T=exp(10).
For x>=T, log(e+x)<=log x+e/x<log x+3/x.
Equation (3) consequently gives

    a_arch(xi)-8-alpha*w(xi)
      >=(9/10)log x-8-(13/10)/x >0.

Indeed log x>=10 and x>=exp(10)>2 already make the right side
larger than 1-13/20>0.

For x<=T, e+exp(10)<exp(11), using 2<e and e<=exp(10).
Hence w(xi)<11. By (1),

    a_arch(xi)-8-alpha*w(xi)
      >=-31/5-8-11/10=-153/10.

Splitting the Fourier integral at T proves

    Q(h,h)>=(1/10)||h||_D^2
            -(153/10)||Fourier(i h)|_(-T,T)||_2^2.  (5)

Equivalently A_Q>=(1/10)I-(153/10)C_T.
This does not assume original positivity at 1.10.
It is valid first on the inherited smooth core and then on the full
canonical carrier by bounded canonical form continuity.

## Spectral head, whole complement, and rank bound

Use RC18's C_T=J_T^*J_T, where J_T restricts the physical Fourier
transform to (-T,T). Its trace is <=4BT.
Let P be its canonical spectral projection onto eigenvalues >1/306,
and H=I-P. Then

    H C_T H <=(1/306)I_H.

Applying (5) gives the WHOLE original complementary bound

    H A_Q H >= [1/10-(153/10)/306]I_H
              =(1/20)I_H.                          (6)

No sampled high-frequency tail or finite complementary matrix is used.
P is a canonical concentration projection, not a physical polynomial
projection. It differs from RC18's threshold and cutoff.

The trace estimate gives

    rank(P)<=4BT*306=(6732/5)exp(10)<30000000,

using a fresh rational Taylor enclosure exp(10)<22100.
The spectral projection is specified analytically; no actual concentration
eigenvalues, eigenvectors, rank or metric conversion are computed.

## Actual remaining arithmetic gate

Let G=P A_Q P be the actual canonical head and
Z=H A_Q P=H i^*R_B i P the actual canonical source residual.
RC18 defines its complete column-error interface; it applies here only
after replacing its head by this new P and retaining the same carrier.

If actual certified estimates give

    G>=(1/4000)I_P,   ||Z||<=1/400,

then (6) yields

    G-Z^*(H A_Q H)^(-1)Z
      >= [1/4000-20*(1/400)^2]I_P
      =(1/8000)I_P.

The bounded exact Schur factorization then certifies original positivity
on the entire cap. No current result shows that these actual estimates
hold. Positive head and tail blocks alone can still have a negative
coupled direction; the validator includes that control.

The improved tail estimate is unconditional for the stated projection.
The head and cross estimates are conditional and unevaluated.
Existing sources for other heads must not be reused without a rigorous
canonical projection and source-error conversion.

## What this resolves and what remains

The generic -16 remainder estimate concealed the actual archimedean
high-frequency growth and forced RC18's exp(24) cutoff.
Equations (1)--(5) retain that growth directly and give exp(10).
The resulting finite head envelope is much smaller, but still enormous.

This is not a theorem that a practical implementation needs 30 million
modes. The trace estimate may be loose. A feasible implementation needs
a certified smaller head or a tractable representation of this head,
followed by actual head and source-residual bounds.
No new arithmetic cancellation or original head positivity is proved.

## Validation and standing

scripts/validate_rpb108_rc19_native_arch_concentration.py passes 34 exact
rational checks: logarithmic enclosures, nonarch negative budget,
Euler-series variation algebra, real-part increments, high-frequency
reserve, low-band penalty, concentration threshold, whole-tail floor,
rank envelope, conditional Schur reserve and unsafe block control.
The infinite Euler-series, integration, operator and whole-tail proofs
are analytic arguments above; finite checks are not digamma sampling.

No actual finite head or source residual is evaluated. No original
negative vector, new whole aperture positivity, RH/F4 theorem or Lean
closure is claimed. The existing 1.06 certificate and prior restricted
results remain intact. Other branches and historical files are unchanged.
