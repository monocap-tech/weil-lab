# Weil-Lab — IV019
## Original signed physical-width capacity, a doubled-radius nonzero Schwartz witness, and actual IV009 compiler recovery

**Canonical independent Phase IV head:** IV019, stacked on IV018 PR #786 → IV017 #785 → IV016 #784 → IV015 #783 → IV014 #781 → IV013 #779 → IV012 #778 → IV011 #774 → IV010 #773 → IV009 #771 → IV008 #769 → IV007 #767 → IV006 #766. This is not the separate NF### Phase III original numerical proof-certificate ledger.

**Actual status:** two new ORIGINAL Lean proof modules, SIXTEEN new proposed source theorems and SEVEN imported standard-axiom anchors. The independent exact-rational capacity/prime-gap computation can be checked before Lean. But **nothing in IV019 is kernel-certified until actual pinned CI compiles all source imports, produces both real .olean objects, and passes every strict #print axioms.** Upstream IV009's previous run FAILED; the corrected summability proof has been committed and propagated through every stacked branch, but the repaired replay was QUEUED at IV019 preparation.

### 1. Why revisit width rather than proliferate abstract Schur tests?

IV018 targets a truly source-specific original Weil lower bound of 1/4 of mass for old two-collar Schwartz S and any new Schwartz t supported in [199/1000,201/1000], with no mixed Schur premise. Its genuine prime preservation mechanism requires a finite arithmetic proof: all original old/new/self active prime correlations vanish, but the historical n=9 old-old translation remains and is charged using the accepted NF600 estimate.

One should not infer that arbitrary wider support choices remain safe. Enlarging the new cell increases two genuinely different costs:
- the physical low-frequency Fourier density and BOTH original pole evaluations, controlled by the support measure;
- new possible active ±log n translated overlaps, which could reintroduce genuine von Mangoldt terms and invalidate NF600's old n=9-only prime bound.

IV019 measures these two obstructions independently before changing any literal source formula.

### 2. NEW original-source analytic capacity theorem

Work in the unchanged ORIGINAL physical cutoff window [-11/10,11/10], with any genuinely complex Schwartz physical f supported there. Let

    M(f) := ‖f.toLp 2 volume‖²,
    L(f) := ‖f.toLp 1 volume‖²,
    P(f) := neutralIV011OriginalMixedPrime (11/10) f f.

The true signed Gamma symbol established earlier gives

    Arch(f) >= (11/10)M(f) − (67/10)LowMass(f),

while the actual Fourier transform always satisfies

    LowMass(f) <= 10 L(f).

Therefore the TRUE unchanged original full Gamma/digamma integral obeys

    Arch(f) >= (11/10)M(f) − 67 L(f).

The real original TWO polar residues are bounded at ±1/2 using the original 11/10 physical window:

    Re Pole(f,f) >= −8 L(f).

No old two-collar support is required for these two inequalities. The source is the same literal signed arithmetic zeta Weil expression and retained true 1/(2π) Gamma transport.

Consequently,

    Re[originalPole(f,f)+originalGamma(f,f)]
      >= (11/10)M(f) − 75 L(f).

Now impose the SOURCE-SPECIFIC genuine von Mangoldt bound

    |Re P(f)| <= (2/5) M(f),

which the historical NF600 proves on the original two collars and IV018 proposes to transport to the original three-cell OLD+NEW sums. **IV019 does NOT assert that this prime estimate holds for arbitrary supported f. It remains an explicit true-source hypothesis.**

With this charge included,

    Re W_original(f,f) >= (7/10)M(f) − 75 L(f).

This is the main new flexible signed REAL zeta Weil source budget: it exposes a sharp-from-these-coarse-estimates physical L1 capacity instead of postulating the sign of the diagonal or forgetting the surviving prime term.

If a physical support class gives

    L(f) <= m M(f),

the candidate theorem `neutralIV019OriginalSignedWeil_massBudget_of_prime` gives

    Re W_original(f,f) >= [7/10 − 75 m] M(f).

**This is conditional ONLY on the explicitly displayed L1 size and genuine original prime bound**, not on an abstract Gram PSD or mixed-Schur determinant.

### 3. Exact geometric radius threshold and new candidate

The original NF543 strict TWO collars have combined exact physical Lebesgue measure

    |E_old| = 1/250.

If one adds a genuinely disjoint central interval around c=1/5 with radius r, its width is 2r and the proposed total support-width budget becomes

    m(r) = 1/250 + 2r.

Cauchy–Schwarz on that union would give the physical charge `L(f) <= m(r)*M(f)` for any actual Schwartz test f supported there. IV019 contains the abstract source budget and EXACT rational radius algebra; it does not silently assert a proved Lean three-cell measure bound for arbitrary new r.

The resulting exact numerical signed original source margin is

    margin(r) = 7/10 − 75*(1/250+2r)
              = 2/5 − 150*r.

Hence

    margin(r) > 0   iff   r < 1/375.

This is a capacity threshold **for this particular signed Gamma+pole+NF600 prime-cost estimate**, not an impossibility/no-go theorem for a larger interval or for other methods. It also is NOT unconditional positivity at these radii until the actual prime bound is transferred.

At the IV018 radius r=1/1000:

    m=3/500, margin=1/4.

At the doubled radius r=1/500:

    m=1/125, margin=1/10.

At the budget threshold r=1/375:

    margin=0.

Both exact rational identities appear as Lean theorem candidates, and are independently checked by Fraction arithmetic.

### 4. NEW genuine doubled-radius Schwartz source and arithmetic prime-gap proof targets

The new physical interval is

    E_new_wide = [1/5−1/500, 1/5+1/500]
               = [99/500, 101/500]
               = [0.198,0.202].

It has twice the former width, is outside the original unchanged two NF543 strict collars and is still inside the original full [-11/10,11/10] physical window.

The new IV019 source imports Mathlib's genuine smooth compact bump existence, as used by IV015, to construct an actual complex Schwartz t with

    t(1/5)=1,
    support(t) ⊆ E_new_wide,
    t not in old original collar-supported class.

This is not an abstract hypothetical vector.

The independent exact Fraction checker covers **every integer n=0,1,...,9**, even those with Λ(n)=0, at **BOTH physical old collar centers and BOTH signed original ±log n translations**. It uses the earlier IV015 rigorous positive atanh logarithmic series with a rational tail enclosure; neither Python's floating log nor empirical samples are trusted.

The new Lean theorem `neutralIV019WideFrozenConcrete_allIntegerGap` attempts to prove those original four signed finite REAL log inequalities directly from IV016's rigorously proved/log-bound CANDIDATE bands, at the larger required physical clearance 3/1000 (old radius 1/1000 + new radius 1/500).

The new self-shift lemma likewise derives actual prime-power nonoverlap from `ArithmeticFunction.vonMangoldt_ne_zero_iff`, m≥2 and Mathlib's rigorous lower bound on log2:

    log m >= log2 > 2/500.

Thus new proof candidates yield the REAL original source claims

    neutralIV014ActivePrimeSeparated S t 10
       for EVERY old collar Schwartz S,

    neutralIV014ActivePrimeSeparated t t 10,

and, using IV011's true original finite prime sum and the unchanged log10>11/5 source cutoff,

    P_original(S,t)=0 and P_original(t,t)=0.

The old-old original n=9 contribution remains and is NOT declared zero.

**Acceptance boundary:** these are proof candidates, not successful new Lean proof receipts. The stronger claim that `P_original(S+v•t,S+v•t)=P_original(S,S)` for the wider interval, and therefore a source-unconditional 1/10 lower bound on ALL old-plus-new tests, requires an IV018-style full original pointwise correlation and actual n=9 transfer generalized to the wider interval. That theorem is not in IV019. Do NOT claim the full new support class has been proved positive merely from arithmetic preflight or the isolated mixed/self zero source candidates.

### 5. The surprising bottleneck: spectral budget, not the first shifted prime collision

The independent exact Fraction checker verifies:
- at r=1/500 the old/new signed log-gap and new self-prime log2 clearance are STRICTLY positive for all real source indices necessary for the original n<10 finite arithmetic sum;
- at r=1/375, the physical old/new arithmetic gap still remains STRICTLY positive, while `margin(r)=0`;
- even at r=1/100, the finite old/new signed log gaps around c=1/5 remain positive although the coarse signed Fourier/pole/prime budget is already negative.

Thus, along THIS centered interval family, **the current analytic uncertainty bound becomes insufficient BEFORE real prime-power log-frequency overlaps appear**. This is valuable for planning Phase IV: further extension may require a sharper signed Gamma estimate, better pole cancellation or more intelligent geometry, not merely excluding new prime frequencies.

This does NOT show that the Weil form itself becomes negative or that any global result is impossible. It only shows where the present sufficient coercivity inequality loses its positive margin.

### 6. Current exact compiler result: IV009 failure, explicit repair

The prior real original IV009 Actions run [44844586039](https://github.com/monocap-tech/weil-lab/actions/runs/44844586039) completed with FAILURE at

    WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean:111

Lean correctly rejected the old `change` tactic that attempted to treat the genuine original Schwartz divisor pair term as definitionally equal to the raw correlation transform summand. Because Lean failed to elaborate that proof, downstream declarations showed a `sorryAx` dependency; those declarations were NOT certified.

**Actual repair committed to PR #771 and propagated through PR #773 → #786:** use the already established exact ORIGINAL `neutralWindowCorrelation_rawTransform` theorem to prove pointwise equality by `funext q`, rewrite the actual `hsource : Summable ...` with that equality, then conclude from the transformed summability theorem. This retains the authentic original correlation and complete divisor multiplicity; it is not an axiom/sorry shortcut.

The repaired IV009 compiler replay [44850887402](https://github.com/monocap-tech/weil-lab/actions/runs/44850887402) was QUEUED on the last check. The repaired IV018 compiler replay [44850967574](https://github.com/monocap-tech/weil-lab/actions/runs/44850967574) was PENDING. IV019's own pinned direct build must also pass before any kernel claim.

### 7. Source and audit ledger

Two NEW original Lean modules:

`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalVariableWidthSignedBudget.lean`

Nine original-source theorem candidates:

1. `neutralIV019OriginalSignedGamma_L1Budget`
2. `neutralIV019OriginalSignedPole_L1Budget`
3. `neutralIV019OriginalAnalytic_L1Budget`
4. `neutralIV019OriginalSignedWeil_L1Budget_of_prime`
5. `neutralIV019OriginalSignedWeil_massBudget_of_prime`
6. `neutralIV019OriginalRadiusMargin_identity`
7. `neutralIV019OriginalRadiusMargin_positive_iff`
8. `neutralIV019OriginalDoubleRadius_margin`
9. `neutralIV019OriginalOneTenth_of_prime_and_L1`

`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWiderPrimeFreeBump.lean`

Seven original-source theorem candidates:

1. `neutralIV019WideAbsClearance`
2. `neutralIV019WideFourSignedGaps_of_band`
3. `neutralIV019WideFrozenConcrete_allIntegerGap`
4. `neutralIV019WideSelfLogClearance`
5. `neutralIV019WideSelfActiveGap`
6. `neutralIV019ExistsWiderOriginalPrimeSeparatedBump`
7. `neutralIV019ExistsWiderOriginalMixedAndSelfPrimeFree`

Total **16 NEW source theorem candidates**, plus **7 genuine upstream strict axiom anchors**, with no extra axioms/sorry or RH assumption.

Strict source-bound auditor:
`scripts/iv019_original_width_capacity_kernel_audit.py`.

Dedicated direct pinned Lean/Mathlib workflow:
`.github/workflows/iv019-original-width-capacity-and-primefree-bump.yml`.

Required green proof custody: both real source .olean objects, every one of the 23 exact original `#print axioms` declarations with only standard `propext`, `Classical.choice`, `Quot.sound`, zero `sorryAx`, original mathematical-source SHA256/manifest toolchain binding, and independent exact Fraction receipt. **The Python source preflight does not and cannot close a Lean theorem.**

### 8. Next — IV020

1. Retrieve actual IV009–IV019 direct compiler logs and fix the earliest real source elaboration/sorry/axiom failure; a queued action is not a PASS.
2. Generalize IV018's authentic all-prime old+new transferred correlation identity to the wider true original central cell [99/500,101/500], including both ±log n terms, the original n=9 surviving old prime and the exact original n>=10 cutoff.
3. Construct the true expanded union support Lebesgue-measure / Cauchy–Schwarz certificate of mass 1/125 for every corresponding old-plus-new complex Schwartz source, and attach the new `neutralIV019OriginalOneTenth_of_prime_and_L1` theorem to derive a genuine 1/10 support-extension coercivity bound with no Schur hypothesis.
4. Beyond the current threshold r<1/375, improve the signed spectral/pole estimate rather than misreport a budget failure as an RH obstruction.

**Neither IV019's new physical source nor IV018's prior 1/4 three-cell theorem can be claimed Lean PASS until the complete original dependency chain is actually accepted. No global Weil positivity or RH is established.**
