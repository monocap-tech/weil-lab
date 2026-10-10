# RPB108 RC48 — complete prime-prime trial source covariance

2026-10-10. Parent RC47: `3634462cee949bb5606dad77657913b3fabe17bf`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

The complete physical prime source Gram on the eight emitted native
trials is now enclosed, retaining every cross-prime and cross-orientation
term. Transport through RC47's correlated Riesz error gives actual
physical prime-source entry enclosures and an entire-map canonical
source bound on **native features 0 through 7**:

    sigma_prime^*sigma_prime <=8.213118217379812... M_8
                            <(4107/500) M_8.

Here M_8 is the actual canonical native Gram. RC43's coarser bound was
16.18710807169097... M_8. The new bound is less than 8.214 M_8, almost
halving that allowance. It does not extend to the full 1250-feature map;
RC43's global operator bound remains available on that larger scope.

Every same-parity prime-head interval is more than 37/20 times narrower
than RC47's interval; the minimum improvement is 1.8695114610.... The
refined prime intervals are assembled with the retained actual
archimedean and signed pole intervals to give a further complete-head
refinement. All eight complete-head diagonal intervals still cross zero.
No positive head floor or whole-aperture positivity is certified.

Generation and an independent affine-segment integration replay pass.
The exact actual canonical source Gram remains unevaluated, as does the
complete archimedean/prime/pole covariance and projected residual.

## Physical and canonical source definitions

Keep B=11/10, x=B t, rho=252/257, and the same canonical logarithmic
Hilbert carrier. Let i denote the physical inclusion, ||i||^2<=rho.
The actual native Riesz map R and the rounded 32-mode trial map V have
the RC47 physical error E_phys=i(R-V). Define

    K_prime f(x)=-sum_(n=p^k active) [log p/sqrt(n)]
                 [f(x+log n)+f(x-log n)],
    F_trial=K_prime iV,
    F_actual=K_prime iR,
    sigma_prime=i^*F_actual.

Functions are zero-extended outside (-B,B). The seven active prime
powers are 2,3,4,5,7,8,9, with both orientations. The next integer 10
is inactive since exp(2B)<10, as already certified in RC43. The physical
prime operator satisfies ||K_prime||<=k_p, using RC43's paired-chain
bound k_p=4.103148316.... No single-orientation norm replaces the
paired norm and no active term is discarded.

Distinguish the three matrices:

    U_trial=F_trial^*F_trial              (physical trial source Gram),
    U_actual_phys=F_actual^*F_actual      (actual physical source Gram),
    U_actual_can=sigma_prime^*sigma_prime (actual canonical source Gram).

Their entries are not interchangeable. In particular, physical entry
intervals cannot simply be multiplied by rho to obtain off-diagonal
canonical entry intervals. The inclusion inequality is used below only
as a Loewner inequality.

## Exact support partition and complete trial covariance

Each physical trial is a supported degree-31 polynomial
v_j(t)=sum_m v_(j,m)t^m, converted exactly from the emitted Legendre
coefficients. In t coordinates,

    (K_prime v_j)(t)=-sum_n c_n [
        v_j(t+ell_n/B) 1_(t<=1-ell_n/B)
       +v_j(t-ell_n/B) 1_(t>=-1+ell_n/B)],
    ell_n=log n, c_n=log p/sqrt(n).

The 14 interior support endpoints, together with -1 and 1, produce
15 segments. Directed 220-digit intervals prove their strict ordering.
For each segment, its midpoint is proved strictly inside or outside
every translated support, establishing its active-term set. All
coefficients and boundaries remain interval-enclosed transcendental
quantities; sorting does not rely on unverified floating comparisons.

On each segment the source is the sum of its active translated
polynomials. The validator multiplies the **summed** sources and
integrates their degree-62 product analytically by a polynomial
primitive. Consequently all prime-prime cross terms are included before
the Gram is bounded. This is more precise than summing separate source
norms or squaring a sum of global operator norms.

The same partition computes <v_i,K_prime v_j> in physical L2. Its
intervals are checked inside RC43's translated-overlap trial-head
intervals, verifying the sign, mass factor B, orientations and
normalization against the earlier attachment. Opposite-parity entries
of both the Gram and head vanish by exact reflection symmetry. Every
upper-triangular interval is saved with rational endpoints at denominator
10^25; same-parity source-Gram widths are below 10^-23.

An independent replay integrates in the affine coordinate
t=left+(right-left)u, 0<=u<=1. It reconstructs each active translated
polynomial in u and integrates coefficient pairs with moments 1/(k+l+1),
rather than subtracting polynomial primitives at the support endpoints.
All resulting source/head integrals lie inside the saved intervals.

## Source-specific actual head transport

Let e_j be RC47's rational upper bound for ||E_phys,j||_2 and let
s_j be the new upward square root of (U_trial)_jj. The trial source
column norm allowances are approximately

    [3.01365790, 1.16438597, 0.99493137, 1.03643579,
     0.61028696, 0.27466670, 0.34207002, 0.33468960].

For every feature the script proves s_j^2<k_p^2 T_jj, where T is the
physical trial Gram. These bounds replace RC47's global k_p sqrt(T_jj)
allowances in the linear terms. Self-adjointness of K_prime gives

    |(R^*i^*K_prime iR-V^*i^*K_prime iV)_ij|
       <=e_i s_j+e_j s_i+k_p e_i e_j.

The first two terms pair the Riesz error with the evaluated trial
source action. Only the quadratic error term uses the global operator
bound. The resulting actual prime intervals are intersected with RC47's
intervals. Their width improvement is verified exactly for every
same-parity entry.

For the actual physical source Gram, ||F_actual,j-F_trial,j||_2<=k_p e_j
gives the entry error

    |(U_actual_phys-U_trial)_ij|
       <=k_p(e_i s_j+e_j s_i)+k_p^2 e_i e_j.

The certificate contains these actual physical source entry enclosures;
diagonal intervals are additionally intersected with the nonnegative
axis by nonnegativity of squared norms. They are not substituted for canonical
source entries.

## Entire-map canonical source allowance

Let U_center be the midpoint matrix of the trial physical Gram and h its
maximum entry halfwidth. RC39's exact P>=I/8 bound gives

    U_trial<=U_up=U_center+64h P.

Indeed an 8-by-8 entry error bounded by h has operator norm at most 8h,
and 8h I<=64h P. The script checks the required physical Gram inequality
and PSD of U_up with exact rational arithmetic.

Let B_err be RC47's whole-map Loewner upper bound for E_phys^*E_phys.
For any positive t, Young's inequality and ||K_prime||<=k_p give

    U_actual_phys <=(1+t)U_up+(1+1/t)k_p^2 B_err,
    U_actual_can <=A_t=rho[(1+t)U_up+(1+1/t)k_p^2 B_err].

This bound pays the whole correlated approximation error, not only its
diagonal. Exact rational PSD bisections certify lambda_t P-A_t>=0
for six stated positive rational t values. The best certified candidate
in that finite set is t=1/32. No floating eigenvalue is accepted as proof
and no optimality beyond that set is claimed.

RC39 supplies M_8>=alpha P, alpha=8947777583/17179869184. Hence

    U_actual_can<=lambda P<=(lambda/alpha)M_8,
    lambda/alpha=8.213118217379812... <4107/500.

The certificate records A_t, lambda, t, and the exact rational final
ratio. This is a whole eight-column canonical source envelope. It does
not compute U_actual_can itself, the projected prime source residual,
or any mixed archimedean–prime–pole covariance.

## Refined complete original head

Add the refined actual prime intervals to RC47's actual archimedean and
signed pole intervals, then intersect with RC47's complete-head intervals.
The diagonal enclosures below are rounded further outward for display:

| Native feature | Complete actual original Weil diagonal |
|---:|---:|
| 0 | [-0.511635, 0.589068] |
| 1 | [-0.134744, 0.213212] |
| 2 | [-0.204382, 0.256540] |
| 3 | [-0.131412, 0.186251] |
| 4 | [-0.115229, 0.170653] |
| 5 | [-0.093519, 0.126982] |
| 6 | [-0.049417, 0.165228] |
| 7 | [-0.036142, 0.151245] |

Their exact rational endpoints and all off-diagonal entries are in the
certificate. Every diagonal still crosses zero, so this refinement does
not certify the required original head floor. Negative interval endpoints
are error allowances, not negative test-vector witnesses.

## Validation and remaining work

Run using the published predecessor certificates:

    python scripts/validate_rpb108_rc48_prime_source_covariance.py
    python scripts/validate_rpb108_rc48_prime_source_covariance.py --replay certificates/rpb108_rc48_prime_source_covariance.json

Generation and replay pass. The script verifies input hashes, all active
supports, every trial source/head entry, source-specific transport,
historical intersections, exact PSD source envelopes and rational width
improvements. Analytic support/source identities and Cauchy/Young
inequalities above give the meaning of the interval checks; no Lean
formalization is claimed.

RC48 evaluates the prime-prime trial correlations and pays the transfer
to actual sources on the low-eight block. The next source obligations
include analogous archimedean/pole actions and their complete mutual
correlations. Full 1250-feature entries, precise native solves and the
full canonical projection remain uncomputed. RC44's complement floor and
RC45's conditioning certificate remain unchanged. No new positivity at
aperture 1.10, RH/F4, or Lean closure follows.
