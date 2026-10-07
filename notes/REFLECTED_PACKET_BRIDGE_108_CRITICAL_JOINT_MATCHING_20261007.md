# RPB108: a joint critical boundary estimate and a lawful signed moment

Date: 2026-10-07 UTC. Recovered live head 89e4f194063f93a073954a813e1dfed39720b0fb.
Definitions: [critical joint boundary matching](../docs/TERMINOLOGY_RPB108_CRITICAL_JOINT_MATCHING.md).
Category: critical derivative promotion / endpoint exclusion.
Analytic implication on actual K_a intersect Xcrit, not a proof of critical membership or L2 derivative promotion.

## Result

For every actual h in K_a intersect Xcrit, the complete right-edge decomposition satisfies

    integral_0^delta |Cf(u)-2A_h(u)|^2/[u log(1/u)]du<infinity.

The actual drive also satisfies

    integral_0^delta |A_h(u)-A_h(0)|^2/[u log(1/u)]du<infinity.

Consequently the signed improper moment exists and the entire Carleman profile has the same ordinary limit:

    M_R(h)=lim_(epsilon down to 0) integral_epsilon^(2a) h(a-v)/v dv
          =lim_(u down to 0) Cf(u)
          =2A_h(0).

Absolute inverse-moment integrability is not proved. Reflection gives the corresponding left-end result. No scalar injectivity, H1 regularity, nonzero actual null existence or contact exclusion follows.

This closes the previously missing EXISTENCE and actual boundary-matching part of the inverse-moment interface under critical membership. The existing noninjectivity audit is preserved. This is not a replacement of the full profile by a scalar for endpoint exclusion.

## 1. Two Fourier difference norms and their boundary consequences

Put r=1+|xi|, w=log(e+|xi|), and choose a fixed delta0<exp(-4). For either sign of translation, the following difference integrals, together with physical L2 mass, give equivalent high-frequency norms:

    D_X(v)=integral_0^delta0 ||tau_t v-v||_2^2
                              log(1/t)/t^2 dt
       corresponds to integral r w |vhat|^2,

    D_E(v)=integral_0^delta0 ||tau_t v-v||_2^2
                              1/[t^2 log(1/t)] dt
       corresponds to integral r/w |vhat|^2.

Tonelli and Plancherel reduce these statements to the cosine multipliers. At large |xi|, split at t=1/|xi|. The low-t upper bound 1-cos(2pi xi t)<=C xi^2 t^2 gives the required |xi|log|xi| or |xi|/log|xi| bound. The upper tails follow by integrating log(1/t)/t^2, respectively 1/[t^2 log(1/t)]. In the latter integral, the derivative of 1/[t log(1/t)] bounds the integrand up to 4/3 while log(1/t)>=4. Lower bounds use t in [1/(8|xi|),1/(4|xi|)], where the cosine defect is bounded away from zero. Low frequencies are controlled by mass.

Apply D_X to the supported h at its right endpoint, comparing each x=a-v with outside points x+t for t in [v,2v]. Positivity of the physical difference integral yields

    integral_0^delta |f(v)|^2 log(1/v)/v dv<infinity.       (1)

Now set q_h=m_a(D)h+p_h and localize it by a smooth compact cutoff equal to one near a. Since |m_a|<=C_a w and h is Xcrit, the localized q_h is in Ecrit, with squared Fourier weight r/w. Exact full-native nullity makes it zero on the physical interior. It is therefore an already exterior-supported Ecrit function near this endpoint.

Apply D_E across that zero side, again using separations between u and 2u. This gives

    integral_0^delta |r_h(a+u)|^2/[u log(1/u)]du<infinity.

The read actual identity r_h(a+u)=-(1/2)Cf(u)+A_h(u) proves the first displayed joint estimate. No sharp critical support projection is used. The full-null interior equation, rather than continuity alone, supplies the zero side of this boundary estimate.

## 2. The continuous drive has the stronger weighted convergence needed here

The previous critical interior-gain theorem gives local Fourier weight r w^3 at every strict prime evaluation point. Its Fourier Cauchy-Schwarz estimate gives, at those fixed interior points,

    |h(x+u)-h(x)|<=C/log(1/u).

Indeed the squared modulus budget is integral min(4,C xi^2 u^2)/(r w^3)dxi. Frequencies below u^(-1/2) contribute O(u), the next band O(log^(-3)(1/u)), and frequencies above u^(-1) contribute O(log^(-2)(1/u)). Taking a square root proves the assertion.

The pole and regular Euler integral in A_h are Lipschitz in u. Every strict prime term obeys the preceding modulus. If a threshold prime log n=2a is present, its boundary profile is O(log^(-1/2)(1/u)) by the same previous theorem and its endpoint value is zero. Thus

    |A_h(u)-A_h(0)|<=C/log^(1/2)(1/u),

with the stronger inverse-log modulus when there is no threshold term. In either case the drive difference has finite weighted integral, since integral du/[u log^2(1/u)] converges.

Combining with step 1 yields

    integral_0^delta |Cf(u)-2A_h(0)|^2/[u log(1/u)]du
       <infinity.                                      (2)

This controls a full actual profile in a critical boundary norm. It does not claim a pointwise limit from weighted L2 alone; the next step uses (1) as well.

## 3. A logarithmic primitive makes the ordinary limit lawful

Choose v0=exp(-L0)<delta, with L0>4, and put F(L)=f(exp(-L)) for L>=L0. Equation (1) is

    integral_L0^infinity L |F(L)|^2 dL<infinity.          (3)

The contribution from v>=v0 has a finite inverse moment m_out. Define

    M(L)=m_out+integral_L0^L F(s)ds.

This is exactly the signed physical inverse moment truncated at epsilon=exp(-L). Writing u=exp(-L), the near-edge Carleman integral becomes

    integral_L0^infinity F(s)/(1+exp(s-L))ds.

Its difference from M(L) is a convolution with

    k(z)=1/(1+exp z)-1_(z<=0),  |k(z)|<=exp(-|z|),

plus an O(exp(-L)) difference from the outer part. Extend F by zero below L0. Since (3) implies F in L2 and k belongs to L1 intersect L2, this difference B(L) belongs to L2(dL), hence to L2(dL/L) for L>=L0, and tends to zero as L tends to infinity. The latter follows from continuity and vanishing at infinity of the convolution of two L2 functions; one may prove it by compact-function approximation and Cauchy-Schwarz.

Equation (2), after u=exp(-L), gives Cf(exp(-L))-2A_h(0) in L2(dL/L). Thus M(L)-2A_h(0) has that same weighted integrability.

Finally use z=log L. The function

    N(z)=M(exp z)-2A_h(0)

belongs to L2(dz), and its weak derivative obeys

    integral |N'(z)|^2 dz
       =integral L |F(L)|^2 dL<infinity.

Therefore N is an H1 function on a half-line. Its continuous representative tends to zero at infinity: the usual one-dimensional tail inequality bounds |N(z)|^2 by twice the product of the L2 tails of N and N'. This proves M(L)->2A_h(0). Since B(L)->0, the same ordinary limit holds for Cf(exp(-L)).

No absolutely convergent infinite inverse sum is substituted, no exchange of divergent moments is taken, and no rate for N beyond its H1 tail conclusion is asserted.

## 4. Exact actual matching, without injectivity

The previous drive formula now gives the lawful relation

    integral_0^(2a) h(a-v)/v dv
       =2p_h(a)
          -2sum_(log n<2a) Lambda(n)/sqrt(n) h(a-log n)
          -2integral_0^(2a) k_reg(v)h(a-v)dv,

where the left integral means the signed improper limit just proved. Threshold-equality terms have limiting value h(-a)=0. All strict prime values are the actual continuous physical evaluations. This is not an assumed equality of a selected packet and a native vector.

The earlier rank-one inverse-moment observation remains noninjective on the general carrier. Its averaged quadratic identity required its own gap or absolute integrability hypotheses; this new signed convergence alone does not establish those hypotheses or justify reusing that identity. No inference M_R=0 -> h=0 is made.

The argument also cannot be advertised as distinguishing every critical positive eigenmode solely by zero normalization. If a native eigenmode satisfies Xcrit, its mass-subtracted residual q_h-mu h is likewise exterior-supported Ecrit and has the same exterior action. Such a vector has not been supplied by the existing rough positive controls. The current theorem uses exact full nullity as stated; the transverse bound alone proves neither its critical premise nor derivative regularity.

## 5. Matching is still weaker than derivative promotion

Take the previously audited compact supported cusp f(v)=v^(1/4)chi(v), with chi equal to one near zero. It is Xcrit and has finite positive inverse moment M. Assign a comparison drive A(u)=M/2 independently. Then

    Cf(u)-M=-u integral f(v)/[v(u+v)]dv=O(u^(1/4)).

The power estimate follows by scaling v=u y; integral y^(-3/4)/(1+y)dy is finite. This profile satisfies (1), the joint critical estimate and the exact matched limit, but its physical derivative is not L2.

This is a matched-cusp comparison, not the actual native A_h for that cusp and not an actual null solution. It disproves regularity-plus-profile-matching -> H1 when the remaining actual interior/source constraints are discarded. It does not disprove critical derivative promotion on K_a.

## Remaining theorem and standing

A joint estimate at the critical boundary threshold has now been obtained under actual critical membership, and a previously unjustified signed boundary limit is now lawful. Neither result supplies the critical positive-source moment on the full contact kernel. Neither yields an L2 derivative.

The remaining homogeneous gate is still K_a intersect Xcrit -> L2 derivative, now with the full-profile estimate, ordinary matched boundary limit, interior log gain and physical endpoint continuity available as proved inputs. The exact native equation must supply a stronger conclusion than the matched-cusp control. Alternatively the unresolved order-3/2 signed contact trace can exclude contact without this critical gate.

The accepted |beta_rho|<=3/8 input remains preserved. It controls the source transverse remainder but did not cause the physical critical matching theorem; the latter uses native multiplier growth, critical membership and the exact zero interior residual. No aperture marching, scalar injectivity, historical packet substitution or enlarged same-vector null transport.

Validation is analytic for difference-kernel equivalence, both boundary inequalities, the drive modulus, exponentially localized convolution and the H1 logarithmic-coordinate limit. No numerical inverse, new external theorem, Lean build, axiom audit or F4 claim. The preceding critical interior-gain result retains its pinned external boundary-theorem dependency. Canonical cursor and custody updated additively; certified 24/25 and newer 97/100 aperture work preserved. Endpoint exclusion, derivative promotion and FULL TRANSPORT CLOSED remain unproved.

## Pinned source custody

- notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_INTERIOR_GAIN_20261007.md, blob 05f53463842cb5aafbb5116c7f3a4bf65207400e.
- notes/REFLECTED_PACKET_BRIDGE_108_COMBINED_RIGHT_EDGE_DRIVE_20261007.md, blob 81851d107b65549dca965f656b92353df7ac0fe7.
- notes/REFLECTED_PACKET_BRIDGE_108_LOGARITHMIC_BOOTSTRAP_20261005.md, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028.
- notes/REFLECTED_PACKET_BRIDGE_108_INVERSE_MOMENT_OBSERVABILITY_AUDIT_20261005.md, blob 1c8b222f6365eaf88c065ad66e28b71be8b7fe15.
- notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_DERIVATIVE_PROMOTION_20261007.md, blob 26627f85c34572a8197b32a1216382e8d02e07f5.
- docs/TERMINOLOGY_RPB108_CRITICAL_INVERSE_TESTS.md, blob c3f80846c112325c2407215f0f9761c3dedd7ba6.
