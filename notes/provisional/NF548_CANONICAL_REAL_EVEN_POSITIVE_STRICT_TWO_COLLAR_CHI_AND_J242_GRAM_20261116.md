# NF548 — Construct ONE canonical real even nonnegative smooth cutoff inside the original Weil endpoint collars

**2026-11-16 PT. Draft stacked on NF547 #575. Compiler acceptance pending; no RH proof.** Source custody: original NF407 J242 SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce` (67 distinct rational frequency groups, 241 genuine sin/cos oscillator modes plus exact `sinh(x/2)` index 241); original NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`; B=11/10, delta=1/500, full genuine zero multiplicity unchanged.

## 1. First ACTUAL cutoff, rather than existence hypotheses

The pinned Mathlib `ExistsContDiffBumpBase.u : ℝ → ℝ` has a kernel-proved C∞ smoothness theorem, nonnegativity `u(x)≥0`, evenness `u(-x)=u(x)`, and **exact** `Function.support u = Metric.ball 0 1`. It is therefore nonzero everywhere in `(-1,1)`.

Take EXACT rational parameters
```
c = 1099/1000 = B - delta/2,
r = 1/2000 = delta/4,
chi_real(x) = u((x-c)/r) + u((x+c)/r)
            = u(2000*(x-c)) + u(2000*(x+c)),
chi(x) = (chi_real(x) : ℂ).
```

The support of the first summand is precisely `(c-r,c+r)=(2197/2000,2199/2000)`; the second is its negative reflection. The ORIGINAL geometry is
```
E = (-11/10, -11/10+1/500) ∪ (11/10-1/500, 11/10)
  = (-1.1,-1.098) ∪ (1.098,1.1).
```
The two new inner bump intervals are **strictly inside** E and do not replace E: they are deliberate strictly interior support regions within the original exact physical collars.

This one `χ` is therefore real, even, nonnegative, C∞, compactly supported, identically zero outside original E, and STRICTLY POSITIVE on the entire open interval `(c-r,c+r)` (and its negative reflection). All these are explicit mathematical assertions about this exact χ, not hypotheses on a supplied arbitrary χ.

The file `WeilDefect/Arithmetic/ActualZetaOriginalCanonicalEvenCollarCutoff.lean` implements the actual cutoff and Lean proof candidates for each of the following, with theorems:
- `neutralNF548RealEvenCollarCutoff_smooth`
- `neutralNF548RealEvenCollarCutoff_even`
- `neutralNF548RealEvenCollarCutoff_nonneg`
- `neutralNF548RealEvenCollarCutoff_supported` — EXACT old E geometry
- `neutralNF548RealEvenCollarCutoff_hasCompactSupport`
- `neutralNF548RealEvenCollarCutoff_pos_center`
- `neutralNF548RealEvenCollarCutoff_pos_interval` and its reflected open interval
- complex cast smooth/support/compact/even
- `neutralNF548CanonicalOriginalWeightedGram` — fixed genuine source operator.

They are UNCOMPILED until the new pinned GitHub check succeeds.

## 2. THE full original Gram is now a fixed mathematical object

NF543: abstract M,R. NF544: generic columns b and invertible G. NF546: actual selected full physical-window (J_i=1_{[-B,B]}j_i) in complex L² and concrete `M_original(f)_i=⟪J_i,f⟫`. NF547: actual source (b_i=χj_i) Schwartz columns, but χ passed with analytic side conditions. NF548 now fixes **the actual χ** and hence

```
G_548 = M_original ∘ [ d ↦ ∑_{j<242} d_j · (χ j_j) ].
```

No arbitrary moment map, column family, or cutoff remains. The original pole is the actual index 241 and all 67 source oscillator frequencies are fixed.

New terminal module `WeilDefect/Arithmetic/ActualZetaOriginalCanonicalGramRightInverse.lean` defines `neutralNF548CanonicalOriginalColumns`, `neutralNF548CanonicalRightInverse`, the exact all-242 right-inverse identity, strict-E support of its range, and `neutralNF548OriginalMomentMatchedLogCarrier`.

**Only one crucial source-specific finite-rank premise remains in the terminal theorem**:

```
for all d : Fin 242 → ℂ, d ≠ 0,
    0 < Re (∑ i, conj(d_i) * (G_548 d)_i).
```

The operator constructed here is a single **canonical actual-source** Gram with explicit original collar geometry. NF545 gives the ANALYTIC proof for the original 136 distinct characteristic roots and real analytic (j_i): with actual real χ≥0 positive on a nonempty open set, (d^*Gd=∫χ |∑d_i j_i|²>0) for every nonzero d. However, **neither the full weighted Gram integral identity nor the exponential-polynomial independence/strict positivity has yet been compiled in Lean**. NF548 absolutely does not claim unconditional formal positivity.

## 3. Compiler recovery and verification state

On NF547 base, focused NF542 [#43900908980](https://github.com/monocap-tech/weil-lab/actions/runs/43900908980) and NF543 [#43900906815](https://github.com/monocap-tech/weil-lab/actions/runs/43900906815) were accepted **Lean PASS**. Subsequent NF544→547 chain required targeted namespace/receipt repairs; the last NF547 workflows [#43942322940](https://github.com/monocap-tech/weil-lab/actions/runs/43942322940) and related NF544/NF545/NF546 inherited checks had been queued at the time of NF548 work; do not claim their successful completion.

New independent `.github/workflows/nf548-original-canonical-even-collar-cutoff.yml`:
1. Python syntax check plus SHA-pinned true original NF407/NF500 242-source frequency/pole audit, exact source receipt.
2. Pinned Lean and Mathlib cache, sequential build original NF544→NF548 dependencies, reject axiom/sorry/admit placeholders.

**Compiler acceptance of all new NF548 Lean proof candidates is pending.** If inherited modules fail, inspect exact job log and repair with a fresh check. No automatic RH inference.

## 4. Remaining strict promotion gates

1. Compile original NF544→NF548 chain to actual accepted Lean, not only source strings.
2. Show the **actual** canonical source Gram (G_{548}) equals the weighted original physical integral (∫χ\,\overline{j_i}j_j) by L² inner-product/Schwartz a.e. compatibility.
3. Formalize the original distinct-frequency exponential-polynomial theorem in Lean, including the 136 characteristic roots `±2πif` and `±1/2`, and derive strictly positive Hermitian form on the canonical χ.
4. Attach actual NF528 original mollified approximants (g_s), preserve all exact 242 moments via the fixed R, prove true full-multiplicity two-source P/N graph convergence to original singular `ell_U`.
5. Independently compile NF527 true gamma/prime n=9/both pole (Q≥1/10‖f‖²), NF539 full true signed original source identity, and original accepted sign.

W_ODD_NEG, full even/odd Weil positivity, and RH remain OPEN. **Disposition:** χ and hence G are no longer hypothetical original objects; they are fixed mathematically and represented by new Lean source. Weighted Gram positivity is analytically justified by original-source uniqueness, but awaits formal Lean certification. No root or data substitutions.
