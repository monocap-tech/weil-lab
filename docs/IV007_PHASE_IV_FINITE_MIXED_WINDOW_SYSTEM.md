# Weil-Lab — IV007
## Original finite-family mixed Weil forms: exact window transport and the support-inclusion barrier

**Phase IV research head:** IV007, stacked directly on corrected IV006 PR #766.
**Standing:** new original-source Lean proof candidates committed; direct build and standard-axiom kernel audit **pending**. No merged-main acceptance or unverified theorem promoted to closed.

## 1. Reason for this stage

IV006 investigates equality of the literal mixed Weil explicit-formula value for **two fixed complex Schwartz tests** when the containing physical observation window is enlarged. That is a representation statement, not an estimate.

IV007 asks the next finite-dimensional question: do ALL mixed entries for an arbitrary finite family and the complete energy of an arbitrary **simultaneous complex linear combination** remain equal when the same supported family is viewed in a larger window? And exactly what does that allow us to conclude about positivity as support classes grow?

The answer proposed here is a precise **yes** for the fixed family's entry matrix and formal finite mixed quadratic energy, but only a **one-way** implication for universal nonnegativity across support classes. The reverse implication is the remaining mathematical barrier.

## 2. Authentic arithmetic definitions and target

For any finite index set `Fin n`, choose arbitrary complex Schwartz functions `s i : 𝓢(ℝ,ℂ)`, each supported in `[-a,a]`. For arbitrary `a≤b`, define genuine original mixed entries

```text
M_a(i,j) :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a ((s i).toLp 2 volume)
                                ((s j).toLp 2 volume)).
```

The arithmetic side includes the complete literal prime, pole, and archimedean terms through the actual original `literatureRHS`. Define the source's original all-multiplicity divisor coordinate entry separately as

```text
D_a(i,j) :=
  Σ'_q conj (neutralWindowEvaluation a (conj ordinate_q) (s_i.toLp 2 volume))
          * neutralWindowEvaluation a ordinate_q (s_j.toLp 2 volume).
```

Then for **every** complex coefficient vector `u : Fin n → ℂ` define the full mixed energy

```text
Q_a(s,u) := Σ_i Σ_j conj(u_i) * M_a(i,j) * u_j.
```

The new IV007 Lean candidates establish, for the SAME FIXED support family,

```text
M_a(i,j) = M_b(i,j) for all i,j
D_a(i,j) = D_b(i,j) for all i,j
Q_a(s,u) = Q_b(s,u) for all complex u
Re Q_a(s,u) = Re Q_b(s,u).
```

In particular, the real-quadratic nonnegativity proposition for every coefficient vector of this ONE finite family is equivalent between any two containing windows.

The finite matrix equality is a genuine source-specific identity. It does not assume `M` is positive, Hermitian, a Gram factorization, or the matrix of a graph-norm inner product. No statement identifies `Q_a(s,u)` with the complete diagonal Weil value of the *sum* Schwartz test; this latter step needs an independently audited sesquilinearity/polarization bridge if used.

## 3. The central new gate: nonnegativity goes only downward in allowed support

Define `UniversalRealNonnegative(a)` to assert that `Re Q_a(s,u)≥0` for every finite family of complex Schwartz tests supported within `[-a,a]`, and for every complex coefficient vector.

The new formal implication is

```text
a ≤ b  AND  UniversalRealNonnegative(b)
     ⇒ UniversalRealNonnegative(a).
```

Proof: an a-supported family is also b-supported, and the same family's exact physical mixed values are equal at both observation windows.

**The converse is not claimed.** Positivity already established for a small frozen support does not control functions that are ONLY supported in the larger interval. Exact equality of unchanged entries has no bearing on the new mixed rows and columns created by genuinely enlarging the allowed test set.

This is the obstruction previously distinguished from window naturality. The earlier Phase IV generic three-support countermodel also cautions that even all 2×2 principal restrictions can fail to control a 3×3 energy.

## 4. Source-specific kernel obligations

File: `WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteMixedWindowSystem.lean`

Seven new proposed theorem declarations:

1. `neutralIV007OriginalMixedEntry_natural`
2. `neutralIV007OriginalDivisorEntry_natural`
3. `neutralIV007OriginalMixedMatrix_natural`
4. `neutralIV007OriginalMixedEnergy_natural`
5. `neutralIV007OriginalMixedEnergy_re_natural`
6. `neutralIV007FixedFamilyRealNonnegative_iff`
7. `neutralIV007UniversalRealNonnegative_antitone`

The module directly imports the **pending** IV006 original-source proof module. Thus IV007 is not independent acceptance: its CI must successfully compile IV006 and the IV007 extension together. Three specific upstream IV006 declarations are also audited directly, plus all seven new proofs.

Workflow: `.github/workflows/iv007-original-finite-mixed-window.yml`.
Audit: `scripts/iv007_original_finite_mixed_window_audit.py`.

The audit requires actual built Lean olean output, exact theorem and upstream anchor names, exactly standard Lean axioms, no `sorryAx`, and source/compiled-object SHA-256 custody. The preparatory source preflight is not represented as kernel verification.

## 5. Scope, limitations, and research consequences

**Not established:** unconditional positivity of the signed original Weil form at any new radius; Hermitian symmetry, source-graph lift compatibility for different radii; an exact `Q(s,u)=W(Σu_i s_i,Σu_i s_i)` bridge; external universal Weil criterion's test-space equivalence; complete Phase III numerical custody; global Weil positivity; RH.

IV005's arbitrary complex Schwartz graph-lift proof remains a distinct compilation/audit prerequisite. IV006's window identities remain pending until their own strict kernel audit. No assumption about a finite selected 242-generator family is added.

**Next analytical fork (IV008 candidate):** (a) attach the actual mixed EF to the diagonal form of finite Schwartz sums through authentic source sesquilinearity, and/or (b) derive cross-support estimates for new rows/columns under `a<b` sufficient for *simultaneous* PSD, not merely pairwise conditions. A genuine increase of the support class must be met with new analytic input; exact window transport alone cannot furnish it.

**Milestone definition:** original finite mixed-value naturality and a correctly directed universal-support obligation, subject to kernel acceptance.
