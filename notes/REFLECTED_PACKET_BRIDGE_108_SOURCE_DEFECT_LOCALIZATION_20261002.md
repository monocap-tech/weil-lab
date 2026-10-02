# RPB-108 — compact source defect localization

Continues from `0a987d79c62dfee094fe5d5b9a515952312be424`.

`NeutralSourceDefectLocalization` defines the actual compact-test defect as
frozen corrected source action minus the concrete exterior candidate pairing.
Genuine candidate integrability proves additivity. Certified exterior
realization proves the defect vanishes on compact tests zero on (-a,a).
Consequently tests agreeing on that open window have equal defects. On a
test supported in the open window, the candidate pairing is zero and the
defect equals the actual corrected source action.

This localizes the remaining obligation; it does not cancel it. Restriction
to an open window also determines boundary jets of smooth tests, so equality
on central restrictions does not exclude boundary-supported distributions.
Next: actual central source cancellation and boundary reconstruction. Whole
compact weak realization and actual source-domain/quadratic/polarization/
normalized estimate witnesses remain open. Full-symbol growth is retained.
Threshold bookkeeping is closed; logarithmic coercivity has not started.

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,982 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `9ef4efd553f38279562a8433f62dc05606d0903c`, run `37071492970`, job `111051735299`, source blob `b2d5fd9bad40f5d01cd82f1b2d1b6b5aab06277b`.

Endpoint audits:

- `neutralExteriorResidualCandidate_compact_pairing_integrable`
- `neutralCompactSourceDefect_add`
- `neutralCompactSourceDefect_exterior_zero`
- `neutralCompactSourceDefect_eq_of_central_eq`
- `neutralCompactSourceDefect_central_eq_action`

The validation PR is closed unmerged after separate research promotion.
Only source, root import and checkpoint documentation are promoted. The
original research workflow is preserved.
