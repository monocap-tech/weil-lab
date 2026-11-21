# Weil-Lab — CP026
## Original Hardy-Z narrow-root Lean-attachment architecture: four explicit unpaid numerical premises, not JSON axioms

**Track:** independent original source CP### cross-projection, stacked on CP025 PR #847 → CP024 #846 → CP023 #845 → CP022 #844 → CP021 #843. Original signed Weil support IV###, original NF### physical numerical kernel certification and PI### prime–pole–Gamma investigations are not mutated.

**Acceptance boundary:** This CP026 stage provides new genuine-source **Lean theorem candidates** plus an exact independent arithmetic receipt reconciliation, with **NO new actual original-v4.35 `.olean`/strict standard-only `#print axioms` acceptance**. No original RH, global signed Weil positivity, complete zero spectral (3\times3) identity, zero rank 53, or whole-interval monotonicity claim.

## 1. First, independently reconcile the actual supplied CP025 numerical receipt

The exact uploaded external CP025 receipt was opened and directly inspected, rather than inferred from its filename or earlier prose. Its actual SHA-256 is

`09c7b1935df3c19c7393a6e34ad47d7095206a1fd184fe498e67c8796795f8ec`.

The independent local `/mnt/data/cp025_build.py` integer/Fraction original M=6,N=256 evaluator was run again, and its **all 26 exact rational point-evidence fields** were compared with the uploaded receipt. **26/26 matched exactly**, including all of:
- the three exact rational heights (149.5,150.05352,150.05353);
- first point original finite-phase real value and both endpoints;
- the published theta approximation error and source original remainder error;
- finite first-derivative approximant and explicit total error;
- the exact lower and upper corrected first-derivative margins;
- both exact narrow-bracket signed values after error budgets.

Independent numerical output supports conservative external rational inequalities

[
\boxed{
2.4426< Z'(149.5)<2.4429,
}
]
[
\boxed{
-0.000000682<Z(150.05352)<-0.000000681,
}
]
[
\boxed{
0.000015519<Z(150.05353)<0.000015520.
}
]

These are the original **EXTERNAL** integer-directed mathematical enclosures, with the original analytic comparison lemmas used as described in CP025. No observed mismatch or float-dependent acceptance was found. The uploaded receipt explicitly has `genuine_Lean_v435_olean_or_axiom_receipts_for_new_CP=false`. This step does **NOT** establish a Lean proof of the rational enclosures.

A separate locally generated `cp026_cp025_receipt_reconciliation.json` records the actual file digest, 26/26 rational replay, and false acceptance flags. The GitHub source checker `scripts/cp026_original_point_receipt_replay_and_conditional_lean_gate.py` can likewise take `--uploaded-cp025 /path/to/file` to verify **23 non-height rational values plus three exact rational heights = 26 fields** against fresh execution of the repository's CP025 255+6-term interval program. This uploaded attachment is not silently presumed to exist in GitHub CI; the optional compare runs only when the file is supplied.

## 2. Original source theorem attachment — use the REAL HardyZ error theorem

Actual original published source `Zeta/Zeros/HardyZ.lean` (frozen Git blob `9975442b0c14011c35f4624197d0bf26169c7665`) already proves:
- `abs_hardyZ_sub_re_le'`: for **any** phase and zeta approximant, the error is bounded by phase error times the NORM OF THE APPROXIMANT, plus actual zeta approximation error.
- `abs_riemannSiegelTheta_sub_approximant_two_le`: (|\theta(t)-\widetilde\theta_{2,0}(t)|\le12/t^4) for (t>0).
- `continuousOn_hardyZ`: Hardy-(Z) continuous on (t≥0).
- `hardyZ_eq_zero_iff_riemannZeta`: for (t≥0), (Z(t)=0\iff\zeta(1/2+it)=0).

Original published `Zeta/EulerMaclaurin/Continuation.lean`, true blob `1bb01e946fa7e344497eaf7694fbecff0a714d09`, proves `riemannZeta_eq_approximant_add_remainder`, and original `Zeta/EulerMaclaurin/ErrorBound.lean`, true blob `01184af0dbfd1369e14725e02e990b016bedfe6f`, proves `norm_zetaRemainder_le`.

Genuine frozen Mathlib v4.35 `Mathlib/Topology/Order/IntermediateValue.lean`, true Git SHA `1635b5c20e7716464de9d2735340336c49794dc7`, contains the EXACT `intermediate_value_Ioo` statement: a continuous function on a closed interval which strictly straddles zero has a zero in the corresponding **OPEN** interval.

Unlike CP025 source-only JSON, CP026's new Lean source bridge refers to those actual definitions directly:

[
s_t=\tfrac12+it,\quad
A(t)=\operatorname{zetaApproximant}(s_t,6,256),\quad
\widetilde\theta(t)=\operatorname{riemannSiegelThetaApproximant}(2,0,t).
]
[
\widetilde Z_A(t)=\Re[e^{i\widetilde\theta(t)}A(t)],
\qquad
E(t)=\frac{12}{t^4}|A(t)|+\frac3{10^{13}}.
]

With one explicit actual source premise

[
\operatorname{zetaRemainderBound}(s_t,6,256)\le3\times10^{-13},
]

the genuinely published original theorems yield the exact analytic bound

[
\boxed{
|Z(t)-\widetilde Z_A(t)|\le E(t).
}
]

The point is precise: **the original source error inequality uses (|A(t)|), not (|\zeta(s_t)|)**. It is the actual `abs_hardyZ_sub_re_le'` variant, avoiding an otherwise incorrect numerical error comparison. The original zeta remainder is linked via `riemannZeta_eq_approximant_add_remainder` and `norm_zetaRemainder_le`. No user JSON is imported or transformed into a postulated Lean theorem.

## 3. Four, and only four, outstanding acceptance obligations for narrow-root existence

`cp011_zeta_v435/CP026OriginalPointBridge.lean` introduces **four** independent original-source theorem candidates, with NO imports of NEW local CP013–CP025 Lean proofs:

1. `original_hardy_error_from_source_Borwein`: original published zeta error and theta-error inequalities yield (|Z(t)-\widetilde Z_A(t)|\le E(t)) whenever the original pointwise Borwein bound is supplied.
2. `original_negative_of_finite_certificate`: (\widetilde Z_A(t)+E(t)<0\implies Z(t)<0).
3. `original_positive_of_finite_certificate`: (0<\widetilde Z_A(t)-E(t)\implies0<Z(t)).
4. `original_critical_line_zero_in_narrow_bracket`: from TWO original source-point Borwein premises and TWO strict finite approximant numerical certificate premises, the genuine original HardyZ continuity and Mathlib `intermediate_value_Ioo` prove

[
\boxed{
\exists t\in(150.05352,150.05353):
\zeta\!\left(\tfrac12+it\right)=0.
}
]

The numerical inputs are **all EXPLICIT proof hypotheses, NOT axiom declarations**:

| Unpaid original Lean premise | External mathematical evidence | New Lean acceptance |
|---|---|---|
| (operatorname{zetaRemainderBound}(s_{150.05352},6,256)≤3e^{-13}) | Original Borwein majorant ≤2.8651e−13 from CP020–21 arithmetic | **Pending** |
| Same actual source bound at (150.05353) | Same original radius/collar inequalities | **Pending** |
| (widetilde Z_A(150.05352)+E(150.05352)<0) | CP025 directed integer certificate with strict negative margin | **Pending** |
| (0<widetilde Z_A(150.05353)-E(150.05353)) | CP025 directed integer certificate with strict positive margin | **Pending** |

The local CP026 bridge can be independently compiled, **if/when its own original Lean toolchain is executed**, without waiting for CP013–CP025 new local proof modules. It is explicitly **CONDITIONAL** even after those four bridge theorems compile; it must NEVER be promoted to an unconditional original-zero proof merely because `#print axioms` is standard-only. A theorem with hypotheses can be kernel sound while the hypotheses are unpaid.

The two original pointwise source-Borwein premises are potentially significantly *cheaper* than CP019's full all-circle complex derivative certificate: original zero **existence** needs only (|R(s_{left/right})|), not any derivative of (R). The original **rank 53 and uniqueness/strict monotonicity** tasks continue to require separate original source zero count and (if this route is chosen) whole-interval curvature/first-jet analysis. The CP025 (Z'(149.5)>2.4426) numerical enclosure is **not** silently promoted to a Lean lemma in CP026.

## 4. Real custody implementation, not fake acceptance

- `cp011_zeta_v435/CP026OriginalPointBridge.lean`: standalone genuine original Zeta/Mathlib imports, **four** genuine source theorem proof candidates, exactly four `#print axioms` targets; **no** `axiom`, `sorry`, `constant`, `opaque`; no new local compiled CP dependencies.
- `cp011_zeta_v435/lakefile.toml`: exactly one additional isolated `[[lean_lib]]` target `CP026OriginalPointBridge`. The original v4.35 frozen Zeta and original NF/IV toolchains are unchanged.
- `scripts/cp026_original_point_receipt_replay_and_conditional_lean_gate.py`: source-only precise four-theorem/four-premise check, three original source SHA checks, full original CP025 directed integer replay, optional strict 26/26 uploaded receipt rational comparison, and genuine `.olean`+actual standard-only `#print axioms` fail-closed kernel audit. Source receipt can only say `CP026_TRUE_ORIGINAL_UPSTREAM_SOURCE_BRIDGE_AND_DIRECTED_POINT_REPLAY_PASS_NOT_LEAN`, and flags every numerical original Lean premise as unpaid.
- EXISTING label/manual **source-only** workflow `.github/workflows/cp021-original-independent-leaf-source-only-opt-in.yml` extended with exact CP026 source and replay gate, using already downloaded original three source files. No extra workflow file created.
- EXISTING label/manual genuine **kernel** workflow `.github/workflows/cp021-original-independent-leaf-v435-lean-kernel-opt-in.yml` now builds CP026 as a **third sequential standalone true-upstream compiler target AFTER the two CP021 leaves**, checks four genuine standard-only Lean axiom receipts, and archives its true compiler logs/`.olean`. Same GitHub runner, no new CI fan-out. **No opt-in label applied, no new workflow dispatched**.

The real GitHub baseline at CP026 inspection:
- CP021 PR #843 inherited CP013 original source-lineage run `44878586071`: **completed/success**;
- CP021 PR #843 inherited CP014 original source-lineage run `44878586072`: **completed/success**;
- CP025 PR #847 head had **no** accepted new CP021–CP025 kernel jobs; CP026 is **still source candidate only**.
Neither old source-lineage PASS upgrades the new formal original `CP026` four point-bridge declarations.

**Actual no-kernel disclaimer:** this chat's container does not contain `lean` or `lake` and raw GitHub network DNS is unavailable. The new source-level theorem tactics have **NOT** been elaborated by Lean. They may need compiler fixes, and no unconditional zero theorem has been demonstrated in the kernel.

## 5. Independent mathematics remains open

CP026 isolates the **minimal two-sign existence interface**. It does not prove the original source zero #53 ranking, whole-interval HardyZ monotonicity/curvature, the three-projection Gram↔Weil dictionary, support-independent signed Weil positivity or RH. In particular:

- An original zero somewhere inside this strict narrow interval may be established once the four genuine pointwise source proofs are paid. It is NOT automatically the 53rd.
- CP025 derivative anchor is independent of the two-sign existence proof, even though the external arithmetic already bounds it.
- IV030's phase/prime graph obstruction and PI027's Gamma–prime sign competition remain relevant to any proposed global cross-projection transfer. Neither is solved by critical-line zero certification.

**Next CP027:** close the two original source-point Borwein inequalities using the exact 13-factor original Pochhammer/Bernoulli majorant, preferably independently of full CP019 Cauchy derivative glue; then transfer the CP025 directed interval proof to original rational inequalities by a small, kernel-checkable arithmetic certificate (rather than a huge untrusted JSON blob). Obtain *actual* v4.35 compiler logs for CP021's two original leaves and the CP026 standalone bridge as NF/IV capacity permits. Reconcile source-defined canonical root ordinal only after actual original source proof acceptance.

**NO RH or full signed Weil positivity claim.**
