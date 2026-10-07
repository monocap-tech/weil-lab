# RPB108: exact local criterion and sparse exceptional actual negative rows

Date: 2026-10-07 UTC. Recovered live head b7012455b4d31bf7b4f267950e8bfc63f4c1d778.
Definitions: [local transverse mass and negative compactness](../docs/TERMINOLOGY_RPB108_LOCAL_TRANSVERSE_COMPACTNESS.md).
Category: endpoint exclusion / actual negative operator scope. Analytic, not a critical source bound or Lean certificate.

## Result

For every fixed a>0 and prescribed actual-copy subset E, the UNWEIGHTED negative analysis on the supported logarithmic domain satisfies

    N_E:D_a->ell2(E) compact
       iff mu_k(E)->0 as |k|->infinity.                 (1)

The averaged actual arithmetic estimate Z2(T)=O(T(log log T)^2/log T) does not supply that uniform local condition for all rows. It does, however, yield an exact actual row decomposition

    N0=(N_good,N_exc), N_good compact on D_a,           (2)

where the number of exceptional unit-height bins in [T,2T] is

    O(T(log log T)^3/(log T)^2)=o(T).                   (3)

All actual copies, normalization weights and signs are retained in (2). The exceptional operator is not removed or proved compact. This is a new actual source decomposition, not global positivity, a critical moment estimate, or the historical restoration packet.

## 1. Sufficiency of the local criterion

Write F_g(theta)=integral g(x)exp(i theta x)dx. For g supported in [-a,a], F_g and its theta derivative belong to L2 by Plancherel, since xg is L2. The one-dimensional interval Sobolev bound gives

    sup_(theta in I_k)|F_g(theta)|^2
      <=C integral_(k-1)^(k+2)(|F_g(s)|^2+|F'_g(s)|^2)ds.

The fixed enlarged integration interval covers its endpoints. If eta_R=sup_(|k|>=R) mu_k(E), then summing with the positive discrete measure beta_q^2 gives

    sum_(q in E,|floor theta_q|>=R) beta_q^2 |F_g(theta_q)|^2
      <=C_a eta_R (||g||_log^2+||xg||_log^2).           (4)

Each integration point is covered a bounded number of times, and log(e+|k|) is comparable with log(e+|s|) on those intervals. Rescaling s=2 pi xi changes only fixed constants in the canonical Fourier norm. This is a weighted local sampling proof, not the replacement of a cumulative count by a local bound.

Now use the EXACT negative profiles from the pinned raw half-difference convention:

    n_q(h)=sum_(m>=0) beta_q^(2m+1)/(2m+1)!
                            F_(x^(2m+1)h)(theta_q).   (5)

The strip bound gives |beta_q|^(2m)<=B^(2m). Triangle inequality in ell2, followed by (4), bounds the high-row norm by

    ||N_E,tail h||<=C_a sqrt(eta_R)||h||_log.          (6)

For completeness, the series of operator bounds is summable. Choose a smooth fixed cutoff chi equal to one on [-a,a] and supported in [-a-1,a+1]. Multiplication by chi x^n on the logarithmic Fourier space has norm bounded by C_a(1+n)^2 A^n, A=max(1,a+1), using the weighted Fourier L1 convolution bound and two cutoff derivatives. The same bound applies to x times that multiplier with n increased by one. Thus the sum in (6) is dominated by

    C_a sum_(m>=0) B^(2m)(1+m)^2 A^(2m+2)/(2m+1)!<infinity.

The expansion converges as an operator series; it is not merely pointwise interchange. Actual bounded sampling/local counting supplies a finite global supremum of mu_k, while the hypothesized limit makes eta_R tend to zero. Finite-height row restrictions are finite rank by actual local zero counting. Equation (6) therefore proves compactness.

## 2. Necessity: supported high-frequency tests detect every bad bin

Choose nonzero smooth real f>=0 supported in (0,min(a,1/4)). Define

    h_k(x)=exp(-ikx)f(x)/sqrt(log(e+|k|)).

The physical vector is a test, not a null vector. Its logarithmic norms are bounded: modulation shifts the Fourier profile, and the log weight inequality bounds its norm by a constant times log(e+|k|) before normalization. Its physical L2 norm tends to zero. Compact physical embedding and injectivity then imply h_k converges weakly to zero in D_a as |k| tends to infinity.

For theta_q in I_k the phase theta_q-k lies in [0,1). On the chosen physical support its cosine is bounded below by a fixed positive constant. The sign of sinh(beta_q x) is the sign of beta_q, and |sinh(beta_q x)|>=|beta_q|x. Taking the real part after that sign change yields

    |n_q(h_k)|>=c_f |beta_q|/sqrt(log(e+|k|)).

Therefore

    ||N_E h_k||^2>=c_f^2 mu_k(E).                    (7)

A compact N_E sends this bounded weakly null sequence to a norm-null sequence. Equation (7) forces mu_k(E)->0, proving the reverse implication in (1). The same test also bounds the mu_k by the already established operator norm of N_E; no distinct-zero independence is inferred from copies.

This is an exact local necessity/sufficiency theorem for these actual sinh profiles. It does not assert that the actual local limit holds.

## 3. What the averaged density REALLY gives

Define good/exceptional bins using the registered threshold kappa_k=1/log log(e^e+|k|). Every good-bin mass obeys mu_k<=kappa_k, which tends to zero. Applying (1) to those unchanged actual rows proves N_good compact on D_a, for every fixed a.

If an integer k lies in [T,2T] and is exceptional, then for large T

    b_k>c log T/log log T.

Summing b_k over these disjoint bins is bounded by Z2(2T+2). The pinned actual second-count estimate therefore gives (3). Negative heights follow the same argument. This is density zero of EXCEPTIONAL BINS, not a claim that the fraction of divisor copies there tends to zero, that the exceptional set is finite, or that no physical vector is observed there.

The full native source dictionary is exactly

    Q(h)=||P0 h||^2-||N_good h||^2-||N_exc h||^2.      (8)

Discarding N_exc would change Q. The rows are selected by actual transverse counts; no polynomial mass observation, effective-background coordinate or prescribed historical selection is substituted. The decomposition does not alter the physical vector.

## 4. Rare clusters control the missing implication

An artificial location measure demonstrates the distinction. Let m_j=2^j, H_j=2^(m_j), j>=1. Put m_j identical norm-weighted copies at theta=H_j with beta=3/8. Optional reflection/sign partners only change a constant. The cumulative transverse second count is O(log T), hence meets the much weaker actual averaged upper bound. Local count is O(log height). Its normalized local mass at the cluster bins is bounded away from zero:

    mu_(H_j)>=1/8

for large j, using log(e+H_j)<=log(2H_j)<(3/4)(m_j+1). Thus its negative observation operator fails compactness by the physical tests (7), even though cluster bins have density zero. A critical-line background may be added without affecting negative rows or Z2 if a total count of order T log T is desired.

These are artificial locations, not actual zeta zeros, an actual explicit-formula model or a null control. Repeated copies are used solely for multiplicity norm weight; no extra independent observation is claimed. This control rejects only the inference from averaged/local-count upper statistics to uniform vanishing of mu_k.

In particular the positive actual eigenmode remains compatible with (2)-(3), since that row decomposition depends only on actual zeros and applies to the whole physical carrier. The decomposition supplies no regularity unique to zero contact.

## Endpoint scope and smallest remaining theorem

The attempted implication averaged actual off-line sparsity -> full unweighted negative compactness is not proved and cannot follow from those location statistics alone. Its exact additional arithmetic condition is the uniform local limit in (1). That condition would establish compactness, but compactness BY ITSELF still would not exclude a finite nonnegative kernel or supply a critical positive moment.

For global endpoint closure the existing smallest signed source estimate remains: bound the actual complete source-height graph error above on the whole hypothetical zero-contact kernel. Along this new split, one must control the contribution of N_exc AND the critical signed coupling; an unweighted small tail of N_good is insufficient. No such estimate is obtained. Formula (8) is kept intact.

This pass records the exact failed average-to-local implication, a rare-cluster control, the actual compact-row consequence that DOES follow, and the smaller extra local theorem for full negative compactness. Those operator results are not called a solution of the endpoint arithmetic target.

## Source custody and validation

Pinned reads at recovered head:
- TRANSVERSE_DENSITY_SAMPLING_20261007: c9950fafef341ee66f62a5b1ab21013ebfd3a716.
- POSITIVE_SOURCE_HEIGHT_MOMENT_20261006: 7997a0a3ccb0666d117f696dd208b743255b7ac5.
- SOURCE_HEIGHT_GRAPH_ERROR_20261007: b968aa0a3c5eb5ba680ee0251692e24853dadd74.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.

The external density theorem is inherited through the pinned prior note's versioned primary URI and interval; no new external theorem is imported. Supported sampling, log multiplier bounds and compact physical inclusion retain their existing custody. Analytic audit: local sampling before count use, uniformly summable actual sinh series, correct domain metric, weakly null modulations, per-bin lower observation, disjoint-bin counting and both terms of the preserved dictionary. Rational controls audit logarithm brackets and rare-cluster masses, not actual zeros or the infinite-dimensional proof. No Lean executable/build/axiom audit, new aperture or critical arithmetic certificate.

Definitions and cursor updated additively. Historical certificates, current whole-domain positivity through 973/1000 and concurrent aperture work are preserved. No aperture marching, retained attachment reopening, same-vector enlarged actual-null transport, endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED.
