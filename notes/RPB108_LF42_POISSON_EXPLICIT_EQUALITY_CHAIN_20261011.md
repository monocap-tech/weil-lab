# RPB108 — LF42: explicit Poisson equality chain

## Compiler evidence

LF41 commit 058f987cebeb81e92a25111461797309c7d7d2ab, run 38148981590 job 114499294730, recompiled TrialJump but failed PoissonAction at the integral-subtraction rewrite. Lean displayed identical pointwise integrands for the rewrite pattern and target, but did not match them. The earlier integrability proof produced no diagnostic. The module as a whole remained uncompiled; downstream targets and the root checks were not reached.

## Repair

Replace rewriting by the instantiated subtraction equation with a calc chain whose intermediate result explicitly states the difference of the two product integrals. Supply integral_sub directly to that equality step, then evaluate the constant product integral using the complex cast identity and the translated Poisson unit-mass theorem. Statements and hypotheses are unchanged.

## Primary source

Pinned Mathlib revision 5ed2965256430c3649e86755f9576b54eca72435, MeasureTheory/Integral/Bochner/Basic.lean: integral_sub directly proves the pointwise difference integral equals the difference of integrals from the two integrability premises.

## Validation boundary

LF42 awaits CI; no local Lean executable is available. LF28 remains the latest full-root success, and TrialJump has module-level compilation evidence. LF40's time-exhaustion theorem and all modules downstream of PoissonAction remain submitted but unverified. Concrete exhaustion, spatial action convergence, physical weak attachment, L2 convergence and spectral identification remain open. No aperture positivity, F4 closure or RH claim.
