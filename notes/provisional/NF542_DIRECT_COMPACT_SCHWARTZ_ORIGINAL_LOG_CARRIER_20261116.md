# NF542 — Direct compact-smooth original two-collar log-Hilbert admission, bypassing derivative L¹/L² compatibility

**2026-11-16 PT. Draft branch `research/nf542-admit-c2-collars-and-repair-lean` stacked on NF541 PR #569. New Lean compiler verdict PENDING.** Original NF494 U400 source SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, the NF523/NF528 `B=11/10`, `δ=1/500` strict support geometry, 242 original moment directions, and all authentic zeta-divisor multiplicity copies unchanged. No source replay or new arithmetic positivity certificate.

## 1. NF541 actual CI: failed, and exact repair

GitHub Actions runs [#43839737274](https://github.com/monocap-tech/weil-lab/actions/runs/43839737274) and [#43839737991](https://github.com/monocap-tech/weil-lab/actions/runs/43839737991) completed FAILURE in the inherited NF540 module. Lean reported `ActualZetaLogCarrierQuadraticMoment.lean:48:4`: after `simp only [Real.norm_eq_abs]`, the **left** absolute-value expression persisted in the `Integrable.mono'` target, while the right one had already simplified. NF542 specifically adds `rw [abs_of_nonneg (mul_nonneg hlow hnsq)]` before invoking the existing monotonic multiplication inequality. This is a source-preserving tactic fix and **requires new CI**, not an accepted proof.

## 2. Important constructive bypass: C∞ instead of an L¹/L² differentiation bridge

NF541 established analytically that each compactly supported C² test has a finite quadratic Fourier moment using its derivative. Its Lean module still explicitly assumed the a.e. L² derivative-Fourier witness, so it has not removed the hypothesis.

However the ACTUAL NF528 inward-contract-and-mollify strict two-collar approximants, together with smooth Gram bumps `χ j_j` (when `χ` and `j_j` are smooth as required), are **C_c∞**, a stronger class. Mathlib supplies the following ready-made original-function bridges:

- `HasCompactSupport.toSchwartzMap` converts a C_c∞ original physical function to a genuine Schwartz vector **with the same pointwise representative**.
- `SchwartzMap.toLp_fourier_eq` identifies the Fourier transform of this physical vector's L² class with the L² class of its genuine Schwartz Fourier transform.
- `SchwartzMap.integrable_pow_mul` and `SchwartzMap.norm_le_seminorm` provide finite weighted polynomial moments and a uniform Schwartz norm bound.

Therefore, for any original `ψ∈C_c∞(ℝ,ℂ)`, with `s=𝓕ψ ∈𝓢`, its Schwartz bound `‖s(ξ)‖≤C`, integrability of `‖s‖²`, and integrability of `‖ξ‖²‖s(ξ)‖` imply

```
∫ (e+1+ξ²) |s(ξ)|² dξ
≤ (e+1)∫ |s(ξ)|² dξ + C ∫ |ξ|²|s(ξ)| dξ < ∞.
```

By exact Schwartz-to-L² Fourier compatibility, this is exactly the NF540 quadratic Fourier moment **of the original L² class**, not of a frequency-space surrogate. If ψ vanishes outside the given physical support window, NF540 supplies `k : NeutralLogHilbertCarrier a` with `neutralLogPhysical k.val = [ψ]_{L²}`.

**Exact physical geometry** is specialized directly to

```
E = (-11/10, -11/10+1/500) ∪ (11/10-1/500, 11/10)
```

without importing unfinished NF534/NF535 modules. The generated proof asserts original physical source preservation, not an equality to a newly synthesized Green packet.

## 3. New Lean code and certification contract

New file: `WeilDefect/Arithmetic/ActualZetaLogCarrierSchwartzCompact.lean`:

1. `neutralSchwartz_quadraticFourierMoment`: polynomial moment integrability for any genuine Schwartz function, via a uniform Schwartz seminorm and integrable norm-weight bound.
2. `neutralSchwartzPhysical_quadraticFourierMoment`: transfer the exact integral to the original physical L² Fourier transform with `SchwartzMap.toLp_fourier_eq`, using an a.e. equality of representatives.
3. `neutralCompactSmoothOriginalLogHilbertCarrier`: unconditional compact-C∞ supported-log Hilbert carrier membership of the SAME original physical L² vector.
4. `neutralOriginalTwoCollarCompactSmoothLogHilbertCarrier`: direct exact two-collar `B, δ` support specialization, with no source synthesis.

A focused independent workflow `.github/workflows/nf542-schwartz-compact-log-carrier.yml` first compiles the repaired NF540 module and then this NF542 module, rejecting `sorry`, `axiom`, or `admit` placeholders. Until successful, these are proof-script CANDIDATES; no promotion to Lean PASS.

This new route removes the earlier derivative-witness premise for the C_c∞ class that is actually needed by NF528. It does not formally prove the previously stated **all C_c²** theorem inside Lean; this is a deliberate narrower, sufficient choice.

## 4. What remains

- Get a genuine compiler PASS for repaired NF540 and NF542, correcting any actual elaboration errors.
- Construct/identify the actual NF528 mollified-and-Gram-corrected approximants as C_c∞ functions within Lean, with precise endpoint collar support and exact 242 moment preservation.
- Independently certify NF527 true gamma/digamma, only the genuine n=9 prime term and both pole terms, with full 1/10 uniform coercivity.
- Compiler-certify the universal true-divisor signed full-source graph identity (NF539), genuine odd graph entry, and the actual original nonsmooth U400 endpoint carrier's complete two-source graph approximation.
- The original nonzero sign, global W_ODD_NEG, global even/odd positivity and RH remain OPEN.

**Disposition:** new unconditional ANALYTIC compact-C∞ log-domain entry route using pre-existing Mathlib Schwartz/L² bridges. Lean acceptance pending, original nonsmooth source transfer unproved.
