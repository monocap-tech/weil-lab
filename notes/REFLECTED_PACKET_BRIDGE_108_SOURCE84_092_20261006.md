# RPB-108: fresh 84-source certificate at aperture 23/25

The aperture a=23/25 fixes the supported physical interval [-a,a]. The
source map acts on the 84 normalized Legendre vectors of degrees 0–83.
Its piecewise polynomial approximation uses the actual nine support panels
for prime powers 2,3,4,5, with Lambda(4)=log(2). The symbol eta denotes the
operator norm upper bound for the difference between the actual source map
and the stored approximation, measured in physical L2. It is obtained by
summing the squared individual source error bounds and taking an outward
square root. Coefficient quantization is included in those bounds.

The fresh source certificate gives eta<1487/10^39 (approximately
1.4862400543182125e-36). It uses 400-digit interval arithmetic, 220-term
logarithm enclosures, exponential order 90, 100 Bernoulli pairs, gamma order
50, and coefficient grid 10^-40. Its common-tail encoding is lossless for
the quantized coefficients. All mixed terms must remain in the subsequent
residual Gram computation; the small source approximation error alone does
not decide its corrected sign.

An independent exact audit tests source products for pairs (0,83), (41,83)
and (83,83), and the corresponding endpoint-log products, on panels
0,3,4,5,8. All 15 source-product and 15 endpoint-log checks agree with direct
double sums and contain direct-convolution intervals. Large integer carry
controls pass and mismatched projections are rejected. This is a sampled
arithmetic audit, not the complete nine-panel 84-source Gram certificate.

The primary source file is 4,608,289 bytes, with SHA-256
`abc0c3c7af3e710b712f2e4502cede787e8a6e8e412dc5a2284e25611ce161fe`
and Git blob `28bb8a4f4a8e407cb733dfaec4b326cc85e1ef77`.

The independent integration audit repeated byte for byte. A second source
calculation is underway. The primary and repeat native matrix calculations are also
underway. Their outward compact enclosures and full Gram remain pending.
Whole-domain positivity remains certified through 91/100. F-4, full
transport, global endpoint exclusion and historical attachment remain open;
Lean and workflows are unchanged.

Custody:

- `notes/data/RPB108_PRIME5_SOURCE84_092_CERTIFICATE_20261006.json`
- `notes/data/RPB108_PRIME5_HANKEL_092_VALIDATION_20261006.json`
- `scripts/validate_native_prime5_source84_092.py` checks all 84 persisted
  physical normalization bounds, all 756 coefficient panels, the full eta
  aggregation, an underreported-error control, and primary/repeat equality.
