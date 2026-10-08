# RPB108 NF56: cancel the prime main term before estimating gain

Date: 2026-10-08 UTC. Recovered head 9be5c1d0227422c2ae22b0538f832c5d46092c92.
Definitions: [prime–pole discrepancy](../docs/TERMINOLOGY_RPB108_PRIME_POLE_DISCREPANCY.md).

This pass tries a direct arithmetic estimate for the original source-gain target. It obtains an exact cancellation formula and checks the first six actual prime-power jumps. The proposed shortcut from a scalar discrepancy sign to a quadratic sign fails on smooth physical tests. No new gain upper bound or positivity interval is obtained.

## Combine the original prime and pole terms

Write E0(h) for the unchanged archimedean form and L=2a. The actual physical formula is

    Q_a(h)=E0(h)-2 sum_(log n<=L) Lambda(n)/sqrt(n) c_h(log n)
                     +4 integral_0^L cosh(s/2)c_h(s) ds.

The pole term comes from the original kernel 2cosh((x-y)/2). It is not declared positive as a quadratic form. Since 2cosh(s/2)=exp(s/2)+exp(-s/2), the definition of dV gives EXACTLY

    Q_a(h)=E0(h)+2 integral_0^L exp(-s/2)c_h(s) ds+R_a(h),
    R_a(h)=-2 integral_[0,L] c_h(s)dV(s).                (1)

The growing exp(s/2) pole term cancels the continuum density exp(s/2)ds inserted in the actual prime sum. This is an algebraic main-term subtraction, not a prime number theorem assumption or an approximation of actual primes. All prime powers remain in dV. Threshold equality is harmless because C_h(L)=0.

Every term in (1) is lawful on the original supported canonical carrier: C_h is continuous by physical L2 translation continuity, |C_h(s)|<=||h||_2², and the measure has finite total variation on [0,L]. The identity is already a bounded physical correction to E0 and requires no null hypothesis. No height limit or source truncation is involved.

The decaying kernel exp(-|x-y|/2) is positive definite: its angular Fourier transform is 1/(eta²+1/4)>0, obtained by integrating the two exponential half-rays. Its form is the middle term in (1). E0 itself has a negative low-frequency part, so positivity of this one contribution does not settle Q_a.

For smooth compact tests integration by parts gives

    R_a(h)=2 integral_0^L V(s)c_h'(s) ds.               (2)

The boundary terms vanish because V(0)=0 and C_h(L)=0. On the full canonical domain use (1); no H1 premise or unsupported absolute-integrability assertion for c_h' is introduced.

## Actual scalar sign through the prime-8 threshold

The complete prime-power list up to 8 is 2,3,4,5,7,8. Between jumps V'(s)=-exp(s/2)<0. At a jump log n,

    V(log n)=sum_(m<=n) Lambda(m)/sqrt(m)-2(sqrt(n)-1).

Exact rational logarithm and square-root enclosures verify V(log n)<-1/4 at EACH of those six jumps. Before log 2, V(s)=-2(exp(s/2)-1)<0 for s>0. Consequently

    V(s)<0 for 0<s<=log 8,
    V(s)<-1/4 for log 2<=s<=log 8.                    (3)

This is an arithmetic scalar bound through a=log(8)/2. It is not a whole-domain positivity certificate at that aperture and does not change the aperture front. No assertion about V at later prime powers follows.

## The sign test fails on the actual physical carrier

One might try to combine V<=0 with (2) to conclude R_a>=0. That requires c_h'<=0, which is false for general supported vectors. In fact R_a takes BOTH signs inside an already certified window.

Choose a=1/4, d=1/8, epsilon=1/64. There are no active primes because 2a=1/2<log 2. Let f_+ and f_- be smooth nonnegative bumps of integral one supported respectively in [d-epsilon,d+epsilon] and [-d-epsilon,-d+epsilon], with f_-(x)=f_+(-x). They lie strictly inside [-a,a]. For h=f_+-f_-, formula (1) reduces the discrepancy form to the original growing kernel:

    R_a(h)=integral integral h(x)conjugate(h(y)) exp(|x-y|/2) dxdy.

Each same-bump term is at most exp(epsilon), and each cross term is at least exp(d-epsilon). Thus

    R_a(f_+-f_-) <= 2exp(epsilon)-2exp(d-epsilon)<0,

because 2epsilon<d. For h=f_++f_-, all four terms are positive. Both are smooth actual physical carrier vectors. These are not freely prescribed divisor packets, artificial zero dictionaries, or null vectors. The complete Q remains positive in this window by the standing certificate; a negative discrepancy component is consistent with that.

This disposes of the scalar-sign shortcut despite the ACTUAL bound (3). The remaining question is the full quadratic balance between E0, the decaying kernel, and the signed discrepancy, not the sign of V alone.

## What this changes in the direct attack

Separate absolute prime and pole budgets discard their leading cancellation. Formula (1) keeps it exactly and gives a finite-window arithmetic object to estimate against the canonical archimedean energy. An upper gain certificate would need a lower bound for the TOTAL expression (1) on every supported vector, with a positive aperture-dependent margin. No such bound is proved here.

A bound on ||V||_infinity times integral |c_h'| is not currently a canonical-domain estimate. Smooth-test density alone does not make its derivative constant uniform. Likewise (3) cannot be promoted to a positive-definite discrepancy kernel. Those two substitutions are excluded from future use of this representation.

The positive-level control remains explicit: replacing Q_a by Q_a-mu||h||_2² changes only the archimedean part of (1) to E0-mu mass. Keeping the SAME dV does not remove mu. Thus this arithmetic representation cannot declare a relative positive-eigenmode contact an original zero contact.

Validation: six actual jump bounds, supported bump inequalities, threshold custody, and algebraic cancellation controls in the companion script. The continuous form identities and smooth-bump sign proof are analytic, not Lean certified. This is one attempted direct estimate with a failed shortcut; it does not discharge the source-gain target, global exclusion, RH, F4 or full transport. Aperture-one and all concurrent custody are preserved.
