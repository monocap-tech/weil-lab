# NF397 — Replace full original Householder matrix by two selected vector transforms

**Date:** 2026-10-29 PT. **Canonical active obligation:** `W-ODD-NEG` **OPEN**. This is a directly motivated **algorithmic equivalence** pass on the SAME original (J_{242}), fourth direction (u_4), fixed original (j_{387}), full signed seven-prime/arch/pole archive and fixed cutoff (2^{24}). It does not assert an original signed numerical result until an authenticated native report is verified. Stacked on NF396 draft PR #381; no merge, historical overwrite, or new exterior-witness family.

## Previous / current / next

**Previous NF396:** Source-authentic rational Machin/Taylor evaluation certified (-9.5\cdot10^{-9}<P_{387}=2\langle FTe_4,s\rangle\langle j_{387},s\rangle<-9.2\cdot10^{-9}). The full selected multiplier moment (W_{\mathrm{odd}}(u_4,j_{387})+P_{387}) remains unmeasured, and `j387` is **UNDECIDED**.

**Recovered native-execution evidence:** The NF395 telemetry, now actually recovered on PR #380, identifies [original Actions run #40998863258](https://github.com/monocap-tech/weil-lab/actions/runs/40998863258), job `original-native` #123878301210 as **cancelled** at step 7. The original exact source, Arb install, original archived signed ZIP download and SHA verification all passed. The log's source-native 242 physical Gram and original 16 quotient-overlap/frame SHA checkpoint passed at `2026-10-30T03:46:54Z` (the run began its selected native step at `03:42:47Z`). The job was cancelled at `04:37:41Z`, after ~51 minutes inside the selected WJJ/WJF calculation. **No signed scalar, pole-corrected result or candidate method verdict was produced.** This is a resource/execution cancellation, not a negative Weil vector or a mathematical failure.

**Current NF397:** Remove the expensive dense matrix construction performed immediately after that checkpoint; replay the original archive's exact same signed scalar using only two vector images. **Next NF398** (if needed): inspect the authenticated original native report or its typed stage failure, then classify only the fixed (j_{387}).

## Exact Householder identity, not a new approximation

The signed archive contains 242 original Householder vectors (v_k), (k=0,\dots,241). The inherited implementation formed

[
H_k=I-\frac{2v_kv_k^\top}{v_k^\top v_k},\qquad Q=H_0H_1\cdots H_{241}.
]

It spent (O(242^3)) arbitrary-precision scalar work creating each updated dense (Q) (and then calculating (Q^\top Q)), even though the only use was

[
W_{JJ}(u_4,j_{387})=
(Q^\top\alpha)^\top\,M\,(Q^\top\beta),
]

where `M` is the unchanged source-pinned complete original (242\times242) transformed signed matrix, `alpha` is the unchanged selected matched source in the original physical dyadic frame, and `beta` is the unchanged selected candidate in that same frame.

Every (H_k) is symmetric. Hence

[
Q^\top z=H_{241}\cdots H_1H_0 z.
]

**Algorithm:** initialize `y=z`, and for `k=0..241` compute `d=v_k^T v_k>0`, `t=2(v_k^T y)/d`, and update `y := y-t v_k`. Perform this for **only** `z=alpha` and `z=beta`. All `v_k` use the original archived dyadic endpoint terms, and every update remains rigorous outward-rounded 4096-bit Arb. Complexity is now (O(242^2)) for the reflection stage, without allocating dense (Q).

The **exact mathematical signed quadratic is identical**, not a shadow or dropped coupling. The original native matrix `M`, original (D), 30,371 archived WJJ/JF signed source cells, global archive norm-error payment `eps` in `mat2_ball`, true pole restoration and selected-source reconstruction are unchanged. The code checks both transformed vectors' Euclidean squared norms and their mutual dot product against the originals with a conservative relative Arb tolerance. Exact independent **Fraction** regression builds small noncommuting Householder matrices (Q) and compares full (Q^\top\alpha,Q^\top\beta) to the new direct transforms for dimensions 2,3,4,5, including the signed bilinear pairing. This tests **transformation order**, a potential silent source error.

## Native replay / custodial acceptance

`scripts/verify_nf390_original_j387_selected_moment.py` now uses `apply_archived_qtranspose_to_one_vector` instead of dense (Q) and emits explicit method/isometry metadata. It still must independently verify original SHA-pinned physical frame, 16 original physical Gram overlaps, 242 original Householder vectors, original J-J and J-F matrix hashes, correct signed error accounting, and the independent direct-versus-reconstructed pole identity. It computes the **entire selected signed scalar** from (M,L), then (W_{\mathrm{odd}}(u_4,j_{387})+2\langle FTe_4,s\rangle\langle j_{387},s\rangle), not a pole-only estimate.

`scripts/local_replay/nf397_householder_two_vector_exact_regression.py` validates exact linear algebra without Arb or the historical archive. A narrowly scoped, push-triggered `.github/workflows/nf397-original-two-vector-signed.yml` authenticates the *same* original archive artifact #12776684037 ZIP SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`, performs exact regression, replays native at `python-flint==0.8.0`, then feeds its actual output to the **preexisting** independent NF394 source/interval attestation and NF391/NF392 strict candidate stop. There is an **always-run** second job that commits typed real job status and last recorded phase to the new research branch, and commits actual native source + exact candidate result **only upon genuine original native and second-attestation success**. An absent/failed/cancelled run remains `UNDECIDED`. It cannot promote RH by passing.

**Acceptance:** a valid native report must include original SHA pins, source frame/16 physical checks, full signed archive, `original_householder_full_dense_Q_constructed=False`, `original_householder_two_vector_isometry_check_pass=True`, original rank-one odd pole identity, valid outward interval identities, zero new signed kernel cells, and an independently recomputed **`STOP` or `INCONCLUSIVE` for frozen (j_{387})**. It does not establish positivity for the full original odd Weil form, or even the original fourth-direction low-band upper unless that is separately proved.

**Open:** selected numeric (W_{\rm odd}(u_4,j_{387})) pending native; actual full original lowband upper; infinite exterior form inverse and signed operator/domain attachment; (W\text{-ODD-NEG}), even/whole Weil, global bridge, RH. No main merge. **No further unrelated source-only threshold tightening until this native result is recovered.**
