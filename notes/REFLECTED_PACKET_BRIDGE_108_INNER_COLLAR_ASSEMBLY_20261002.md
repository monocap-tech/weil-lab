# RPB-108 — certified inner-collar regularity assembly

Date: 2026-10-02 (America/Los_Angeles).
Recovered parent: `4cea4deb386799457578f9cefccccc329a859f4b`.
Terminology: [inner collar with fixed cutoff](../docs/TERMINOLOGY_RPB108_INNER_COLLAR.md).
Written predecessor: [analytic reduction](REFLECTED_PACKET_BRIDGE_108_INNER_COLLAR_REGULARITY_20261002.md), preserved unchanged.

## Result and witness scope

The inner-collar regularity reduction is now implemented in `NeutralInnerCollarRegularity.lean`. The auxiliary symbol's temperate growth is derived from the retained target symbol and certified finite-prime growth. The constructed collar is locally integrable; its archimedean gap is `b-c` while its full prime cutoff remains `a`. Actual central cancellation proves zero on the open overlap, yielding almost-everywhere agreement with the existing concrete residual. A constructed smooth bump splits every compact test; the resulting whole-test identity gives the zero function as a genuine representative of the actual defect. The final theorem immediately consumes the existing boundary-removal theorem.

No spectral L2 or independent regular-defect representation premise is introduced. The only remaining source-specific input to this regularity/whole-realization assembly is actual central cancellation, alongside the existing carrier, strict support margin and target-symbol hypotheses. The theorem does not attach or prove that central witness. Actual WD-T38 carrier density/form-domain/quadratic identification and same-domain mixed/normalized attachment remain OPEN. Named-density energy custody remains certified. Spectral L2 membership is unproved and unassumed; the weaker regularity route now suffices conditional on actual central cancellation. Threshold bookkeeping stays CLOSED; F-4 logarithmic Gaussian coercivity is NOT STARTED. WD-T40/RH standing is unchanged.

## Certified declarations

- `neutralWeilSymbolTemperate_at_radius`
- `neutralInnerCollarResidual_locallyIntegrable`
- `neutralInnerCollarResidual_exterior_pairing`
- `neutralInnerCollarResidual_overlap_zero`
- `neutralInnerCollarResidual_eq_candidate_exterior`
- `neutralInnerCollarResidual_ae_eq_candidate`
- `neutralExteriorResidualCandidate_represents_of_central`
- `neutralCompactSourceDefect_zero_of_central`
- `neutralExteriorIntegralGrowthResidual_realizes_of_central`

The local-integrability theorem is unconditional on central cancellation. The collar pairing is an actual source pairing for support-separated tests, obtained by consuming the existing archimedean attachment and exact full-prime split. The overlap, candidate agreement, whole-test realization, zero actual defect and final boundary-removal application depend explicitly on the actual central witness. No endpoint-null or scalar quadratic hypothesis is silently substituted for it.

## Source attachment remains the next frontier

The repaired WD-T38 output retains the named-density witnesses but does not identify that density with the actual Fourier density of the physical carrier. Its independent scalar Q/symbol/pole identity still needs to be attached to sourceDomainQuadratic on the actual source form domain. The selected/effective synthesis defect also needs lawful identification with the full geometric source form. Existing diagonal/polarization and normalized comparison bridges are to be consumed once those identities are available.

Central cancellation on the enlarged interval is not a consequence of endpoint nullity alone. This pass eliminates a separate regularity assumption from the downstream assembly; it does not eliminate the actual source-identification or persistence obligation.

## Proof mechanics

Choose `b=(c+a)/2` and an outer bump radius `d=(b+a)/2`. The bump equals one on `[-b,b]` and has topological support inside `(-a,a)`. For a compact test u, its bump multiple w is a central compact Schwartz test and v=u-w vanishes on the inner interval. The collar represents the target action on v while agreeing almost everywhere there with the concrete candidate. Central cancellation annihilates w. Actual integrability justifies all sums and differences of integrals.

The prime cutoff stays `a` throughout. The auxiliary symbol growth at b is a consequence of the certified archimedean/full-prime split, not a fresh hypothesis. Local integrability comes from the continuous gap convolution, finite-prime translated L2 carrier and actual pole. The final theorem invokes `neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation` with the constructed zero function representing the actual source defect.

## Validation

Whole-root `lake build WeilDefect` succeeded: **9,021 jobs**. The nine declarations above passed individual axiom audits with only `propext`, `Classical.choice`, and `Quot.sound`. The unfinished-declaration gate passed.

- Validation commit: `f1489847e9f5ac62ad7d2f9b6742ba47722b45a2`.
- Validation tree: `dcb6a25062bac2a1b9448762c815ed0870a1e24c`.
- Run: `37088695271`.
- Job: `111104179282`.
- Certified module blob: `68166c337aa9845133eddbc6374bdd9223f57ff0`.
- Root import blob: `8402bdefa1507bd31a809bdf974fd8dc2d09f1cf`.

The initial theorem-target check also passed (8,984 jobs, nine clean audits) at `fa657f3b7f0a980266582dfb178f78a5e89dcb33`, run `37088301589`, job `111103010825`. The final whole-root certificate uses the identical module bytes.

Only the new module, its root import and additive documentation are promoted. The validation workflow is excluded from research promotion; the research workflow remains byte-identical. No historical note is rewritten.
