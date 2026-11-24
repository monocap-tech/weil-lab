# F41-033 — staged original full NF702-payment physical H/V row63 Lean kernel

**SOURCE STAGED ONLY; NO PR/COMPILER/CERTIFICATION FOR ROW63 YET.** The accepted original NF690/NF702 full-payment H/V Boolean physical predicates currently cover rows 0–61 = **62/242**, with 180 pending. F41-031 original row62 has passed genuine original Lean [run 45283118623](https://github.com/monocap-tech/weil-lab/actions/runs/45283118623), but separately hosted F41-032 archive custody [run 45287533245](https://github.com/monocap-tech/weil-lab/actions/runs/45287533245) is still pending; row62 cannot be accepted without its independent archive pass and receipt.

The new row63 original full-payment theorem is:
```lean
theorem f41033Attach063ActualPayment :
  neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    nf702OriginalInputs.payment (63 : Fin 242) = true
```
It demands exactly **64 original lower-H comparisons, 4 mixed-V, 242 H-center symmetry checks**, five local-to-full original NF702 global payment equalities (H row/H column/V/global eH/eV), and nine exact named standard-only Lean `#print axioms` reports (3 local, 6 attached). No proxied or synthetic numerical source.

The staged source generator and source-scoped genuine Lean workflow bind frozen original mathematics commit `a431f903254000bb5ad8edbc276ccc8599da98f5`, historical NF707 compiler `3d3fa66956bef3a63f90ed9b5325141afaf43cb5`, actual NF690/NF691 original bank, true original NF631 242-row physical H/V numerical source and original global eH/eV radii, complete original NF702 payment and compiled source. They require true pinned Lean 4.34.0 local/full-payment `.olean` builds, two adversarial row/numeric rejection tests, nine exact actual ordinary-axiom stdout lines, compiler/source proof archive with independently bound source hashes.

**Acceptance:** submit genuine row63 PR only after row62 dual-gate acceptance; separately hosted independent F41-034 artifact/source/ZIP/SHA/9-axiom audit is mandatory. Both gates would conditionally advance F41 original H/V Boolean-row frontier to **64/242** (178 pending). F40 finite original HD/A remains separately **968/968**. This does not establish entire original physical 242×242 analytic H/V enclosure, `hbank`, `htri`, `hcache`, `hpay`, conditioning/inverse/residual, F42 original signed Weil positivity, or RH.
