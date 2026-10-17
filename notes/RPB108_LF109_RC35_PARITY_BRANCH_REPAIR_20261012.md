# LF109 — RC35 parity branch repair

LF108 run 38294059166, job 114965741996, passed cumulative certificate targets but failed the root build. The only reported error was `No goals to be solved` at the imported RC35 parity proof. Its combined `norm_num at hij ⊢` location list tried to normalize a goal after the impossible parity hypothesis had already closed that branch.

This checkpoint sequences hypothesis and goal normalization with `<;>`, so the second tactic acts only on surviving goals. Exact rational data and theorem statements are unchanged. No errors were reported for the trial continuity proof, but the module/root is not claimed compiled until this repair passes.

Local structural and unfinished-declaration checks pass; no local Lean executable is available. LF106 (945b189cb489a1c6afa20440f9f7a4425abf651a; run 38269079086) remains the latest full-root validated checkpoint. LF109 requires cumulative CI. Next: derivative regularity and physical carrier identities of the assembled RC35 trials. No aperture positivity, F4 closure or RH is claimed.
