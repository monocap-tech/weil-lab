# Weil-Lab — IV012
## Genuine original cross-support quantitative prime/pole/Gamma arithmetic envelope

**Canonical stage:** IV012 (independent Phase IV series, not Phase III NF numerical iteration).
**Stack:** IV006 PR #766 → IV007 #767 → IV008 #769 → IV009 #771 → IV010 #773 → IV011 #774 → IV012 (this stage).
**New kernel standing:** 13 original-source Lean candidates, 4 upstream anchors, strict source-bound kernel verification PENDING. The existence of code, preflight, or PR does not confer theorem acceptance.

### 1. New genuine quantitative arithmetic estimate

For complex Schwartz functions `s,t`, with `supp s ⊆ [-a,a]`, `supp t ⊆ [-b,b]`, `a≤b`, IV011's original mixed physical correlation is

```text
C_b(s,t)(τ) = ∫ x, t(x) * conj(s(x-τ)).
```

A natural NONNEGATIVE physical overlap cost is

```text
J(s,t;τ) := ∫ x, ‖t(x)‖ * ‖s(x-τ)‖.
```

The new original-source candidate proves `‖C_b(s,t)(τ)‖ ≤ J(s,t;τ)` directly from the actual translated-product integral. This is a concrete source bound, not an arbitrary matrix assumption or an application of positive-definiteness of the Weil form.

Under IV011's exact support cutoff `a+b<log(n)` for every `n≥N`, define

```text
Pbudget_N(s,t) := Σ_{n<N} Λ(n)/√n *
                   (J(s,t;log n) + J(s,t;-log n)).
```

The source candidate proves the quantitative genuine mixed-prime bound

```text
‖P_b(s,t)‖ ≤ Pbudget_N(s,t),
```

with all original von Mangoldt coefficients, both sign samples, no discarded prime powers below the exact finite cutoff, and no numerical approximation.

### 2. Original two-pole budget with exact source moments

The actual original two zeta polar residues on the mixed correlation have the exact source moment representation

```text
pole_b(s,t)
  = conj(moment_b(-1/2,s)) * moment_b(+1/2,t)
  + conj(moment_b(+1/2,s)) * moment_b(-1/2,t).
```

This uses the already established original `neutralWindowCorrelation_poleCrossTerms`; it is NOT a new hypothesized pole factorization.

The new nonnegative pole envelope is

```text
Rbudget_b(s,t) =
  ‖moment_b(-1/2,s)‖ ‖moment_b(+1/2,t)‖
  + ‖moment_b(+1/2,s)‖ ‖moment_b(-1/2,t)‖.
```

The source proves `‖pole_b(s,t)‖ ≤ Rbudget_b(s,t)`.

### 3. Genuine archimedean bracket integral

Do not drop or approximate the original Gamma/digamma term. Define

```text
Gbudget_b(s,t) :=
  (1/(2π)) ∫_{ℝ} ‖paperFT(C_b(s,t))(r)‖ * |gammaBracket(r)| dr.
```

Here `gammaBracket` is the actual imported `Zeta23.EF.gammaBracket`. The proposed formal proof uses `norm_integral_le_integral_norm` and the exact original (1/(2π)) normalization to show

```text
‖arch_b(s,t)‖ ≤ Gbudget_b(s,t).
```

The Gamma budget remains a genuine infinite real-frequency integral. IV012 does NOT produce a computable upper interval or prove the budget small.

### 4. The new simultaneous source-specific arithmetic modulus envelope

Let

```text
E_N(b;s,t) = Pbudget_N(s,t) + Rbudget_b(s,t) + Gbudget_b(s,t).
```

By the exact original source split

```text
W_b(s,t) = pole_b(s,t) - prime_b(s,t) + arch_b(s,t),
```

IV012 introduces the actual arithmetic estimate

```text
‖W_b(s,t)‖ ≤ E_N(b;s,t).
```

Every term is now a fully identified physical Schwartz/arithmetic expression on the unchanged original zeta EF. No synthetic matrix replaces the Weil pairing.

For an old finite physical superposition `S=Σ_i u_i•s_i` and newly admitted `t`, if

```text
A = Re Q_a(s,u) ≥ 0,
D = Re W_b(t,t) ≥ 0,
E_N(b;S,t)^2 ≤ A * D,
```

then the sharp source-specific IV010 Schur condition holds automatically:

```text
|W_b(S,t)|² ≤ A*D.
```

The new final candidate therefore gives

```text
∀ v : ℂ, Re W_b(S+v•t,S+v•t) ≥ 0.
```

**The crucial square comparison `E_N²≤AD` and the new diagonal sign `D≥0` are hypotheses, NOT newly proved zeta inequalities.** Moreover this envelope loses cancellations in prime, pole, and Gamma contributions; it may be too coarse for support expansion and might require improvements by mixed spectral structure.

### 5. Formal implementation and acceptance boundary

New module: `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean`.

It declares thirteen concrete source-specific theorem candidates: physical overlap nonnegativity and correlation bound; exact finite-prime envelope positivity and norm domination; exact two-pole source-moment dictionary and norm domination; Gamma absolute integral positivity and norm domination; complete original EF arithmetic envelope positivity and norm domination; conditional envelope-to-Schur transfer; conditional genuine original one-new-support positivity.

Strict audit: `scripts/iv012_original_cross_support_arithmetic_envelope_audit.py`.
CI: `.github/workflows/iv012-original-cross-support-arithmetic-envelope.yml`.

The CI checks all thirteen new plus four existing true source anchors with direct `#print axioms`, only standard Lean axioms `propext`, `Classical.choice`, `Quot.sound`, no `sorryAx`, and SHA-256 binding of actual original source dependencies plus compiled object.

### 6. Upstream compiler recovery

**Live CI information retrieved before IV012 was opened:**
- IV006 run 44798507850 — **LEAN SUCCESS**.
- IV007 run 44800983463 — **LEAN SUCCESS**.
- IV008 run 44812749256 — **LEAN FAILURE** at its mixed-energy Hermitian proof: Lean expressed complex conjugation as `star`, but the rewrite lemma was syntactically stated with `conj`. The same IV008 proof error caused the first IV009–IV011 workflows to fail at import/dependency build, before their new proof modules were compiled.
- A source-level repair normalizing `star` to explicit complex conjugation was committed on **IV008, IV009, IV010 and IV011 branches separately**, with fresh independent CI runs queued. This is a **candidate repair**, not yet accepted by Lean.

IV012 was stacked onto the repaired IV011 head so its proof source contains this upstream compiler repair. Until the upstream IV008 correction succeeds, no IV009–IV012 theorem is kernel-verified.

### 7. What remains open and next stage

Real analytic work still required:
- A **sharper** finite mixed prime bound exploiting disjoint supports or source cancellations rather than only the absolute overlap budget.
- Quantitative Gamma term control with a suitable uniform support-dependent constant, rather than a bare absolute integral.
- A new-support lower bound on `D`, simultaneously for all newly admitted Schwartz directions.
- Sufficiently strong original cross-mixed cancellation estimates to prove `E_N²≤AD`, or a demonstration that this absolute-value majorant cannot deliver it.
- A compatible global all-support Weil criterion and the independent numerical Phase III terminal obligations.

This is **NOT** an enlarged-support positivity theorem, global Weil positivity, or RH.

**IV013 frontier:** evaluate the viability of the newly explicit budget (including unavoidable lower-bound and cancellation obstructions) rather than declaring that the budget-square hypothesis holds.
