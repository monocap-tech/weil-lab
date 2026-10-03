# RPB-108 — certified source-witness independence audit

Date: 2026-10-02 (America/Los_Angeles).
Recovered parent: `ec88ac9a8de20b1f7ae8e3375d9129564702eb54`.
Terminology: [source-witness independence](../docs/TERMINOLOGY_RPB108_SOURCE_WITNESS_INDEPENDENCE.md).

## Finding and scope

The source-witness independence audit is certified in `NeutralSourceWitnessAudit.lean`. The named scalar source identity accepts zero density and zero pole for any symbol and shift; all corresponding integrals are genuinely zero. Zero named density and scalar Q satisfy the existing arithmetic output. More decisively, every `NeutralDefectMorphology` can be reindexed to those zero arithmetic data while preserving the attained neutral branch, coefficient/physical carrier, physical null equation, extension map, and the exact same null-extension package (endpoint vector, operators, restrictions and proofs). Separately, L2 Fourier inversion proves that the nonzero concrete physical carrier's normalized Fourier norm-square density is not almost-everywhere zero.

Thus the named-density identification is not enforced by the current typed output. The audit does not instantiate an actual-zeta neutral branch, refute the documented mathematical carrier-identification hypothesis, or prove nonderivability of form energy or spectral L2 by every possible argument. It certifies why simply consuming the retained named-density integrability cannot be called an actual carrier attachment.

Actual carrier density/source-form-domain/quadratic identification and same-domain polarization/normalized attachment remain OPEN. Actual enlarged central cancellation remains OPEN. The certified inner-collar assembly from `ec88ac9` already derives regularity and whole compact realization once actual central cancellation is supplied, with no independent regularity premise. Spectral L2 membership remains unproved and unassumed. Threshold bookkeeping is CLOSED; F-4 logarithmic Gaussian coercivity is NOT STARTED. WD-T40/RH standing is unchanged.

## Certified declarations

- `wd_t38_zero_density_sourceIdentity`
- `wd_t38_zero_density_arithmetic`
- `NeutralDefectMorphology.zeroDensityReindex`
- `NeutralDefectMorphology.zeroDensityReindex_nullExtension`
- `neutralPhysicalFourierDensity_ne_zero`

The reindexing function carries the original physical/null fields through unchanged and replaces only the arithmetic field, Q and density. Its null-extension equality is definitional. In particular, this audit is stronger than observing that an isolated generic scalar theorem accepts zero density.

The reindexing theorem starts from an existing typed package. It does not assert that the false-RH attained branch is inhabited or construct a new actual-zeta null vector. If a retained package has an external identification law not encoded in its type, that law is not automatically transferred to the audit reindexing.

The Fourier-density result uses only the concrete physical carrier's nonzero L2 class and the certified Fourier-inversion identity. It needs neither logarithmic energy nor operator-domain spectral membership. Equality almost everywhere to zero would force the Fourier L2 class to be zero, and hence the physical mode to be zero, contradicting its existing nonzero witness.

## Consequence for witness attachment

The documented WD-T38 carrier-identification hypothesis is essential: it must be instantiated for the actual source model and carried into Lean. It cannot be replaced by the independent density/Q parameters, the logarithmic comparison conclusion, or preservation of the abstract endpoint null equation.

For the actual attachment, recover the normalized physical map and source form realization; identify the named density with the actual Fourier density and the scalar diagonal with sourceDomainQuadratic; preserve the source domain and lawful full/selected/effective synthesis relation. Only then may the existing same-domain polarization and normalized comparison bridges be consumed. Enlarged central cancellation also needs its lawful source persistence/null witness. The inner-collar theorem is ready to consume it immediately.

This audit adds no conditional representation layer or stronger premise. It does not upgrade form energy to spectral L2. It records a proved interface obstruction to one specific attachment inference, while leaving independent analytic derivations open.

## Validation

Whole-root `lake build WeilDefect` passed: **9,022 jobs**. All five audited declarations use only `propext`, `Classical.choice` and `Quot.sound`. The unfinished-declaration gate passed.

- Validation commit: `e1959d1c6858c092a7cc51511bf667b13812768e`.
- Validation tree: `ea9e54de264c48b085bb8258792008e13b6155d2`.
- Run: `37089994701`.
- Job: `111108107011`.
- Certified source blob: `cef6b6e6802491f18263132356d0a57ebbccea21`.
- Root import blob: `67e5592e0c07889cb1d5ada2c740a94b90687d88`.

The final validation dependency cache contains the complete successful root build under `rpb108-lean434-mathlib5ed296-rpb108-root-v1`. This is validation infrastructure only; no workflow change is promoted.

Promotion includes the certified module and root import, terminology, a new immutable pass note and additive current status/track/overview/provenance updates. The original research workflow is preserved; the validation workflow is excluded. Historical notes are unchanged.
