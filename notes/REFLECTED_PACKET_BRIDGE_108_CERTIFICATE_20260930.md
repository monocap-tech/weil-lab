# RPB-108 — verified Hermitian bridge certificate and continuation

**Date:** 2026-09-30 (America/Los_Angeles)
**Effective status:** HERMITIAN CUTOFF BRIDGE CERTIFIED FROM THE EXACT COMPACT WEAK WITNESS / REAL POLARIZATION ALGEBRA CERTIFIED / CORRECT HERMITIAN POLE PAIRING CERTIFIED / ACTUAL EXT-4 WHOLE-LINE ATTACHMENT STILL OPEN / RPB-108 CONTINUES / COERCIVITY NOT STARTED.

This final certificate supersedes only the build-pending status in the earlier [RPB-108 checkpoint](REFLECTED_PACKET_BRIDGE_108_20260930.md). Its source-scope analysis and explicit remaining obligations stand unchanged.

## Direct runner evidence

```text
repository: monocap-tech/weil-lab
validation branch: validation/rpb108-hermitian-cutoff
PR: 23
run: 36813420117
job: 110213211667
checked-out HEAD: db57718d34c7e064744ba8e7b6eca21be0b6592a
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
actual target: lake build WeilDefect.Morphology.NeutralGaussianHermitianBridge
result: PASS (8949 build jobs)
endpoint axiom inspection: PASS
declaration rejection gate: PASS
```

Runner: https://github.com/monocap-tech/weil-lab/actions/runs/36813420117/job/110213211667

The runner printed these exact source blobs:

```text
NeutralGaussianDualityAudit.lean:
e9d4fde62ea2bbd8e7c586b134e81e58103b9085

NeutralGaussianHermitianBridge.lean:
b32fc8623b6c3e69efd3c0e82019997bf76a1e92
```

The new module passed on its first direct attempt. Its only new warning was an unused `norm_mul` simp argument; no proof repair or hypothesis change was necessary.

The eight inspected endpoints each printed exactly `[propext, Classical.choice, Quot.sound]`:

```text
realSymmetricBilinear_eq_of_diagonal
realBilinearComplexification_eq_of_diagonal
conjugateSchwartz_apply
integrable_conjugateSchwartz_mul
rightLimitWeilWeakIdentity_of_integrableSchwartz
rightLimitWeilGaussianHermitian_of_growth
neutralWeilPoleMoment_conjugate_integral
neutralWeilSourcePole_hermitian_pairing_eq
```

There is no `sorryAx` or project axiom in these inspected dependency closures. Imported hypotheses remain explicit parameters and are not established by this axiom audit. Certification covers the named module and its transitive imports, not an independent build of every unrelated root module.

## Delivered endpoint

For `G_R = movingGaussianFilteredMode`, the new theorem proves genuine residual/pole integrability and

```math
\int \overline{G_R(x)}q(x)\,dx
=T_a(\overline{G_R})+\int\overline{G_R(x)}p(x)\,dx.
```

This is derived using the existing compact cutoff sequence and ordinary-integral convergence. The bilinear distribution interface is retained; the test is correctly conjugated. The theorem is `LEAN-CERTIFIED-FROM-IMPORTED-PREMISE` with respect to the exact all-compact-test witness `RightLimitWeilWeakRealizationPremise`, the symbol premise, and the explicitly supplied carriers/hypotheses.

The correct pole diagonal for complex carriers is also certified:

```math
\int \overline{h(x)}p_h(x)\,dx
=M_{-1/2}(h)\overline{M_{1/2}(h)}
 +M_{1/2}(h)\overline{M_{-1/2}(h)}.
```

The RPB-107 unconjugated identity is still correct as a bilinear identity, but it is not the general complex Hermitian quadratic diagonal.

## What remains open

The polarization theorems determine mixed terms on their given real vector space and transport equality to the explicitly defined complexification. They have not been instantiated with the entire source form-domain/residual realization. Polarization does not expand a fixed compact support window.

The exact remaining source task is to define the selected fixed-cutoff whole-line extension, show that its compression matches the source's polarized compact-window form, and identify the supplied residual with that extension. Any route through larger source windows must retain the finite-prime-shift correction rather than silently keeping the old symbol. No noncompact identity, actual residual-growth realization, or positive Gaussian normalization is silently assumed in this attachment.

The certified Gaussian seed, Schwartz realization, generic cutoff topology theorem, ordinary-integral limit theorems, and the new conjugated cutoff bridge must not be rebuilt from scratch.

## Live cursor

```text
RPB-108 / WD-T40 F-4
HERMITIAN GAUSSIAN CUTOFF BRIDGE: CERTIFIED CONDITIONAL
SCOPED POLARIZATION ALGEBRA: CERTIFIED
CONTINUE: FROZEN-CUTOFF EXT-4 EXTENSION + ACTUAL RESIDUAL WITNESS ATTACHMENT
LOGARITHMIC COERCIVITY: NOT STARTED
```

RPB-108 is not marked fully closed because its requested source-operator attachment is not yet discharged. The original wrong-target RPB-104/105 run claims remain superseded by RPB-106, not retroactively repaired.
