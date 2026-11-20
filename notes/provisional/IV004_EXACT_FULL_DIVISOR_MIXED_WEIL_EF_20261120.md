# IV004 — Exact mixed full-divisor source → literal two-argument Weil EF

**Research track:** Phase IV, isolated from the Phase III numerical/matrix runners.

**Status:** New complete Lean theorem *candidates* committed on `research/phaseiv-iv004-exact-mixed-weil-EF`. Kernel and strict standard-axiom audits **NOT YET EXECUTED**. Do not count any IV004 declaration as accepted until that happens. Existing certified NF533/NF598 source results are distinguishable from the new composed theorem.

## 1. Discovered prior theorems — these were ALREADY in the source

The following are real existing results, not IV004 assumptions:

1. `ActualZetaSourceDecomposition.lean`, `neutralLogPairSource_mixed_difference`: for distinct physical source vectors `f,g`, each authentic divisor coordinate `q` (including all multiplicity copies), the mixed P/N difference is the sum of **two** oriented partner products.
2. `ActualZetaWeilZeroForm.lean`, `neutralActualZetaDivisorPairEquiv`: the exact conjugate-ordinate equivalence of the actual zeta divisor, with multiplicities intact.
3. `ActualZetaSmoothLiteralFormulaAutomatic.lean`, `neutralActualZetaWindowCorrelation_literature_of_contDiff`: for **arbitrary two** physical `RealComplexL2` vectors `f,g`, *if their literal windowed mixed correlation is C²*, its complete original zeta divisor sum equals `Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g)`. The genuine external EF theorem already carries the archimedean, prime-power and pole terms; no invented positivity functional.
4. `ActualZetaSmoothCorrelationRegularity.lean`, `neutralWindowCorrelation_contDiff_of_ae_smoothSecond`: one compactly supported C² physical representative, for the second correlation input, suffices for C² mixed correlation; no pointwise continuity of an `L²` equivalence-class representative needed.
5. Mathlib `lp.hasSum_inner` / `lp.inner_eq_tsum`: both authentic source analysis vectors are in complex `ℓ²`, so their mixed Hilbert inner products are the sums of their coordinate products.

These are the precise constituent types whose **composition** the IV004 source now proposes.

## 2. Fully mixed arithmetic dictionary — new proposed theorem

Define the source-graph signed Hermitian form (IV003) using Mathlib's second-slot-linear inner product with arguments reversed:

```text
B_a(u,v) = 1/2 · ( ⟪P_a v, P_a u⟫_ℂ − ⟪N_a v, N_a u⟫_ℂ ).
```

The new IV004 `neutralIV004WindowedMixedEF a u v` is **literally**

```text
Zeta23.EF.literatureRHS
  (neutralWindowCorrelation a
    (neutralNF598GraphPhysical a v)
    (neutralNF598GraphPhysical a u)).
```

Notice the order `v,u`: the signed form is linear in `u`, while the physical correlation is conjugate-linear in its first argument and linear in its second.

For all `a : ℝ` and actual full-source graph vectors `u,v : NeutralActualZetaSourceDomain a`, under the explicit C² hypothesis on the mixed window correlation,

```text
     B_a(u,v) = Zeta23.EF.literatureRHS(k_{v,u}).
```

The proof is not a new explicit formula, and not a diagonal-only polarization shortcut. It combines genuine arithmetic EF of `k_{v,u}` with the *off-diagonal*, multiplicity-aware P/N identity. It establishes the intermediate exact identity

```text
∑_q (conj(P_v[q])*P_u[q] − conj(N_v[q])*N_u[q])
              = 2 · Zeta23.EF.literatureRHS(k_{v,u}).
```

The two coordinate contributions are equal after the *actual conjugate-divisor partner reindexing*; the factor 2 is canceled by the existing signed-source normalization. There is no new zero-count, RH assumption or truncation.

**Proposed source theorems:**
- `neutralIV004SourceMixed_fullDivisorSum`
- `neutralIV004GraphMixed_eq_literature_of_C2`
- `neutralIV004GraphMixed_eq_literature_of_smoothRepresentative`
- `neutralIV004OriginalCollarsMixedEF`.

The first two establish the global-in-the-divisor (but fixed-window) mixed correspondence. The third discharges C² from an a.e. smooth compact representative of one input. The fourth reuses the authentic original collar geometry to give the exact mixed formula for any **two** complex Schwartz tests that actually possess source-graph lifts with the specified physical coordinates. Neither real-odd symmetry nor the original 242 generators are present in the mathematical identity itself.

## 3. Scope precision: what was retyped, what remains open

| Layer | Now in existing source or IV004 candidate | Open |
|---|---|---|
| P/N mixed finite-coordinate algebra | Existing NF source | None for exact algebra |
| All authentic divisor multiplicities / partner involution | Existing NF source | None for exact index transport |
| Genuine TWO-ARGUMENT zeta EF with C² window correlation | Existing NF533 | None under its hypotheses |
| Mixed P/N ℓ² inner product → literal mixed EF | **NEW IV004 candidate** | New Lean kernel check |
| Automatic mixed C² when one window representative is compact smooth | Existing NF534 | Physical test → graph lift |
| Mixed EF of arbitrary complex smooth test **given its graph lifts** | **NEW IV004 candidate** | Establish the lifts uniformly |
| Window enlargement / truly unwindowed support | Not claimed | Exact naturality/EF conventions |
| `|B_a(u,v)|²≤B_a(u,u)B_a(v,v)` for arbitrary admissible inputs | Not claimed | **Essential positivity estimate** |
| General Weil criterion / RH | Not claimed | Unproved |

This is a meaningful *type-conversion recovery*: the mixed explicit formula was already present on the physical side, and the off-diagonal P/N identity on the graph side. The new work proposes the exact composition of those two existing mechanisms, preserving all multiplicities and the two-point symmetry factor.

### A subtle positive consequence, but not a global conclusion

For all **actual** signed graph vectors with a sufficiently smooth mixed window correlation, the mixed arithmetic form is already expressible in the same exact EF format as the diagonal. It therefore becomes possible to study the precise archimedean, prime-power, and pole contributions without first inventing an unrestricted mixed divisor summation theorem.

However, this does not make the signed form nonnegative: it is a *difference* of two positive Hilbert-source inner products. The ordinary graph-norm Cauchy–Schwarz inequality is not the desired signed-Weil Cauchy–Schwarz bound.

## 4. Separate runner policy and verification

No PR is opened and no Actions job is automatically launched from IV004, preserving isolation from Phase III numerical runner scheduling. The only new verifier is a **manual shell entry point**:

```bash
bash scripts/verify_iv004_mixed_weil_ef.sh
```

It builds the actual source-specific Lean module with the pinned repository toolchain, independently prints its four theorem axiom dependencies, rejects `sorryAx` and nonstandard dependencies, and emits an authenticated local result. This has **not** yet been executed; an unrun verifier is not a proof receipt.

Source audit should also validate that the corresponding IV003 imported module is genuinely kernel accepted. The IV004 theorem is NOT self-contained without its III/IV003 compilation dependency.

## 5. Next structural obligation (IV005)

The immediate next investigative question is no longer the mixed explicit-formula summation: its entire source and target are now explicitly connected.

Instead, **arbitrary complex smooth compact test → full source graph lift** remains. The real-odd NF573 convenient lift is narrower than the all-complex NF600 local coercivity type. The accepted generic `neutralActualZetaFullSourceLiftOfRawSamples` already states exactly which two partner zero-sample `ℓ²` bounds suffice; IV005 should try to discharge them from smooth compact support via vertical transform decay and full zeta divisor counting, with neither RH nor a real-odd premise.

The later and logically independent task is the global mixed PSD estimate for separated supports and exact window enlargement. If that estimate is equivalent to RH in an established criterion, merely restating it is not a proof.

**No universal Weil positivity, RH, or completed Phase III claim.**
