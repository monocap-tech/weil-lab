# RPB108 LF15: jump sign repair and module checkpoint

LF14 run 38099142951, job 114351242653, compiled the physical-source,
endpoint-source, Laplace, Poisson and PoissonMass modules. This provides
module-level kernel evidence for LF05 through LF08 after the repairs.
The Poisson warnings were unused-tactic/style warnings, not unfinished
declarations. No `declaration uses sorry` warning occurred in this run.

The targeted build then failed in `NeutralLogMetricJumpBounds`, preventing
LF10 through LF13 from being reached and skipping the complete root check.
LF01 through LF04 remain the full-root checked boundary.

## Repair submitted

Two exponential majorant proofs attempted to show `-exp(1)*t <= 0` by
nonlinear arithmetic with t>0. The tactic normalized exponential terms
without closing the sign contradiction. Replace both calls with the direct
ordered-ring multiplication lemma, using `-exp(1) <= 0` and `0 <= t`.
No theorem statement or hypothesis changes.

## Validation boundary

LF15 requires another cumulative targeted build and full-root build.
LF09 through LF13 remain unchecked. Module evidence for LF05 through LF08
does not imply that the complete root has passed. There is no local Lean
executable; source scans do not substitute for compilation. Research refs
and the pinned PR base remain unchanged.

## Next cursor

Resolve remaining LF09 onward elaboration diagnostics, then establish
actual endpoint-source square integrability using LF13's logarithmic
majorant. Mixture exchange, zero-extension splitting, physical L2 limit
attachment and identification with the spectral source remain open. No
new aperture, F4, Green-domain identification or RH claim is made.
