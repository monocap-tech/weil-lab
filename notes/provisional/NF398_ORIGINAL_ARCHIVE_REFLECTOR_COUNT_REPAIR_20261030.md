# NF398 — Authenticate the real original Householder archive length; rerun unchanged signed scalar

**2026-10-30 PT.** Active canonical obligation `W-ODD-NEG` remains **OPEN**. Draft continuation stacked upon NF397 PR #382; no merge or replacement of historical original source evidence. This is a **precise verified execution repair**, not a new signed kernel calculation, stronger Fourier bound, selected candidate rejection, or theorem proof.

## Previous → current → next

**Previous NF397:** replaced dense `242×242` original signed-frame orthogonal matrix reconstruction with direct application of archived Householder reflections to the two required vectors `alpha` and `beta`, preserving their complete original signed bilinear `(Q^T alpha)^T M(Q^T beta)`, original 30,371 archived signed cells and error payment. Independent exact Fraction small-dimension full-length reflector regression passed. The original branch-native workflow [run #41016847062](https://github.com/monocap-tech/weil-lab/actions/runs/41016847062) **DID EXECUTE AND FAIL**, while its independent execution-status job succeeded and committed actual `NF397_native_execution_status.json` declaring `native_job_result=failure`, `last_saved_phase=two-vector-native-signed-scalar`, and `j387=UNDECIDED`. No native signed moment exists.

**Exact recovered failure:** The native job #123935004523 log shows original source preflight PASS, original exact Fraction Householder regression PASS for n=2..5, original Arb installed, historical signed selected ZIP SHA PASS, and original 242 physical Gram, all 16 quotient overlaps and frame SHA PASS at **2026-10-30 06:59:09 UTC**. Then `scripts/verify_nf390_original_j387_selected_moment.py` failed at line 157:

```python
assert len(mat['householder_vectors']) == 242
```

The **actual original signed archive contains fewer Householder reflections than its ambient 242-dimensional selected space**. The old NF380 implementation never imposed equality: it initialized `Q=I_242` and iterated only over `matrix['householder_vectors']`, checking each archived reflector's `start==j` and suffix length `242-j`. Hence the NF397 `==242` assertion was newly introduced and wrong. This is an **archive representation-contract defect**, not a failure of the exact `Q^T` two-vector identity or an original Weil sign observation.

**Current NF398:** Restore historical accepted archive contract `0<len(householder_vectors)<=242`; check each real archived `r['start']==k` and `len(r['vector'])==242-k`. Let `m` be the **actual** archived reflector count, not inferred from rank; `Q=H_0 H_1 ... H_(m-1)` exactly. In that case `Q^T alpha` and `Q^T beta` are still obtained by applying the stored `H_k` to each current vector in ascending k; any unstored trailing transformation is identity. **No artificial 242nd reflector is added.**

- `scripts/verify_nf390_original_j387_selected_moment.py` was updated to accept the exact old source contract, report the actual count and test the two-vector isometry. Original full SHA pins, 16 physical overlaps and signed matrix/mixed matrices are unchanged. The signed scalar remains `(Q^T alpha)^T M (Q^T beta) + f^T L^T j387`, with full original archive native-error payment and mandatory independently checked pole correction.
- `scripts/local_replay/nf397_householder_two_vector_exact_regression.py` now tests **each partial reflector count 1..n**, as well as full count, at small noncommuting rational ranks 2..5. It compares the direct two-vector transform to the original complete dense Q reference, preserves both vector squared norms/mutual inner product and the transformed signed bilinear.
- `scripts/local_replay/nf398_original_archive_reflector_header.py` performs a **fast original-data SHA-pinned read** of the historical source ZIP SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`, original WJJ matrix JSON SHA256 `33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa`, and records the exact archived reflector count, start and suffix shapes as a separate non-theorem artifact. The count is **NOT invented in this note**; its actual numerical value must be read from authenticated replay.
- `.github/workflows/nf398-original-archive-count-signed.yml` runs the fast archive-header test before native Arb replay, retains the independent original NF394 source/moment interval attestation, and has an always-run separate job that commits typed failure/success status to the NF398 branch. Only genuine source-verified native success commits `NF398_original_j387_selected_signed_native.json` and `NF398_original_j387_exact_candidate_decision.json` with `STOP` or `INCONCLUSIVE`.

## Mathematical acceptance remains untouched

Original source, (J_{242}) selected basis, matched fourth source (u_4), original pole (s=\sinh(x/2)), exact full signed WJJ/WJF archive, frame transformation and NF375 cutoff (2^{24}) are identical to NF397 and NF390. NF396 independently certified (-9.5\times10^{-9}<P_{387}=2\langle FTe_4,s\rangle\langle j_{387},s\rangle<-9.2\times10^{-9}), but the remaining original signed `Wodd(u4,j387)` is not yet accepted.

**Next:** inspect source-header count and actual native CI/branch telemetry. If genuine original signed selected native is certified, recompute unchanged NF391/NF392 strict candidate test and classify **only frozen** (j_{387}) `STOP` or `INCONCLUSIVE`. A failed or incomplete execution remains `UNDECIDED` and must be debugged from its real reported stage. Original full lowband upper, infinite exterior inverse, operator-domain audit, `W-ODD-NEG`, even/whole Weil, global bridge, RH all **OPEN**.

**No original archive modification, no merge, no theorem promotion.**
