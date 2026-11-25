# Weil-Lab — IV010
## Original zeta Weil mixed Schur gate for one newly admitted physical Schwartz support

**Canonical Phase IV iteration:** IV010 (the user shorthand “NF” means advance the IV series in this Phase IV thread).
**Stack:** corrected IV006 PR #766 → IV007 PR #767 → IV008 PR #769 → IV009 PR #771 → IV010 (this stage).
**Standing:** new source-specific Lean proof CANDIDATES committed, strict original Lean kernel build / source-bound axiom audit PENDING. No fresh cross-support zeta arithmetic estimate has been proved; no expanded-support positivity has been established.

## 1. The precise mathematical obstruction

Fix a smaller window [-a,a] inside a larger [-b,b], with a≤b.

Let a finite family of arbitrary complex Schwartz tests s_i be supported in the SMALLER window. For arbitrary complex coefficients u_i, write

    S = Σ_i u_i s_i.

Let t be ONE additional complex Schwartz test supported inside the LARGER window but not necessarily inside the smaller one. For an arbitrary complex v consider the genuine new physical test

    S + v•t.

The existing original source establishes a literal two-argument mixed Weil expression on any two supported functions, including complete original zeta zeros with their multiplicities and prime/archimedean/pole contributions:

    M_b(f,g) = Zeta23.EF.literatureRHS
      (neutralWindowCorrelation b (f.toLp 2 volume) (g.toLp 2 volume)).

Define:

    A = Re Q_a(s,u),
    B = M_b(S,t),
    D = Re M_b(t,t).

Here Q_a is IV007's authentic finite mixed Weil arithmetic energy of the OLD family. By IV006–IV009's proposed exact source dictionaries, the full NEW original arithmetic diagonal decomposes exactly into

    Re W_b(S + v•t, S + v•t)
       = A + 2 Re(B*v) + D (v.re² + v.im²).

The critical distinction: only A is already controlled by the old support class, under appropriate existing local coercivity assumptions. Neither D nor B follows from representation-window naturality. They reflect genuinely NEW functions and genuinely NEW mixed arithmetic entries.

## 2. Sharp complex one-site positivity condition

The IV010 algebraic lemma reuses the repository's NF740 sharp complex Hermitian 2×2 PSD theorem. It proves that if

    A ≥ 0,
    D ≥ 0,
    B.re² + B.im² ≤ A*D,

then

    ∀ v : ℂ, 0 ≤ A + 2 Re(B*v) + D|v|².

The final IV010 theorem ATTACHES this algebraic implication to the ACTUAL original signed arithmetic mixed Weil form:

    neutralIV010OriginalOneNewSource_nonnegative_of_crossBound.

This is a conditional theorem with an explicit mixed-determinant premise. It does NOT assert that the original zeta pairing satisfies the premise on expanded support. It handles zero-diagonal degeneracy through the underlying NF740 2×2 positivity algebra, without assuming D>0.

### Simultaneous finite-family quantifier

To extend positive semidefiniteness of an entire old family by adding t, the sharp inequality must hold for **every coefficient vector** u of that old family, not merely for each original generator s_i considered separately.

This matters because the generic three-support pairwise-PSD obstruction in the earlier NF740 Phase IV investigation already showed that all separate 2×2 checks need not control a complete 3×3 mixture.

Thus the genuine unproved analytic gate is a source-specific estimate of the form

    |M_b(S,t)|² ≤ (Re Q_a(s,u)) * Re M_b(t,t)

for **all** old finite superpositions S = Σ_i u_i s_i and each newly admitted t, together with nonnegativity of the new diagonal. The original full-divisor arithmetic signs must be controlled; this cannot follow merely from the 2×2 algebra.

## 3. Genuine source proof plan and dependency graph

The new Lean source module imports only the actual prior Phase IV / existing original-source modules, not a substitute EF oracle:

- `ActualZetaPhaseIVOriginalSchwartzPolarization.lean` (IV009 exact original physical Schwartz sum / finite divisor interchange, kernel pending).
- `ActualZetaPhaseIVHermitianTwoBlockPSD.lean` (NF740 exact complex Hermitian 2×2 algebra, independent compiler audit pending).

The new source-specific declarations build the exact original two-test witness, apply IV009 to the literal physical sum f+v•g, derive the authenticated mixed EF Hermitian exchange from IV008, transfer the OLD finite entry block by IV007, and isolate the REAL new-row/column formula before applying the source-identified NF740 sharp algebra theorem.

Nine new proposed theorem declarations:

1. `neutralIV010TwoTests_supported`
2. `neutralIV010TwoTests_physicalSum`
3. `neutralIV010TwoSource_literalBlock`
4. `neutralIV010Mixed_hermitian`
5. `neutralIV010Diagonal_im_zero`
6. `neutralIV010OldPlusNew_exactBlock`
7. `neutralIV010OldPlusNew_realBlock`
8. `neutralIV010HermitianTwoBlock_nonnegative`
9. `neutralIV010OriginalOneNewSource_nonnegative_of_crossBound`

Source file:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean`

The formal proof hypotheses identify which inequalities are actually missing:
`hOld : 0 ≤ Re Q_a(s,u)`,
`hNew : 0 ≤ Re W_b(t,t)`,
`hCross : |M_b(S,t)|² ≤ (Re Q_a(s,u))*(Re W_b(t,t))`.

The last two are new-support inputs, not conclusions.

## 4. Build, audit, and validity separation

Workflow: `.github/workflows/iv010-original-cross-support-schur.yml`.
Audit: `scripts/iv010_original_cross_support_audit.py`.

The strict CI:
1. Preflights exact source declarations and correct genuine zeta EF references, rejecting new `axiom`, `sorry` or `admit`.
2. Builds the actual original Lean module against pinned Lean 4.34 / Mathlib 4.34 dependencies (including the upstream IV006–IV009 sources).
3. Directly replays `#print axioms` for all nine new IV010 theorems and four upstream anchors: NF740 Hermitian PSD, IV009 original Schwartz polarization, IV008 original mixed Hermitian exchange, IV007 fixed-family window transport.
4. Rejects nonstandard axioms and `sorryAx`, requires an actual compiled `.olean`, and SHA-binds all source dependencies and the compiled theorem object.

**A source preflight or PR creation is NOT a kernel certificate.** Record LEAN PASS only if the specific IV010 Actions job succeeds and the strict axiom audit artifact is produced.

## 5. What IV010 does and does not accomplish

**New structural target:** exact source-specific block decomposition under support enlargement, and a mathematically explicit sufficient cross-support mixed determinant bound for the genuine arithmetic Weil form.

**Still NOT established:** the missing zeta mixed determinant inequality for any newly supported t, new diagonal nonnegativity outside the frozen collars, an all-support factorization, full graph/source isometry across radii, an exact external universal Weil test-class equivalence, Phase III terminal numerical custody, global Weil positivity, or RH.

The original local two-collar `2/5` inequality (NF600/NF738) and the proposed IV009 exact polarization provide control of A only when S lies in the genuinely original frozen support. IV010 never transfers that inequality to newly admitted t automatically.

## 6. Next investigation — IV011

The logical next stage is to evaluate the **actual arithmetic cross-support bound**, not repeat the algebra:
- Does the original literal mixed zero-side/prime/archimedean/pole structure supply `|M_b(S,t)|²≤A D` for any genuinely new support direction t?
- Can new-support diagonal D be bounded below by an original source analytic estimate?
- If either inequality fails in a suitable model/explicit sample, identify a rigorous obstruction before attempting an unsupported global extrapolation.
- Investigate a simultaneous Schur-complement / bounded-map argument for the entire old span; separate a genuine uniform estimate from testing a few pairwise minors.

**Milestone definition:** source-accurate, conditional one-site extension/Schur gate with full original mixed EF custody, pending Lean verification. Global positivity and RH remain OPEN.
