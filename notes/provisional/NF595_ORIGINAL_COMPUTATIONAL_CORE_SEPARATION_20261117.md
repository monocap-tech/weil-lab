# NF595 — separate executable computation from proof dependencies

Stacked on NF594 #625. New code and proof repairs compiler-pending.

## Verified receipts

NF594-head NF593 run 44148266146 jobs 134269233285 and 134269233841 accepted the entire literal original normalized complex source (including real restriction and derivative) and the sound Machin pi input / exact periodic phase. NF594 run 44148266179 job 134269233421 accepted the complete exact integer and analytic degree cutoff arithmetic. These are substantive new Lean successes. NF590 run 44148266495 job 134269235699 independently accepted the ungrouped 374-primitive Arb replay again. Its Lean job 134269235967 accepted generic recurrence, frozen regularity and infinite tail, but the source all-order recurrence failed on three residual real-part equalities. NF594 source-disc assembly failed on coarse arithmetic tactic sequencing and even-zero simplification. NF595 commits repairs to those sites. The source-specific recurrence and full disc assembly remain unaccepted.

The cache and kernel experiments were skipped because NF593 cached proof modules import the unfinished source analytic recurrence and disc proof. Thus there is still no Lean executable replay, no 800-endpoint comparison and no kernel trial result. This was a dependency-order problem, not evidence that the computation exceeded a resource budget.

## New architecture

Moved all 65 existing interval structures and definitions from ten proof modules into ActualZetaOriginalFixedpointComputationalCore.lean. Re-fetched committed core and compared every moved declaration verbatim against NF594: all 65 identical. The proof modules now import that core and retain their original theorem statements. The core imports Mathlib, original frozen data and node signature, already accepted finite normalized budgets and remainder parameters; it does not import the unfinished source-specific analytic recurrence/disc, phase soundness, cache equality or block soundness proofs. The existing NF593 executable preflight now imports this same core. No replacement evaluator, data, rounding convention, changed uncertainty box or approximation was introduced by this refactor.

New focused workflow attempts core compilation, then standalone full 400-order executable replay with comparison of all 800 exact scaled endpoints against NF591, and a separate first-order `decide +kernel` trial (even if executable diagnostic fails). A second job independently recovers analytic recurrence/disc, phase soundness, cached equality and reduced block soundness. The actual evaluator may have computability or performance issues; those are now testable without the remaining analytic proof failures. No local Lean environment, no new numerical computation in this pass. No claim of checker truth or unchanged compiler behavior until verification.

Original solve-box custody, full disc and recurrence proofs, checker soundness and kernel truth, and terminal graph correction remain open. Full Weil coercivity, W_ODD_NEG and RH OPEN. No main merge.
