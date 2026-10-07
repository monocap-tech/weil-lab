# RPB108: reciprocal boundary cancellation closes critical derivative promotion

Date: 2026-10-07 UTC. Recovered live head 80f60b52b18c6362baaa81769ed4f207d320f19f.
Definitions: [critical reciprocal promotion](../docs/TERMINOLOGY_RPB108_CRITICAL_RECIPROCAL_PROMOTION.md).
Category: critical derivative promotion / endpoint exclusion.
Analytic theorem using the previously pinned logarithmic boundary theorem. Not Lean-certified.

## Outcome

For the actual full-native kernel at every fixed finite aperture,

    K_a intersect Xcrit = K_a intersect H1(R).                 (1)

For h in this intersection, h' is the same global distribution as an element of K_a. The critical derivative-promotion gate is therefore analytically discharged.

The proof does NOT assume critical regularity of a generic forced inverse. Such a premise was refuted earlier and remains refuted. Instead a smooth-forcing inverse is bounded and has inverse-square-root-log boundary decay. Its exterior residual may grow like square-root-log; the critical physical Hardy tail of h makes the reciprocal boundary pairing vanish anyway. Exact full-nullity makes the pairing on the other side vanish.

Whole-contact-kernel critical membership remains unproved. Consequently no actual contact is excluded yet, no critical positive-source moment bound is claimed, and F4 is not assembled.

## 1. Bounded-forcing canonical solutions are bounded: actual jump semigroup proof

Suppose u in D_a solves q_u=f on I_a weakly, with f bounded. This step needs no nonnegativity of the full native form. Its pole p_u is bounded on the fixed interval by the already proved L2 moment bounds. Thus the pole-free Dirichlet equation is

    B_a u=F0,    F0=f-p_u in L2(I_a) intersect L-infinity(I_a). (2)

The equation in the supported form domain puts u in the operator domain of B_a. No global critical inverse regularity is assumed.

The exact Euler kernel gives, with w_n=Lambda(n)/sqrt(n),

    psi_a(xi)=m0(xi)-t_a(xi)-mu_a
      =2 integral_0^infinity k(s)[1-cos(2 pi xi s)]ds
         +2 sum w_n[1-cos(2 pi xi log n)] >=0,
    k(s)=exp(-s/2)/(1-exp(-2s)), mu_a=m0(0)-2 sum w_n.

This is the entire actual prime sum. The singular kernel is positive and has finite integral against min(1,s^2). Truncate k below s=delta. The resulting finite jump measure has a positive compound-Poisson convolution semigroup. Its Dirichlet restriction counts only paths whose vertices remain in I_a, so the positive exponential series gives domination by the free semigroup, for every finite truncation.

Here is the limit justification rather than an assumed native/full-line inversion. The nonnegative zero-extension energy forms of these truncated jump measures increase to the form of psi_a on D_a. For a fixed right-hand side, the minimizers of form_N(v)+||v||_2^2-2 Re<F,v> have bounded norms and energies. Every weak limit minimizes the limiting form: apply weak lower semicontinuity at each fixed truncation and then take the supremum. Uniqueness identifies the limit. The identity form_N(v_N)+||v_N||_2^2=Re<F,v_N> and the corresponding limiting identity imply norm convergence, hence strong resolvent convergence. Polynomial approximation in (1+B)^(-1) then gives strong semigroup convergence, because exp(-t lambda) is a continuous function of (1+lambda)^(-1) on [0,1], zero at zero. This also proves that the limit is the Dirichlet form operator, not a different boundary extension. Passing the finite-truncation domination along almost-everywhere convergent L2 subsequences preserves it.

The free limiting convolution is positive of mass one. At t>1/2 its Fourier transform exp(-t psi_a) is L2, since the native envelope |m0-w|<=C0 and bounded t_a give exp(-t psi_a)<=C_(a,t)(e+|xi|)^(-t). Its probability measure consequently has an L2 density H_t, by Plancherel. Therefore E_a(t)=exp(-t B_a) satisfies

    ||E_a(t)v||_infinity <= exp(-mu_a t)||H_t||_2 ||v||_2,
       t>1/2,
    ||E_a(s)F0||_infinity <= exp(-mu_a s)||F0||_infinity,
       s>=0.                                               (3)

The mass-one assertion can also be obtained directly from the finite jump measures: psi_a is continuous at zero and psi_a(0)=0, so the weak limit has total mass one. We do not invoke a positive semigroup for the full pole-added form.

Since u is in the operator domain in (2), the spectral theorem and integration of the semigroup derivative give, in L2,

    u=E_a(t)u+integral_0^t E_a(s)F0 ds.

Take t=1. Both terms are bounded by (3); the integral bound follows first for finite Riemann/Bochner sums and then by the L2 limit. Thus u is bounded. This proves the needed generic bounded-forcing fact without an aperture certificate, spectral sign or Xcrit inverse hypothesis.

## 2. The same inverse test has the precise boundary/exterior upper bounds

Use a smooth cutoff chi supported in a short endpoint interval and equal to one near that physical endpoint. The pinned actual commutator [m0(D),chi]:L2->H1 gives

    m0(D)(chi u)=chi(f+T_full u-p_u)+[m0(D),chi]u
       on that short interval.

All terms on the right are bounded: f and u are bounded, every frozen translation is bounded, the pole is smooth, and H1 embeds into bounded continuous functions in one dimension. The localized chi u is itself bounded. On an interval of length less than one, the already audited bounded transfer is

    m0(D)(chi u)=(1/2)L_Delta(chi u)+c0 chi u-k_reg*(chi u).

The pinned Theorem 1.1 of Hernandez-Santamaria, Lopez Rios and Saldana applies to this bounded zero-exterior weak solution with bounded forcing. The interval has uniform exterior sphere geometry. It yields, at both actual endpoints,

    |u(a-v)|+|u(-a+v)| <= C_u/sqrt(log(1/v)).                 (4)

Only this existing upper theorem is used, not a derivative or trace-classification theorem.

The exact exterior Euler/prime/pole action then gives the local bound

    |q_u(a+v)|+|q_u(-a-v)| <= C_u[1+sqrt(log(1/v))].          (5)

Indeed the singular piece is a Carleman integral. Near zero, split its integral at s=v. Below v the bound in (4) gives O(1/sqrt(log(1/v))); above v it is bounded by integral_v^b ds/[s sqrt(log(1/s))]=O(sqrt(log(1/v))). The outer part is bounded, as are the regular kernel, actual prime profiles and pole. Threshold-equality translations are included and still bounded. No absolute inverse moment of u is asserted. The same forced L2 boundary-removal argument read in the subcritical promotion note gives a global L2 multiplier representative; alternatively local pairings below only require the resulting locally L2 residual.

## 3. Critical full-null data used, and mollifier support custody

Now let h in K_a intersect Xcrit. The pinned joint matching theorem gives

    E_h(epsilon)->0,

and the continuous drive plus ordinary signed Carleman limit gives a continuous representative of q_h near each endpoint which equals zero at that endpoint and throughout I_a. Thus omega_h(epsilon)->0. These are conclusions of exact full-nullity and critical membership, not generic regularity premises.

Choose a fixed nonnegative real even smooth mollifier phi supported in (-1,1), integral one, and let h_epsilon=phi_epsilon*h. Its support is contained in [-a-epsilon,a+epsilon]. It is smooth compact. It is a changed test vector, not a same-vector enlarged-null transport.

The exact frozen multiplier and all finite translations commute with convolution and differentiation. The actual pole kernel is the Hermitian translation kernel 2 cosh((x-y)/2), with the pinned moment normalizations; convolution commutes with it locally as well. Therefore

    q_(h_epsilon')=(phi_epsilon*q_h)'.

All identities may be paired on a fixed compact interval containing these supports; compact pole extensions equal to the actual pole there give the same pairings. Exponential growth at infinity is not treated as a tempered Fourier multiplier.

Take any f in C_c^infinity(I_a) physically orthogonal to K_a. The actual Fredholm form provides u in D_a with q_u=f on I_a. Sections 1-2 apply to this u. No subtraction of a possibly unbounded kernel projection from f is needed: f itself is chosen in the finite-codimension orthogonal subspace.

Self-adjointness of the real frozen multiplier and Hermitian pole, with h_epsilon' a smooth compact test, gives the lawful exact reciprocal identity

    <q_(h_epsilon'),u> = <h_epsilon',q_u>.                  (6)

The u on the left is zero-extended. No support indicator is commuted through a critical multiplier and no unproved inverse pairing domain is used.

## 4. Both boundary errors vanish at the exact critical threshold

On the part of I_a more than epsilon from the endpoints, q_(h_epsilon')=0. On the remaining strips,

    |q_(h_epsilon')| <= ||phi'||_1 omega_h(epsilon)/epsilon.

Since u is bounded, the left side of (6) tends to zero, with upper bound C||u||_infinity omega_h(epsilon).

For the right side of (6), the interior part is

    integral_I h_epsilon' conjugate(f)
       =-integral_I h_epsilon conjugate(f')
       ->-<h,f'>,

because f is compact interior. The full exterior part must still be estimated; it is not discarded.

At the right endpoint put L_epsilon=log(1/epsilon) and let E_R(epsilon) be its Hardy tail. Cauchy-Schwarz gives

    integral_0^epsilon |h(a-v)|dv
       <= E_R(epsilon)^(1/2)
             (integral_0^epsilon v/log(1/v)dv)^(1/2)
       <= epsilon E_R(epsilon)^(1/2)/sqrt(2 L_epsilon).

Consequently, for 0<u<epsilon,

    |h_epsilon'(a+u)|
       <= C_phi E_R(epsilon)^(1/2)/(epsilon sqrt(L_epsilon)).

From sqrt(L+z)<=sqrt(L)+z/(2sqrt(L)), and integral_0^1 log(1/t)dt=1, we have

    integral_0^epsilon sqrt(log(1/u))du
       <= epsilon[sqrt(L_epsilon)+1/(2sqrt(L_epsilon))].

Combining this with (5) yields

    |integral_a^(a+epsilon) h_epsilon' conjugate(q_u)|
       <= C_(u,phi) E_R(epsilon)^(1/2) ->0.                (7)

Reflection handles the left strip. There are no other exterior contributions because h_epsilon' is compact in that enlarged collar. The square-root-log residual growth exactly cancels the square-root-log denominator supplied by the critical Hardy weight; the remaining tail tends to zero.

Equations (6)-(7) now prove

    <h,f'>=0 for every smooth compact f physically orthogonal to K_a. (8)

This is the new reciprocal cancellation estimate. It neither puts u in Xcrit nor assumes absolute inverse-moment integrability. The previous actual rough forced inverse, with its allowed inverse-square-root-log edge, is consistent with the proof and no longer blocks it.

## 5. Finite-codimension recovery and global endpoint removal

Let g=h' as a global distribution. Equation (8) says its interior action annihilates the kernel of the finite map f -> (<f,e_j>_2)_j for an L2 orthonormal basis of K_a. That map has rank dim K_a on smooth compact tests: otherwise a nonzero L2 kernel combination would vanish on all such tests. Elementary finite-dimensional annihilator algebra therefore identifies g on I_a with an L2 linear combination k of those e_j.

Both g and k are supported in [-a,a], and g belongs to Zcrit by h in Xcrit; L2 embeds in Zcrit. Their difference is supported at the two endpoints. No nonzero finite-point-supported distribution belongs to Zcrit: even a delta has divergent integral log(e+|xi|)/(1+|xi|), derivatives are worse, and distinct endpoint phases cannot cancel the leading diagonal contribution under frequency averaging. Thus g=k globally.

Hence h' is globally L2, h is H1, and its unchanged global derivative is in the actual K_a. The reverse inclusion H1 subset Xcrit is immediate from r log(e+|xi|)<=C(1+|xi|^2). This proves (1). The earlier supported-L2 derivative/domain promotion remains independently applicable; no spectral-domain assumption on the starting h was made.

## 6. Exact new endpoint gate, and controls

On actual K_a, finite critical positive-source height moment (order one) is now equivalent to H1, by the pinned critical source/Fourier comparison. H1 full-null vectors have lawful derivative-domain promotion and the previously derived order-two moment; intermediate positive orders follow. Thus the critical order joins the already unified supercritical finiteness locus.

If the whole hypothetical contact kernel has finite order-one positive-source trace, every vector is Xcrit and hence H1. Differentiation is then an endomorphism of the finite-dimensional kernel; the existing polynomial-Fourier independence argument forces K_a=0. The established first-contact dichotomy then supplies global all-window positivity if this whole-contact-kernel critical premise is proved at every possible contact. That arithmetic/source moment estimate is NOT proved here.

A hypothetical nonzero contact kernel must therefore have infinite critical positive-source trace. This is a conditional consequence, not existence of such a kernel and not divergence for every individual vector. An individual H1 null vector can coexist with a higher-dimensional rough kernel.

The positive-energy critical cusp control is not a contradiction: its full interior residual is nonzero, so the left side of (6) has an interior contribution instead of shrinking to a vanishing boundary strip. The existing rough positive eigenmode does not have a certified critical moment. We do not claim that the mechanism is an arithmetic sign inequality unique to eigenvalue zero: an eigenvalue-shifted homogeneous version would require the corresponding Fredholm and mass-subtracted residual inputs. No critical positive eigenmode or its impossibility is asserted here.

The accepted external |beta_rho|<=3/8 is preserved but is not what supplies this physical cancellation. It still controls transverse source corrections. Whole-contact critical membership, the alternative signed order-3/2 bound, global endpoint exclusion, retained historical packet attachment, same-vector enlarged-null transport and F4 remain open. No historical selected witness is identified with h or u.

## Custody, external dependency and validation

Read at the recovered head:

- CRITICAL_JOINT_MATCHING_20261007, blob 299cea4f1fe5b45b844c52a7912842f93d21dd9a.
- CRITICAL_INTERIOR_GAIN_20261007, blob 05f53463842cb5aafbb5116c7f3a4bf65207400e.
- SUBCRITICAL_DISTRIBUTIONAL_PROMOTION_20261007, blob 665a473edee975b2d346d0511a292e4a64cb56e8.
- LOGARITHMIC_BOOTSTRAP_20261005, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028.
- CRITICAL_INVERSE_TESTS_20261007, blob 0a5acc72749e39a54e92cbdc8c16337e81e36702.
- L2_NULL_DOMAIN_PROMOTION_20261006, blob b8ef9607e6823444a887ac71d8ec08bc21242510.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006, blob 955ff7b4bd0d7f58221c300a962a803824232fd6.
- POSITIVE_SOURCE_HEIGHT_MOMENT_20261006, blob 7997a0a3ccb0666d117f696dd208b743255b7ac5.

External input reread: Hernandez-Santamaria, Lopez Rios, Saldaña, arXiv:2401.18033v2 (3 July 2024), Theorem 1.1, https://arxiv.org/html/2401.18033v2, DOI 10.3934/dcds.2024084. Its hypotheses are bounded weak zero-exterior solution, bounded forcing, and uniform exterior sphere geometry. It supplies continuity and inverse-square-root-log upper decay only. The new reciprocal promotion theorem is not attributed to that paper. No external derivative theorem or imported semigroup domination theorem is assumed; the finite jump domination and resolvent/semigroup limit proof are given above.

Analytic audit: actual jump positivity including every prime, closed-form/operator domain identification, domination limit, boundedness before invoking the external theorem, exact residual matching, both reciprocal sides, full exterior support, critical Hardy tail, Hermitian pole differentiation and global finite-point removal. The companion rational/exponent check validates threshold calculations and a rejected loss-of-log budget. It does not certify the infinite-dimensional argument, arithmetic moment, or Lean.

No Lean/lake runtime is available in this mirror; no Lean build or axiom audit claimed. Historical notes stay immutable, with the critical gate closure added to the canonical cursor. Publication recovered newer head e8746a5cf6ed92bac69cda54a5a76ac773db66f8, where the independent aperture lane certified whole-domain positivity through 973/1000 (certificate note blob 6b79a6119e3b01cfbe7aa049b64f154f123cde2d). That complete prime-7 certificate and historical stronger 97/100 bounds are preserved; no certificate is recomputed here. No new aperture certificate, RH, F4 or FULL TRANSPORT CLOSED.
