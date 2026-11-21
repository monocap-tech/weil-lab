# Weil-Lab — IV023
## Every original four-cell Schwartz test: smooth three-component partition, complete von Mangoldt prime preservation, candidate signed one-sixteenth coercivity

**Canonical independent Phase IV:** IV023. Stacked on IV022 PR #800 → IV021 #794 → IV020 #788 → IV019 #787 → IV018 #786 → IV017 #785 → IV016 #784 → IV015 #783 → IV014 #781 → IV013 #779 → IV012 #778 → IV011 #774 → IV010 #773 → IV009 #771 → IV008 #769 → IV007 #767 → IV006 #766. **This work is separate from ongoing Phase III NF### exact original numerical source certification and from the parallel cross-projection hypothesis inquiry.**

**Current proof status:** TWO genuine original-source Lean modules, **18 new theorem PROOF CANDIDATES plus eight strictly audited original upstream anchors**, dedicated pinned two-module Lean/Mathlib workflow and independent exact-Fraction geometry/negative controls. NO IV023 terminal successful Lean kernel .olean/strict axiom artifact was available at source creation. The source does not use `sorry` or new `axiom` declarations, but that is not compiler acceptance. At kickoff all checked IV009 / IV018–IV022 real Actions runs were still queued/pending. A source-only geometric calculation MUST NOT be promoted to a verified original Weil theorem.

## 1. Exact original physical four-cell setting

The historical NF543 ORIGINAL source is the unmodified pair of strict width-1/500 collars:

    E_old =
      Ioo(-11/10,-11/10+1/500)
      ∪ Ioo(11/10-1/500,11/10).

The first added interval is

    E_plus = [99/500,101/500]
           = [0.198,0.202].

The second truly new narrow physical interval is

    E_minus = [-1/5-1/4000,-1/5+1/4000]
            = [-801/4000,-799/4000]
            = [-0.20025,-0.19975].

The complete restricted source is

    E_4 = E_old ∪ E_plus ∪ E_minus.

All four cells lie in the SAME original physical explicit-formula window [-11/10,11/10]; the old collars are NOT enlarged or relocated. IV022 calculates the exact Lebesgue mass budget

    Leb(E_4) = 1/250+1/250+1/2000 = 17/2000.

The arithmetic test is the unmodified ORIGINAL signed zeta Weil form (true Zeta23 original formula): complete genuine von-Mangoldt coefficients, both ±log n correlations, BOTH original zeta pole residues, complete signed Gamma bracket, original log10 cutoff n<10.

## 2. A second real Mathlib smooth plateau, composing with the existing IV021 cutoff

IV021 proposed a genuine C∞ cutoff separating E_plus from E_old. That only gives a three-cell partition. An arbitrary fourth-cell-supported Schwartz test f requires another ACTUAL physical Schwartz decomposition — merely pointing to the prime-gap inequalities is insufficient.

IV023 constructs a second Mathlib `ContDiffBump` with center -1/5, inner plateau radius1/20, outer radius1/10:

    β_minus(x)=1  for all x∈E_minus,
    β_minus(x)=0  for all x∈E_old∪E_plus.

The full second physical cell is inside the cutoff's inner plateau because its radius is only1/4000. The nearest point of the already existing first-new physical cell is at distance199/500=.398 from -1/5; the nearest original left collar is at449/500=.898. Both distances exceed outer cutoff radius1/10. These EXACT rational strict inequalities are independently checked.

As in IV021, the operator is genuinely continuous on COMPLEX Schwartz space:

    t_minus := SchwartzMap.smulLeftCLM ℂ β_minus f.

Mathlib's `ContDiffBump.hasCompactSupport.hasTemperateGrowth` guarantees Schwartz closure. No discontinuous `Set.indicator` is used.

Define

    U := f - t_minus.

Then U is a Schwartz function supported on E_old ∪ E_plus. IV021's existing true physical first smooth-cut decomposition (which remains a Lean source candidate upstream) gives

    S := neutralIV021OldCellPart U,
    t_plus := neutralIV021NewCellPart U.

The new theorem `neutralIV023EveryFourCellSchwartz_decomposes` targets, for EVERY complex Schwartz f supported on E_4,

    f = (S+t_plus)+t_minus,
    support(S)⊆E_old,
    support(t_plus)⊆E_plus,
    support(t_minus)⊆E_minus.

There is NO finite-dimensional coefficient restriction, no assumed surjectivity of a Gram map, no arbitrary extra positivity condition, and no spectral eigenvector interpretation.

## 3. Genuine original arithmetic prime preservation: the missing IV022-C theorem

The original IV022-C conjecture was

    P_original(f,f) = P_original(S,S)

for every f supported in E_4 and its original old-collar component S.

**IV023 turns this into a specific full original-source Lean PROOF CANDIDATE**, with a complete dependency trail rather than an assumption:

### (a) Active separation survives base addition

For arbitrary three-cell U, use IV021's decomposition U=S+t_plus. IV022 proved the genuine original ±log active-prime support gaps for both S against t_minus and t_plus against t_minus. The new source lemma

    neutralIV023ActiveSeparated_add

shows the actual pointwise `neutralIV014ActivePrimeSeparated` property is stable when S and t_plus are added, using the literal fact that every translated summand vanishes.

The entire three-cell U is therefore genuinely ±log prime-separated from t_minus at all arithmetic-active n<10. The second component also is genuinely self-separated by IV022's real log2 bound.

### (b) All complex orientations of the translated correlation

The actual original correlation is NOT an abstract orthogonal projection or a Hermitian hypothesis:

    C(U,t;τ) = ∫ t(x) conj(U(x−τ)) dx,

with the genuine original physical L2 representatives.

For every genuine active n<10 and both τ=±log n, IV023 proves all three actual pointwise non-base translated products are zero:

    t_minus(x)·conj(U(x−τ))=0,
    U(x)·conj(t_minus(x−τ))=0,
    t_minus(x)·conj(t_minus(x−τ))=0.

Hence

    C_original(U+v·t_minus,U+v·t_minus;±log n)
       = C_original(U,U;±log n),

for EVERY complex coefficient v, including phase-sensitive terms.

The proof constructs `neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros` by rewriting the actual original correlation into the true real Schwartz integral and expanding the complex source product. This step does not assume that arbitrary mixed residuals have favorable signs.

### (c) All original prime-power terms, not only individual samples

At n with Λ(n)=0, the literal original prime coefficient vanishes without imposing false overlap requirements. At every n≥10 the unchanged original [-11/10,11/10] physical cutoff makes both genuine translations vanish by IV011's exact finite-sum theorem and IV015's rigorous log10 bound.

Thus the proposed theorem `neutralIV023ThreeCellSecond_originalPrime_eq` gives

    P_original(U+v·t_minus,U+v·t_minus)
      = P_original(U,U).

IV021's original first-new-cell dictionary then gives

    P_original(U,U)=P_original(S,S).

Combining,

    P_original(f,f)=P_original(S,S).

**The old n=9 prime term remains live**. It is not asserted zero: the rigorous exact-rational negative control finds a genuine overlap across the two unchanged original collars at log9.

## 4. Mass monotonicity and removal of the explicit four-cell prime hypothesis

IV020 already targeted authentic physical mass addition for disjoint old-collar S and first-new-cell t_plus. IV023 adds the SAME real complex Lebesgue mass identity for the whole three-cell U and the second disjoint cell:

    Mass(U+v·t_minus)=Mass(U)+Mass(v·t_minus).

With v=1 and the actual decomposition f=U+t_minus,

    Mass(S)≤Mass(U)≤Mass(f).

NF600's authenticated original old-collar source bound is

    |Re P_original(S,S)| ≤ (2/5)Mass(S).

The IV023 theorem `neutralIV023EveryFourCell_originalPrime_real_bound` now targets the *unconditional-on-any-new-prime-premise* derived source result

    |Re P_original(f,f)| ≤ (2/5)Mass(f)

for every genuine complex Schwartz f supported in E_4.

This is the new source proof of IV022's previously explicit missing arithmetic hypothesis, using ONLY the literal actual original formula, physical support and earlier source theorems. It is not an arbitrary inequality about a surrogate positive Gram operator.

## 5. The prospective entire four-cell original signed one-sixteenth theorem

IV022 retained the original physical measure17/2000 and the EXACT signed source estimates:

    LowMass(f) ≤ (17/200)Mass(f),
    Original signed Gamma(f)≥(1061/2000)Mass(f),
    BOTH original pole residues cost≤(17/250)Mass(f),
    original surviving n9 prime cost≤(2/5)Mass(f).

The exact sufficient margin is

    1061/2000−17/250−2/5 = 1/16.

Previously the complete four-cell prime cost was a hypothesis. IV023 attaches the explicit genuine-source derived prime transfer:

    neutralIV023WholeFourCellOriginalWeil_oneSixteenth:
      ∀ f:𝓢(ℝ,ℂ),
        (∀x, x∉E_4 → f x=0) →
          (1/16)Mass(f) ≤ Re W_original(f,f).

**Mathematical status: Lean PROOF CANDIDATE only, pending direct kernel acceptance of EVERY IV009–IV023 dependency.** If the kernel genuinely accepts this theorem with standard axioms, it proves full arbitrary Schwartz-function positivity on this one fixed FOUR-CELL region only. It does not prove Weil positivity on all compact Schwartz functions or RH.

## 6. Falsifiability and invariant classification

The new exact original four-cell prime dictionary is falsified by:
- discovery of ANY genuinely active original n with a new-new or old-new physical shifted overlap on the stated E_4;
- a false smooth cutoff support decomposition;
- a mismatch between the original actual two-sign von-Mangoldt series and the proposed old-old preserved value;
- a failed original source lemma or a nonstandard axiom in the true Lean dependencies.

The independent exact-rational checker includes a sharp negative control: an incorrectly placed additional cell at distance 693/1000 from the first new center collides with a genuinely active n=2 log translation. That test correctly rejects a universal invariance claim. It also explicitly preserves the historical original n=9 overlap.

**Intrinsic to the unchanged ORIGINAL source/form:** the quadratic value W(f,f), genuine prime P(f,f), two original polar residues, signed Gamma term, physical complex Lp norms and actual real support, genuine arithmetic translated correlations. Their values do not change under mere basis relabeling.

**Intrinsic to the chosen source support set but not universal:** membership of f in the FOUR-CELL geometric domain, source measure17/2000, and genuine prime translation nonoverlap laws. Another support set may introduce new arithmetic interactions.

**Auxiliary numerical/proof choices:** the two smooth cutoff functions and their plateau radii, source coordinate center/radius parametrization, the rough Fourier L1→low-frequency loss, the coarse gamma lower symbol bounds, pole loss8 and n9 cost2/5, and the resulting one-sixteenth signed positive margin. The margin is a certified candidate *sufficient estimate* and NOT a proven optimal spectral eigenvalue or basis-free coercivity best constant.

**Distinct cross-projection requirement:** This is a dictionary WITHIN ONE original signed-zeta physical realization. It does NOT identify an independent spectral or arithmetic construction, establish a canonical map between projections, or prove any "three projections equivalent" claim. A cross-projection compatibility conjecture requires two separately defined spaces and pairings, an explicitly verified transport map, common-domain assumptions and a counterexample test. IV023 does not assume these.

## 7. Strict kernel / provenance custody

New real original Lean module A:

`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalFourCellSmoothSchwartzPartition.lean`

SIX new original source proof candidates:
- `neutralIV023SecondCutoff_one`;
- `neutralIV023SecondCutoff_base_zero`;
- `neutralIV023SecondCutoff_hasTemperateGrowth`;
- `neutralIV023SecondPart_apply`;
- `neutralIV023FourCell_split_threePlusOne`;
- `neutralIV023EveryFourCellSchwartz_decomposes`.

New original Lean module B:

`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalFourCellPrimeTransferCoercivity.lean`

TWELVE new original source proof candidates:
- `neutralIV023BaseSecond_supportedFourCell`;
- `neutralIV023BaseSecond_mass_add`;
- `neutralIV023BaseMass_le_expandedMass`;
- `neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros`;
- `neutralIV023ActiveSeparated_add`;
- `neutralIV023ThreeCellSecond_activeSeparated`;
- `neutralIV023ThreeCellSecond_activeCorrelation_eq`;
- `neutralIV023ThreeCellSecond_originalPrime_eq`;
- `neutralIV023EveryFourCell_originalPrime_eq_old`;
- `neutralIV023OldMass_le_fourCellMass`;
- `neutralIV023EveryFourCell_originalPrime_real_bound`;
- `neutralIV023WholeFourCellOriginalWeil_oneSixteenth`.

All 18 genuine original Lean theorem names and EIGHT true upstream original source anchors have 26 direct `#print axioms` receipts in the candidate source. No local `axiom`, `sorry` or `sorryAx` is introduced. This is a source fact only; upstream Lean source imports might still fail.

Independent exact-rational checker and **fail-closed kernel auditor**:

`scripts/iv023_original_four_cell_prime_transfer_audit.py`.

Pinned direct genuine Lean/Mathlib two-module workflow:

`.github/workflows/iv023-original-four-cell-prime-preservation-kernel.yml`.

**PASS requires**: all upstream original source modules from IV009–IV022 genuine successful Lean compiler/elaboration; BOTH real IV023 .olean files; direct source-bound `#print axioms` for all 26 named declarations with ONLY `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`; SHA-256 custody binding true original Zeta23 literature source, all NF543/NF600/IV009–IV022 source modules and pinned lake-manifest/toolchain to both real compiled objects; independent exact Fraction cutoff and negative-control receipt.

**No compiler success observed at IV023 creation.** At kickoff prior runs 44850887402 (repaired IV009), 44850967574 (IV018), 44851439481 (IV019), 44851946887 (IV020), 44852596209 (IV021) and 44853338807 (IV022) were all queued/pending. We do NOT promote any of these or IV023 to Lean PASS from source existence, exact-rational calculations or a queued Actions job.

## 8. Next — IV024

1. Recover earliest actual real Lean compiler logs for IV009–IV023 (if Actions remains QUEUED, acknowledge the blocker), repair concrete elaboration/proof failures and propagate changes through the complete stacked draft PR chain. Do not create more positivity layers until genuine kernel results are available.
2. Parameterize admissible multiple new real support cells: the relevant property is FINITE true `Λ(n)≠0` ±log prime-power translated overlap exclusions for all old/new/new-new pairs, plus strict signed Fourier/pole width capacity. Verify a real smooth multi-cell partition theorem, not an assumed spectral or Gram embedding.
3. Advance the distinct cross-projection research only upon a truly independent arithmetic or spectral model: specify a map, two pairings, preservation law, explicit hypotheses and a counterexample condition; do not substitute the internal original-source prime dictionary for cross-projection equivalence.
4. Keep original Phase III NF### exact physical numerical certification progressing without interruption.

**No global Weil positivity, RH, or independent spectral equivalence.**
