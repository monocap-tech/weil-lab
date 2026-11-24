# F41-037 — staged original full NF702-payment physical H/V row65 Lean candidate

**SOURCE STAGING ONLY; no compiler result or row65 certificate.** Independently accepted original NF690/NF702 full-payment physical H/V Boolean predicates cover rows 0–63 = **64/242**. Genuine [F41-033 row63 Lean run 45291263611](https://github.com/monocap-tech/weil-lab/actions/runs/45291263611) and independent [F41-034 custody run 45294456777](https://github.com/monocap-tech/weil-lab/actions/runs/45294456777) passed and their PRs #981/#982 merged. The subsequent original row64 genuine [F41-035 PR #983](https://github.com/monocap-tech/weil-lab/pull/983) is still undergoing its own source-bound Lean CI; its separate F41-036 independent archive custody must pass before row64 acceptance.

**Exact original row65 full-payment theorem target:**
```lean
theorem f41037Attach065ActualPayment :
  neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    nf702OriginalInputs.payment (65 : Fin 242) = true
```
Requires **66 original lower-H comparisons**, **4 mixed V**, **242 H-center symmetry checks**, five exact H-row/H-column/V/original global eH/eV equalities against the *complete original NF702 payment*, and nine actual named `#print axioms` standard-only reports (three row-local and six full-payment).

The staged generator and source-scoped Lean CI workflow pin frozen original mathematical source commit `a431f903254000bb5ad8edbc276ccc8599da98f5`, historically successful NF707 compiler `3d3fa66956bef3a63f90ed9b5325141afaf43cb5`, genuine NF690/NF691 source-bound moment bank, actual full NF631 242-row original physical H/V and globally original eH/eV radii, entire NF702 original payment and authenticated compiled input. The workflow demands adversarial source/radius mutation rejection, actual Lean 4.34.0 `.olean` builds of both local and complete original-payment attached modules, nine exact named permitted-only Lean axioms, and source/compiler ZIP provenance.

**No promotion from staging.** Submit a row65 actual Lean PR only after row64 passes separate genuine Lean and F41-036 independent archive gates. The subsequent separate F41-038 row65 archive audit must check authenticated producer source/ZIP SHA/nine named actual Lean axioms, all seven frozen mathematical source SHA values, generated source hashes, four negative controls, and F41/F42/RH false flags. Both gates would conditionally advance original physical H/V *Boolean row* frontier to **66/242**, 176 pending. F40 original finite HD/A separately remains 968/968.

This does not certify the entire original 242×242 physical H/V **analytic** enclosure, `hbank`, complete `htri`, `hcache`, `hpay`, conditioning/inverse/residual, F42 signed Weil positivity or RH.
