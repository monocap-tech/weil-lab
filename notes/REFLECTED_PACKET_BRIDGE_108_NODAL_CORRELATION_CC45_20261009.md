# RPB108 CC45 — Exact native nodal test and an atom-free balanced control

Date: 2026-10-09 UTC. Publication base 368dbee08f9223dcbcc602eb685bdd16586196bd.
[Definitions](../docs/TERMINOLOGY_RPB108_NODAL_CORRELATION_CC45.md).
This tests the even invisible channel identified by CC43–44. It retains
the full native gamma term, all active prime powers and both pole terms.

## 1. Necessary arithmetic inequality at an actual invisible contact

Assume Q>=0 on the whole cap and h is a nonzero real even original null
with c(h)=0. Put h=u-v, A=c(u)=c(v)>0. Both poles vanish on h, so
H(h)=Q(h)=0. CC43's canonical-domain absolute-value identity gives

    D(h)=4 integral integral j(x-y)u(x)v(y) dx dy
       +2 sum c_n integral (|h(x)h(x+ell_n)|
                                      -h(x)h(x+ell_n)) dx,       (1)

where j(d)=exp(-|d|/2)/(1-exp(-2|d|)), c_n=Lambda(n)/sqrt(n),
ell_n=log n. Every term is nonnegative, and the continuous term is
strictly positive. The integral is finite on the logarithmic form domain
by CC43; no pointwise operator action or boundary trace is asserted.

Since c(|h|)=2A, original positivity on |h| implies

    0<=Q(|h|)=H(|h|)+2c(|h|)^2=-D(h)+8A^2.

Thus an actual even invisible null must satisfy

    0<rho(h)=D(h)/(4A^2)<=2.                                (2)

An additional estimate rho(h)>2 for every actual such null would exclude
this channel. It is a sufficient contradiction criterion only; no claim
is made that it is the minimal collective defect-relative frame estimate.
The endpoint rho=2 also needs care: |h| would itself be an original null,
with nonzero moment, so neither nonnegativity nor strict comparison alone
rules it out. The odd invisible channel and moment-carrying thresholds
are not eliminated by this even test.

Equivalently introduce probability measures dnu_+=cosh(x/2)u(x)dx/A,
dnu_-=cosh(y/2)v(y)dy/A. Then

    rho(h)=integral integral j(x-y)/(cosh(x/2)cosh(y/2))
                                           dnu_+(x)dnu_-(y)
            + [complete nonnegative prime cost]/(4A^2).        (3)

This identifies the missing spatial information: how an actual null's
opposite signs correlate at continuous separations and prime displacements.
A scalar pole susceptibility observes only A, not these correlations.

## 2. The coefficient-only strict inequality is false inside the anchor

Take b=2log(3/2)=log(9/4), which is strictly below 21/20. Put a smooth
nonnegative even positive packet near 0, and negative packets symmetrically
near +/-b. Use sufficiently small disjoint supports and scale the negative
pair to enforce c(u)=c(v)=1 EXACTLY. Then h=u-v is smooth, real, even,
supported strictly inside the anchor, and has exactly zero cosh moment.

The distances between opposite signs converge to b. Since exp(b)=9/4
is not an integer, no prime-power displacement equals b. The finite active
prime set has a positive distance from b; sufficiently narrow packets
therefore make EVERY cross-sign prime overlap zero. Interactions within
one sign do not contribute to (1). The negative-negative separation 2b
has exp(2b)=81/16, also nonintegral, although this avoidance is not needed.

By continuity of j away from zero and concentration of the two weighted
probability measures, the exact ratio tends to

    j(b)/cosh(b/2)
      =[(3/2)^3/((3/2)^4-1)] / [(3/2+2/3)/2]
      =648/845 < 2.                                         (4)

Consequently rho(h)<2 for sufficiently narrow actual native balanced
trials. This disproves a proposed universal strict nodal inequality on
ALL even moment-zero vectors; actual coefficients and all prime terms
have been retained. It does NOT exhibit a native null or counterexample
to RH. These packets in fact have positive original energy at the certified
anchor. Independently, shrinking a fixed smooth packet shape drives its
logarithmic energy divided by physical mass to infinity, whereas CC33's
physical remainder is bounded; their narrow-support high-frequency cost
prevents their use as near-critical witnesses.

For an exact anchor check use log(3/2)<(3/2-1)=1/2, giving b<1<21/20.
The rational validator verifies the ratio, balanced atomic-limit weights,
and separation from every integer 2 through 8 in the anchor prime set.
All 25 new exact checks pass; no historical chain total is added.
It does not evaluate smooth packet energies, actual zeta eigenvectors,
or the null-adapted inequality (2) beyond its analytic derivation.

## 3. Positive-level and genuine-crossing discrimination

For Q_mu=Q-mu||h||_2^2 the absolute-value difference is unchanged because
||h||_2=|| |h| ||_2. If a shifted whole-domain nonnegative form has a
zero-moment even null, the same derivation gives D(h)<=8A^2. Thus this
necessary nodal comparison does not discriminate an original zero from
a shifted positive eigenlevel. The full physical mass term cancels in
the comparison; it must be retained in the separate null equation.

For a smooth real Dirichlet differential control, the local kinetic and
mass energies are unchanged under absolute value; there is no nonlocal
strict cross-sign cost. Its D is zero, so the proposed >2 exclusion fails
there. This distinguishes the native nonlocal sign structure from that
local control, but it does not establish a native arithmetic advantage
strong enough to cross the actual threshold2. No new source-shell rate
or genuine-crossing exclusion is inferred.

## 4. Result and remaining task

The actual null must obey (2), whereas actual noncritical balanced trials
can also obey it. The generic favorable-kernel route therefore cannot
supply the missing floor. A viable next estimate must use the complete
mixed-null equation to constrain the probability measures in (3), rather
than treating them as arbitrary balanced measures. That arithmetic
correlation estimate is not proved here. CC44's moment-zero spectral floor,
the collective source-frame bound, contact exclusion and RH/F4/Lean remain
open. The whole-domain positive anchor remains21/20; concurrent NF14
E48/E64 finite certificates do not establish full positivity at53/50.
