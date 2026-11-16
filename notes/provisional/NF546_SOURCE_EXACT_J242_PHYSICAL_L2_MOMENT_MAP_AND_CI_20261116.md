# NF546 — Original 242 J-source physical L² moment map; NF542/543 accepted; inherited compiler/source audit repairs

**2026-11-16 PT. Draft stacked on NF545 #573. New full-chain Lean CI/source auditor pending.** Original NF407 J242 source JSON SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`, original NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, original NF500 SOURCE-NATIVE RAW output digest `7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05`. That last value is NOT the SHA256 of the separate *NF500 custody JSON* in the repo. Preserve real 242 selected directions including original sinh pole, B=11/10 and delta=1/500, and all zeta-divisor multiplicity copies. No new Weil sign or RH claim.

## 1. ACTUAL compiler recovery

The latest previously queued focused GitHub checks completed:

| Component | GitHub run | result |
|---|---|---|
| NF542 strict original Schwartz compact log Hilbert carrier | [#43900908980](https://github.com/monocap-tech/weil-lab/actions/runs/43900908980) | **LEAN SUCCESS** |
| NF543 exact 242 correction + complete normed graph convergence | [#43900906815](https://github.com/monocap-tech/weil-lab/actions/runs/43900906815) | **LEAN SUCCESS** |
| NF544 original finite-rank Gram inverse | [#43900907060](https://github.com/monocap-tech/weil-lab/actions/runs/43900907060) | FAILED at unknown `Basis.constr_apply_fintype`, line 93; exact theorem does exist in pinned Mathlib `Mathlib.LinearAlgebra.Basis.Defs`. NF546 adds an explicit import. Fresh compilation required. |
| NF545 exact source signature + original source function definitions | [#43903455719](https://github.com/monocap-tech/weil-lab/actions/runs/43903455719) | FAILED both jobs. Auditor mixed NF500 native raw SHA with different custody JSON SHA; fixed below. The two `decide` rational list claims did not reduce; patched to `decide +kernel` for single-pass, kernel-checked finite verification. Fresh compilation required. |

No NF544 or NF545 LEAN PASS is asserted.

## 2. Concrete original full-window L² moments, not an abstract M

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242PhysicalMomentMap.lean` imports the source-faithful NF545 `nf545OriginalSelectedRealGenerator : Fin 242 → ℝ → ℝ`, which is EXACTLY the unchanged original NF407 frequency/order sine/cosine family and sinh pole.

For EACH i<242, let

```
j_i^window(x) = (if x ∈ [-11/10,11/10]
                 then (nf545OriginalSelectedRealGenerator i x : ℂ)
                 else 0).
```

This is the **original full physical window**, NOT a new thin two-collar source or smooth cutoff. The new Lean proof candidate directly establishes that each genuine (j_i\) is continuous globally before truncation, its indicator has compact support, that indicator is measurable and uniformly bounded on its compact window, and hence (j_i^{window}\in L²(\mathbb R,\mathbb C)) by the pinned Mathlib compact-supported bounded-`MemLp` theorem. The windowed L² class is the genuine original physical source generator.

The original true complex-linear physical selected-moment map is THEN DEFINED, not supplied as an arbitrary parameter:

```
J_i := (MemLp j_i^window).toLp,
M_originalCLM : L²(ℝ,ℂ) →L[ℂ] (Fin 242 → ℂ),
M_original = M_originalCLM.toLinearMap,
M_original(f)_i := ⟪J_i,f⟫_ℂ .
```

Moreover, the source map is constructed from the bounded `innerSL ℂ J_i` functionals with `ContinuousLinearMap.pi`, not merely `LinearMap.pi`. The newly included `neutralNF546OriginalSelectedMoments_tendsto` proves actual all-242 source moment convergence from genuine **physical L² convergence** for any sequence or net of physical tests. This is a useful original NF528 correction input, but it is **not** the stronger full true-divisor two-source graph convergence.

The complex convention is essential: this is **linear in f** and conjugate-linear in fixed (J_i). Because the original (j_i) are REAL, the pairing is precisely (\int_{-B}^{B}j_i(x)f(x)\,dx\) (for arbitrary complex (f\), interpreted in the L² sense). This is NOT a new frequency response, finite sample projection, or Green packet.

The source-specific true Gram is now

```
G_original(b) = neutralNF544PhysicalGram M_original b.
```

Under explicit strict positivity of this true Gram for supported smooth columns `b`, NF544's constructed inverse and NF543's admitted original physical log carrier give a corrected Schwartz representative with **all TRUE 242 selected original physical moments preserved exactly**. In that theorem, the formerly abstract 242-moment `M` is **no longer a hypothesis**. The remaining source-specific premise is the actual `b_i=χ j_i` construction and positive weighted-Gram proof, analytically derived in NF545 but not yet Lean-proved.

**Current gate:** module committed; Lean compiler has not yet accepted this proof, so these are proof candidates, not claimed formal theorems until green CI.

## 3. Source-audit repair, not source mutation

NF545 auditor incorrectly checked the SHA256 of `notes/data/provisional/NF500_original_all_242_selected_smooth_log_moment_native_custody.json` against `7e261d...`. The latter is the **original independent source-native RAW output** digest stored in that custody document, not that custody document's own hash. NF546 now checks the original RAW digest *as a field* in NF500 custody JSON, and explicitly records the separate actual custody-JSON digest in the new audit receipt. The original NF407 file's own exact raw SHA256 and its consistency with NF500's `original_nf407_sha256` remain strictly checked. No original file or coefficient changed.

NF545 Lean `decide` failures were exactly two large rational list calculations (distinctness and positivity); NF546 uses `decide +kernel` rather than `native_decide`, retaining proof checking solely in the Lean kernel without trusting compiler-inserted axioms. The old count/241/pole structure is unchanged. This is a candidate repair until CI confirms.

NF544 fix explicitly imports pinned Mathlib `Basis.Defs` to expose `Basis.constr_apply_fintype`; also a compiler candidate.

## 4. Verification

New independent `.github/workflows/nf546-original-j242-physical-moment-map.yml` has two jobs: (i) exact original NF407/NF500 source identity/analytic-signature Python replay and receipt upload; (ii) pinned Lean and Mathlib restore, then strict build NF542→NF544→NF545 rational source signature→NF545 full original 242 generator functions→NF546 original true physical L² moment map; final check rejects proof placeholders.

No legacy errors are hidden behind passing unrelated targets.

## 5. Remaining promotion obligations

1. Green compiler acceptance of full NF544→NF546 chain (NF542/NF543 now green in dedicated runs).
2. Implement a **real even smooth χ inside E** and each explicit original `b_i=χ j_i` as a Schwartz function; prove E support, oddness and the direct physical Gram integral identity `c*Gc=∫χ|Σc_i j_i|²`.
3. Port NF545 actual 136-characteristic-root exponential-polynomial independence proof into Lean and deduce `G_original` is positive definite for real source functions. Existing NF545 proof is ANALYTIC, not Lean-certified.
4. Attach NF528 original inward-affine mollified `g_s` and all original 242 exact moments; prove complete all-true-divisor-multiplicity P/N graph convergence to the singular original (\ell_U).
5. Formal NF527 true gamma+prime n=9+both poles uniform coercivity, NF539 complete mixed signed zero/source identity, source-specific original positive/negative decision. W_ODD_NEG and RH OPEN.

**Disposition:** Source-selected physical moment map now explicitly constructed in Lean code and submitted to compiler; the abstract M premise of NF543/NF544 is removed in the new terminal theorem, but source-specific Gram positivity and the exact smooth columns remain uncompiled.
