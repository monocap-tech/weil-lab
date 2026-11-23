# F41-031 — staged genuine original full-payment physical H/V row62 Lean candidate

**SOURCE-ONLY / NO COMPILER RUN OR ACCEPTANCE.** The independently certified F41 original NF690/NF702 physical H/V full-payment Boolean frontier currently ends at row60: **61/242 accepted**. Genuine row61 remains in [F41-029 Actions run 45276538414](https://github.com/monocap-tech/weil-lab/actions/runs/45276538414) and requires a separate F41-030 independent archive audit before it can be accepted. No row62 claim follows merely from this source proposal.

The intended original row62 proof target is
```lean
theorem f41031Attach062ActualPayment :
  neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    nf702OriginalInputs.payment (62 : Fin 242) = true
```
with **63 lower-H comparisons**, **4 mixed V**, **242 H-center symmetry checks**, five exact original global H-row, H-column, V, eH, eV full-payment equalities and **nine** distinct ordinary-only actual Lean `#print axioms` declarations (three row-local, six complete-payment).

Immutable research commit `a431f903254000bb5ad8edbc276ccc8599da98f5`, original NF690/NF691 bank, full NF631 original 242-row physical H/V source and its globally original eH/eV radii, complete original `nf702OriginalInputs.payment`, and historical NF707 compiler commit `3d3fa66956bef3a63f90ed9b5325141afaf43cb5` must remain frozen. Real Lean 4.34.0 `.olean` builds and independent F41-032 ZIP/SHA/source/nine-axiom audit are required before row62 could increase the frontier to **63/242**, 179 rows pending.

**Staging status:** `verification/f41/f41_031/f41_031_original_row062.py` generator exists. The original row62 CI workflow is not yet committed; a prior attempt to create that file was blocked. No PR or Lean job has been started. The independent F41-032 source-only audit is staged separately. This is not a whole physical H/V matrix analytic enclosure, `hbank`, complete `htri`, `hcache`, `hpay`, inverse/residual/conditioning, F42 global signed Weil positivity, or RH.
