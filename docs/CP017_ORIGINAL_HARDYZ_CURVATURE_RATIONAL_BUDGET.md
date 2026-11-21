# Weil-Lab — CP017
## Exact rational Hardy-Z derivative/curvature budget for numerical ordinal-53 attachment

**Scope:** Independent CP### cross-projection research branch, stacked CP016 PR #837 → CP015 #836 → CP014 #831 → CP013 #829 → CP012 #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. No mutation of original IV### signed Weil support-extension Lean/custody, NF### original physical numerical enclosure, or PI### separate pole–prime–Gamma projection.

**Status:** source-matched exact mathematical SUFFICIENCY calculation and explicit genuine original v4.35 Lean SOURCE PROOF CANDIDATE, **NOT yet a real Lean kernel PASS**. Original CP013–CP016 new Lean proofs on which this builds have not yet produced accepted `.olean`/standard-axiom receipts, and the source workflows in the inherited stack are queued. The original source itself continues to provide separately genuine finite-height RH/count/simplicity. No global RH or global Weil positivity.

## 1. Actual new analytic reduction: two independent rational inequalities suffice

Define the frozen source seam and proposed first RS refined bracket upper endpoint
[
a=149500/1000=149.5,quad
b=15005353/100000=150.05353,quad
Delta=b-a=55353/100000=0.55353.
]
Set (Z(t)=\texttt{Zeta.hardyZ}(t)), the *original* real Hardy-Z function from the pinned Zeta release. The exact sufficient inequalities are:

[
\boxed{Z'(a)\ge 12/5}
\qquad\text{and}\qquad
\boxed{\forall t\in[a,b],\quad |Z'(t)-Z'(a)|\le4(t-a).}
]

The whole second inequality follows from a more primitive, formally stated original Mathlib mean-value checklist:

[
\text{(i)}\quad Z'\text{ differentiable on }[a,b];
\qquad
\text{(ii)}\quad
\forall t\in[a,b),\;
|\operatorname{derivWithin}(Z',[a,b],t)|\le 4.
]

For every (t\in[a,b]),
[
\begin{aligned}
Z'(t)
&\ge Z'(a)-4(t-a)\\
&\ge\frac{12}{5}-4(b-a)\\
&=\frac{12}{5}-4\frac{55353}{100000}\\
&=\boxed{\frac{4647}{25000}=0.18588>0}.
\end{aligned}
]

**All equalities and the strict positive margin are exact rational arithmetic. No claim that the preceding two real-function inequalities have yet been rigorously certified.** This reduces a global-in-window strict monotonicity check to one original Hardy-Z derivative *anchor* plus one original Hardy-Z *curvature* interval enclosure. The exact critical permissible curvature with the chosen anchor is
[
M<\frac{(12/5)}{(55353/100000)}
=\frac{80000}{18451}\approx4.33580835727.
]
The proposed (M=4) leaves a strict positive margin. Negative controls: (M=5) with the same anchor or anchor (2) with (M=4) would **not** suffice.

Thus a TRUE uniform proof of the two inequalities yields `StrictMonoOn Zeta.hardyZ (Icc a b)` from original Mathlib `strictMonoOn_of_deriv_pos` plus original upstream `continuousOn_hardyZ`.

## 2. Actual direct numerical exploration (NONRIGOROUS, never a proof)

As a **feasibility screen only**, I evaluated `mpmath.siegelz` at 50 decimal digits, differentiating numerically at **81 equally spaced ordinates** on the entire interval. It produced:

| Numerical check | Floating-point screen |
|---|---|
| (Z'(149.5)) | (\approx 2.442738145848111116449719) |
| Minimum of 81 **sampled** (Z') | (\approx 1.6201346488531756) at (150.05353) |
| Maximum of 81 **sampled** `abs(Z'')` | (\approx 3.0838450939148268) at (150.05353) |
| Chosen rational endpoint derivative anchor | (12/5=2.4) |
| Chosen rational uniform curvature threshold | (4) |
| Exact consequent margin, **if hypotheses proved** | (4647/25000=0.18588) |

**CRITICAL:** Those 81 evaluations are neither validated intervals nor a guarantee for intermediate points. Numerical `mp.diff` cannot establish ANY of the universally quantified analytic hypotheses. The proposed two rational targets remain **OPEN** until proved with actual analytic error bounds and/or rigorous interval arithmetic. Do not interpret the sampled extremum as a certified supremum or assume `Z''` exists with the required certified formula from a numerical differentiation call.

Optional reproducibility: `python scripts/cp017_hardyZ_curvature_budget_preflight.py --numeric-screen --sample-count 81`. This explicitly labels output NONRIGOROUS. It is not run by the CP017 source or Lean workflows.

## 3. Formal Lean source dependency and numerical zero identity: no missing proof hidden

New `cp011_zeta_v435/CP017CurvatureBudget.lean`, **original external Lean 4.35 source candidate** contains SEVEN theorem targets:

1. `exact_positive_derivative_margin`: exact `0 < 12/5 − 4(b−a)`, no analytic assumption, `norm_num` proof.
2. `uniform_derivative_margin_of_rational_budget`: explicitly assumes (Z'(a)\ge12/5) and the universal derivative variation; proves `∀t∈Icc a b, 4647/25000 ≤ deriv Zeta.hardyZ t`.
3. `strictMonoOn_original_hardyZ_of_rational_budget`: same premises, genuine original `continuousOn_hardyZ`, and actual Mathlib `strictMonoOn_of_deriv_pos`.
4. `derivative_variation_of_curvature_bound`: with explicit differentiability of (Z') and universal bound on `derivWithin Z'` in `Ico a b`, uses the genuine Mathlib `norm_image_sub_le_of_norm_deriv_le_segment` to prove the universal Lipschitz variation. No sample is inserted as a proof.
5. `strictMonoOn_original_hardyZ_of_curvature_bound`: composes 1–4; no analytic bounds are ever supplied by an axiom.
6. `narrowRightLtOriginalGram`: *unconditional original-source bound* (b<g), deduced from original `certifiedGramBlockSeq.head_left_le_gramPoint` and the exact last original RS interval right endpoint `1000449.286`. This eliminates a previously redundant extra height-window premise from the final theorem.
7. `refined_narrow_root_is_source_53rd_of_rational_budget`: conditional on a genuine source-analytic zero existence theorem `ζ(1/2+i t)=0` with (t\in(150.05352,150.05353)), and analytic A+B. Invokes the **SOURCE-CANDIDATE** CP016 identity theorem to conclude that this newly certified zero must equal the source-defined first RS zero and hence has (N(t)=52), i.e., ordinal 53. The theorem does **not** claim the narrow candidate zero or the curvature enclosure has been proved.

This is more economical than CP016's arbitrary monotonicity hypothesis because it assigns exact numerical rational targets to the separate small analytic proof obligations.

**Unproved primary analytic inputs after CP017:**
- The *actual* original (Z'(149.5)\ge12/5) must be proved using a certified analytic derivative/enclosure, NOT `mpmath.diff`.
- (Z') must be shown differentiable across the whole interval with an original-source-compliant formula, and (‖\operatorname{derivWithin}(Z',[a,b],t)‖\le4) must hold **for every** point. A validated interval method / explicit Taylor or original Euler–Maclaurin / Riemann–Siegel derivative remainder is needed.
- A true original-v4.35 new root-existence certificate for (t\in(150.05352,150.05353)) must pass its sign/error kernel check (CP010). The current original source batch public count/outer endpoint and a floating-point sign change do not provide this.
- CP013–CP016 source-dependent first-RS rank/zero-roster work must pass its actual Lean v4.35 kernel checks. An upstream original imported certificate acceptance alone is insufficient for new local theorem declarations.

## 4. Original-source custody, exact rational tests and CI discipline

Directly re-fetched FOUR *actual* original source files at pinned revisions:

| Original source | Immutable Git blob | Real source fact |
|---|---|---|
| `smmercuri/zeta@c06b4e13...`: `Zeta/Zeros/HardyZ.lean` | `9975442b0c14011c35f4624197d0bf26169c7665` | `Zeta.hardyZ`, continuity, HardyZ⇔critical zero |
| Zeta `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | original `N(g)`, simplicity, finite-height RH |
| `mathlib4@v4.35.0`: `Mathlib/Analysis/Calculus/Deriv/MeanValue.lean` | `b72f134c66e2fc86a0ac93dd241629881b9e7d1b` | real `strictMonoOn_of_deriv_pos` |
| `mathlib4@v4.35.0`: `Mathlib/Analysis/Calculus/MeanValue.lean` | `7004c9f6d2bf12928f02be9ee35a814aed17e254` | real `norm_image_sub_le_of_norm_deriv_le_segment` |

**4/4 primary Git-blob and target-signature checks PASSED directly during CP017 authoring.** Exact fractions independently verified `55353/100000`, `4647/25000`, `80000/18451`, and the two failed negative budget controls. This is **real SOURCE/EXACT MATH preflight, not a Lean kernel acceptance**.

New `scripts/cp017_hardyZ_curvature_budget_preflight.py`: exact Fraction assertions, negative controls, pinned Zeta & Mathlib original Git blob SHA/source signature verification, explicit unproved-result JSON, and optional 50-digit/81-point mpmath SCREEN whose output labels state NONRIGOROUS.

New `scripts/cp017_original_curvature_lean_axiom_audit.py`: requires actual compiled external v4.35 `CP017CurvatureBudget.olean`, all eight imported original RS/finite-count/HardyRank proof candidate `.olean` files, actual **SEVEN** new standard-only `#print axioms` receipts and source/compiled artifact hashes. A success, if any, prints **CP017_ORIGINAL_HARDYZ_RATIONAL_CURVATURE_CONDITIONAL_KERNEL_PASS_ONLY**, explicitly recording that the *analytic premises and root existence remain UNPROVED*.

New workflows (no automatic PR creation/synchronization/push fanout):
- `.github/workflows/cp017-curvature-rational-source-opt-in.yml`: explicit PR label `cp017-curvature-source` (or eligible manual dispatch) does exact rational and original 4-file SHA audit. NOT Lean.
- `.github/workflows/cp017-original-hardyZ-curvature-v435-lean-opt-in.yml`: explicit PR label `cp017-curvature-lean` (or eligible manual dispatch) invokes actual original Zeta v4.35 build and strict standard-axiom receipt; **not dispatched while IV###/NF### backlog is crowded**.

No new CP017 Lean kernel acceptance or accepted actual analytic derivative interval enclosure has been reported. This track's PR remains a **draft**.

## 5. Preservation law and next exact obligation

**Intrinsic:** original true zeta zero #53 by rank; CP016 source-defined finite RS-minimum uses original complete Turing count and original finite-height simplicity. An independently certified numerical zero can be identified with it by **strict monotonicity**, without numerically exposing original first RS row's private endpoint.

**Certificate-relative:** source 52/1,747,950 method segmentation, the interval `[149.5,150.05353]`, exact rational bounds `12/5,4,4647/25000` and source SHA. These are selected sufficient proof parameters, not intrinsic zero invariants.

**Unknown analytically:** whether a usable original-source derivative formula plus bounded remainder makes the two rational hypotheses *actually provable* at affordable finite precision. That is the immediate falsifiable CP018 task, alongside recovering any accepted CP013–CP017 Lean compiler result.

**Next CP018:** derive a rigorous source-compatible (Z') formula at 149.5 and a true explicit enclosure of (Z'') on the ENTIRE interval, or use a different finite rank count. Avoid scaling the 1,747,950 refined zero coordinates until the first numeric root #53 is truly certified and attached. Original signed Weil Pole−Prime+Gamma 3×3 vs complete spectral zero-side normalization/quadratures remain independent OPEN obligations. NO global Weil positivity or RH claim.
