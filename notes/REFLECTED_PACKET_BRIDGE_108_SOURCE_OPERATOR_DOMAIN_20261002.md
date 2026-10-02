# RPB-108 — spectral operator-domain source regularity

Continues from `592eaf780c9c93b93689156b9c3a649971981fc3`.

`NeutralSourceOperatorDomain` gives a concrete spectral route to source
regularity. If the exact right-limit symbol times the carrier's L2 Fourier
transform lies in L2, its inverse Fourier transform is an actual physical
L2 core. Distributional multiplication is identified with the spectral
product using genuine a.e. representative laws. Compatibility of L2 and
tempered Fourier transforms proves exact whole-line core attachment and
pairing. Adding the actual pole and subtracting the existing exterior
candidate constructs a locally integrable representative of the actual
compact source defect, with the correct compact-test pairing. The preceding
boundary-removal theorem then derives whole compact integral-growth weak
realization when actual central source cancellation is supplied.

Actual spectral operator-domain membership and actual central cancellation
remain open witnesses. This criterion is stronger than the source form's
one-logarithm quadratic energy; no form-to-operator-domain upgrade is claimed.
No pointwise exponential growth premise or actual full-source weak identity
is assumed to construct the core. Full-symbol temperate growth is retained.
Whole-source realization and actual source-domain/quadratic/polarization/
normalized estimate witnesses remain open. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,984 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `ab3cdf9f9740142e2a4313b86f0c19eb1509d935`, run `37074199465`, job `111060294126`, source blob `2d7f07fe842550a4b2e5958e7d3a0d8c2de81250`.

Endpoint audits:

- `l2SpectralProduct_toTemperedDistribution`
- `neutralWeilOperatorDomainCore_toTemperedDistribution`
- `neutralWeilOperatorDomainCore_pairing`
- `neutralWeilOperatorDomainDefect_locallyIntegrable`
- `neutralWeilOperatorDomainDefect_represents`
- `neutralExteriorIntegralGrowthResidual_realizes_of_operatorDomain`

The general spectral-product theorem does not assume the symbol itself
belongs to Lp. Its product with the Fourier carrier supplies the needed L2
class. The exact inverse Fourier core is identified through
`Lp.fourier_toTemperedDistribution_eq` and
`Lp.fourierInv_toTemperedDistribution_eq`. Its ordinary representative is
locally integrable by genuine L2 membership. Compact pole and candidate
integrability justify addition and subtraction in the actual defect pairing.

Next: establish actual spectral operator-domain membership from applicable
source information, or construct actual defect regularity by a weaker route;
and prove central cancellation of the actual corrected source action.
Compact support and the abstract endpoint null equation do not themselves
supply either witness. The operator-domain criterion is a sufficient route,
not a new requirement imposed on every possible form-domain solution.
Actual logarithmic form-domain custody and source quadratic identification
remain independent open attachments.

The validation PR is closed unmerged after separate research promotion.
Only source, root import and checkpoint documentation are promoted. The
original research workflow is preserved.
