# RPB108 CC46 — Mixed nullity forces two negative nodal energies

Date: 2026-10-09 UTC. Publication base 9c95fc2fb3c1027ea8734ca433306c9456ed4fc2.
Fresh integration base4cd98892a146e86b9bf58e2207d902c065f120d2 preserves the concurrent NF15 E80 handoff; it is not used to infer whole-domain positivity.
[Definitions](../docs/TERMINOLOGY_RPB108_NODAL_ENERGY_CC46.md).
This adds the actual mixed-null equation to CC45's necessary nodal test.

## 1. The stronger exact balance

Assume Q>=0 on the whole cap and h is a nonzero real even original
null with c(h)=0. The two poles vanish in all mixed pairings with h.
Nonnegative-form mixed nullity therefore gives H(h,f)=0 for every
supported form-domain f. Positive and negative parts u,v belong to that
domain by CC43's absolute-value contraction. Taking f=u and f=v gives

    H(u,u)=H(u,v)=H(v,v)=-C,  C=D(h)/4>0.            (1)

Here the exact continuous and prime terms make H(u,v) negative: their
cross-sign expression is the one in CC45, including all prime powers.
Thus BOTH nodal parts must have strictly negative pole-free energy.
This conclusion uses mixed nullity; arbitrary balanced trials need not
and generally do not satisfy it. Their pole-free form Gram is exactly

    -C [[1,1],[1,1]],                                (2)

with one negative and one zero direction. It is compatible with CC43's
one-negative-eigenvalue index and supplies no contradiction by itself.

Since c(u)=c(v)=A, their original form Gram is

    (2A^2-C) [[1,1],[1,1]].                          (3)

Original nonnegativity is equivalent on this span to C<=2A^2,
recovering CC45. These are form Grams on nonnormalized u,v, not physical
operator eigenvalues. The full mixed-null equation on other tests remains
stronger than these two selected tests.

## 2. An effective support-measure obstruction from the native remainder

On any fixed finite cap B, CC33/37 give

    H(f)=E_log(f)+<f,R_0(B)f>,
    ||R_0(B)||<=r_0(B)=8+2 sum_(log n<=2B) Lambda(n)/sqrt(n). (4)

There is no pole norm in (4); both pole terms have actually been removed.
For B<=21/20 the exact coefficient sum upper bound12093/3740 gives
r_0<8+2(12093/3740)=27053/1870<15. On arbitrary finite caps the finite
sum remains a valid cap-dependent envelope; no all-cap constant15 is used.

If nonzero f has support measure m, the pinned Fourier convention and
Cauchy-Schwarz imply |Fourier f(xi)|^2<=m||f||_2^2. Thus the physical
mass in [-R,R] is at most2Rm times the total mass. Since log(e+|xi|)>=1,
for 2Rm<=1,

    E_log(f)/||f||_2^2
       >=1+(1-2Rm)[log(e+R)-1].                     (5)

Choose R=1/(4m). If H(f)<0, (4) and (5) imply

    [1+log(e+1/(4m))]/2 < r_0,
    m > 1/[4(exp(2r_0-1)-e)].                       (6)

A negative H trial requires r_0>1; if r_0<=1 then E_log>=mass already
rules it out, so no nonpositive denominator in (6) is interpreted.
Applying (6) independently to u and v yields an explicit positive lower
measure for EACH nodal set of an actual invisible null. Also (1),(4) give

    C <= (r_0-1)||u||_2^2,
    C <= (r_0-1)||v||_2^2.                          (7)

At the anchor envelope15 this is the conservative lower nodal measure
1/[4(exp29-e)]. It is extremely small and does not certify a new aperture.
These statements use only the closed logarithmic form and bounded
physical remainder, not an unrestricted Fourier operator domain, H1
regularity, endpoint values or an attachment theorem.

## 3. What this does to the previous control

CC45's narrow balanced atom-free packets have nodal measures tending
to zero. Their ratio C/A^2 tends to648/845<2, so sign balance alone admits
them. Equations (1) and (6) prohibit them from being actual nulls once
their nodal measures fall below the cap-dependent threshold. This is
a concrete restriction supplied by the mixed equation, rather than an
assumption that arbitrary balanced measures behave like eigenvectors.

It does not prove rho>2 for the remaining broad nodal profiles, force a
positive cross-sign prime overlap, or supply the moment-zero spectral
floor. Positive-measure disjoint nodal sets can avoid a finite collection
of displacements; no contrary implication is asserted from (6).

## 4. Required controls and remaining arithmetic question

In the CC44 rational favorable-sign model, the null z=(1,-1,0) has
u=e1,v=e2 and H(u)=H(u,v)=H(v)=-1/6. Its moment profile gives c(u)=c(v)
and its original Gram is exactly (3). Thus even the strengthened energy
balance still permits a genuine higher null in the structural control.

For a full physical level shift Q_mu=Q-mu||h||_2^2, the corresponding
pole-free H_mu=H-mu I has remainder envelope r_0+mu for mu>=0. If the
shifted form is nonnegative with a zero-moment null, the same nodal balance
and support argument apply to H_mu, using that enlarged envelope. The
full mass term is retained. This cannot certify that a shifted null is
an original null.

The local differential genuine-crossing control has a nonnegative even
ground null with nonzero pole moment, so it is outside the assumed
invisible, sign-changing channel. No exclusion of that control follows
from this channel-specific theorem.

The validator checks the rational remainder bound, nonnormalized H/Q
Grams and shifted mass corrections, and exact algebra in the Fourier
band bound. Its finite checks do not evaluate native nulls or certify
transcendental support thresholds numerically. The analytic proof of
(5) is Plancherel and Cauchy-Schwarz, not a numerical sample.
All40 new exact checks pass; no historical chain total is added.

Next: use the full native mixed equation to control broad nodal profiles
that satisfy (1),(6), and their prime overlaps. The elementary support
floor does not supply the desired quantitative collective source frame.
RH/F4, the original all-cap arithmetic floor, contact exclusion and Lean
remain open. Whole-domain positivity remains21/20 with physical margin
1/(3*10^63); finite E64/F112 certificates still need full mixed control.
