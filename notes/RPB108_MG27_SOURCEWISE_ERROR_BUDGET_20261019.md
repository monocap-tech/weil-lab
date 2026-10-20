# MG27 — Original-source error-budget attribution against verified MG26

October 19, 2026 local. Stacked on [MG26 #275](https://github.com/monocap-tech/weil-lab/pull/275). This is an **original physical source error audit**, not a new spectral positivity or RH theorem.

## Reason

MG26 successfully implemented exact 24-channel original source Fourier mass/first/second moment enclosures on a contiguous [0,4] positive-frequency prefix with original sinh pole, both frequency signs, and genuine seven-prime/digamma positive multiplier. But although refining its 8-cell mesh to 16 cells greatly decreased the final full-frequency Gstar/Sstar trace widths, the best were still roughly **35–40 times wider** than already ineffective MG24 brackets. This suggests a source error-loss bottleneck. Before spending more CI on larger meshes, distinguish source Taylor uncertainty, Young splitting, and multiplier interval width **on the actual source**.

## Exact identity replayed

For each true-positive frequency cell `[a,b]` (width w), MG14/15 gives, on the same 23 adapted SI10 boundary-vanishing sources plus the original sinh pole,

```
T_i(xi)=v_i +d_i (xi-(a+b)/2)+e_i(xi),  |e_i(xi)|<=r_i
r_i = up(r_value_i+r_derivative_i+r_curvature_i).
```

`r_value` contains exact original interval source-Fourier value uncertainty, `r_derivative` its interval first-derivative uncertainty times half-width, `r_curvature` the genuinely original second-derivative bound times half-width squared/2, and `up` adds a nonnegative outward rounding fee. Every original mixed pole/boundary correction enters these transformed intervals.

Let `C_ii=v_i²+(w²/12)d_i²`, `R=sum_i r_i`, `0<l<=weight^p<=u` be the exact original whole-cell signed positive multiplier envelope for moment `p=0,1,2` (where `p=0` denotes unweighted source mass). With MG26's **same accepted rational tau** from the sourcewise-Young family, the upper minus lower TRACE of each double-sided frequency cell splits EXACTLY as

```
  2w (u-l) sum_i C_ii                   [multiplier interval width]
+ 2w tau (u+l) sum_i C_ii               [Young nominal affine mixing]
+ 2w ((u+l)/tau +(u-l)) R sum_i r_i      [Taylor source uncertainty].
```

The third term is decomposed additively for each source into
`r_value`, `r_derivative`, `r_curvature`, and `r_rounding`, with exactly the same positive prefactor. All six fees are **nonnegative exact Fraction quantities**. The script reconstructs the original 8-/16-cell source values and derivatives, reproduces MG26's sourcewise tau choices on **every cell**, sums the six fees, and verifies the exact pre-export trace width agrees with the original MG26 24×24 matrix brackets up to MG26's independently nonnegative outward matrix export fee.

For each moment p and each mesh, publish six category shares and the six most expensive true sources; also identify the highest Taylor-radius cells to support targeted, rather than blind uniform, refinement. Do not infer superior Loewner bounds merely from trace statistics.

## Acceptance and progression rule

Require:
1. Original MG26 independent-source artifact from successful [Actions 39380800739](https://github.com/monocap-tech/weil-lab/actions/runs/39380800739), pinned by run ID/name.
2. Whole actual original source [0,4], no gaps, no shortcut physical/synthetic source.
3. Exact per-cell fee identity and exact restoration of MG26 published prefix-moment upper-minus-lower trace.
4. Separate source value, derivative, curvature, and outward rounding loss; no floating empirical allocation.
5. A **method selection after observing the actual dominant fee**, not a forecast that 32 cells must succeed.

MG27 does not improve existing Gstar/Sstar original whole-frequency Loewner enclosures. The original full 470 strong residual, signed 51/56 negative cap, independent Fourier/form/domain audit, complete odd/even/Weil/CC27 and RH remain OPEN.

**CI acceptance: pending.**
