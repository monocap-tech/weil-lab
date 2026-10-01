# RPB-108 — frozen compact-test extension and finite-radius correction

**Date:** 2026-09-30 (America/Los_Angeles)
**Research base:** `cd44f380b53b325fd542c5439e6e7d83299a8745`
**Effective status:** FROZEN COMPACT-TEST ACTION AND EXACT MULTIPLIER CUTOFF CORRECTION BUILD-CERTIFIED / PHYSICAL PRIME-SHELL SUPPORT THEOREM BUILD-CERTIFIED / FOURIER-PHYSICAL IDENTIFICATION AND ACTUAL EXT-4 RESIDUAL ATTACHMENT STILL OPEN / RPB-108 CONTINUES / COERCIVITY NOT STARTED.

This is a continuation of the [Hermitian bridge certificate](REFLECTED_PACKET_BRIDGE_108_CERTIFICATE_20260930.md), not a replacement for it. No Gaussian seed, Schwartz realization, or cutoff convergence proof is restarted. The [terminology supplement](../docs/TERMINOLOGY_RPB108_FROZEN_EXTENSION.md) is an additive companion to the repository registry.

## 1. Construction delivered

The new module `WeilDefect/Morphology/NeutralWeilFrozenExtension.lean` defines the selected whole-line action on compact Schwartz tests:

```math
E_a(h;u)=T_a(h)(u)+\int_{\mathbb R}u(x)p_h(x)\,dx.
```

The cutoff radius `a` stays fixed when the test support varies. Compact support of `u` is an explicit argument. `compactSchwartz_mul_locallyIntegrable` proves genuine integrability of the pole pairing; `frozenWeilCompactAction_add` proves additivity using that integrability. The action is not claimed to be a tempered distribution: the pole is allowed fixed exponential growth.

The definition does not declare a supplied residual to be this action. `frozenWeilCompactAction_represents_iff` proves that its representation by the supplied residual on every compact test is exactly the existing named-pole `RightLimitWeilWeakRealizationPremise`. That is a characterization, not a constructed source witness.

## 2. Exact change-of-cutoff correction

For `a <= b`, set

```math
S_a=\{n:\ n\text{ is a prime power},\ \log n\le 2a\},
\qquad S_{a,b}=S_b\setminus S_a.
```

The finite sets retain the project's strict-right equality-threshold convention. Lean proves their monotonicity and

```math
D_{a,b}(\xi)
=\sum_{n\in S_{a,b}}\frac{2\Lambda(n)}{\sqrt n}
 \cos(2\pi\xi\log n)
=\Psi_a^{ml}(\xi)-\Psi_b^{ml}(\xi).
```

The exact multiplier theorem is

```math
T_a(h)-T_b(h)=\mathcal F^{-1}\bigl(D_{a,b}\mathcal F h\bigr).
```

Consequently the difference of the two compact-test actions is precisely that shell multiplier evaluated on the test. The named pole cancels because it depends on the physical carrier, not the auxiliary source-window radius.

Certified declarations:

```text
rightLimitPrimePowerFinset_mono
frozenWeilPrimeShellSymbol_eq
temperedFourierMultiplier_sub
frozenWeilMultiplier_radius_correction
frozenWeilCompactAction_radius_correction
```

No equality of the two whole-line operators is assumed, and no newly activated prime is discarded silently. The pre-existing symbol temperate-growth premises remain explicit.

## 3. Physical support geometry

The module separately defines

```math
P_{a,b}h(x)=\sum_{n\in S_{a,b}}\frac{\Lambda(n)}{\sqrt n}
 \bigl(h(x-\log n)+h(x+\log n)\bigr).
```

Every shell member satisfies `log n > 2a`. When `supp h` is contained in `[-c,c]` and `c <= a`, both shifted evaluations are zero for `-a < x < a`. This gives the certified theorems

```text
frozenWeilPrimeShellPhysical_zero_on_window
frozenWeilPrimeShellPhysical_pairing_zero
```

The second theorem applies to every test supported in the old open window. Its integrand is pointwise zero, so it does not rely on assigning a default value to a nonintegrable integral.

**Important boundary:** the physical shell and the Fourier shell multiplier are defined separately. Their identification has not been proved in this Lean module. Therefore the two results above must not yet be reported as a certified source-compression equality.

The explicit next transport target is

```math
\operatorname{FM}(D_{a,b})h=P_{a,b}h,
```

with the fixed mathlib Fourier convention. It is the cosine/translation correspondence with the exact coefficient `2 Lambda/sqrt` becoming `Lambda/sqrt` for the symmetric translation pair.

## 4. Source scope

The pinned source was re-read at Zhu, arXiv:2608.24827v2, equations (2)-(3) and the compact-support truncation immediately following (3):
https://arxiv.org/html/2608.24827v2

This continuation implements the explicit finite correction required when comparing source formulas at different compact windows. It does not infer all-compact-test source realization from polarization on one fixed window.

After the Fourier/physical shell identification, source compression must still be attached on the retained form domain, and the actual residual must represent the selected frozen extension with the required regularity/growth conditions. The compact L2 carrier and finite translations alone are not used as a proof of a pointwise exponential bound. No source-domain or residual-growth hypothesis is silently discharged here.

## 5. Direct build certificate

```text
repository: monocap-tech/weil-lab
validation branch: validation/rpb108-frozen-extension
PR: 24
run: 36816700002
job: 110223216703
checked-out HEAD: 248b7e9e881324fc230a40d09ed51e93ed40abd3
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
actual command: lake build WeilDefect.Morphology.NeutralWeilFrozenExtension
result: PASS (8950 build jobs)
source blob: 9499aed94305708e559f2e8acbd63ee086f62c04
```

Runner evidence:
https://github.com/monocap-tech/weil-lab/actions/runs/36816700002/job/110223216703

The runner printed the exact source blob above and the unchanged Hermitian bridge blob `b32fc8623b6c3e69efd3c0e82019997bf76a1e92`.

All eight inspected endpoints reported exactly `[propext, Classical.choice, Quot.sound]`:

```text
compactSchwartz_mul_locallyIntegrable
frozenWeilCompactAction_add
frozenWeilCompactAction_represents_iff
frozenWeilPrimeShellSymbol_eq
frozenWeilMultiplier_radius_correction
frozenWeilCompactAction_radius_correction
frozenWeilPrimeShellPhysical_zero_on_window
frozenWeilPrimeShellPhysical_pairing_zero
```

The declaration rejection gate also passed. No `sorryAx` or project axiom appeared in those inspected dependency closures. Explicit imported hypotheses are parameters, not consequences of the axiom audit. The certificate covers this target and its transitive imports, not a separate build of the root aggregate or unrelated modules.

The initial run `36816152700` was superseded by the terminology commit. The first completed direct build, `36816257547` / job `110221892736`, exposed one unclosed Fourier-linearity step in multiplier subtraction. Commit `248b7e9e881324fc230a40d09ed51e93ed40abd3` made the composed Fourier continuous-linear map explicit and applied `map_sub`. No mathematical statement or hypothesis changed. Two deprecated-alias warnings remain nonblocking.

## 6. Live continuation

```text
RPB-108 / WD-T40 F-4 — CONTINUES
Frozen compact-test action: CERTIFIED
Exact finite-shell symbol/core correction: CERTIFIED
Physical shell vanishing on old open window: CERTIFIED
Fourier/physical shell identification: NEXT
Polarized source compression: OPEN
Actual residual representation/domain/growth attachment: OPEN
Hermitian Gaussian cutoff bridge: PREVIOUSLY CERTIFIED CONDITIONAL
Logarithmic coercivity: NOT STARTED
```

Do not mark the full EXT-4 attachment closed from the frozen action definition or from the representation equivalence. Do not restart the Gaussian constructions. Historical RPB-104/105 wrong-target claims remain superseded by RPB-106; this certificate does not retroactively change those runs.
