# NF565 — Original 67-block source Hermite multiplicities, exact 68-node root budget, NF561 compiler recovery

**2026-11-16 PT. Draft stacked on NF564 PR #592. New NF565 source-specific algebraic and finite root-budget Lean modules and NF561 compiler repairs COMMITTED; fresh compiler acceptance PENDING. This is not a claim of unconditional original J242 independence, strict canonical Gram positivity or RH.**

## 1. Verified upstream

- The genuine original NF407/NF545 index-241 selected function **sinh(x/2)**, its all-order odd initial derivative formula and the negative squared-frequency dual evaluation are **LEAN PASS**, NF562 workflow run `43979120808`, source-pole job `133690686104`. A true original 242-row left-kernel pole equation therefore forces `p_a(-1/4)=0`.
- NF542–NF549 genuine original L² physical moment/canonical cutoff/continuous Gram integral have previously **LEAN PASS**, including exact NF549 within NF561 dependent build.
- NF553 generic degree obstruction, NF554 derivative vanishing→root multiplicity, NF555 quadratic factorization, NF556 exact positive-root multiplicity transfer are **LEAN PASS**.
- The new NF564 full all-241 oscillator analytic-to-Hermite bridge and NF550 physical weighted-square repairs have **NO new ACCEPTED CI** as of NF565 commit. Jobs in run `43987898385` were still queued at latest query. No inferred compiler acceptance.

## 2. Original 67 real source frequency blocks, not generic interpolation assumptions

The true original selected oscillator table has 67 rational groups `g=(f,m)`. Its unchanged expansion is

```
nf545OriginalSelectedOscillatorNodes
  = originalGroups.flatMap fun (f,m) =>
      (List.range m).map fun k => (f,k).
```

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242FrequencyBlockHermiteMultiplicity.lean` formalizes the source-index coverage theorem:

```
∀ g∈originalGroups, ∀ k<m_g,
  ∃ i : Fin 241, nf545OriginalOscillatorNodeAt i = (f_g,k).
```

This is the missing **source multiplicity aggregation** step. It proves that each historical original frequency block supplies all prescribed derivative orders `k=0,...,m_g−1`, not only the zero-order sine generator. The proof uses the *literal* original `flatMap/List.range` expansion and list index membership, with no fabricated oscillator or assumed frequency multiplicity.

Composing the NF564 candidate analytic original source derivative-to-polynomial equation with these genuine indices gives all Hermite conditions:

```
∀ g∈originalGroups, ∀ k<m_g,
  eval (2πf_g) ((Polynomial.derivative^[k]) F_a) = 0,
F_a(X) = X*p_a(X²).
```

The new source file then uses the **already-accepted** NF554 and NF556 generic Mathlib theorems to derive the candidate **actual source** root-multiplicity bound (assuming `p_a≠0`):

```
m_g ≤ rootMultiplicity ((2πf_g)²) p_a.
```

A separate lemma proves `F_a≠0` from `p_a≠0` using Mathlib's **injective polynomial expansion** `expand ℝ 2 p = p.comp (X²)`, not a source independence axiom. The real frequency `2πf_g` is positive because every original rational `f_g>0` and `π>0`.

**ALL new frequency-block assembly theorems are formal Lean CANDIDATES pending CI.** Their upstream NF564 oscillator source-analytic bridge is likewise awaiting its own compiler acceptance.

## 3. Exact original 68-node weighted ledger

New `WeilDefect/Arithmetic/ActualZetaOriginalJ242Exact68NodeBudget.lean` constructs explicitly:

```
[ (((2π)² * real(f²)), m) | (f,m) in frozen NF545 groups ]
  ++ [(-1/4,1)].
```

This keeps the source exactly:

- 67 genuine positive-frequency real square nodes, each with its ORIGINAL individual oscillator monomial multiplicity m;
- ONE separate actual negative real `-1/4` sinh pole (not a 68th oscillator);
- exactly **68** weighted source entries;
- pairwise distinct real node first-coordinates, using NF557 original exact rational-square nodup and strict sign separation of the last negative pole;
- combined multiplicity **Σ m+1=241+1=242**;
- **no numerical π rounding**, source replacement or estimated root product.

The proposed Lean theorems are `neutralNF565Actual68WeightedNodes_length`, `neutralNF565Actual68WeightedNodes_nodup`, `neutralNF565Actual68WeightedNodes_budget`. Their CI acceptance is PENDING.

## 4. General simultaneous multiplicity degree obstruction

New independent Mathlib-based `WeilDefect/Arithmetic/ActualZetaOriginalJ242FiniteRootBudget.lean` provides an abstract **finite distinct-root budget theorem**:

Given any real polynomial p, distinct real node Finset s and prescribed natural weights m, if

```
∀ x∈s, m(x) ≤ rootMultiplicity x p
AND
natDegree(p) < Σ_(x∈s) m(x),
```

then `p=0`. The proof translates Mathlib's `rootMultiplicity` into the counts of p's actual root multiset, bounds the count on the selected finite nodes by the full root multiset cardinality, and uses `Polynomial.card_roots'` to bound that cardinality by degree. This is **a candidate Lean implementation pending compiler acceptance**; it strengthens the last original degree criterion without computing a determinant.

The next finite task is to instantiate that generic Finset weight theorem *specifically* with the 68-entry original ledger, prove exact weight transport through distinct node mapping, and combine the now-verified true sinh root and the NF565 per-block conditional oscillator multiplicities to conclude `p_a=0`. That final original source global certificate is NOT established by NF565.

## 5. Actual NF562 compiler failures repaired

The latest actual NF562 workflow rerun `43979662203`, oscillator job `133692558052`, **FAILED** in `ActualZetaOriginalJ242OscillatorTrigJets.lean` with precise new parser/elaboration errors:

1. `open scoped ContDiff` reserves **ω** as analytic/smoothness notation, so source theorem binders `(ω : ℝ)` produced `unexpected token 'ω'` at four oscillator-derivative theorem declarations. NF565 renames that LOCAL scalar variable `freq` throughout the file, preserving every actual original source frequency value and theorem type.
2. The Mathlib `iteratedDeriv_fun_pow_zero` lemma elaborates a cast of a Nat-valued if-expression, while the source goal has an if-expression returning real casts. NF565 changes the proof from `simpa only` to full `simpa` to normalize this coercion.
3. A separate overly strict `simp only` step in the initial-point higher Leibniz theorem reported `simp made no progress`; NF565 combines the exact original Mathlib monomial derivative theorem, sum selector and index facts into one targeted simplification.

These are real compiler-diagnosis-driven adjustments. **Compiler acceptance pending**. Their failure had blocked genuine source-indexed NF562, NF563, NF564 oscillator theorems; no such upstream success is inferred.

NF562's separate source-pole job `133692558469` **PASS**, and exact SHA-pinned full 58,564-entry original odd-jet source audit job `133692558642` **PASS** in this same workflow.

The NF562 physical Gram job `133692558521` still failed on the earlier NF550 a.e. L² finite-sum/conjugation/real-integral proof mismatches; NF563/NF564 committed later repairs but their new focused jobs were still queued. **NF550–NF551 remain OPEN in Lean.**

NF565 additionally corrects a likely fragile NF564 `(-1)^n` parity proof rewrite by establishing a precise standalone exponent factorization before rewriting the outer sign expression. This preserves the signed analytic math.

## 6. Acceptance matrix

| Obligation | Status |
|---|---|
| Original NF542–NF549 physical L²/cutoff/integral | LEAN PASS |
| Original NF550 weighted-square / NF551 local-global | COMPILER PENDING |
| Generic NF553–NF556 root-degree and quadratic multiplicity | LEAN PASS |
| Original NF557–NF560 dual coefficient & true sinh pole | LEAN PASS inside NF562 source-pole build |
| Original NF561–NF564 all-oscillator analytic-to-Hermite | NEW COMPILER REPAIRS PENDING |
| NF565 exact 67 source-block order coverage | New Lean pending |
| NF565 original 67 positive + true negative 68 ledger | New Lean pending |
| NF565 generic finite distinct root budget theorem | New Lean pending |
| NF565 source-specific 67 squared-root multiplicity theorem | New Lean pending |
| Unconditional original real/complex J242 independence | OPEN |
| Unconditional canonical original Gram strictly positive | OPEN |
| Original correction real-data conjugation equivariance | OPEN |
| NF528 full original all-divisor source graph | OPEN |
| NF527 full gamma+prime n=9/both pole 1/10 coercivity | OPEN |
| NF539 signed Weil source identity | OPEN |
| W_ODD_NEG / RH | OPEN |

## 7. NF566 target

Obtain actual focused compiler feedback on the new NF565 source-indexed oscillator/root theorem, generic finite-root theorem and true 68-node list; fix any exact Lean diagnostics. Once all are accepted, explicitly instantiate the finite weighted-root budget with the ORIGINAL unique 68 nodes and 241+1 multiplicities to force the original real odd-jet left kernel to vanish. Then prove the real-square rank/complex generator independence transfer and remove the original NF550 Gram strictness hypothesis after that source branch has compiled. Preserve the exact original NF407 SHA signatures; do not detour into sampled or numerical Grammian approximations.
