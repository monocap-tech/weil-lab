# NF735 (canonical; legacy NF734) — Phase IV type audit: local support positivity versus universal Weil positivity

> **Registry correction (2026-11-20):** This Phase IV investigation is canonical **NF735**, following Phase III NF734 (PR #758). The existing branch `research/nf734-phaseiv-collar-type-audit`, source filename, and `neutralNF734…` Lean theorem identifiers are retained as immutable legacy source identifiers. Canonical numbering does not imply these new Lean proofs are accepted; the original CI run 44784200222 failed on a closure proof-term type mismatch, repaired in a later commit and subject to a fresh kernel check.

Status: **analytical investigation and standalone generic Lean proof candidates**. No universal Weil claim, no RH claim. Numerical Phase III continues independently.

## 1. The first important result is already stronger than “one positive carrier”

The existing repository source `WeilDefect/Arithmetic/ActualZetaOriginalCollarCoercivity.lean` states:

```lean
theorem neutralNF600SmoothCollarLower :
    neutralNF599SmoothCollarLower (2/5)
```

The type is expanded in `ActualZetaOriginalSupportCoercivityTransfer.lean`:

```lean
def neutralNF599SmoothCollarLower (c : ℝ) : Prop :=
  ∀ s : 𝓢(ℝ,ℂ), (∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) →
    c * ‖s.toLp 2 volume‖^2 ≤ neutralNF598SmoothWeil s
```

And `ActualZetaOriginalCollar242Correction.lean` defines the **literal** fixed support:

```
E = (-11/10, -11/10+1/500) ∪ (11/10-1/500, 11/10).
```

Thus the source establishes **a coercive positivity assertion for every complex Schwartz function supported in E**, not merely the 242-parameter original source and not merely real-odd tests. The finite numerical solve is used to select and authenticate the original *nonzero carrier* and its coefficient box, not to supply this whole support-class lower bound.

This means there already is **infinite-dimensional local support-class positivity** in Phase III. We had underreported its quantifier in ordinary progress summaries.

As a direct algebraic consequence, for every finite family `s₁,…,sₙ` supported in E and arbitrary complex scalars `c₁,…,cₙ`,

```text
  neutralNF598SmoothWeil (Σ i, cᵢ • sᵢ)
    ≥ (2/5) * ‖(Σ i, cᵢ • sᵢ).toLp 2 volume‖².
```

The support condition is preserved under finite linear combinations. This is a derived statement on the **same local support space**, not a global theorem and not a new numerical result. A future source-bound Lean wrapper can record it explicitly.

## 2. Exact source-side type of the functional

`ActualZetaOriginalSignedGraphLimit.lean` defines

```lean
def neutralNF598SmoothWeil (s : 𝓢(ℝ,ℂ)) : ℝ :=
  (Zeta23.EF.literatureRHS
    (neutralWindowCorrelation (11/10:ℝ)
      (s.toLp 2 volume) (s.toLp 2 volume))).re
```

`ActualZetaOriginalSignedGraphForm.lean` relates the full source-graph signed form to the literal EF diagonal, when the original support and physical-lift conditions hold.

The window parameter `11/10` is *literal*, not a free parameter. For supported tests in E, NF573 certifies that the window representative equals the underlying physical test almost everywhere; outside that fixed window, this equality is not automatic. In particular, **shifting a test function outside the original window cannot be treated as a proven invariance of `neutralNF598SmoothWeil`**. Any proposed translation or window-exhaustion argument first requires a true unwindowed/variable-window correlation bridge.

`ActualZetaOriginalPhysicalStripFullGraph.lean` (NF575) provides a substantial convergence transfer, but its inputs have support in `[-11/10, 11/10]` and require a common strip-envelope bound. It does **not** state that all compactly supported smooth tests can be approximated within the graph topology, or that the signed form is continuous in an unrestricted global test topology.

## 3. External target theorem and normalization discipline

The classical target is positivity of the **Weil autocorrelation quadratic form** for every admissible test, not positivity of an arbitrary linear functional on arbitrary functions. See Lagarias, *The Riemann Hypothesis: Arithmetic and Geometry*, Theorem 3.2, equation `W^(1)(f * tilde(f)) ≥ 0` for all nice tests: https://websites.umich.edu/lagarias/doc/mt-holyoke-rev.pdf .

The repo's EF sign, Fourier convention, window normalization, complex involution, pole terms and test-class restrictions must be reconciled **on the nose** before invoking that criterion. No extant Phase IV result identifies the exact repo `neutralNF598SmoothWeil` at arbitrary support with that external global form. Published equivalents are mathematical references, not imported Lean axioms or source-specific kernel certificates.

## 4. The actual missing type conversions

| ID | Existing type | Required type / property | Standing |
|---|---|---|---|
| IV-1 | All complex Schwartz tests supported in fixed two-collar E | Arbitrary admissible compact tests | **OPEN: support enlargement** |
| IV-2 | `neutralWindowCorrelation (11/10)` | Full autocorrelation / variable-support window and exact EF normalization | **OPEN: domain and sign dictionary** |
| IV-3 | Full source-graph continuity on fixed `NeutralActualZetaSourceDomain (11/10)` and NF575 sequences with common strip bounds | Continuity in a topology admitting the entire criterion test class, or a proven compatible graph exhaustion | **OPEN: topology** |
| IV-4 | Strong positivity on each local test *within E* | Positive semidefinite mixed Gram form across decomposed/translated support pieces | **OPEN: cross terms** |
| IV-5 | Fixed collar geometry: total length `1/250`, low Fourier band `(-5,5)`, only exceptional prime-power `9` in the support calculation | A uniform replacement as the support and prime-overlap pattern vary | **OPEN: quantitative scaling** |
| IV-6 | Original 242-dimensional selected source and nonzero strict carrier | Arbitrary finite families or a proven dense exhaustion and a global limit | **OPEN: quantifier/exhaustion** |

Note: IV-1 is **not** simply a missing finite-dimensional rank argument. The local theorem already ranges over infinitely many functions. Conversely the two collars, as a strict support restriction, do not form a dense subspace of the original full L² window: any nonzero smooth interior test supported, say, in `(-1,1)` is orthogonal to every E-supported test. This invalidates a naive appeal to physical-L² density.

## 5. Two formalizable metaresults and the non-transfer test

`WeilDefect/Arithmetic/ActualZetaPhaseIVTypeAudit.lean` proposes two standalone interfaces using only standard Mathlib:

- **Dense/continuous transfer:** a continuous real-valued functional nonnegative on a dense set is nonnegative everywhere. The theorem does not assert that the collar class is dense or that the actual global Weil functional is continuous in the required topology.
- **Mixed-term obstruction:** the quadratic form `Q(x,y)=x²+y²−3xy` is nonnegative on each coordinate axis but `Q(1,1)=-1`. Thus positivity on two local support subspaces separately does not imply positivity on their sum. This is a logical countermodel, *not* a negative example for the actual zeta Weil form.

The support-class theorem **does** imply positivity of all linear combinations whose individual tests stay within E. The barrier begins when combining genuinely new support locations, because their mixed correlations enter the arithmetic explicit formula.

A productive bridge would define the full sesquilinear mixed pairing `B(s,t)` from the literal EF applied to a genuine (unwindowed) cross-correlation, prove Hermitian/polarization identities with exact conventions, and determine when `[B(sᵢ,sⱼ)]` is positive semidefinite for families **not all contained in E**. Positivity of a 2×2 block requires cross control; this is not supplied by the existing local coercivity proof. In general one needs bounds of the form `|B(s,t)|² ≤ B(s,s) B(t,t)` under the appropriate hypotheses, but establishing them universally could be as hard as RH. Do **not** assume such bounds.

## 6. First Phase-IV investigative execution sequence

1. **Dictionary audit.** Typecheck exact passage from `NF598SmoothWeil` to the complete conventional zeta-Weil criterion, including sign, conjugation/involution, pole residues and the test class. Prove or document any mismatch; never silently identify the two forms.
2. **Local retyping.** Create source-bound theorem `∀` finite families of complex Schwartz tests supported in E, their complete local Weil Gram form satisfies the same `2/5` coercivity. Reuse `neutralNF600SmoothCollarLower`; do not introduce numerical inputs.
3. **Variable-window interface.** Prove window-parameter naturality for supported Schwartz functions, then formulate a clean global cross-correlation function independent of a fixed `11/10` carrier. Keep fixed physical window versus unrestricted test-support domains distinct.
4. **Mixed two-support pilot.** Test and bound the exact mixed EF pairing for two translated copies of the original collars; expose all new prime overlaps and the norm/Gram off-diagonal requirements. A failed bound is information, not a reason to change the original signed form.
5. **Only then density/limit.** Determine whether an actually positive, linearly stable test family is dense in the correct criterion topology. A family of individually positive vectors is insufficient. Prove the continuity needed for passage to the limit.

## 7. Research conclusion

The claim “Phase IV still requires substantial new mathematics” was premature as a diagnosis of *which* mathematics is missing. There is an already-proved infinitely quantified local support positivity theorem, so the first move is to retype that result, not to generate yet another 242-dimensional numerical system.

However, **the cross-support mixed form, varying support window, and exact global test-domain/topology remain genuine mathematical obligations**. Merely rephrasing the finite original strict carrier or tiling its support cannot discharge them.

Nothing here claims Phase III or Phase IV completion, full global Weil positivity, or RH. The accompanying generic Lean file is a kernel **candidate** until CI and strict axiom audit pass.
