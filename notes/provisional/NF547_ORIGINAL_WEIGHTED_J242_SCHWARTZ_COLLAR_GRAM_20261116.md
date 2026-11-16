# NF547 — Exact original χ·J242 strict collar Schwartz Gram: eliminate the abstract 242-column family

**2026-11-16 PT. Stacked draft on NF546 #574. All new NF547 Lean proof obligations PENDING actual compiler acceptance.**

## Source custody and established compiler facts

- Unchanged authentic original NF407 selected J242 JSON SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`; exact 67 distinct positive rational oscillator frequencies with 241 contiguous sin/cos monomial modes; final index 241 `sinh(x/2)`.
- Unchanged NF494 original U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, original B=11/10, δ=1/500 strict two terminal collars and all actual zeta divisor multiplicity copies.
- NF542 accepted [#43900908980](https://github.com/monocap-tech/weil-lab/actions/runs/43900908980) LEAN SUCCESS. NF543 accepted [#43900906815](https://github.com/monocap-tech/weil-lab/actions/runs/43900906815) LEAN SUCCESS.
- NF544 inherited Gram module on NF546 [#43933544362](https://github.com/monocap-tech/weil-lab/actions/runs/43933544362) FAILED: missing identifier `Basis.constr_apply_fintype`. The source of pinned Mathlib v4.34.0 declares this inside **namespace Module.Basis** in `Mathlib/LinearAlgebra/Basis/Defs.lean`; merely importing the file was insufficient, so NF547 explicitly uses `Module.Basis.constr_apply_fintype` and opens `Module`. This requires NEW Lean check.
- NF545/NF546 exact source Python audit on [#43933953973](https://github.com/monocap-tech/weil-lab/actions/runs/43933953973) still failed with a **literal escaped newline** in the receipt JSON dict; NF547 fixes that exact syntax, distinct from source-SHA validity. Native-vs-custody hashes are carefully distinguished.
- NF546 prior and latest CI follow-up requires a new full-chain receipt. No unobserved PASS is claimed.

## Actual finite-rank original column construction

The previous abstract proof layers established the algebra

```
NF543: arbitrary M and arbitrary R with M R = I.
NF544: arbitrary M and arbitrary b_j, define G = M ∘ B and R = B ∘ G^{-1}.
NF546: true fixed M_original(f)_i = ⟪ J_i, f ⟫ where J_i are genuine original
       full-window L² indicator versions of original NF407 j_i.
```

**New NF547 Lean source:** `WeilDefect/Arithmetic/ActualZetaOriginalJ242WeightedCollarGram.lean`.

For ONE cutoff `χ : ℝ → ℂ` with `ContDiff ℝ ∞ χ`, `HasCompactSupport χ`, and pointwise `χ=0` outside exact (E=(-B,-B+δ)\cup(B-δ,B)), define

```
b_i(x) = χ(x) · j_i(x),   i : Fin 242,
```

with the exact original `nf545OriginalSelectedRealGenerator` sine/cosine/pole function and its complex cast. The new declarations establish (conditional on compiler):

- `neutralNF547OriginalComplexGenerator_smooth`: each original real-analytic J242 source function is C∞ as a complex-valued function.
- `neutralNF547OriginalWeightedColumn`: **construct** the true source product `χ*j_i` as a genuine SchwartzMap via Mathlib's `HasCompactSupport.toSchwartzMap`, not merely a postulated arbitrary `b_i`.
- `neutralNF547OriginalWeightedColumn_apply`: exact pointwise product identity.
- `neutralNF547OriginalWeightedColumn_supported`: original STRICT E support follows from χ.
- `neutralNF547OriginalWeightedColumns`: the entire fixed indexed 242 source-column family, without any arbitrary column supplied to the theorem.
- `neutralNF547OriginalWeightedGram`: the ACTUAL original physical Gram `G_χ = M_original ∘ B_{χj}`; the original selected physical M is fixed, and the only free input defining G is χ.
- `neutralNF547OriginalWeightedGram_correctedLogCarrier`: under strict Hermitian positivity of this concrete source Gram, NF544 explicitly constructs `R=B G^{-1}`, NF543 corrects ALL **true original** 242 physical moments EXACTLY and NF542 admits the corrected strict collar Schwartz physical test to the **genuine** original logarithmic Hilbert carrier.

No arbitrary `M` or arbitrary `b_i` appears in this terminal theorem. This is a more source-specific operator definition than NF546, while still **conditional** on χ regularity, support, and strict positive definiteness.

## Mathematical Gram positivity proof and remaining Lean obligation

NF545 already provides the complete SOURCE-SPECIFIC analytical proof of the positive definite genuine weighted Gram: source SHA-pinned 67 distinct positive rational frequencies; all 136 roots (\pm2\pi if,\pm1/2) distinct; exponential-polynomial differential-operator annihilation yields independence on each nonempty open collar interval. For a fixed smooth even REAL χ≥0, strictly positive somewhere inside E,

```
Re ∑_i conj(d_i) (G_χ d)_i
    = ∫ χ(x) |∑_j d_j j_j(x)|² dx > 0  for d ≠ 0.
```

That equality and strict inequality are **NOT YET Lean-certified** for the concrete NF547 source definition. Nor is the existence of an even REAL positive χ explicitly constructed in Lean; NF547's complex-valued cutoff parameter does NOT by itself ensure reality, evenness, positivity, or oddness of the corrected test. These are separate source-specific premises to discharge, not hidden conclusions.

For physical graph membership of the 242 correction columns, the source-aware Fourier estimate from NF545 requires **u-dependent derivative terms** in the strip, not the older incorrect omission:

```
|F_b(t+iu)| ≤ e^{B/2}(‖b''‖_1+‖b'‖_1+¼‖b‖_1)/|t|²
  for |t|≥1, |u|≤1/2.
```

That repaired estimate is in the NF545 note inherited by NF547. The complete actual-positive and actual-negative divisor P/N source graph convergence for the original singular `ell_U` remains independent of boundedness of the correction columns.

## Verification and next promotion

New independent `.github/workflows/nf547-original-j242-weighted-collar-gram.yml` builds repaired NF544, NF545 exact list, NF545 real generator family, NF546 original full-window L² moment map, and NF547 original χj source-weighted Gram. It also runs `python3 -m py_compile` and an exact source-native SHA audit, and rejects `axiom`, `admit`, `sorry` placeholders. **Source and Lean CI pending at submission.**

NF548 priority: obtain accepted NF544→NF547 compiler receipts; construct one genuine real even nonnegative `C_c∞(E)` χ with positive open collar mass, show (G_χ) physically equals weighted original source integral, and formalize the 136-characteristic-root independence to promote analytic strict Gram positivity into Lean.

Remaining separately: original full P/N graph limit and NF528 mollifier, NF527 true gamma+n9+both poles `Q≥(1/10)‖f‖²` Lean, NF539 mixed signed source identity, original W_ODD_NEG and RH OPEN.

**Scope:** NF547 is an authentic original source-attachment increment and compiler-repair PR. It does not assert universal Weil positivity, RH, a nonzero signed test, or an unconditional Lean proof of the weighted Gram.
