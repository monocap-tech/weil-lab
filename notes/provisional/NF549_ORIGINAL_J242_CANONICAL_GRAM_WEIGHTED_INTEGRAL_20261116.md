# NF549 — Original source J242 canonical weighted Gram is a TRUE physical L² integral and quadratic pairing

**2026-11-16 PT. Research increment stacked on NF548 draft #576; new Lean compilation PENDING. Do not promote as accepted formal theorem without actual green receipts.**

## 0. Custody / exact source

Original NF407 `notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json` SHA256 **`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`**, unchanged. It contains exact 67 distinct positive rational oscillator frequency groups, 241 actual monomial sine/cosine directions, and true index-241 `sinh(x/2)` pole. Original NF494 U400 SHA256 **`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`**, untouched. Original B=11/10, delta=1/500, two strict terminal collars and all true source divisisor multiplicities unchanged. No surrogate polynomial family or root set.

## 1. Compiler recovery: actual new receipts

Latest NF547-head [NF544 focused run #43942319623](https://github.com/monocap-tech/weil-lab/actions/runs/43942319623) **LEAN SUCCESS** after correcting the pinned Mathlib v4.34.0 `Module.Basis.constr_apply_fintype` namespace. NF547 [original SHA-pinned source audit in run #43942322940](https://github.com/monocap-tech/weil-lab/actions/runs/43942322940) **SOURCE AUDIT SUCCESS**. NF545 source SHA auditor in [#43942320522](https://github.com/monocap-tech/weil-lab/actions/runs/43942320522) **PASS**; its Lean job failed at `ActualZetaOriginalJ242SourceFunctions.lean:27:2` because the kernel `decide` check of full `List.flatMap` generator-node expansion hit the default `maxRecDepth`. The exact rational frequency signature list itself compiled; **this is NOT mathematical counterevidence about 241 nodes**. NF548's [#43944122678](https://github.com/monocap-tech/weil-lab/actions/runs/43944122678) source-audit job **PASS**; canonical-cutoff Lean job still in progress / pending at time of writing.

NF549 sets `maxRecDepth 8192` exclusively around that true 241-node-length theorem and uses the Lean KERNEL `decide +kernel`, not `native_decide` or any new axiom. This repairs the known failure only if a fresh compiler run accepts it. Failing to compile should result in a new diagnostic and repair, not a false PASS.

## 2. New source-specific integral bridge, not merely algebraic Gram notation

New Lean module `WeilDefect/Arithmetic/ActualZetaOriginalCanonicalGramPhysicalIntegral.lean` tackles the exact missing interface from the true physical source to the fixed original 242 weighted integral.

Recall the ORIGINAL full-window source functions

```
j_i(x) = (source NF407 x^k sin(2π f x), x^k cos(2π f x), or sinh(x/2)),
J_i(x) = 1_{[-11/10,11/10]}(x) · j_i(x),
M_original(f)_i = ⟪[J_i]_{L²}, f⟫_ℂ.
```

Let `χ(x)=u(2000(x−1099/1000))+u(2000(x+1099/1000))` be the **one actual** real even positive Mathlib smooth flat bump from NF548, supported strictly inside original E. Let `b_j=χj_j∈𝓢(ℝ,ℂ)` and `Bχ(c)=∑ c_j b_j`.

### Formal source identities submitted

1. **Actual selected physical moment integral.** For every `i<242` and Schwartz `s`, the new theorem identifies

```
M_original(s.toLp)_i =
    ∫_ℝ conj(J_i(x)) · s(x) dx.
```

The Lean proof explicitly uses `MeasureTheory.L2.inner_def`, the **honest a.e. equality** of NF546's physical indicator L² class and the unchanged original source function, and Mathlib's Schwartz `coeFn_toLp`. It does NOT falsely identify an arbitrary L² equivalence class pointwise.

2. **TRUE canonical Gram entry.** For every `d∈ℂ^242, i<242`,

```
G_548(d)_i =
   ∫_ℝ conj(J_i(x)) · Bχ(d)(x) dx.
```

This is EXACT original continuous physical (L²) integration, not selected abscissas, six-polynomial controls, quadrature or interpolated Green packets.

3. **ACTUAL canonical synthesis.** Pointwise,

```
Bχ(d)(x) = χ(x) · ∑_{j<242} d_j j_j(x).
```

This follows from `Module.Basis.constr_apply_fintype` and the exact NF547 weighted-source Schwartz constructor. It is an identity for the **one canonical original χ and unchanged original j_i**, not a free list of columns.

4. **TRUE original weighted integral.**

```
G_548(d)_i =
  ∫_ℝ conj(J_i(x)) χ(x)
       (∑_{j<242} d_j j_j(x)) dx.
```

This settles the exact source-identity side of the NF548 canonical physical Gram conditional on compiler acceptance; the full [-B,B]-window is respected and χ is supported in the strict original E.

5. **True source Hermitian quadratic as L² pairing.** Define `V(d)=∑_{i<242}d_i[J_i]_{L²}` from the original selected physical J_i. Prove

```
∑_{i<242} conj(d_i) G_548(d)_i
   = ⟪V(d), [Bχ(d)]_{L²}⟫_ℂ .
```

Again no independent moment map, test columns, or χ variable occurs.

**Status:** All five are Lean SOURCE PROOF CANDIDATES awaiting explicit Actions acceptance. Do not report them as accepted Lean results until verified.

## 3. Mathematical reduction now maximally concrete

Because χ is supported strictly within [-B,B] and is nonnegative real,

```
  ⟪V(d), [Bχ(d)]_{L²}⟫_ℂ
    = ∫_ℝ χ(x)|∑_{j<242}d_j j_j(x)|² dx.
```

The analytic strict positivity follows from the original 136 distinct exponential-polynomial roots and real-analytic independence established in NF545: if d≠0 the original selected source combination cannot vanish on any nonempty open subinterval; χ is positive on one such interval. Hence the integral is >0.

**The last display and strict positivity are NOT yet Lean-certified.** NF549's source integral is a required bridge for these final two steps, but does not smuggle the analytic independence into Lean or assume the RH sign certificate. The original real odd symmetry of source χj columns remains mathematically clear, but a dedicated Lean proof of parity is a separate obligation.

## 4. Verification

A new `.github/workflows/nf549-original-gram-physical-integral.yml` checks original source Python exact SHA/242-node audit and pinned Lean build for NF545 actual source functions, NF546 physical moments, NF548 actual even cutoff, NF548 canonical inverse, and NF549 weighted original physical integral plus Hermitian pairing. It rejects `sorry`, `admit`, and `axiom`.

## 5. Strict NF550 promotion gates

- First obtain actual compiler PASS for the inherited NF545 full-node theorem, NF546 real full-window L² moment CLM, NF547 exact weighted Schwartz columns, NF548 explicit χ and NF549 integral identities. Repair any failing proof before promotion.
- Formalize the **real χ / original window cancellation** on its exact collar support and derive `⟪V(d),Bχ(d)⟫=∫χ|Σd_jj_j|²` in Lean.
- Formalize source-specific 136-root exponential-polynomial uniqueness on open real intervals, then deduce positive definiteness for the one canonical original G.
- Use resulting original finite Gram inverse with actual NF528 smooth inward-affine-mollified `g_s` and prove all-multiplicity two-source P/N graph convergence to original `ell_U`. The existence and source convergence of g_s do not follow just from the finite-dimensional Gram algebra.
- Independently prove full NF527 true gamma+n9+both poles `1/10` coercivity and NF539 original complete mixed signed identity in Lean.

**Disposition:** NF549 commits the actual continuum source integral and Hermitian pairing bridge as compiler-pending source, plus a focused correction to the original generator list's recursion-depth proof. NF542/NF543, NF544 have real historical Lean passes; NF545 list and NF548/549 are pending. Original signed certificate / W_ODD_NEG / RH remain OPEN.
