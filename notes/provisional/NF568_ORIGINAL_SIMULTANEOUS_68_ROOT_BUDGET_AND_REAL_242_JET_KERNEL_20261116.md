# NF568 — Simultaneous ORIGINAL 68-node root-count contradiction and terminal real 242 analytic odd-jet left kernel

**November 16, 2026 PT (GitHub CI timestamps may be November 17 UTC). Draft stacked on NF567 PR #599. New proof implementations and focused CI COMMITTED, NOT YET LEAN-ACCEPTED.**

## 1. First genuinely accepted NF565 algebraic component

NF565 workflow run `44002413454`, job `133769466691`, **SUCCESS**: the original 242-coefficient real signed dual `p_a(T)=Σ_n(-1)^n a_n T^n`, and the true frequency polynomial `F_a(X)=X p_a(X²)=Σ_n(-1)^n a_n X^(2n+1)`, have a compiler-accepted identity and complete formal higher-derivative expansion. Exact 58,564-entry NF407-source odd-jet custody **PASS** (job `133769466750`).

Already confirmed in earlier source-chain CI: NF557–NF560 original real 242-coefficient dual, signed polynomial injectivity, true analytic sinh(x/2) pole and actual 242×242 odd-jet matrix pole column; generic NF553–NF556 polynomial degree/Hermite multiplicity/quadratic source-node transfer; genuine NF542–NF549 physical J242 source integral, all **LEAN PASS**.

The current **NF566/NF567 oscillator real analytic-to-Hermite bridge CI and independently compiled 67-block source index coverage jobs are still QUEUED** at the most recent check. NF550 original weighted-square Gram and NF551 downstream analytic identity remain COMPILER OPEN. A symbolic 58,564 odd-jet coefficient replay PASS is not a substitute for the actual iteratedDeriv Lean proofs.

## 2. The formerly missing SIMULTANEOUS root-count obstruction (new algebraic proof implementation)

NF567 source-specific theorems provide exact rational group multiplicities `m_g>0`, group count 67, `Σ_(g:Fin67) m_g = 241`, genuine real positive squared-frequency nodes `t_g=(2πf_g)^2`, distinctness of the t_g, and separation from the true negative sinh-pole node `t_*=-1/4`. Their proofs are committed, pending compiler acceptance.

NF568 implements the key **single simultaneous root-budget lemma**, independently of the pending NF566 analytic source function formalization:

```
neutralNF568Distinct67PlusPole_rootCountBound
```

For arbitrary nonzero real polynomial p, injectively indexed nodes `t_g`, a separate pole `t_*`, positive integer weights `m_g`, and actual root-multiplicity lower bounds

```
∀g:Fin67, m_g ≤ rootMultiplicity(t_g,p),
eval(t_*,p)=0,
```

the theorem proves

```
(Σ_g m_g)+1 ≤ natDegree(p).
```

**Crucial non-double-counting step:** Rather than merely adding 67 local multiplicity bounds, it constructs the finite set `s=univ.image nodes`, establishes the pole is NOT in s, and proves `insert pole s ⊆ p.roots.toFinset`. The proof uses:

- actual `Polynomial.count_roots` and `Multiset.count_pos` for the positive multiplicity constraints;
- `Finset.sum_image` with explicit source-node injectivity;
- `Finset.sum_insert` with the separately proven negative node not in s;
- `Finset.sum_le_sum_of_subset_of_nonneg` to compare source-root counts to the *entire* roots multiset;
- `Multiset.toFinset_sum_count_eq` and `Polynomial.card_roots' p` for the rigorous bound `card(p.roots) ≤ natDegree(p)`.

Therefore **without assuming polynomial splittings over ℝ**, it supplies the terminal global root-count certificate needed to make the original NF553 degree obstruction apply.

The exact source instantiation is

```
neutralNF568Original68NodeMultiplicityForcesPolynomialZero :
 (natDegree(p)<242) →
 (∀g, m_g≤rootMultiplicity(t_g,p)) →
 (eval(-1/4,p)=0) →
 p=0
```

because `Σ_g m_g+1=242`. A further theorem applies it to the literal NF557 242-dimensional original polynomial p_a with its already-accepted `natDegree(p_a)<242`:

```
neutralNF568OriginalDual68Roots_forcesZero.
```

**These are Lean proof implementations, not yet independently compiler-accepted.**

The general, source-independent multiset theorem was isolated in `WeilDefect/Arithmetic/ActualZetaOriginalJ242Generic67PlusPoleRootCount.lean`. The *actual NF407* 67 positive-square plus true sinh-pole specialization and 242-degree contradiction are in `WeilDefect/Arithmetic/ActualZetaOriginalJ242Original68RootBudget.lean`. The standalone generic theorem is compiled first so a later source-index elaboration error cannot obscure its result.

## 3. Remove the outstanding hidden nonzero hypothesis

NF567's original squared-node multiplicity transfer explicitly needed both `p_a≠0` and `F_a≠0`. NF568 proves the missing implication as a **standalone algebraic module** importing only the ALREADY accepted NF565 frequency-polynomial identity:

```
neutralNF568OriginalFrequencyHermite_ne_zero :
 p_a≠0 → F_a≠0.
```

A more general exact real-polynomial theorem proves

```
p≠0 → X*p.comp(X²)≠0.
```

It uses Mathlib `Polynomial.comp_eq_zero_iff`, the nonconstant nature of `X²` from its degree 2 vs a constant's degree 0, and `Polynomial.X_ne_zero`. It is not an interpolation assumption or a numerical surrogate.

File: `WeilDefect/Arithmetic/ActualZetaOriginalJ242FrequencyNonzero.lean`. NF568's independent algebraic CI job will compile this separately from the still-unaccepted actual oscillator differentiated functions.

## 4. Full original real 242×242 analytic odd-jet left-kernel theorem (new source-dependent proof candidate)

The **source-dependent** terminal file

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242ActualOddJetKernelClosure.lean
```

implements the logically complete argument for the *literal true analytic NF560 original matrix*

```
A_(n,j)=D_x^(2n+1)[nf545OriginalSelectedRealGenerator j](0)
```

with all 241 frozen actual sine/cosine-monomial generators and the genuine index-241 `sinh(x/2)`:

```
neutralNF568OriginalActual242OddJetMatrix_leftKernel_zero :
 ∀a:Fin242→ℝ,
   (∀j:Fin242, ∑_(n:Fin242) a_n A_(n,j)=0) →
   a=0.
```

The proof does NOT assume that p_a≠0 unconditionally. Instead, suppose `p_a≠0`. The independent new nonzero theorem forces `F_a≠0`; the NF566 true analytic source-to-Hermite and NF567 full 67-block-index completeness transfer, if compiler accepted, then supply the authentic 67 squared-node multiplicity bounds plus the true sinh pole. NF568's genuine simultaneous 68-node root-count theorem forces `p_a=0`, contradiction. Finally the compiler-accepted NF558 true original coefficient injectivity gives `a=0`.

A second theorem derives injectivity of the real finite left-kernel linear action `a ↦ (j ↦ Σ_n a_n A_(n,j))`.

**This is a complete candidate SOURCE-SPECIFIC mathematical argument; it is not yet a Lean-certified theorem.** It inherits all actual NF566/NF567 analytic derivative proof compiler obligations. The bounded-degree arithmetic is now implemented rather than merely outlined, but its correctness as Lean code remains CI PENDING.

## 5. Specific verification/branch boundary

New pinned workflow `.github/workflows/nf568-original-68-roots-and-real-kernel.yml` separates:

1. **Independent algebraic root budget**: first compile the completely generic 67+pole root multiset count (Mathlib-only), then NF567 frozen source block coverage, then the original p_a≠0⇒F_a≠0 lemma and the genuine NF407 68-node 242-degree contradiction. None imports pending NF566 analytic-source proof code.
2. **Full real analytic original matrix left kernel**: the already accepted NF565 frequency polynomial, genuine analytic sinh source, NF566 authentic all-241 oscillators and 242×242 kernel conditions, NF567 group multiplicity transport, and the new NF568 terminal real kernel.
3. **Independent original physical NF549→NF550 weighted-square and NF551 downstream**: still compiler-open, no positivity claim.
4. **Exact SHA-pinned immutable source custody**: all 58,564 original NF407/NF500 symbolic source coefficients.

No new `axiom`, `sorry` or `admit` is introduced in the NF568 modules.

## 6. Remaining after NF568

**Compiler recovery is the critical gate.** Even a correct root-count theorem with pending Lean dependencies cannot be called an accepted source-independence proof.

When the algebraic root-budget and original analytic source kernel both pass, the next step is to prove that trivial left kernel of the genuine real **square 242×242** odd-jet matrix implies its right-kernel triviality (finite-dimensional invertibility), and to show differentiation of any zero original real/complex global generator combination yields such a right-kernel vector. Then recover complete original 242-generator global independence and insert it into the actual compiled NF550 weighted-square and NF551 collar uniqueness bridge for unconditional canonical weighted Gram strict positivity.

The original NF528 full source all-divisor graph convergence, NF527 gamma+prime n9+both poles 1/10 coercivity, NF539 signed Weil source equality, W_ODD_NEG, original real-data correction conjugation-equivariance and RH remain **OPEN**.

**NF569:** consume actual NF568 independent and source-dependent Lean diagnostics and prioritize compiler acceptance; then square matrix right kernel and original complex real/imaginary analytic independence. Avoid transferring this finite source theorem to the RH-facing full correction until the actual graph and 1/10 coercivity gates are independently discharged.
