# RPB-108 — actual complex Mellin tail comparison (2026-10-03)

Parent promoted head: `0e42a95623513527ed8c13b779cbf9d43496ca90`.

The new source connects the existing actual theta polynomial moments to complex Mellin weights. For s.re - 1 ≤ n and t ≥ 1, the norm of t^(s-1) K(t) is bounded by t^n |K(t)|. This proves integrability of the complex tail over (1,∞) and the same actual factorial norm bound, with p and C independent of s and n.

On ‖z‖ ≤ n, the two exponents z/2 and (1-z)/2 both satisfy this moment condition. No zero-count input, packet representation or spectral operator-domain assumption enters the argument.

## Next analytic obligation

Mathlib defines completedRiemannZeta₀ through the modified FE-pair Mellin kernel over (0,∞). The small-t modified kernel must be transported under t ↦ 1/t, with the measure Jacobian retained. The intended identity is

completedRiemannZeta₀(z) =
  (I(z/2) + I((1-z)/2)) / 2,

where I(s) is the actual tail integral defined by the new integrand. This identity has not been certified by this chunk.

A concrete formal route is to express the actual modified FE-pair kernel as the large-t remainder plus a t^(-1/2)-weighted inverted large-t remainder (up to the irrelevant value at t=1). The existing pinned `mellin_cpow_smul` and `mellin_comp_inv` theorems then transport the second piece to exponent (1-z)/2, with the Jacobian already included. Integrability must be provided before splitting the integral.

After identification, triangle inequality would bound the entire completed term by the common factorial majorant B_n. Pole clearing would then give a disk bound
‖z(z-1) completedRiemannZeta₀(z) + 1‖ ≤ n(n+1) B_n + 1
for ‖z‖ ≤ n. Neither this actual entire-function bound nor its logarithmic O(R log R) conversion is claimed here.

Cumulative divisor growth, local unit-height logarithmic bounds and logarithmic-domain sampling boundedness remain separate obligations. The current cursor is the small-t reflected Mellin identity followed by pole-clearing and circle-envelope growth.

WD-T38 source/null attachment and enlarged central cancellation remain open. Spectral L2 remains unproved and unassumed. Threshold closed; F-4 pending; RH standing unchanged.

## Validation

Exact candidate `bd69341e8aec0243e08381446c6d37ea17cf7aea` passed [run 37160286394](https://github.com/monocap-tech/weil-lab/actions/runs/37160286394), job `111312154237`. The isolated module and full `lake build WeilDefect` passed (3,205 and 9,049 jobs). All three theorem audits report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed. Source, root import and terminology are promoted without the validation workflow.

The runner saved the compiled project/dependency cache under `rpb108-mellin-growth-compiled-v1`. Reuse the existing validation branch and draft PR #35 for the next bounded analytic chunk, retaining access to this validation cache.
