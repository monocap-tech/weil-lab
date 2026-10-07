# RPB108: negative distributional promotion lowers the endpoint moment target

Date: 2026-10-07 UTC. Recovered live head 0f092bd6a21685dfdf95ff2108ebb784822e5e2c.
Definitions: [subcritical distributional promotion](../docs/TERMINOLOGY_RPB108_SUBCRITICAL_DISTRIBUTIONAL_PROMOTION.md).
Analytic closure of a regularity implication. No actual arithmetic moment bound or Lean certification.

## New conclusion

For 0<sigma<1/2, every distribution g in Y_-sigma supported in [-a,a] that satisfies the exact actual equation

    m_a(D)g+p_g=0 on (-a,a)

belongs to L2, D_a and the actual full-native kernel K_a. The proof uses the existing actual logarithmic Fredholm form, its inverse on the kernel complement and the subcritical fractional bootstrap with an inhomogeneous right side. It does not assume the proposed distribution is an L2 input.

Consequently for each 1/2<alpha<1,

    K_a intersect Y_alpha = K_a intersect H1.

For an actual full-null vector, finiteness of ANY positive source height moment of order 1<r<2 is therefore equivalent to global H1, and hence to the already identified order-two derivative/source criterion. The sufficient whole-kernel target drops from order two to any fixed order strictly greater than one.

The exact critical order-one premise remains outside this theorem.

## 1. Distributional domain and endpoint removal below one half

Write P=P_a, m_a=m0-t_a, T_a=t_a(D). The read fractional bootstrap gives P and [m0(D),P] bounded on Y_t for 0<t<1/2. By duality their bounds also hold on Y_-t: P is self-adjoint, while the commutator is skew-adjoint. Finite prime translations are bounded on every Y_t.

Choose delta>0 with sigma+delta<1/2. Logarithmic growth puts m0(D)g in Y_(-sigma-delta). Multiplication by P is bounded there. The distribution P(m_a(D)g+p_g) vanishes in the interior and outside the closed support; it is therefore supported at the endpoints. It lies in Y_(-sigma-delta).

No nonzero finite-point-supported distribution belongs to H^-t for t<1/2: derivatives of deltas have polynomial Fourier growth, and even a delta fails square integrability against (1+|xi|)^(-2t). For distinct endpoint phases, the diagonal leading term survives frequency averaging. Thus the endpoint-supported distribution is zero. The same argument gives Pg=g for the bounded extension of P to Y_-sigma.

The commutator identity, initially in Y_(-sigma-delta), now gives

    m0(D)g=P T_a g-P p_g+[m0(D),P]g.

Its right side belongs to Y_-sigma: the compact distribution's two pole moments are finite and P p_g is a cutoff smooth exponential, hence is L2. Therefore the full frozen multiplier m_a(D)g belongs to Y_-sigma as well. This supplies a lawful dual pairing domain, not yet an L2 derivative estimate.

## 2. Inhomogeneous subcritical regularity of inverse tests

Take a physical L2 orthonormal basis e_1,...,e_d of K_a. This is possible because the full form kernel is finite-dimensional. Each e_j belongs to Y_t for every t<1/2 by the existing actual bootstrap.

For f in C_c^infinity(-a,a), put F=f-Pi_K f. The physical projection makes F L2-orthogonal to K_a. The logarithmic form Riesz operator is self-adjoint I+compact. Its range is the logarithmic orthogonal complement of its kernel, and the functional v -> <F,v>_2 annihilates that kernel. Its inverse on that complement therefore supplies a canonical-domain u satisfying

    Q_a(u,v)=<F,v>_2 for every v in D_a.

No inverse of a singular whole form is taken. The forcing F is in every Y_t with t<1/2.

The L2 boundary-removal argument extends to this forced equation: on the interior the multiplier representative is F-p_u, and outside it is the existing L2 Carleman/finite-prime expression. Its endpoint defect is removed exactly as for supported-L2 null promotion. Thus m_a(D)u is globally L2.

The capped-weight bootstrap now has the extra term P F=F:

    m0(D)u=P T_a u-P p_u+[m0(D),P]u+F.

At any fixed 0<t<1/2 its norm estimate is

    ||rho_M m0 uhat||_2 <= B_t ||rho_M uhat||_2
                          +F_(a,t)||u||_2+||F||_(Y_t),

with the SAME B_t and uniformly capped rho_M from the read fractional proof. The high-frequency absorption still has coefficient B_t/[2(B_t+1)]<1/2; the forcing adds a finite constant independent of M. Hence u and m_a(D)u belong to Y_t. In particular choose sigma<t<1/2 to obtain the dual regularity needed below.

## 3. Testing the negative distribution against the inverse

Supported u in Y_t, t>sigma, can be approximated by C_c^infinity(-a,a) in Y_sigma. To see the support custody directly, shrink u by a dilation with factor tending to one, which converges in Y_t and puts support strictly inside the interval, then mollify inside that margin. These approximating tests are only a proof device: the physical vector in the conclusion is unchanged.

The distribution q_g=m_a(D)g+p_g annihilates all those interior tests. For supported tests use P p_g in the pairing; it is L2. The multiplier is in Y_-sigma, so the pairing is continuous in Y_sigma. Therefore

    <m_a(D)g,u>+<p_g,u>=0.

The real frozen multiplier and the actual Hermitian pole pairing give, by Fourier duality and the exact pole moments,

    <g,m_a(D)u+P p_u>=0.

The inverse equation gives P(m_a(D)u+p_u)=F. Both sides belong to Y_sigma, and the support projection is bounded there. Since Pg=g, the exterior part cannot contribute. Thus <g,F>=0.

For every interior smooth f this is <g,f-Pi_K f>=0. Writing the physical projection in the basis e_j shows g equals an L2 linear combination of e_j on the interior. The difference is supported at the endpoints and belongs to Y_-sigma, so step 1 removes it. Consequently g is the SAME global distribution as an element of K_a. This proves promotion without assuming spectral regularity of g.

## 4. Derivative and actual source consequences

Let h in K_a belong to Y_alpha, 1/2<alpha<1. Its global derivative g=h' is supported in [-a,a] and belongs to Y_(alpha-1). Distributional differentiation commutes with the frozen multiplier and the pole moments, with

    M_-(h')=M_-(h)/2,   M_+(h')=-M_+(h)/2.

The exact differentiated interior equation holds. Apply the theorem with sigma=1-alpha<1/2: g belongs to K_a and L2. Hence h is globally H1. Conversely H1 is contained in Y_alpha. This proves the displayed equality.

The read actual source/Fourier equivalence for 0<s<1 gives finite source order r=2s>1 -> h in Y_s -> H1. For h in actual K_a intersect H1, the existing supported-L2 derivative promotion puts h' in D_a; the earlier order-two source theorem then makes its order-two moment finite, and every lower moment follows by adding base source energy. Thus all orders 1<r<=2 have the same finiteness locus on K_a. This statement is restricted to actual full-null vectors; it is false for unrestricted supported functions, including the cusp control from the preceding pass.

If the whole hypothetical contact kernel has a finite actual positive source trace of any fixed order 1<r<2, it lies in H1. Differentiation is then an endomorphism of the finite-dimensional kernel. Iteration and Fourier-polynomial independence exclude every nonzero vector. This closes a sufficient implication; the arithmetic trace estimate itself is unproved.

Equivalently, a nonzero contact kernel forces an infinite positive trace at every order r>1. Individual regular vectors may remain in a larger kernel; the whole-kernel quantifier is essential.

## Exact remaining boundary and dependency graph

    actual order r>1 trace bound on whole K
        -> whole K in Y_(r/2)
        -> negative distributional derivative promotion
        -> whole K in H1
        -> derivative endomorphism + finite dimension
        -> no contact
        -> global all-window positivity by established dichotomy.

The first node remains an actual arithmetic obligation. Existing source orders r<1 do not reach it. At r=1 the derivative belongs to the critical negative space, where bounded support projection, the duality domain and the test approximation argument used above are not supplied. No critical-limit assertion is made.

This is endpoint exclusion, not prescribed retained attachment or same-vector enlarged null transport. No historical P,C,k is replaced. No full-native vector is dilated in a transport conclusion. The conditional nonpersistence results and F4 entry audit retain their existing scope.

## Source custody and validation

Pinned reads at the recovered head:
- FRACTIONAL_NULL_REGULARITY_20261005, blob f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff: support projection/commutator bounds, capped absorption and actual kernel Y_t regularity.
- LOGARITHMIC_BOOTSTRAP_20261005, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028: exact frozen multiplier, finite prime set, Hermitian pole and commutator identity.
- NATIVE_MASS_CONTACT_20261006, blob 65b45b856fdb33014f9dee0468d0cf75ff413539: actual logarithmic form Fredholm kernel and physical eigenvalue custody.
- L2_NULL_DOMAIN_PROMOTION_20261006, blob b8ef9607e6823444a887ac71d8ec08bc21242510: global L2 exterior candidate, endpoint removal and derivative signs.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006 and POSITIVE_SOURCE_HEIGHT_MOMENT_20261006: complete actual source normalization and moment equivalences.
- CRITICAL_DERIVATIVE_PROMOTION_20261007: critical boundary retained additively.

Validation is analytic: both negative-space endpoint removals, forced inverse solvability, forced capped absorption, two supported dual pairings and the derivative threshold are given explicitly. Existing fractional and critical rational controls are rerun only as regression controls; they do not certify this theorem. No new numerical certificate or aperture calculation. No Lean build, axiom audit or CI claim. Certified 24/25 whole-domain frontier preserved. Actual arithmetic endpoint exclusion, historical retained attachment, enlarged full-null transport, F4 and FULL TRANSPORT CLOSED remain open.
