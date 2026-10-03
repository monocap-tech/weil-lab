# RPB-108: actual reflected Mellin representation

`neutralActualZetaThetaTailKernel` is the actual complex theta remainder on (1,∞), extended by zero elsewhere. Its Mellin transform is exactly the previously defined complex tail integral.

The reflected tail kernel is `t^(−1/2) • neutralActualZetaThetaTailKernel(t⁻¹)`. It represents the small-t part of Mathlib's actual modified even FE-pair kernel. Both kernels are Mellin-convergent for every complex exponent.

The actual half-sum identity identifies `completedRiemannZeta₀ z` with half the sum of the tail integrals at `z/2` and `(1-z)/2`. Mathlib's Mellin inversion accounts for the Jacobian. This is a representation identity for the actual function; an explicit disk/circle growth estimate remains separate.
