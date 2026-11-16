# NF561 — Authentic oscillator higher-derivative kernel, NF558 exact coefficients and NF549 parser recovery

**2026-11-16 PT. Draft stacked on NF560 PR #588. New source-relevant Lean work committed, all NF561 jobs PENDING. No original global independence / canonical Gram strict positivity / signed Weil / RH claim.**

## 1. Latest actual GitHub compiler diagnostics

The NF559 original dual source job, run 43970851150, job 133662294691, had progressed through the repaired NF557 source polynomial and exact 67-node proofs, then failed **in NF558** at the exact coefficient identity:

```
ActualZetaOriginalJ242DualPolynomialCoefficient.lean:25:32
unsolved goal:
(∑ x : Fin 242, if x.val = i.val then (-1)^x.val*a x else 0)
    = (-1)^i.val*a i.
```

The previous proof simplified each polynomial monomial coefficient, but forgot the `Fin.val` injectivity needed to collapse the finite conditional sum. NF561 adds `Fin.val_inj` to that exact simplification. This is a **compiler repair candidate**, not yet verified.

Separately, the NF558 genuine physical source-chain job, run 43969875677, job 133658906218 (also reproduced by NF559 job 133662295096), failed at NF549:

```
ActualZetaOriginalCanonicalGramPhysicalIntegral.lean:59:62
unexpected token 'set_option'; expected 'lemma'
```

NF558's attempt to scope recursion depth inserted `set_option maxRecDepth 4096 in` directly after a doc comment, where the Lean parser expected a theorem declaration. NF561 replaces that with a standalone `set_option maxRecDepth 4096` placed BEFORE the doc comment, then restores `maxRecDepth 1000` after that single theorem. It retains the corrected source Schwartz synthesis expression and removes no physical pairing assumptions. This only fixes the parser; additional elaboration or actual proof errors may still appear once NF549 is compiled. **NF549 compiler acceptance remains PENDING**.

The immutable NF557–NF559 SHA-pinned NF407 58,564 odd-jet coefficient audits have continued to **PASS**, including NF559 job 133662295034 and NF558 job 133658906409. These are exact source audits, not proof acceptance of original analytic derivatives.

## 2. New substantive analytic kernel for original oscillator family

The 241 genuine original oscillator generators have the form

```
j_(f,k)(x) =
   x^k*sin(ω_f*x)  for even k;
   x^k*cos(ω_f*x)  for odd k,
ω_f=2π f,
```

where the rational `f` and order `k` are read unchanged from the NF407 table. The genuine separate pole remains `sinh(x/2)`.

Mathlib contains both `iteratedDeriv_comp_const_mul` for every scaling `ω` and the exact sine/cosine parity derivatives. NF561 creates the focused standalone Lean module

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242OscillatorTrigJets.lean
```

with proposed theorems, for every real `ω` and every `n≥0`:

```
(d/dx)^(2n+1) sin(ω*x)|_(x=0) = (-1)^n * ω^(2n+1).
(d/dx)^(2n)   cos(ω*x)|_(x=0) = (-1)^n * ω^(2n).
(d/dx)^(2n)   sin(ω*x)|_(x=0) = 0.
(d/dx)^(2n+1) cos(ω*x)|_(x=0) = 0.
```

All are proven as *Lean source candidates* from Mathlib analytic higher derivatives; they are not inferred from the Python auditor and have not yet passed GitHub Actions.

The generic original monomial contribution also has a source-relevant Mathlib identity:

```
(d/dx)^m x^k |_(x=0) = if m=k then k! else 0.
```

NF561 attaches the exact `iteratedDeriv_fun_pow_zero` theorem and a candidate combined initial-point Leibniz selector for any smooth `g`:

```
(d/dx)^m [x^k*g(x)]|_(x=0)
   = if k≤m then C(m,k)*k!*g^(m-k)(0) else 0.
```

The proof uses the full true higher Leibniz rule `iteratedDeriv_mul`, not a symbolic hand-inserted formula or substitute generator. This general lemma is the missing reusable kernel for all 241 originals.

Combining it with the trigonometric parity identities above yields, for `m=2n+1` and authentic `ω=2πf`, exactly the source-audited NF554 oscillator formula

```
(d/dx)^(2n+1) j_(f,k)(0)
 = 0                                                        if k>2n+1,
 = (-1)^(n+floor(k/2)) (2n+1)!/(2n+1-k)! * ω^(2n+1-k)  otherwise,
```

where the oscillator parity k even/odd selects sine/cosine. That LAST source-indexed closed form has not yet been derived in Lean from the general NF561 lemma; the generic source-ready mathematical engine is this stage's new target.

## 3. Source-specific integration remaining OPEN

Once NF561's generic trigonometric/Leibniz theorem actually compiles, formalize for each authentic `j_(f,k)` the relation

```
Σ_(n<242) a_n*(d/dx)^(2n+1) j_(f,k)(0)
 =
 (-1)^floor(k/2) * (d/dω)^k [ω*p_a(ω²)]|_(ω=ω_f)
```

with the exact true `p_a(T)=Σ_n(-1)^n a_n T^n`. NF560's genuine source `sinh(x/2)` derivative proof/pole root should compile separately. Then the accepted NF554 Hermite derivative multiplicity and NF556 quadratic multiplicity equality yield the prescribed `m_f` root multiplicities at the 67 positive real squared source nodes. The pole supplies `-1/4`, total 242. A 68-node multiplicity product/divisibility theorem and square finite real/complex matrix rank transfer are still needed to conclude source independence, followed by NF551 local/global and NF550 canonical weighted square to prove strict Gram positivity unconditionally.

## 4. Actual previous results and verification boundary

- NF542–NF546 original source physical modules: **LEAN PASS**.
- NF547–NF548 true smooth source weighted columns and canonical even cutoff: **PASS in genuine dependent build**.
- NF549–NF551 full chain: **OPEN**, latest parse repair committed.
- NF553–NF556 generic polynomial root and quadratic multiplicity architecture: **LEAN PASS**.
- NF557 original source polynomial/nodes: first failed redundant `norm_num` fixed in NF559; NF559 source build passed beyond this file, but full dependent chain failed at NF558.
- NF558 exact original dual coefficients: latest single finite conditional-sum proof failure fixed this stage; **acceptance pending**.
- NF559 finite genuine sinh pole dual algebra and NF560 actual sinh all odd iterated derivatives: **compiler pending**.
- NF561 all frequency-scaled oscillator sin/cos jets plus monomial Leibniz selector: **new source Lean, compiler pending**.
- Original global 242 independence, unconditional real/complex canonical weighted Gram positivity, original real-data correction equivariance: **OPEN in Lean**.
- Original NF528 positive/negative all-divisor source graph convergence, NF527 1/10 gamma+prime n=9+both poles coercivity, NF539 signed Weil equality, W_ODD_NEG and RH: **OPEN**.

New focused CI `.github/workflows/nf561-original-oscillator-jets.yml` builds the new generic analytic oscillator derivatives independently of the pending source polynomial chain, then separately tests NF557→NF560 authentic source proofs, NF546→NF551 physical source chain and unchanged 58,564-entry source audit. No proof holes are allowed in the oscillator module.

## Next NF562

Use actual CI errors to bring the monomial high-derivative selector and both NF558/NF549 repairs to Lean PASS. Prove the FULL exact odd-source oscillator formula for every actual `f,k,n`, then attach it to the true `242×242` analytic odd-jet matrix already defined in NF560. This will be the first complete real-source derivative bridge; then formalize the dual polynomial identity and 68-node product-root degree contradiction, rather than returning to numerical Gram experiments.
