# Weil-Lab — IV009
## Exact original physical Schwartz-sum polarization through all-multiplicity zeta divisors

**Canonical investigation:** IV009, Phase IV independent series.
**Stack:** IV006 PR #766 → IV007 PR #767 → IV008 PR #769 → IV009 (this branch).
**Current standing:** eight new Lean proof candidates committed, full upstream-dependent kernel build and standard-axiom audit **pending**. A source preflight, a pull request, or the existence of theorem text is NOT a kernel PASS.

## 1. New exact identity being tested

For any natural number `n`, arbitrary complex Schwartz test family `s : Fin n → 𝓢(ℝ,ℂ)` and arbitrary complex coefficients `u : Fin n → ℂ`, let

```text
S := Σ_i u_i • s_i : 𝓢(ℝ,ℂ).
```

Assume each original physical test vanishes outside the same symmetric containing window `[-a,a]`. Define the **actual** mixed original zeta Weil entry

```text
M_a(i,j) :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a
      ((s i).toLp 2 volume)
      ((s j).toLp 2 volume)).
```

As in IV007, define the *unmodified* finite complex mixed energy

```text
Q_a(s,u) := Σ_i Σ_j conj(u_i) * M_a(i,j) * u_j.
```

The principal IV009 proof candidate asserts exactly

```text
Q_a(s,u) =
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a
      (S.toLp 2 volume) (S.toLp 2 volume)).
```

It is an equality in **ℂ**, not merely equality of real parts, and it uses the genuine original prime, archimedean, and pole values through the unchanged `Zeta23.EF.literatureRHS` on the original correlation.

This is the direct missing original physical polarization bridge, not an assumed sesquilinearity axiom and not an abstract Hermitian-matrix equality.

## 2. Proposed source-grounded proof architecture

1. **Physical sum support.** Finite complex superposition preserves pointwise membership in the same frozen physical window.
2. **Complex-linear exact original frequency samples.** The existing `neutralWindowEvaluation_eq_inner` identifies the actual original window sample with a complex Hilbert-space inner product whose second slot is linear. The genuine Mathlib `SchwartzMap.toLpCLM ℂ ℂ 2 volume` is complex-linear, so at every actual complex frequency `z`,

   ```text
   neutralWindowEvaluation a z (S.toLp 2 volume)
     = Σ_i u_i * neutralWindowEvaluation a z ((s i).toLp 2 volume).
   ```

3. **Original full-divisor summability.** For any supported complex Schwartz second input, NF533/NF534 gives a `ContDiff ℝ 2` original window correlation. Original `neutralActualZetaDivisor_rawTransform_summable_of_contDiff` and `neutralWindowCorrelation_rawTransform` imply unconditional summability of the exact product of conjugate partner sample and direct sample for the full multiplicity-preserving zeta divisor.
4. **Pointwise coefficient expansion.** At each original divisor copy `q`, expand the sample pair of `S` into `Σ_i Σ_j conj(u_i) * D_q(s_i,s_j) * u_j`, preserving the first-antilinear convention and partner conjugation.
5. **Justified finite/infinite interchange.** Each weighted mixed divisor series is summable, and `Summable.tsum_finsetSum` transports the two finite sums across the actual all-copy infinite divisor. No unfounded Fubini assumption is introduced.
6. **Original arithmetic EF attachment.** IV008 attaches each `M_a(i,j)` to the very same original mixed divisor series; NF533/NF534 attaches the physical diagonal of `S` back to the complete literal arithmetic right-hand side. Combining them yields the principal complex identity.

No RH assumption, reality/oddness hypothesis, finite selected 242-generator restriction, fake signed Weil functional, or replacement divisor is introduced.

## 3. Local quantitative corollary — SAME frozen original support

If the family members satisfy the **original two strict endpoint collars** (the existing `neutralNF543OriginalCollars` at `B=11/10`), then the original NF600/NF738 coercivity theorem applies to the actual Schwartz sum `S`. The proposed IV009 source theorem transfers the established local inequality to the actual mixed matrix:

```text
(2/5 : ℝ) * ‖S.toLp 2 volume‖^2
   ≤ (Q_(11/10)(s,u)).re.
```

This certifies a whole finite family **inside the exact same fixed two-collar class**, subject to successful Lean compilation/audit of IV009 and all pending upstream proof modules. It is not an inequality for new support locations, arbitrary window radius, or the full Weil class.

The existing NF740 three-support logical obstruction is compatible with this result: the local bound comes from a simultaneous whole-sum source inequality, not checking separate 2×2 minors.

## 4. Exact new theorem candidate list

Source file: `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean`.

- `neutralIV009PhysicalSchwartzSum_supported`
- `neutralIV009WindowEvaluation_finiteLinear`
- `neutralIV009OriginalPairTerm_summable`
- `neutralIV009OriginalDivisorTerm_finiteExpansion`
- `neutralIV009FiniteMixedEnergy_eq_originalDivisorDiagonal`
- `neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal`
- `neutralIV009OriginalCollars_supported_window`
- `neutralIV009OriginalCollars_mixedEnergy_lower`

The proof file also defines the exact physical Schwartz sum, source-specific mixed divisor summand, and weighted finite-family mixed summand. Each theorem includes an executable Lean proof **candidate**, not an axiomatized restatement.

Four selected existing original/upstream anchors are audited together with these eight new declarations:

- `neutralWindowEvaluation_eq_inner`
- `neutralActualZetaDivisor_rawTransform_summable_of_contDiff`
- `neutralIV008OriginalMixedEntry_eq_divisor`
- `neutralNF738OriginalFiniteCollarSpan_coercive`

The strict audit rejects nonstandard Lean axioms and `sorryAx`, requires a genuine compiled `.olean`, and SHA-binds original source dependencies and the compiled object into a machine-readable certificate. The direct Lean build necessarily imports upstream IV006/IV007/IV008 code, all still subject to independent acceptance.

Workflow: `.github/workflows/iv009-original-schwartz-polarization.yml`.
Audit script: `scripts/iv009_original_schwartz_polarization_audit.py`.

## 5. What still remains mathematically open

Even a successful IV009 would NOT establish positivity outside the existing two strict endpoint collars. Exact source polarization determines the right simultaneous mixed quadratic form and its equivalence with the diagonal Weil value; it does not supply a lower bound for functions newly permitted outside the frozen collars.

Remaining distinct barriers:
- The prerequisite IV006–IV008 kernel/axiom audits and any compiler repairs, plus NF738 source acceptance.
- Authentic source-graph lift/observation compatibility over varying support radii, not merely matching EF values of fixed supported functions.
- A true **support-expanding positive estimate** or all-support factorization for the original arithmetic Weil form, simultaneously controlling all mixed combinations.
- Exact match of the repo's sign/test-class convention to the external universal Weil criterion.
- Independent ongoing Phase III numerical enclosure and terminal certification.

Universal Weil positivity and the Riemann hypothesis remain OPEN.

## 6. IV010 research gate

The natural next Phase IV investigation is **support-expansion obstruction and cross-support positivity**. Audit actual new-support mixed entries against the available frozen-collar coercivity, derive a necessary/sufficient block-extension criterion (e.g., via source-backed Schur complement under justified invertibility), and decide whether a real analytic inequality can control the new rows/columns rather than recycling fixed-support window naturality.

**Milestone:** exact original complex Schwartz polarization (including physically supported finite combinations) and authentic same-collar finite Gram coercivity, pending source-specific Lean kernel acceptance.
