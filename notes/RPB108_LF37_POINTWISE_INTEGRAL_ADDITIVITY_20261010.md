# RPB108 LF37 — Pointwise integral additivity normalization

## Change

Instantiate the two integral-additivity equations separately and normalize
function addition with `Pi.add_apply` in those equations before rewriting the
pointwise three-region partition. LF36 already removed the lambda application;
this addresses the remaining distinction between `(f+g)(y)` and `f(y)+g(y)`
in the rewrite patterns. Definitions, hypotheses and conclusions are unchanged.

## Validation evidence

LF36 run 38111299026 job 114387250084 failed TrialJump at line 98 with only
the additivity rewrite mismatch. The target's beta-redex was gone, while the
lemma pattern retained function addition. LF37 normalizes the instantiated
lemmas explicitly. Other TrialJump proofs produced no diagnostic, but the
module remained failed. Downstream Poisson and cutoff modules were unbuilt.
LF37 is submitted for fresh cumulative kernel checking.

LF28 remains the latest full-root success (run 38107491130), including the
unfinished-declaration rejection. No unfinished proof or project axiom is
introduced. No new aperture positivity, F4 or RH claim.

## Next cursor

Resolve fresh cumulative diagnostics, then prove truncated-kernel convergence
and use the actual full-jump majorant for cutoff removal. Physical weak
attachment, L2 convergence and spectral source identification remain open.
