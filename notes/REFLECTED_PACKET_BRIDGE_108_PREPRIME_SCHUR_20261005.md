# RPB108: whole-domain sign at the pre-prime-3 aperture 27/50

Base: be3a1fc2ff49d500cc47a3f3f827d4ae0d1aa1c4.
Definitions: docs/TERMINOLOGY_RPB108_PREPRIME_SCHUR.md. The supported logarithmic form domain, actual native mixed form, physical twenty-vector basis, residual projection, and exact lift-corrected Schur form retain the definitions of the preceding 51/100 certificate.

## Result and aperture consequence

At a=27/50, exact rational arithmetic and the actual source/complement estimates give

S_20 > (1/20000000)I,
Q_a(h) >= (1/1480000000)||h||_2^2 for every supported logarithmic form-domain h.

The weak kernel is zero, and the established same-vector energy/factorization criterion supplies full-source WD-T10 unit domination at this aperture. Physical inclusion gives the same physical lower bound on smaller supported domains. Under the existing canonical positivity-aperture theorem, the first positive endpoint must lie strictly above 27/50 or be absent. The theorem does not exclude a finite endpoint farther out.

## Uniform complement

Only prime 2 is active because log(2)<1<=2a<=27/25<log(3), as checked with rational logarithm enclosures. With k=20 and T=43/10, use the previously proved scaled integrated-Bessel observation majorant

rho(a,T)=4aT [2a(22/7)T]^40 / [(41!!)^2(1-q)],
q=[2a(22/7)T]^2/(41*43),
p(a)=16a(a/2)^40/(20!)^2.

Both majorants increase with a on this interval. The actual high symbol lower bound is c=log(T)-1/(2T)-sqrt(2)log(2); the low symbol lower bound remains -10. At a=27/50 the physical complement bracket c-(10+c)rho-p is greater than 0.3384968001146, hence greater than 1/3. At logarithmic cutoff 4, the bracket 1/10-(51/5)rho(a,4)-p is greater than 0.0988250915990, hence greater than 9/100.

Thus the twenty-moment complement has physical coercivity 1/3 and logarithmic coercivity 9/100 uniformly for 1/2<=a<=27/50. The latter supplies the lawful form-domain lift; the former gives inverse factor 3. No physical spectral operator-domain membership is assumed.

## Independently recomputed native matrix and sources

The native constructor is narrowly extended to rational aperture 27/50 for its degree-19 matrix return. The same rational checks validate the old remainder constants at L=4a=54/25: L<log(9), log(4)<L<9/4, and L/6<1. Native correlations, pole moments, prime shift log(2)/(2a), and orthonormal normalization sqrt((2i+1)(2j+1))/(2a) are all recomputed.

The raw matrix is positive, but the prior raw shift 1/2000000 fails its interval pivot check. Halving the proposed shift until all twenty interval pivots pass certifies the smaller raw margin 1/16000000. Unshifted positivity and negative diagonal rejection remain verified. This failed stronger margin is not a negative actual-form witness.

The source calculation uses d=2a=27/25 and t=(x+a)/d. It recomputes A_d(s)=(1/2)B(2ds)exp(-ds/2), its integrated endpoint-H polynomials, the constant -gamma-log(2pi)-log(d), the physical pole moments including the measure factor d, and the exact prime panels cut at log(2)/d and 1-log(2)/d. The endpoint logarithm L(t)=-(log t+log(1-t))/2 is retained exactly. The analytic error and physical L2 normalization are those proved in REFLECTED_PACKET_BRIDGE_108_LARGER_APERTURE_SCHUR_20261005.md, with the new d in every bound. The combined source-map error is below 3.30e-27.

## Full residual Gram and corrected sign

All log/log, smooth/smooth, both log/smooth mixed terms, and physical projection products are included in the full twenty-source Gram. Rational primitive integration uses the exact interval-enclosed prime endpoints and outward grid 10^-120. The normalized coordinate's measure factor cancels the two source normalization factors; it does not eliminate the aperture dependence of the actual smooth sources.

All 400 source/native pairings agree within their certified source errors; their maximum discrepancy is below 2.94e-34. The actual residual Gram operator error delta=eta(2M+eta), with M bounded by the square root of the surrogate trace, is below 1.12e-26. The maximum entry enclosure width is below 1.22e-52. The source and native JSON byte hashes are pinned.

Interval elimination certifies Q_20-3Rtilde_20-3delta I-(1/20000000)I>0. The larger initial corrected shift 1/10000000 does not pass, while its half does. These are certified sufficient margins, not assertions of optimal coercivity. Replacing the first diagonal of the checked lower matrix by -1 is rejected.

The lift squared norm bound is 9[trace(Rtilde_20)+delta]<25.817<36, giving ||z_e||_2<=6||e||_2. With h=e+f and v=f+z_e, exact square completion gives Q_a(h)=S_20(e,e)+Q_a(v). Orthogonality of e and z_e yields ||h||_2^2<=74||e||_2^2+2||v||_2^2. Hence the whole-domain margin is (1/20000000)/74=1/1480000000. The complement margin 1/3 exceeds twice this number.

## Validation and cursor

The scalar complement, native matrix, and source certificates reproduce exactly. At 51/100, the extended native/source constructors reproduce the previous matrix certificate and all source data exactly. The complete 27/50 Gram certificate reproduces byte-for-byte. All source/native pairing checks and shifted rational interval pivots pass. Matrix and corrected-form negative diagonal controls are rejected; the scalar invalid-ratio control is rejected. The analytic estimates above justify what the arithmetic certifies.

Artifacts: scripts/certify_native_preprime_{complement,matrix,source,gram}.py and notes/data/RPB108_PREPRIME_{COMPLEMENT,MATRIX,SOURCE,GRAM}_CERTIFICATE_20261005.json. Historical data and conclusions are unchanged. The native constructor's additional aperture is explicitly guarded.

Next: cross prime 3's activation at log(3)/2 (approximately 0.5493061443) with its actual translation, source panel cuts, amplitude and mixed Gram terms, or pursue independent global endpoint exclusion. No continuity argument permits silently omitting that term beyond activation. Estimates here stop at 27/50; the interval from 27/50 to activation is not newly certified by these data.

Global endpoint exclusion, all-window unit domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged; this analytic/rational certificate is not Lean formalized.
