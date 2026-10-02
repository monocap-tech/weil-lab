# RPB-108 — canonical supported logarithmic form domain

Continues from `e12e1a1c2499f20829148cd1115cfa9b551e7241`.

`NeutralCanonicalFormDomain` constructs the full complex submodule of
physical L2 vectors supported almost everywhere in [-a,a] whose normalized
Fourier transforms have finite logarithmic energy. Weight continuity,
a.e. L2 representative laws and a square-norm domination prove genuine
addition and complex-scaling closure. Every lawful existing source-domain
attachment is contained in this concrete domain. A constructor attaches
the actual physical carrier to it from one explicit finite-log-energy
witness, deriving the enlarged support condition from the carrier itself.

Actual finite logarithmic energy of the carrier remains open. The constructor
does not identify the imported source form or prove its quadratic identity.
Source quadratic/polarization/normalized estimate attachment, actual spectral
operator-domain membership, central cancellation and whole-source realization
remain open. The canonical form domain is not the stronger operator domain;
no form-to-operator-domain upgrade is claimed. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,985 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `c35677bfc7b61f08e9adc56fff688005c145a835`, run `37075421157`, job `111064120041`, source blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`.

Endpoint audits:

- `logarithmicFourierWeight_continuous`
- `finiteLogFourierEnergy_add`
- `finiteLogFourierEnergy_smul`
- `mem_neutralCanonicalLogFormDomain_iff`
- `sourceFormDomain_le_canonical`
- `neutralCanonicalSourceFormDomainAttachment`

The addition proof uses the exact L2 Fourier linear-isometry map and its
representative addition law, with the bound
`norm(F+G)^2 <= 2*(norm(F)^2+norm(G)^2)` under the nonnegative logarithmic
weight. The scaling proof transfers energy by the factor `norm(z)^2` and
the a.e. representative scaling law. Zero energy and physical support are
also proved through a.e. L2 laws rather than assumed pointwise for selected
representatives. The concrete domain includes all eligible vectors.

The constructor eliminates the need to supply an arbitrary domain record:
finite carrier logarithmic energy plus its existing support data suffice
for a lawful concrete attachment. It does not prove carrier energy or
identify the imported source domain/form with the whole canonical domain.
The existing mixed-form and polarization machinery can consume this record
once its energy witness and the actual source quadratic identity are supplied.

Next: prove actual carrier logarithmic energy and source quadratic attachment;
also pursue actual defect regularity and central source cancellation. The
operator-domain route is sufficient for regularity but is not imposed as a
requirement on every possible form-domain solution.

The validation PR is closed unmerged after separate research promotion.
Only source, root import and checkpoint documentation are promoted. The
original research workflow is preserved.
