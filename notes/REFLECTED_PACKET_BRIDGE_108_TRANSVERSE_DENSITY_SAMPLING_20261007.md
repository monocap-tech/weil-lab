# RPB108: actual zero-density gain for weighted negative observations

Date: 2026-10-07 UTC. Recovered live head 6e1ed1631e54388120ffe65b3e7b90f71ea8a3da.
Definitions: [transverse count and weighted negative sampling](../docs/TERMINOLOGY_RPB108_TRANSVERSE_DENSITY_SAMPLING.md).
Category: endpoint exclusion / arithmetic input scope. Analytic external density input; no new critical source bound or Lean certification.

## Actual arithmetic result

The published uniform near-line zero-density estimate, combined with the already accepted |beta_rho|<=3/8 strip and functional symmetry, gives

    Z2(T)<<T (log log T)^2/log T.                       (1)

Consequently, for every fixed a and eta>0, the actual weighted negative observation operator Nminus_eta on physical L2(-a,a) is Hilbert-Schmidt and compact:

    sum_actual_copies beta_rho^2 /
       [(1+|theta_rho|)log(e+|theta_rho|)^eta] < infinity. (2)

This is a genuine arithmetic gain for the actual divisor-location measure and a lawful actual negative operator extension with the stated weights. It applies to ALL supported physical L2 vectors, including the rough positive eigenmode. It does not distinguish a hypothetical zero kernel or supply its critical positive-source moment.

The proposed route from global off-line sparsity to unweighted negative compactness or a critical source-height bound therefore remains unclosed. In particular global density is not a uniform local counting estimate at each large height.

## 1. Primary external source and scope

Read primary source: Shashi Chourasiya and Aleksander Simonic, An explicit form of Ingham's zero density estimate, arXiv:2507.15184v2, 30 September 2025, Corollary 1 and the following bound:

https://arxiv.org/html/2507.15184v2

For T>=3*10^12 and 1/2<=sigma<=5/8 the paper gives

    N(sigma,T)<=8.185 T^[3(1-sigma)/(2-sigma)]
                        (log T)^[(7-5sigma)/(2-sigma)]
                +9.461(log T)^2+167.8 log T.           (3)

The same source records total counting N(T) asymptotic to T log T/(2 pi). We only need the resulting O(T log T) bound. Multiplicities are counted, not discarded. We import these published analytic statements without a local proof rebuild or Lean axiom audit. No numerical first-contact certification is inferred from their constants.

## 2. Derivation of the transverse second-count gain

For sufficiently large T set L=log T and delta=3 log L/L, so 0<delta<=1/8. Split Z2 into |beta|<=delta and its complement. The first part is at most delta^2 times the total actual zero count, hence O(T (log L)^2/L).

Functional symmetry reflects left-side zeros to right-side zeros with their multiplicities; conjugation handles both ordinate signs. Thus the count in the second part is bounded by a fixed multiple of N(1/2+delta,T). The accepted strip makes every squared displacement at most (3/8)^2.

For sigma=1/2+delta, the density exponent obeys

    3(1-sigma)/(2-sigma)
       =1-2 delta/(3/2-delta)<=1-(4/3)delta.

The logarithmic exponent in (3) is at most 3 on this interval. Therefore its first term is at most

    8.185 T exp(-(4/3)delta L)L^3=8.185 T/L.

The two additive logarithmic terms are asymptotically absorbed into O(T/L). The far transverse contribution is O(T/L), dominated by the near contribution. This proves (1). Low heights contain only finitely many copies and do not affect the asymptotic conclusion.

This is an averaged SECOND transverse count. It does not assert a pointwise decay of beta_rho, RH above a height, or a local upper bound on the off-line count in every unit interval.

## 3. Weighted actual negative analysis on physical L2

From the pinned raw-coordinate convention,

    n_rho(h)=integral h(x) exp(i theta_rho x)sinh(beta_rho x)dx.

The L2 observation norm equals ||sinh(beta_rho x)||_L2(-a,a). Since |sinh(beta x)|<=|beta x| exp(|beta x|) and |beta|<=3/8,

    ||n_rho||_(L2->C)^2
          <=beta_rho^2 exp(3a/4)*(2a^3/3).            (4)

The theta phase is unit modulus. This tracks the actual profiles and physical adjoint metric; no logarithmic Riesz representative is substituted.

Divide these squared norms by the denominator in (2). For dyadic large heights 2^j<=|theta|<2^(j+1), (1) bounds the block sum by a fixed multiple of

    (log j)^2/j^(1+eta).

That series is summable for every eta>0. Finitely many low-height copies contribute finite norms. Summing (4) proves Hilbert-Schmidt boundedness of Nminus_eta, including convergence of the actual coordinate series for every supported physical L2 vector. Finite-row truncations converge in operator norm, with tail bound given by the omitted Hilbert-Schmidt norm. This establishes compactness of THIS weighted operator.

An asymptotic squared tail bound is O((log log T)^2/(log T)^eta), obtained by the corresponding integral test. Constants depend on fixed support and eta; no explicit optimized constant or aperture certificate is claimed.

The inverse-height weight is essential to the conclusion established here. It suppresses large ordinates. The required endpoint quantity instead multiplies the POSITIVE observation energy by |theta|. Inverting a compact weighted observation operator does not provide that estimate.

## 4. Borderline control and the failed local inference

Removing the positive log saving gives the block majorant (log j)^2/j, which is not summable. That failure of this upper bound is not a proof that the ACTUAL borderline operator fails to be Hilbert-Schmidt.

An artificial location measure shows why the available counting information alone cannot settle the borderline. For each j>=3, take j copies at every integer height in [2^j,2^(j+1)), with displacement beta=1/j. Add reflected/sign partners if desired; these only change a fixed factor. Then |beta|<=1/3<3/8, the unit-interval count is O(log height), total count is O(T log T), and the second transverse count is O(T/log T), stronger than (1).

Each block has second displacement sum 2^j/j. After inverse-height weighting, its sum is at least 1/(3j), so the eta=0 location series diverges. For eta>0 its blocks are O(j^(-1-eta)), hence summable. On any nonzero support interval, ||sinh(beta x)||_2^2>=beta^2*(2a^3/3), so the analogous artificial observation family also fails the borderline Hilbert-Schmidt test. These are artificial locations; no zeta divisor, explicit formula, source positivity or native null equation is claimed. They control ONLY the inference from the specified location statistics.

Likewise a cumulative density bound does not by itself force the unit-interval count to be o(log T) at EVERY T. Sparse high-height clusters are compatible with sublinear cumulative bounds for zeros at a fixed transverse distance. Thus the attempted operator-norm compactness of UNWEIGHTED N0 cannot be obtained by silently replacing an averaged count with a local sampling bound. No actual cluster or noncompactness counterexample is asserted.

## 5. Endpoint implication audit

The gain (1)-(2) holds for the same actual rough positive eigenmode at 24/25 whose critical positive-source moment diverges. It is therefore not a zero-specific regularity estimate. Weighted negative compactness plus finite kernel cannot be used to discard the complete graph error isolated in the preceding source-height audit.

Exact failed closure: actual global density + |beta|<=3/8 -> the required critical positive moment or uniform signed first-height head via negative-source smoothing. The derived theorem only controls inverse-height WEIGHTED negative observations; the critical signed/positive quantity lies on the opposite side of that weight. No implication upgrading those weights is proved.

The smallest remaining theorem remains the actual zero-contact signed graph-error upper bound (or its Abel/critical-positive equivalent). For this new density route, an additional lawful actual source inequality must transfer the proved negative weighted count into that critical signed quantity. Such an inequality would have to fail on the pinned positive eigenmode; none is supplied here. Ordinary compactness, finite source compression and the external strip do not perform that transfer.

## Repository custody and validation

Pinned reads at recovered head:
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007: c369d3760606d9e5b9ae0f4862156fd712e5be29.
- POSITIVE_SOURCE_HEIGHT_MOMENT_20261006: 7997a0a3ccb0666d117f696dd208b743255b7ac5.
- SOURCE_HEIGHT_GRAPH_ERROR_20261007: b968aa0a3c5eb5ba680ee0251692e24853dadd74.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5 (unchanged retained actual positive control).

External custody is the versioned primary URI, author/date, Corollary 1, uniform sigma interval and constants in (3), recorded in the manifest. Proof body/dependency replay is not claimed. Analytic validation tracks our transverse beta versus the paper's real-part notation, the uniform shrinking delta range, multiplicity-preserving symmetry, both near/far counts, actual sinh sampling norms, dyadic summability and the inverse-versus-positive-height scope. Rational controls check the density exponent inequality and artificial block bounds; they are not actual zero data, a critical arithmetic certificate or Lean proof.

Definitions/cursor updated additively; historical certificates and concurrent aperture work preserved. No aperture marching, retained attachment substitution, same-vector enlarged actual-null transport, endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED.
