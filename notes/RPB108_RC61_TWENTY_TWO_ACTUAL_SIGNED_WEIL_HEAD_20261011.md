# RPB108 RC61 — 22-feature actual signed Weil head

RC61 attaches the complete original Weil head to the 22 actual native Riesz features at cap B=11/10. All **253 upper-triangle entries** are enclosed, including 121 exact opposite-parity zeros. The construction evaluates the archimedean trial form, all seven active prime-power translations, and the signed rank-two pole term, then transports them with RC60's sharper actual Riesz errors.

The resulting entry bounds certify positive original Weil values in **20 individual feature directions**. Degrees **8 and 11** remain sign-unresolved by these bounds. This is not a uniform positive floor for arbitrary combinations of the 22 features, and the two unresolved intervals are not negative-value certificates.

## Fixed native and trial interfaces

The native features are q_j(x)=Chebyshev_j(x/B), j=0,...,21, with actual canonical Riesz representatives R_j. RC59 supplies their exact physical Gram P22, fixed 32-mode trial matrix V22, and canonical Gram/inverse enclosure. RC60 supplies whole-matrix upper bounds for canonical and physical Riesz errors E22=R22-V22.

Every trial column is unchanged. Input hashes connect RC61 to those two certificates, the corrected constant from RC56, and the previously certified kernel, prime-chain and pole-norm interfaces. The original low-eight actual head bounds are intersected before final outward serialization rounding.

## Archimedean trial form

Use y=(x/B+1)/2 and the exact transformed Legendre polynomials. The nominal archimedean form is evaluated by its endpoint-log term, harmonic diagonal term, old constant center, and regular-kernel convolution. The degree-192 regular kernel coefficients are inherited from RC46, with uniform remainder

\[
\varepsilon_{\rm reg}=\frac{375}{4}\left(\frac{11}{15}\right)^{193}<10^{-23}.
\]

Generation constructs the convolved polynomial on the left triangle and pairs it using exact rational polynomial moments. The actual bounded archimedean remainder is obtained by subtracting the nominal canonical trial metric GT_nom.

Let d and delta_c be RC56's constant shift and radius, and eps_G the inherited metric series/rounding error after removing the old scalar radius. The actual bounded-remainder correction is paid by

\[
\delta_S=|d|+\delta_c+\varepsilon_G+2B\varepsilon_{\rm reg}.
\]

The inherited physical bounded-remainder norm is at most 8. For physical Riesz error column bounds e_i and physical trial norms v_i, the mixed transfer allowance for entry (i,j) is

\[
8(e_i v_j+e_j v_i+e_i e_j).
\]

This retains the distinction between the unbounded original archimedean form and its bounded physical remainder.

## Complete prime and signed pole terms

Since 9<exp(2B)<10, the complete active prime-power set remains **2,3,4,5,7,8,9**. Each paired translation is integrated over its actual overlap interval. The certified path-chain bounds from RC43 provide a whole physical prime operator norm, which transports every trial entry to its actual Riesz entry.

The pole term retains its original sign:

\[
K_{\rm pole}=2|\cosh(x/2)\rangle\langle\cosh(x/2)|
-2|\sinh(x/2)\rangle\langle\sinh(x/2)|.
\]

Trial exponential moments use a rational degree-80 expansion and uniform remainder. Actual moments are enclosed with RC60's physical error norms and the separate even/odd test-function norms. The two nonzero parity blocks give actual signed-pole **rank 2 and inertia (1,1,20)** on the enlarged native space. This preserves the negative odd pole block.

## Refined canonical Gram and full head assembly

Exact physical pairing gives J=R22*V22. The Riesz identity

\[
M_{22}=J+J^*-G_{T,\rm actual}+E_{22}^*E_{22}
\]

gives refined actual Gram entry bounds. On the diagonal the error Gram is nonnegative, so its lower allowance is zero; off the diagonal its magnitude is bounded by the product of certified canonical error norms. The inherited actual trial-metric error is paid separately. These bounds are intersected with RC59 and the finer RC56 low-eight bounds.

The actual archimedean, prime, and signed-pole entry intervals are then added to enclose the complete original head. The certificate also stores the corrected actual original trial-head intervals. For those trial intervals, the constant-dependent projection terms cancel before taking norm bounds, leaving the center correction dT.

All final actual matrix-entry intervals are rounded outward to denominator 10^24 using exact rational floor/ceiling. No floating eigensolver is used to accept the certificate.

The positive individual feature directions are

\[
0,1,2,3,4,5,6,7,9,10,12,13,14,15,16,17,18,19,20,21.
\]

For the two unresolved directions, the current enclosures are approximately

| Feature degree | Actual original Weil quadratic lower | Upper |
|---|---:|---:|
| 8 | -0.091174 | 0.159608 |
| 11 | -0.077444 | 0.141028 |

The table endpoints are outward decimal summaries of the exact rational certificate. Positive diagonal entries do not establish positivity of combinations with off-diagonal correlations.

## Independent replay

Replay uses three alternate evaluations:

- Regular-kernel coefficients come from division by (1-exp(-2r))/(2r), and kernel pairings use direct triangle beta moments rather than the convolved polynomial. Endpoint terms are rebuilt from the Legendre endpoint matrix.
- Prime overlaps use exact rational shifted polynomials at the midpoint translation, with explicit coefficient and moving-endpoint derivative allowances, instead of directed transcendental overlap integration.
- Pole moments use the positive Rodrigues series rather than the power-basis exponential expansion.

Replay verifies every saved nominal enclosure, rebuilds all actual transfers and intersections, and compares the complete certificate exactly. Generation and independent replay pass.

From the repository root:

```sh
python scripts/validate_rpb108_rc61_twenty_two_signed_head.py > certificates/rpb108_rc61_twenty_two_signed_head.json
python scripts/validate_rpb108_rc61_twenty_two_signed_head.py --replay certificates/rpb108_rc61_twenty_two_signed_head.json
```

## Remaining obligation

The complete 22-feature signed source covariance is still unevaluated. It is the next input needed to exploit original-source cancellation, sharpen the remaining head bounds, and form the actual projected-source estimate. RC61 certifies neither a uniform 22-feature original-head floor nor the enlarged projected-source threshold.

The existing actual low-eight floor remains valid. The inherited complementary floor belongs to the 1250-feature complement; no 22-feature complement floor is supplied. No whole-aperture positivity, aperture extension, RH, or F4 completion is claimed.
