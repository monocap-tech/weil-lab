# RPB108 CC29: critical flux limit and weaker sufficient arithmetic target

2026-10-08 UTC. Coupled parent CC28
`2683f62ce7351007e2a2ed1cbc35f86f69ed5cd1`; paused Global NF71
`6ed350cb6736993fa9801bce9ab15f096c10c200`.
[Definitions](../docs/TERMINOLOGY_RPB108_CRITICAL_FLUX_LIMIT.md).

**Sufficiency refinement, not a new arithmetic covariance estimate.**
For the inherited actual source framework, ANY uniform vanishing modulus
of critical leakage suffices to exclude first contact, provided its band
and positive aperture step are cap-only. A strict reserve below1 and a
low-output bound are not needed for THIS endpoint argument. They remain
inputs to the separate finite-step quantitative continuation proof.

Conditionally on actual first contact, we prove a quantitative lower
divergence of the critical reaction at any fixed strictly larger target.
This is a statement about the actual complete source operators under a
contact hypothesis, not a counterexample establishing actual contact.
No uniform vanishing estimate for zeta is established.

## 1. The newly specified sufficient property

Let a0=21/20 be the inherited strict original source anchor. For every
finite B>a0, ask for cap-only eta_B in (0,1), h_B>0, C_B<infinity and a
bounded nonnegative function omega_B on [0,eta_B], with

    lim_{x->0+} omega_B(x)=omega_B(0)=0.

For EVERY old strictly positive s in [a0,B) and EVERY
s<t<=min(s+h_B,B), put

    E_s=1_[1-eta_B,1)(A_s),
    G_s=E_s(I-A_s)E_s on ran E_s,
    L_st=E_s K_st.

The arithmetic target is the complete matrix/operator inequality

    L_st L_st*<=C_B omega_B(G_s).                           (1)

There is NO requirement C_B<1, NO low-output premise, and NO assumption
that the target t is already positive. All constants and the band are
independent of the old defect. h_B cannot collapse with that defect.
The theorem works on the whole spectral band without a rank assumption.
On a protected finite critical-output chart it is the same full matrix
condition, with all incoming and off-diagonal correlations retained.

Examples of admissible moduli include x^alpha for ANY alpha>0 and
1/log(e/x), continuously extended by0 at x=0. The modulus expresses
decay as the old critical defect vanishes; no such decay is supplied
by the current native identities or existing absolute estimates.

## 2. Strong source exhaustion, without operator-norm continuity

Fix a finite cap B. Extend T_B=N_B P_B^-1 by zero off V_B. The exact
NF67 range identities give

    A_s=T_B Pi_s T_B*,
    A_t-A_s=K_st K_st*>=0.                                (2)

All sources are the original complete divisor sources with multiplicity
copies. Positive observability protects P_B^-1; all operators in (2)
are bounded on this fixed cap, without requiring target positivity.

As s increases to a<=B, the union of D_s is dense in D_a in the canonical
logarithmic norm, by the inherited inward-dilation/smooth-core theorem.
Bounded P therefore gives closure(union V_s)=V_a. Increasing closed
range projections satisfy Pi_s->Pi_a STRONGLY. Hence

    A_s->A_a strongly as s approaches a from below.        (3)

No norm continuity of Pi_s, compactness of T_B, pointwise zero kernel,
finite source cutoff, or differentiated aperture equation is asserted.
This is exact support exhaustion of complete fixed-cap sources.

## 3. Actual contact has nonzero flux into every strict enlargement

Suppose a is an actual nonnegative contact and h is a nonzero original
weak-null vector in D_a. Normalize p=P h to have norm1 and set y=N h.
The contact contraction gives

    ||p||=||y||=1, T_a p=y, T_a* y=p, A_a y=y.

For any t>a in the cap, set

    gamma_t=<y,(A_t-A_a)y>=||K_at* y||^2.                  (4)

**gamma_t>0.** If it were0, then K_at* y=0. Decomposing any P f in
V_t=V_a direct-sum W_at, the old relation T_a* y=p and the zero shell
row would give

    Q(h,f)=<p,P f>-<y,N f>=0 for EVERY f in D_t.

In particular Q(h,tau_r h)=0 for |r|<t-a. Choose a still larger finite
cap if necessary and freeze its native symbol. CC28 says the native
stationary correlation of nonzero h cannot be real analytic at0. A
correlation identically zero on this neighborhood would be analytic,
which is a contradiction. Thus (4) is positive for EVERY t>a.

The same conclusion follows from the earlier strict-enlargement
weak-null rigidity theorem; CC28 supplies a direct native multiplier
proof. Neither route says that actual contact exists. Low outputs
cannot cancel (4), since the shell covariance is nonnegative.

## 4. Critical projection captures the complete contact vector

Let s<a be old strictly positive and eta=eta_B be fixed. On the complete
negative ambient define

    d_s=<y,(I-A_s)y>, y_s=E_s y.

By (3) and A_a y=y, d_s->0. Since A_s>=0 and ||A_s||<1, the defect
I-A_s is positive, d_s>0, and spectral calculus gives

    ||y-y_s||^2<=d_s/eta,
    <y_s,(I-A_s)y_s><=d_s.                                (5)

Thus y_s->y even though no continuity of E_s as an operator is assumed.
The estimates apply to the WHOLE spectral projection, not a selected
approximate eigenvector or a finite zero packet.

Fix t>a and choose s sufficiently close to a that t-s<=h_B. Set
M=||A_t||, which is finite. With A_s<=A_t and ||y_s||<=1,

    n_s=<y_s,(A_t-A_s)y_s>
        >=gamma_t-2M sqrt(d_s/eta).                       (6)

Indeed <y,(A_t-A_s)y>=gamma_t+d_s, and replacing y by y_s changes
the pairing by at most2M||y-y_s||. Consequently n_s>=gamma_t/2
for d_s<=eta gamma_t^2/(16M^2). In particular

    <y_s,L_st L_st* y_s>=n_s ->gamma_t>0.                 (7)

This is the crucial incompatibility: the contact component of incoming
covariance stays nonzero, while its old defect tends to zero.

For omega(x)=x, (5)-(7) prove the explicit conditional lower bound

    ||G_s^(-1/2)L_st L_st*G_s^(-1/2)||
        >=gamma_t/(2d_s) ->infinity.                      (8)

G_s is invertible on the old band because the old gain is strictly
below1. This bound is in the exact original source metric. d_s is the
expected source defect of the hypothetical contact vector, not the
joined physical certificate margin. No numerical gamma_t is evaluated.

For alpha>0, spectral Jensen when alpha<=1, and x^alpha<=x on [0,1]
when alpha>=1, give

    <y_s,G_s^alpha y_s><=d_s^min(alpha,1).

Hence the analog of (8) is at least
gamma_t/[2d_s^min(alpha,1)]. Even a sublinear power target fails at a
fixed enlargement under the actual contact hypothesis.

## 5. Any uniform vanishing modulus contradicts contact

Let mu_s be the spectral measure of I-A_s in the fixed unit vector y.
For epsilon in (0,eta), boundedness and nonnegativity of omega give

    <y_s,omega(G_s)y_s>
       <=sup_{0<=x<=epsilon} omega(x)
                            +||omega||_infinity d_s/epsilon. (9)

The first term tends to0 with epsilon; for fixed epsilon the second
tends to0 with s approaching a. Thus (9) tends to0. If (1) held, it
would imply n_s->0, contradicting (7). All mixed critical entries remain
inside this tested quadratic; it is not a sum of separate row bounds.

Only ONE fixed t>a is needed for this contradiction. Given an interior
contact a<B, choose t-a<min(h_B/2,(B-a)/2), then take s close enough
to a. This is why a positive cap-only step is essential. An estimate
restricted to already-positive targets, or to steps tending to0 with
d_s, cannot be substituted for (1).

## 6. All-cap logical strength and the earlier product budget

The inherited actual first-contact constructor gives a norm-continuous
identity-plus-compact physical form family on one dilated logarithmic
domain. From the strict anchor and any actual negative compact test,
take the EARLIEST nonpositive lower spectral bound. It is an interior
attained null contact; all preceding forms are strictly coercive. Their
source gains are strictly below1 by the complete positive upper bound.
This dilated form operator is not the source Gram A_a; no compactness
of T_B is inferred.
This uses that existing constructor, not a renewed regularity or generic
continuity investigation. No actual negative vector is supplied here.

If the property (1) holds on every finite cap, such contact is impossible
by sections3-5. Hence there is no actual negative compact test. The
classical compact-test Weil criterion, imported in CC26, then gives RH.
Conversely RH makes every original negative profile zero, so T_a=0,
A_a=0 and all critical bands for eta<1 are empty. Property (1) holds
with zero covariance. Under the inherited analytic framework, the fully
specified all-cap vanishing-modulus property is therefore RH-equivalent.
The property is NOT proved. This is not an RH proof or an independence
theorem about the complete identities.

On a finite generalized critical chart, the power version is equivalent
to the independently specified arithmetic target

    J M_t^-1 J*<=C_B Lambda G^alpha.                      (10)

Lambda and G commute in the eigenbasis. All original native rows and
the whole protected positive inverse remain. alpha<1 weakens the target
relative to a uniform defect-relative lower frame bound; it can allow
G^-1-weighted costs to diverge while still excluding contact through the
endpoint argument. No arbitrary cap-only absolute bound supplies (10).

CC26's finite-step product proof still requires a strict whole budget,
including low outputs. This note adds a DIFFERENT endpoint sufficiency
argument. It does not retroactively assert that an unspecified critical
estimate, a shrinking band, or stalling steps were sufficient. There is
no newly evaluated product reserve, positive frame constant, accumulated
loss bound or aperture certificate. This audit changes the minimum
sufficient target; it does not count as a proved arithmetic upper bound.

## 7. Genuine crossing and complete positive-level controls

The inherited differential crossing has lambda=u^2, defect1-u^2 and
complete old-ground leakage2u(v-u). At a fixed target v=1+h, h>0,
the numerator tends to2h>0 as u approaches1. Dividing by ANY positive
power of1-u^2 diverges. These are genuine source-shell values including
the interior lift, not naive strip norms. The next physical level stays
separated at contact. Thus the weaker target still rejects the genuine
crossing and has not smuggled a structural no-crossing assumption in.

At a shifted positive physical level, the full negative analysis must
include sqrt(mu) times the ENTIRE physical vector. Its own contact
output and critical projection then replace the original ones in (4)-(9).
The argument detects shifted contact as well; it is not by itself an
original-nullity discriminator. Apply (1) only to the ORIGINAL actual
sources. The finite P=I, N=(9/25,12/25) control has original budget9/34<1;
the full16/25 mass shift gives critical plus low budget1. The validator
retains this distinction and replays CC28's genuine shifted operator.

The new finite operator checks have rotating noncommuting critical
projections, monotone positive defects, nonzero contact flux and exact
inverse-defect/power growth. They validate the spectral algebra, not an
actual zeta contact or a numerically evaluated infinite source map.
24,872 exact checks pass: 124 new checks and 24,748 inherited CC28 checks.
The strong limit, modulus argument and native no-flatness are analytic,
not certified by finite samples or new Lean theorems.

## Standing and source custody

Original whole-domain anchor remains21/20 even0/odd0, joined PHYSICAL
margin1/(3*10^63), not a numerical source defect. No new aperture. RH/F4,
retained attachment, reusable continuation, accumulated finite-cap loss
and Lean closure remain open. Coupled alone advances; Global NF71,
Aperture and Pre-Contact Shadow remain paused.

Inherited proofs: ACTUAL_FIRST_CONTACT_CONSTRUCTOR (2026-10-04),
SOURCE_SHELL_GAIN/NF67, LOG_SOURCE_ANALYSIS, CC20 covariance and CC28
native nonanalyticity. All are used in their published analytic scope.
Classical criterion: Connes--Consani arXiv2006.13771v1 introduction(2),
AppendixC PropositionC.1, rechecked2026-10-08. No new external arithmetic
correlation input is claimed.
