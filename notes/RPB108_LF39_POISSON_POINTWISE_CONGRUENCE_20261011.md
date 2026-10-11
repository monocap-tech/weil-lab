# RPB108 — LF39: Poisson pointwise congruence

## Recovered validation

LF38 commit `321eb19fd122802b62c64bd90ea556f8a591e334`, Lean run `38147541909`, job `114493944760`, recompiled TrialJump but failed PoissonAction. At line 56, simplification retained subtraction of functions inside Integrable, while the target used a pointwise lambda. At line 69, the attempted Pi.sub_apply simplification of the integral-subtraction equation made no progress. Downstream mixture/truncated modules were not built; root and unfinished-declaration checks were skipped.

## Repair

Transfer integrability from the difference of the two integrable products using Integrable.congr and an explicit everywhere-valid sub_mul identity. Remove the non-progressing simplification of the already pointwise integral-subtraction equation; retain beta reduction before rewriting. Statements, definitions, and hypotheses remain unchanged.

## Evidence boundary

LF39 is submitted for CI; no local Lean executable is available. TrialJump is module-checked by LF37 and LF38. LF28 remains the last successful complete-root checkpoint. PoissonAction and its downstream modules await checking. Cutoff removal, physical weak attachment, L2 convergence, and spectral identification remain open. No aperture, F4, or RH claim.
