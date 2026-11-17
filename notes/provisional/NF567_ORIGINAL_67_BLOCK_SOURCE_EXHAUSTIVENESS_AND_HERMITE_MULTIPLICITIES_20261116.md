# NF567 — ORIGINAL 67-block exhaustive source-index certificate and complete squared-frequency Hermite root obligations

**2026-11-16 PT. Draft stacked on NF566 PR #598.** New original-source Lean mathematics and focused CI committed. NF567 Lean verification **PENDING**. Complete source independence, unconditional canonical Gram strict positivity, signed Weil certificate, W_ODD_NEG and RH **OPEN**.

## 1. Newly confirmed source-specific compiler acceptance

The NF565 original frequency-side algebraic polynomial job, run `44002413454`, job `133769466691`, now **LEAN PASS**. It includes the exact NF557 original 242-row signed polynomial, coefficient injectivity, and the actual NF565 frequency polynomial `F_a(Z)=Z*p_a(Z²)` with its full formal `k` derivative coefficient expansion. This is an actual compiler acceptance result, not just the older symbolic coefficient replay.

The NF565 exact original all-entry source custody job `133769466750` **PASS** as well. The audit includes all 58,564 original symbolic oscillator and sinh-pole odd-jet coefficients and is independent of the actual oscillator higher-derivative Lean proof.

The NF565 analytic oscillator job `133769466310` **FAILED** at two remaining function-valued constant evaluations `((-1)^n) 0` after Mathlib's real iterated sine/cosine derivatives. NF566 patched these using `Pi.pow_apply`, `Pi.neg_apply`, `Pi.one_apply`; its compilation is not yet accepted. The NF565 physical NF550 weighted-square Gram job `133769466884` **FAILED** with genuine a.e. sum-coercion and real/complex integral-cast problems, addressed by NF566 source edits; new compiler result still pending.

Previously accepted exact source chain:
- NF542–NF549 genuine physical J242 source synthesis and continuous canonical Gram integral: **LEAN PASS**.
- NF553–NF556 generic polynomial degree and Hermite multiplicity plus exact quadratic root-transfer machinery: **LEAN PASS**.
- NF557–NF560 authentic original 242 signed source polynomial, 67 positive rational nodes, coefficient injectivity, actual `sinh(x/2)` odd analytic derivatives, and true `242×242` odd-jet matrix pole root: **LEAN PASS** in NF562 source pole job `133692558469`.
- NF565 genuine 242-coefficient frequency-side polynomial and all formal derivatives: **NEW LEAN PASS** at job `133769466691`.
- NF566 original signed source coefficient sum / 241 real analytic oscillator-to-Hermite transfer: **SOURCE IMPLEMENTED; CI PENDING**.
- NF550 actual original physical weighted-square equality and NF551 dependent analytic identity: **COMPILER OPEN**.

## 2. Missing exact arithmetic-source property now formalized

The original NF545 table has **67** genuinely distinct positive rational frequencies `f_g`, each with a strictly positive multiplicity `m_g`; the original table gives

```
Σ_(g:Fin67) m_g = 241.
```

The literal NF545 flattened source is

```
originalNodes = originalFrequencyGroups.flatMap
  (fun group => (List.range group.2).map (fun k => (group.1,k))).
```

The missing *surjectivity onto every source order* was not merely a cardinality statement. It needed to be proved that for **every** original group index `g : Fin67` and **every** `k < m_g`, there is a literal original oscillator index `i : Fin241` satisfying

```
nf545OriginalOscillatorNodeAt i = (f_g,k).
```

NF567 now proves this as a **Lean candidate** using the genuine original `List.flatMap`/\`List.range\`/\`List.mem_iff_get\` construction. No invented groups, resampled frequencies, or independent interpolating basis enter.

This exact source-index certificate is isolated into

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242Actual67BlockCoverage.lean
```

which imports only NF545 original source tables, NF553 accepted generic node-separation mathematics, and Mathlib. Its focused CI job is therefore **independent of the still pending NF566 analytic oscillator differentiation proofs**.

Additional new original data theorems in the same independent module:
- the 67 actual source group multiplicities are all positive;
- their exact sum is 241;
- the exact rational frequencies are injective on `Fin67` (from NF545's already accepted `Nodup` theorem);
- true angular frequencies `ω_g = 2πf_g` are positive and injective;
- true real squared nodes `ω_g²` are positive and injective (via NF553);
- no `ω_g²` collides with the genuine sinh node `-1/4`.

All new Lean proofs remain **PENDING** despite the unchanged frozen source data being independently audited.

## 3. Full ORIGINAL 67-block Hermite derivative conditions

The second new module imports both independent original block coverage and NF566's source-specific analytic odd-jet derivative bridge:

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242Actual67BlockHermiteCompleteness.lean
```

It proves the following **candidate** chain.

For a real original 242-row coefficient vector `a` satisfying all 241 actual oscillator odd-jet column equations,

```
∀ i : Fin241,
   (D_polynomial^(k_i) F_a)(2π f_i) = 0,
```

the source-index completeness theorem guarantees, **for every group `g : Fin67`**, the entire original range:

```
∀ k < m_g,
   (D_polynomial^k F_a)(ω_g) = 0.
```

If `F_a≠0`, the independently Lean-accepted NF554 Hermite theorem yields

```
∀ g : Fin67,
  m_g ≤ rootMultiplicity(ω_g,F_a).
```

If additionally `p_a≠0`, the already-accepted NF556 quadratic-transfer theorem, combined with the **newly compiler-accepted NF565 identity `F_a(X)=X*p_a(X²)`**, yields

```
∀ g : Fin67,
  m_g ≤ rootMultiplicity(ω_g²,p_a).
```

The actual NF560 pole identity gives the other required node:

```
p_a(-1/4)=0.
```

NF567 packs this conclusion as `neutralNF567OriginalFull242Kernel_squaredDualRootMultiplicities`: **given the exact literal 242×242 original real analytic odd-derivative matrix left-kernel equations** plus the explicit nonzero `p_a`, `F_a` hypotheses, every one of the 67 authentic positive squared source nodes has its intended `m_g` multiplicity and the genuine negative sinh node is a root. There is NO new matrix or source independence premise. The proof's actual source-analytic NF566 dependency has not yet compiled.

## 4. What NF567 DOES NOT yet prove

A set of individual multiplicity inequalities is *not* automatically the global polynomial degree contradiction. The final algebra must construct (or otherwise certify) a single simultaneous 68-node root budget:

```
Σ_(g:Fin67) m_g + 1 = 241 + 1 = 242
```

with all **68 distinct real nodes** `ω_g²` and `-1/4`. Then use `Polynomial.roots`/\`rootMultiplicity\` or product divisibility to show any nonzero `p_a` must have `natDegree p_a ≥242`, contradicting NF557's accepted `natDegree p_a<242`.

**Two distinct nonzero gates remain**: the proof uses `p_a≠0` and `F_a≠0` explicitly. The implication `p_a≠0 ⇒ F_a≠0` is mathematically true because `F_a=X*p_a(X²)`, but still needs a Lean proof. Neither nonzero fact is declared as an unconditional conclusion from a source left kernel.

Then NF558 original coefficient injectivity would give `a=0`; the resulting real finite odd-jet square matrix invertibility plus a real/imaginary decomposition could prove global independence of the exact 242 complex original functions. Genuine NF550 and NF551 must also compile to infer unconditional strictly positive canonical weighted Gram, and the correction reality/equivariance constraint remains separate.

No RH result is inferred. The outstanding independent arithmetic and analytic components — NF528 full positive/negative divisor source graph convergence, NF527 complete 1/10 gamma+prime n9 and both pole coercivity, NF539 signed Weil source equality, W_ODD_NEG and RH — remain **OPEN**.

## 5. Verification plan and NF568

New pinned `.github/workflows/nf567-original-67-block-hermite-completeness.yml` independently tests:

1. **Standalone immutable original 67-block coverage, positive frequencies, squared-frequency injectivity and true negative pole separation** from NF545/NF553. Does not import pending NF566.
2. **Complete source-dependent actual analytic original 242 odd-jet matrix left kernel → full 67-block formal Hermite derivatives → 67 positive squared `p_a` root multiplicity bounds + true sinh-pole negative root**, via NF565/NF566 and the accepted NF554/NF556.
3. Original NF549→NF550 physical weighted-square and NF551 analytic local-global source compiler.
4. Full exact SHA-pinned original all-entry odd-jet source replay.

All NF567 new Lean/compiler jobs remain **PENDING**. No `axiom`, `sorry` or `admit` inserted.

**NF568 priority:** consume actual NF566/NF567 CI compiler diagnostics; get independent original block-coverage job to LEAN PASS and repair its source-index transport if needed; then discharge the algebraic `p_a≠0 ⇒ F_a≠0` fact and the **simultaneous 68-node 242-multiplicity root-budget degree contradiction**. Do not claim finite source independence until the genuine analytic dependencies and terminal polynomial contradiction both pass Lean.
