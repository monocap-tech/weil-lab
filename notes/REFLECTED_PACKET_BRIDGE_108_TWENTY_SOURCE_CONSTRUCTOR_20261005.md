# RPB108: actual twenty-source constructor and finite custody bound

## Definitions and certified inputs

At aperture a=1/2 let H be the actual supported logarithmic form domain, Q its native multiplier-plus-pole form, and E_20 the physical span of v_n(x)=sqrt(2n+1)P_n(2x), 0<=n<=19. The degree-20 physical complement F_20 is independently coercive. The actual finite matrix A_20 has entries Q(v_i,v_j); it is distinct from the corrected form S_20 obtained by eliminating F_20.

For e in E_20, define the actual interior source J_20 e=q_e by Q(e,f)=<q_e,f>_2 for every f in H. The earlier polynomial interior-source proof establishes this L2 function without assuming spectral operator-domain membership. The new constructor covers every source direction needed for both the remaining degrees 8..19 and their mixed coupling to degrees 0..7.

**Certified raw matrix theorem:** A_20>(1/2000000)I physically. All 400 entries are enclosed; their maximum width is below 3.65e-44. Reflection makes opposite-parity entries exactly zero. The native prime 2, pole moments and archimedean correlations are included.

**Certified source theorem:** There are explicit rational polynomial approximations to q_i-v_i L on each exact prime panel, L(t)=-(log t+log(1-t))/2 and t=x+1/2. The combined source-map error eta_20 is below 2.02e-29. All first-eight source rows coincide exactly with the preceding eight-source certificate. The endpoint logarithm is retained exactly. Polynomial degrees are at most 143.

Artifacts: `scripts/certify_native_twenty_matrix.py`, parameterized `scripts/certify_native_smooth_source.py`, `notes/data/RPB108_NATIVE_TWENTY_MATRIX_CERTIFICATE_20261005.json`, and `notes/data/RPB108_TWENTY_SMOOTH_SOURCE_CERTIFICATE_20261005.json`.

## Native matrix construction

The existing exact physical correlation polynomial identity is evaluated for all degrees 0..19. Its degree is at most i+j+1. On even i+j the two directed correlations agree, by r -> u-r and Legendre parity; opposite-parity symmetrized correlations vanish. Thus one directed correlation suffices for each even entry, without changing the form or its source.

The archimedean integrand is enclosed by exponential order 80 and 60 Bernoulli pairs. Gamma uses Euler--Maclaurin order 12 at n=100 with the next-term remainder. Constants, prime shift evaluation and normalization use rational intervals at a 10^-120 intermediate grid. The established rectangle remainder proof is unchanged; increased orders control the larger polynomial coefficient sums. No floating values enter the certificate.

Interval Schur elimination certifies both A_20>0 and A_20-(1/2000000)I>0. Replacing the first diagonal by -1 is rejected. Elimination pivots are not eigenvalues. This raw sign does not certify S_20 or the remaining twelve-coordinate form.

## Efficient source construction with the same trial vectors

The earlier actual smooth-source approximation theorem applies to every Legendre polynomial used here, with |P_i(2x)|<=1 and |d_x P_i(2x)|<=i(i+1). Its Bernoulli/exponential orders remain 32 pairs and 60. Constants, endpoint H functions, poles and exact prime translates retain the same physical vector.

To compute the regular arch difference polynomial efficiently, write p_i(t)=sum_j c_j t^j and Atilde(s)=sum_k a_k s^k, the approximation to sK(s). The left integral is exactly the rational polynomial

Jminus(t)=sum_(j,k) c_j a_k t^(j+k) sum_(r=1)^j binomial(j,r)(-1)^r/(k+r).

Legendre reflection gives the right integral Jplus(t)=(-1)^i Jminus(1-t). Subtract both from the smooth source. This avoids repeatedly expanding every distance power; it preserves the polynomial exactly. Interval midpoint coefficients and uniform remainders are enclosed by the existing theorem. The first-eight output rows agree exactly with the original slower expansion.

## Minimal finite source custody theorem

For every e in E_20,

(1/2000000)||e||_2 <= ||J_20 e||_2 <= 23489||e||_2.

For the lower bound, the actual pairing gives Q(e,e)=<q_e,e>_2; combine the certified raw coercivity and Cauchy--Schwarz. For the upper bound, the previously proved actual source estimate ||q_p||_2<=26 max|p|+5 max|p'| gives each normalized source norm at most sqrt(2i+1)[26+5i(i+1)]. Sum their squares to bound the operator norm. The square sum is strictly below 23489^2, checked with integer arithmetic.

Therefore ker J_20=0, its finite-dimensional image is closed, and its inverse on that image has norm at most 2000000. This is a verified actual finite source carrier, not an assertion that raw actual-divisor multiplicity copies furnish independent observations. It neither identifies J_20 with the global graph observation map nor proves a global positive-carrier contraction. All source and null statements still use the same e.

## Certified residual error budget and remaining arithmetic

Let Pi_20 be the physical projection onto E_20 and r_e=(I-Pi_20)q_e. Let rtilde use the exact endpoint-log component and the certified smooth polynomial source. Physical projection contracts the source error. The actual source-map upper bound implies ||rtilde||<=23489+eta_20, and consequently

||r* r-rtilde* rtilde|| <= eta_20(46978+3eta_20) < 9.47e-25.

This encloses the source approximation contribution to the full twenty-source residual Gram before its integrals are evaluated. It does not enclose errors of an unperformed or floating Gram integration. All log/smooth mixed terms, exact prime cutoffs and projection products must still be included in that calculation.

The canonical complement theorem gives S_20>=A_20-5R_20, where R_20 is the actual residual Gram. This estimator may or may not certify the full sign; failure would not establish actual negativity. If a sharper enclosure is needed, construct approximate coercive lifts against F_20 and certify their same-vector source residuals.

The already certified E_8 block of S_20 and its twelve-coordinate Schur reduction remain intact. The next concrete work is the full projected twenty-source Gram, followed by the corrected mixed/remaining sign enclosure. No retained membership, full graph density, simplicity or background positivity is assumed. The global endpoint input, F4 and FULL TRANSPORT CLOSED remain open.

## Validation and formalization scope

The degree-seven half-window output reproduces unchanged. Every first-eight new native matrix interval lies inside the independently computed older interval. Four high-degree directed-correlation reflection checks pass. First-eight smooth-source coefficient/error rows agree exactly with the earlier certificate; the extended source certificate reproduces its numerical data. Independent source checks at t=1/10,2/5,3/5,9/10 across all twenty degrees agree within 2.29e-14; this is a convention check, not the proof of the source error. The matrix negative control is rejected.

These are rational arithmetic and analytic results. Lean source, axioms and previously reported CI claims are unchanged; the new constructor and finite bounds have not been formalized in Lean.
