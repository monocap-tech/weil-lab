# Weil-Lab — CP027
## Original critical-line center Borwein payment without whole-circle Cauchy: exact (328/27) prefactor, and a TWO-finite-signs remaining proof interface

**Independent CP### cross-projection stack**, based on CP026 draft PR #848 → CP025 #847 → CP024 #846 → CP023 #845 → CP022 #844 → CP021 #843. The original Phase-IV signed Weil support investigation, Phase-III NF physical source numerical certification, and PI pole–prime–Gamma competition are entirely unaffected.

**Status:** The exact source original analytic inequality and pure rational majorant were independently checked. Two new original Zeta-v4.35 source modules (11 source theorem candidates plus 1 integration candidate) were committed, but **none of their proof scripts were compiled or kernel accepted**. The external pure rational preflight is NOT a Lean theorem. The two original finite Euler–Maclaurin pointwise sign inequalities are still **UNPAID**. No ordinal 53, uniqueness, signed Weil–spectral dictionary, RH, or global positivity statement follows.

### 1. What was unnecessarily hard in CP021–CP026

CP021's original `zetaRemainderBound` estimate targeted *every point of every complex radius-1/4 Cauchy circle* throughout ([149.5,150.05353]). This is precisely what is needed for **complex derivatives**, the original global phase/Hardy-(Z) monotonicity approach, and curvature analysis. It is *NOT* required to use two strict Hardy-(Z) signs and the original intermediate-value theorem to prove existence of some critical-line zeta zero inside the narrow open interval.

CP026 identified the **four** independent kernel-proof hypotheses for that zero-existence transfer: two true center-point `zetaRemainderBound` inequalities and two actual finite (A_{6,256}) signed inequalities.

The main CP027 innovation is to pay the **two source center-point Borwein hypotheses** through an independently compillable upstream-only original Lean leaf, without importing CP019's holomorphy/Cauchy proof candidates or CP021's moving-circle geometry. Once the original CP027 source proofs are truly compiled, **only two genuine finite-approximant numerical inequalities will remain** in the integration theorem. This reduces the source-level theorem premise roster; it does NOT count the two Borwein premises as kernel-paid today.

### 2. Exact genuine original Borwein factor at the centers

The original frozen `Zeta.EulerMaclaurin.ErrorBound.zetaRemainderBound` has the explicit formula, with (M=6), (N=256), (z=1/2+it),

[
\operatorname{zetaRemainderBound}(z,6,256)=
\frac{|z+13|}{\Re z+13}
\left|
\frac{B_{14}}{14!}(z)_{13}\,256^{-z-13}
\right|.
]

At the exact rational heights

[
t_L=\frac{15005352}{100000}=150.05352,\qquad
t_R=\frac{15005353}{100000}=150.05353
]

the original center has (\Re z=1/2) **exactly** and (|z|≤1/2+t<151). Thus

[
\Re z+13=\frac{27}{2},\qquad
|z+13|≤|z|+13≤164,
]

and the **sharper center-only prefactor** is

[
\boxed{
\frac{|z+13|}{\Re z+13}≤\frac{164}{27/2}=\frac{328}{27}
\approx12.148148\ldots
}.
]

The full moving-circle proof had needed the coarser (656/53\approx12.377358\ldots), because a circle point may have real part only (1/4). Source-independent 13-term original polynomial norm and complex power bounds give

[
\left|(z)_{13}\right|
\le\prod_{j=0}^{12}(151+j),\qquad
\left|256^{-z-13}\right|\le256^{-13},
\]

with genuine original Mathlib Bernoulli (B_{14}=7/6) from its rational recursive definition.

Therefore, at **both exact centers**, the original source pointwise majorant is at most

[
\boxed{
\frac{328}{27}\cdot
\frac7{6\cdot14!}\cdot
\frac{\prod_{j=0}^{12}(151+j)}{256^{13}}
=
\frac{1069402300239520471}
{3802951800684688204490109616128}
\approx2.812032222041268\cdot10^{-13}
<
\frac3{10^{13}}.
}
]

The exact fraction, (B_{14}=7/6), all point/triangle inequalities and strict margin
(approx1.8796777795873212\cdot10^{-14}) were **independently verified using only Python `fractions.Fraction` and integer arithmetic**. There is no numerical Γ, ζ, zero, mpmath, floating oracle, or uncertified zeta approximation inside this scalar proof. Explicit negative controls establish that replacing (328/27) by the overly loose 13 loses the (3\cdot10^{-13}) target, and that claiming a (2.8\cdot10^{-13}) cap is false.

### 3. Actual source theorem candidates, original upstream *only*

New `cp011_zeta_v435/CP027PointwiseBorwein.lean` imports ONLY:

- `Zeta.EulerMaclaurin.ErrorBound`;
- `Mathlib.RingTheory.Polynomial.Pochhammer`;
- `Mathlib.NumberTheory.Bernoulli`;
- `Mathlib.Analysis.SpecialFunctions.Pow.Real`.

It contains **11 genuine-source Lean theorem CANDIDATES**, with 11 exact `#print axioms` source targets:

1. source `ascPochhammer` arbitrary-order complex norm product bound;
2. exact (B_{14}=7/6) from original rational recursion;
3. original Bernoulli coefficient complex norm;
4. true two-endpoint center geometry (\Re s_t=1/2,\; |s_t|≤151);
5. sharper true center `K≤328/27`;
6. original complex-power norm bound;
7. original leading omitted term bound;
8. **exact rational** strict center cap;
9. true source `zetaRemainderBound(center(t),6,256)≤3\cdot10^{-13}` for the entire narrow interval;
10. original left source-center cap;
11. original right source-center cap.

This target has **zero** CP013–CP026 local `.olean` imports. The only compiler dependencies are the genuine published frozen original Zeta source and Mathlib v4.35. It uses no new axiom, sorry, opaque, or substitute approximation. **But no original Lean kernel has yet elaborated these tactics**; in particular the exact (B_{14}) recursion and complex-power tactics still need concrete compiler feedback.

New `cp011_zeta_v435/CP027TwoFiniteSigns.lean` separately imports the *conditional* CP026 bridge and the new independent CP027 pointwise proof leaf. Its single new theorem CANDIDATE is:

[
\boxed{
\begin{gathered}
\widetilde Z_A(t_L)+E(t_L)<0,\qquad
0<\widetilde Z_A(t_R)-E(t_R)\\
\Longrightarrow
\exists t\in(t_L,t_R)\quad
\zeta(1/2+it)=0.
\end{gathered}
}
]

The original center Borwein lemmas are offered **as source proofs**, not introduced as premises and not imported from JSON. The **two true finite-sign hypotheses remain explicitly unpaid**. This integration Lean module is not independent of CP026 (by design), and may compile only AFTER CP026 and the CP027 pointwise upstream-only leaf actually compile.

### 4. Custody, exact source checks and CI protection

Directly re-fetched and verified immutable original source Git blobs and actual theorem/API strings **5/5**:

| Frozen genuine original source | Git blob | API |
|---|---|---|
| `Zeta/EulerMaclaurin/ErrorBound.lean` | `01184af0dbfd1369e14725e02e990b016bedfe6f` | `zetaRemainderBound` |
| `Zeta/EulerMaclaurin/Continuation.lean` | `1bb01e946fa7e344497eaf7694fbecff0a714d09` | `zetaApproximant` |
| `Mathlib/NumberTheory/Bernoulli.lean` | `45d389886738789e80185fd2a6da4185727ab502` | actual rational `bernoulli` |
| `Mathlib/RingTheory/Polynomial/Pochhammer.lean` | `f3503627af3430a48c087b85b03095e84dfb2824` | `ascPochhammer_succ_eval` |
| `Mathlib/Analysis/SpecialFunctions/Pow/Real.lean` | `97c12aed7085a7fc77727567d87e508064b49a18` | `norm_cpow_eq_rpow_re_of_pos` |

New `scripts/cp027_original_center_borwein_328_over_27_source_gate.py` performs exact rational+negative control tests; checks **12/12** source theorem and actual `#print axioms` text contracts; checks true 5 original Git source SHA and key API strings; and FAILS CLOSED on a genuine `.olean` + 12 actual standard-only `#print axioms` requirement. It never labels source text or an external Python certificate as `LEAN PASS`.

Two new `[[lean_lib]]` targets are registered in the unchanged original Lean4.35 workspace. The **EXISTING** strictly label/manual source-only workflow was enriched with CP027 pointwise arithmetic and five frozen upstream source SHA checks. The **EXISTING** strictly opt-in kernel workflow was updated to compile the new upstream-only pointwise leaf **FIRST**, before the older CP021/26 source stack, then compile the CP027 two-sign integration **LAST**. This ensures that any compiler failure in the inherited CP021 chain cannot prevent a diagnostic for the new independent pointwise source theorem. All genuine compiler logs, 12 actual axiom outputs and both `.olean` artifacts are collected if the existing manual/label-only job is deliberately run.

**No new workflow file, no new ordinary push or PR-create/synchronize triggering, no opt-in label applied and no additional CP027 CI launched.** Inherited CP013/CP014 source-lineage workflows can still run automatically, as they did in CP026; the CP027 new source proof audit is separate. No claim that the original NF/IV runner backlog is fully recovered.

A local exact rational mathematical preflight receipt was created as `cp027_original_center_Borwein_exact_fraction_preflight_NOT_LEAN.json`. Its exact status is `CP027_INDEPENDENT_CENTER_ONLY_BORWEIN_FRACTION_PASS_NOT_LEAN` and it marks all pending new Lean kernels, finite signs, ordinal 53, Weil and RH as **false**.

### 5. Next mathematical/compiler interface

**CP028:** obtain a *genuine v4.35 compiler receipt* for the independent CP027 center-only Borwein source leaf and fix actual errors. Separately convert the *two CP025 external finite-approximant sign intervals* into fully source-bound Lean-checked rational/Taylor/interval certificates, not copied Python booleans or declarations of desired endpoints as new axioms.

The source zero ordinal #53, original support-independent signed Weil positivity, complete spectral ↔ prime/Gamma (3\times3) normalizations, whole-height curvature and RH remain OPEN. Narrow existence of a critical-line zero is NOT enough to identify its ordinal or to prove RH.

**No RH or signed global Weil positivity claim.**
