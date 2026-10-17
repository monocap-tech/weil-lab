# RPB108 LF16: preserve the damping parameter in exponential comparison

LF15 run 38099693336, job 114352881170, compiled the physical-source,
endpoint-source, Laplace, Poisson and PoissonMass modules again. The targeted
build stopped in JumpBounds before reaching the later endpoint estimates.
The complete root and unfinished-declaration check were skipped.

## Precise diagnostic and repair

The prior proof began with `rw [<- Real.exp_zero]`. Rewriting all matching
ones changed not only the target upper bound 1, but also the damping
parameter inside `exp(1)` to `exp(exp(0))`. The intended direct positivity
proof then had a syntactic type mismatch. This explains both sign failures
and why LF15's direct sign lemma alone did not repair them.

Use an explicit calculation: compare `exp(-exp(1)*t)` with `exp(0)` using
the sign of the product, and only then evaluate that terminal `exp(0)` as
one. Both time-domination proofs retain the original damping expression.
No theorem statement or assumption changes, and no new declarations are added.

## Validation boundary

LF01 through LF04 retain full-root build evidence; LF05 through LF08 have
repeated module-level compilation evidence. LF09 onward remain unchecked
pending the new cumulative targeted build and complete root. There is no
local Lean executable; source review is not kernel certification. The
research refs and pinned PR base remain unchanged.

The next cursor is to clear the downstream diagnostics, then prove actual
endpoint-source square integrability from the logarithmic majorant. Mixture
exchange, zero-extension splitting, physical L2 convergence and spectral
source identification remain open. No aperture, F4 or RH claim is made.
