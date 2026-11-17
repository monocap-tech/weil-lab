# NF564 — Exact original oscillator Lean binder recovery and canonical NF550 Gram physical integral repairs

**2026-11-16 PT. Draft stacked on NF563 PR #591. Source-specific repairs COMMITTED; new NF564 focused GitHub verification PENDING. No unconditional original 242-generator independence, strict canonical Gram positivity, signed Weil positivity, W_ODD_NEG, or RH claim.**

## 1. Actual new completed Lean evidence

The NF562 workflow `43979662203`, job `133692558469` **PASSED**:

```
nf562-original-pole-source-lean: SUCCESS
```

This is a significant source-specific recovery: the exact original 242 dual polynomial/nodes (NF557), 242 coefficient injectivity (NF558), genuine sinh pole dual polynomial (NF559), and **actual analytic sinh(x/2) odd derivative and source-indexed 242x242 odd-jet matrix pole identity (NF560)** all compile as a single dependency chain at the NF562 source head. The parallel NF561 original-dual-pole compilation also **PASSED** (run 43979662476, job 133692559874), confirming the pole chain is no longer stopped at the former power-rewrite bug.

Separately, the entire original source SHA-pinned 58,564 exact odd-jet coefficient replay continued to **PASS** in NF562 and NF563 workflows, including job 133702586897.

The latest NF563 `43982599680`, job `133702586345` standalone original sine/cosine source compiler **FAILED** at the NF561 general trigonometric/monomial module, *before compiling the new first positive-node source theorem*. The NF562 exact 241 oscillator module failed at the same upstream import. Precise compiler messages:

```
ActualZetaOriginalJ242OscillatorTrigJets.lean:27:38:
 unexpected token 'ω'; expected '_' or identifier
```

repeated for all four frequency-scaled real sine/cosine declarations. The Greek symbol `ω` has a reserved token conflict in the pinned Lean syntax, despite its mathematical conventionality. The exact other errors were `Nat.cast (if m=k then k! else 0)` vs `if m=k then (k!:ℝ) else 0` and an unresolved final conditional finite Leibniz sum. These are compiler/syntax failures, not incorrect derivative identities.

## 2. NF564 oscillator compiler repairs

NF564 directly edits the genuine source-ready higher derivative files:

- `ActualZetaOriginalJ242OscillatorTrigJets.lean`
- `ActualZetaOriginalJ242MonomialTrigOddJets.lean`
- `ActualZetaOriginalJ242FirstSineOddJetDual.lean`

All original real angular frequency **binders** formerly spelled `ω` are renamed `freq` (no frequency value, function or source coefficient changes).

The arbitrary-frequency analytic identities remain exactly

```
D^(2n+1) sin(freq*x)|_0 = (-1)^n * freq^(2n+1)
D^(2n)   cos(freq*x)|_0 = (-1)^n * freq^(2n)
D^(2n)   sin(freq*x)|_0 = 0
D^(2n+1) cos(freq*x)|_0 = 0
```

The monomial initial-jet theorem now explicitly converts the Nat-valued `if` under its real cast using `Nat.cast_ite` and `Nat.cast_zero`. The real higher-Leibniz selector converts the casted monomial conditional before distributing multiplication and collapsing the `Finset.range` sum. These are **proof candidate repairs**, compiler acceptance pending.

Once accepted, the exact NF562 indexed 241-source odd derivatives, the original two source parity/factorial formulas, and the NF563 real first positive-source `f=37/64` `k=0` signed-dual root theorem will be able to compile without the former parsing stop. Other Lean proof errors may still arise downstream.

## 3. NF549 has passed; next exact original Gram compiler stop is NF550

The original physical source-chain in NF563 successfully compiled all NF546→NF549 authentic physical L²/collar/canonical source integral modules. NF563 main job `43982599680`, job `133702586898`, **FAILED** subsequently at `ActualZetaOriginalCanonicalGramWeightedSquare.lean`. The errors explicitly name:

1. `Lp.coeFn_fun_finsetSum` returns a pointwise lambda sum while `eventuallyEq_sum` supplies a sum of functions. NF564 replaces it with `Lp.coeFn_finsetSum`, matching the exact types of finite sums of representatives before `Finset.sum_apply`.
2. Normalizing `Pi.basisFun.equivFun` inside the true 242-index linear synthesis exceeded the default recursion bound. NF564 scopes `maxRecDepth 4096` to the genuine finite source a.e. synthesis theorem, then returns to `1000`.
3. The inner-product term in Mathlib is `y*conj x`, whereas the pointwise weighted source-square theorem has `conj x*y`. NF564 states the commutative complex multiplication step explicitly and then applies the exact NF550 source pointwise norm-square identity. **No bogus convention swap is allowed.**
4. The integrand `∫x, ((real χ*norm²):ℂ)` was not recognized by the previous unqualified direct rewrite. NF564 states an explicitly typed complex Bochner integral equality using Mathlib's `integral_ofReal`, then takes real parts.

All repairs preserve the authentic 242 original sine/cosine/sinh generators, NF546 full physical window `[-11/10,11/10]`, NF548 real nonnegative even two-collar cutoff χ, NF549 physical (L^2) source pairing and original NF550 Gram. **NF550 source compilation remains pending**; no strict-positivity theorem has been concluded.

The accepted physical chain is **NF542–NF549 LEAN PASS**, with NF550 and the downstream NF551 local-global analytic identity not yet accepted as a complete chain.

## 4. Genuine finite mathematics and remaining non-transfer

The original source signature has been checked directly from the actual immutable NF545 Lean list: the first genuine frequency is exactly `37/64` with multiplicity 14; all 67 original frequency/multiplicity pairs are present, 241 oscillator columns, plus authentic separate `sinh(x/2)`. NF563's conditional source k=0 lemma, once its compile passes, will give for every original k=0 index

```
Σ_n a_n [D^(2n+1) j_i](0) = freq_i * p_a(freq_i²).
```

The first authentic source left-kernel equation yields `p_a((2π·37/64)²)=0`. NF553–NF556 generic polynomial degree, Hermite derivative multiplicity, and positive root-square multiplicity transfer are **LEAN PASS**. The source proof still needs higher multiplicity `k>0` equations for each frequency, a simultaneous real 68-node root multiplicity/divisor budget, and real-square matrix plus complex source global independence. No unconditional strict positivity follows from merely writing the weighted-square integral.

## 5. Verification and next NF565

New `.github/workflows/nf564-original-trig-and-gram.yml` separately compiles the generic sine/cosine/monomial engine, the original 241 indexed oscillator and closed parity jets, the first exact positive source oscillator polynomial evaluation, the genuine NF550 weighted physical-square identity and NF551 dependent continuation, plus independently replays exact original 58,564-entry source custody. All compiler jobs currently PENDING.

NF565 priority is to consume actual compiler logs, correct any remaining NF561 Leibniz or NF550 physical Gram errors and secure **Lean PASS** of both, then complete the authentic source-indexed odd derivative-to-`D^k (freq*p_a(freq²))` correspondence for `k>0`. After that, prove 67 positive squared-frequency multiplicity contributions plus the -1/4 sinh pole sum 242, so a nonzero polynomial `p_a` of degree ≤241 cannot annihilate all 242 original odd-jet columns.

NF528 original full positive/negative divisor source graph convergence, NF527 complete gamma+prime n9+both poles 1/10 coercivity, NF539 signed Weil source identification, true real-data correction conjugation-equivariance, W_ODD_NEG and RH **OPEN**.
