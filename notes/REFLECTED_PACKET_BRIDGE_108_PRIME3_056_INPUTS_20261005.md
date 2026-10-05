# RPB108: actual 36-vector inputs at aperture a=14/25

Base: 075d10ea6534fe19ad93cd773e6f53e6dac9103a.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_056_INPUTS.md.

## Concrete result

The full actual native restriction Q_36 at a=14/25 is strictly positive on all 36 physical Legendre directions, with raw physical margin 1/64000000. All 36 actual source enclosures on the five prime panels are certified, with combined physical source-map error below 2.144e-25, including coefficient rounding. The actual 36-moment complement has physical coercivity 31/100 and logarithmic coercivity 9/100 uniformly through this aperture, giving inverse factor 100/31.

These are the complete native inputs for the next full residual Gram. They do not yet decide the corrected sign or whole-domain positivity at 14/25. The earlier whole-domain result at 11/20, with margin 1/4000000000, remains the current certified sign aperture.

## Native restriction and audit bounds

The degree-35 matrix constructor is narrowly extended to the new rational aperture 14/25 in matrix-return mode. The old apertures and their branches keep their arithmetic. The twenty-vector and seven-vector constructors are not enabled at this new aperture.

Here L=4a=56/25<9/4 and L<log(10), while L>log(4); thus the previously proved exponential multiplier 10 and kernel multiplier 3 remain valid. The actual prime thresholds log(3)<2a<log(4) are checked by rational intervals, so the constructor integrates the actual shifts for prime powers 2 and 3. It retains both pole terms and the physical factor 1/(2a).

The constructor uses exponential order 120, 100 Bernoulli pairs, gamma order 12, exact integer correlation accumulation, outward grid 10^-200 and square roots on that grid. Every mixed entry is included, with odd entries exactly zero by reflection. All 36 raw and shifted elimination pivots pass after subtracting 1/64000000. The maximum matrix entry width is below 1.097e-47. Replacing the first diagonal by -1 is rejected.

## All 36 actual source enclosures

The existing source formula admits a=14/25 explicitly while retaining its original a=11/20 default. A small new entry script evaluates that formula at d=28/25. All analytic assertions are re-evaluated: log(3)<d<log(4), 2d<log(10), log(4)<2d<9/4 and d/2<log(2).

The actual sources retain the exact endpoint logarithm, both regular difference integrals, all five actual prime panels, both actual pole moments and physical normalization sqrt((2n+1)/d). Exponential order 60, 32 Bernoulli pairs, gamma order 20 and intermediate grid 10^-200 are unchanged. Every midpoint coefficient is rounded to denominator dividing 10^40, and the total absolute coefficient change is added to its panel error budget. All 36 row errors and the resulting physical L2 source-map error are recomputed at this aperture.

The complete rounded source-map error is below 2.144e-25. This is an actual error bound at the new aperture, not reuse of the smaller-aperture source coefficients or errors. No source/native pairing at the new aperture is asserted before its Gram integration.

## Uniform lawful complement through 14/25

The same integrated-mass theorem is evaluated at upper aperture 14/25, k=36 and physical cutoff T=15/2. With y=2a(22/7)T and q=y^2/(73*75), its bound rho=4a T y^72/[(73!!)^2(1-q)] is valid with q<1. It dominates the smaller-aperture masses by monotonicity.

Writing S=sqrt(2)log(2), A=log(3)/sqrt(3), c(T)=log(T)-1/(2T)-S and p=16a(a/2)^72/(36!)^2, the proved actual physical complement lower bracket is c(T)-(10+c(T))rho-p-A. Its exact lower value exceeds 0.3180393848, so physical coercivity 31/100 is valid. Prime 3 is bounded by its compressed adjacency norm one; this remains conservative below activation as well.

The independent logarithmic proof retains cutoff 7 and gives unrounded lower value above 0.0999004813, hence logarithmic coercivity 9/100. The lawful form-domain lift exists on the same supported logarithmic domain, and its correction satisfies K_36<=(100/31)R_36 once the actual residual Gram is integrated. No spectral operator-domain premise is introduced.

## Validation and next step

The full native matrix, rounded source enclosures and complement certificate reproduce byte-for-byte. Matrix parity, all 36 shifted pivots, negative diagonal control and the published rational error/coercivity bounds pass. Input file hashes and scope are recorded in the validation manifest.

Next: integrate every log/log, smooth/smooth and both log/smooth term on all five panels; remove the same 36-vector projection; check all 1296 native pairings; carry the actual Gram operator error; and decide Q_36-(100/31)R_36. The raw finite sign does not substitute for this coupling calculation.

Artifacts: scripts/certify_native_prime3_{matrix36,source36,complement36}_056.py, narrowly extended native/source constructors, and notes/data/RPB108_PRIME3_{MATRIX36,SOURCE36,COMPLEMENT36}_056_CERTIFICATE_20261005.json.

Corrected sign and whole-domain positivity at 14/25, global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged; these new analytic/rational inputs are not Lean formalized.
