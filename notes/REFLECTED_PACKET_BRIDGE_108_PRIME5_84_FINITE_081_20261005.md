# RPB108: actual 84-coordinate prime-5 finite restriction and sources

Base: 75cee9f00696fdd3a82bd1ec82050a2e0129f688.
Definitions: docs/TERMINOLOGY_RPB108_PRIME5_84_FINITE_081.md.

## Result and scope

The complete physical 84-coordinate native restriction at aperture a=81/100 is strictly positive, with Q_84>=10^-28 I. All 84 native and shifted pivots pass; the negative diagonal control is rejected. The maximum native entry width is below 8.105e-61.

All 84 actual nine-panel sources are enclosed with aggregate physical L2 source-map error below 1.772e-50. This includes the entire endpoint-logarithm source, regular terms, poles and active prime powers 2,3,4,5.

The certified uniform 84-moment complement from the previous entry is retained: physical lower bound 51/100, logarithmic lower bound 9/100 and inverse energy factor 100/51 at aperture 81/100. These new finite and source certificates match that dimension. The complete actual residual source Gram and corrected sign remain open. Consequently whole-domain positivity remains certified through a=4/5.

## Full native restriction

The new aperture is enabled only for degree 83 with matrix return. All actual prime powers 2,3,4,5, both pole moments and the actual archimedean kernel remain present. Prime 4 uses Lambda(4)=log(2); prime 5 uses Lambda(5)=log(5). Physical normalization is sqrt((2n+1)/(2a)), n=0..83. Exact reflection parity is retained.

Here a=81/100, d=81/50 and L=81/25. Rational bounds log(5)<L<log(26) give exponential multiplier 26 and kernel multiplier (81/25)/(4/5)=81/20. Native exponential order is 260, Bernoulli pairs 230, gamma order 20, logarithm series 220 and outward interval grid 10^-400.

The exact polynomial-kernel integration acceleration computes once the rational moments integral_0^1 t^m kernel(t)dt. It clears the kernel denominator and a common multiple of all integer integration denominators. Each entry then clears the numerator polynomial denominator and forms one integer dot product. This is exactly the original full polynomial convolution integral, with no quadrature or approximation. Independent comparisons on actual entries (0,0), (80,82) and (83,83) pass. The Taylor exponential factors are also summed into these moments once, yielding a direct integer dot product with each correlation polynomial. Independent comparisons with full convolution on the same three actual entries pass. Logarithmic constants are cached at the same precision. The finite logarithm series is summed over one common odd denominator using integer Horner evaluation; its rational sum, remainder and outward endpoints are identical to the original series.

## Actual nine-panel sources

The sources retain the exact endpoint logarithm, both regular-difference terms, both pole moments and all nine actual translation panels. Their endpoints and coefficients are those certified in the previous prime-5 activation entry. Prime-5 source amplitude is log(5)/sqrt(5); the prime-4 amplitude remains log(2)/2.

Source exponential order is 90, Bernoulli pairs 100, gamma order 50, logarithm series 220 and interval grid 10^-400. The kernel remainder is 4(d/3)^202/[1-(d/3)^2]; its exponential remainder multiplier is 81/40, half the certified kernel multiplier. The pole exponent has absolute argument at most d/4=81/200<log(2), proving Taylor multiplier 2. All polynomial coefficient rounding at grid 10^-60 is included in the error budgets.

The higher source gamma order is required by coefficient amplification: the original order-32 enclosure would contribute about 7.516e-32 to the absolute coefficient sum at degree 83, while order 50 reduces that contribution below 1.584e-63. These are enclosure-budget diagnostics, not physical sign conclusions.

All 24444 regular-source factor identities for j=0..83 and k=0..290 agree with the original binomial sums. Exact correlation checks at (0,83), (80,83) and (83,83) agree with the original correlation identity. Unsupported aperture/dimension combinations are rejected.

Exact reflection p(1-t) clears one rational denominator and performs the binomial sum over integers. It agrees with the original rational composition on the degree-83 Legendre polynomial, degree-290 kernel primitive and degree-373 regular-source polynomial. Repeated interval translation compositions are computed once per source and reused without changing their arithmetic order within any panel.

## Lossless coefficient encoding and panel checks

The source certificate stores integer coefficient numerators at common denominator 10^60. For source degree j, coefficients above j are identical across all nine panels and are stored once as a common row tail. Each panel stores its low-degree numerators and its complete original coefficient-radius budget. Expansion reconstructs the original rational coefficient strings exactly, and the encoder verifies equality with the entire expanded certificate. No source errors are removed or recomputed by compression.

All 672 adjacent-panel jump checks pass. For each source and each panel boundary, the difference between adjacent polynomial pieces is independently compared with the appropriate signed prime-translation polynomial. This verifies all eight activation changes for degrees 0..83, including both new prime-5 edge panels. The maximum jump discrepancy is below 6.074e-60 and lies below twice each source's certified uniform error. The constant-row prime-5 omission control is rejected.

## Validation and standing

The matrix, source certificate and source panel controls reproduce byte for byte. The native reproduction compares two independently organized exact integration methods. The source reproduction compares the original rational reflection/repeated translation method with exact integer reflection/cached translations. Thirty-six exact logarithm endpoint comparisons, including a 400-digit denominator input, agree with the original finite series. Both previous a=4/5 matrix and source certificates reproduce unchanged. Shared accelerations are selected only in the new degree-83 constructor.

The next load-bearing task is the entire matching 84-source residual Gram, including endpoint-log/log, endpoint-log/smooth and smooth/smooth terms, followed by all 7056 native/source pairings and the corrected Schur sign with factor 100/51. Finite restriction positivity alone does not imply whole-domain positivity. Lean, axioms and CI are unchanged. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open.
