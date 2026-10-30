# NF401 — Recover actual original NF400 242-dimensional native column from failed independent receipt

**2026-10-30 PT.** Canonical obligation `W-ODD-NEG` OPEN. Research branch stacked over NF400 PR #386; no source modification, no 242×242 signed matrix reintegration, no main merge.

## Previous → current → next

**NF400 previous:** Authentic [GitHub original-native run #41024355742](https://github.com/monocap-tech/weil-lab/actions/runs/41024355742) executed source-only preflight, 4096-bit original physical Gram/frame, 16 quotient overlaps, verified original full 30,371-cell signed archive ZIP, four archived reflector transforms, and completed the **entire original 242-dimensional selected signed/multiplier column computation**. The log explicitly printed `NF400 authentic original signed 242-column / j387 contraction PASS` and a projected norm interval. It took about 171.59 seconds for the complete native original computation; this did not fail or time out.

The **next**, independent exact receipt command failed at `scripts/local_replay/nf400_original_selected_column_exact_receipt.py` line 79 while evaluating `F(native['certified_global_source_archive_D_frame_l2_error_upper'])`. The native producer stored an Arb **interval** as the string `[mid +/- radius]`, not a Fraction literal. The numeric ball was approximately `[1.17098e-299 +/- 7.59e-1532]`; the receipt parser rejected its *representation*, not the sign, physical Gram, column moment, or an impossibility theorem. The run has `original-native-column: failure` (from the receipt), `durable-receipt: success` (typed failure saved), and the genuine completed **unaccepted** native output was archived as [artifact #12964112303](https://github.com/monocap-tech/weil-lab/actions/runs/41024355742/artifacts/12964112303), ZIP SHA256 `eda8bff1c1fa8289cc514d5956a57af2b65e1fa2cd0e4771ed68d74fcf1c7b8e`. Historical source commit of the original run: `0ef3078dfa15c73f35c60180cb23133c1cd6c18b`; actual original NF400 branch now `1f6532d52a6e999b67affe6f6df837f03312dbe1`, with failed typed receipt. **Do not reinterpret the original workflow as passing.**

**NF401 current:** Restore the independent receipt's ability to parse the original Arb interval representation *without changing the native source report*. Its `exact_arb_upper` parser checks an exact rational first; otherwise matches exactly `[decimal midpoint +/- decimal radius]`, converts both decimals into exact `Fraction(Decimal(...))`, and uses **midpoint+radius** (never midpoint) as the conservative original upper bound. A standalone exact regression verifies rational and error-ball formats and refuses negative radius, non-ball and NaN.

A new dedicated branch-only workflow retrieves **only** the actual original NF400 Actions artifact #12964112303, authenticates its complete original ZIP SHA, and runs the corrected independent 242-entry receipt against the unmodified recovered bytes. It checks the NF398 true signed j387 original moment SHA, source archive/frame/physical/pole SHA, all 242 raw and transformed moment outward intervals, the exact dyadic two-coordinate original j387 re-contraction, projected Gram norm/norm-square compatibility and original tiny error upper, and the original native j387 scalar report. Only on a genuine pass does the always-run status job commit the preserved native column, scalar crosscheck and exact acceptance JSON with original source hashes and typed successful NF401 receipt. Otherwise the execution is recorded with `accepted=false` and the original source artifact remains external.

**Next:** Upon accepted original 242D column, inspect the actual projected norm and source-adapted raw coefficients. The genuine `J242^perp` lowband norm **upper** is a different obligation: NF400 exact gate `||(I-P)t_L|| <= 2.75e-13` would suffice for `||t_L-Pm(D)u4||<2.8e-13` under the inherited source-domain realization, but has NOT been measured or established. Do not confuse the finite selected norm with an upper on the complement or RH.

## Scope

The mathematical complete-column formula remains the NF400 finite identity. NF401 is a **source-recovery/verification** pass that either promotes the actual original 242D numerical computation to source-verified standing or records the exact remaining execution defect. No fresh original signed kernel cells, no newly invented candidate or external theorem, no main merge, no whole original odd form classification. `W-ODD-NEG`, even/whole Weil and RH OPEN.

## Post-execution acceptance and mathematical consequence

**Genuine source recovery now ACCEPTED.** [NF401 original-source Actions #41109578378](https://github.com/monocap-tech/weil-lab/actions/runs/41109578378) completed both native source-recovery and durable-receipt jobs **SUCCESS**. Actual original NF400 unaccepted run #41024355742 stays a recorded **FAILURE**: no retroactive run-status rewrite. Original byte-identical native 242D JSON is now permanently preserved on this NF401 unmerged branch with SHA256 `644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515`; independent exact Fraction receipt validated 242 interval rows, source/physical/pole/frame hashes, nonzero original dyadic j387 raw two-coordinate recontraction, physical Gram norm² compatibility and exact outgoing archived error-ball upper. The original ZIP digest is verified; zero new signed kernel cells. The accepted projected norm is approximately

```
||P_J m(D)u4|| = 0.7028719679151...    (original 242D physical projection)
```

This is **not** `||t_L-P_J m(D)u4||`, not original `J242^perp` mass and not an upper for the full lowband error. The inherited original strong Fourier realization and original/source domain remain separately audit-required.

**New universal source-dependent candidate localization:** write `w=m(D)u4`, `t_L=w-e`, and `||e||<=H` at unchanged `Lambda=2^24`, `tau=2.8e-13`. If `j∈J242` satisfies the proposed norm lowband fit `||t_L-j||<=tau`, orthogonal projection `P_J` gives

```
||j-P_J w|| <= ||j-P_J t_L|| + ||P_J e|| <= tau+H.
```

The source-pinned accepted native interval, NF398 highband bound and exact Fraction comparisons verify

```
tau+H < 329/10^15 = 3.29e-13,
||P_J w||_lower > 702871967/10^9 + (tau+H),
||P_J w||_upper < 702872/10^6.
```

Hence **every** possible selected lowband fit, if one exists, must lie in the fixed physical Hilbert ball

```
||j-P_J m(D)u4|| < 3.29e-13,  ||j||>0.702871967.
```

This sharpens NF399's lower norm `>0.3153944` without scanning more selected trial vectors. All valid candidates are narrowly **localized in physical norm** around one now source-authenticated original projection. The geometric restriction is independent of how original selected raw coefficients happen to represent that vector; it is not itself a Fourier-tail or coefficient-quantization certificate.

**Next stopping interface:** inspect original **Fourier high-frequency tail of this now determined selected projection**, with source coefficient dynamic range and cancellation paid outward, against the limited `3.29e-13` candidate adjustment, *and* independently assess original `J242^perp` lowband norm upper. The tail and complement are different interfaces. A large selected norm by itself does not certify failure, positivity or an RH resolution. Never invert the archived n512/n513 lower observations into a complement upper.

**Permanent evidence:** `notes/data/provisional/NF401_original_242D_execution_receipt.json`, `NF401_original_242D_selected_column_source_native.json`, `NF401_original_242D_selected_column_independent_acceptance.json`, `NF401_original_j387_scalar_crosscheck_source_native.json`; new `scripts/local_replay/nf401_original_selected_projection_localization.py` and focused exact workflow. No main merge.
