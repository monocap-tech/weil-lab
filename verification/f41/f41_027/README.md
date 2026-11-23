# F41-027 — Next original H/V full-payment physical row60 Lean proof candidate

**SOURCE STAGING ONLY, NOT A LEAN PASS OR ACCEPTANCE.** Accepted original F41 NF690/NF702 Boolean H/V row predicates remain **0–58 = 59/242** while the F41-025 row59 genuine Lean run and separate F41-026 custody gate are pending. Row59 may advance to 60/242 only after both gates independently pass. This candidate targets the subsequent **row60** and must itself pass new genuine Lean and independent custody before becoming accepted (**61/242**, 181 pending). F40 HD/A inventory remains separately 968/968.

**New physical row60:** 61 lower-triangular original H comparisons, four original mixed V comparisons, 242 H-center symmetry checks, five exact full original NF702 global payment projection equalities (H row/col, V, original global eH, eV), nine `#print axioms` original Lean declaration checks (three row-local and six full-payment). The exact target is:
```lean
theorem f41027Attach060ActualPayment :
  neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    nf702OriginalInputs.payment (60 : Fin 242) = true
```

**Original sources immutably pinned:** frozen mathematical commit `a431f903254000bb5ad8edbc276ccc8599da98f5`, historical NF707 compiler `3d3fa66956bef3a63f90ed9b5325141afaf43cb5`, exact original NF690/NF691 moment bank, immutable original NF631 physical H/V 242-row enclosure numerics and original eH/eV, complete original NF702 global payment including previously authenticated compiled input. Source SHA and numerical archive bindings and adversarial row/radius mutation rejection are required before any actual Lean build.

**No promotion without evidence:** only actual Lean 4.34.0 `.olean` success and 9/9 named ordinary-only `#print axioms` checks, followed by a *separate independent source/ZIP SHA/axiom verifier* against the remotely authenticated actual producer can accept row60. This staging is not proof of the entire 242×242 original physical H/V analytic enclosure, `hbank`, all-row `htri`, `hcache`, `hpay`, inverse/residual/conditioning, F42 global signed Weil positivity or RH.
