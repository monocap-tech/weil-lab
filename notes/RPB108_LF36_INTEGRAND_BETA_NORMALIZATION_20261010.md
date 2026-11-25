# RPB108 LF36 — Normalize rewritten integral functions

## Change

After rewriting the TrialJump pointwise partition, beta-normalize the rewritten
integrand before applying integral additivity. Make the same adjustment after
the function equality rewrite in TruncatedJump's inner complex mixture.
No definition, theorem statement or hypothesis changes.

## Validation evidence

LF35 run 38110108787 job 114384522440 passed the previously failing exterior
indicator transport. TrialJump now reported only the integral-additivity
rewrite mismatch at line 97: the target still had `(fun y => ...) y`.
Its convergence theorem produced no diagnostic, but the whole module remained
failed and downstream Poisson/cutoff modules remained unbuilt. LF36 removes
that exact beta-redex before applying the rewrite and addresses the analogous
downstream function-rewrite pattern.

LF28 remains the latest complete-root success, run 38107491130. LF36 is
submitted for fresh cumulative kernel checking. No unfinished proof or
project axiom is introduced. Absence of diagnostics in individual proofs is
not claimed as an independent compilation certificate.

## Next cursor

Resolve fresh diagnostics, then establish truncated-kernel convergence and
cutoff removal with the actual full-jump majorant. Weak attachment, L2
convergence and spectral source identification remain open. No new aperture
positivity, F4 or RH claim.
