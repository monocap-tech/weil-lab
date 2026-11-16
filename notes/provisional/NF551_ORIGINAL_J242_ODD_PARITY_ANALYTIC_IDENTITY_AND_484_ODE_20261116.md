# NF551 — Original 242 REAL-ODD Weil parity, real-analytic local→global uniqueness, and the exact order-484 even ODE

**2026-11-16 PT. Draft stacked on NF550 #578. New Lean files, and the inherited NF546→NF550 chain, are NOT yet compiler accepted; source audits and historical successes are reported precisely. RH OPEN.**

## 1. Source and compiler custody

Unchanged original NF407 selected source JSON SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`; exact 67 positive rational oscillator frequency groups and 241 monomial source rows; the unchanged 242nd generator at index 241 is **`Real.sinh (x/2)`**, not a surrogate. Unchanged NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, original physical aperture B=11/10, strict original δ=1/500 endpoint collars E, genuine prime/zero divisor source multiplicities unchanged.

**Confirmed:**
- NF542 [#43900908980](https://github.com/monocap-tech/weil-lab/actions/runs/43900908980) LEAN PASS.
- NF543 [#43900906815](https://github.com/monocap-tech/weil-lab/actions/runs/43900906815) LEAN PASS.
- NF544 [#43942319623](https://github.com/monocap-tech/weil-lab/actions/runs/43942319623) LEAN PASS.
- NF545 repaired original 241-node list/source functions: [#43947651211](https://github.com/monocap-tech/weil-lab/actions/runs/43947651211) LEAN PASS and SOURCE SHA AUDIT PASS. The crucial repair replaces expensive full `decide` with the exact original 67-block sum using `List.length_flatMap`; no axiom/native_decide.
- NF546 original source physical L² moments: inherited [#43947651324](https://github.com/monocap-tech/weil-lab/actions/runs/43947651324) LEAN FAILURE, source SHA audit PASS. Exact failures were `dsimp made no progress`, wrong inference of compact-set `exists_bound_of_continuousOn'`, true sinh-pole/cast indicator rewrite, and omission of `hg` to NF544 terminal. **NF551 commits targeted repairs for each**: omit dsimp, explicitly prove the source physical Icc compact set, rewrite the true pole via `congrArg Complex.ofReal`, pass `hg`. Their acceptance PENDING fresh check.
- NF547, NF548, NF549 dependent CI on old source failed at NF546; source audits PASS where completed. NF550 queued / pending. Do not claim NF550 or NF551 Lean PASS.

## 2. Forgotten critical mathematical structure: original REAL-ODD tests

The physical original NF407 generators are not just continuous source moment functionals. They are REAL and ODD:

```
j_{f,k}(x) = x^k sin(2π f x)   for even k;
j_{f,k}(x) = x^k cos(2π f x)   for odd k;
j_{241}(x) = sinh(x/2).
```

In each case `j_i(-x)=-j_i(x)`. The ORIGINAL NF548 canonical cutoff is real, even and supported in two strict collars. Therefore every ACTUAL `b_i=χ j_i` is ODD; so is **every complex-linear finite synthesis** `Bχ(d)` and every Gram right inverse `R(d)` once its canonical inverse is defined.

New Lean module `WeilDefect/Arithmetic/ActualZetaOriginalJ242OddParity.lean` implements these pointwise parity theorems across ALL 242 unchanged original source indices, including both oscillator order parities and true `sinh(x/2)`. Also proves the canonical χ is real-valued as a complex function. This is substantive for the Weil original-odd test admissibility: **finite physical L² moment matching alone never implied that the correction remained odd.**

**Important subtlety:** A general complex coefficient vector d produces a **complex odd** correction, not necessarily a REAL-valued test. NF551 does not claim the complete corrected Weil source test is real without a separate conjugation-equivariance/real-data theorem. That is an explicit future obligation.

## 3. LOCAL original collar independence is EXACTLY equivalent to GLOBAL source independence

The NF550 finite-Gram gate was

```
∀d≠0, ∃x ∈ I=(2197/2000, 2199/2000):
 S_d(x)=Σ_{j<242}d_j j_j(x) ≠ 0.
```

Each genuine original source j_i is an entire real-analytic function (sin, cos, sinh, monomial). Hence every **complex-valued** finite combination `S_d : ℝ→ℂ` is real-analytic. Mathlib's actual analytic identity theorem `AnalyticOnNhd.eq_of_eventuallyEq` says that if a real-analytic function vanishes on any open real neighborhood, it vanishes on the connected whole real line.

New module `WeilDefect/Arithmetic/ActualZetaOriginalJ242AnalyticIdentity.lean` supplies Lean proof candidates:

- `neutralNF551OriginalRealGenerator_analytic`: every true NF407 selected j_i real-analytic on all ℝ.
- `neutralNF551OriginalComplexGenerator_analytic`: faithful cast into complex linear moments is real-analytic via `Complex.ofRealCLM.analyticOnNhd`.
- `neutralNF551OriginalSourceCombination_analytic`: genuine finite source combo is real-analytic via `Finset.analyticOnNhd_fun_sum`.
- `neutralNF551OriginalSourceCombination_eq_zero_of_collar_eq_zero`: **Lean real-analytic identity principle** transferring exact I-vanishing to global ℝ-vanishing.
- Define `NeutralNF551OriginalJ242GlobalIndependence`: global source formula only, with actual original selected j_i.
- `neutralNF551OriginalJ242GlobalIndependence_iff_collar`: equivalence of global original source independence and the one NF550 original E-local separation condition.
- Hence global original source independence implies strict positivity of the **fixed canonical** original Gram through the already defined NF550 weighted integral.

**Every NF551 Lean theorem still needs actual pinned compiler acceptance.** This is a precise conditional analytic transfer, not an axiom smuggling source independence.

## 4. A better certificate architecture: the single even constant-coefficient ODE

Write the genuine exact 67-frequency groups as `(f,m_f)`, and put `ω_f=2πf`. The original 242 functions are solutions of

```
L(D) y = 0,
L(D) = (D²−1/4) · ∏_{f original} (D²+ω_f²)^{m_f}.
```

Exact order:

```
2 + Σ_f 2m_f = 2+2·241=484.
```

Its 136 distinct complex characteristic-root LABELS are
`{±2πif : f original} ∪ {±1/2}`. Each oscillator root has multiplicity `m_f`; each real pole root has multiplicity one. They are pairwise distinct because all source rational frequencies are positive and distinct, π>0, imaginary roots cannot equal real ±1/2. In the associated 484-dimensional real solution space, `L` is EVEN in D, so its odd-real solution subspace has initial data exactly the 242 odd derivatives `y'(0),y'''(0),...,y^{(483)}(0)`. The original 242 REAL-ODD source functions have the correct count to be a basis of this odd solution space.

There are TWO mathematically equivalent independence routes:

**(A) Exponential-polynomial annihilators (NF545):** Expand the original generator family into `x^k exp(±iω_f x)` and `exp(±x/2)`. If a relation `S_d(x)≡0`, distinct-root exponential-polynomial uniqueness forces all polynomial coefficients at each root to vanish. For every original k, the coefficient of `x^k exp(+iω_f x)` is *exactly* `−i d_{f,k}/2` (even k sine) or `d_{f,k}/2` (odd k cosine), both nonzero multipliers. At the real `+1/2` pole root the coefficient is exactly `d_{241}/2`. Therefore every original d coefficient vanishes: global source independence follows. This is a clean source-specific analytic proof on paper.

**(B) Odd ODE initial jets:** Prove these exact 242 source functions form a fundamental system of odd solutions of the single even order-484 operator by checking their 242×242 odd-jet determinant. This is a confluent Vandermonde route; it avoids needing arbitrary sample-point arithmetic or a 242×242 numerical Gram enclosure. It still needs a formal nonzero determinant or a general distinct-root uniqueness theorem.

New exact source replay `scripts/local_replay/verify_nf551_original_J242_odd_ode_signature.py` verifies in exact rational arithmetic:
- The same NF407 source SHA and original NF500 native raw digest.
- Exact 67 original f,m blocks and 241 source monomial k rows in unchanged order, plus genuine last pole.
- Original real-odd k/sin versus k/cos convention; no substituted parity.
- Exact characteristic root count 136 with multiplicities summing to the ODE order 484.
- Unique positive oscillator-root/monomial-degree column for all 241 oscillator modes, with nonzero exact Gaussian rational coefficients `(-i/2)` or `1/2`; and exact nonzero `±1/2` pole coefficients.
- It does **NOT** claim numerical Gram positivity or an accepted Lean proof of the general exponential-polynomial theorem. Independent SHA source proof obligations remain visible.

## 5. Verification and NF552 target

New independent `.github/workflows/nf551-original-j242-odd-real-analytic.yml`: exact-source Python audit plus pinned Mathlib Lean compilation of NF545→NF551 original function/moment/canonical cutoff/integral/weighted-square/parity/analytic-continuation chain, with proof-placeholder rejection. New branch and draft PR must not merge until genuine compiler acceptance.

**Next NF552:** first fix any remaining actual compiler errors on NF546→NF551 based on source line diagnostics; then formalize one general exponential-polynomial distinct-root uniqueness theorem, use the exact diagonal oscillator/pole coefficient map to discharge **`NeutralNF551OriginalJ242GlobalIndependence`** with no premise, derive NF550 original collar separation and hence the true canonical original 242 Gram unconditional positive definiteness.

After finite Gram: genuine NF528 inward/affine mollification, original full positive/negative all-multiplicity divisor source graph convergence, NF527 gamma+prime n=9+both poles 1/10 coercivity, NF539 complete signed Weil source identity, W_ODD_NEG and RH **ALL OPEN**. An odd parity theorem and a positive Gram do not imply RH.
