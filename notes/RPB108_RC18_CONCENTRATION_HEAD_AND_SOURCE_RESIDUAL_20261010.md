# RPB108 RC18 — concentration head and actual source-residual gate

2026-10-10. Independent route consolidation.
Parent: ea6d50805df507e0f5a2507514c5450870ca85a1 (RC17).
Only research/rpb108-route-consolidation is written.

## Result and scope

A finite head defined by low-frequency concentration gives a certified
WHOLE complementary original-form floor of 1/6 at B=11/10.
The frequency cutoff is exp(24), rather than RC17's exp(16000000).
The improvement requires a separate bound on the ACTUAL source residual;
it does not follow by substituting the generic remainder norm.

For this precisely defined head, positivity follows if BOTH

    actual canonical head floor >=1/4000,
    actual canonical source cross norm <=1/200.

The Schur reserve is then at least 1/10000.
Neither actual head nor source cross norm is certified in this step.
The concentration head is analytically finite but is not instantiated.
Its crude rank upper bound is below 12 trillion, still far beyond a
practical full matrix computation. This is a complete tail theorem and
a source-specific finite certificate interface, not positivity at 1.10.

## Carrier and native input

Let D_B be the supported logarithmic carrier with

    ||h||_D^2 = integral log(e+|xi|)|Fourier(h)(xi)|^2 dxi,

Fourier convention exp(-2pi i xi x), and inclusion
i:D_B -> L2(-B,B), ||i||<=1. Physical vectors are extended by zero.
The original canonical bounded form operator is

    A_Q=I+i^*R_B i.

The unbounded logarithmic principal part of physical Q is represented
by I in D_B; no bounded physical operator for full Q is assumed.
RC17 supplies -16I<=R_B<=21I and ||R_B||<=21 at B=11/10, including
all archimedean, prime and signed pole contributions.
RC17 pins these to CC27/CC37 at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.
This step concerns the original form, not the phase-average reference.

## Low-frequency concentration operator

For T>0 define the band restriction map

    J_T:D_B -> L2(-T,T),   J_T h=Fourier(i h)|_(-T,T),

and its positive canonical concentration operator

    C_T=J_T^*J_T.

The corresponding physical map from L2(-B,B) to L2(-T,T)
has integral kernel exp(-2pi i xi x), squared Hilbert--Schmidt norm
4BT. Composing it with the contraction i gives

    trace(C_T)=||J_T||_HS^2 <=4BT.

For completeness, for any canonical orthonormal basis (p_j), the adjoint
image of the physical kernel vector at each xi has squared norm at most
its physical norm squared, 2B. Integrating and applying the nonnegative
sum/integral identity gives the stated trace bound.
Thus C_T is positive trace class. This is a finite-band trace estimate;
it does NOT claim that the full physical inclusion is Hilbert--Schmidt.

Fix a threshold theta>0. Let P be the canonical spectral projection of
C_T onto eigenvalues GREATER than theta, and H=I-P.
Then P has finite rank, with

    rank(P) <=trace(C_T)/theta <=4BT/theta,
    H C_T H <=theta I_H.

Eigenvalues equal to theta may remain in H. P is defined using the
D_B metric, not a physical Fourier or polynomial projection.
The existence and spectral inequalities specify P analytically.
No numerical eigenspace or projection error certificate is supplied.

## Entire physical tail and original-form lower bound

For h in range(H), Plancherel and the logarithmic weight give

    ||i h||_2^2
      =||J_T h||_2^2 + integral_|xi|>T |Fourier(i h)(xi)|^2 dxi
      <= [theta+1/log(e+T)]||h||_D^2.

This estimates EVERY vector in the complement; it is not a sampled tail.
With T=exp(ell), log(e+T)>ell. Hence

    H A_Q H >= [1-16(theta+1/ell)] I_H.

The estimate uses RC17's negative remainder bound, so the full signed
native form remains attached.

Choose

    ell=24, T=exp(24), theta=1/96.

Then theta+1/ell=5/96 and

    ||i H||^2 <=5/96,
    D:=H A_Q H >=(1/6)I_H.

Also rank(P)<(2112/5)exp(24)<12*10^12.
A fresh exact exponential enclosure exp(24)<27000000000 proves the last
rational bound. This is an upper bound, not the actual rank or a claim
that this many features are necessary.

## Actual source residual and finite Schur gate

Let the actual head be G=P A_Q P on range(P).
The cross block is

    Z=H A_Q P=H i^*R_B i P,

since H I P=0 in the canonical metric.
Call Z the canonical source residual: it is the part of the full native
remainder response to head vectors lying outside the chosen head.
It includes the signed poles as well as every active prime and the
archimedean remainder. It is neither an exterior physical tail nor the
shell covariance from RC3.

Suppose actual certified bounds give

    G>=m I_P,    ||Z||<=beta.

Since D>=I_H/6, the actual finite Schur complement satisfies

    G-Z^*D^(-1)Z >=(m-6beta^2)I_P.

At m=1/4000 and beta=1/200,

    6beta^2=3/20000,
    m-6beta^2=1/10000>0.

The bounded block factorization then proves strict positivity on the
whole canonical carrier. The entire infinite complement has already
been paid by the analytic tail estimate; the head and residual still
require actual arithmetic certification.

To make the residual obligation concrete, take a canonical orthonormal
head basis p_1,...,p_r and source columns

    sigma_j=i^*R_B i p_j.

Then

    ||Z||^2 <=sum_j ||H sigma_j||_D^2.

For any rigorously constructed z_j in range(P), orthogonal best
approximation implies

    ||H sigma_j||_D <=||sigma_j-z_j||_D.

Thus certified column errors epsilon_j with sum epsilon_j^2<=1/40000
are sufficient for beta<=1/200. This is a sufficient
Hilbert--Schmidt residual budget; correlated operator estimates may be
much sharper. The source columns and projection must correspond to THIS
canonical concentration head. Existing source data for a different
physical basis cannot be inserted without a certified metric conversion.

## Why this is a different obligation, not a free improvement

Using only ||R_B||<=21 and ||iH||^2<=5/96 gives the generic estimate

    ||Z||^2 <=441*(5/96).

It fails the displayed Schur gate by a large margin. The new small beta
must come from actual source structure, not the norm envelope.
A positive finite head and a positive tail alone also do not suffice:
a 2-by-2 block with head 1/4000, tail 1/6 and cross entry 1/100 has
negative determinant. The validator includes this control.

RC17 demanded small uniform physical inclusion error to pay the cross
block by a worst-case norm estimate. This step permits a coarse inclusion
tail and instead asks for small source leakage from the actual head.
Its cutoff exp(24) is therefore not an unconditional substitute for
RC17's exp(16000000); the residual hypothesis is additional and unproved.

The analytic rank bound remains enormous, and computing the concentration
eigenspace, head and sources is not presently feasible by that bound.
Possible practical progress requires sharper concentration rank estimates,
a smaller certified substitute head that retains the tail bound, or
source-specific spectral compression. No such construction is supplied
here. This step advances the whole-tail interface, not the arithmetic
positivity or computational feasibility frontier.

## Validation and standing

scripts/validate_rpb108_rc18_concentration_source_screen.py passes 15 exact
rational checks: concentration threshold, full tail floor, conditional
Schur reserve, finite-rank envelope, exponential enclosure, failure of
the generic cross estimate, column residual budgets, and an unsafe
blockwise-positivity control. The trace, spectral and whole-complement
arguments are analytic proofs above.

No concentration eigenspace, actual finite head or source residual is
computed. No original negative vector, new whole aperture positivity,
RH/F4 theorem or Lean closure is claimed. The existing 1.06 certificate
and restricted results remain intact. Other branches and historical
files are unchanged.
