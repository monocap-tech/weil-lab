# RPB108 RC9 — a proved two-packet relative gluing bound

2026-10-10. Independent route consolidation.
Parent: 84eee499e5cf35b64a999b052438de2042a86fa3 (RC8).
Only research/rpb108-route-consolidation is written.

## Result and scope

The negative narrow-packet correction from RC8 can be paid by the COMPLETE
local energies. This step proves a uniform relative-loss bound on a specific
infinite-dimensional family, with independent arbitrary complex profiles:

    epsilon = 1/1000, L = log9,
    I_left  = (-L/2-epsilon, -L/2+epsilon),
    I_right = ( L/2-epsilon,  L/2+epsilon).

For smooth complex u,v supported in I_left,I_right respectively, set h=u+v
and E=Q(h)-Q(u)-Q(v). Then

    |E| <= (568/585)[Q(u)+Q(v)],
    Q(h) >= (17/585)[Q(u)+Q(v)]
         >= (17/1500)||h||_2^2.                         (1)

The complete signed native form is used. These are unrestricted complex
profiles on the two small intervals: they need not be even, nonnegative,
proportional, or flat. Arbitrary relative amplitudes and phases are allowed.

The union fits inside aperture 11/10. Formula (1) is NOT whole positivity
on that centered interval: its gap is excluded from the supported family.
No whole-aperture certificate is extended. The existing anchor is used only
on auxiliary tests lying within 1.06, not on the target at 1.10.

## Definitions and pinned dependencies

Q denotes the original native Weil form, with all archimedean, prime-power
and signed pole terms attached. It is stationary under simultaneous physical
translation. For disjoint ordered packets its separated continuous kernel is

    K_cont(d)=2cosh(d/2)-j(d),
    j(d)=exp(-d/2)/(1-exp(-2d)), d>0,

and its prime atoms have coefficient -c_n at +/-log n,
c_n=Lambda(n)/sqrt(n). This is the same CC27 attachment used by RC7--RC8:
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.

The inherited CC119 anchor, under its original source/domain/high-floor
attachments, supplies

    Q(g) >= eta ||g||_2^2, eta=1/10^37,

for smooth g supported in (-53/50,53/50). This step does not rerun that
source certificate or add a new Lean theorem.

For a profile phi supported in (-epsilon,epsilon), define
q_phi=Q(phi), m_phi=||phi||_2. In this report m_phi is a PHYSICAL norm;
it is not RC8's pole moment. The self-energy is the entire Q, not an
archimedean-only or source-truncated quantity.

## Borrowing a local energy floor from the anchor

Let phi be any smooth complex profile with m_phi=1. Form two exact copies

    a(x)=phi(x+log2/2), b(x)=phi(x-log2/2).

Their supports are disjoint and lie strictly inside the certified anchor:
log2<7/10 and log2/2+epsilon<53/50.
Stationarity gives Q(a)=Q(b)=q_phi.

Their mixed prime2 contribution is exactly -c_2, because the forward
translation overlap is integral conjugate(phi)phi=1. The reverse orientation
has no overlap. Every other prime power has displacement at least log3>1,
while all cross distances are between 1/2 and 1. Those overlaps vanish.

On the entire cross-distance range,

    |K_cont(d)|<5.

Indeed exp(1/2)<5/3 bounds the pole kernel by 3, and exp(1)>2 bounds j by 2.
Physical Cauchy--Schwarz gives ||phi||_1^2<=2epsilon even for a complex,
sign-changing profile. Hence the complete continuous mixed pairing has
absolute value at most 10epsilon=1/100.

Since log2>3/5 and sqrt2<3/2, c_2>2/5. Therefore

    Re Q(a,b) < -2/5+1/100 = -39/100.

Apply the ACTUAL anchor to a+b, whose physical mass is 2:

    2q_phi + 2 Re Q(a,b) >= 2eta,
    q_phi > 39/100 + eta.

Scaling, translating, and including the zero profile give the useful bound

    Q(phi) >= (39/100)||phi||_2^2                       (2)

for every smooth complex profile of this small support width.

This uses short-prime arithmetic and the completed anchor to extract a
substantial self-energy floor. It does not use target positivity or
signed Cauchy--Schwarz at a potentially unproved target aperture. It also
does not estimate the singular archimedean self-energy in isolation.

## Bounding the long-jump mixed pairing for independent profiles

Write u,v as translates of independent profiles phi,psi supported in
(-epsilon,epsilon), with physical norms x,y. Their mixed pairing is

    Q(u,v) = continuous_cross - c_9 integral conjugate(phi)psi.

The prime9 coefficient is c_9=log3/3, not log9/3. The reverse orientation
vanishes. All other active prime overlaps vanish:

* exp(1099/500)>9 ensures the union fits aperture 11/10;
* exp(11/5)<10 gives active powers 2,3,4,5,7,8,9;
* exp(1/500)<9/8 excludes prime8 and all smaller displacements;
* the next possible displacement is also outside the support range.

The aligned overlap now need not equal one, but its absolute value is at
most xy by physical L2 Cauchy--Schwarz.

Every cross distance is in (2,12/5). On this entire range the pole kernel
is <5 and j(d)<1, so |K_cont(d)|<6. Also

    ||phi||_1 ||psi||_1 <= 2epsilon xy.

The complete continuous mixed pairing is consequently at most
12epsilon xy in absolute value, including the signed poles.
Since log3<11/10,

    |Q(u,v)| <= [11/30+12epsilon]xy
              = (142/375)xy.                          (3)

Equations (2)--(3) retain all original terms and require no agreement of the
two profiles, no favorable phase, and no pointwise positivity of the kernel.

## Relative loss and amplitude optimization

Put q_u=Q(u), q_v=Q(v), d=39/100 and r=142/375.
From (2), q_u>=d x^2 and q_v>=d y^2. Thus

    |Q(u,v)| <= (r/d) sqrt(q_u q_v),
    r/d = 568/585 < 1.

The elementary inequality 2sqrt(q_u q_v)<=q_u+q_v gives

    |E| = |2 Re Q(u,v)|
         <= (568/585)(q_u+q_v).

This proves the relative-loss estimate, rather than inferring it from the
negative correction alone. It handles every relative amplitude and phase.

Alternatively the absolute mass bound follows directly from

    Q(u+v) >= d(x^2+y^2)-2rxy
            = (d-r)(x^2+y^2)+r(x-y)^2,
    d-r = 17/1500.

The supports are disjoint, so ||u+v||_2^2=x^2+y^2.
Both deductions give (1).

For matching normalized profiles, the actual two-dimensional Gram matrix
has diagonal q_phi and mixed entry Q(u,v); its eigenvalues are
q_phi +/- |Q(u,v)|. The computed reserve pays both eigenvalues. A positive
mixed correction for equal coefficients, as in RC8's wider example,
would not by itself suffice: opposite phases can reverse its contribution.
Here the ABSOLUTE mixed estimate explicitly covers that issue.

## What this changes and what remains open

RC8's narrow negative correction is not an obstruction to quantitative
gluing on its own test family. A certified local-energy budget pays it
with relative reserve 17/585. The proof improves on using only the tiny
common anchor guard eta: the short-prime probe converts the complete
anchor into the stronger profile-specific width bound (2).

The result does not imply arbitrary partition gluing, wide-packet control,
a train of many packets, or near-null outward decay. Many pieces can
accumulate several mixed interactions, and more separations can activate
additional atoms and continuous pole correlations. A two-piece relative
bound cannot simply be multiplied into a whole-domain theorem.

The broader route still needs a collective estimate against complete local
energies, or RC5's arithmetic decay on genuine near-null vectors. This is a
positive restricted gluing theorem inside that investigation, not closure
of the endpoint route.

## Fresh validation

scripts/validate_rpb108_rc9_two_packet_gluing.py passes 37 new exact rational
checks: support caps, log and root enclosures, atom exclusions, continuous
allowances, d=39/100, r=142/375, theta=568/585, and both reserves.
Exponential bounds use positive rational Taylor sums and a geometric
remainder bound. Finite algebra controls illustrate the exact square
identity; they do not replace the analytic universal argument.

No actual critical mode is evaluated. No negative original vector,
whole-aperture extension, RH/F4 theorem, or Lean closure is claimed.
Other branches and historical files remain unchanged.
