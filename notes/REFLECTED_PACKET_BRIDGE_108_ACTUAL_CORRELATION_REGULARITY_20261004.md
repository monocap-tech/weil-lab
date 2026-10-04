# RPB108 mixed Fourier moments and C² inverse regularity — 2026-10-04

Definitions: [inverse regularity terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_CORRELATION_REGULARITY.md).
Parent: `b35532d28d8573b390cdecc8ed914ef00f9bd49c`.

## Certified result

The new module `WeilDefect/Arithmetic/ActualZetaCorrelationRegularity.lean` defines the concrete mixed L² Fourier product

`S_a(v,w)(ξ) = conj(F_a(v)(ξ)) F_a(w)(ξ)`

and its full-line inverse integral `J_a(v,w) = FourierInv(S_a(v,w))`, in Mathlib's 2π normalization.

L² membership gives absolute integrability of the mixed product by the elementary bound AB ≤ A²+B². For a > 0, the previously proved derived frequency membership ξ F_a(v), ξ F_a(w) in L² places one frequency factor in each slot. The same bound then gives the second absolute moment

`Integrable (ξ ↦ ‖ξ‖² ‖S_a(v,w)(ξ)‖)`.

The zeroth and second moments dominate the first, using ‖ξ‖ ≤ 1+‖ξ‖². Thus all moments of order n ≤ 2 are integrable. Mathlib's Fourier-integral regularity theorem and reflection identify the inverse integral as a C² function on the full real line.

This is derived regularity of the constructed actual-divisor Green vectors. It does not assume retained WD-T38 spectral L²/operator-domain membership.

Four public theorems:

- `neutralActualZetaGreenCorrelationSpectrum_integrable`
- `neutralActualZetaGreenCorrelationSpectrum_secondMoment`
- `neutralActualZetaGreenCorrelationSpectrum_moments`
- `neutralActualZetaGreenCorrelationInverse_contDiff`

## Validation

Exact candidate `c373d83ae0dfa4124fe96e51e954c12149ff48d8` passed [run 37174021939](https://github.com/monocap-tech/weil-lab/actions/runs/37174021939), job `111352757871`: isolated module 9,030 jobs; full `lake build WeilDefect` 9,063 jobs. All four public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The promoted source and root import match the exact validated contents. Workflow and pinned manifest remain validation-only.

Candidate `eec979edacd008062748d3b31b0efceabf04a3e0` exposed pointwise Pi-function reduction, the measurable conjugation API, and the Real namespace of the inverse Fourier reflection theorem. These were corrected without adding a premise. Candidate `2173b08c09b67b8c41265053cf56fcbf9c49be82` left one explicit Pi-power reduction in the first-moment estimate; the final candidate fixed that reduction.

## Remaining representative boundary

This step proves C² regularity of the concrete inverse spectral integral. Equality with the compact mixed correlation K_a(G_a(v),G_a(w)) has not yet been certified. Compact support is therefore not claimed for J_a(v,w), and the external explicit formula cannot yet be applied to it. The already certified all-complex raw-transform samples, pole terms, and actual-divisor zero sum still belong to the exact compact correlation; transporting them to J requires a proved representative identity.

The intended next transport is L¹/L² Fourier agreement and inverse/distribution uniqueness. Once equality almost everywhere is proved, continuity of J and almost-everywhere vanishing outside [-2a,2a] can give actual compact support. Integral identities can then transfer through the almost-everywhere equality. This is a proof target, not an accepted hypothesis or a new representation wrapper.

## Cursor and residue

Next cursor: prove that the certified C² inverse spectral integral J_a(v,w) agrees almost everywhere with the exact compact correlation K_a(G_a(v),G_a(w)). Establish the Fourier normalization and L¹/L² transform agreement, then inverse/distribution uniqueness; do not add the representative identity as a hypothesis. Use continuity and the correlation's almost-everywhere vanishing outside [-2a,2a] to obtain compact support, and transport the already certified all-complex samples, pole operator and actual-divisor zero sum through the proved identity. Recover and audit the external EF_lit_zeta proof-bearing dependency closure under Lean/Mathlib 4.34.0 before applying it, then attach the exact prime/digamma symbol terms. Recover the retained WD-T38 coefficient/source dictionary and prove the same-vector source/null identity before transferring these constructed-carrier results to that witness. No conditional representation wrapper discharges that identity.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed G_a(v) are unproved. The typed WD-T38 record still permits independently named density/Q and abstract P/C operators; the zero-density reindex audit blocks inferring a physical source identity from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
