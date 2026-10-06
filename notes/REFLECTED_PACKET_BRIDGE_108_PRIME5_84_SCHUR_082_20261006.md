# RPB108: complete actual prime-5 Gram and estimator obstruction at 41/50

Base: `8615813fb188a5fae0da50134af63dbb8af3b156`.
Definitions: [actual 84-source certificate at 41/50](../docs/TERMINOLOGY_RPB108_PRIME5_84_SCHUR_082.md).

## Lawful extension of the constructors

This pass uses the actual native form on the physical interval [-41/50,41/50]. Its matching finite basis and complement use all Legendre degrees 0 through 83. The active prime powers are 2,3,4,5; the prime-4 amplitude uses Lambda(4)=log(2). Prime 7 is inactive. Both signed pole contributions and all source translation panels are retained.

The shared native and source constructors admit only the additional audited aperture 41/50 with degree 83. The previously supported aperture cases retain their own constants and formulas. For the native correlation length L=82/25, exact logarithm intervals verify log(5)<L<log(27), L<6 and log(5)<2a<log(7). Therefore exp(L)<27 and L/(1-exp(-L))<5L/4=41/10. The native wrapper uses exponential order 260, Bernoulli order 230, gamma order 20, logarithm order 220 and a 400-digit outward grid.

For the source length d=41/25, the Bernoulli polynomial has alternating, decreasing absolute coefficients through order 100. On [0,1], paired terms bound it between 1+ds and 1+ds+d^2s^2/3. Consequently half its absolute value is below 41/20, the new exponential Taylor ceiling. Also d/2<1 and d<3, retaining the respective exponential and Bernoulli remainder estimates. The source constructor uses exponential order 90, Bernoulli order 100, gamma order 50 and 220 logarithm terms on a 400-digit grid. Smooth coefficients are rounded to denominator 10^40 with the coefficient rounding budget explicitly added to every certified source error.

The new native and source certificates each reproduce byte for byte in two independent executions. The original full native matrix is represented by an outward 80-digit lower-triangle enclosure, with all 7,056 containment checks, symmetry, exact odd reflection zeros and two fresh 42-dimensional parity-block sign checks. The compact file records the original full matrix SHA256 and Git blob hash and hashes of its constructor, shared helper and compact exporter. Reproduction starts from the full native constructor before the outward export. The default quarter-window certificate remains byte identical to the unmodified helper; unsupported aperture/degree combinations reject.

## Actual complement and full residual Gram

A target-specific rerun of the actual 84-moment complement gives an unrounded physical lower bound approximately 0.5006312676825696, allowing c=1/2 and beta=2 uniformly for 1/2<=a<=41/50. The logarithmic complement lower bound is 9/100. Both frequency cutoffs, moment mass estimates, pole loss, joint prime-2/4 norm and joint prime-3/5 norm are rechecked. Independent signed 4x4 positive pivots certify the chain bound; an undersized chain bound rejects. Two complement runs agree byte for byte.

Since a<log(6)/2, the existing ordered nine-panel source geometry remains valid. The full residual Gram subtracts the complete matching 84-coordinate source projection and retains endpoint-log/log, endpoint-log/smooth and smooth/smooth terms, including every mixed entry. All 7,056 source/native pairings must agree within the respective actual physical source error. The resulting Gram is symmetric and every entry width is required to be below 10^-55.

The Gram uses exact integer Hankel contractions, 500-term outward endpoint logarithms and a 300-digit outward grid. All 14,112 endpoints are stored losslessly as exact finite-decimal strings. The source errors remain actual analytic bounds, not grid errors: with aggregate source error eta and surrogate residual-map bound M, the actual Gram error is delta=eta(2M+eta). The matrix tested is Q84-2Rhat84-(2delta+tau)I.

An initial run retained the older 10^-45 auxiliary delta check, which is incompatible with the new 40-digit coefficient budget; it produced no certificate. The corrected pass requires delta<10^-30 and deducts the entire exact computed delta in the sign test. The proof uses this actual deduction, not the auxiliary threshold. Lower precision is accepted only after the unchanged entry-width and pairing checks pass.

Independent direct double sums agree with the integer-packed bounds for source pairs (0,83), (41,83), (83,83) on panels 0,4,8, for both power and endpoint-log contractions. All 18 comparisons pass and the packed intervals contain the original convolution intervals. Large integer carry and mismatched source/projection controls also pass.

## Certified outcome and exact directional obstruction

The two complete Gram runs agree byte for byte. The native finite restriction satisfies Q84>=10^-18 I, but the matched no-lift lower estimator Q84-2R84 is rigorously negative in an explicit rational direction v. The stored witness has 84 coordinates and is evaluated using every Gram entry.

After the full actual Gram operator error is added, its exact quadratic upper bound U is below -2*10^-14 (display: approximately -2.3990786235127062*10^-14). The corresponding Rayleigh upper bound is below -10^-14. The same vector's exact native energy lower bound is above 3*10^-12 (display: approximately 3.4892129351694658*10^-12). Thus v is not an actual native negative witness. In particular, failure of this sufficient estimator does not establish a negative full native form.

The maximum Gram entry width is approximately 3.041949685829048*10^-114. The surrogate map norm bound M is approximately 4.937970538998575; the exact actual Gram correction delta is below 1.5*10^-35 (display: approximately 1.4653068160216015*10^-35). These displays are not used in sign decisions. The certificate stores all exact rational bounds and binds both complete inputs by SHA256.

The negative upper bound gives a directional lower requirement of -U on the improvement to the inverse-complement estimate. Precision error is far below this obstruction. A refined actual energy lift or inverse-complement estimate is therefore the next sign target; simply claiming the raw finite margin or dropping residual terms cannot certify this aperture. No positive corrected tau, whole-domain mu or logarithmic kappa is supplied at 41/50.

## Reproduction and custody

Run from the repository root with ordinary Python 3 and no external numerical package:

```sh
python scripts/certify_native_prime5_matrix84_082.py > /tmp/native082.json
python scripts/compact_native_prime5_matrix84_082.py --input /tmp/native082.json --output notes/data/RPB108_PRIME5_MATRIX84_082_COMPACT80_20261006.json
python scripts/certify_native_prime5_source84_082.py > notes/data/RPB108_PRIME5_SOURCE84_082_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_complement84_082.py > /tmp/complement082.json
python scripts/certify_native_prime5_gram84_082.py > notes/data/RPB108_PRIME5_GRAM84_082_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_gram84_082.py > /tmp/gram082-repeat.json
python scripts/validate_native_prime5_84_hankel_082.py > /tmp/hankel082.json
python scripts/validate_native_prime5_84_schur_082.py /tmp/gram082-repeat.json /tmp/hankel082.json
```

The stored-certificate validator checks byte-identical full Gram reproduction, both source/native input SHA256 hashes, all exact endpoint grids and widths, symmetry and delta. It independently evaluates the stored negative direction against the exact full native and Gram endpoint matrices, verifies its strictly negative corrected-estimator upper bound and strictly positive native lower bound, and verifies that no actual negative witness or whole-domain positivity is asserted. Two complete checks agree byte for byte. A changed-source-hash control is rejected, and the original file is restored and compared byte for byte afterwards.

The complete source certificate, outward native matrix, complement, complete Gram, both validation reports, constructors, definitions and this proof note are committed together. The full source and Gram files are Git blobs referenced by the commit tree, with exact content readback. Historical 81/100 notes and certificates remain intact.

## Remaining scope

This completes the lawful 41/50 constructors and matching actual source/Gram enclosure and records an exact obstruction for the current no-lift estimator. The certified actual whole-domain positivity frontier remains 81/100. The complete Gram can be reused for sharper inverse or lift estimates without repeating its construction. An enlarged finite space instead requires a correspondingly enlarged actual complement and source projection.

No historical selected off-line packet is instantiated. Global endpoint exclusion, actual endpoint existence, all-window unit domination, selected inverse-response certification and retained witness/null attachment remain open. F4 and FULL TRANSPORT CLOSED remain open. No Lean, axiom or workflow edits; no CI run is requested.
