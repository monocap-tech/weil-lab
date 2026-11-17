# NF570 — compiler recovery: actual source odd derivatives and original NF550 weighted-square Gram now accepted

**2026-11-16 PT. Stacked on NF569 PR #601.** This step consumes newly completed CI. All NEW NF570 repairs and endpoint candidate remain pending, but several formerly blocked original source modules now have concrete successful compiler receipts.

## 1. Newly accepted original source and physical modules

NF565 rerun at NF566 source head, run 44004239824, job 133775535111 **SUCCESS**:
- Original scaled sine/cosine and monomial Leibniz jets: ActualZetaOriginalJ242OscillatorTrigJets.
- Both parity-specific monomial trigonometric odd initial derivative formulas: ActualZetaOriginalJ242MonomialTrigOddJets.
- All 241 literal original indexed oscillator analytic odd derivatives: ActualZetaOriginalJ242ActualOscillatorOddDerivatives.
- Exact original first sine-to-dual positive squared root, including every k=0 original column under its order condition: ActualZetaOriginalJ242FirstSineOddJetDual.

NF566 run 44004240240 job 133775535862 independently builds the first three modules successfully. Its next import, the signed finite-sum module, fails (see below). NF566 immutable source SHA audit job 133775535603 **SUCCESS**: all 58,564 original coefficient comparisons.

NF565 rerun job 133775535324 **BUILT** the exact original NF550 canonical weighted-square module and separation gate, before failure in NF551 odd parity. NF566 job 133775535886 independently repeats both successes: output 03:17:34 UTC Built ActualZetaOriginalCanonicalGramWeightedSquare; 03:17:41 UTC Built ActualZetaOriginalCanonicalGramSeparationGate. This is **LEAN PASS for both NF550 modules**, not a claim that their containing jobs passed. The former weighted-square and real/complex integral coercion blockage is resolved.

Consequently the exact original finite canonical physical Gram quadratic functional equals the original real weighted squared norm, and the conditional collar-separation implication to strict positivity and exact original moment right inverse are accepted. Unconditional strict positivity remains pending the actual source-independence proof.

## 2. The next actual analytic Hermite compiler stop

NF566 jobs 133775535862 and 133775535972 both fail ONLY at the `iteratedDeriv` identifiers of the generic conditional analytic transfer theorem in ActualZetaOriginalJ242HermiteSignedOscillatorSum.lean, lines 150, 154, 164. The source log explicitly says the identifier is unknown and Lean autoImplicit treats it as an untyped variable. No errors are reported in the preceding signed coefficient finite-sum/Hermite multiplicity statements. This is not a certified module until a complete build succeeds.

NF570 adds the exact Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas import. It retains the genuine 242-dimensional signed dual, all source coefficients, all k orders and the generic conditional analytic theorem. It additionally makes the parity sign proof and substitution in the subsequent actual 241-source bridge more explicit, as preventive elaboration hygiene rather than a repair inferred from a downstream log. No changes to source functions or arithmetic.

## 3. The new NF551 parity compiler stop

Both the NF565 and NF566 physical jobs fail at ActualZetaOriginalJ242OddParity.lean:132. The previous rewrite searched for neutralNF550OriginalSourceCombination d (-x), whereas the earlier source synthesis rewrite had already exposed its explicit finite sum. NF570 restores the exact definitional form via a typed `change`, then applies the authentic source oddness lemma and ring normalization.

This preserves original source parity and original fixed cutoff; it is a targeted compiler candidate, acceptance pending. NF551 analytic local-to-global is still unverified.

## 4. Direct canonical odd supported right inverse endpoint

NF570 adds a small direct endpoint to ActualZetaOriginalJ242CanonicalGramPositivity.lean, using NF569's already implemented strict canonical Gram candidate, accepted NF550 conditional physical machinery and NF551 parity:

```
neutralNF570Original242OddSupportedRightInverse :
  ∃ R : NeutralNF543RightInverse,
    (∀ d, neutralNF546OriginalSelectedMoments ((R d).toLp 2 volume) = d) ∧
    (∀ d x, x ∉ neutralNF543OriginalCollars → (R d) x = 0) ∧
    (∀ d x, (R d) (-x) = -(R d) x).
```

The witness is the unchanged NF548 canonical right inverse, not an abstract replacement lift. The new terminal theorem has no explicit source-separation/Gram premise; dependencies remain compiler-pending. It does NOT yet assert real-data conjugation equivariance, correction energy estimates or RH-facing positivity.

## 5. Next compiler frontier

NF567–NF569 CI still queued at last check. New two-job focused workflow tests (1) repair signed oscillator coefficient import, actual Hermite source, block coverage and terminal global independence and (2) already accepted physical weighted-square / separation, NF551 parity / analytic identity, and the exact odd supported 242 right inverse endpoint. No duplicate broad audit. Actual source-independent and physical proof candidates at later stages are not promoted to PASS before compiler receipts arrive.

NF571: consume the next actual logs for NF566 and NF551, and independent NF567–NF569. Repair the earliest concrete failure and prove actual full chain. Correction reality, NF528 source graph, NF527 cofinite 1/10 gamma/prime/pole coercivity, NF539 signed Weil, W_ODD_NEG and RH remain OPEN.
