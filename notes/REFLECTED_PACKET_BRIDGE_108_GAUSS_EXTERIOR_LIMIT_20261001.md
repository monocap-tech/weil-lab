# RPB-108 — quantitative exterior finite Gauss convergence

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `d1649813180a75d93222e0fffc0f1d9e14df7fe8`.

## Uniform geometric kernel error

The exact finite geometric remainder gives, whenever |z|≥δ>0,

    |K_N(z) + signedGapKernel_δ(z)| ≤ exp(-2δ)^N / (1-exp(-2δ)).

The signed gap kernel is negative. The finite kernel is positive, so its
limit is the negative of that signed kernel. The denominator is strictly
positive, and the geometric ratio lies strictly between zero and one.

## Actual rough-carrier convergence

The actual finite convolution is exactly its compact carrier integral.
Its integrand is genuinely integrable by compact L1 membership and the
continuous finite kernel. For x outside (-a,a), every displacement from
y in [-c,c] has absolute value at least a-c>0. Integrating the uniform
kernel bound gives

    ‖finiteConvolution_N(x) + signedGapFunction_(a-c)(x)‖
      ≤ compactL1Mass(h) exp(-2(a-c))^N / (1-exp(-2(a-c))).

This bound is independent of the exterior point x. It uses actual L1
mass and imposes no pointwise boundedness or smoothness on h. Geometric
decay and the norm criterion give actual pointwise convergence of the
finite convolution to the negative of the signed gap function throughout
the exterior.

## Remaining obligations

This closes the finite physical convolution's exterior limit. It does
not close the shifted digamma action's support-separated estimate or weak/
operator limit. That action is still the remaining term in the certified
exact operator split. No singular whole-line Gauss integral or whole
archimedean source identity follows from the exterior limit alone.

Whole residual/source attachment, central cancellation, boundary
reconstruction and actual source-domain/quadratic/polarization/normalized
estimate witnesses remain open. Threshold bookkeeping is closed;
logarithmic coercivity has not started. Canonical Weil, main and WD-T40
mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,968 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `3650789ba52f28a3c08c8f7e49c0881c9bc62e34`,
run `36964811880`, job `110706170139`, source blob
`9ec7fdf7e472a0b602482c1089a22ab7d7005eb8`.

Validation-only workflow/cache changes
are excluded from research promotion; prior checkpoint notes are immutable.
