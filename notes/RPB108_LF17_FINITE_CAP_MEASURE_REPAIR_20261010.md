# RPB108 LF17: finite-cap constant-integrability repair

LF16 run 38101145659, job 114357156263, compiled JumpBounds successfully.
The module-level checked boundary now includes LF09's actual off-diagonal
jump-integral convergence, reciprocal majorant and Lipschitz cancellation,
as well as the repaired LF05 through LF08 modules. Full-root validation
still remains LF01 through LF04 because the targeted build failed later.

## Observed LF10 diagnostic and repair

The finite-cap integral norm theorem invoked `integrableOn_const` with its
default finite-measure proof. The default aesop search could not close
`volume(Icc(-B,B)) != top` within its rule-depth limit. The identical finite
measure obligation was already proved explicitly by simplification in the
preceding spatial-integrability theorem.

Supply that same explicit interval-volume proof to `integrableOn_const`.
No theorem statement, modulus, cap hypothesis or analytic assumption is
changed. The correction addresses elaboration of a genuine finite-measure
fact rather than increasing tactic search limits.

## Validation and cursor

LF10, LF12 and LF13 remain unchecked pending the fresh cumulative targeted
build. The complete root and unfinished-declaration check were skipped
after the LF10 error. No local Lean executable is available. The branch
lease and pinned PR base are preserved; research refs remain unchanged.

Resolve any downstream compiler diagnostics, then establish actual
endpoint square integrability from the logarithmic majorant. Mixture
exchange, zero-extension splitting, physical L2 convergence and spectral
source identification remain open. No new aperture, F4 or RH claim is made.
