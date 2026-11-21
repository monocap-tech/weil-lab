# Weil-Lab — IV016
## Close frozen original two-collar finite logarithmic gap in Lean, and isolate the genuine new diagonal pole/Gamma remainder

**Canonical independent Phase IV head:** IV016. Stacked on IV015 PR #783, IV014 #781, IV013 #779, IV012 #778, IV011 #774, IV010 #773, IV009 #771, IV008 #769, IV007 #767, IV006 #766. Not the independent NF### Phase III numerical enclosure track.

**Formal standing:** TEN NEW original-source Lean theorem **CANDIDATES** and FOUR original upstream source axiom audits. Direct pinned Lean + Mathlib kernel build / strict standard-axiom verification is **PENDING** until GitHub Actions reports successful actual compilation and publishes the source-bound artifact. Source existence and independent exact-rational Python preflight alone are not proof.

### 1. What specifically changes relative to IV015?

IV015 established a genuine nonzero complex C∞ compactly supported Schwartz bump construction using Mathlib and the actual frozen original NF543 two-collar source class

    E_original = Ioo(-11/10, -11/10+1/500)
                ∪ Ioo(11/10-1/500, 11/10).

For a proposed new bump centered at c=1/5, r=1/1000, with original physical window b=11/10 and prime cutoff N=10, IV015 verified all relevant shifted support inequalities independently by exact rational series arithmetic. **But it retained a finite numerical gap PROP as an explicit Lean premise**, namely

    neutralIV015FrozenTwoCollarActiveGap (1/5) (1/1000) 10.

IV016 removes precisely that explicit finite side hypothesis in a NEW Lean theorem by showing the real inequalities directly, using Mathlib's independently proved exact `Real.log` bounds. The source has no `sorry`, oracle, local `axiom` or trust of a Python-produced witness. Only a real kernel/axiom PASS can certify it.

### 2. The rigorous logarithmic band proof

The four original finite physical support translations involve the old collar centers

    cL = -1099/1000, cR = 1099/1000,

the new center c=1/5, and exact clearance δ+r=1/500.

The four true inequalities are

    1/500 < |1299/1000 − log n|,
    1/500 < |−899/1000 − log n|,
    1/500 < |1299/1000 + log n|,
    1/500 < |−899/1000 + log n|.

These are required for every original integer 0≤n<10 — **stronger** than limiting to original von Mangoldt-active n. No fake prime-power classification is needed to settle this finite leaf.

The new core theorem `neutralIV016FrozenLogBand_lt10` uses exact provable four-way cases:

    log n ≤ 7/10                         (n=0,1,2)
    109/100 ≤ log n ≤ 11/10             (n=3)
    138/100 ≤ log n ≤ 14/10             (n=4)
    16/10 ≤ log n                      (n=5,...,9).

The boundary estimates come from the *real* standard Mathlib lemmas `Real.log_two_gt_d9`, `Real.log_two_lt_d9`, `Real.log_three_gt_d9`, `Real.log_three_lt_d9`, `Real.log_four_eq`, `Real.log_five_gt_d9`, plus `Real.log_le_log` for n≥5, and the correct `log 0=log 1=0` cases.

Another small source lemma `neutralIV016NatLog_nonnegative` treats the full natural input including n=0. An elementary strict absolute-value clearance lemma converts each rational band into ALL four actual positive frozen-interval exclusion margins, without floating-point arithmetic. The final theorem

    neutralIV016FrozenConcrete_allIntegerGap

is the direct Lean target establishing the formerly missing IV015 arithmetic condition. Its verification is the decisive **kernel check** for this stage.

The separate original infinite prime cutoff n≥10 was already a dedicated IV015 Lean theorem candidate `neutralIV015FrozenConcrete_logCutoff`, using the rigorous source equality `log 10=log 2+log 5`.

### 3. Unconditional-on-the-gap nonzero original Schwartz bump

Given only the authentic old finite complex Schwartz family s, old coefficients u, and the ORIGINAL strict two-collar support condition on every s(i), the new theorem candidate

    neutralIV016FrozenConcrete_originalPrimeFreeBump

constructs a t with

    t(1/5)=1,
    support(t) ⊆ [-11/10,11/10],
    t not in original NF543 collar-supported class,
    t ≠ Σ_i u_i•s_i,
    P_original(Σ_i u_i•s_i, t)=0,
    W_original(Σ_i u_i•s_i, t)
      = originalPole(Σ_i u_i•s_i,t)
        + originalGamma(Σ_i u_i•s_i,t).

The finite **log gap no longer appears in this target's hypothesis**; it is proved internally by the preceding actual real-log theorem candidate.

This is a nonzero physical function statement for the true original zeta mixed arithmetic Weil expression, not an abstract PSD criterion. Even after successful Lean acceptance it does not prove any positivity.

### 4. NEW mathematical result: the chosen bump's OWN prime diagonal vanishes too

The small bump's support diameter is just

    2r = 1/500 = 0.002.

For each original nonzero von Mangoldt index m, Mathlib's actual
`ArithmeticFunction.vonMangoldt_ne_zero_iff` gives that m is a prime power and hence m≥2. Rigorous original real logarithm monotonicity and the Mathlib bound

    log 2 > 0.6931471803 > 0.002

then guarantee the original t–t correlation vanishes at **both ±log m** for every arithmetic-active m below the source cutoff N=10. The IV011 exact support cutoff annihilates all higher m.

Thus IV016 adds the genuine new *self-pairing* theorem target

    P_original(t,t) = 0,

and, by the COMPLETE UNCHANGED literal signed original zeta EF,

    D = W_original(t,t)
      = originalPole(t,t) + originalGamma(t,t).

The full mixed source identity for old finite S and selected t is simultaneously

    W_original(S,t)
      = originalPole(S,t) + originalGamma(S,t).

This distinction matters: IV015 established only the MIXED old/new prime-free relation. IV016 extends that exact prime elimination to the NEW DIAGONAL, a different authentic source interaction. No original von Mangoldt coefficient, pole residue or Gamma bracket is dropped from the overall EF; their prime terms individually vanish by real physical support geometry.

### 5. A single source existence theorem with both exact identities

`neutralIV016ExistsConcretePrimeFreeMixedAndDiagonal` is the final original-source Lean proof candidate:

For any finite old complex Schwartz family supported within the **real historical two collars** and any old coefficient vector, there exists a NONZERO new complex Schwartz test t such that:

- `t(1/5)=1`, while every old collar finite combination vanishes at 1/5;
- t genuinely lies outside the original two-collar test class and old finite span;
- original mixed von Mangoldt prime term is EXACTLY zero;
- original new diagonal von Mangoldt prime term is EXACTLY zero;
- both the real original mixed Weil value and the real original new diagonal are EXACTLY their original two-pole-plus-Gamma residues.

**This does not assert that the new diagonal is positive.** The pole+Gamma remainder's sign, size and interaction with the old source are still genuine open analytic inequalities. Prime-free original diagonal alone is not global Weil positivity.

### 6. What is and is not validated

**Already independently exact arithmetic verified in IV015:** c=1/5, r=1/1000, true original collars ±1099/1000 width1/500; all four translated interval inequalities for all integers 0≤n<10; min clearance approximately 0.08529436; n=10 cutoff clearance approximately 0.10258509. The checker uses exact `Fraction` arithmetic and rigorous positive log-series tail enclosure, not floating point.

**NEW IV016 Lean proof targets:** direct entire finite `Real.log` gap without arithmetic premise; genuine source nonzero bump with mixed prime zero; nonzero bump's own original prime diagonal zero; true EF pole+Gamma identity for both mixed and diagonal. Kernel verification is still pending.

**Still OPEN:** sign of `Re(originalPole(t,t)+originalGamma(t,t))`; the full original mixed Schur bound `|W(S,t)|²≤A D`; uniform positivity on an entire expanded support class; original Phase III complete numerical enclosure; global Weil criterion and RH.

A new bump witness at an already existing **coarse window radius 11/10** enlarges the actual TWO-COLLAR test class, but is not yet an enlargement to arbitrary radius and does not by itself produce a full global Weil condition. No positivity inference is licensed just because original prime terms vanish for the selected pair.

### 7. Direct formal audit

New Lean module:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean`.

Ten new actual original-source theorem targets:

1. `neutralIV016FrozenLogBand_lt10`
2. `neutralIV016NatLog_nonnegative`
3. `neutralIV016AbsClearance`
4. `neutralIV016FrozenFourSignedGaps_of_band`
5. `neutralIV016FrozenConcrete_allIntegerGap`
6. `neutralIV016FrozenConcrete_originalPrimeFreeBump`
7. `neutralIV016FrozenSelfLogClearance`
8. `neutralIV016FrozenSelfActiveGap`
9. `neutralIV016FrozenSmallBump_selfPrime_zero`
10. `neutralIV016ExistsConcretePrimeFreeMixedAndDiagonal`

Plus FOUR strict upstream source `#print axioms` anchors.

Strict auditor:
`scripts/iv016_original_concrete_log_gap_kernel_audit.py`.

Independent workflow:
`.github/workflows/iv016-original-concrete-gap-primefree-diagonal.yml`.

This directly compiles the ORIGINAL Lean module, requires a source-bound real `.olean`, verifies all 14 `#print axioms` receipts with only `propext`, `Classical.choice`, `Quot.sound`, rejects `sorryAx`, binds source + original true dependencies + compiled object by SHA-256. The separate IV015 exact-rational checker remains cross-validation only, not proof promotion.

### 8. IV017 frontier

When IV016's real direct Lean compilation is accepted:

1. Examine the **authentic two-pole moments** of the selected nonzero real-positive physical bump, including whether its pole contribution has positive real sign and how sharply it can be bounded relative to its actual L² mass.
2. Analyze the real original Gamma/digamma diagonal residual for that SAME selected Schwartz bump, with rigorous weighted-frequency lower bounds, rather than an absolute majorant that destroys sign.
3. For any old finite physical two-collar combination S, bound the remaining true pole/Gamma mixed cross interaction against old coercivity A and new diagonal D. This is the untouched sharp Schur question.
4. Verify full original two-collar prior IV009–IV015 upstream Lean source/audit completion separately. Never promote a queued source file to kernel PASS or use independently exact Fraction intervals as substitute for Lean.

**Current truth boundary:** NO new-source diagonal positivity, no new-support PSD, no global Weil positivity or RH. Phase III remains independent.
