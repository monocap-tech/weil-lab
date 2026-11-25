# Weil-Lab — IV011
## Exact original cross-support prime cutoff and strict Schur failure witness

**Canonical research stage:** IV011, separate from NF### Phase III numerical production.
**Stack:** IV006 #766 → IV007 #767 → IV008 #769 → IV009 #771 → IV010 #773 → IV011 (this stage).
**Kernel:** **PENDING.** Twelve source-specific Lean theorem proof candidates and four upstream anchor receipts must pass a real Lean kernel build before any acceptance claim. The source and this note distinguish exact proposed facts from verified compiler status.

## 1. Why IV011 is not another formal 2×2 PSD lemma

IV010 exposed the necessary genuine original arithmetic one-site extension condition. With an old superposition `S`, newly admitted physical Schwartz test `t`, old energy `A`, mixed new cross term `B`, and new diagonal `D`, the exact real diagonal is

    Re W_b(S + v•t, S + v•t) = A + 2 Re(B*v) + D |v|².

The old fixed-support positivity work can constrain `A`. But an enlarged test class cannot inherit nonnegativity without an actual bound on new-support `D` and `B`.

The new mathematical work in IV011 acts directly on the **original mixed arithmetic prime term** in `Zeta23.EF.literatureRHS`, rather than merely importing the abstract positivity criterion.

## 2. Authentic mixed Schwartz correlation has support radius a+b

Let `s : 𝓢(ℝ,ℂ)` be supported in `[-a,a]`, and `t : 𝓢(ℝ,ℂ)` be supported in `[-b,b]`, with `a≤b`. No real, odd, nonvanishing or RH assumptions are imposed. The ORIGINAL L² window correlation at the LARGER window is

    C_b(s,t)(τ) =
      neutralWindowCorrelation b
        (s.toLp 2 volume) (t.toLp 2 volume) τ.

IV011 proves as a source-bound Lean candidate, using the existing true a.e. Schwartz-to-window dictionary, that

    C_b(s,t)(τ) = ∫ x : ℝ, t(x) * conj(s(x-τ)).

If the product is nonzero, then `x∈[-b,b]` and `x-τ∈[-a,a]`, forcing `|τ|≤a+b`. Thus the exact **mixed** support radius is `a+b`:

    a+b < |τ| ⟹ C_b(s,t)(τ) = 0.

This improves the coarse same-large-window bound `|τ|≤2b` whenever the old support radius a<b, with no approximation or new source.

## 3. The original prime side truncates FINITELY

Define the unmodified actual mixed arithmetic prime term

    P_b(s,t) =
      Σ'_{n:ℕ} (Λ(n)/√n)
        [ C_b(s,t)(log n) + C_b(s,t)(-log n) ].

For every `n` with `a+b < log n`, both literal prime samples vanish. An integer `N` with `log n > a+b` for all `n≥N` exists because `N>exp(a+b)` can be chosen by Archimedean growth.

The source proves an exact, NOT approximate equality:

    P_b(s,t) =
      Σ_{n<N} (Λ(n)/√n)
        [ C_b(s,t)(log n) + C_b(s,t)(-log n) ].

Only finitely many genuine original von-Mangoldt coefficients remain. No extra zero cutoff, unverified analytic summability, abstract sieve, or synthetic arithmetic oracle is inserted.

**Important limit:** this finite-support argument does not bound the remaining sum tightly enough to establish the missing determinant inequality `|B|²≤AD`. The finite sum's size/sign is a new mathematical estimate.

## 4. All original arithmetic contributions retained

The source defines the actual mixed poles

    pole_b(s,t) =
      paperFT(C_b(s,t))(i/2) +
      paperFT(C_b(s,t))(-i/2),

the unchanged original Gamma/digamma term

    arch_b(s,t) =
      (1/(2π)) ∫_ℝ paperFT(C_b(s,t))(r) * gammaBracket(r) dr,

and the exact finite original mixed prime term `P_b(s,t)`.

Then the actual original zeta Weil mixed value decomposes exactly as

    W_b(s,t) = pole_b(s,t) - P_b(s,t) + arch_b(s,t).

After the cutoff, the sole unbounded prime SERIES disappears from the source arithmetic expression, leaving a finite original prime-power sum and the two unchanged analytic terms. This is a concrete analytic reduction, not an unconditional positivity theorem.

For the new-support diagonal `D=W_b(t,t)`, the old function and new function coincide, so the relevant prime radius becomes `2b` instead. This confirms that mixed prime truncation alone does not transfer the old local (2/5) lower bound to new supports.

## 5. Exact failure witness for the real original Weil block

Assume the new diagonal `D=Re W_b(t,t)` is strictly positive.

The exact minimizing complex coefficient for the original real block is

    v* = -conj(B)/D

where `B=W_b(S,t)`.

The formal algebraic identity is

    A + 2 Re(B*v*) + D|v*|² =
      (AD - |B|²)/D.

Consequently, if the actual original zeta cross-support inequality fails, `|B|²>AD`, then the ACTUAL physical Schwartz superposition `S+v*•t` has strictly negative original signed Weil value.

This gives a **concrete falsification mechanism** with the unchanged original full zeta explicit formula, not a proxy Gram example. No candidate example or violation is claimed to exist.

The converse is also formalized conditionally. When `A≥0` and `D>0`, combining IV010 sufficiency with IV011's negative-witness necessity yields

    [∀ v∈ℂ, Re W_b(S+v•t,S+v•t) ≥ 0]
      ↔ [|W_b(S,t)|² ≤ A D].

The right side is still the missing source-specific *analytic inequality*, not an assumption discharged by the cutoff.

## 6. Formalization ledger

Twelve new proposed Lean declarations:
1. `neutralIV011MixedCorrelation_eq_schwartzIntegral`
2. `neutralIV011MixedCorrelation_vanish_far`
3. `neutralIV011MixedPrime_logFar_vanish`
4. `neutralIV011ExistsPrimeCutoff`
5. `neutralIV011OriginalMixedPrime_eq_finite`
6. `neutralIV011OriginalMixed_arithmeticSplit`
7. `neutralIV011OriginalMixed_finitePrimeArithmetic`
8. `neutralIV011SchurMinimizer_value`
9. `neutralIV011SchurFailure_negative`
10. `neutralIV011OriginalCrossFailure_negativeWitness`
11. `neutralIV011OriginalCrossBound_necessary`
12. `neutralIV011OriginalOneNew_nonnegative_iff_crossBound`

Actual original source:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean`

Standalone pipeline:
`.github/workflows/iv011-original-cross-support-arithmetic.yml`

Strict source-bound axiom auditor:
`scripts/iv011_original_cross_support_arithmetic_audit.py`

It requires a real Lean build, an actual compiled `.olean`, all twelve new and four upstream actual-source `#print axioms` receipts, only the standard Lean axioms `propext`, `Classical.choice`, `Quot.sound`, and SHA-256 of the compiled object and all source dependencies. It rejects `sorryAx`.

The source preflight is NOT a compiler acceptance certificate. IV006–IV010 upstream source candidates and other required source modules must independently pass before this kernel chain can be accepted.

## 7. Remaining mathematical obstruction and IV012

**Open new analytic statements:**
- An upper bound for the **finite genuine mixed prime sum** strong enough, after including full original pole and arch contributions, to imply the actual cross-support determinant inequality.
- A strict or non-strict lower bound on the NEW diagonal `D` outside the frozen original collar.
- Uniform control over **every** old finite physical superposition, not merely each old test separately.
- A coherent multi-site extension beyond a single newly admitted Schwartz direction.

Neither the prime cutoff nor the strict failure witness proves a real negative original zeta example, a new positive support radius, universal Weil positivity, or RH.

**IV012 suggestion:** source-specific quantitative cross-support prime bound and Gamma/pole separation, with an audit of which estimates are genuinely capable of delivering the required Schur inequality rather than recycling abstract PSD facts.

**Milestone:** finite original cross-support arithmetic reduction and explicit source-specific positivity-failure criterion, pending Lean kernel verification.
