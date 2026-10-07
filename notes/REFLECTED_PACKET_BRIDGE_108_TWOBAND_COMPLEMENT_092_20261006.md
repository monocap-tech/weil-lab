# RPB108: two-band archimedean comparison at 23/25

Definitions: [two-band comparison](../docs/TERMINOLOGY_RPB108_TWOBAND_COMPLEMENT_092.md).
Lane: aperture. The complete native, source and nine-panel Gram inputs of
the preceding obstruction checkpoint are reused without modification.

## Analytic comparison

The retained actual archimedean estimates are m(t)>=-27/5 everywhere and
m(t)>=g(|t|) for |t|>=1, where g(u)=log(u)-7/(216u^2).
Since g'(u)=1/u+7/(108u^3)>0, for 1<=S<T we have the pointwise lower bound

\[
m(t)\ge g(T)-(g(T)-g(S))1_{|t|<T}
                   -(g(S)+27/5)1_{|t|<S}.
\]

The right side equals -27/5, g(S), or g(T) on the three regions.
For f in W_84, integration against the actual nonnegative Fourier density,
Plancherel and the two complete mass bounds therefore give

\[
Q_a(f)\ge\{g(T)-(g(T)-g(S))\rho(T)
                    -(g(S)+27/5)\rho(S)-L_{24}-L_{35}-P\}\|f\|_2^2.
\]

L_24 and L_35 are the unchanged actual joint prime-chain norm bounds;
P is the unchanged signed pole allowance. Both coefficients multiplying
mass are positive, so replacing mass by its upper bound has the correct
inequality direction. For endpoint rounding, the constructor uses the
lower endpoint of g(T) in the leading term, upper g(T) minus lower g(S)
for the outer coefficient, and upper g(S)+27/5 for the inner coefficient.

Choose S=263/20 and T=72/5. Both arguments remain inside the proved
positive Bessel region and all 48 integrated rates are positive.
The exact outward lower bound is approximately 0.6855142242160204,
so the physical complement bound is c=17/25. The independent logarithmic
complement bound 9/100 is retained. No new tail degree is discarded.

The improvement removes the prior unnecessary global-floor charge on the
outer frequency band. Merely increasing finite damping depth was not the
main source of loss. Exploratory cutoff searches select the parameters;
only the exact rational constructors and independent audits supply proof.

## Validation and scope

The constructor records separate complete legacy mass certificates for
both cutoffs. The independent audit applies the existing separate
polynomial recurrence, all 48 degree bounds, infinite tail, rate and
positive-region checks to each, then recomputes the two-band endpoint sum
and checks all three pointwise regions. Prime/pole/logarithmic custody is
unchanged. Repeat and full corrected sign are recorded separately.

## Complete corrected sign

The matching sign constructor pins the unchanged native, source and Gram
hashes and the new complement hash. It checks Q-(25/17)R with the full
operator error delta, finds a strictly positive shifted margin, and retains
all 84 corrected pivots. The physical/logarithmic norm conversions use the
same exact determinant identity as the prior certified aperture.

Both sign outputs repeat byte for byte. The independent whole-form audit
rebuilds all 84 corrected pivots at a wider 80-digit grid, recomputes the
source error and both conversion determinants, and rejects the negative
diagonal and oversized-conversion controls. Its repeat is byte identical.
The certified conversions give approximately
1.1630174590320121e-26 physical coercivity and
5.056597647965271e-29 logarithmic coercivity, hence

\[
Q_a(h)\ge10^{-26}\|h\|_2^2,\qquad
Q_a(h)\ge5\cdot10^{-29}E_{\log}(h),\quad a=23/25.
\]

This closes whole-domain positivity at 23/25, excludes fixed-aperture weak
null modes and supplies the existing unit-domination consequence there.
No actual negative full-form witness has been constructed.
Global endpoint exclusion, historical attachment, F4 and full transport
remain open. Lean and workflows are unchanged.

## Custody

- `scripts/certify_native_prime5_twoband_complement84_092.py`
- `scripts/validate_native_prime5_twoband_complement_092.py`
- `scripts/certify_native_prime5_twoband_schur84_092.py`
- `scripts/validate_native_prime5_twoband_whole_092.py`
- `notes/data/RPB108_PRIME5_TWOBAND_COMPLEMENT84_092_CERTIFICATE_20261006.json`
- `notes/data/RPB108_PRIME5_TWOBAND_COMPLEMENT_092_VALIDATION_20261006.json`
- `notes/data/RPB108_PRIME5_TWOBAND_SCHUR84_092_CERTIFICATE_20261006.json`
- `notes/data/RPB108_PRIME5_TWOBAND_WHOLE_092_VALIDATION_20261006.json`

Prior obstruction evidence remains historically correct for its named
scalar estimate. No earlier certificate, failed direction or proof body
is rewritten by this comparison improvement.
