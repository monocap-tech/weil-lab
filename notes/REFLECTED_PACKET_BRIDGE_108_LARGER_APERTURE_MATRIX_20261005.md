# RPB108: native twenty-vector restriction at aperture 51/100

Base: f131e274e390d2ae46cf6e15ea45a4f571740966.

## Definitions and result

The larger-aperture native matrix is the restriction of the actual form Q_a to the twenty orthonormal physical vectors e_n(x)=sqrt((2n+1)/(2a)) P_n(x/a), 0<=n<20, at a=51/100. Its entries are the same-vector native mixed form Q_a(e_i,e_j). This is the raw restriction; the corrected Schur form also subtracts the actual complement lift energy.

Exact rational interval elimination proves

Q_a(e,e) > (1/2000000)||e||_2^2

for every nonzero vector e in this twenty-dimensional subspace. All twenty shifted pivots are positive. The previous uniform complement certificate supplies physical coercivity 2/5 and logarithmic coercivity 9/100 at this aperture, but the actual coupling correction is still uncomputed here.

## Aperture-dependent construction

The existing native constructor is extended only to the exact rational aperture 51/100 and only for its degree-19 matrix return. Other newly requested apertures continue to be rejected. The quarter- and half-aperture calculations are preserved.

Set L=4a=51/25. The existing correlation polynomial has coefficients a*2^k times the unit Legendre correlation coefficients, so the constructor already scales the native correlation correctly. The physical prime-2 shift is y=log(2)/(2a), and the prime term is included at this aperture. Rational logarithm checks establish log(2)<2a<log(3), so no additional prime power contributes.

Pole moments are recomputed with this a and the actual exponent exp(x/2). The archimedean series uses this L in every exponential and Bernoulli coefficient. No half-aperture matrix or pole moment is substituted.

The audited exponential remainder multiplier 9 remains valid because L<log(9). The audited kernel multiplier 3 remains valid: L>log(4) implies exp(-L)<1/4, and L<9/4 gives L/(1-exp(-L))<3. The kernel is increasing on the real integration interval, so this bounds it throughout. The existing Bernoulli-tail estimate is evaluated with the new L; L/6<1. Gamma and pi enclosures are aperture-independent. Exponential order 80, Bernoulli pairs 60, gamma order 12, and outward interval grid 10^-120 are retained.

The unnormalized matrix is converted to the stated orthonormal basis by multiplying each entry by sqrt((2i+1)(2j+1))/(2a). Omitting the denominator would change the claimed physical norm margin. Exact reflection parity still makes every odd mixed entry zero.

## Validation

The new certificate reproduces exactly. All twenty shifted interval pivots are positive, every odd mixed entry is exactly zero, and replacing the first diagonal by -1 is rejected. The largest entry enclosure width is below 10^-25.

At a=1/2 the extended constructor reproduces every matrix interval, every raw pivot, and every shifted pivot of RPB108_NATIVE_TWENTY_MATRIX_CERTIFICATE_20261005.json exactly. The new matrix differs from the half-aperture matrix as required. These checks validate the rational calculation and regression; the analytic remainder justification is given above.

Artifacts: scripts/certify_native_larger_aperture_matrix.py and notes/data/RPB108_LARGER_APERTURE_MATRIX_CERTIFICATE_20261005.json. The underlying scripts/certify_native_legendre_small_window.py receives the narrowly scoped aperture extension.

## Next obligation and status

Rebuild the full twenty-source residual Gram at a=51/100 on these same vectors. The existing smooth-source script uses t=x+1/2, endpoint panels based on log(2), and half-aperture pole moments. It must use the aperture-scaled coordinate t=(x+a)/(2a), prime shifts log(2)/(2a), the appropriately scaled endpoint logarithm and smooth kernel, and the actual pole moments and physical normalization. All mixed source terms and the induced Gram operator error must be retained. Its current half-aperture JSON is not a larger-aperture Gram enclosure.

Only after bounding Q_20(a)-(5/2)R_20(a), including the actual Gram error, can the existing square-completion route establish a larger-aperture whole-domain bound. The certified finite restriction alone does not control the complement correction.

Whole-domain positivity above 1/2, global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. The promoted full-domain checkpoint remains 901aa29. Lean source, axioms and prior CI claims are unchanged; this certificate is not Lean formalized.
