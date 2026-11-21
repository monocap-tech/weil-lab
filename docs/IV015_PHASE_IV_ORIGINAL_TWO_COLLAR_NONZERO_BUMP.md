# Weil-Lab — IV015
## Actual nonzero complex Schwartz bump outside frozen NF543 collars, with exact Λ-active arithmetic separation

**Canonical track:** independent Phase IV IV015, stacked on IV014 PR #781, IV013 #779, IV012 #778, IV011 #774, IV010 #773, IV009 #771, IV008 #769, IV007 #767, IV006 #766. **Not** Phase III NF749 original numerical matrix production.

**Compiler standing:** source candidates COMMITTED; genuine original Lean/Mathlib module builds + standard-axiom audits PENDING. Source existence, exact-rational Python bounds and proof candidates are **not** terminal kernel certification.

### 1. Correct geometric object: original TWO collars, not the coarse 11/10 window

The unchanged, literal, historical NF543 original physical support is

    E_original =
      Ioo(-11/10, -11/10+1/500)
        ∪ Ioo(11/10-1/500, 11/10).

This is a pair of width-1/500 **open** Schwartz support collars, not all of [-11/10,11/10]. In particular, a new test around 1/5 can be outside this original source class while remaining inside the SAME broad original physical window.

**This distinction is central.** Forcing new physical tests to live outside [-11/10,11/10] when establishing an enlargement of the original narrow collar class would have manufactured a needless, possibly infeasible, prime-shift gap condition.

The exact centers of the frozen original collars are

    cL = -1099/1000, cR = +1099/1000,

with exact closed interval radii 1/1000 enclosing the original strict collars. No original test, coefficient, prime weight or cutoff geometry is altered.

### 2. First actual nonzero complex physical Schwartz construction

Mathlib already proves `exists_contDiff_tsupport_subset`: for any neighborhood of a center c in a finite-dimensional real normed space, an actual real C∞ compactly supported bump f exists with f(c)=1. IV015 uses that theorem on the real open interval

    (c-r,c+r), r>0.

It maps the real bump through the genuine `Complex.ofRealCLM` and packages the resulting *actual* complex Schwartz function using `HasCompactSupport.toSchwartzMap`.

The new Lean source establishes as a proof candidate:

    ∃ t : 𝓢(ℝ,ℂ),
      t(c)=1,
      t(x)=0 for x∉[c-r,c+r].

This is a genuine nonzero Schwartz object construction, **not** a hypothetical nonzero Gram vector. The support remains explicitly controlled.

The next abstract theorem says: if c lies outside the old source interval [-a,a], the bump t cannot equal any old finite complex Schwartz combination supported in [-a,a]. This does not require arithmetic or PSD.

### 3. Uniform prime-free source construction for the ORIGINAL narrow collars

IV015 then addresses the **real** frozen original source class. Let `neutralNF735InOriginalCollars s` be the unchanged existing actual source predicate, defined by vanishing off `neutralNF543OriginalCollars`. The old finite complex sums are preserved in that class by the existing `neutralNF738OriginalCollars_finset_linear` theorem.

For a new bump around c with outer radius r, impose the genuine finite von-Mangoldt-active conditions

    δ+r < |c-cL-log n|, δ+r < |c-cR-log n|,
    δ+r < |c-cL+log n|, δ+r < |c-cR+log n|,

for each `n<N` with **actual `Λ(n)≠0`** and δ=1/1000.

These FOUR inequalities certify separation from both original physical collars and both original ±log n prime translations.

The new theorem `neutralIV015ExistsNonzeroNewTwoCollarPrimeSeparatedBump` is a *uniform existence proof candidate*: for any center/radius satisfying the explicit finite gaps, the **same** nonzero t is prime-separated from **every** original collar-supported old Schwartz test, rather than one arbitrarily selected vector.

It also proves `t(c)=1` outside E_original, so `t` is NOT in the old original collar support class. In particular it cannot equal any old finite physical Schwartz superposition.

This is substantially stronger than IV014's conditional assertion `IF a proposed new t is prime-separated`; IV015 supplies an explicit nonzero Schwartz construction from a checkable geometric hypothesis.

### 4. An actual rational center with independently certified interval feasibility

An independent exact-arithmetic certificate selects

    c = 1/5 = 0.2,
    r = 1/1000 = 0.001,
    b = 11/10 = 1.1,
    N = 10.

The new bump interval [0.199,0.201] lies strictly inside [-1.1,1.1] but is disjoint from both original source collars near ±1.1.

Script `scripts/iv015_frozen_collar_exact_log_gap.py` checks **all integers n=0,...,9**, including n where von Mangoldt would vanish (this is *stronger* than the Λ-active hypothesis), and all FOUR signed original physical collar separations. It uses ONLY `fractions.Fraction` and positive rational bounds from

    log n = 2 * Σ_{k≥0} y^(2k+1)/(2k+1),  y=(n-1)/(n+1),

with an exact one-sided tail bound

    tail ≤ 2*y^(2K+1)/((2K+1)*(1-y²))

for `K=96`. The arithmetic enclosure is therefore rational and exact, not `math.log`, approximate floats, empirical interval sampling or external numerical package assumptions.

The independent exact lower bound for the MINIMUM of all true translated interval exclusions is approximately **0.08529436**, attained near n=4. The certified lower cutoff margin at n=10 is approximately

    log(10) - 11/5 > 0.10258509.

Values shown as decimals here are only for readability; the generated receipt stores the exact positive rational lower bounds and source parameters.

The independent regression tests reject an old-collar center collision, an oversized candidate bump radius, a new test outside its physical window and an invalid too-early log-prime cutoff. These are **source arithmetic checks, not Lean proof receipts**.

### 5. What EXACTLY is proved or left open inside Lean?

The source contains a concrete frozen-center theorem target

    neutralIV015FrozenConcrete_originalPrimeFreeBump_of_gap

at c=1/5,r=1/1000,N=10. This theorem does **NOT** assume the existence of a Schwartz bump: it constructs the genuine complex Schwartz bump from Mathlib and proves that it leaves the original two-collar test class and any old finite span.

The original infinite mixed prime cutoff is separately targeted as a fully Lean-based result

    neutralIV015FrozenConcrete_logCutoff:
       ∀ n≥10, (11/10)+(11/10) < Real.log n,

using Mathlib's rigorous explicit bounds for `log 2`, `log 5`, and `log 10 = log 2 + log 5`.

**Crucial remaining leaf:** the specific finite real logarithmic inequalities for the four collar translations n<10 are a *visible premise* of the final concrete Lean existence theorem, named

    neutralIV015FrozenTwoCollarActiveGap (1/5) (1/1000) 10.

The independent rational arithmetic checker establishes these interval facts externally, but the new Lean source DOES NOT yet discharge them as kernel theorems. To promote the concrete source witness without numerical side hypotheses, those rational logarithm inequalities must be formalized in Lean, using the Mathlib exact log bounds or its certified dyadic interval tactic. **Do not present this external source preflight as a completed Lean proof of the numerical gap.**

### 6. Exact original signed arithmetic consequence

Given the genuine old finite family s with all source rows supported in E_original, the new bump construction yields

    t(c)=1, S(c)=0,
    t ≠ S,
    P_b(S,t)=0,

where `S=Σ_i u_i•s_i` and `P_b` is the COMPLETE original `Zeta23.EF.literatureRHS` von-Mangoldt mixed prime contribution.

The original mixed signed Weil value therefore satisfies the exact arithmetic source identity

    W_b(S,t) = originalPole_b(S,t) + originalGamma_b(S,t).

All divisor multiplicities, original two polar evaluations and the original Gamma/digamma term are preserved. No synthetic matrix or generic prime oracle is substituted.

**Very important:** this is a *prime-free mixed CROSS term*, not a claim that the newly admitted test has a prime-free DIAGONAL or positive Weil energy. The self-pairing `W_b(t,t)` involves different source correlations. This distinction prevents a false step from mixed cross geometry to global positivity.

### 7. Formal ledger and independent kernel workflow

New Lean modules:
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean` — five general complex Schwartz construction and original EF source theorems;
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean` — eight original two-collar, finite logarithmic center and exact EF witness proof candidates.

**Total: thirteen new Lean theorem proof candidates**, plus imported strict-axiom source anchor checks. Nonzero bump construction, frozen physical collar exclusion, genuine prime-freeness, finite old-span separation and exact original EF recovery are distinguished as separate declarations.

Independent strict audit:
`scripts/iv015_original_nonzero_two_collar_schwartz_audit.py`.

Dedicated pinned Lean/Mathlib workflow:
`.github/workflows/iv015-original-nonzero-two-collar-schwartz-bump.yml`.

The workflow first checks all exact-rational arithmetic negative regressions, then builds both real Lean physical Schwartz modules, requires two real compiled `.olean` objects, replays direct `#print axioms` for **all new and original source anchor declarations** with only standard `propext`, `Classical.choice`, `Quot.sound`, rejects `sorryAx`, and records SHA-256 source, manifest, object and exact-rational receipt custody.

Successful Python does NOT count as a successful Lean source theorem. Success of old IV006–IV008 does NOT establish IV009–IV015.

### 8. What remains open, including IV016

- **IV009–IV014 original Lean dependency chain:** pending real terminal source builds and axiom receipts at IV015 creation. IV006–IV008 kernel pass.
- **Concrete finite log-gap Lean proof:** the frozen c=1/5,r=1/1000,N=10 arithmetic side condition is independently exact-rational checked, but still a named Lean premise in the concrete bump theorem.
- **Original new diagonal:** `D=Re W_b(t,t)` has NO established nonnegativity just from construction or prime-free mixed pairing.
- **Residual Schur determinant:** `|W_b(S,t)|²≤AD` remains open; zero mixed prime component is not enough.
- **Beyond a single new source:** extending an entire support class still requires uniform multi-direction positivity and a genuine global all-support Weil criterion.
- **Phase III numerical certification:** independent NF749 track and its own source/kernel/payment obligations.

**Next IV016:** (1) discharge the concrete rational `±log n` finite gaps DIRECTLY in the Lean kernel using known rigorous Mathlib log bounds, (2) quantify actual original two-pole-plus-Gamma mixed residual for the new frozen-center Schwartz source, and (3) test the new diagonal without assuming its sign.

No global Weil positivity, Riemann hypothesis, new-support diagonal positivity, or complete Phase III enclosure is claimed.
