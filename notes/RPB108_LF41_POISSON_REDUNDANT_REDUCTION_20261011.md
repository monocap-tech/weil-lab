# RPB108 — LF41: remove redundant Poisson reduction

## Compiler evidence

LF39 commit d3e225fc27dd5e176f99b3744f820d8710930345, run 38148324601 job 114496270980, completed with failure. TrialJump recompiled. The sole PoissonAction diagnostic was line 75: dsimp made no progress. The earlier integrability-congruence proof produced no diagnostic, but the module as a whole did not compile. Downstream modules were not built, and root/unfinished-declaration checks were skipped.

## Repair

Remove the redundant dsimp only at hsub and the goal. The instantiated integral_sub equation is already reduced after simp_rw sub_mul, so this mandatory non-progressing tactic prevents the subsequent rewrite from being attempted. No theorem statement or mathematical hypothesis changes.

## Evidence boundary

LF41 awaits CI. LF40's generic time-exhaustion convergence theorem remains submitted and unverified; its run was in progress at preparation and inherits the same PoissonAction blocker. LF28 remains the latest full-root success; LF37/LF38/LF39 provide module-level TrialJump evidence. A concrete exhausting interval sequence, spatial cutoff removal, weak attachment, L2 convergence and spectral source identification remain open. No new aperture positivity, F4 closure or RH claim.
