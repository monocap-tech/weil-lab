# RPB108: sharp zero-sum and Sonine framework obstructions

Date: 2026-10-07 UTC. Recovered and rechecked live head 1b42e0a5f400225f607e2412a2b66e48bf7491de.
Definitions: [sharp arithmetic framework audit](../docs/TERMINOLOGY_RPB108_SHARP_ARITHMETIC_FRAMEWORK_AUDIT.md).
Publication recovery: the aperture lane advanced to 83278548b6090c43a05debf154c67e828876c0f2 while this audit was running, publishing positivity through 99/100. Its current cursor and tree are preserved as the publication base; no aperture proof was recomputed here.
Category: signed sharp-head arithmetic / candidate-specific obstructions. Analytic; not Lean-certified.

## Result and scope

No actual bounded-return mechanism or checked external reduction was found in the audited Landau-Gonek, Burnol, Suzuki and Connes-Consani results. Two direct routes have rigorous obstructions: pointwise zero-sum asymptotics cannot be paired with the rough autocorrelation without a uniform critical error estimate, and the direct compact logarithmic lift cannot be a nonzero Sonine vector. Completeness of linear zero evaluators does not turn the actual mixed Gram radical into simultaneous zero evaluations.

The established implication remains

    actual full nullity -> unsigned tail O(1/T)
      -> bounded Abel-minus-sharp error
      -> S_K(T)/log T -> (2/pi)Lambda_K.

For K nonzero, Lambda_K>0. The missing arithmetic arrow remains

    actual source-range FULL UNSHIFTED mixed-nullity
      -> liminf S_K(T)/log T<=0.

It is unproved. The dependency graph does not shorten. This audit does not restart endpoint regularity, compactness, Abel transfer, aperture calculations or historical packet attachment.

## 1. Exact finite arithmetic pairing

In the registered raw convention,

    p_rho(h)=integral h(x) exp(i theta x) cosh(beta x) dx,
    n_rho(h)=integral h(x) exp(i theta x) sinh(beta x) dx.

Expanding their squared norms and using the hyperbolic subtraction identity gives exactly

    |p_rho(h)|^2-|n_rho(h)|^2
      =integral C_h(u) exp(i theta u) cosh(beta u) du.

Here C_h(u)=integral h(y+u) conjugate(h(y))dy. Compact supported L2 implies L1; hence finite Fubini is valid. Translation continuity gives C_h continuous, and compact support gives integrability. Summing the finite actual zero head proves the registered S_K pairing. No rough infinite explicit-formula interchange is used.

The transverse reflection beta -> -beta leaves each signed diagonal unchanged: p is unchanged and n changes sign. It doubles, rather than cancels, matched reflected contributions. For real h, the theta-reflected contribution is also equal. On beta=0 the contribution is nonnegative. Thus functional-equation symmetry alone supplies no opposite-sign pairing. These statements retain multiplicities and apply equally to the actual rough positive eigenmode.

## 2. Landau-Gonek: the critical pairing is not a fixed-frequency theorem

Primary source: Farzad Aryan, [On an extension of the Landau-Gonek formula](https://arxiv.org/pdf/1902.05473), arXiv:1902.05473v1, introduction and Theorem 1.1. The introduction records Landau's fixed x>1 formula sum_(0<Im rho<T) x^rho=-(T/2pi)Lambda(x)+O_x(log T), and explains weighted Dirichlet-polynomial applications. Theorem 1.1 has Gaussian zero-pair weighting and rational x=r/s of restricted size. It is not the present unsmoothed quadratic head for an arbitrary rough supported L2 vector.

The exponentials in section 1 do connect to x^rho at x=exp(u), after the half-line normalization and actual reflection symmetry. However, u=0 and prime-power frequencies are singular in the limiting distribution; the current test is a continuum autocorrelation, not a finite Dirichlet polynomial. Even at a fixed nonzero nonsingular u, multiplying a partial sum by ordinate via partial summation turns an O_u(log T) remainder into an O_u(T log T) budget. This budget cannot supply o(log T) for its integral against C_K. A uniform formula may be useful, but its error must actually be checked after this rough pairing and after full-null cancellation. The cited theorem does not perform that step.

Precise pointwise-to-pairing obstruction: put phi(v)=(1-|v|)_+, whose integral is one, and R_T(u)=T log T phi(Tu), T>1. For each fixed u!=0, R_T(u) is eventually zero. Nevertheless for every continuous compact C,

    integral C(u)R_T(u)du / log T
       =integral C(v/T)phi(v)dv -> C(0).

For C_K, this is dim K, strictly positive for K nonzero. Either sign is obtained by replacing R_T by -R_T. This is an artificial remainder control, not a claim about the actual zero kernel. It rigorously rejects the inference from pointwise oscillation/errors away from the diagonal to the needed rough-test bound. The O(1/T) source tail controls Abel-minus-sharp, not this proposed zero-kernel remainder.

Almost-periodic oscillation in u likewise does not imply returns in the cutoff T: the phases already occur inside a fixed quadratic weight, and changing T adds terms rather than translating u. No almost-periodicity or Littlewood-type theorem was found here with hypotheses covering this signed weight and unshifted null equation. This is a statement about the results audited, not a nonexistence theorem about all literature.

## 3. Burnol: a direct source-range attachment is impossible

Primary source: Jean-Francois Burnol, [Two complete and minimal systems associated with the zeros of the Riemann zeta function](https://arxiv.org/pdf/math/0203120), arXiv:math/0203120v7; sections 2-3, Theorems 3.1-3.3. L_lambda requires both f and its cosine transform constant on (0,lambda); the Sonine subspace requires both zero there. Zero derivative evaluators are complete in L_lambda exactly for lambda>=1. At lambda<1 their orthogonal complement is the co-Poisson subspace. At lambda=1, zeta(s)/(s-rho)^l forms a complete minimal system in the Mellin-transform space, with triangular evaluator duals. These are linear evaluation statements on specified Mellin/cosine-gap carriers.

The natural lift U is genuinely isometric:

    integral_0^infinity |U h(t)|^2dt=integral_R |h(x)|^2dx,
    Mellin(U h)(s)=integral h(x)exp((1/2-s)x)dx.

Its support is [exp(-a),exp(a)]. Its cosine transform

    2 integral_0^infinity U h(t) cos(2pi tz)dt

is entire in z, because U h is compact and L1. If it were constant on any nonempty real interval, the identity theorem would make it constant everywhere. Riemann-Lebesgue on the real axis makes that constant zero; cosine-transform injectivity then gives h=0. Consequently

    U(D_a) intersect L_lambda={0} for every lambda>0,

and the same holds for the Sonine subspace. This excludes DIRECT identification for every nonzero actual physical vector, including the shifted eigenmode. It does not exclude a nonlocal transformation producing noncompact tails.

Co-Poisson transformations cannot be silently substituted: their Mellin formula contains a zeta factor, so zero evaluations may vanish by construction while the original actual source samples do not vanish. To use completeness for exclusion one would need a proved injective nonlocal map into the appropriate complete-system carrier that sends the exact UNSHIFTED mixed-null equation to orthogonality to all its zero derivative evaluators, with multiplicities and normalization checked. No such map is supplied by the cited completeness theorem or current repository. A gap parameter below one would also leave the stated co-Poisson complement. This identifies the attachment needed for this candidate framework; it does not replace the global arithmetic gate by an established theorem.

## 4. Linear completeness is not mixed-null orthogonality

For the actual closed complete analysis range V=Ran Gamma, full nullity says

    J Gamma h perpendicular to V,

not Gamma h=0 and not that every scalar zero evaluator annihilates h. The existing positive observability is injective, but its use does not erase the negative channel.

A finite exact control makes the logical distinction explicit. On C^r take Gamma v=(v,v) and J=diag(I,-I). Both coordinate families are complete and Gamma is injective, yet Gamma*J Gamma=0 on every vector. Assign heights 2 to the positive slots and 1 to the negative slots: for T>=2 the signed first-height trace of any unit vector is 1. Interchanging heights makes it -1. This is an abstract mixed-range control, not actual zeros; it proves that injectivity/completeness and mixed-null orthogonality alone give no sharp-head sign. A valid actual range theorem must use more than these properties.

## 5. Positive models and trace formulas: hypotheses stop short

Primary source: Masatoshi Suzuki, [A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/pdf/1204.1827), Proposition 1.2. For omega0>0, zero-freeness in Re s>1/2+omega0 is equivalent to meromorphic innerness of Theta_omega for EVERY omega>omega0. The accepted seven-eighths theorem therefore supplies inner models for omega>3/8. It does not supply the entire family down to omega=0. Importing that family would demand stronger zero-freeness. Nor is a fixed shifted model identified with the present unshifted physical source graph or its height-weighted sharp trace.

Primary source: Alain Connes and Caterina Consani, [Weil positivity and Trace formula, the archimedean place](https://arxiv.org/pdf/2006.13771), Theorem 1 and Corollary 2. The theorem treats smooth multiplicative tests supported in [2^(-1/2),2^(1/2)] with specified transform vanishing. Corollary 2 includes an extra c|g-hat(0)|^2 contribution. These carrier/support/vanishing hypotheses are not consequences of full nullity at an arbitrary contact. The theorem gives no sign statement for the critical sharp ordinate-weighted trace at issue. Its small support is already inside the certified physical frontier after taking logarithms.

No trace/index cancellation was imported. On a nonzero kernel the signed first-height sum already diverges logarithmically and the unsigned first-height moment is infinite. An ordinary absolutely trace-class height compression is therefore unavailable. A regularized commutator trace could still be meaningful, but a lawful full-graph identity with a forced sign/vanishing has not been exhibited. The existing bounded-cutoff graph identity remains valid and its error sign remains open.

## 6. Four required controls

| Control | What this audit must preserve |
|---|---|
| Rough actual positive eigenmode | Same actual zeros, symmetries, source range, finite pairing, weak tail and strictly positive sharp/log limit. The interior equation has residual mu h!=0. Every argument ignoring that residual fails to distinguish it. No bounded-return claim is made for it. |
| Artificial compact-good-row logarithmic vector | Positive slope despite compact good rows and strong density. It is not the actual divisor and does not satisfy actual full nullity. The diagonal spike and finite completeness controls above are also explicitly artificial. |
| Fixed finite actual restoration | For each fixed physical kernel basis, finitely many first-height terms contribute O(1); division by log T gives zero. Such restoration cannot remove the terminal coefficient or prove the missing arithmetic sign. |
| Two-row comparison contact | Exact derivative-chain contact geometry survives with auxiliary smooth rows. Those rows are not the actual divisor. No actual Landau/source-range attachment is inferred from this geometry. |

## 7. Custody and validation

Internal dependencies, with verified Git blob pins, are recorded in the companion JSON: actual sharp/log limit, actual null Abel slope and eigenmode extension, compact-good logarithmic control, two-row comparison contact, and complete source-graph error. The companion script checks polynomial source-pair cancellation, the continuum diagonal spike on nonconstant tests, exact mixed-range controls of both signs, and finite-restoration normalization budgets. These checks validate the obstructions, not an actual arithmetic theorem. The infinite Sonine exclusion follows from the analytic proof above; it is not asserted as numerically certified.

Historical wording/certificates remain unchanged. No new aperture estimate, Lean morphology or axiom claim is introduced. Actual endpoint exclusion, historical transport and F4 remain open. The exact outstanding implication is still actual source-range unshifted nullity -> bounded/sublogarithmic sharp subsequence (or nonpositive sharp/log liminf).
