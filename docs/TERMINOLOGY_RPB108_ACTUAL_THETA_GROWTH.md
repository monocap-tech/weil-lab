# RPB-108: actual theta growth ingredients

`neutralActualZetaThetaRemainder t` is the actual zero-parameter even theta kernel minus its constant term: `HurwitzZeta.evenKernel 0 t - 1`. This is the kernel entering Mathlib's actual completed-zeta Mellin construction.

The global exponential majorant means there are positive constants p and C, obtained from the actual kernel, for which |remainder(t)| ≤ C exp(-p t) for all t ≥ 1. Compactness supplies the finite initial interval; the pinned actual-kernel decay theorem supplies the tail.

The polynomial moment majorant is C n!/(p/2)^n exp(-(p/2)t). The moments on (1,∞) are integrable and bounded by C n!/(p/2)^n exp(-p/2)/(p/2), with the same actual constants for every natural n.

These are analytic growth ingredients, not an entire-circle growth-rate certificate, local logarithmic zero count, infinite sampling estimate, or WD-T38 coefficient identification. All of those downstream obligations remain open. Spectral L2 remains unproved and unassumed.
