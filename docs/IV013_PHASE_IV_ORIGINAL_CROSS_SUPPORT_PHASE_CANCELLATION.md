# Weil-Lab — IV013
## Original zeta cross-support phase interference and prime-separated physical tests

**Canonical independent Phase IV iteration:** IV013.
**Stack:** IV006 #766 → IV007 #767 → IV008 #769 → IV009 #771 → IV010 #773 → IV011 #774 → IV012 #778 → IV013 (this branch).
**Formal standing:** nine new actual-source Lean theorem **candidates**, four upstream anchor checks, independent compiler/standard-axiom audit **pending**. All equations and conclusions below are **proposed Lean targets**, not kernel-certified new results until the CI is green.

### 1. Why IV012's triangle budget loses mathematically important information

The true original signed arithmetic mixed Weil expression at the physical window radius b is

    W_b(s,t) = R_b(s,t) − P_b(s,t),

where the prime term P retains every genuine von Mangoldt coefficient and two translated correlations; the *same true* analytic remainder

    R_b(s,t) = originalPole_b(s,t) + originalGamma_b(s,t)

retains BOTH literal zeta polar residues and the unmodified 1/(2π) original Gamma/digamma integral. This identity comes directly from `Zeta23.EF.literatureRHS`.

The IV012 envelope bound

    |W_b(s,t)| ≤ poleBudget + primeBudget + gammaBudget

drops all complex cancellation. IV013 restores the relevant exact interference term **without** modifying the original EF or assuming RH:

    |W_b(s,t)|²
      = |R_b(s,t)|² + |P_b(s,t)|²
        − 2 Re(R_b(s,t) * conj(P_b(s,t))).

This is an algebraic identity attached to actual original arithmetic pieces, not a new positivity estimate.

The sharp one-new-support condition of IV010/IV011, `|W_b(S,t)|²≤AD`, is thus **equivalent** to

    |R_b(S,t)|² + |P_b(S,t)|²
      ≤ A*D + 2 Re(R_b(S,t)*conj(P_b(S,t))),

with `A=Re Q_a(s,u)` the old genuine finite mixed energy, `S=Σ_i u_i•s_i`, and `D=Re W_b(t,t)` the new genuine diagonal.

**Interpretation:** the actual arithmetic analytic task is to secure a sufficiently favorable alignment/cancellation of the original finite prime contribution against the unchanged pole+Gamma remainder, OR control their individual magnitudes strongly enough. There is no valid implication from the IV012 absolute envelope to this sharp inequality unless its separate square condition is discharged.

### 2. Source-specific geometric class where the mixed prime contribution vanishes exactly

IV011 proved (kernel pending) that an old physical Schwartz test `s` supported in `[-a,a]` and a new test `t` supported in `[-b,b]` yield genuine mixed prime samples only for finitely many `n<N`, where `log n>a+b` for all n≥N.

Define the explicit **prime-separated physical Schwartz condition**:

    ∀ n<N, ∀ x∈ℝ,
      t(x)=0 OR
      [s(x−log n)=0 AND s(x+log n)=0].

This checks literal physical translated overlap at the finitely many actual prime-power candidate frequencies. It is NOT an abstract claim that Weil positivity holds on new supports. Under this condition the proposed source proof establishes, by direct translated-product integral vanishing,

    C_b(s,t)(+log n)=C_b(s,t)(−log n)=0
    for every n<N.

Since all n≥N vanish by IV011's actual support cutoff,

    P_b(s,t)=0 exactly,

and therefore

    W_b(s,t)=R_b(s,t)

with no residual prime sum and no dropped pole or Gamma factors.

No source-independent cancellation assumption or oracle is introduced. The condition may be strong and can fail when supports overlap at prime shifts, but it isolates a genuine geometric support subclass with **zero original mixed prime interactions**.

### 3. Exact conditional support-extension and negative-witness gates

For any old finite supported physical combination `S`, any new test `t`, and any complex coefficient `v`:

- **Phase-aware sufficient gate:** with `A≥0,D≥0`, the exact source interference inequality above implies `Re W_b(S+v•t,S+v•t)≥0`.
- **Phase-aware failure gate:** with `D>0`, strict failure of that inequality gives the explicit negative original Schwartz source `S−conj(W_b(S,t))/D•t` from IV011.
- **Prime-separated subclass:** if the mixed prime side vanishes geometrically, the condition reduces to `|R_b(S,t)|²≤AD`. Coupled with the unchanged explicit old/new sign hypotheses, this implies conditional positivity for every `v`.

These are exact mathematical reductions, NOT proof that the arithmetic inequalities or the prime-separation property hold for arbitrary extended support tests. Diagonal `D` positivity remains independently open. For the positivity of an entire old family enlarged by t, the condition must hold for every old complex coefficient vector `u` simultaneously.

### 4. Formal module

New actual original-source file:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean`.

Nine new Lean theorem **candidates**:

1. `neutralIV013OriginalMixed_eq_analytic_sub_prime`
2. `neutralIV013OriginalMixed_phaseInterference`
3. `neutralIV013OriginalMixed_crossBound_iff_alignment`
4. `neutralIV013PrimeSeparated_correlationVanish`
5. `neutralIV013PrimeSeparated_originalPrime_zero`
6. `neutralIV013PrimeSeparated_originalMixed_eq_analytic`
7. `neutralIV013OriginalOneNew_nonnegative_of_alignment`
8. `neutralIV013OriginalOneNew_negative_of_alignmentFailure`
9. `neutralIV013PrimeSeparated_oneNew_nonnegative_of_analyticBound`

The module also defines `neutralIV013OriginalMixedAnalyticRemainder` and `neutralIV013OriginalPrimeSeparated` using the genuine previously constructed arithmetic source functions.

Strict source-bound audit:
`scripts/iv013_original_phase_cancellation_audit.py`.

Direct independent Lean workflow:
`.github/workflows/iv013-original-cross-support-phase-cancellation.yml`.

The workflow requires a genuine `.olean`, all nine new and four upstream source `#print axioms` receipts, no `sorryAx`, only `propext`, `Classical.choice`, `Quot.sound`, and SHA-256-binding of new source, actual original dependency sources, and the compiled object. Preflight alone is not proof.

### 5. Source-specific compiler recovery discovered during IV013 work

Live workflow checks on November 20, 2026 showed:
- IV006 run 44798507850: PASS.
- IV007 run 44800983463: PASS.
- Original IV008 run 44812749256: FAIL at the `star`/complex conjugation rewrite. The patch was then submitted on IV008–IV011 source stacks.
- IV008 repair run 44836233452: **PASS**. The exact original Hermitian source dependency thus now has a successful dedicated kernel workflow.
- IV009 repair run 44836237492: FAIL at its **new** `neutralIV009OriginalPairTerm_summable` theorem, because Lean retained source conjugation as `starRingEnd` while the new target was defined using `conj`. In that run other new IV009 declarations, except those depending on this lemma, already printed only standard axioms.
- Repaired IV009 source was subsequently committed to the IV009, IV010, IV011 and IV012 branches, and IV013 inherits the patch from the last IV012 head. The fix uses Lean definitional `change` rather than the mismatched source-only simp sequence; this is a **candidate repair**, still awaiting its OWN successful kernel run.
- The first IV010–IV012 failures are downstream of IV009's import error and should not be misclassified as independent mathematical counterexamples or formal refutations.

Full IV009–IV013 kernel closure, including new proof compilation and standard-axiom audits, is still open at the time of this stage.

### 6. What remains open — IV014 frontier

**New mathematical estimates still required:**
- A genuine uniform lower bound for `D=Re W_b(t,t)` on *newly* admitted support tests.
- Nontrivial source estimates on `Re(R_b(S,t)*conj(P_b(S,t)))` or otherwise sharp signed arithmetic estimates; the interference identity does not sign the term.
- A viable nonempty family of genuinely expanded-support tests satisfying the prime-separated geometric condition (if it is to be used for positive extension).
- Controlling pole+Gamma remainder against the old and new diagonals; the prime-free condition by itself does NOT guarantee positivity.
- All-old-coefficient-vector uniformity and eventual iterated extension across support radii, with proper external Weil criterion normalization.

**Next IV014:** source-specific geometric prime-overlap feasibility / quantitative residual analysis, while clearing the IV009–IV013 compiler chain. Avoid further stacked claims until relevant upstream kernel results are independently verified.

Global Weil positivity, the Riemann hypothesis, and Phase III numerical terminal certification remain OPEN.
