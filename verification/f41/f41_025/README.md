# F41-025 — Genuine original physical H/V row59 compiler candidate

**Status: STAGED SOURCE ONLY / NO PR, NO ROW59 LEAN COMPILATION AND NO PROMOTION.** F40 HD/A remains 968/968. Accepted original F41 H/V full-payment Boolean rows are 0–57, **58/242**; F41-023 genuine row58 kernel and F41-024 independent archive must pass first. This gate targets a new row59 predicate, with **60 exact lower-H**, **4 mixed-V**, and **242 H-center symmetry** checks. It does **not** claim the original physical matrix, any complete moment-bank analytic soundness, inverse/residual/conditioning, F42 signed Weil positivity, or RH.

The workflow checks out the exact successful NF707 historical compilation source `3d3fa66956bef3a63f90ed9b5325141afaf43cb5` and independently confirms seven physical source Lean files are byte-identical to the immutable mathematical source `a431f903254000bb5ad8edbc276ccc8599da98f5`. All original NF631 source entries and NF702 complete payment artifacts are downloaded by pinned ZIP SHA256. Genuine original NF690/NF691 lookup source, bank objects and NF707 compiled input artifacts are restored with hash/environment binding.

The candidate generator emits **one local original physical payment projection** for row59 from the archived NF631 242-row numerical data, using the global NF631 eH/eV; the local Boolean truth is computed by Lean on the actual original NF690/NF691 moment bank. It then proves **five exact projection equalities** from this local payment to the full original `nf702OriginalInputs.payment` (H row, H column, four V entries, eH, eV) before invoking the original literal row-transport theorem to establish:

```lean
theorem f41025Attach059ActualPayment :
    neutralNF674OriginalRowCheck
      (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
      nf702OriginalInputs.payment (59 : Fin 242) = true
```

The script generates three local declarations and six full-payment declarations. Its `audit` mode rejects missing/extra names or nonstandard axioms. The workflow emits a compact artifact with the exact source manifest and compiler logs; no `.olean` object needs to be shared in the final receipt. No such audit is equivalent to the still-unproved analytic `hbank`, complete `hcache` or `hpay` obligations.

**Acceptance rule:** (1) genuine row-local and full-payment `.olean` builds, (2) 9/9 exact named ordinary-only `#print axioms` reports, (3) source and parent archive SHA bindings, (4) independent ZIP rehash/replay/refusal tests, then and only then row59 may be promoted, making the narrow row frontier **60/242**, with 182 remaining. If the compiler stops before elaboration, do not treat it as a numerical contradiction; preserve the failed preflight stage.