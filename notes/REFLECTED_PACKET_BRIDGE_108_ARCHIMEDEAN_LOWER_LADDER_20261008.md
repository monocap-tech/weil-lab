# RPB108 NF63: globally convergent archimedean cutoffs and monotone original lowest levels

Date: 2026-10-08 UTC (2026-10-07 Pacific). Recovered head b546c15d45b61c79ff8c63fc81d5376176395aa2.

This provides a radius-free, one-sided ORIGINAL-form certification route. The cutoff lowest levels increase to the original lowest level at every fixed finite aperture. Strict original positivity is equivalent to success of some finite archimedean cutoff on the WHOLE physical space. No cutoff's full sign is certified here. At a=21/20, N=32 already gives a proved positive bounded background; its compact gain remains to be bounded.

Definitions: [finite archimedean forms](../docs/TERMINOLOGY_RPB108_ARCHIMEDEAN_CUTOFF.md). The Euler/Laplace identity is inherited from ARCHIMEDEAN_CONTACT_CONTROL_20261006; the new results below are the ordered cutoffs, lowest-level convergence, and exact bounded-background/compact criterion. The identity itself is not reclaimed as new.

## 1. Preserve the original primes and poles; truncate only positive archimedean terms

Set q_j=j+1/4 and m00=m0(0). The established original symbol is

    m0(xi)=m00+sum_{j>=0} pi^2 xi^2/[q_j(q_j^2+pi^2 xi^2)].

Every summand is nonnegative. Define the **archimedean cutoff N** by

    m_N(xi)=m00+sum_{j=0}^{N-1} pi^2 xi^2/[q_j(q_j^2+pi^2 xi^2)],
    L_N=m00+sum_{j=0}^{N-1} 1/q_j.

Since each summand equals 1/q_j-q_j/(q_j^2+pi^2 xi^2), physical Fourier inversion gives the bounded operator

    A_arch,N=L_N I-sum_{j<N} K_j,
    (K_j h)(x)=integral_-a^a exp(-2q_j|x-y|)h(y)dy.

K_j is positive: its full-line multiplier is q_j/(q_j^2+pi^2 xi^2). It is compact on the supported physical space, has continuous kernel, and ||K_j||<=1/q_j. The same formula follows directly by integrating the positive jump energy against exp(-2q_j s). No whole-carrier derivative assumption is used.

Let A_prime be the COMPLETE original operator from NF62, with every active prime power, correct Mangoldt weight, both orientations and endpoint equality; let P_pole retain the original kernel 2cosh((x-y)/2). Define

    Q_N(h)=<A_arch,N h,h>-<A_prime h,h>+<P_pole h,h>.

Each Q_N is a bounded Hermitian form on the ENTIRE supported physical L2 space. For canonical h,

    Q_N(h)<=Q_(N+1)(h)<=Q_original(h),
    Q_N(h) -> Q_original(h).

The increment is nonnegative by its Fourier multiplier. The limit is justified by Tonelli. For physical vectors outside the canonical logarithmic domain, the increasing arch energy tends to +infinity; they are not newly attached to the original actual-divisor source domain. Q_N is a lower comparison form, not a modified zeta divisor or source graph.

## 2. The continuous kernel converges globally, without an origin-series radius

The integrated ORIGINAL archimedean kernel of NF61 has the exact expansion

    k_arch(t)=-m00|t|/2
                 +sum_{j>=0}[exp(-2q_j|t|)-1]/(4q_j^2).

One can obtain it from the Fourier identity above, or by distributional differentiation: minus the second derivative of each summand is (1/q_j)delta_0-exp(-2q_j|t|). Its additive affine ambiguity is fixed by evenness and k_arch(0)=0. The first N terms give k_arch,N. For ALL real t,

    |k_arch(t)-k_arch,N(t)|
          <= (1/4)sum_{j>=N}q_j^-2
          <= (1/4)[q_N^-2+q_N^-1].                (1)

Thus the continuous kernel converges uniformly on the whole real line. The prime hinges and exact integrated pole are added unchanged. This removes the Maclaurin distance-radius restriction identified by the aperture scalability audit; it does not repair old Bernoulli data or retroactively certify their invalid remainder beyond the published radius.

The small uniform kernel error is NOT a small relative canonical-energy error. For every FIXED N, m_N is bounded whereas m0(xi) grows like log|xi|, so

    [m0(xi)-m_N(xi)]/log(e+|xi|) -> 1 as |xi|->infinity.

Hence this sequence does not converge in the full canonical form norm. On the NF61 mean-zero derivative carrier, (1) gives an absolute compact-kernel approximation, while mass-relative differentiation restores the lost high-frequency cost. This is an actual archimedean example of the distinction exposed by NF61. We use ONE-SIDED form order, not a false uniform small-error transfer.

For h in H0^1, a useful separate estimate is

    0<=Q_original(h)-Q_N(h)
       <= (1/4)[q_N^-3+(1/2)q_N^-2]||h'||_2^2.     (2)

Indeed the Euler tail is at most pi^2 xi^2 sum_{j>=N}q_j^-3, and physical Plancherel gives ||h'||^2=4pi^2 integral xi^2|hhat|^2. The decreasing-series integral comparison gives the bracket. Endpoint-nonzero polynomial profiles are not silently put in H0^1; (2) is not their source error bound.

## 3. WHOLE-space cutoff lowest levels converge to the original lowest level

Fix a and define the **cutoff lowest level** ell_N=inf_{||h||2=1}Q_N(h), over supported L2. Let lambda be the original attained lowest physical level on the canonical domain. Then

    ell_N increases to lambda.                    (3)

Proof: write W=-A_prime+P_pole, a fixed bounded physical operator. Every Q_N>=m00 mass-||W||mass, so ell_N is bounded below. Q_N<=Q_original on the canonical domain gives ell_N<=lambda. Thus ell_N has a finite limit ell<=lambda.

Choose physical unit vectors h_N with Q_N(h_N)<=ell_N+1/N. Their nonnegative archimedean increments have uniformly bounded expectation:

    integral (m_N-m00)|hhat_N|^2 <= C.

For any fixed M and N>=M this also bounds m_M-m00. That multiplier is increasing in |xi| and tends to sum_{j<M}1/q_j at infinity. The latter constants tend to infinity as M grows. Given eta>0, first choose M with sum_{j<M}1/q_j>2C/eta, and then R with m_M(R)-m00>C/eta. For all N>=M,

    integral_|xi|>R |hhat_N|^2 <= eta.

The supported-to-low-frequency Fourier restriction is Hilbert–Schmidt. This tail bound therefore makes h_N precompact in physical L2. Take a strongly convergent subsequence with unit limit h. For fixed M, the bounded form Q_M passes continuously to the limit, while Q_M(h_N)<=Q_N(h_N). Hence Q_M(h)<=ell. Monotone convergence in M puts h in the original canonical domain and gives Q_original(h)<=ell. Thus lambda<=ell, proving (3). Attainment of ell_N is not assumed.

Consequences:

    lambda>0 iff ell_N>0 for SOME finite N.         (4)

If Q_N>=gamma mass, gamma>0, then Q_original>=gamma mass. The existing original Garding estimate then gives a strictly positive canonical-energy bound and strict ORIGINAL complete source gain, as in NF55/NF61. Conversely strict original positivity guarantees that some cutoff eventually succeeds. This is a convergence/equivalence theorem, not an independent proof that the original form is positive at every aperture. No effective N is supplied from an unknown original gap.

For a positive original level mu, shifted cutoff levels are exactly ell_N-mu and converge to lambda-mu. When mu=lambda>0, they are nonpositive and tend to zero. An original positive mode is not converted into an unshifted original kernel by this limit.

## 4. A finite exponential cutoff has a compact, mass-relative sign obstruction

Choose a VERIFIED bound B>=||A_prime|| and N with L_N>B. Set delta=L_N-B>0. Write c(x)=cosh(x/2), s(x)=sinh(x/2). Define

    F_N=L_N I-A_prime+2|c><c| >= delta I,
    D_N=sum_{j<N}K_j+2|s><s| >=0,
    Q_N=F_N-D_N.

The **cutoff background** F_N is positive on the WHOLE physical space. D_N is positive compact with continuous kernels; it retains the original negative pole. Define the **cutoff compact gain**

    g_N=||F_N^(-1/2) D_N F_N^(-1/2)||.

This is distinct from the original divisor source gain. The cutoff criterion is exact:

    ell_N>0 iff g_N<1.

If g_N<=theta<1, then Q_N>=delta(1-theta)mass and the original form has the same physical lower bound. Conversely a positive physical cutoff margin bounds the normalized compact operator strictly below one because F_N is also bounded above. Compactness permits finite approximation, but a verified whole-operator remainder is mandatory; finite positive matrices alone remain upper tests.

The prime part of the background has an explicit inverse without any expansion in physical kernel distance. Put A=L_N I-A_prime and r=B/L_N<1. Then

    A^-1=(1/L_N)sum_{j>=0}(A_prime/L_N)^j,
    ||A^-1-(1/L_N)sum_{j=0}^J(A_prime/L_N)^j||
             <= r^(J+1)/delta.                   (5)

Each finite term keeps ALL ordered active-prime paths and supported intermediate points. Different primes remain coupled. The positive pole is included exactly by

    F_N^-1=A^-1
       -2|A^-1 c><A^-1 c|/[1+2<c,A^-1 c>].       (6)

The denominator is at least one. Formula (5) is a bound on A^-1, not silently the same bound on the rank-one-corrected F_N^-1; any numerical use of (6) must propagate vector and denominator errors. An error epsilon in F_N^-1 changes the equivalent compact operator D_N^(1/2)F_N^-1D_N^(1/2) by at most ||D_N||epsilon, with ||D_N||<=sum_{j<N}1/q_j+2(sinh(a)-a). This specifies a complete inverse-error transfer, not a finite gain certificate.

## 5. Concrete original prime-8 standing

At a=21/20, keep the recovered JOINT bound B=1063939/500000, not NF62's weaker separated-prime budget. The established archimedean lower constant m00>=-27/5 and an exact rational harmonic sum give, with N=32,

    L_32-B >= -27/5+sum_{j=0}^{31}4/(4j+1)-B
               >157/1000.                       (7)

Thus this target has a positive bounded background with only 32 exponential kernels left in its compact negative part, plus the exact negative sinh pole. This is a usable starting point for a different whole-operator sign calculation. It is NOT Q_32>=157/1000, and does not repair the old failed corrected 112-vector Schur matrix.

For every fixed finite aperture, L_N tends to infinity and the complete prime bound is finite, so a positive cutoff background can always be reached. The compact gain can still reach or exceed one. Its sign is exactly where the original positivity problem remains. No upper compact-gain calculation is completed in this NF.

## Decision and custody

Adopt this radius-free ordered cutoff framework as an available ORIGINAL positivity test. Unlike fixed-width prime smearing, it has a proved one-sided relation and its whole lowest levels converge to the original level. The next admissible calculation is a rigorous whole compact-gain bound with all cross-prime paths, pole slots and approximation errors, or an independent arithmetic inequality that supplies it. An additional generic approximation theorem alone does not count as a gain estimate.

No paused aperture/precontact experiment is resumed; concurrent coupled work and all prior certificates remain unchanged. Whole-domain standing stays a=1. Global gain, endpoint exclusion, RH, F4 and full transport remain open. The validator checks 228 exact finite symbol, background, inverse, tail and shifted-level controls. The convergence and operator theorems are analytic, not Lean-certified; no existing finite sign certificate is relabeled as this new compact-gain test.
