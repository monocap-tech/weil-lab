# RPB-108 — selected/full neutral background custody

Continues from `7738aa2de2bd9fd0a6ffda1a03ca08a066512179`.

The selected/full source check consumes existing WD-T07, WD-T09 and WD-T10 definitions. For WD-T38's same unit-gain physical mode, `NeutralSelectedBackground` proves that the full shared defect equals minus the unselected negative covariance on that vector. Thus selected nullity is full nullity exactly when the background adjoint coefficient is zero. No such coefficient vanishing is inferred from selected neutrality.

The lawful alternative is already present in WD-T10: if the background has its existing contractive factorization and the retained unit-gain/adjoint realization uses the effective positive synthesis, its null mode cancels the full shared defect. The new theorem immediately consumes that reduction; it does not add a representation field that assumes full source cancellation.

The actual WD-T38 adapter still carries an arbitrary P and no data identifying it with this effective synthesis, no background factorization instance and no concrete full Weil source identity. Consequently actual source witness attachment and actual compact central cancellation are not proved. The geometric explicit formula represents the full Weil form; a raw selected defect cannot be silently substituted for it. The specialization map's full/selected distinction and effective-positive route must be respected on the actual source domain.

This is a certified algebraic attachment requirement and a lawful reduction, not an actual zeta/Weil source realization. Carrier logarithmic-energy membership, source quadratic/polarization/normalized attachment, strict enlarged cancellation, actual locally integrable defect and whole compact realization remain open. Spectral-product L2 membership is not established from WD-T38 and is not assumed. Threshold bookkeeping is closed; logarithmic Gaussian coercivity has not started.

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,938 target build jobs passed. Three endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; unfinished-declaration gate passed. Validation head `149144c67804741da37f9dd4ae1e1781fddd471d`, run `37084121121`, job `111090796458`, source blob `be63417e922d7050e9c11d550b5e2b2f1265f64f`. This target imports the algebraic WD-T38/WD-T10 chain; the preceding canonical-energy/source certificates remain unchanged.

Audited endpoints:

- `wd_t38_full_defect_on_selected_neutral`
- `wd_t38_full_null_iff_background_analysis_zero`
- `wd_t38_effective_positive_full_null`

Repository evidence:

- `docs/ZETA_WEIL_SPECIALIZATION_MAP.md` §§3,5 distinguishes selected signed and full Weil forms; §4 permits incorporation of helper channels into an effective synthesis.
- `WeilDefect/Screening/Quadratic.lean` defines full quadratic value as selected value minus the background adjoint norm square.
- `WeilDefect/Screening/BackgroundCustody.lean` defines WD-T09's full shared defect.
- `WeilDefect/Screening/ResidualBudget.lean` proves WD-T10's exact full-defect reduction to the effective positive synthesis.
- `WeilDefect/Morphology/Neutral.lean` supplies the unit-gain null identity but has no effective-positive/background/source-model identification fields.

Next substantive attachment check: determine the actual P used by the retained source realization and carry its existing background reduction, rather than assuming a new full-null column. Then identify that full source form on its lawful domain and consume the existing diagonal/polarization bridges. These algebraic results do not construct the required carrier/source witness.

Validation-only workflow/cache changes are excluded. Historical notes and canonical/WD-T40 standing remain unchanged.
