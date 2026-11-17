# NF565 — Exact original 242-frequency Hermite polynomial, all formal derivatives and focused source compiler recovery

**2026-11-16 PT. Draft stacked on NF564 PR #596. New actual-source algebraic bridge and targeted source compiler fixes COMMITTED, acceptance pending. No original global independence / unconditional canonical Gram strict positivity / signed Weil / W_ODD_NEG / RH claim.**

## 1. New complete algebraic structure of the true original odd-jet dual

The source-exact original NF557 coefficient polynomial is

```
p_a(T) = Σ_(n:Fin 242) (-1)^n a_n T^n
```

for the **original odd derivative row coefficient vector** `a : Fin 242 → ℝ`. The actual source signature has 67 distinct positive rational oscillator frequency groups, 241 original sine/cosine monomial generators, and one genuine `sinh(x/2)` pole. NF560 pole analysis and the original coefficient injectivity now **LEAN PASS** as one combined NF562 workflow (`43979662203`, job `133692558469`), with no surrogate source or polynomial assumption.

NF565 introduces `WeilDefect/Arithmetic/ActualZetaOriginalJ242FrequencyHermitePolynomial.lean` and defines the exact frequency-side finite polynomial

```
F_a(Z) = Σ_(n<242) (-1)^n a_n Z^(2n+1).
```

It proves candidate Lean identities:

```
F_a(Z) = Z * p_a(Z²)
```

as an **actual polynomial identity over ℝ**, and

```
F_a(freq) = freq*p_a(freq²)
```

for every real frequency. These identities preserve the true original signed dual coefficients and historical source dimensions; there is no abstract 242-control substitution.

More importantly, NF565 implements for **every natural k** the explicit formal-polynomial higher derivative formula

```
(D_poly^k F_a)(freq)
 = Σ_(n:Fin 242) (-1)^n a_n *
      Nat.descFactorial(2n+1,k) * freq^(2n+1-k).
```

The proof uses Mathlib's formal polynomial `iterate_derivative_sum`, `iterate_derivative_C_mul`, and `iterate_derivative_X_pow_eq_C_mul`. This is precisely the algebraic right-hand side needed by *each* historical monomial oscillator's analytic derivative left-kernel constraint. It is the finite algebraic half of

```
Σ_n a_n D_x^(2n+1) j_(f,k)(0)
  = (-1)^floor(k/2) (D_poly^k F_a)(2πf).
```

The actual-source derivative half still requires NF562's formalization of `x^k sin(2π f x)` and `x^k cos(2π f x)` for all k, plus a signed factorial identification and source-specific 67-block aggregation.

**The new polynomial and derivative proofs remain source-dependent Lean CANDIDATES until CI runs; no claim of kernel acceptance.** The independent NF553–NF556 generic degree, Hermite derivative/root multiplicity and quadratic square-node transfer theorems remain Lean accepted.

## 2. Recover original NF561 trigonometric and Leibniz compiler from precise pinned logs

The latest NF561 workflow at NF564 head (`44001580451`, job `133766705609`) FAILED but passed the earlier fatal `ω` binder parse error and real monomial cast mismatch. It stopped at three concrete residual source issues:

1. `Real.iteratedDeriv_odd_sin` and `Real.iteratedDeriv_even_cos` rewrite to **function-valued** products `((-1)^n * Real.cos)` evaluated at zero. The proof tried to rewrite `Real.cos_zero` before distributing function multiplication. NF565 explicitly uses `Pi.mul_apply`, then `Real.cos_zero`, and `ring_nf` for the exact frequency-power exponent normal form.
2. The original NF561 finite higher Leibniz selector's `simp only [Finset.sum_ite_eq', Finset.mem_range, Nat.lt_succ_iff]` had already CLOSED its goal. A trailing `split_ifs <;> simp_all` produced the actual compiler diagnostic `No goals to be solved`. NF565 deletes only this redundant tactic.
3. No original function formula, rational frequency, finite dimension, cutoff or source parity has been changed; only proof implementation.

The new NF565 workflow isolates this source derivative compilation from the independent original frequency polynomial and the physical NF550 compiler chain.

## 3. Original NF549 is accepted; NF550 still open

The genuine original NF542–NF549 physical and analytic synthesis is compiler-accepted. The NF563 canonical weighted-square job (`43982599680`, job `133702586898`) FAILED at NF550 on a.e. finite `L²` synthesis, exact inner-product conjugation order and real/complex integral coercions. NF564 committed targeted fixes and scoped Lean recursion; its latest NF550 compiler jobs were still queued at NF565 creation. **NF565 does not claim NF550 success merely by inheriting these changes.**

The actual weighted Gram goal remains

```
Σ_(j<242) conj(d_j) * Gχ(d)_j
 = ∫_ℝ χ(x) |Σ_(j<242) d_j j_j(x)|² dx.
```

This is a nonnegative exact source identity once accepted. Unconditional strict positivity requires a separate full original analytic generator independence theorem (unproved in Lean).

## 4. Verification architecture

New `.github/workflows/nf565-original-frequency-hermite-and-lean.yml` independently tests:

1. Genuine original 242 signed dual coefficients, 67 source-node structure, source-defined `F_a=Xp_a(X²)` and **all k formal polynomial derivatives**, with no source-independent substitution.
2. Repaired real scaled sin/cos and monomial Leibniz initial jets, true 241 source-indexed oscillator higher derivatives and first original k=0 positive squared root theorem at f=37/64.
3. Original NF549→NF550 complete authentic physical weighted-square and dependent NF551 analytic collar source.
4. SHA-pinned exact NF407 original 58,564 odd-jet symbolic source custody, including the true sinh pole.

No new axioms, `sorry`, or `admit` are introduced in the new algebraic module. **All NF565 new compiler jobs pending.**

## 5. Outstanding obligations and NF566

The next proof target is to match the explicit NF565 formal polynomial derivative coefficient

```
(-1)^n a_n * descFactorial(2n+1,k) * freq^(2n+1-k)
```

with the exact NF562 analytic source odd-jet coefficient for every original oscillator, including both k parities, **as a finite 242-term sum**. Then the literal left-kernel vanishing for `j_(f,k)` yields the formal `D_poly^k F_a(freq_f)=0` for all `k<m_f`. Accepted NF554 Hermite multiplicity, NF556 transfer to `p_a(freq_f²)`, and the genuine sinh-pole `p_a(-1/4)=0` must be assembled into a simultaneous **68-node 242-multiplicity divisor** whose degree contradicts the NF557 `p_a` degree bound. A square real matrix kernel argument, complex coefficient split, and NF551 analytic collar transfer then remain before unconditional strict positive canonical Gram.

NF528 authentic all-positive/negative divisor graph convergence, NF527 gamma+prime n9 and both-pole 1/10 coercivity, NF539 signed Weil identity, real-data correction conjugation equivariance, W_ODD_NEG and RH **OPEN**.

## 6. Finite parity preservation and current workflow acceptance boundary

The frequency polynomial module additionally proves a candidate **odd-evaluation identity**
```
F_a(-freq) = -F_a(freq)
```
from the exact source-level `F_a(freq)=freq*p_a(freq²)`. This mirrors the genuine odd symmetry of all 242 original generators, with no new assumption. It has not yet passed the pinned Lean compiler.

NF565 draft PR #597 opened and the new `NF565 original frequency Hermite polynomial and source compiler closure` workflow **queued** (initial run #44002413454). Its jobs for original algebraic frequency-side polynomial, original analytic 241 oscillators, physical NF550 Gram, and source SHA custody are **PENDING**. The previous NF564 `nf564-exact-original-odd-jet-source-audit` job #133766712702 is **PASS**, while its new oscillator/NF550 compiler jobs were still queued or running. No mathematical theorem beyond the accepted original pole and NF549 physical chain is upgraded to LEAN PASS before those runs finish.
