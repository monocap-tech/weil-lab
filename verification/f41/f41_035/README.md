# F41-035 — staged original full NF702-payment physical H/V row64 Lean candidate

**SOURCE STAGING ONLY; not a row64 Lean PASS or acceptance.** Original NF690/NF702 full-payment physical H/V Boolean row predicates **0–62 = 63/242** have been accepted following F41-031 original row62 genuine Lean [run 45283118623](https://github.com/monocap-tech/weil-lab/actions/runs/45283118623) and independent F41-032 original row62 archive custody [run 45287533245](https://github.com/monocap-tech/weil-lab/actions/runs/45287533245), merged PRs #976/#978. F41-033 original row63 [draft PR #981](https://github.com/monocap-tech/weil-lab/pull/981) is separately in genuine compiler CI, and must pass independent F41-034 archive audit before row63 is accepted.

The next candidate targets the *true original full global NF702 physical payment*:
```lean
theorem f41035Attach064ActualPayment :
  neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    nf702OriginalInputs.payment (64 : Fin 242) = true
```
It checks exactly **65 original lower-H comparisons**, **4 mixed V**, **242 H-center symmetry** cases, five exact H-row, H-column, V and global original eH/eV local-to-complete-NF702-payment equalities, and nine actual named standard-only Lean `#print axioms` reports (three local, six original global payment). It is not a numerical proxy.

Source pins remain frozen original mathematical research commit `a431f903254000bb5ad8edbc276ccc8599da98f5`, historical NF707 compiler `3d3fa66956bef3a63f90ed9b5325141afaf43cb5`, genuine NF690/NF691 bank, true NF631 original physical 242-row H/V source with original global eH/eV radii, complete original NF702 payment source and compiled input. Source-scoped CI requires two adversarial source/mutation controls, true Lean 4.34.0 row-local and entire original-payment attached `.olean` builds, nine named ordinary-only axiom outputs and preservation of full source/compiler receipts.

**Conditional promotion only:** after row63 has passed both independent hosted gates, submit this row64 genuine compiler as a PR; subsequently the separate F41-036 original row64 ZIP/SHA/7-original-source/9-axiom custody must pass, and only then could the narrow original H/V Boolean row frontier reach **65/242**, 177 rows pending. F40 finite original HD/A remains separately 968/968.

The entire original physical 242×242 analytic H/V matrix enclosure, analytic `hbank`, all-row `htri`, integer center `hcache`, complete `hpay`, inverse/residual/conditioning, F42 signed Weil positivity and RH remain unproved.
