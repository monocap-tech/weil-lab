# RPB108 exact compact-correlation pole attachment — 2026-10-04

Definitions: [correlation pole terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_CORRELATION_POLES.md).
Parent: `5cae49493af43cf202649bbd0175c994d241b825`.

## Certified result

The new module `WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean` proves the exact imaginary-axis moment dictionary for arbitrary physical L² inputs:

`E_a(i s,f) = M_a(-s,f)`.

The existing all-complex correlation transform identity then gives

`H(K_a(f,g),i s) = conj(M_a(s,f)) M_a(-s,g)`.

At the two explicit-formula poles, the exact sum is

`H(K_a(f,g),i/2) + H(K_a(f,g),-i/2) = conj(M_a(-1/2,f)) M_a(1/2,g) + conj(M_a(1/2,f)) M_a(-1/2,g)`.

The reversal of the exponential sign follows from i²=-1 in the positive-exponent raw convention. The two terms are opposite-slot cross moments, not positive squares of separate moments.

On the existing complete logarithmic Hilbert carrier, this sum is exactly `inner ℂ f (neutralLogPoleOperator a g)`. Its diagonal is the existing real cross-pole expression. Substituting the exact canonical images of G_a(v), G_a(w), and using their already proved physical reconstruction identity attaches the same compact Green correlation to this pole operator without a representation hypothesis.

Six public theorems:

- `neutralWindowEvaluation_imaginary`
- `neutralWindowCorrelation_imaginary`
- `neutralWindowCorrelation_poleCrossTerms`
- `neutralLogHilbertCorrelation_poleOperator`
- `neutralLogHilbertCorrelation_poleDiagonal`
- `neutralActualZetaGreenCorrelation_poleOperator`

## Validation

Exact candidate `8c2caf41f171ea8b7d6902a362d84e8a6fb33637` passed [run 37173417283](https://github.com/monocap-tech/weil-lab/actions/runs/37173417283), job `111350934366`: isolated module 9,029 jobs; full `lake build WeilDefect` 9,062 jobs. All six public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The promoted source and root import match the exact validated contents. Workflow and pinned manifest remain validation-only.

## Boundary and cursor

This step uses certified project modules and Mathlib only. It does not import the external EF_lit_zeta statement stub, assume an explicit formula, or establish its C² test-function premise. Prime/digamma transport remains open. The constructed canonical Green image remains distinct from the retained WD-T38 mode until the coefficient/source dictionary and same-vector identity are proved.

Next cursor: certify C² regularity of the compact mixed correlation K_a(G_a(v),G_a(w)), or supply a smooth approximation with justified passage in both the zero-side and arithmetic forms. The raw-transform product and actual-divisor zero-sum dictionaries are now proved; do not reintroduce them as hypotheses. Recover and audit the external EF_lit_zeta proof-bearing dependency closure under Lean/Mathlib 4.34.0, then attach the exact prime/digamma symbol terms on this same carrier. Recover the retained WD-T38 coefficient/source dictionary and prove the same-vector source/null identity before transferring these constructed-carrier results to that witness. No conditional representation wrapper discharges that identity. The imaginary-axis moment dictionary and both pole samples are now certified against the existing cross-pole operator on the exact constructed canonical Green image; do not replace them by separate positive moment squares.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed G_a(v) are unproved. The typed WD-T38 record still permits independently named density/Q and abstract P/C operators; the zero-density reindex audit blocks inferring a physical source identity from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
