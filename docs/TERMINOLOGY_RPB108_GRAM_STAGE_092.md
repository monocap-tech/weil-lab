# RPB-108 complete Gram stage at aperture 23/25

- **Complete panel checkpoint:** the input-bound CS, smooth and cross
  contraction matrices after all nine actual support panels are integrated.
  It contains every retained mixed term, but does not decide corrected sign.
- **Residual Gram surrogate R:** the 84-by-84 matrix formed by adding the
  endpoint-log residual Gram, smooth-source Gram and both endpoint-log/source
  cross terms, and removing all 84 retained projection components.
- **Source approximation error eta:** the physical L2 operator error between
  the actual 84-source map and the quantized polynomial approximation.
- **Gram error delta:** eta(2M+eta), where M bounds the norm of the surrogate
  residual source map. It transfers the surrogate Gram to the actual Gram.
- **Corrected finite matrix:** Q-beta R-beta delta I, where Q is the matching
  native finite restriction and beta is the inverse of a certified complete
  complement lower bound. Its positive sign is a separate obligation.
- **Gram/sign boundary:** the first call to the unchanged constructor's
  positive-pivot routine, after complete R, native/source pairing checks,
  source norm, delta and certificate fields have been computed. Export at
  this boundary preserves the complete Gram while leaving its sign pending.

The extraction wrapper observes the completed result at this precise call,
checks that the caller is the original compute function and the argument is
its G matrix, and aborts before sign computation. It changes no numerical
operation before that boundary. The original constructor file and all
checkpoint bindings remain unchanged.

Neither a complete panel checkpoint nor a residual Gram certificate alone
is a whole-domain positivity certificate. All data remain on the actual
23/25 aperture; no historical packet attachment or global/F4 closure is
inferred.
