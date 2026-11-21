# Weil-Lab — CP021
## Break the uncompiled CP013–CP020 dependency chain: upstream-only original Zeta v4.35 kernel leaves

**Independent CP### track, stacked on CP020 PR #842 → CP019 #840 → CP018 #839 → CP017 #838 → CP016 #837 → CP015 #836 → CP014 #831 → CP013 #829, etc.** Original **IV###** support-extension/signed-Weil compiler, original **NF###** numerical matrix certificate backlog, and independent **PI###** pole/prime/Gamma compatibility work remain unchanged. **NO RH/global signed Weil positivity or spectral 3×3 form equivalence claim.**

### 1. The honest starting failure mode: advancing source ahead of compiled custody

The original signed Weil support/certificate programs run independently. The CP013/CP014 original source-verification workflow runs on CP020's head were STILL **queued** on GitHub, not passed. GitHub commit workflow query returned:
- CP013 genuine source-lineage run `44877396195`: QUEUED on CP020 head at inspection;
- CP014 source/finite-rank run `44877396230`: QUEUED on CP020 head at inspection.
No CP020 new original Lean compiler or `.olean` passed. In the current local environment, neither `lean` nor `lake` executable is installed and outbound network DNS access to fetch a Lean compiler failed. Consequently **an actual original external v4.35 kernel test cannot be truthfully claimed here**. Three prior CP020 source modules contain new lean proof candidates and their actual import graph is source-level; it is not enough to discover their theorem names or original source Git SHA to certify them.

The CP020 strict kernel audit had **15 separate NEW prior CP013–CP019 `.olean` prerequisites** plus 3 new CP020 artifacts and 17 actual standard-only axiom receipts. One mathematical leaf theorem was therefore blocked by unrelated massive source work. That is a **verification scheduling/dependency problem**, not a mathematical requirement.

### 2. New concrete repair: two truly independent original source leaves

**New `CP021BorweinLeaf.lean`** directly imports ONLY authentic published `Zeta.EulerMaclaurin.ErrorBound` and genuine frozen Mathlib `RingTheory.Polynomial.Pochhammer`, `NumberTheory.Bernoulli` and `Analysis.SpecialFunctions.Pow.Real`. It copies and isolates **10** proof-candidate theorem statements/their tactics from CP020 without ANY CP011–CP020 import:

1. arbitrary-n source `ascPochhammer` product norm inequality,
2. genuine rational (B_{14}=7/6),
3. actual original Bernoulli coefficient complex norm,
4. nonnegative 13-factor majorant,
5. full actual moving Cauchy circle complex geometry,
6. source original (K(z)\le656/53),
7. original complex `256^(-z-13)` norm ≤ `256^-13`,
8. omitted `B14/14!×(z)_{13}×256^{-z-13}` norm,
9. exact rational final bound,
10. **original `zetaRemainderBound(z,6,256)≤3/10^{13}` for EVERY (t∈[149.5,150.05353]), every (z) with (|z-(1/2+it)|=1/4)**.

The final theorem has **NO** additional `hBorweinOnCircle` premise; it is the genuine mathematical source result the CP019 Cauchy transfer requires. The proof is still a NEW original Lean **SOURCE CANDIDATE**, not kernel accepted. A real compiler might expose tactic/type errors, particularly in the exact `bernoulli 14` normalization, `Complex.norm_cpow_eq_rpow_re_of_pos`, `Finset` norm product, or positivity step. They will require real compiler logs rather than presumed PASS.

**New `CP021GermLeaf.lean`** directly imports ONLY published `Zeta.EulerMaclaurin.Continuation` and `Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas`. It isolates **3** new source-candidate theorems without numerical or CP dependencies:
- original `ζ(s)-A_{6,256}(s)=R_{6,256}(s)` as equality of functions on a genuine open complex neighborhood of each (Re s>-13), (s\ne1),
- exact equality of **every** iterated complex derivative `D^k(ζ-A)=D^k(R)` from original `Filter.EventuallyEq.iteratedDeriv_eq`, **not** by differentiating a real-axis error inequality,
- exact nonpole and domain proof for every (s_t=1/2+it).

The true new compiler dependency is now only

```
Published original Zeta@c06b4e + genuine Mathlib@v4.35.0
    ├── CP021BorweinLeaf.lean [10 independent source candidates]
    └── CP021GermLeaf.lean    [ 3 independent source candidates]
```

**Zero CP013–CP020 local `.olean` files are required by these two targets.** Some original published Zeta package compilation and original Mathlib caches are still required, which the opt-in workflow permits. This reduces the *new local* compile frontier from **18 pending `.olean` modules to 2**.

### 3. Exact mathematical content is unchanged

For (M=6,N=256), (r=1/4), (t∈[149.5,150.05353]), every complex circle point satisfies (Re z≥1/4, |z|<151). Original (B_{14}=7/6), source 13-factor Pochhammer norms, source complex power and original Borwein prefactor yield

[
\boxed{
\operatorname{zetaRemainderBound}(z,6,256)
\le\frac{181596617021805363}{
633825300114114700748351602688
}<3\times10^{-13}.
}
]

The original published Euler–Maclaurin function identity and Mathlib germ derivative invariance give

[
D^k(\zeta-A_{6,256})(s)=D^k R_{6,256}(s)
]

for all (k) in its actual open domain. Consequently, **IF CP021's genuine independent Lean leaf theorems and the original complex holomorphy+Cauchy source bridge gain accepted kernel receipts**, the uniform complex original (zeta-A_{6,256}) error budgets are

| k | uniform complex derivative error |
|---:|---:|
| 0 | (3\times10^{-13}) |
| 1 | (1.2\times10^{-12}) |
| 2 | (9.6\times10^{-12}) |
| 3 | (1.152\times10^{-10}) |

CP021 does **NOT** independently reprove holomorphic Cauchy integral estimates in its two leaf modules; the published Mathlib theorem and CP019 source holomorphy/Cauchy bridge remain a distinct integration dependency. Two upstream-only leaves cover precisely the source all-circle numerical bound and exact original derivative germ invariance.

An exact rational arithmetic check was independently run locally: `B14=7/6` via recurrence, exact original fraction `181596617021805363/633825300114114700748351602688`, and all four k=0–3 Cauchy caps match prior calculations. This local arithmetic verification is **not original Lean kernel acceptance**.

### 4. Five genuine frozen source API pins and strict fail-closed custody

Directly re-fetched all FIVE genuine frozen source files, independently checking immutable Git blob IDs and actual advertised source declarations:

| Source | Git blob SHA | Published theorem or definition |
|---|---|---|
| Original Zeta `Zeta/EulerMaclaurin/Continuation.lean` | `1bb01e946fa7e344497eaf7694fbecff0a714d09` | `riemannZeta_eq_approximant_add_remainder` |
| Original Zeta `Zeta/EulerMaclaurin/ErrorBound.lean` | `01184af0dbfd1369e14725e02e990b016bedfe6f` | `norm_zetaRemainder_le` |
| Original Mathlib `Mathlib/RingTheory/Polynomial/Pochhammer.lean` | `f3503627af3430a48c087b85b03095e84dfb2824` | `ascPochhammer_succ_eval` |
| Original Mathlib `Mathlib/NumberTheory/Bernoulli.lean` | `45d389886738789e80185fd2a6da4185727ab502` | exact rational `bernoulli` |
| Original Mathlib `Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean` | `d9348833bece1297dd8ffe57e6b976fcc268af38` | `Filter.EventuallyEq.iteratedDeriv_eq` |

Exact source-level check from connected GitHub results: **13/13 new theorem declarations matched the 13 `#print axioms` instructions and the new auditor target names**, and both new leaf modules have **zero local CP imports**, importing only original Zeta/Mathlib modules. NO actual new kernel receipt.

The new `scripts/cp021_independent_leaf_v435_source_kernel_gate.py` separates 4 gates:

1. `--self-test`: exact independent `fractions.Fraction` Bernstein/Bernoulli/Pochhammer arithmetic and deliberate too-tight negative bound controls.
2. `--source-check`: inspect BOTH leaf sources to confirm only original upstream imports, no `sorry`, new `axiom`/opaque/constant declarations, exactly 13 theorem and `#print axioms` source contracts.
3. `--original-zeta <source> --original-mathlib <source>`: FIVE true immutable published Git blob SHA + signature checks.
4. `--kernel-audit`: FAIL-CLOSED: requires actual external original Lean4.35 `CP021BorweinLeaf.olean` and `CP021GermLeaf.olean`, source SHAs, **13 actual** standard-only axiom log receipts, no `sorryAx` or compiler errors, and original toolchain pin. Only then emits `CP021_GENUINE_UPSTREAM_ONLY_ORIGINAL_ZETA435_LEAF_KERNEL_PASS`.

The previous CP020 full chain was an ambitious but expensive compiler gate; CP021's leaf gate is a **strictly smaller, independently falsifiable** alternative and DOES NOT relabel any queued old CI job as passed.

Two opt-in only workflows, ZERO automatic ordinary push or PR creation/synchronize jobs:
- `cp021-leaf-source` → exact arithmetic + five source SHAs + 13 theorem/axiom source import checks (NOT LEAN);
- `cp021-leaf-lean` → genuine original external v4.35 source pin, Mathlib cache, **build only the TWO new leaf targets**, actual 13 standard-only axiom audit (if intentionally dispatched). No label applied, no workflow launched in CP021. Protects queued NF###/IV### runner capacity.

### 5. The exact remaining compiler and analytic tasks

**Immediate independently checkable CP022 compiler path:** run just the opt-in CP021 two-leaf original v4.35 kernel once runner capacity permits and repair the **first actual error**, not speculate. This is much smaller than the inherited CP013–CP020 compilation.

**Remaining NEW mathematical/analytic work:** real original complex holomorphy/Cauchy integration, genuine validated original finite (A_{6,256}) derivative balls across complete intervals, source-compatible digamma/theta phase balls, true Hardy-(Z) endpoint derivative (Z'(149.5)≥12/5), uniform curvature (|Z''|≤4), independent CP010 real root sign existence in ((150.05352,150.05353)), CP016 source-defined ordinal 53 attachment, original Weil signed form to normalized complete zero-side 3×3 compatibility. None of these follows from an isolated complex zeta remainder leaf theorem alone.

**Source provenance preservation law:** Equality of holomorphic functions on an open complex neighborhood transports **all local derivatives**. Uniform complex-neighborhood norm bounds transport derivatives through Cauchy estimates; real-axis value-only error bounds do **not**. The numerical original Weil cross-projection requires further prime/phase/mass normalization and is NOT implied by this carrier.

**NO global Weil positivity or RH claim.**
