# NF560 — Genuine original sinh-pole analytic odd derivatives and the authentic 242×242 matrix

**2026-11-16 PT. Draft stacked on NF559 PR #587. The new NF560 original source-analytic Lean module and focused Actions CI are COMMITTED; compiler acceptance pending. No original global independence, unconditional canonical 242 Gram, Weil signed positivity, W_ODD_NEG, or RH conclusion is asserted.**

## 1. The first authentic odd-initial-derivative calculation in Lean source

NF559 proved a candidate *algebraic* identity relating the finite dual polynomial at -1/4 to the sequence of numerical coefficients 2^(-(2n+1)). The crucial missing piece was to prove that those coefficients are actually the derivatives of the authentic, unchanged NF407 final generator:

```
j_241(x) = Real.sinh (x/2).
```

Mathlib contains two exact source-relevant analytic results, not an external heuristic:

```
Real.iteratedDeriv_odd_sinh (n : ℕ) :
  iteratedDeriv (2*n+1) Real.sinh = Real.cosh

iteratedDeriv_comp_const_mul (h : ContDiff ℝ n f) (c : ℝ) :
  iteratedDeriv n (fun x => f (c*x))
    = fun x => c^n * iteratedDeriv n f (c*x).
```

The second result applies because `Real.contDiff_sinh` holds to all orders. Substituting `c=1/2` and `x=0`, with `Real.cosh 0=1`, directly gives, **for every natural n**,

```
(iteratedDeriv (2*n+1) (fun x : ℝ => Real.sinh (x/2))) 0
      = (1/2 : ℝ)^(2*n+1).
```

This is an actual analytic derivative theorem, not a finite test of a guessed source coefficient list. It uses the original source generator `nf545OriginalSelectedRealGenerator ⟨241,...⟩` via the existing NF545 Lean-accepted pole-is-sinh identity, so the true last source row is not replaced by a formal pole coordinate.

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242ActualPoleOddDerivatives.lean` contains the candidate theorems:

- `neutralNF560SinhHalf_oddIteratedDeriv`: all odd derivatives of `sinh(x/2)` at zero;
- `neutralNF560ActualOriginalPole_oddIteratedDeriv`: identical claim for the actual original index-241 generator, not a substitute function.

**These are source-level Lean proof implementations pending compiler verification.**

## 2. Introduce the actual original analytic 242×242 odd-jet matrix

The same module now defines the object which all preceding Hermite algebra was really designed to invert:

```
A : Matrix (Fin 242) (Fin 242) ℝ
A[n,j] = (iteratedDeriv (2*n.val+1)
             (nf545OriginalSelectedRealGenerator j)) 0.
```

This is the complete **actual** 241 original sine/cosine monomial oscillators and genuine sinh pole, indexed in their exact NF407 order, with derivative orders 1,3,...,483. It is not a symbolic proxy or numerical determinant.

The initial column theorem is

```
A[n,241] = (1/2)^(2*n+1)
```

for all `n : Fin 242`. It is linked to the *actual analytic source* by the preceding theorem, not by postulating these values as a matrix definition.

## 3. Connect the authentic last column to the original dual polynomial

NF559's finite exact negative-pole identity was

```
(1/2)*p_a(-1/4) = Σ_(n<242) a_n*(1/2)^(2n+1),
```

where `p_a(T)=Σ_(n<242)(-1)^n a_n T^n`.

NF560 combines it with the genuine analytic sinh derivative result:

```
Σ_(n<242) a_n * A[n,241] = (1/2) * p_a(-1/4).
```

Hence **the actual original matrix left-kernel pole condition**

```
Σ_(n<242) a_n * A[n,241] = 0
```

implies

```
p_a(-1/4)=0.
```

The proof uses only `1/2≠0`; it does not assume source independence, a Gram eigenvalue, arbitrary polynomial interpolation data, or analytic sign positivity.

The new theorems are

```
neutralNF560ActualOriginalPole_dualOddJets
neutralNF560ActualOriginalOddJetMatrix
neutralNF560ActualOriginalOddJetMatrix_pole
neutralNF560OriginalMatrixPoleKernelForcesRoot
```

along with `neutralNF560OriginalPoleForcesDualRoot`. **Compiler acceptance is pending.**

## 4. What remains of the original oscillator source derivatives

The original 241 oscillator rows still require their **analytic**, source-exact Lean derivative formulas:

```
j_(f,k)(x)=x^k*sin(2πfx)   for even k,
j_(f,k)(x)=x^k*cos(2πfx)   for odd k.
```

For each n,k, we need the iterated derivative identity

```
A[n,(f,k)] =
  0                                       if k>2n+1,
  (-1)^(n+floor(k/2)) (2n+1)!/(2n+1-k)! ω_f^(2n+1-k)
                                          otherwise,
```

where `ω_f=2πf` and the original source group determines k. NF554's SHA-pinned script previously checked all 58,322 oscillator coefficients, but no Lean theorem for the genuine higher derivatives exists yet. Those should be proved by a generic polynomial-times-sine/cosine iterated derivative theorem, then instantiated with the NF545 source index/order table.

Once source derivatives are available, the original left-kernel equations force vanishing of the appropriate derivatives of `F_a(X)=X*p_a(X²)` at each of the 67 positive ω nodes. NF554's accepted Hermite derivative multiplicity and NF556's accepted positive quadratic multiplicity transfer provide the generic root steps. Still needed: 68-node source-multiplicity aggregation/divisibility and finite real-square matrix/complex coefficient bridge. Original global independence and original canonical Gram positivity are still OPEN in Lean.

## 5. Existing compiler recovery accurately stated

- NF542–NF546 original-source modules **LEAN PASS**.
- NF547–NF548 original real-even canonical cutoff modules **PASS within genuine dependent build**.
- NF549 is the next actual completed compiler obstruction: source synthesis recursion depth at `ActualZetaOriginalCanonicalGramPhysicalIntegral.lean:69`; NF558 scoped repair committed, full chain pending.
- NF553–NF556 standalone generic algebraic root-budget infrastructure **LEAN PASS**.
- NF557 source-specific dual polynomial/nodes failed one redundant `norm_num` tactic, repaired NF559; focused retry pending.
- NF558 actual dual coefficient injectivity/new pole dual polynomial NF559 are still awaiting compiler acceptance and transitively precede this NF560 source-analytic module.
- NF557 exact source custody 58,564-entry audit has **PASS**; NF559/NF560 fresh reruns pending.

## 6. Verification, NF561 and non-transfer

New `.github/workflows/nf560-original-sinh-odd-derivatives.yml` separately checks the exact NF557→NF560 original dual and pole analytic Lean chain, replays source custody, and attempts the authentic NF546→NF551 Gram physical source compiler sequence.

**No acceptance is claimed merely from committing a Lean file.**

Next NF561 should repair any NF559/NF560 Lean diagnostics and recover NF549 first, then construct generic analytic polynomial-times-trigonometric odd-derivative identities for the exact original oscillators and integrate their source-specific derivative dual with the 68-node Hermite root budget.

The larger NF528 positive/negative all-multiplicity divisor source graph, NF527 true gamma+prime n9+both poles 1/10 coercivity, NF539 complete signed Weil equality, original real-data correction equivariance, W_ODD_NEG and RH are all **OPEN**.
