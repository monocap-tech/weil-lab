# RPB-108 — Fourier/physical prime-shell identification and internal compression

**Date:** 2026-09-30 (America/Los_Angeles)
**Research base:** `5945dba27f16c5c20ae18722b0fa58eae7291ef1`
**Effective status:** FOURIER/PHYSICAL FINITE-SHELL PAIRING IDENTITY BUILD-CERTIFIED / GENUINE PAIRING INTEGRABILITY CERTIFIED / INTERNAL FROZEN-ACTION COMPRESSION EQUALITY CERTIFIED / EXTERNAL SOURCE-FORM AND ACTUAL RESIDUAL ATTACHMENT STILL OPEN / RPB-108 CONTINUES / COERCIVITY NOT STARTED.

This continues the [frozen-extension certificate](REFLECTED_PACKET_BRIDGE_108_FROZEN_EXTENSION_20260930.md). The Gaussian seed, moving-mode Schwartz realization, generic cutoffs, and Hermitian cutoff bridge are unchanged.

## 1. Exact connection closed

The new module is:

```text
WeilDefect/Morphology/NeutralWeilPrimeShellTranslation.lean
```

For the finite shell `S_{a,b} = S_b \ S_a` already defined in the frozen-extension module, write

```math
D_{a,b}(\xi)=\sum_{n\in S_{a,b}}\frac{2\Lambda(n)}{\sqrt n}
  \cos(2\pi\xi\log n),
```

and

```math
P_{a,b}h(x)=\sum_{n\in S_{a,b}}\frac{\Lambda(n)}{\sqrt n}
  \bigl(h(x-\log n)+h(x+\log n)\bigr).
```

The endpoint

```lean
frozenWeilPrimeShell_fourier_physical_pairing
```

proves, for every complex Schwartz test `u`,

```math
\bigl[\operatorname{FM}(D_{a,b})h\bigr](u)
=\int_{\mathbb R}u(x)P_{a,b}h(x)\,dx.
```

The companion `frozenWeilPrimeShell_pairing_integrable` proves genuine integrability of the ordinary integral. This is a weak/distributional identification on all Schwartz tests; it is not a claim that a distribution is pointwise equal to a function by definition. No compact-support restriction is imposed on `u` for this identification, and no differentiability of `carrier.h` is assumed.

## 2. Proof mechanism and normalization

The inverse-Fourier translation formula is derived from the pinned mathlib API, using its `exp(-2*pi*i*x*xi)` forward convention. The exact cosine identity then gives the half-sum of opposite translations on Schwartz tests. This half-factor converts `compactWindowPrimeCoefficient = 2*Lambda/sqrt` to the physical coefficient `Lambda/sqrt`; no normalization factor is suppressed.

The distributional multiplier acts by transposition on the test. The proof therefore differentiates neither the physical carrier nor a chosen representative of it. It uses:

```text
inverseFourier_sub_const
schwartz_inverseFourier_sub_const
cosine_eq_fourierChar_pair
schwartz_cosineMultiplier_transpose
neutralPhysical_temperedMode_apply
neutralPhysical_shift_pairing_integrable
neutralPhysical_shift_pairing
cosineFourierMultiplier_physical_pairing
```

Evaluation of `carrier.temperedMode` is explicitly transported to the actual representative `carrier.h` using the certified a.e. equality of its L2 class. Schwartz tests lie in L2, so Holder integrability supplies every translated product. Translation-invariance of the integral transfers the shift from the test to the carrier. The finite shell is then summed using the integrability of every weighted term.

## 3. Internal compression equality

The prior pass separately established the radius-correction multiplier and the physical support geometry. They are now connected by the new identification.

The theorem

```lean
frozenWeilCompactAction_compression_eq
```

proves

```math
E_a(h;u)=E_b(h;u)
```

whenever `c <= a <= b`, both symbol temperate-growth premises are supplied, and `u` is compactly supported with `support u` contained in the old open window `(-a,a)`.

Indeed, the previously certified difference is the shell multiplier. The new theorem identifies it with the physical shell pairing, and the already certified shell support theorem makes that pairing zero. This establishes equality between the two internally defined frozen actions on that window. It does not assert that their whole-line actions are equal. The strict-right prime-set convention, including equality thresholds, is unchanged.

## 4. Source boundary retained

Internal compression invariance is not yet the attachment of those actions to the externally pinned quadratic Weil form. The scoped polarization results must still be instantiated on the retained source form domain, including the actual compact L2 carrier where applicable. The supplied residual must then be identified with the selected frozen extension, with its representation, local integrability, growth, and central vanishing requirements justified rather than postulated implicitly.

In particular, neither `frozenWeilCompactAction_represents_iff` nor the new compression equality constructs the missing `RightLimitWeilWeakRealizationPremise`. No new all-compact-test witness, source-domain inclusion, exponential residual bound, or positive Gaussian normalization is claimed by this pass.

The formerly separate Fourier and physical shell objects no longer constitute a missing connection. The next task is the actual source-form/residual attachment, not another cosine/translation reconstruction.

## 5. Direct build certificate

```text
repository: monocap-tech/weil-lab
validation branch: validation/rpb108-prime-shell-translation
PR: 25
run: 36818895703
job: 110229945734
checked-out HEAD: bf38f197440a0fd1ea11b699813547672dad3b34
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
actual target: lake build WeilDefect.Morphology.NeutralWeilPrimeShellTranslation
result: PASS (8951 build-graph jobs)
source blob: 628f979cb0e7b33d22c1a1144ae9e5c25560d257
unchanged frozen-extension blob: 9499aed94305708e559f2e8acbd63ee086f62c04
```

Runner evidence:
https://github.com/monocap-tech/weil-lab/actions/runs/36818895703/job/110229945734

The checked-out SHA, Lean/mathlib pins, exact target, and source blobs were read from the completed runner log. The new target built without a new warning. Existing dependency linter warnings remain nonblocking.

All nine inspected endpoints reported exactly `[propext, Classical.choice, Quot.sound]`:

```text
inverseFourier_sub_const
cosine_eq_fourierChar_pair
schwartz_cosineMultiplier_transpose
neutralPhysical_temperedMode_apply
neutralPhysical_shift_pairing_integrable
cosineFourierMultiplier_physical_pairing
frozenWeilPrimeShell_fourier_physical_pairing
frozenWeilPrimeShell_pairing_integrable
frozenWeilCompactAction_compression_eq
```

The declaration-rejection gate also passed. No `sorryAx` or project axiom appears in these inspected dependency closures. Explicit hypotheses remain theorem parameters, not conclusions of the axiom inspection. The certificate covers this module and its transitive imports, not an independent build of unrelated root modules.

### Repair history

The first direct run `36817865664` / job `110226768777` failed on a backwards cosine-coercion rewrite, an unavailable subtraction alias, and the pointwise-versus-function-valued finite-sum form. Commit `7bbcd2bb6b85d0e0012e1d7912c8bad550406261` repaired those proof-script issues.

The second run `36818284808` / job `110228064330` accepted the translation/cosine transport but exposed a remaining pointwise-function-addition simplification and an omitted explicit finite-set argument to `integral_finsetSum`. Commit `bf38f197440a0fd1ea11b699813547672dad3b34` repaired those two details. No theorem statement or hypothesis changed in either repair.

The earlier failed runs remain failed history. This certificate does not retroactively alter them or the older RPB-104/105 wrong-target records.

## 6. Live continuation

```text
RPB-108 / WD-T40 F-4 — CONTINUES
Fourier/physical finite-prime-shell identification: CERTIFIED
Integrability of physical shell pairings: CERTIFIED
Internal frozen-action compression equality: CERTIFIED
NEXT: SOURCE FORM-DOMAIN / POLARIZED COMPRESSION ATTACHMENT
THEN: ACTUAL RESIDUAL REPRESENTATION WITH RETAINED DOMAIN/GROWTH CONDITIONS
Hermitian Gaussian cutoff bridge: PREVIOUSLY CERTIFIED CONDITIONAL
Logarithmic coercivity: NOT STARTED
```
