# RPB108: complete actual prime-5 84-source Gram and corrected sign

Base: 6336ff00d596187907c9e16ec7bdfdb156b35109.
Definitions: docs/TERMINOLOGY_RPB108_PRIME5_84_SCHUR_081.md.

## Result

The complete actual corrected form at a=81/100 is positive with physical margin 1/100000000000000000000000000000. The full-domain physical quadratic form satisfies Q(h)>=1/20200000000000000000000000000000 ||h||_2^2. This closes the matching 84-coordinate sign problem, excludes fixed-aperture weak null modes and establishes fixed-aperture full-source unit domination.

## Matching actual ingredients

At aperture a=81/100, the physical basis has Legendre degrees 0..83 and the matching orthogonal complement annihilates those same 84 moments. The active prime powers are 2,3,4,5; Lambda(4)=log(2), Lambda(5)=log(5). The previously certified full native restriction has raw margin 10^-28. All 84 actual sources retain endpoint logarithms, regular differences, both pole moments and all nine actual translation panels, with aggregate physical L2 source-map error below 1.772e-50.

The uniform actual complement bounds are 51/100 physically and 9/100 logarithmically. They use the joint prime-2/4 and prime-3/5 translation norms and the actual quarter-line archimedean estimates. The inverse complement energy factor beta is 100/51. The source and native certificates are identified by SHA-256 in the complete Gram certificate.

## Complete actual residual Gram

The actual source Gram contains endpoint-log/log, endpoint-log/smooth and smooth/smooth terms. The complete matching 84-coordinate source projection is subtracted. Every mixed term remains present, including terms that rounding might prevent from cancelling by reflection. The 84-source/84-projection endpoint-log helper is newly admitted; mismatched (83,52) and (51,84) degree/dimension pairs are rejected.

All 7056 native/source pairings are independently compared with the native matrix and bounded by each source's certified physical L2 error. With M a surrogate residual-source map norm bound and eta the aggregate actual source-map error, delta=eta(2M+eta) bounds the actual residual Gram operator error. The corrected sign test uses Q84-beta Rhat84-beta delta I with an additional rational margin when positive. No actual negative witness is inferred merely from a failed sufficient lower estimator.

For a positive corrected form, write the full vector using its finite component v and the energy-orthogonal complement remainder z after the certified lift. The energy is at least tau||v||^2+c||z||^2. If the lift norm is at most L, the full physical norm squared is at most 2(1+L^2)||v||^2+2||z||^2. This yields min(tau/[2(1+L^2)],c/2) for the full form.

All 84 interval pivots of Q84-(100/51)Rhat84-((100/51)delta+tau)I are strictly positive. The certified lift norm is strictly below the integer 10, yielding the whole-domain coefficient 1/20200000000000000000000000000000. The negative diagonal control is rejected.

The maximum full-Gram interval width is approximately 3.041950e-114. The aggregate surrogate residual-source norm bound is approximately 4.78362661477; the actual Gram operator correction delta is approximately 1.695255e-49. These decimal values are displays; every load-bearing bound is stored as an exact rational in the certificate.

## Exact integer moment integration

The exact source encoding is expanded without modifying the coefficient radius or the previously certified physical L2 source budget. The new integration changes only the arithmetic used to integrate the same surrogate source map.

All 14,112 Gram interval endpoints are stored as exact finite-decimal strings on the same outward grid. This is a lossless representation change to fit the connector request limit, with no floating conversion. For each of two complete arithmetic runs, every converted endpoint equals its original exact rational; both canonical certificates remain byte identical.

All smooth polynomials are decoded as integer coefficients with common denominator 10^60. Endpoint power and endpoint-log moments are enclosed on outward grid 10^-600. The panel-boundary and endpoint logarithms use 500 finite atanh-series terms, with rational remainder enclosures. An initial 220-term, 400-digit Gram run failed the unchanged entry-width requirement; no sign claim or certificate was produced by that run. The increased precision addresses amplification by large expanded polynomial coefficients. Both integrands are nonnegative on [0,1], so moment lower endpoints may be intersected with zero.

For integer polynomial vectors u,v and moment intervals [l_k,h_k], the exact center numerator is sum u_i v_j(l_{i+j}+h_{i+j}). An outward radius numerator is sum |u_i v_j|(h_{i+j}-l_{i+j}). Division by twice the moment grid and polynomial denominators gives the enclosed integral. This radius can be more conservative than grouping the polynomial convolution coefficients first; it remains outward.

The Hankel products are computed by integer polynomial packing. Positive and negative coefficient parts are packed separately. Block width exceeds the bit length of min(length(u),length(moments))*max coefficient*max moment, preventing any convolution coefficient carry across blocks. Integer multiplication and block extraction give the exact convolution windows, with no floating FFT or fixed-width integer overflow. Each source coefficient vector is applied to the moment matrices once per panel and reused in the complete Gram contractions.

Before squaring, the largest expanded source coefficient absolute sum is approximately 1.55e81. At 220 logarithm terms, the ln(2)/d boundary width alone is approximately 2.448e-213; multiplication by the square of that coefficient sum gives an amplification scale of approximately 5.88e-51. This diagnostic explains why the old full-Gram precision was inadequate for the required 1e-55 entry width. It is not a sign estimate.

Independent checks compare packed bounds with direct double sums and the original polynomial-convolution interval formula on source pairs (0,83), (41,83), (83,83), both for power moments and endpoint-log moments, on panels 0,4,8. All nine source/source and nine endpoint-log/source comparisons pass, and all new intervals contain the original convolution intervals. Large-integer carry controls pass.

## Validation and standing

Two fresh complete arithmetic runs produce byte-identical certificates, including after lossless finite-decimal endpoint encoding; all 14,112 endpoint conversions per run equal their original exact rational values. The independent custody/sign validator passes source/native SHA-256 checks, every stored entry width, symmetry, the source correction, sign fields and (when positive) the lift and whole-domain bound. All 18 sampled Hankel contractions pass direct double-sum equality and convolution-interval containment; large integer carry and mismatched projection controls pass.

The logarithm, basis normalization and sign decisions remain rational/outward interval computations. Float displays do not enter certification. Lean, axioms and CI remain unchanged. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open.
