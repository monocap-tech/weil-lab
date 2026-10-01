# RPB-108 — Hermitian Gaussian cutoff bridge and scoped EXT-4 polarization

**Date:** 2026-09-30 (America/Los_Angeles)
**Recovered research base:** `94ad59e7331f7d3b6f3881e2639bfb60f493da8b`
**Status at this checkpoint:** SOURCE IMPLEMENTED ON VALIDATION BRANCH / DIRECT BUILD IN PROGRESS / FULL SOURCE-WITNESS ATTACHMENT STILL OPEN / COERCIVITY NOT STARTED.

## 1. Recovery

RPB-107 was recovered from the live research branch, including its successful exact-module run `36807944842`, job `110196386366`, and duality-audit blob `e9d4fde62ea2bbd8e7c586b134e81e58103b9085`. Its note, root import, terminology entry, and status/control updates are already present. No Gaussian seed, Fourier normalization, or cutoff construction is restarted.

The new implementation is on `validation/rpb108-hermitian-cutoff`, PR #23. Initial validation source head: `db57718d34c7e064744ba8e7b6eca21be0b6592a`. Initial run: `36813420117`, job `110213211667`. Its command is explicitly `lake build WeilDefect.Morphology.NeutralGaussianHermitianBridge`. It checks out the PR head, asserts the pinned Lean/mathlib versions, records source blobs, and audits endpoint transitive axioms. This checkpoint makes no successful-build claim.

## 2. The bilinear distribution interface remains valid

A complex distribution acts linearly on its test. There is no reason to replace the existing compact-test identity merely because it is written as

```math
\int u(x)q(x)\,dx=T_a(u)+\int u(x)p(x)\,dx.
```

To use this as a Hermitian pairing with the filtered mode `G_R`, select `u = conjugate(G_R)`. The previous unconjugated Gaussian identity remains a valid, different bilinear identity. It is not the desired Fourier energy for a general complex carrier.

The new module implements:

```text
integrable_conjugateSchwartz_mul
rightLimitWeilWeakIdentity_of_integrableSchwartz
rightLimitWeilGaussianHermitian_of_growth
```

The first transfers product integrability to the conjugated Schwartz factor by equality of pointwise norms. Measurability of the other factor is explicit and is supplied in the application by the existing residual/pole local-integrability fields.

The second extends the existing all-compact-test weak identity to any Schwartz test whose residual and pole products are integrable. It uses the already certified generic compact cutoff sequence, its Schwartz convergence, the existing dominated-convergence theorem, and continuity of the tempered multiplier core.

The third applies this general theorem to the RPB-107 conjugated moving-Gaussian test. Its conclusion contains both genuine integrability statements and the corrected weak identity. The identity is derived by the cutoff limit, not assumed as an extra Gaussian premise.

The exact compact weak witness, residual carrier, symbol premise, pole-growth carrier, and the existing large-R hypotheses remain explicit inputs. Their actual source realization is not established by this construction.

## 3. Correct complex pole pairing

Write `M_s(h) = integral h(x) exp(s*x) dx` using the compact support, and let `A=M_{-1/2}(h)`, `B=M_{1/2}(h)`. The existing named pole is

```math
p_h(x)=A e^{x/2}+B e^{-x/2}.
```

RPB-107 correctly proved the bilinear algebraic identity `integral h*p_h = 2*A*B`. The claim that this alone attaches the source's general complex quadratic pole must be qualified: it matches the real-carrier formula, but not the general Hermitian complex diagonal.

RPB-108 implements the actual Hermitian identity:

```math
\int \overline{h(x)}p_h(x)\,dx
=A\overline B+B\overline A
=2\operatorname{Re}(A\overline B).
```

The code proves the cross-moment sum; the last real-part equality is its elementary interpretation. The new declarations are `neutralWeilPoleMoment_conjugate_integral` and `neutralWeilSourcePole_hermitian_pairing_eq`.

This is consistent with the source's real-even positive pole, real-odd negative pole, and real/imaginary splitting. No theorem from RPB-107 is refuted; the correction concerns which pairing is the complex quadratic form.

## 4. Polarization: algebra versus analytic domain

The source was re-read at its exact pinned version:

- Zhu, arXiv:2608.24827v2, equations (2)-(3), sections 1.6 and 2;
- section 6.1, Lemma 6.1 and its proof;
- https://arxiv.org/html/2608.24827v2#S6.SS1

Outside section 6 the stated test convention is real and even. Lemma 6.1 supplies the arbitrary-real parity decomposition and the complex real/imaginary splitting.

The new algebraic declarations are:

```text
realSymmetricBilinear_eq_of_diagonal
realBilinearComplexification
realBilinearComplexification_eq_of_diagonal
```

For symmetric real bilinear forms on one vector space, equality of diagonals implies equality of mixed terms, by expanding the diagonal at `x+y`. The explicit antilinear-first complexification on pairs of real components then preserves that equality.

These are algebraic transfer results. They have not been instantiated with the full source form domain and the rough compact L2 carrier. They do not enlarge the space on which the diagonal identity is known.

In particular, a formula on functions supported in `[-a,a]` determines the compressed operator on that window. It does not, by polarization alone, determine an operator action against every compact test anywhere on the line. An exterior-supported correction is invisible to tests in the fixed window. The RPB-108 Gaussian cutoffs have expanding supports and eventually leave that window.

Increasing the source support parameter to cover a larger test also changes the prime set in the source symbol. Therefore an all-compact-test identity with the original fixed symbol cannot be inferred simply by applying the fixed-window formula at larger supports.

## 5. Exact remaining construction

A natural route is to define the whole-line fixed-cutoff extension explicitly:

```math
W_a^{ext}h=\Psi_a(D)h+p_h,
```

where the active prime set is frozen at the selected enlarged/right-limit radius. Then prove that its compression agrees with the polarized source form, and attach the supplied residual representative to that specific extension. Alternatively, a larger-window derivation must carry the corresponding finite-prime-shift correction explicitly.

This is a concrete source-realization task, not a reason to restart the Gaussian analysis or to add an unlabelled global identity as a premise. The existing theorem can consume the exact all-compact witness once it is supplied. The current pass has not constructed that witness.

The residual's required representation/growth fields, the form-domain inclusion of the actual carrier, the strict/equality-threshold convention, and the source-to-mathlib Fourier normalization must remain visible in that attachment. The generic complex normalization `Ck` is not automatically a positive Gaussian Fourier multiplier.

## 6. Current cursor

```text
RPB-108 / WD-T40 F-4
HERMITIAN GAUSSIAN BRIDGE: DIRECT BUILD PENDING
SCOPED POLARIZATION ALGEBRA: DIRECT BUILD PENDING
NEXT SOURCE TASK: FIXED-CUTOFF WHOLE-LINE EXTENSION + RESIDUAL WITNESS ATTACHMENT
LOGARITHMIC COERCIVITY: NOT STARTED
```

Do not label the full RPB-108 source attachment closed merely because the conditional Hermitian bridge compiles. No change is made here to the historical RPB-104/105 wrong-target correction or to the mathematical standing of WD-T40.
