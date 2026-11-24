# F41-039 — staged genuine original full NF702-payment physical H/V row66 Lean candidate

**SOURCE STAGING ONLY — NO ROW66 LEAN RUN OR CERTIFICATION.** Independently accepted F41 original NF690/NF702 complete-payment physical H/V Boolean predicates cover rows 0–63 = **64/242**. F41-035 genuine original row64 [run 45294777191](https://github.com/monocap-tech/weil-lab/actions/runs/45294777191) remains in compilation and requires F41-036 independent custody before row64 acceptance. Row65 F41-037 and independent F41-038 are separately source-staged only. All prior original H/V row certificates are narrow Boolean row checks, not an analytic full-matrix enclosure.

The row66 candidate targets the actual original NF702 payment:
```lean
theorem f41039Attach066ActualPayment :
  neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    nf702OriginalInputs.payment (66 : Fin 242) = true
```
Exact obligations: **67 lower-triangular original H comparisons**, **4 mixed-V comparisons**, **242 original H-center symmetry comparisons**, five local-to-global H-row/H-col/V/original-global-eH/eV projections onto the *complete original* NF702 payment, nine actual named Lean `#print axioms` outputs (3 local + 6 complete payment), permitting only `propext`, `Classical.choice`, `Quot.sound`.

The generator and source-scoped genuine Lean 4.34.0 workflow preserve original frozen mathematical commit `a431f903254000bb5ad8edbc276ccc8599da98f5`, NF707 historical compiled bank source `3d3fa66956bef3a63f90ed9b5325141afaf43cb5`, authentic NF690/NF691 moment bank, complete original NF631 242-row H/V physical source and original global eH/eV radii, and complete original NF702 payment with historical source-verified compiled input. The workflow must reject original source/radius mutations, genuinely compile local and complete-payment `.olean` with pinned Lean, verify nine ordinary-only Lean axiom lines, and preserve all source/manifest/compiler/axiom evidence in a ZIP.

**Required promotion sequence:** row64 F41-035 genuine compiler + separate F41-036 full original archive success → 65/242. Row65 F41-037 genuine compiler + separate F41-038 archive success → 66/242. Only afterward launch row66 F41-039 genuine compiler, and require a separate F41-040 independent archived source/ZIP/external SHA/seven-original-math-SHA/nine-axiom audit before advancing to **67/242**, 175 remaining. No row66 proof or independent audit has run yet.

F40 HD/A 968/968 is separately accepted. This staging does not establish the original full physical 242×242 analytic H/V enclosure, analytic `hbank`, complete `htri`, `hcache`, `hpay`, conditioning/inverse/residual, F42 signed Weil positivity or RH.
