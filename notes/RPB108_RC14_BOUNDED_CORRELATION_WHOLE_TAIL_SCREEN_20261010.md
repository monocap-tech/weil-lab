# RPB108 RC14 — bounded correlation operator and whole-tail screen

2026-10-10. Independent route consolidation.
Parent: 43e0001e16467227f1377120840478ba7bec3bc2 (RC13).
Only research/rpb108-route-consolidation is written.

## Result and exact standing

RC13's missing-correlation correction is a bounded self-adjoint operator
on physical L2 at every finite cap. An explicit cap/mask norm allowance is
proved below. The positive phase-average form then supplies a lawful
canonical reference metric for a compact self-adjoint correlation screen.

The remaining relative-gluing target is EXACTLY that this screen stay above
-1. It is not automatically weaker than whole positivity. A finite head can
certify it only with the complete high-space and cross-block bounds stated
below. No actual correlation spectrum or whole tail is certified in RC14.

This consolidates a concrete certification interface and identifies what
arithmetic work it still requires. It does not infer a global breakthrough
from the existence of a positive reference form.

## Physical correction and explicit norm allowance

Use RC13's nonnegative real smooth periodic mask g, period L=log9,
normalized autocorrelation a(d), and Delta(d)=1-a(d). Put

    D=(integral_0^L |g'|^2)/(integral_0^L |g|^2),
    0<=Delta(d)<=1,
    Delta(d)<=D d^2/2.

Let Q be the full native form, F its mass-preserving phase average, and
E=Q-F. Their native attachment is pinned to
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.

On cap (-B,B), the continuous correction kernel is

    [2cosh(d/2)-j(|d|)]Delta(d),
    j(r)=exp(-r/2)/(1-exp(-2r)),

and the correction atoms are -c_n Delta(log n) at both shift orientations,
c_n=Lambda(n)/sqrt(n), log n<=2B. The local archimedean renormalization
cancels. This includes the signed poles, not an archimedean-only correction.

For 0<r<=2B,

    j(r)<=1+1/(2r),
    |2cosh(r/2)-j(r)|<=2exp(B)+1+1/(2r).

The first inequality follows from exp(2r)>=1+2r and exp(-r/2)<=1.
Given any split scale 0<r_0<=2B, the continuous kernel has L1 norm at most

    4B(2exp(B)+1)+D r_0^2/4+log(2B/r_0).

Indeed the bounded kernel part uses Delta<=1, while the singular integral
is bounded by

    integral_0^(2B) Delta(r)/r dr
      <= D r_0^2/4+log(2B/r_0).

Young's inequality for the zero-extended physical function, or the elementary
Schur kernel bound, gives the same physical operator norm allowance.
Each compressed paired translation has norm at most 2. Therefore

    ||T_E||<=C_E,
    C_E =
      4B(2exp(B)+1)+D r_0^2/4+log(2B/r_0)
      +2 sum_{log n<=2B} c_n Delta(log n).             (1)

Replacing Delta by one in the last finite sum gives a coarser fully paid
allowance. The kernel is integrable at zero, and the finite paired shifts
are bounded; hence E(h,f)=<h,T_E f>_L2 with T_E bounded self-adjoint.
The physical atom operator is not declared compact.

At the certified anchor B=53/50, take r_0=1/81000.
The fresh bounds exp(B)<3 and exp(13)>2B/r_0, together with RC5's inherited
prime sum upper 12093/3740, yield the conditional explicit allowance

    C_E <= 459523/9350 + D r_0^2/4.                   (2)

D is the derivative ratio of the actual chosen mask. It has not been
numerically certified for a newly constructed explicit mask in this step.
The symbolic finite bound suffices for the operator and metric arguments.

## Canonical coordinates and a genuinely positive reference metric

Let D_B be the inherited canonical logarithmic Hilbert carrier and
i_B:D_B -> L2(-B,B) its physical inclusion. The existing attachment gives

    Q(h)=||h||_D^2+<i_B h,R_B i_B h>,
    ||R_B||<=M_B<infinity,

where R_B is the full physical remainder. At the 1.06 anchor RC5 supplies
M_B=20; this is not a new source audit. On every finite cap i_B is compact:
the canonical Fourier weight diverges at high frequency, giving uniform
L2 Fourier-tail control, while supported functions have no spatial escape.
This is the inherited compact form-carrier inclusion, not an assumption
of the previously unresolved spectral L2 source realization.

The exact canonical phase-reference operator is

    A_F=I+i_B^*(R_B-T_E)i_B,
    F(h)=<h,A_F h>_D.

RC12--RC13 already prove F(h)>=gamma||i_B h||_2^2 on this whole support
domain, gamma=627/16000. Smooth-core density and the bounded canonical
representation extend that inequality to D_B.

Also

    F(h)>=||h||_D^2-(M_B+C_E)||i_B h||_2^2.

Combining the two inequalities gives the explicit CANONICAL floor

    A_F>=f_B I,
    f_B=gamma/(gamma+M_B+C_E)>0.                      (3)

Thus the positive reference is invertible in the canonical metric. It is
not merely a physical mass floor mistakenly treated as a canonical floor.

Define the normalized correlation screen by

    K=A_F^(-1/2) i_B^* T_E i_B A_F^(-1/2).

K is compact self-adjoint on D_B: the inclusion i_B is compact, T_E is
bounded on physical L2, and A_F^(-1/2) is bounded on D_B. The exact identity is

    Q(h)=<A_F^(1/2)h,(I+K)A_F^(1/2)h>_D.             (4)

In particular the full missing signed correlation, including every active
prime power and pole term, is inside K.

## What the spectrum condition does and does not accomplish

The sought whole-domain relative-gluing estimate is

    Q(h)>=nu_B F(h), nu_B>0.

By (4) it is equivalent to I+K>=nu_B I, or inf spectrum(K)>-1.
Since K is compact, strict positivity of Q on every nonzero canonical
vector is already equivalent to the existence of some nu_B>0:
a nonpositive direction of I+K occurs in an eigenmode, and nonzero compact
eigenvalues cannot accumulate at -1.

Thus the relative estimate is a faithful formulation of target positivity,
not an independent arithmetic theorem implied by the positive reference.
Compactness locates the problem in finitely many potentially dangerous
spectral directions at each fixed threshold; it does not exclude their
contact with -1.

For an elementary quantitative comparison, if Q>=kappa||i_B h||_2^2 is
ALREADY known, then boundedness of T_E gives

    F=Q-E <= Q+C_E||i_B h||_2^2
           <= (1+C_E/kappa)Q,
    Q>= [kappa/(kappa+C_E)]F.

Conversely Q>=nu_B F gives Q>=nu_B gamma||i_B h||_2^2.
At the 1.06 anchor kappa=eta=1/10^37 supplies such a relative bound.
This uses the existing positivity certificate; it is not an extension to
a larger cap and is consistent with RC13's negative correction test.

## A finite certificate with its whole-space obligations explicit

Let P be a finite-rank orthogonal projection in the NORMALIZED canonical
coordinates of (4), H=I-P. Define

    A=P(I+K)P on range(P),
    D_H=H(I+K)H on range(H),
    C=HKP.

Suppose certified estimates give

    A>=m I, m>0,
    ||HKH||<=tau<1,
    ||HKP||<=rho,
    m>rho^2/(1-tau).                                 (5)

Then D_H>=(1-tau)I, and the exact Schur complement satisfies

    A-C^*D_H^(-1)C
      >= [m-rho^2/(1-tau)]I >0.

This proves I+K>0 with a positive lower bound and therefore proves target
whole positivity on that cap. The high-space and cross estimates are
over the ENTIRE canonical complement. A sampled tail, a physical-coordinate
bound substituted for the normalized one, or a positive finite compression
alone does not satisfy (5).

For rational finite controls:
m=3/4, tau=1/10, rho=1/5 gives Schur reserve 127/180>0.
A positive head can coexist with an unexamined tail eigenvalue -11/10 of K.
Positive head and tail blocks can also coexist with excessive cross mixing:
I+K=[[1,2],[2,1]] has determinant -3. Compact diagonal controls permit both
contact and crossing through the eigenvalue -1. These controls test the
sufficient certificate boundary, not actual zeta negativity.

## Consolidation consequence and remaining work

There is now a positive whole-support reference form and an exact bounded
physical correction. This makes a finite correlation screen lawful, with
a known metric, full signed operator, and explicit tail requirements.

No estimate on the ACTUAL low spectrum, HKH, or HKP is established here.
Computing a finite head would be only the first part of (5). The remaining
arithmetic task is to certify the complete normalized tail and mixing, or
to obtain RC5's near-null decay directly. The positive reference and compact
screen do not supply either estimate automatically.

## Fresh validation and standing

scripts/validate_rpb108_rc14_correlation_screen.py passes 33 exact rational
checks: the anchor split and norm constants, reference-floor and known-anchor
relative-floor identities, the paid Schur reserve, and failure controls for
an unexamined tail, omitted mixing, contact and crossing. Exponential bounds
use rational positive Taylor sums with geometric upper tails. The operator,
compactness and equivalence arguments are analytic proofs above, not sample
inferences.

No actual correlation spectrum or whole tail is certified. The original
whole 1.06 certificate, RC12 sparse theorem and RC13 correction test remain
intact. No whole-aperture extension, original negative vector, RH/F4 theorem
or Lean closure is claimed. Other branches and historical files are unchanged.
