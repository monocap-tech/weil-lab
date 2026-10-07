# RPB108: attach the actual operator to the exterior logarithmic Laplacian

Date: 2026-10-07 UTC. Recovered live head 6cc48df565bb30f3859256932ccf1292ccb737a2 and the canonical cursor.
Definitions: [actual logarithmic-operator attachment](../docs/TERMINOLOGY_RPB108_ACTUAL_LOG_OPERATOR_ATTACHMENT.md).
Category: structural compatibility development following the outside-zeta audit. Analytic, not Lean-certified.

## Result

For EVERY fixed finite actual window I_a, the full native form and its physical operator satisfy

    Q_a(u,v)=(1/2)E_L,a(u,v)+<B_a u,v>,
    A_a=(1/2)L_a+B_a,
    dom(A_a)=dom(L_a).

The same supported physical vector and canonical form domain are retained. The complete actual prime/pole correction is explicit and bounded on physical L2. This extends the existing small-window forced-inverse comparison to all fixed windows, with all frozen primes and exact operator-domain custody. It supplies an ACTUAL interface to the closest external operator, not another regularity investigation.

The immediate research consequence is concrete: in this direct comparison the actual arithmetic selects spectral position through a bounded correction inside a common domain. It does not select a different boundary extension of the same interior expression. Boundary-domain exclusion therefore needs an extra null-specific equation; the generic shared logarithmic endpoint scale does not encode the selection.

## 1. Exact complete correction, including long distances

Use angular Fourier frequency eta and the native physical Euler identity already pinned:

    E0(u)=m00||u||_2^2+integral_0^infinity k(s)||tau_s u-u||_2^2 ds,
    k(s)=exp(-s/2)/(1-exp(-2s)).

Let rho_1 be the constant in the one-dimensional physical logarithmic-Laplacian formula. [Chen-Weth, arXiv:1710.03416, Theorem 1.1 and the form preceding Theorem 1.4](https://arxiv.org/pdf/1710.03416) give

    (1/2)L_Delta u(x)
       =(1/2) integral_(|x-y|<1) [u(x)-u(y)]/|x-y| dy
        -(1/2) integral_(|x-y|>=1) u(y)/|x-y| dy
        +(rho_1/2)u(x).

Its supported form carrier is the zero-extended logarithmic difference-energy space. Define

    j(s)=k(s)-1/(2s), s>0, j(0)=1/4,
    c0=m00-rho_1/2
          +2 integral_0^1 j(s)ds+2 integral_1^infinity k(s)ds.

The small-s expansion and exponential decay of k make c0 finite. j is continuous and bounded on every [0,2a]; for s>=1 its formula still subtracts 1/(2s), not zero. Pairing the two physical representations first on supported smooth tests gives

    m0(D)u=(1/2)L_Delta u+c0 u
                         -integral_Ia j(|x-y|)u(y)dy

ON I_a. The near diagonal has an integrable remainder. The multiplier mass terms use the integrals defining c0; the long-distance convolution subtracts the external 1/(2s) tail too. There is no omitted outer residual or use of full-line nullity.

Write J_a for that integral operator, P_a for the exact kernel 2cosh((x-y)/2), and

    T_a u(x)=sum_(log n<=2a) Lambda(n)/sqrt(n)
                       [u(x-log n)+u(x+log n)],
    B_a=c0 I-J_a-T_a+P_a.

Zero extension is understood before every translation. Threshold equalities remain in the frozen dictionary. The identity above and the full native prime/pole signs give the asserted mixed form formula by polarization. The actual source-analysis Gamma_a is unchanged; no continuous Fourier source model replaces it.

## 2. Boundedness and domain attachment

Let j_a=max_(0<=s<=2a)|j(s)| and S_a=2sum_(log n<=2a) Lambda(n)/sqrt(n). Schur and translation bounds give

    ||J_a||_2 <= 2a j_a,
    ||T_a||_2 <= S_a,
    ||P_a||_2 <= 4a cosh(a),
    ||B_a||_2 <= |c0|+2a j_a+S_a+4a cosh(a).

These are qualitative finite budgets; no new aperture estimate or sign certificate is computed. J_a is self-adjoint Hilbert-Schmidt. Compressed opposite translations are adjoints, so T_a is self-adjoint. The symmetric pole is self-adjoint of rank at most two: 2cosh((x-y)/2)=2cosh(x/2)cosh(y/2)-2sinh(x/2)sinh(y/2). A pointwise positive pole kernel is not asserted a nonnegative quadratic operator. Each displayed norm bound also holds on supported L-infinity with the same constants.

The native logarithmic carrier and external supported carrier agree with equivalent energy-plus-mass norms. One direct check uses their identical local 1/(2s) singularity and the bounded form difference just calculated. Alternatively the external local difference symbol has logarithmic high-frequency growth, while its low-frequency part is mass bounded. The canonical native logarithmic norm supplies the same growth. Smooth compact interior tests are a common dense form core on an interval; the exact identity consequently extends to every supported canonical pair.

Operator-domain equality now follows directly from the definition of the associated operator, without any presumed global multiplier domain. For u in the common form domain,

    Q_a(u,v)=<f,v> for all v in D_a
       iff E_L,a(u,v)=<2(f-B_a u),v> for all v in D_a.

Since B_a u is physical L2, the left representation exists iff the right one does. This proves dom(A_a)=dom(L_a) and A_a u=L_a u/2+B_a u. The graph norms are equivalent as well: either action norm is bounded by twice the other plus a fixed multiple of ||u||_2. Every actual full mixed-null vector is in this operator domain by its zero representing vector. This is an interior supported operator statement, not enlarged cancellation.

## 3. Where the null-specific compatibility now sits

For the actual full K_a,

    L_a h=-2B_a h
       =-2c0 h+2J_a h+2T_a h-2P_a h.

For the actual physical positive eigenmode the SAME attachment gives

    L_a h=2(mu h-B_a h).

No term is dropped because it is bounded or lower order. On the bounded actual eigen/null vectors already established, B_a h is bounded, so both right-hand sides are bounded. This explains why the external boundary scale is shared: the logarithmic principal operator sees bounded forcing in both cases. It does not show that either trace vanishes.

The direct external attachment therefore replaces a conjectural domain-selection picture by an exact operator compatibility problem. The prime translations and pole can move the energy while retaining the carrier and domain. Shifting A_a by mu simply replaces B_a by B_a-mu I, with that same domain. Thus a boundary condition possessed by EVERY vector of the common operator domain cannot reject our rough positive eigenmode while holding for a null vector merely because its eigenvalue is zero.

A valid distinguishing statement must use the specific equation with the actual B_a, or an actual source-range identity equivalent to it, and keep the mu residual when testing the positive control. This identifies where to develop a compatibility theorem; it does not provide one by nomenclature. In particular, no positivity-preserving semigroup, principal-eigenfunction sign, Hopf conclusion for the entire native operator, or sign of B_a is inferred. Actual prime/pole interactions need not satisfy the external comparison hypotheses.

This is NOT a new reformulation claimed to discharge the global arithmetic gate. The actual sharp/log theorem is unchanged. What is closed is the all-window attachment of the closest outside operator and the location of the correction in a common domain. The global route still needs actual unshifted full-null source range -> nonpositive signed sharp/log liminf.

## 4. Controls, source custody and standing

| Control | Attachment audit |
|---|---|
| Actual rough positive eigenmode | Same domain, same complete B_a, exact residual 2mu h retained. It rejects null-exclusive conclusions based only on the common boundary domain. |
| Artificial compact-good rows and NF37 chain form | They may be bounded perturbations too, but their corrections are not this actual prime/pole operator. No source-range identification is inferred. |
| Fixed finite actual source restoration | Its normalized sharp change remains o(1). The operator identity already uses the complete native form; any artificial source modification requires its own correction and cannot be silently absorbed. |
| Two-row comparison contact | Its auxiliary rows change the correction operator and spectral compatibility. Same logarithmic leading scale does not make its null equation actual. |

The manifest pins the Euler/native dictionary, prior small-window comparison, all-window physical remainder and the outside audit. Rational tests check cutoff-mass cancellation, compressed opposite-shift adjointness, the pole's rank-two algebra and the retained eigenvalue residual. They audit algebra, not infinite-dimensional domain equivalence or a sign theorem.

The logarithmic-Laplacian integral/form normalization is an inspected primary analytic input. The extension from the earlier small-window formula, bounded-correction proof and exact domain attachment are proved here. No Lean build or axiom closure, new endpoint regularity or compactness investigation, aperture marching, historical attachment or F4 closure is asserted. The concurrent 0.995 native/source milestone and historical wording remain intact.
