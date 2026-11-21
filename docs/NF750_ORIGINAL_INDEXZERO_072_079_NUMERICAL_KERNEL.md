# Weil-Lab — NF750
## Actual NF748/NF749 compiler recovery; new ORIGINAL index-zero 72–79 numerical proof candidates

**Canonical Phase III iteration:** NF750. Separate from the parallel Phase IV `IV###` support-extension and cross-projection research. It does not assert global mixed-form positivity or RH.

### 1. Exact prior compiler recovery at submission

- **NF748 original HD/A index-zero 64–71:** [Actions run 44846764448](https://github.com/monocap-tech/weil-lab/actions/runs/44846764448), genuine job **136668270768**; live state **queued**, no resulting kernel/strict-axioms proof artifact available.
- **NF749 original HD/A index-zero 24–31:** [Actions run 44847296036](https://github.com/monocap-tech/weil-lab/actions/runs/44847296036), genuine job **136670051321**; live state **queued**, no resulting kernel/strict-axioms proof artifact available.
- Historical NF734 24–31 workflow failures (runs 44783797637, 44783948984, 44789881706) had no jobs or numerical artifacts; they remain non-certificates.
- Certified prior *original numerical* source-specific frontier: **596/968** true HD/A gate instances. This comprises the prior 532 (24 HD+A index-zero positions and all 242 index-one HD+A positions), plus four independent real original 16-gate index-zero numerical batches NF737, NF739, NF742 and NF743. None of the two queued new batches is counted.

### 2. New NF750 genuine ORIGINAL source-bound pilot

The next disjoint eight-coordinate shard is **72–79**:

```lean
nf703OriginalCache.HDGate nf702OriginalInputs 0 (i : Fin 242) = true
nf703OriginalCache.AGate  nf702OriginalInputs (i : Fin 242) 0 = true
```

For each literal `i = 72,…,79`, the original frozen `NF704Frontier.ColNNN.lean` emits four source-specific declarations (`DGate`, `DProjection`, `HD`, `A`); together with three shared declarations, the actual strict axiom audit has **35 exact targets**.

The proposal reuses the complete previously source-authenticated NF737 242-column numerical bank (source bank **227 MB**) rather than constructing substitute numerical data. It verifies the original NF702/NF703/NF681/NF704 manifest and exact original sources, the accepted NF728/NF729 immutable center-cache artifact/source identity, and the *live, nonoverlapping* NF748 historical 596-gate receipt. It preserves the original required compilation DAG:

```
NF681.Common.olean
  → NF703Cache.Frontier.olean
  → NF681.Col072..079.olean
  → NF704Frontier.Common.olean
  → NF704Frontier.Col072..079.olean
```

The actual compiler must build all eight original global NF704 columns, replay all 35 `#print axioms` declarations, permit only `propext`, `Classical.choice`, `Quot.sound`, forbid `sorryAx`, and publish the genuine source-bound Lean numerical kernel artifact.

**Proposed source, accepted cache, or queued job is not a numerical certificate.**

Files:
- `scripts/nf750_original_indexzero_072_079_cached_kernel.py`
- `scripts/nf750_original_indexzero_import_order_guard.py`
- `.github/workflows/nf750-original-indexzero-072-079-cached-kernel.yml`

### 3. Distinct and conditional proof count

With current accepted 596, each new genuine eight-index proof batch contributes **16 nonoverlapping HD/A instances**:

| Proven new numerical batches after strict Lean audit | Correct accepted count |
| --- | ---: |
| None | **596** |
| Any one of NF748, NF749, NF750 | **612** |
| Any two | **628** |
| All three | **644** |

If and only if all NF748 64–71, NF749 24–31 and NF750 72–79 finish with authentic numerical Lean/axiom/immutable-artifact proof, the index-zero original frontier becomes contiguous **0–79**. The remaining **80–241** index-zero positions (162 per HD/A family = 324 actual gate instances) still require their own numerical Lean proofs. Even then the complete 242×242 physical matrix, full payment/vector enclosure, Phase III terminal enclosure, global Weil positivity and RH are **OPEN**.

### 4. NF751 recovery instruction

Recover real Actions job statuses and steps for NF748, NF749 and NF750. For any completed new numerical shard, require a successful source-bound kernel job, complete strict 35-target axiom audit, standard-axiom record, and immutable numerical artifact ID/SHA. Classify queued or failed workflows as unaccepted; recover the precise failing step and compiler output when failure occurs. Update the permanent canonical [registry #761](https://github.com/monocap-tech/weil-lab/issues/761) only on authentic acceptance. Do not convert the NF744 logical `Fin 242` source cover to full original matrix numerical certification.

The independent Phase IV extension and cross-projection investigation proceeds under `IV###`; NF750 does not change its scope or assumptions.
