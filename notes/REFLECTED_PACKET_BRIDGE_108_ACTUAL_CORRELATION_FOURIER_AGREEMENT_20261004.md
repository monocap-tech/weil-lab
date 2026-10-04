# RPB108 L¹/L² Fourier agreement and exact correlation spectrum — 2026-10-04

Definitions: [Fourier agreement terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_CORRELATION_FOURIER_AGREEMENT.md).
Parent: `725d65b40582ccde103699c186625a0b647261e5`.

## Certified result

The new module `WeilDefect/Arithmetic/ActualZetaCorrelationFourierAgreement.lean` proves ordinary-integral/L² Fourier agreement for an integrable physical L² function. The proof evaluates Mathlib's distributional/L² Fourier identity on Schwartz tests, applies ordinary Fourier integral duality, and uses compact smooth test uniqueness between locally integrable representatives.

For the actual Green synthesis, global L¹ integrability is derived from the certified compact support and compact-window exponential integrability. Thus the actual ordinary transform agrees almost everywhere with the same vector's existing L² Fourier coordinate.

The normalization is proved explicitly:

`Fourier(k)(ξ) = H(k,-2πξ)`.

The window indicator's ordinary Fourier integral is exactly E_a(-2πξ,f). The already certified support identity removes the indicator for G_a(v), giving pointwise ordinary-transform/window-sample agreement. The all-complex correlation identity, specialized to this real parameter, then gives

`Fourier(K_a(G_a(v),G_a(w))) =ᵐ S_a(v,w)`.

This is the exact concrete Fourier product whose inverse integral J_a(v,w) was already certified C². Its existing absolute integrability transfers to the compact correlation's ordinary Fourier transform. Both sides now have the L¹ prerequisites for the remaining inverse identification; these prerequisites were proved rather than supplied.

Eight public theorems:

- `neutralIntegrableL2_fourier_ae`
- `neutralActualZetaGreenSynthesis_integrable`
- `neutralActualZetaGreenSynthesis_fourier_ae`
- `neutralRawTransform_fourier`
- `neutralWindowRepresentative_fourier`
- `neutralActualZetaGreenSynthesis_fourier_window`
- `neutralActualZetaGreenCorrelation_fourier_spectrum_ae`
- `neutralActualZetaGreenCorrelation_fourier_integrable`

## Validation

Exact candidate `ee8d6f160399d66481355158ffb82b4595141954` passed [run 37174603447](https://github.com/monocap-tech/weil-lab/actions/runs/37174603447), job `111354503494`: isolated module 9,031 jobs; full `lake build WeilDefect` 9,064 jobs. All eight public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The promoted source and root import match the exact validated contents. Workflow and pinned manifest remain validation-only.

Candidate `3055d16d58a8abdeb5246a886f867f5c8ef9f541` exposed an unresolved measure argument for Schwartz integrability in the Fourier pairing and the missing ContDiff notation scope. The final candidate pins volume explicitly and opens the scope. Candidate `3419eaa0f52b161310255aaca8e17b690dd043c5` then exposed the symmetric real-inner bilinear flip normalization; standard simplification completes that conversion. No mathematical premise was added.

## Remaining inverse boundary

Equality J_a(v,w)=ᵐ K_a(G_a(v),G_a(w)) has not yet been proved. This module therefore does not claim compact support of J or apply the external explicit formula. The compact correlation's all-complex samples, pole operator identity and zero sum remain certified on their original kernel.

A concrete next proof uses inverse Fourier integral duality against compact smooth tests: pairing J with u becomes pairing S with FourierInv(u); the new spectrum identity substitutes Fourier(K); ordinary duality and Schwartz inversion return pairing K with u. Locally integrable test uniqueness then identifies J and K almost everywhere. Continuity and exterior almost-everywhere vanishing can then yield compact support. This is a proof target, not a representation premise.

## Cursor and residue

Next cursor: identify the already certified C² inverse spectral integral J_a(v,w) with the exact compact correlation K_a(G_a(v),G_a(w)) almost everywhere. The Fourier normalization, constructed Green L¹/L² transform agreement, correlation spectrum identity and L¹ Fourier integrability are now proved; do not reintroduce them as premises. Prove inverse integral duality against compact smooth tests and use locally integrable test uniqueness, then continuity plus almost-everywhere exterior vanishing to obtain compact support. Transport the already certified all-complex samples, pole operator and actual-divisor zero sum through this proved identity. Recover and audit the external EF_lit_zeta proof-bearing dependency closure under Lean/Mathlib 4.34.0 before applying it, then attach the exact prime/digamma symbol terms. Recover the retained WD-T38 coefficient/source dictionary and prove the same-vector source/null identity before transferring these constructed-carrier results to that witness. No conditional representation wrapper discharges that identity.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed G_a(v) are unproved. The typed WD-T38 record still permits independently named density/Q and abstract P/C operators; the zero-density reindex audit blocks inferring a physical source identity from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
