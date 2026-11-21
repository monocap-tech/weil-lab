# Weil-Lab — IV021
## Genuine smooth Schwartz partition of EVERY supported function in the enlarged original three-cell domain

**Canonical independent Phase IV:** IV021, stacked on IV020 PR #788 → IV019 #787 → IV018 #786 → IV017 #785 → IV016 #784 → IV015 #783 → IV014 #781 → IV013 #779 → IV012 #778 → IV011 #774 → IV010 #773 → IV009 #771 → IV008 #769 → IV007 #767 → IV006 #766. **Not Phase III NF###** original numerical gate/payment production.

**IMPORTANT formal boundary:** SEVEN new actual original-complex-Schwartz Lean proof candidates and FOUR original source dependency axiom anchors, with direct pinned Lean/Mathlib kernel compilation and source SHA custody. IV021 is NOT kernel accepted at source creation. Earlier IV009 source repair run 44850887402 and IV018–IV020 full dependency-chain builds were still queued/pending at the latest check, and IV021 cannot leapfrog their real kernel results.

### 1. The exact gap in IV020: decomposition of arbitrary supported tests

IV020's main genuine original signed Weil theorem target says for any complex Schwartz test `S` supported in the TWO original historical NF543 strict collars, any complex Schwartz `t` supported in the NEW doubled-radius central interval, and every complex coefficient `v`,

    Re W_original(S+v•t, S+v•t)
       >= (1/10) Mass(S+v•t).

IV020 also builds a selected genuinely nonzero new smooth bump outside the old source class.

**However**, an arbitrary complex Schwartz `f` whose support is contained in the geometric THREE-CELL UNION had not yet been formally decomposed as `S+t`. Treating IV020 as positivity on the whole geometric support class without that lemma would be an unjustified extrapolation.

The original strict support is unchanged:

    E_old = Ioo(-11/10,-11/10+1/500)
          ∪ Ioo(11/10-1/500,11/10).

The new doubled-radius support is the TRUE closed physical interval

    E_new = Icc(99/500,101/500) = [0.198,0.202].

The entire admitted support set is

    E_3 = E_old ∪ E_new.

All three cells are disjoint and lie in the SAME original explicit-formula physical radius 11/10. Their certified prospective Lebesgue measure is 1/125. No original coefficient, pole term, gammaBracket, prime divisor or cutoff is changed.

### 2. A literal Mathlib C∞ plateau—not an unsafe characteristic-function projection

For an arbitrary Schwartz `f : 𝓢(ℝ,ℂ)` supported in E_3, the obvious formula `f·1_{E_new}` would require multiplying by the **discontinuous indicator** of an interval. A discontinuous multiplier is not Schwartz and would invalidate the proof.

Instead IV021 constructs a TRUE smooth bump

    β : ContDiffBump (1/5 : ℝ),

with EXACT rational radii

    rIn = 1/20 = 0.05,
    rOut = 1/10 = 0.1.

The central interval [0.198,0.202] is STRICTLY within the inner plateau |x−0.2| ≤ 0.05. Both original historical collar intervals near ±1.099 are STRICTLY beyond the outer support ball |x−0.2| <0.1.

Mathlib's genuine `ContDiffBump.one_of_mem_closedBall` and `zero_of_le_dist` therefore give pointwise:

    β(x)=1   for EVERY x ∈ E_new,
    β(x)=0   for EVERY x ∈ E_old.

These are real physical coordinate equalities for entire intervals, not isolated sample points or finite matrix vectors.

The independent exact `fractions.Fraction` preflight verifies:
- E_new maximum center distance 1/500 is LESS than the plateau radius 1/20;
- nearest old-collar distance from 1/5 is 449/500, GREATER than support radius 1/10;
- the three-cell measure remains 1/125;
- counterfactual undersized plateau and oversized support radii are correctly rejected.

The independent script is a geometric source consistency check, NOT a proof that the corresponding Lean theorem compiled.

### 3. This multiplier REALLY preserves the complex Schwartz class

Mathlib already proves

    HasCompactSupport.hasTemperateGrowth

for a compactly supported C∞ real bump. IV021 attaches the actual `β.hasCompactSupport` and `β.contDiff` facts and constructs the Schwartz endomorphism with

    SchwartzMap.smulLeftCLM ℂ (fun x : ℝ => β x).

This is a genuine CONTINUOUS ℝ-linear scalar multiplication map on Schwartz space, acting on complex-valued functions, and not a data-level placeholder.

The new-cell component of `f` is defined as an actual Schwartz function

    t = neutralIV021NewCellPart f = β·f.

The old-cell component is another actual complex Schwartz function

    S = neutralIV021OldCellPart f = f−t.

Pointwise support:

- If x ∈ E_old, β(x)=0, hence t(x)=0.
- If x ∈ E_new, β(x)=1, hence S(x)=0.
- If x lies outside E_3, f(x)=0, and both S(x) and t(x) vanish.

Therefore

    neutralNF735InOriginalCollars S,

    t(x)=0 for x∉E_new,

    f=S+t.

No finite old coefficient expansion is needed and no Hilbert-space matrix representation is inserted. This is the actual original complex Schwartz function space.

**NEW MAIN decomposition theorem target:**

    neutralIV021EveryThreeCellSchwartz_decomposes.

This is a support-class statement on *all* physically admissible Schwartz tests in E_3, not just old finite combinations.

### 4. The complete original arithmetic prime dictionary extends automatically

Once the genuine decomposition f=S+t is established, IV020's actual original arithmetic transfer becomes available with coefficient `v=1`:

    P_original(f,f)=P_original(S,S).

This preserves the HISTORICAL NF600 n=9 old-old correlation term. It does not assert that the entire new support has zero primes; only the old-new, new-old and new-new translated products are zero at each authentic von-Mangoldt-active original prime-power frequency, and n≥10 is controlled by the original real log cutoff.

The resulting IV021 proof candidate is

    neutralIV021EveryThreeCell_originalPrime_eq_old.

It is an exact equality for EVERY complex Schwartz f supported in E_3, without requiring the original finite row coordinate representation. This is the source-level physical relationship needed for a future cross-projection dictionary: the original arithmetic prime functional depends on the OLD source component, while the C∞ cutoff choice is simply a constructive means to identify that component.

**Do not infer arithmetic/spectral equivalence from this statement.** It is a dictionary inside the same original signed-zeta physical support model, not an independent spectral realization.

### 5. The entire geometric three-cell restricted Weil positivity theorem target

IV020's original signed lower bound, applied to the genuine decomposition of arbitrary f, yields the IV021 theorem candidate

    neutralIV021WholeThreeCellOriginalWeil_oneTenth:

    for EVERY f:𝓢(ℝ,ℂ),
      (∀x, x∉E_3 → f(x)=0) →
      (1/10)*Mass(f) <= Re W_original(f,f).

This is stronger than IV020's literal direct-sum form: the actual input is an ARBITRARY Schwartz f supported on the entire E_3, not a selected new bump or an old finite index family.

The prior source estimates underlying that candidate remain fully authentic:

    Mass(f)=‖f.toLp 2 volume‖²;
    volume(E_3)=1/125;
    LowMass(f)≤2/25 Mass(f);
    Arch(f)≥141/250 Mass(f);
    both original poles cost≤8/125 Mass(f);
    original n9 old prime cost≤2/5 Mass(f).

Their exact arithmetic difference is

    141/250 − 8/125 − 2/5 = 1/10.

The final IV021 theorem is not a global Weil criterion: E_3 is a small fixed bounded union of three specific physical support cells inside the original window, not all compactly supported Schwartz functions or the global admissible Weil test space.

### 6. Intrinsic versus auxiliary choices

The chosen cutoff β and its radii 1/20 and 1/10 are AUXILIARY proof coordinates: different smooth cutoffs agreeing on E_old/E_new would produce the same physical S and t on a function supported in E_3, because those supports are disjoint and the source function vanishes elsewhere.

The resulting restricted original Weil positivity statement concerns every f supported in the ACTUAL geometric E_3 and is independent of a finite old row basis or selected bump shape. But its numerical margin 1/10 still comes from coarse physical-support measure and specific signed symbol bounds; it is a sufficient lower estimate, not an intrinsic best coercivity constant.

An exact equivalence with an independent arithmetic or spectral construction, or a systematic global extension law, remains a DISTINCT research question; IV021 does not assume such an equivalence.

### 7. Strict source-bound formal custody

New Lean module:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition.lean`

Seven genuine original source Lean theorem candidates:

1. `neutralIV021Cutoff_old_zero`
2. `neutralIV021Cutoff_new_one`
3. `neutralIV021Cutoff_hasTemperateGrowth`
4. `neutralIV021NewCellPart_apply`
5. `neutralIV021EveryThreeCellSchwartz_decomposes`
6. `neutralIV021EveryThreeCell_originalPrime_eq_old`
7. `neutralIV021WholeThreeCellOriginalWeil_oneTenth`

Imported originals checked by four strict `#print axioms` anchors:
- `neutralIV020WideThreeCell_volume`
- `neutralIV020WideOriginalOldPlusNew_oneTenth_coercive`
- `neutralIV020WideExpandedPrime_eq_old`
- `neutralNF600Prime_bound_actual`

Independent strict auditor:
`scripts/iv021_original_three_cell_smooth_partition_audit.py`.

Dedicated direct pinned Lean/Mathlib workflow:
`.github/workflows/iv021-original-whole-three-cell-schwartz-partition.yml`.

The workflow requires:
- a genuinely compiled ORIGINAL source .olean object;
- direct `#print axioms` receipts for ALL seven new + four original anchors, only the three standard axioms `propext`, `Classical.choice`, `Quot.sound`, zero `sorryAx`, and no compiler errors;
- SHA256 custody of the actual Lean file, historical Zeta23 and NF543/NF600 originals, every IV009–IV020 mathematical source dependency, original toolchain/manifest and real compiled .olean;
- separate exact rational cutoff plateau and exclusion receipt, which cannot be promoted to a Lean proof.

**Formal state at creation: SOURCE COMMITTED, REAL KERNEL PENDING.** Prior IV009 repair and IV018–IV020 Actions were queued/pending. The candidate theorem is NOT a Lean-accepted proof until the full dependency chain and the new audit produce terminal success.

### 8. Next — IV022

1. First retrieve the actual earliest failed original IV009–IV021 compiler module and use exact diagnostic lines to fix it; propagate accepted source repairs through the full stacked branch chain. Do not silently count a pending build.
2. Once IV021's actual whole-three-cell partition and 1/10 source positivity pass, investigate parameterized safe support intervals and prove whether the original signed source margin can be maintained under multiple added cells. Each new original ±log prime-power interaction must be accounted for, including self, pairwise new-new and old-new shifts.
3. Distinguish the coordinate-invariant restricted quadratic form from the nonsharp numerical L1/mass bound and auxiliary smooth cutoff. Formulate an external arithmetic/spectral compatibility conjecture with exact map, preservation law, and counterexample conditions, but do not claim equivalence without a separately verified construction.

Phase III original numerical gate enclosure/payment remains an independent track. Global Weil positivity and RH remain OPEN.
