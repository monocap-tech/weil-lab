# RPB108 exact right-limit prime spectral transport — 2026-10-04

Definitions: [prime transport terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_PRIME_TRANSPORT.md).
Parent research: `d51e3d3b512631e9777faac7033d1c94b1ed2602`.

## Certified result

The literal prime term on J_a(v,w), the already proved compact C² inverse correlation, is exactly the existing right-limit prime Fourier multiplier pairing:

PrimeForm_a(v,w) = ∫_ξ rightLimitPrimeSymbol(a,2πξ) · S_a(v,w)(ξ),

where S_a(v,w) is the conjugate of the first physical Green L² Fourier transform times the second.

The support certificate for J closes the finite cutoff. If n is not a prime power, Λ(n)=0. If n is a prime power outside rightLimitPrimePowerFinset a, then log n > 2a and both J(log n) and J(−log n) vanish. Thus the literal infinite prime series has finite support, is summable, and equals the finite sum over the existing right-limit set. Equality-threshold prime powers are retained, preserving the existing log n ≤ 2a convention.

The exact inverse Fourier dictionary evaluates this same J by the raw transform of this same S at the dual frequency 2πt. Pairing the t and −t evaluations gives 2 cos((2πξ)t). Each phase has norm one; the already proved L¹ spectrum supplies integrability. Multiplication by Λ(n)/√n gives the existing coefficient 2Λ(n)/√n. The finite sum can therefore pass through the integral lawfully, yielding rightLimitPrimeSymbol(a,2πξ), with its existing normalization and sign in the parent literal formula.

No chosen physical representative is evaluated at prime points in place of J. No independent source identity, operator-domain assumption or conditional representation premise is introduced.

Seven public theorems:

- `neutralActualZetaGreenPrimeSummand_zero`
- `neutralActualZetaGreenPrimeSummand_summable`
- `neutralActualZetaGreenPrimeForm_finite`
- `neutralActualZetaGreenCorrelationInverse_spectral`
- `neutralActualZetaGreenCorrelationInverse_pair_spectral`
- `neutralActualZetaGreenPrimeSummand_spectral`
- `neutralActualZetaGreenPrimeForm_spectral`

The prime summand definition precedes its use. Supporting proofs also establish integrability of each spectral prime summand before the finite integral interchange.

## Validation

Exact candidate `a5bba52d42d9b2e0f7d0e5f92cef020fc6a1d219` passed [run 37178978420](https://github.com/monocap-tech/weil-lab/actions/runs/37178978420), job `111367555930`: isolated module 9,148 jobs; full `lake build WeilDefect` 9,181 jobs. All seven public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The validation cache was saved under `rpb108-actual-prime-transport-verified-v1`. Promotion uses the exact validated source and root import; workflow and pinned dependency manifest remain validation-only.

Initial candidate `e76ea7ff0a7d4286da50865989a58fcb3cf3d7df` was superseded after making the phase domination constant and pointwise addition explicit. Candidate `18276ca726684c65613d7a2732b77e865a36b368` compiled the substantive cutoff and spectral proofs but left the established 0 < a argument as an unsupplied rewrite goal in the final theorem. The final candidate passes that existing argument explicitly. No new mathematical hypothesis was added.

## Boundary and cursor

The prime cutoff and exact prime multiplier dictionary are closed on this constructed carrier. The literal digamma term still requires its corresponding spectral dictionary and absolute-integrability proof before combining the two arithmetic terms into rightLimitCompactWeilSymbolMathlib plus the existing pole operator pairing.

Next cursor: prove the exact digamma/archimedean spectral dictionary for the already constructed inverse correlation J_a(v,w). Derive its Fourier transform = the same mixed spectrum almost everywhere from J=AE K and the certified correlation spectrum; apply the fixed r = -2πξ change of variables, prove gamma-bracket symmetry/normalization and needed absolute-integrability using the certified external special-function bounds and existing Green spectral moments. Combine this with the closed right-limit prime spectral identity and same-canonical-image pole pairing to attach the actual zero form to rightLimitCompactWeilSymbolMathlib plus pole on the existing source form. Recover retained WD-T38 coefficients/source data and prove same-vector source/null identity before transferring constructed-carrier results. No retained spectral operator-domain membership is assumed.

WD-T38 same-vector source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed Green synthesis are unproved. The zero-density reindex audit blocks inferring physical source identity from independently named density/Q fields. Retained spectral L²/operator-domain membership remains unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
