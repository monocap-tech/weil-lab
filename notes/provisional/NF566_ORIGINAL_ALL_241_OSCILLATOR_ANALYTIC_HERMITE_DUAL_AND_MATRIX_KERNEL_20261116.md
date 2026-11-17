# NF566 — Complete authentic 241 oscillator-to-Hermite dual bridge implemented, with real 242×242 left-kernel and sinh pole packaged

**Date: 2026-11-16 PT. Draft stacked on NF565 PR #597. New source mathematics, exact analytic source-indexed bridge, compiler repairs and focused CI COMMITTED. Lean compiler acceptance of the NF566 statements is PENDING. No unconditional original 242-generator independence, Gram positivity, signed Weil, W_ODD_NEG or RH claim.**

## 1. Genuine original source custody and accepted pole status

The immutable NF407/NF500 source is unchanged:

- The original 67 distinct positive rational oscillator frequencies, with integer monomial multiplicities summing to **241**.
- Their 241 **true** generators: for original frequency f and order k, `x^k*sin(2π f x)` for even k and `x^k*cos(2π f x)` for odd k.
- The single genuine final generator `sinh(x/2)` at index 241.
- Exactly 242 real odd-derivative rows of orders 1,3,...,483 and 242 source columns.
- The original physical window [-11/10, 11/10] and canonical even collar cutoff inside E; neither source nor cutoff was altered.

Previously established compiler facts:

- NF542–NF549 genuine original physical source modules **LEAN PASS**, including the actual NF549 L² continuous physical Gram integral.
- NF557–NF560 genuine original 242 dual polynomial, 67 rational squared source nodes, coefficient injectivity, true sinh negative pole algebra and its analytic odd derivatives **LEAN PASS** as the complete NF562 source-pole job 133692558469 (also NF561 job 133692559874).
- NF553–NF556 generic polynomial degree and Hermite root multiplicity/positive quadratic-root transfer **LEAN PASS**.
- Original source SHA-pinned **58,564** odd-jet symbolic derivative entries PASS, repeatedly; latest NF565 source custody job 133769466750 PASS. Source audit does not by itself prove source analytic derivatives in Lean.
- NF550 genuine full weighted-square source module still FAILED most recently in NF564, and NF551 downstream compiler acceptance is not established.

## 2. New exact signed source coefficient-to-formal Hermite identity (independently compilable)

The original real odd-jet dual is the accepted finite coefficient vector `a : Fin 242 → ℝ`, with exact

```
p_a(T) = Σ_(n<242) (-1)^n a_n T^n,
F_a(Z) = Z p_a(Z²) = Σ_(n<242) (-1)^n a_n Z^(2n+1).
```

The NEW `ActualZetaOriginalJ242HermiteSignedOscillatorSum.lean` defines the *true original source-audited coefficient*, using the polynomial descending factorial:

```
C_(n,k)(freq)
 := (-1)^(n + k/2) *
       (Nat.descFactorial (2n+1) k : ℝ) *
       freq^(2n+1-k).
```

Because `Nat.descFactorial m k=0` for k>m, this gives exactly the authentic source's zero-before-monomial-order case; no division by zero and no unproved frequency positivity hypothesis are required. Mathlib's exact identity `Nat.descFactorial_eq_factorial_mul_choose` gives

```
(2n+1)_{falling k} = k! * choose(2n+1,k),
```

so it reproduces the monomial Leibniz coefficient even at k>2n+1.

The key NEW finite **242-term identity**, valid for every real frequency and every natural k, is

```
Σ_(n<242) a_n C_(n,k)(freq)
   = (-1)^(k/2) * [(D_polynomial^k F_a)(freq)].
```

This is proved by substituting the NF565 formal polynomial derivative expansion and normalizing the literal source-parity sign using `pow_add`. The sign factor is always ±1, hence invertible, so NF566 also implements the exact vanishing equivalence

```
Σ_n a_n C_(n,k)(freq)=0
   ↔ (D_polynomial^k F_a)(freq)=0.
```

A third theorem applies the already LEAN-PASSED NF554 Hermite root multiplicity machinery: for any positive integer m, if the true signed source coefficient sums vanish at orders k=0,...,m-1, then, for F_a≠0,

```
m ≤ rootMultiplicity(freq, F_a).
```

The analytic-source equality is explicitly marked as a separate premise in an additional generic transport theorem; there is **no assumption of original independence and no unguarded identification of symbolic coefficient audits with real analytic derivatives**.

## 3. Complete original 241-index analytic source to Hermite derivative bridge (new Lean candidate)

The second NEW module `ActualZetaOriginalJ242ActualOscillatorHermiteBridge.lean` imports the source-exact NF545 oscillator table and the authentic NF561/NF562 higher iterated-derivative implementation. Its two fundamental generic analytic results are:

```
[D_x^(2n+1) (x^(2r) sin(freq*x))]_(x=0)
     = C_(n,2r)(freq)
[D_x^(2n+1) (x^(2r+1) cos(freq*x))]_(x=0)
     = C_(n,2r+1)(freq).
```

They include both n≥r and n<r cases, with a precise real sign identity `(-1)^(n-r)=(-1)^(n+r)` for n≥r. They do not replace the original source functions with hypothetical polynomials.

The source-indexed theorem unfolds the ACTUAL original `nf545OriginalSelectedRealGenerator ⟨i.val,...⟩` for every i:Fin241, reads its genuine frequency `freq_i=2πf_i` and monomial degree `k_i`, splits on the source's true parity, and proves a candidate analytic equality

```
[D_x^(2n+1) j_i(x)]_(x=0) = C_(n,k_i)(freq_i).
```

Combining this real analytic source identity with the exact finite 242-term algebraic sum gives the central original-source bridge:

```
Σ_(n<242) a_n [D_x^(2n+1) j_i]_(0)
  = (-1)^(k_i/2) * (D_polynomial^(k_i) F_a)(freq_i)
```

for **all 241 original oscillators** and all 242 original odd-jet rows. Its intended mathematical content is precisely the historical original NF554 symbolic formula and not a substitute test family. Compiler acceptance of the entire genuine analytic source bridge is **PENDING** (including its inherited NF561–NF562 dependencies).

## 4. First FULL original 242×242 matrix left-kernel reduction

NF566 goes beyond the former NF563 isolated k=0 first frequency by packaging the TRUE NF560 original **analytic** 242×242 odd-jet matrix A:

```
A_(n,j) = [D_x^(2n+1) j_j(x)]_(0).
```

For any real a satisfying the *literal complete original analytic matrix left-kernel equations*

```
∀ j : Fin 242, Σ_(n<242) a_n A_(n,j)=0,
```

the new source bridge derives TWO separate precise consequences:

**Oscillators**:
```
∀ i:Fin241,
 (D_polynomial^(k_i) F_a)(freq_i)=0.
```

**Genuine sinh pole**:
```
p_a(-1/4)=0.
```

This packaged theorem `neutralNF566OriginalFullActualOddJetKernel_rootObligations` is the **first candidate Lean statement covering all 242 actual source columns at once**. It is not itself a full multiplicity or degree contradiction, and it has not yet received compiler acceptance.

## 5. Compiler recovery updates from actual NF564/NF565 diagnostics

**Original oscillator generic analytic source**: NF564 job 133766713082 FAILED on two small goals after earlier binder and Nat-cast recovery: `Real.iteratedDeriv_odd_sin` and `Real.iteratedDeriv_even_cos` expressions still contained a function-typed constant `((-1)^n) 0` after `Pi.mul_apply`. NF565 resolved the function multiplication but did not reduce `Pi.pow_apply`, `Pi.neg_apply`, `Pi.one_apply`; NF565 job 133769466310 thus FAILED with exactly these two goals, confirming all other generic NF561 goals had closed. NF566 adds those precise function-valued constant normalization steps to the true generic oscillator module. Fresh source compiler acceptance PENDING.

**NF550 original physical weighted-square**: NF564 job 133766713066 FAILED at four remaining proof-integration issues after previous repairs. There was a function-valued `Finset.sum` vs `fun x => ∑` mismatch, a 242-index basis source identity rewrite failing, and a polymorphic real-to-complex integral theorem with an unconstrained `RCLike` instance. NF566 repairs the genuine NF550 module using:

1. an explicit `funext x; simp only [Finset.sum_apply]` equality between the exact source finite sum of 242 functions and the pointwise source sum;
2. a separately typed actual `neutralNF549OriginalPhysicalSynthesis d = Σ_i d_i • J_i` L² identity followed by a direct a.e. representative equivalence;
3. the specialized `integral_complex_ofReal` followed by real part, rather than the polymorphic `integral_ofReal`.

These are **candidate compiler fixes**, not NF550 acceptance. No change to the original 242 sources, cutoff or physical Gram.

## 6. Still outstanding, with hard correctness boundary

The independent NF553–NF556 Hermite machinery is accepted; NF566 now provides candidate original source-indexed analytic identities to feed it. To prove original finite independence *unconditionally*, Lean must still establish:

1. Compiler acceptance of the complete NF565 formal F_a derivative expansion, NF566 signed algebraic 242-term sum, NF566 genuine 241 analytic oscillator correspondence and the full 242×242 matrix source-pole obligations.
2. **Original block completeness**: the literal NF545 flattened index table contains each k=0,...,m_f−1 exactly once at each of the 67 distinct original positive rational frequency groups. Source scripts audit this, but no general source-indexed Lean extraction theorem currently packages it.
3. For each of the original 67 f and m_f, combine the source-indexed original kernel equalities with accepted NF554 to force root multiplicity m_f in F_a at freq_f and NF556 to transport to p_a at freq_f². The authentic sinh pole supplies `p_a(-1/4)=0`.
4. Formalize simultaneous **68-node Hermite multiplicity**: 67 real positive distinct squared frequency nodes with multiplicities totaling 241, plus distinct negative -1/4 node multiplicity 1, hence product/divisor degree 242. NF553 then rules out any nonzero degree<242 p_a.
5. NF558 coefficient injectivity gives a=0. Prove true real 242×242 odd-jet invertibility, real and complex global original generator independence, and apply compiled NF550/NF551 local-to-global/weighted-square results to unconditional strict positive original 242 canonical Gram.

No source-independent Gram axiom or RH proof has been inserted. The full NF528 positive and negative all-divisor graph source convergence, NF527 original full gamma+prime n9 both poles 1/10 coercivity, NF539 signed Weil identity, real-data correction conjugation equivariance, W_ODD_NEG and RH remain OPEN.

## 7. New NF566 verification and NF567

`.github/workflows/nf566-original-analytic-hermite-source-bridge.yml` has four independent jobs: (1) the exact original signed 242-coefficient Hermite algebra/multiplicity (no pending analytic source import), (2) all 241 actual oscillator higher derivatives + exact dual bridge and first original positive-root cross-check, (3) genuine NF549→NF550 original physical weighted square and NF551 parity/local-to-global continuation, and (4) SHA-pinned exact original all-entry 58,564 source custody. No new `axiom`, `sorry`, or `admit` introduced.

**NF567**: inspect NF566 compiler logs and close exact errors; then prove original flattened 67-source block completeness and simultaneous 68 distinct-root multiplicity divisor/degree obstruction for the now source-linked dual `p_a`. Only after source-global independence is compiled can strict original Gram positivity be made unconditional. Treat source analytics/compiler and RH-facing analytic/arithmetic obligations separately.
