# RC214 — complete correlated difference action

Parent: RC213 `4424d4573be099cc364d99bfa60f022fbedd112d`.

RC214 certifies the complete supported canonical action on the unchanged native source δ = z_b6 − v10. The complete D-norm error is at most **0.000016312335** (outward decimal), or **10.578259%** of a certified lower bound for the native difference norm. The difference-direction sufficient half-Gram error test passes: εδ² < ||δ||D²/2. This is a one-direction action-error test, not an expanded inverse result.

## Shared source reconstruction

The validator reconstructs the balanced input and all 4096 native z coefficients through degree 8190, verifies their original RC132 hashes, and subtracts the pinned native v coefficients before applying the operator. It reproduces RC153's exact finite difference hash and RC134's finite difference energy upper bound. The full source retains RC134's combined selected analytic tail; no source is replaced by a truncated polynomial. All input certificates and imported helpers are pinned to immutable Git blob hashes.

## Complete action and error payment

For the endpoint contraction C, input coefficients through degree 4094 are applied to output degrees through 8190 using directed arithmetic. The infinite output uses 25 exact signed moments and a paid geometric remainder. Every finite difference coefficient is negative, so the absolute remainder is bounded by the next absolute moment. The endpoint trial also includes one half of the actual omitted native difference source. Since 0 ≤ C ≤ I, its omitted-input error is at most one half of that input's full D norm. No cutoff commutation is used.

The −(789/125) D⁻¹δ multiplier is retained exactly on the entire native source. The regular term uses the explicit signed degree-128 projection, its complete infinite output payment, and high-input smoothing applied to the full omitted native difference energy. Adding the endpoint and regular errors gives the reported bound.

## Compatible correlated z carrier

Define the rebuilt z trial action as the pinned RC203 v10 trial action plus the new RC214 difference trial action. Linearity gives the exact error identity e_z = e_v + e_δ. Thus its complete action error is at most **0.000034103550**, improving the old independently constructed RC211 z bound by more than **17.61 times**. The generator map from (e_v, e_δ) to (e_v, e_z) is [[1,0],[1,1]]. This identity applies to the rebuilt z trial, not to the old RC211 trial. Subsequent mixed/action matrices must rebuild their centers accordingly; merely replacing an old marginal radius would be invalid.

## Validation and scope

The certificate passes full reversed-order replay. Wrong immutable input pins are rejected before computation. Publication adds the validator, certificate, this note, and a terminology document on the current research branch, without editing historical artifacts.

The accepted RC210 six-source inverse width remains 0.436100. The eight-source inverse, augmentation/source-range obligations, odd coverage, Stage I, RH, F4, and Lean closure remain open.

Next cursor: RC215 — correlated common carrier and conditioned expanded action/residual assembly, preserving the accepted six-source result.
