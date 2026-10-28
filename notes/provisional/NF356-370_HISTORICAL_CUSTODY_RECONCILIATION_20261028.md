# Weil-Lab — NF356–NF370 historical custody reconciliation

**2026-10-28.** The original NF356–NF364 49-file package is byte-custodied on draft PR #356, stacked on draft PR #355. **No mathematical/theorem status is promoted.** The canonical `active_obligation` remains `W-ODD-NEG` **OPEN**. No merge to `main`.

## 1. Source recovery and non-destructive transfer

- Original ZIP SHA256: `18a70ff301da621a9aaaaa420922a544f17e46a5f905947d6433932c962fa1fc`. Exactly 49 files, including the original historical workflow and the 48-entry SHA256 file manifest.
- The 46 non-parent files were transferred losslessly using `notes/data/provisional/transfer/NF356-364_NONPARENT_PAYLOAD.tar.xz.b64`, xz SHA256 `0a62aae0307b37c5ef1d13ce13a608dbf5699e3b4ee2d00569a2be303a3e507f`.
- The three *original* native snapshot JSONs were restored from SHA-pinned PR #348/#350/#355 GitHub Actions artifacts. Original ZIP hashes, respectively: `735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968`, `3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09`, `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`.
- **PR #350 final accepted artifact ID is `12770022548`, not `12752629674`.** The historical staging runner preserved in the 49 files had the old ID but expected the final ZIP SHA; that historical `--download` mode therefore fails. Preserve it as historical evidence; the corrected verifier downloads final artifact ID and runs the original historical checks with `--offline`.
- Manifest SHA256 `ba22fbea27c06c6725807d906e5af1ddfd96026bae3d6e679238b02ed52f05ed` covers all 48 listed files; the manifest is the 49th file. The restored file hashes are checked byte-for-byte. No different existing file is overwritten. No NF365–NF370 result was changed by this transfer.

## 2. GitHub verification and exact scope

Restoration workflow run **40770378835** completed successfully after the GitHub token workflow-file permission boundary was handled separately: it validated and committed the original historical notes/data/scripts; the final original workflow was added by the authorized GitHub connector, byte-for-byte.

Reconciled post-transfer workflow **40770808980 SUCCESS**: checked all **49 committed original paths** (`new 0; already identical 49`), every manifest record, all three original ZIP and child JSON hashes, and **nine historical portable rational checks**: NF358, NF359, NF360, NF361, NF362, NF363 producer, NF363 independent replay, NF364 producer, NF364 independent replay.

The historical `.github/workflows/provisional-nf356-364-custody.yml` remains byte-exact but its download path is a **STOPPED transport method** because of the original PR350 ID mismatch. Its red status is not to be reported as successful CI. Use the corrected `.github/workflows/nf356-364-historical-verify.yml`. Verification demonstrates **historical evidence provenance and independently replayed arithmetic only**—NOT original native/Arb recomputation, original functional-analytic domain acceptance, or whole Weil sign.

## 3. Typed results

| Object | Status | Scoped result; unresolved remainder |
| --- | --- | --- |
| PR #348, #350, #354, #355 | **ACCEPTED SCOPED PARENTS**, conditional on original form/domain | Original critical four-plane, J242 leakage, finite signed selected Gram, physical quotient and finite exterior probe data; **no full signed Schur** |
| NF356 stronger exterior floor ~0.009981 | **PROVISIONAL LOCAL** | Replayed calculation; new native/Arb CI and operator-domain audit absent |
| NF357–NF359 residual/energy-dual preflights | **PROVISIONAL** | No complete strong/form-dual exterior residual upper |
| NF360 uniform 0.99832 inverse sufficiency | **STOPPED** (NF361, conditional strengthened floor) | False sufficient gate; **not** an actual Weil negativity result |
| NF361–NF364 min–max/no-go, directional Neumann, original Fourier/pole tail | **PROVISIONAL, HISTORICALLY REPLAYED** | Actual projected whole-exterior response not computed |
| NF365 matched physical/positive-energy projection | **SCOPED ALGEBRA CI** | Strong positive action not inferred from L2 closeness |
| NF366 bounded Kminus quotient transport | **SCOPED CI REPLAY** | Original positive strong action still open |
| NF367 positive form and weak-form quotient transport | **SCOPED CI REPLAY** | Whole signed inverse not bounded |
| NF368 four-plane positive margin | **SCOPED EXACT REPLAY** | Finite 4D only, strong residual uncomputed |
| NF369 original 8D signed finite Schur | **SCOPED NATIVE+RATIONAL CI** | Finite exterior correction `D_E < P4/8000` is only a Galerkin **lower slice** of full correction |
| NF370 original-source Feshbach shear and dyadic `T,d` budget | **SCOPED IDENTITY/ACCEPTANCE GATE** | Full exterior matched covariance `R* C^-1 R` **UNMEASURED** |
| Whole complement, remaining 238 selected directions, original-domain audit, even/whole Weil, RH | **OPEN** | No W-ODD-NEG O1/O2 proof or arithmetic RH closure |

These states are mathematical **jurisdictions**. A passing replay or native focused workflow is not a theorem promotion.

## 4. Obligation graph (historical cursor → current gap)

```text
#348 critical 4-plane + #350 original leakage + #354 J242 signed block + #355 quotient
      │                       [ACCEPTED SCOPED / inherited domain]
      ├── NF356 floor [PROVISIONAL] → NF360 scalar gate [STOPPED by NF361]
      ├── NF357–364 [PROVISIONAL, nine historical checks REPLAYED]
      └── NF365–367 physical/form transfer [SCOPED]
                 ↓
          NF368 selected 4D margin [SCOPED]
                 ↓
          NF369 original 8D finite Schur [SCOPED]
                 ↓
          NF370 source shear / dyadic residual budget [SCOPED]
                 ↓
         **OPEN** matched whole signed exterior residual
              R* C^-1 R <= P4 - D_E
                 ↓
         **OPEN** other 238 J242 modes and all mixed coupling
                 ↓
         **OPEN** complete original O1/O2 + inherited domain audit
                 ↓
         **OPEN** even / whole Weil / arithmetic RH transfer
```

Here `C` is the positive *signed exterior form* realization on `J242^perp`, not `QW^-1Q`; `D_E` is a finite Galerkin lower approximation to the full correction. Four-plane positivity alone does not close the other 238 selected dimensions.

**Stopping rule:** The 49-file historical source custody is reconciled; proof closure is not. Do not launch NF371 or treat the package's existence as mathematical acceptance. When research is separately resumed, the necessary gate remains an actual certified full exterior form-dual residual upper on NF370's fixed original directions. `W-ODD-NEG`, inherited original-domain review, even/whole Weil and RH remain **OPEN**.
