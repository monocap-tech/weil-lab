# RPB-108 terminology: spectral operator-domain source regularity

The exact spectral product is `neutralWeilSpectralProduct`: the right-limit
Weil symbol in mathlib frequency multiplied by the L2 Fourier transform of
the actual physical carrier. Operator-domain membership means this product
belongs to L2. It is an explicit witness obligation, stronger than finite
one-logarithm quadratic form energy.

The operator-domain core is the inverse L2 Fourier transform of that product.
Its equality with the actual tempered multiplier core is proved from a.e.
product laws and L2/tempered Fourier compatibility. It is a constructed L2
representative, without any pointwise exponential growth claim.

The operator-domain defect is this core plus the actual physical pole minus
the existing zero-continued exterior residual candidate. It is locally
integrable and represents the actual compact source defect. Boundary removal
can therefore consume it once actual central source cancellation is proved.
The construction does not prove operator-domain membership for the actual
carrier or obtain it from form-domain membership.
