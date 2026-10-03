# RPB-108 — retained WD-T38 arithmetic energy custody

Continues from `c968341ec2655ae5b68d597a6d6d46122524fa64`.

This pass repairs witness erasure in the existing WD-T38 adapter, without adding a representation layer or a new premise. `NeutralArithmeticMorphology` now retains its supplied `densityIntegrable` and `logEnergyIntegrable` proof fields. `wd_t38_neutral_arithmetic_morphology` fills them with its existing `hdensity_int` and `hlog_int` inputs. The unchanged-input attained-neutral constructor carries these proofs through the existing arithmetic field of `NeutralDefectMorphology`.

These retained proofs concern the constructor's named density. They do not identify it with the actual physical carrier's normalized Fourier norm-square density. They do not attach the independent Q/symbol/pole scalar identity to sourceDomainQuadratic, or identify the selected/effective P with the full geometric source form. Actual source witness attachment, same-domain source polarization/normalized estimate attachment, enlarged central cancellation, actual locally integrable defect representation and whole compact realization remain open.

Model recovery checked canonical `monocap-tech/weil` main head `b019d40205680f9761a4b0a80cbcad56ee1b606b`: all 43 Lean modules are already present in the lab, with identical module blobs before this repair. The original Neutral source blob is `5f20024f9d8d6567584f838478dca071848a7618`. The WD-T38 synthesis parameters remain generic; the concrete WD-T38 application, physical density normalization and background/effective-positive instance were not recovered from that inspected tree. This is a scoped inspection of canonical main, not a claim about every historical branch.

The next mathematical attachment task is the actual source form-space realization and its map into physical L2. The repaired retained finite-energy proof can then be consumed, rather than reconstructed from a stronger spectral assumption. A new assumed source-identification field would not resolve that task.

Spectral-product L2 membership remains unproved and is not assumed. One-logarithm energy is not silently upgraded to squared-symbol L2. Threshold bookkeeping remains closed; logarithmic Gaussian coercivity has not started.

Certification: whole-root `lake build WeilDefect` passed under Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`: 9,020 build jobs. All four retained-field/constructor audits use only `propext`, `Classical.choice`, and `Quot.sound`; unfinished-declaration gate passed. Validation head `53e6ac21137286efe6e1c72cfdea0539e3c31712`, run `37085401789`, job `111094526098`, source blob `4dc461eb06a2839d6e181958f623ede3e21818be`.

Audited endpoints:

- `NeutralArithmeticMorphology.densityIntegrable`
- `NeutralArithmeticMorphology.logEnergyIntegrable`
- `wd_t38_neutral_arithmetic_morphology`
- `wd_t38_attained_unit_gain_neutral_morphology`

The attained-neutral constructor's source text and input signature are unchanged; the arithmetic result type is strengthened with the two original proofs. The whole-root build checks all current imports after that strengthening.

Validation-only workflow changes are excluded. The original research workflow remains unchanged. Historical note bodies and canonical/WD-T40 standing remain unchanged.
