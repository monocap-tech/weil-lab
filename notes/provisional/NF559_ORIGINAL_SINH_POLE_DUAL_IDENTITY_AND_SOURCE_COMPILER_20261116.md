# NF559 — Original negative-pole dual identity and compiler-stage recovery

**2026-11-16 PT. Draft stacked on NF558 PR #586.** New source-specific negative-pole polynomial evaluation and the NF557 failed proof repair are committed; focused compiler verification pending. Nothing here certifies original generator independence, unconditional weighted Gram positivity, the signed Weil identity or RH.

## 1. New verified compiler evidence, not inferred acceptance

The NF557 isolated source module failed its actual GitHub Actions compilation (workflow #43968722883, job #133654894603), with a *single* compiler error:

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242DualPolynomialSourceNodes.lean:113:2:
No goals to be solved
```

The preceding line had already proved the 241+1=242 true original Hermite budget by `rw [nf545OriginalOscillatorDimension]`. The trailing `norm_num` was therefore invalid. NF559 deletes the redundant tactic, without changing theorem statements, source multiplicities, or the original frequency table. This is a narrowly targeted **candidate repair** pending new CI.

The NF557 immutable source SHA and full original dual odd-jet 58,564-check audit did **PASS** (workflow #43968722883, job #133654895093).

The NF558 coefficient-injectivity and NF549 physical-source jobs were still queued at the latest observation; do not infer their acceptance. The last completed physical-source compiler chain is NF556 #43967237428 job #133649771908: NF546→NF548 compiled and the first failure was **NF549**, recursion-depth exhaustion in its pointwise Schwartz synthesis. NF558 committed a scoped maxRecDepth adjustment and removed a no-effect simplifier; acceptance pending.

## 2. Genuine source analytic pole separated from its elementary finite dual algebra

The original frozen NF407 selected basis has exactly 241 sine/cosine monomial oscillator rows plus **one genuine final pole row**
```
j_241(x)=sinh(x/2).
```

For odd initial derivative order `2n+1`, the genuine pole coefficient is
```
j_241^(2n+1)(0) = 2^(-(2n+1)).
```

This real analytic fact has been exact-source audited by NF554. To connect it to the original Hermite dual polynomial in Lean, NF559 starts by proving the **finite algebraic identity** rather than jumping directly to an unproved analytic source-derivative statement.

For `a:Fin 242→ℝ`, the actual NF557 original dual is
```
p_a(T)=Σ_(0≤n<242)(-1)^n a_n T^n.
```

At the true negative node `-1/4`:
```
(1/2)*p_a(-1/4)
 = Σ_(n<242) (1/2)*(-1)^n a_n (-1/4)^n
 = Σ_(n<242) a_n*2^(-(2n+1)).
```

This uses the exact power identity `(-1)^n*(-1/4)^n=(1/4)^n` and `(1/2)*(1/4)^n=(1/2)^(2n+1)`. No numerical approximation of π, replacement with another oscillator, or dependence on an arbitrary 242 generator family.

The new source module `WeilDefect/Arithmetic/ActualZetaOriginalJ242OriginalPoleDual.lean` contains candidate Lean theorems

- `neutralNF559OriginalPoleCoefficientIdentity`: the exact scalar power identity for every `n` and real coefficient;
- `neutralNF559OriginalDualPolynomial_pole_eval`: exact original finite dual evaluation equals the weighted original 242 odd pole coefficients.

These proofs depend on the repaired NF557 source polynomial and NF558 exact coefficient module. They are **candidate formal proofs, not yet compiler accepted**.

To turn the second theorem into the genuine left-kernel pole equation, Lean must still establish the actual analytic derivative identity `(d/dx)^(2n+1)sinh(x/2)|_(x=0)=(1/2)^(2n+1)` for every `0≤n<242`. NF559 does *not* silently assume or claim that as a Lean theorem.

## 3. Remaining original oscillator bridge

For each of the **exact** 67 oscillator frequencies `ω_f=2πf>0`, and original monomial order `k<m_f`,

```
j_(f,k)(x)=x^k*sin(ω_f x) when k even,
j_(f,k)(x)=x^k*cos(ω_f x) when k odd.
```

The full NF554 source auditor verified all 58,322 exact oscillator coefficient comparisons, but Lean must still formally differentiate their genuine odd jets and identify their dual relation with

```
F_a(X)=X*p_a(X²).
```

The generic multiplicity transfer `rootMultiplicity ω_f F_a = rootMultiplicity ω_f² p_a`, once `p_a≠0`, has already been **LEAN PASS** at NF556. NF557 and NF558 provide the concrete polynomial degree, source-node and coefficient recovery gates (subject to their own new compiler acceptance). Combining the 67 source multiplicities plus the true pole yields the required 242-degree contradiction after the 68-factor product divisibility theorem is formalized.

## 4. Verification

New `.github/workflows/nf559-original-pole-dual.yml` isolates:

1. Pinned original-source NF557 dual polynomial and node Lean compilation, NF558 coefficient injection, and the new NF559 true negative-pole finite polynomial identity, rejecting proof holes.
2. Genuine NF546→NF551 Lean source chain, including NF549 continuous Gram physical pairing and the NF550/551 downstream analyses.
3. Immutable original NF407 SHA-pinned 58,564 dual odd-jet coefficient audit.

No workflow pass or branch acceptance is assumed until GitHub Actions reports it.

## 5. Next NF560 / non-transfer

Next: use actual NF559 compiler feedback to repair the exact source polynomial/pole module and NF549 source synthesis proof, then formalize actual `sinh(x/2)` odd derivatives in Lean. The original oscillator derivative bridge and 68-node product root-bound remain open. A real square-matrix rank and complex coefficient split are still required before transferring global source independence through NF551 collar identity and NF550 weighted Gram.

The NF528 original positive/negative all-multiplicity divisor source-graph convergence, NF527 full 1/10 coercivity including gamma/prime n=9/both poles, NF539 signed Weil source equality, true real-data conjugation equivariance, W_ODD_NEG and RH **OPEN**.
