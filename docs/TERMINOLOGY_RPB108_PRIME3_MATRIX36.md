# RPB108 full prime-3 matrix/source terminology

- **Full 36-vector native restriction:** the actual mixed form on the orthonormal physical vectors sqrt((2n+1)/(2a))P_n(x/a), 0<=n<36, at a=11/20. It includes primes 2 and 3, poles and archimedean terms, and is distinct from the corrected Schur form.
- **Integer-denominator correlation construction:** the existing exact Legendre correlation identity evaluated after clearing its rational coefficient and integration denominators once. It changes the arithmetic, not the polynomial or carrier.
- **Full 36-source enclosure:** the five-panel approximation to every actual interior source for these 36 vectors, retaining the exact endpoint logarithm. It does not by itself certify all 1296 source/native pairings or the full residual Gram.
- **Coefficient rounding budget:** the sum of absolute coefficient changes caused by rounding to the rational grid 10^-40. On t in [0,1] this bounds the polynomial change uniformly and is added to the source error before normalization.
- **Shared-block enclosure check:** each of the refined first twenty native matrix intervals is contained in its previously certified interval. It verifies overlap of independent calculations; it is not a new full-domain sign argument.

The actual 36-moment complement theorem remains available. The corrected 36-coordinate sign, whole-domain positivity at 11/20, global endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain open. Historical statements remain unchanged; no Lean formalization is claimed.
