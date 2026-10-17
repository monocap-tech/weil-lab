# RPB108 LF18: endpoint inverse-square rewrite repair

LF17 run 38102261349, job 114360445128, compiled the finite-cap JumpCap
module successfully. The checked module boundary now includes LF05 through
LF10. Complete-root validation remains LF01 through LF04.

The next failure was in EndpointBounds: both inverse-square comparison
proofs attempted `Real.rpow_neg` while their goals still contained applied
anonymous functions. LF18 explicitly changes these goals to pointwise
equalities, with the real exponent written as `-(2 : ℝ)`, before applying
the negative-power and square identities. The statements and analytic
assumptions are unchanged.

EndpointBounds and EndpointLog still require a fresh cumulative check.
The full-root and unfinished-declaration checks were skipped after the
targeted failure. There is no local Lean executable. No hand-written sorry,
admit or project axiom is introduced. Research refs remain untouched.

After downstream compilation, the next analytic frontier is actual
endpoint square integrability from the logarithmic majorant. Mixture
exchange, zero-extension splitting, physical L2 convergence and spectral
source identification remain open. No aperture, F4 or RH claim is made.
