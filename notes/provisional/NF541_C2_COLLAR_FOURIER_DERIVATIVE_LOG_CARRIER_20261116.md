# NF541 — Genuine strict smooth collar logarithmic-domain admission via Fourier derivative

**2026-11-16 PT. DRAFT; NEW LEAN ACCEPTANCE PENDING.** Research branch `research/nf541-collar-h1-fourier-domain-bridge` is stacked on NF540 PR #568. Keep original NF494 complete U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, original NF523/NF528 two-collar geometry, original 242 selected moments, and actual true-zeta multiplicity copies unchanged. No claim of RH, W_ODD_NEG, global positivity or original endpoint-source Lean certification.

## 1. Actual NF540 compiler verdict: one local proof-script error, not a mathematical counterexample

Dedicated independent NF540 run [#43834206106](https://github.com/monocap-tech/weil-lab/actions/runs/43834206106) **FAILED** when compiling `ActualZetaLogCarrierQuadraticMoment.lean:49`: the `simp only [Real.norm_eq_abs]` step had already removed both absolute values from the inequality, making subsequent `rw [abs_of_nonneg ...]` inapplicable. NF541 removes those redundant rewrites and applies the previously present monotonic multiplication inequality directly. The original pointwise bound, finite-moment admission theorem, physical reconstruction theorem and logarithmic Fourier weight are unchanged. A NEW focused compiler check is required; do not call this Lean PASS yet.

## 2. ANALYTIC strict C² collar moment theorem (complete proof)

Let `B=11/10`, `delta=1/500` and `E=(-B,-B+delta) union (B-delta,B)`. Take any genuine physical `psi : R -> C` of class `C_c^2` with `supp psi subset E`, including every actual NF528 strict smooth two-collar corrected approximant once its representative and support conditions are established. Set `g=psi` as an a.e. physical L² class and `d=psi'/(2*pi)` as an a.e. L² class. Because `psi` and `psi'` are continuous and compactly supported, both belong to `L¹ intersection L²`.

Use the actual Fourier convention `F(psi)(xi)=integral psi(x) exp(-2*pi*i*x*xi) dx`. Integration by parts (no endpoint terms, by compact support) proves for every real `xi` that

```
F(psi')(xi) = (2*pi*i*xi) * F(psi)(xi),
F(d)(xi) = i*xi*F(psi)(xi).
```

The pointwise Fourier integrals agree almost everywhere with the corresponding **physical L² Fourier transforms**, by the `L¹ intersection L²` compatibility theorem. Hence

```
||F_L2(d)(xi)||² = xi² * ||F_L2(g)(xi)||², a.e. xi.
```

By Plancherel,

```
integral_R xi² * |F_L2(g)(xi)|² dxi
  = ||d||²_L2
  = ||psi'||²_L2 / (4*pi²).
```

Consequently, with **the original NF540 spectral weight and no replacement source**,

```
M2(g) = integral_R (e+1+xi²) * |F_L2(g)(xi)|² dxi
      = (e+1) ||psi||²_L2 + ||psi'||²_L2/(4*pi²)
      < infinity.
```

Together with `1 <= log(e+|xi|) <= e+1+xi²` and actual support, this gives a genuine `k : NeutralLogHilbertCarrier B` whose physical reconstruction equals `g` exactly AS AN L² CLASS. This proof uses neither RH, zero-height enumeration, Green-packet density, nor new source moments. It is valid for each compact smooth test, not directly for the singular original `ell_U`.

## 3. What the new Lean module actually encodes

New `WeilDefect/Arithmetic/ActualZetaLogCarrierFourierDerivativeWitness.lean` has:

1. `neutralQuadraticFourierMoment_of_derivativeWitness`: for any genuine physical L² `f,df`, the a.e. norm identity `||F(df)||²=xi²||F(f)||²` implies the full NF540 quadratic Fourier moment is integrable, by existing L² square-integrability and linearity.
2. `neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_derivativeWitness`: combines that unconditional L² calculation with the authentic supported NF540 log-Hilbert carrier theorem and exact same-source reconstruction.
3. `neutralCompactSmoothL2_hasOriginalLogHilbertCarrier_of_derivativeWitness`: constructs the exact compact-smooth a.e. physical L² representative without assuming pointwise smoothness of the quotient representative, and gives original log carrier admission **under the displayed Fourier-derivative witness premise**.

A separate `nf541-collar-fourier-derivative.yml` workflow compiles both the repaired NF540 prerequisite and the new NF541 module with pinned Lake/Mathlib, rejecting `sorry`, `admit`, `axiom`. The file's presence and no-placeholder scan do NOT certify Lean correctness. The *classical* construction of `df=psi'/(2*pi)` and `L¹/L² Fourier coincidence` above is analytic; its exact new Lean port still remains to be completed, not smuggled in as an assumed theorem.

**NF542 obligation:** formalize the `C_c²` -> normalized physical L² Fourier derivative witness using Mathlib's `Real.fourier_deriv` and `Lp` Fourier compatibility, for the actual NF535 strict endpoint collar; obtain `exists df` from C² and compact support, thereby removing the witness hypothesis in the third NF541 theorem. Then proceed to NF527 true gamma/n=9/pole one-tenth coercivity Lean certificate, NF524/NF528 full original two-source graph convergence formalization and original nonzero sign. In particular `ell_U` need not be H¹ (its log endpoint singularity prevents automatic differentiation); do not transfer the smooth-test H¹ norm identity directly to it.

## 4. Certification boundaries

- Original smooth strict-collar log-domain admission: **ANALYTIC PROOF**, with genuine Fourier normalization and same-source interpretation.
- Derivative-witness L² lemma and repaired NF540 gate: **LEAN CODE WRITTEN, NEW CI PENDING**.
- Elimination of derivative-witness premise for the actual C² `psi` inside Lean: **OPEN**.
- NF539 universal raw divisor identity compiler status: **separate pending/failure status**; no automatic promotion from this module.
- NF527 arithmetic coercivity, original `ell_U` full-graph source transfer and certified sign: **NOT Lean certified**.
- Global W_ODD_NEG and RH: **OPEN**.
