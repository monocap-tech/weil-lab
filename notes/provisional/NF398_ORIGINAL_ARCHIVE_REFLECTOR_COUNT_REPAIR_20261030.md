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

## POST-REPLAY ACCEPTANCE — original native data now successfully custodied

The same source-pinned optimized NF398 job **subsequently completed successfully**, [GitHub Actions run #41020943169](https://github.com/monocap-tech/weil-lab/actions/runs/41020943169). Both `original-native` and `durable-result` jobs report SUCCESS. The exact source archive header has **FOUR** original Householder reflectors in 242-dimensional selected space; this is why NF397's assertion `len==242` was invalid. The original signed archive ZIP and matrix/mixed source SHA values are unchanged.

Two actual source-authenticated native files have been **committed on the unmerged NF398 branch**:
- `notes/data/provisional/NF398_original_j387_selected_signed_native.json` (original-source 4096-bit Arb report; Git blob SHA1 `8b1c24046f2170b21700115ab68425d3e1c926cc`, native SHA256 `a3d0e30970b898050fc6e222b3a0ddfc024d4e6a74c6cef6e708945dd9dc8dca`).
- `notes/data/provisional/NF398_original_j387_exact_candidate_decision.json` (independent exact-Fraction attestation; Git blob SHA1 `144a3b04ab7534d36eade50c25c57796727ab87c`, verdict `STOP`). 
- The typed `notes/data/provisional/NF398_native_execution_status.json` records `native_job_result=success`, source run `41020943169`, `original-native-source-verified` and the same report SHA256.

The archived 242-dimensional physical Gram/frame and **16 NF369 quotient overlaps**, original exact source/rank, `30371` archived WJJ/WJF signed source cells, the **actual four-reflector** isometry, mandatory original selected odd-pole restoration, independent direct-vs-reconstructed physical pole interval overlap, signed-plus-pole multiplier interval identity and selected (j387) positive physical norm² **all passed**.

An additional independent exact rational verification of the actual GitHub committed native endpoints (no floating-point interpretation for proof) established:

```
0 < Wodd(u4,j387) < 10^-21
-9.5e-9 < 2<FTe4,s><j387,s> < -9.2e-9
<m(D)u4,j387> < 0
0 < ||j387||² < 10^-15
<m(D)u4,j387> - ||j387||² < -9e-9
(original NF375 isolated moment threshold) < 1.31e-20
```

In particular, the original discrepancy lower is **strictly greater than (9\times10^{-9})** in absolute value while the full needed moment tolerance is below (1.31\times10^{-20}). The native output's original physical low-band error lower is even **strictly greater than (31/100)**, compared with the unchanged `2.8e-13` future physical norm target. These are valid **under the original inherited strong Fourier/operator interface used in NF375–NF392**, not an independent proof of that global domain identification.

**Accepted precise method stop: `NF387 original frozen j387 STOP`.** This selected two-coordinate dyadic vector provably cannot satisfy the original fourth-direction NF375 low-band sufficient acceptance criterion. The positive original selected signed `Wodd` scalar is tiny (~`9.604e-24`), and the source-verified restored pole contribution dominates (~`-9.3495e-9`). This discharges the previously open *evaluation of this specific frozen candidate*, not the original low-band upper for some other (j\in J_{242}), let alone the original odd signed negative-frequency operator, infinite complement, even sector, full Weil positivity, global bridge or RH.

**REVISED NEXT CURSOR:** Do not run another arbitrary exterior harmonic or further tune thresholds for rejected j387. Return to the **source-adapted selected-space approximation problem**: preserve original rank 242, fourth source and true pole, construct a different physically meaningful (j\in J_{242}) that may satisfy the complete source action, or demonstrate a true method-specific obstruction to any such selected (j). The *method stop* is accepted; **`W-ODD-NEG` remains OPEN**.

The earlier portions of this note describe its initial (pre-run) state and remain as historical process snapshots; this addendum supersedes the earlier `native pending` statements for NF398's completed run.

## Actual runtime and complexity correction

NF398's authenticated native log started the selected signed step at **2026-10-30 07:35:12 UTC**, completed original physical/16-overlap/frame check at **07:38:40 UTC**, computed the archived WJJ scalar by **07:38:47 UTC**, and logged original native `STOP` at **07:38:53 UTC**. The entire selected native stage completed in approximately **3 minutes 41 seconds**, compared with the NF395 older dense calculation which ran for roughly 55 minutes and was cancelled after the physical checkpoint. This is a measured execution improvement on the preserved source and not a claim about untested workloads.

The original archive holds **m=4** Householder reflections, not m=242. Therefore the earlier NF397 generic description “dense reconstruction O(n^3) versus two-vector O(n^2)” is **not the accurate workload-specific count**. For general ambient dimension n and m stored reflectors, the old right-applied dense-Q updates take O(m*n^2) arithmetic operations and the two vector transforms take O(m*n), with a separate unchanged O(n^2) signed-M construction/bilinear operation. On this actual original archive, m=4; the equivalence and speed improvement are nevertheless genuine. The previously erroneous m=n assertion is the direct reason NF397 failed and NF398 restored source compatibility.
