# NF394 — Repair native selected-moment execution and persist its result as an original-source receipt

**Date:** 2026-10-29 PT. **Canonical frontier:** `W-ODD-NEG` **OPEN**. This pass is deliberately a *verification/recovery* pass, not a fourth numerical-threshold refinement and not a new exterior harmonic. **No completed original (j_{387}) selected signed moment is asserted at initial custody.**

## Previous → current → next

**Previous NF393:** exact pole-source identity `<u4,s>=<F*T*e4,s>` for `u4=F*T*e4-E*(I+Y0)*T*e4`, `E⊂J242^⊥`, `s=sinh(x/2)∈J242`. Authenticated original 242 selected signed WJJ and 968 WJF archive, SHA-pinned. The genuine NF387 selected trial remained **UNDECIDED** because no completed pole-restored native report was available.

**Current NF394:** discover and repair the **actual GitHub Actions workflow authentication defect** in NF393, then establish a durable result-acceptance contract that can be inspected on the research branch *without relying on the first 50 retrieved workflow runs*. **Next:** fetch `notes/data/provisional/NF394_original_j387_pole_restored_native.json` and `.../NF394_original_j387_selected_native_acceptance.json` if and only if the native source job created them, independently check the original source SHA and exact Boolean result, and then mark only this candidate as STOP/INCONCLUSIVE.

## Concrete workflow defect in NF393

The file `.github/workflows/nf393-original-direct-pole-native.yml` originally contained malformed authentication:

```yaml
env:
  GH_${{ github.token }}: TOKEN
```

instead of

```yaml
env:
  GH_TOKEN: ${{ github.token }}
```

The wrong key was introduced by an overly broad text replacement during workflow authoring. It is an **execution defect**, not a failed original Weil-form calculation. The NF393 parent draft branch was repaired in place with commit `ccfe1f00f73c1e75acf87d83a98511474a937415` before NF394 was branched from its repaired head. This preserves the original NF393 research result and exact mathematical scope. GitHub's commit-workflow connector shows only the first 50 runs for the requested commit and can hide these focused workflows; no claim that a hidden run succeeded or failed follows from its absence.

## Durable native result acceptance architecture

A new **push-triggered** research-branch-only workflow `.github/workflows/nf394-original-native-selected-receipt.yml` runs on the exact branch `research/nf394-native-selected-moment-durable-receipt`, with narrowly limited `contents: write` and `actions: read`. It performs:

1. Exact original NF393 `-Y0*T*e4` source preflight plus NF392 true original selected (j_{387}) polynomial/Bessel gate, using unchanged original SHA pins.
2. Download the historical original archive artifact #12776684037 from the correct repository with correctly declared `GH_TOKEN: ${{ github.token }}`; verify full ZIP SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`, and through the inherited NF390 source program verify historical WJJ SHA256 `33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa`, WJF SHA256 `19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23`, original rank 242, original physical-frame SHA, complete 16 original physical quotient overlaps, and 30,371 archived signed cells reused with ZERO new kernel cells.
3. Run corrected genuine original `scripts/verify_nf390_original_j387_selected_moment.py` at pinned `python-flint==0.8.0` 4096-bit inherited precision. Its original selected moment `<m(D)u4,j387>` restores the **nonvanishing selected odd pole** from direct source overlap `(V*T)[241,3]`; the reconstructed old expression `(H*D*alpha+V*f)[241,0]` must overlap as an independent Arb check.
4. Run `scripts/local_replay/nf394_original_native_j387_receipt.py`: a **second, pure Fraction exact interval checker** requiring original source/frame/archive SHA pins, both physical pole overlap interval intersection, the algebraic enclosure `Wodd + pole = multiplier moment`, the native (j_{387}) norm² interval and selected discrepancy interval, unchanged accepted NF380/NF375/NF387 inputs, and the original NF391/NF392 squared-Bessel candidate decision. Explicitly output **STOP** if the actual candidate is ruled out, otherwise **INCONCLUSIVE**; *never* call an inconclusive candidate PASS or positivity closure.
5. **Only after success**, copy the actual native JSON bytes plus source-attested method verdict to two new, immutable-on-conflict, additive research-branch custody paths `notes/data/provisional/NF394_original_j387_pole_restored_native.json` and `notes/data/provisional/NF394_original_j387_selected_native_acceptance.json`. The workflow commits and pushes these two files back to **only** the NF394 draft branch. It refuses to overwrite differing existing content, does not touch main or any original 49-file package, and its push path selector excludes the resulting data files so it cannot self-loop.

These two resulting files, checked for exact origin/source SHA against the workflow after the native run, are the **positive acceptance evidence**. An absent file proves only "not custodied", not "failed". An incomplete Actions job or invalid native input cannot silently promote a conjectural (j_{387}) result.

## Mathematical obligation is unchanged

The NF392 source-only sufficient rejection gate remains

[
|⟨m(D)u_4,j_{387}⟩-‖j_{387}‖^2| > 1.31\times 10^{-20}
 Rightarrow “	ext{this fixed }j_{387}	ext{ fails the original NF375 fourth low-band acceptance}”.
]

The **native physical (j_{387}) norm² and direct pole-corrected exact intervals** are passed to NF391's stricter squared-rational condition; a rejected (j_{387}) is **not** a negative original Weil vector. An inconclusive result gives no actual original low-band upper. No change to the original 242 selected sources, four matched critical probes, seven-prime signed multiplier, pole, NF369 Y0, NF370 T, original 30,371 signed cells, global source domains, or the canonical open objective.

**NF394 initial verification standing:** authentication defect identified and repaired in parent; full original historical ZIP SHA independently confirmed locally; new authentic native acceptance/branch-archiving contract committed. Actual original selected moment measurement, j387 candidate verdict, source-native job completion and resulting branch files **NOT YET VERIFIED**. Do not infer a green workflow from an authored YAML file.
