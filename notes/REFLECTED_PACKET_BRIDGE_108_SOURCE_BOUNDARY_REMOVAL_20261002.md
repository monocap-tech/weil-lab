# RPB-108 — regular source defect boundary removal

Continues from `48771be33f1091d4a5e89ed9bdfce08e9c795ebc`.

`NeutralSourceBoundaryRemoval` transfers mathlib's smooth compact-test
fundamental lemma to complex compact Schwartz tests on open sets. If a
locally integrable function represents the actual compact source defect,
certified exterior attachment forces it to vanish almost everywhere outside
[-a,a]. Actual central source cancellation forces it to vanish almost
everywhere in (-a,a). The two endpoints are volume-null, so the representative
vanishes almost everywhere and every compact defect is zero. This gives
whole compact weak realization for the existing integral-growth candidate.

This is a conditional reconstruction theorem. Actual central cancellation
and a locally integrable representation of the actual defect are retained
as explicit, unconstructed hypotheses. In particular, regularity is not
inferred from exterior equality or from a tempered distribution. Under this
regularity hypothesis boundary removal is proved, rather than assumed.
Whole-source realization is not yet constructed. Actual source-domain/
quadratic/polarization/normalized estimate witnesses remain open.
Full-symbol growth is retained. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,983 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `d26dbe343dd85772593ee963d9d073af6bda9145`, run `37073137273`, job `111056978955`, source blob `5cb7d738eed3876a2acf3ca03252954be1dbbbda`.

Endpoint audits:

- `locallyIntegrable_ae_zero_of_compactSchwartz_on_open`
- `neutralCompactSourceDefect_regular_exterior_zero`
- `neutralCompactSourceDefect_regular_central_zero`
- `neutralCompactSourceDefect_zero_of_regular_central_cancellation`
- `neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation`

The open-set detection proof consumes the pinned mathlib theorem
`IsOpen.ae_eq_zero_of_integral_contDiff_smul_eq_zero`, converting real smooth
compact tests into complex Schwartz tests through `Complex.ofRealCLM`.
Exterior attachment supplies vanishing outside the closed window. The
central source action cancellation remains explicit. Volume-null endpoints
complete the regular-function reconstruction. The resulting all-compact
identity fills `IntegralGrowthWeilWeakRealization` for the existing candidate.
It does not add a Gaussian identity premise or pointwise growth requirement.

Next: construct the actual locally integrable defect representation and
prove the actual central cancellation, rather than repackaging either
hypothesis. The abstract endpoint null interface does not itself identify
its operator with this corrected source action. Logarithmic domain custody
and source quadratic attachment remain separate obligations.

The validation PR is closed unmerged after separate research promotion.
Only source, root import and checkpoint documentation are promoted. The
original research workflow is preserved.
