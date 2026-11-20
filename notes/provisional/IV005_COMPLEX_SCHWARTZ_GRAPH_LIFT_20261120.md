# Phase IV — IV005: arbitrary complex compact Schwartz full-divisor graph lift

**Research status:** complete Lean source **candidates** committed. No Lean kernel run, no strict axiom audit, no claim of unconditional accepted IV005 theorem. This is an **isolated Phase IV research branch**, not an NF-series numerical/physical matrix runner stage. No new Actions workflow or PR is triggered. Existing IV003/IV004 candidates are not silently assumed accepted.

## 1. Unexpected structural reduction: no new zeta-zero counting estimate needed

We previously expected arbitrary complex smooth graph lifts to require independent vertical-strip decay bounds and a zeta zero-count theorem. Source inspection reveals a sharper route **using the already accepted NF533 two-argument zeta explicit formula**.

Let `s : 𝓢(ℝ,ℂ)` have compact support in the same original finite window `[-a,a]`. Define the anti-linear reflection

```text
s†(x) = conj(s(-x)).
```

Its *actual* source-normalized positive-exponent raw Fourier transform obeys

```text
F_(s†)(z) = conj(F_s(conj z)).
```

This has no reality or oddness assumption and holds for every complex z. The source-bound IV005 reflection lemma proves it by a measure-preserving substitution, then transports it to authentic `neutralWindowEvaluation` via the existing NF573 a.e.-window/raw transform bridge.

Now consider the genuine mixed physical correlation

```text
k(t) = neutralWindowCorrelation a ((s†).toLp 2 volume) (s.toLp 2 volume) t.
```

Because `s` is compact smooth, NF534's *already proved* `neutralWindowCorrelation_contDiff_of_ae_smoothSecond` makes `k` C². Its support is compact, since this is an actual finite-window correlation. The actual EF theorem `neutralActualZetaDivisor_rawTransform_summable_of_contDiff` (NF533) therefore supplies

```text
Summable [q ↦ conj(F_(s†)(conj z_q)) * F_s(z_q)]
```

over EVERY original actual zeta zero coordinate `q`, including all multiplicity copies, without truncating the divisor.

By the reflection identity,

```text
conj(F_(s†)(conj z_q)) * F_s(z_q)
      = F_s(z_q)^2.
```

Consequently, absolute convergence of the mixed EF summands gives

```text
Σ_q |F_s(z_q)|² < ∞.
```

Finally `neutralActualZetaDivisorPairEquiv` is an already-accepted bijection of the complete conjugate divisor, so the partner family `Σ_q |F_s(conj z_q)|²` also converges. These are exactly the two input obligations for `neutralActualZetaFullSourceLiftOfRawSamples` (NF537).

**This is a structural recovery, not a conjectured positivity estimate and not an RH-dependent argument.** Its correctness at the level of new *Lean source composition* remains compiler/audit-pending.

## 2. Physical carrier custody is also already generalized

NF542's existing `neutralSchwartzPhysical_quadraticFourierMoment` supplies the actual quadratic Fourier moment for any complex Schwartz `s`. The generic accepted

```text
neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
```

then constructs `k : NeutralLogHilbertCarrier a` with

```text
neutralLogPhysical k.val = s.toLp 2 volume.
```

With the two authentic `ℓ²` raw sample receipts above, NF537 constructs a genuine `NeutralActualZetaSourceDomain a` element with exactly that physical coordinate.

The main proposed IV005 theorem is therefore:

```lean
theorem neutralIV005ComplexSchwartz_fullSource
    (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ∃ v : NeutralActualZetaSourceDomain a,
      neutralLogPhysical (neutralActualZetaSourcePhysical a v).val =
        s.toLp 2 volume
```

**No real-valued assumption, no oddness assumption, no fixed two-collar support, no original 242 generators, no numerical sources, and no RH assumption.** The window `a` remains an explicit input, not a hidden choice.

A companion candidate handles any compactly supported complex `C^∞` test `ψ` through Mathlib's existing `HasCompactSupport.toSchwartzMap`, preserving its original L² class.

## 3. New files, and dependency isolation

| Source | Function |
|---|---|
| `ActualZetaPhaseIVComplexReflection.lean` | Construct `s†` with genuine Schwartz closure, fixed-window support, exact a.e. representative and actual complex Fourier reflection |
| `ActualZetaPhaseIVComplexSchwartzFullSource.lean` | From NF533 mixed EF derive BOTH full-divisor sample ℓ² families; combine with existing NF542 physical log carrier and NF537 full source graph lift |
| `ActualZetaPhaseIVAnyComplexMixedEF.lean` | Compose IV005 arbitrary complex source lifts with **pending** IV004 mixed graph/EF dictionary for two independently arbitrary complex tests sharing a finite window |
| `scripts/verify_iv005_complex_full_source.sh` | Manual-only sequential local Lean build plus strict proof axiom/source hash audit |

The first two files depend ONLY on existing NF source theorems. They deliberately **do not** depend on IV003 or IV004. This allows their kernel proof to be evaluated separately, even if the new IV004 mixed EF composition needs elaboration repairs.

The third file is a higher-level **conditional on its imported source module being kernel accepted** composition, and must not be counted independently of IV004 verification.

## 4. What the proposed composite yields

Given two arbitrary complex Schwartz tests `s,t` supported in `[-a,a]`, there would be genuine source-graph lifts `u,v` preserving their physical classes, and — after separate IV004 kernel acceptance — an exact *arithmetic* mixed EF dictionary

```text
B_a(u,v)
  = Zeta23.EF.literatureRHS
      (neutralWindowCorrelation a
        (t.toLp 2 volume) (s.toLp 2 volume)).
```

No `real` or `odd` guard survives; the quantification reaches every **complex compact Schwartz test within any chosen finite window**.

This is not yet support-window naturality: the graph spaces `NeutralActualZetaSourceDomain a` change with a, and the statement does not prove their physical forms are compatible under changing a. It also does not prove that every possible external Weil-criterion test has been normalized into this `s` class.

## 5. The exact surviving Phase IV obligations

1. **Compiler and kernel verification** of all new IV003/IV004/IV005 proof candidates with only standard Lean axioms and preserved source SHA. Until then, the new graph lift is a mathematical **candidate**, not accepted.
2. **Variable-window naturality / unwindowed dictionary**: prove that the mixed and diagonal literal EF values are invariant when a containing window is enlarged, and align the Fourier sign/involution and external Weil test class exactly.
3. **Global signed positivity**: prove `B_a(u,u) ≥ 0` for all appropriate lifts, or the equivalent PSD mixed Gram condition, uniformly over all admissible supports. The existing graph norm bound and old fixed-collar coercivity do not yield it. This can be as difficult as the original RH criterion; do not disguise it as a routine compilation step.
4. **No Phase III closure inference**: original analytical-bank, physical-entry, matrix-product and payment certification are independent of this Phase IV retyping.

## 6. Assessment

The suspected *new analytical summability estimate* is likely a **typing issue** rather than missing mathematical machinery: the accepted two-argument literal EF already contains enough absolute convergence to certify both raw sample families if paired with the **correct conjugate-reflected complex test**.

This eliminates the special real-odd symmetry input at the proposed graph-entry level. It does not eliminate the global mixed-sign question.

**IV005 could close the complex source-graph-entry component outright after Lean verification. It does not by itself move global Weil positivity or RH from open to proved.**
