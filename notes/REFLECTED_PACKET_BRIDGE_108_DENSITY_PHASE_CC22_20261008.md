# RPB108 CC22: actual density phase modulus and failed weight transfer

Date: 2026-10-08 UTC. Parent: 625d506c479d03e466cde975bf1f77d8b6d97941.
Definitions: [density phase modulus](../docs/TERMINOLOGY_RPB108_DENSITY_PHASE.md).
Classification: A, actual arithmetic weighted negative phase estimate; C, separated weight-transfer closure cannot furnish an old-gap-independent original shell bound. No new aperture or Lean certification.

## Result and scope

The inherited actual transverse density estimate gives, on every fixed finite physical cap B and for every eta>0,

    ||(U_r-I) N_eta||_HS^2
       <<_{B,eta} (log log(1/|r|))^2 / (log(1/|r|))^eta.       (1)

This tends to zero and is independent of the old signed gap. It applies to the COMPLETE weighted negative source, with every actual divisor copy retained. It is an analytic asymptotic theorem, not an optimized effective numerical certificate.

It does not bound the complete unweighted critical incoming covariance. Restoring the height weight and then applying the old inverse defect produces a factor at least 1/delta_min in the squared estimate, even in rank one with a uniformly protected positive Gram. The arithmetic estimate controls neither that factor nor the mixed change of the old positive-source projection. Consequently this particular density-to-phase-to-relative-loss argument does not close the continuation gate.

This is not a counterexample to the desired ACTUAL zeta bound. In particular we have not proved formal logical independence from the complete Weil identities: our finite controls do not satisfy their arithmetic explicit formula. The precise negative result is the failure of the separated estimator; the actual required joint correlation remains unproved.

## 1. Actual arithmetic input and normalization

The inherited [transverse density sampling proof](REFLECTED_PACKET_BRIDGE_108_TRANSVERSE_DENSITY_SAMPLING_20261007.md) uses Chourasiya and Simonic, An explicit form of Ingham's zero density estimate, arXiv:2507.15184v2, Corollary 1:

https://arxiv.org/html/2507.15184v2

The primary paper was read again in this pass. Its uniform sigma interval [1/2,5/8] and T>=3*10^12 allow the shrinking near-line split, with multiplicities and functional symmetry retained. Together with the separately accepted |beta|<=3/8 strip, the inherited derivation yields

    Z2(T)<< T (log log T)^2/log T.                            (2)

The paper is a density input, not the source of our accepted strip. No new audit of the strip or proof replay of the external density theorem is claimed.

The original pair coordinates remain

    p_q(h)=integral h(x) exp(i theta_q x) cosh(beta_q x) dx,
    n_q(h)=integral h(x) exp(i theta_q x) sinh(beta_q x) dx.

The negative physical row norm obeys

    ||n_q||^2 <= K_B beta_q^2,
    K_B=exp(3B/4) (2B^3/3).                                 (3)

This is the normalized Q=P*P-N*N convention, not the raw doubled pair form. No replacement by a pointwise infinite zero kernel occurs.

## 2. Proof of the complete phase modulus

Use |exp(i theta r)-1|^2<=min(4,theta^2 r^2). Nonnegative summation and (3) give the lawful Hilbert-Schmidt estimate

    ||(U_r-I)N_eta||_HS^2
      <= K_B sum_q beta_q^2 min(4,theta_q^2 r^2)/W_eta(q).     (4)

The inherited weighted sum is finite for eta>0, so (4) concerns the complete infinite operator, not a retained finite source truncation.

For sufficiently large integer j, the block 2^j<=|theta|<2^(j+1) has transverse mass at most C 2^j (log j)^2/j by (2). W_eta is bounded below by a constant times 2^j j^eta. Let m=floor(log_2(1/|r|)). The block contribution to (4) is bounded by

    C_B min(4,2^(2j+2)r^2) (log j)^2/j^(1+eta).             (5)

For j<=m, summation of the geometrically growing factor gives

    O_{B,eta}((log m)^2/m^(1+eta))+O_B(r^2).

To justify the endpoint domination, split at m/2: the lower part is exponentially small times a bounded or polynomial sum, while on [m/2,m] the slowly varying factor is comparable to its value at m and the geometric sum is bounded. Finitely many low blocks contribute O_B(r^2).

For j>m, the integral test for sum (log j)^2/j^(1+eta) gives

    O_{B,eta}((log m)^2/m^eta).

This dominates and proves (1). The unsquared HS modulus is the square root of the displayed rate. Constants can be expressed using an inherited cumulative constant, finitely many low rows and the explicit series (5); no optimized numerical constant is provided. Eta=0 is excluded. Failure of its summable majorant does not prove failure of the actual borderline operator.

Thus arithmetic density supplies an actual quantitative phase bound, beyond an appeal to qualitative compactness. We do not reopen endpoint regularity or generic continuity as a closure argument.

## 3. Where it enters the shell problem

Keep the CC21 whole incoming frame, its two translated branches and all mixed covariance terms. With Ttilde=T_s Pi_s, the pure phase part is

    H_r=U_-r Ttilde-Ttilde U_+r
       =(U_-r-I)Ttilde-Ttilde(U_+r-I).                       (6)

On p=P_s h in the old positive range, the first term is (U_-r-I)N h. Its WEIGHTED negative version has (1), and positive observability supplies ||h||_2<=c_B^(-1)||p||. Density alone does not bound the second term Ttilde(U_+r-I)p, which includes the changed old positive-range projection, nor the resulting joint critical covariance. The accepted strip's boost estimate from CC21 remains valid, but it does not remove (6).

For incoming K and D_s=I-A_s, the exact whole target remains

    ||K*D_s^(-1)K||<1.                                     (7)

On the near-critical output E with G=E D_s E and L=E K, the minimal critical matrix estimate is

    L L*<=q G.                                             (8)

A low-output cost ell and q+ell<1 suffice for (7). Condition (8) alone does not dispose of the low output. The equivalent CC20 physical formulation is J M_t^(-1)J*<=q Lambda G, with protected positive Gram M_t, all forced rows and their mixed products retained. The weighted density estimate is not an evaluation of either covariance.

## 4. Exact obstruction to separated weight transfer

For a negative output y in the domain of W_eta^(1/2),

    <y,(U_r-I)N f>
      =<W_eta^(1/2)y,(U_r-I)N_eta f>.                       (9)

If that domain condition fails, the corresponding Cauchy-Schwarz transfer has no finite coefficient. Finite critical rank does not imply a coordinate height moment for its infinite-support basis vectors. We make no assertion that an actual critical negative vector has an infinite moment.

If the moment is finite, the separated matrix estimator introduces

    C_s=||G^(-1/2) E W_eta^(1/2)||^2.

Since W_eta>=I, its quadratic form satisfies

    G^(-1/2) E W_eta E G^(-1/2)>=G^(-1).

Hence C_s>=1/delta_min. This proves a precise impossibility: THIS separated coefficient cannot have a finite bound independent of the old defect as delta_min tends to zero. It does not prove impossibility of a bound for the actual joint expression G^(-1/2)E(U-I)N, where covariance cancellation could supply the missing defect factor.

Rank-one controls make the weight loss transparent. Put the critical output at height Theta, W=W_eta(Theta), old gain lambda=1-delta, and incoming alignment k. Its weighted squared alignment is k^2/W, while its original relative cost is k^2/delta. Restoring the dual factor W/delta cancels the height saving exactly. Choose W tending to infinity and delta to zero independently: weighted smallness coexists with divergent original relative cost. Positive Gram can remain I. Sparse isolated high rows are compatible with the coarse cumulative transverse upper bound, but we claim neither their occurrence in the actual divisor nor satisfaction of the full explicit formula.

The lower bound C_s>=1/delta_min also shows why making r depend on the known old gap is an ordinary gap-dependent step, not the requested old-gap-independent continuation theorem. A quantitative cap-only phase rate alone supplies no common step that works as the old defect vanishes.

## 5. Crossing and positive-level controls

The inherited genuine H01 differential model Q(h)=||h'||^2-||h||^2 crosses at a*=pi/2. With u=2s/pi and v=2t/pi, its old defect is 1-u^2 and exact critical shell leakage is 2u(v-u). At contact v=1, the relative critical cost is 2u/(1+u), tending to one; the whole cost is one. For a fixed target v=9/8 beyond contact, the critical cost diverges as u tends to one. Small unweighted leakage is therefore not a relative safe budget. The new validator checks these exact dimensionless identities and replays the prior genuine crossing controls. This model is not an arithmetic Weil counterexample.

The positive-level source control remains P=I, N=(9/25,12/25), physical eigenlevel mu=16/25. The original incoming cost is 9/34<1. For Q-mu I, the COMPLETE added negative physical mass channel sqrt(mu)I is retained: old gain 481/625, old defect 144/625, critical plus low cost exactly one and shifted Schur complement zero. It is a positive original level, not an original zero. Density smoothing applies to all supported physical L2 vectors, so that estimate alone is not a zero-level discriminator. No claim about negative critical moments is imported from the older rough positive eigenmode's divergent POSITIVE moments.

## 6. Validation and standing

The exact validator adds 4,356 rational checks: 3,552 dyadic min/split controls, 480 weight-transfer and protected-Gram Schur controls, 320 genuine crossing controls and four full positive-level checks. It replays 13,996 inherited CC21 checks; total 18,352 pass. The analytic logarithmic rate is established by the proof above, not by those rational proxies. No actual zeta covariance matrix is numerically evaluated.

Whole-domain original positivity remains internally certified only through 21/20, even0/odd0, joined physical margin 1/(3*10^63). RH/F4, retained attachment, reusable continuation, accumulated finite-cap relative loss and Lean closure remain open. Global stays paused at NF71; independent Aperture and Pre-Contact Shadow stay paused. This pass adds an actual arithmetic estimate but certifies no new original near-critical shell budget.

The next required theorem is the joint unweighted forced-source covariance estimate (8), including phase/gain correlation and low output, with constants depending only on the finite cap. A negative-source height estimate could contribute only if supplied jointly with the old defect cancellation. Further separated weighted norm estimates cannot resolve that missing correlation.
