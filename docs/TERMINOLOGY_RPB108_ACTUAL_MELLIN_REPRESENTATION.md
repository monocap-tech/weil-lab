# RPB-108: actual reflected Mellin representation

`neutralActualZetaThetaTailKernel` is the actual complex theta remainder on (1,∞), extended by zero elsewhere. Its Mellin transform is exactly the previously defined complex tail integral.

The reflected tail kernel is `t^(−1/2) • neutralActualZetaThetaTailKernel(t⁻¹)`. It represents the small-t part of Mathlib's actual modified even FE-pair kernel. Both kernels are Mellin-convergent for every complex exponent.

The actual half-sum identity identifies `completedRiemannZeta₀ z` with half the sum of the tail integrals at `z/2` and `(1-z)/2`. Mathlib's Mellin inversion accounts for the Jacobian. This is a representation identity for the actual function; an explicit disk/circle growth estimate remains separate.

The completed-zeta disk bound is the same factorial tail bound, obtained by the half-sum identity and triangle inequality. The pole-cleared factorial majorant `neutralActualZetaFactorialMajorant p C n` is
n(n+1) C n!/(p/2)^n exp(-p/2)/(p/2) + 1.

This majorant bounds the actual entire function on ‖z‖ ≤ n. For enclosing radius 2(|T|+2) ≤ n it bounds the existing actual circle envelope. Jensen then bounds the actual height-window multiplicity count by its logarithm divided by log 2. The radius condition merely chooses a large enough natural moment order; it supplies no independent zero-count data. The O(T log T) conversion and local sampling estimates remain separate.
