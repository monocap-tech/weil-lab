# NF672 — strict original 242-source physical Gram and authentic 227-Schur response

## Verification baseline (do not conflate with new declarations)

- NF667 corrected run **44455028120** fully Lean SUCCESS under standard axioms: the original 15-source physical H has exact `10^-60` coercivity.
- NF668 run **44457538220** fully Lean SUCCESS: the same original selected H is strictly positive definite and injective.
- NF669 run **44459126587** fully Lean SUCCESS: original 242-source indexing is exactly 15+227, the source-specific A/B/C dictionary is real and the finite Schur algebra works.
- The original 242 real-generator **global linear independence** theorem `neutralNF569OriginalRealCombination_globalIndependence` and original fixed-collar separation `neutralNF569OriginalCollarSeparatesJ242` were accepted during NF569/NF570 recovery and were used in the earlier canonical Gram chain.
- At NF672 authoring, NF670 run **44460719268** and NF671 run **44466173424** were still queued. **Do not promote any NF670/NF671/NF672 dependent theorem before its full compiler build and source-specific axiom whitelist succeed.**

## New NF672 mathematical step

The NF671 full original *unweighted physical* Gram identity proposes (not yet certified on the present head)

```
Q_H(z) = ∫_{-11/10}^{11/10} (Σ_{i=0}^{241} z_i j_i(t))² dt.
```

The previously accepted analytic source independence provides a precise missing strictness witness for every nonzero `z : Fin242→ℝ`. The existing NF569 fixed positive collar

```
(1099/1000 - 1/2000, 1099/1000 + 1/2000)
```

is strictly inside the original physical integral window. Its source-separation theorem gives a real `t` in this collar where the *unchanged original generator sum* does not vanish. By continuity, the interval integral of its square is strictly positive.

Two new files capture this:

1. `WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramStrictWitness.lean` — source-independent finite continuous Gram strict positivity from a single in-window witness; no matrix inversion and no assumed eigenvalue.
2. `WeilDefect/Generated/NF672/OriginalPhysicalFullGramStrict.lean` — exact real/complex original sum casting, source-specific nonzero collar witness, and target
   `∀ z : Fin242→ℝ, z≠0 → 0 < Q_H(z)`.

The same source-bound module uses NF670's exact source-partition assembly and NF671's already proposed physical Schur integral-square identity to establish the *qualitative* 227-source Schur strictness target

```
∀ y : Fin227→ℝ, y≠0 → 0 < Q_C(y) - Q_A(U(y)).
```

The key nondegeneracy step: `Assemble(-U(y),y)` is a nonzero original 242-vector when its complement coordinate `y` is nonzero; this is a direct consequence of the original NF669 index partition, not a numerical independence hypothesis.

## Precise limits

- The new assertions are **Lean candidates**, not kernel-accepted results. The full source-specific dependency chain has not yet passed, and the new code has not been locally compiled.
- Strict positive definiteness in finite dimension would imply some positive minimum eigenvalue; this work does **not** provide an *explicit rational lower bound*, a condition-number estimate, or the interval enclosures required for the original selected physical solve.
- Original 242-coefficient selected-box containment has **external exact-arithmetic evidence**, but the complete source-to-Lean numerical receipt/payment attachment remains OPEN.
- Physical Gram energy `∫(Σz_i j_i)²` is a nonnegative integral-square object. The **signed** Weil form is a separate mathematical object. Neither full physical H positivity nor physical Schur positivity proves global signed Weil positivity or RH.
- The NF670/671/672 complement line should not silently expand the Phase III exit criterion. Phase III still requires formal custody of the original 242-coefficient solve and unconditional original signed-carrier theorem.

## CI and release gate

`.github/workflows/nf672-original-full-gram-strict.yml` has:

- a bounded generic strict-witness Lean build/audit;
- a complete pinned-source replay from original NF621/NF631/NF632/NF648 receipts through NF655–NF665, NF669–NF671 and the new NF672 source theorem;
- a focused strict standard-axiom whitelist over the new declarations and essential imported original-source endpoints.

Promote `nf672OriginalFullPhysicalGram_strict` and `nf672ActualPhysicalSchur_strict` **only after both jobs fully succeed**, the declaration types match the genuine source integrals, and each axiom audit contains no `sorryAx` or nonstandard axioms.

## Subsequent priority

After compiler feedback, if any NF670/671/672 proof fails, repair the earliest failed dependency first. Separately, prioritize the **complete 242-coefficient analytic-entry-to-frozen-box numerical custody** so the signed-Weil Phase III exit theorem is not blocked by indefinite physical-Gram extensions.
