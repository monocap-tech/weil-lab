# MG30 — Original anchored nonscalar source-residual acceptance on MG29

October 20, 2026. Stacked on [MG29 #278](https://github.com/monocap-tech/weil-lab/pull/278), both original calculation-bearing runs passed. MG29's original 32-cell direct-adapted-third-derivative complete-frequency pole-corrected Gstar/Sstar **trace widths** reached 1.0356–1.0728 times the independently certified MG24 benchmark, yet no strict scalar matrix contraction was proved. MG30 tests whether actual nonscalar source geometry overcomes this.

## Exact physical source residual

The true original finite source map `F: R^24 -> odd L²` contains 23 original MG11 dual-trace-kernel sources and actual sinh pole. Its exact physical H=F*F 24D Gram is reconstructed from the original SI10 25-generator interval Gram, with outward Loewner Hlo/Hup. For the **complete original-frequency original pole-corrected** `Astar`,

```
G=F*Astar F,      S=(Astar F)*(Astar F),
R=F-Astar F B,    R*R=H-G B-B^T G+B^T S B.
```

The full-original Fourier first/second source **Loewner brackets**, not exact numerically evaluated G/S values, are supplied by the successful pinned MG29 Actions #39440914565. They include true original prime7/digamma multiplier, all remaining real-frequency positive mass H-H_C, SM41 complete-frequency tail, and entire original rank-one pole mixed first/second terms.

## Improved source-aware Loewner uncertainty accounting

Unlike the earlier generic MG25 rule that paid the entire scalar trial with `2||E|| ||B||I`, decompose each exact rational trial matrix as

```
B=tI+D, t>=0; LG<=G<=UG; E=(UG-LG)/2; Gc=(UG+LG)/2; S<=US.
```

Then

```
R*R <= Hup -2t LG -Gc D -D^T Gc
           +B^T US B + 2||E||upper ||D||upper I.
```

This is valid for **arbitrary nonsymmetric and noncommuting D**: the scalar `-2tG` uses true original lower LG, and only the unknown non-scalar cross terms pay the conservative operator norm uncertainty. `||E||upper` is exact rational max-row/column absolute sum; `||D||upper` is also a rational max-row/column bound. It includes all physical source crosses and all original pole terms. Its exact algebraic reduction is independently checked against a genuine nontrivial rational 3D rank-one pole surrogate for both exact G and widened Loewner brackets.

The physical-square one-step source contraction acceptance is **strict**: if exact Gershgorin lower `m>0` for `Hlo-Rupper` and certified `H<=K I`, then `R*R<=H-m I <= (1-m/K)H`. Report `gap=max(0,min(1,m/K))`. Otherwise gap is exactly 0 and the case must fail closed. Even strict 24D one-step contraction would **not** demonstrate finite source invariance, an iteratable global Neumann inverse, or the original 470-source signed 51/56 gate.

## Original exact-rational trial experiment

On *both* verified MG29 16-/32-cell original matrices and original low cutoff k=12/16:

- Replay MG24 scalar baseline `B=tI` and deterministic half/double variants to establish a common comparison.
- Propose genuine source-dependent diagonal `B` with exact rationalized per-coordinate `Gc_ii/US_ii` and bounded blending into the scalar anchor.
- Propose regularized matrix least-squares directions `B=(1-alpha)tI+alpha(US+lambda ||US||I)^(-1)Gc`; any temporary floating solve **only proposes** the candidate, then quantize to exact denominator `2^17` and independently re-evaluate the complete inequality in exact rational arithmetic.

The candidate family is *finite*, not globally optimized. A negative margin is **failure of this acceptance method**, never evidence that `Astar` has negative spectral directions or cannot be inverted. Report all signed Gershgorin margins, source residual gaps, true nonscalar-cross Loewner charges and the best tested direction. A reduction in MG29 vs MG24 *trace width alone* is not a matrix-order comparison.

## Forward route

If MG30 yields no strict source contraction, prioritize hybrid disjoint MG24 selected-cell information plus MG29 true [0,4] contiguous prefix as a same-basis joint Loewner bound. Avoid double-counting any overlapping frequency panel and do not equate same-basis trace comparisons with a Loewner envelope intersection. Re-test a genuinely full original 24D residual before extrapolating to 470 dimensions.

**Existing canonical obligations remain OPEN:** W-ODD-NEG; true original all-470 `J-AstarY` strong inverse, signed original odd 51/56 negative cap; independent Fourier/form-domain identification; complete even/Weil/CC27/RH.

**CI acceptance: PENDING.**
