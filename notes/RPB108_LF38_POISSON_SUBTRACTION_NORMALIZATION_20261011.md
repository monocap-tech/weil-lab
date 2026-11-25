# RPB108 — LF38: Poisson subtraction normalization

## Evidence recovered

LF37 commit `ca62a4189fd2376580f70c4d8b6249829b561b4f`, Lean run `38111780095`, job `114388672533`, compiled `NeutralLogMetricTrialJump`. This validates its full-line spatial integrability, exact internal/exterior integral split, and endpoint-candidate identity. The cumulative targeted build then failed in `NeutralLogMetricPoissonAction` at lines 56 and 68. The root build and unfinished-declaration check were skipped. LF28 remains the latest successful full-root checkpoint.

## Change

Normalize function subtraction with `Pi.sub_apply` in the integrability proof. Instantiate the integral-subtraction theorem, normalize its pointwise application and beta-redexes, then rewrite the cancelled action using that equation. These are proof elaboration repairs; no theorem statement, domain, definition, or mathematical hypothesis changes.

## Validation boundary

LF38 is submitted for fresh CI validation; no local Lean executable is available. The Poisson-action module and downstream mixture/truncated-kernel modules are not yet certified. Cutoff removal, physical weak attachment, L2 convergence, and spectral source identification remain open. No aperture positivity, F4 closure, or RH claim follows.
