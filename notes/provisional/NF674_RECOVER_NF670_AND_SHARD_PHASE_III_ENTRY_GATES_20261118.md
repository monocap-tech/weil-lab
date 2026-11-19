# NF674 — recover NF670's original full-source Lean compiler blocker and shard Phase III row gates

## Verified compiler evidence

NF670 original 242-source physical run **44460719268**, original-source job **135359497990**, terminated FAILURE at `WeilDefect/Generated/NF670/OriginalPhysicalFullQuadratic.lean`. Exact compiler errors:

- line 88: `nf669OriginalSourceEquiv (Sum.inl i)=k` was not simplified to the definitionally equivalent `nf669SourceSum (Sum.inl i)=k` in `nf670AssembleOriginal_roundtrip`;
- line 93: same mismatch for `Sum.inr j`;
- line 133: the original physical block energy `change` expected `A+B` then `Bᵀ+C`, but `Fintype.sum_sum_type` expands the **inner** Sum first, producing `A+Bᵀ` then `B+C`.

The failed Lean build printed `sorryAx` for the unfinished NF670 roundtrip and two dependent quadratic identities; these were **never** certified. **No failure is being recast as a mathematical contradiction.**

NF665 original 15-source physical coercivity was previously FULL PASS in run **44455028120**; NF668 original 15-source positive definiteness in **44457538220**; NF669 source-index partition plus generic Schur algebra in **44459126587**, all standard axiom audits only.

NF671 generic interval-square equality and qualitative PSD job **135364375635** in run **44466173424** passed Lean with standard `[propext, Classical.choice, Quot.sound]`, while the genuine original 242-source attachment remained compiling during NF674 preparation.

## NF674 repaired source

`WeilDefect/Generated/NF670/OriginalPhysicalFullQuadratic.lean` contains TWO focused proof repairs:

1. Explicitly type `hk : nf669SourceSum (nf669OriginalSourceEquiv.symm k)=k` using `Equiv.apply_symm_apply`. After case-splitting on `nf669OriginalSourceEquiv.symm k`, rewrite by the case equality and `hk`. This avoids depending on simp normalization of `Equiv.ofBijective`.
2. Align the `change` statement with the **actual** expansion of nested Sum sums: `(A+Bᵀ)+(B+C)`. Then apply the authentic physical H symmetry theorem to turn `Bᵀ` into `B`, and `ring`.

This repair is **compiler pending**; do not promote it merely because it targets the exact logged errors. The NF674 full-source workflow rebuilds the pinned original NF655–665 proof bank, NF669 source dictionary, and the corrected NF670 FullQuadratic, original Riesz and full Schur, then NF671 original integral-square/Schur source results, and audits their true axiom dependencies.

## Phase III original 242-source numerical custody plan

The NF673 fast conditional Phase III theorem now needs genuine literal Lean truths:

- `hbank` — complete valid 7,835-key, 37,994-row NF624 original moment bank;
- `hcov` — complete original 242-source frequency/degree coverage;
- `htri` — original **29,403** lower H enclosure checks, exact 242×242 rational center symmetry, and all **968** mixed V enclosure checks;
- `hcache` — exact checked integer center product/cache;
- `hpay` — all 242 defect/residual/frozen-box payment gates.

NF629 had independently supplied rowwise lower-triangle soundness before NF673; NF673 supplies a single combined `EntryCheck` and conditional original signed-Weil margin theorem. None of these facts establishes the original Boolean truth.

`WeilDefect/Arithmetic/ActualZetaOriginalPhysicalShardedEntryCustody.lean` introduces one small decidable gate per original source index, combining its lower-H, exact center symmetry, and four mixed-V comparisons. It proves the *logical equivalence*:

`(∀ i : Fin242, originalRowCheck(i)=true) ↔ neutralNF673EntryCheck(M,p)=true`.

It also transports proven row receipts to the authentic original real analytical H/V interval error bounds through NF673's original source checker. This permits independent, bounded Lean kernel evaluation for each genuine source row without introducing any untrusted checker or reducing the required inequalities.

`scripts/emit_nf674_original_triangular_row_gates.py` is a deterministic proof-proposal generator: for explicit original bank/module and payment/module symbols, emits 242 (or user-selected subset) separate Lean theorem candidates `neutralNF674OriginalRowCheck ... i = true := by decide +kernel`; prints the source-specific `#print axioms`, and records SHA256 for every output. Its self-test checks serialization only. False rows must fail Lean; the emitter **never** claims they pass.

**The required actual original data banks and full cache have not been generated and kernel-accepted in NF674.** This is a certificate-execution architecture, not numerical closure.

## New pinned CI

`.github/workflows/nf674-original-reindex-and-row-gates.yml` provides:

1. `rowwise-physical-entry-soundness`: Lean builds the sharding equivalence and exact analytical soundness against NF673, then checks explicit standard-axiom whitelist for its three theorems.
2. `row-gate-emitter-test`: reproducible synthetic and tiny real-index emitter tests; does not assert generated proof truth.
3. `recovered-full-original-physical-reindex`: exact original pinned source regeneration and repaired NF670/671 physical-source theorem build and strict axiom whitelist.

## Next

1. Check compiler outcome of NF674 row/real source jobs; resolve **first failed declaration**, if any, before extending work.
2. Generate original NF628 bank from the eight NF621 source shards, prove all key/degree checks and bind `nf630Inputs.payment` on the unchanged historical original frame and moment-derived H/V entries.
3. Prove all 242 literal row receipts in separately bounded modules; then attach validated cache/payment gates to NF673's original strict corrected 2/5 signed-Weil carrier theorem.
4. Until `hbank,hcov,htri,hcache,hpay` are all **kernel proven on the same pinned original data**, full unconditional Phase III closure remains OPEN. The original strict carrier is not the global signed Weil positivity theorem and no RH claim follows.

NF674 draft stacked on NF673; no merge to main.
