## Verified MG28 result — direct original curvature computation

[Actions #39438064440](https://github.com/monocap-tech/weil-lab/actions/runs/39438064440) **PASSED** the original complete source/pole calculation and independent exact-Fraction/no-promotion checks (artifact `mg28-actual-original-direct-curvature-brackets`). The analytic nonsingular original sinh pole T'' interval was used and the 23 original double-boundary-adapted source second derivatives were combined before taking absolute values.

| Original [0,4] partition | Improved source/cell channels | New/old H_C bracket trace-width | New/old G_C | New/old S_C |
|---|---:|---:|---:|---:|
| 8 equal cells | **0** | **1.000000** | **1.000000** | **1.000000** |
| 16 equal cells | **384 / 384** | **0.715006632** | **0.712776122** | **0.710265087** |

**Complete-frequency pole-corrected coupled source bracket widths, 16 cells:**
- At cutoff `2^12`: Gstar **0.719596932×** MG26, Sstar **0.697700236×** MG26.
- At cutoff `2^16`: Gstar **0.719982410×** MG26, Sstar **0.699062655×** MG26.

The 8-cell result means the independently verified older MG26 curvature bound dominates this direct midpoint+third drift bound on **every** tested channel at that coarse cell size. At 16 cells, retaining cancellation yields a strict improvement on **all 384 source/cell pairs**, reducing the sum of source Taylor radii by about **30.07202033**. This is a real certified improvement in **trace-width precision**; it does NOT itself certify a positive residual. MG26's prior roughly 35–40× wider-than-MG24 bracket deficiency is reduced in scale but not eliminated: the new 16-cell whole-frequency matrices are still far less sharp than MG24.

**Next method frontier:** directly certify the *adapted third derivative* too, or combine MG24 selected panels with the MG28 contiguous-prefix mass enclosures in a same-basis joint split to avoid discarding already accepted nonflat-cell lower information. If using multi-resolution cell widths, test actual error budgets; do not infer improvement from the 8-cell result. Independent original Fourier/form-domain identification, entire 470-source strong inverse and signed 51/56 negative cap, complete odd/even/Weil/CC27 and RH all remain **OPEN**.

---

# MG28 — Directly certify the original adapted Fourier second derivative

October 20, 2026. Stacked on verified [MG27 PR #276](https://github.com/monocap-tech/weil-lab/pull/276). MG27 established that source Fourier curvature, *not signed multiplier-width*, dominates the uncompetitive MG26 8-/16-cell [0,4] positive-frequency source moment trace widths. This MG28 trial must measure whether preserving actual source cancellation inside the second derivative reduces those certified errors.

## Original operator and same physical source basis

Use the original SI10 25 true supported physical odd generators, with 23 MG11 double-boundary-adapted
`h_i=f_i-a_i*s-c_i*f_{23}` and genuine unchanged pole `s=sinh(x/2)` as the 24th coupled source channel. All `a_i,c_i` are true rational endpoint-trace *intervals*, never floating coefficients.

On every rational midpoint of the 8- and 16-cell contiguous true-original positive-frequency [0,4] partition, reconstruct the same original Fourier midpoint values `v_i`, derivatives `d_i`, and rigorous true multiplier bounds as MG26.

## The source curvature refinement

The previous accepted MG26 source second-derivative budget applies the triangle inequality before combining the physical source:

`Kold_i=K_i+|a_i| K_pole+|c_i| K_pivot`.

MG28 instead forms the actual *combined exact interval*

`D2hi_i = T''_i(mid)-a_i*T''_pole(mid)-c_i*T''_pivot(mid)`.

Its sourcewise third-frequency-derivative budget `L3i=J_i+|a_i|J_pole+|c_i|J_pivot` proves
`|T''_hi(xi)| <= maxabs(D2hi_i)+L3i*cell_half`
for **every real frequency** in each cell. Choose `Knew_i=min(Kold_i, that bound)`. Thus `0<=Knew_i<=Kold_i` is a theorem, without assuming any favorable cancellations.

Important pole detail: SM46 exposes `T''_pole=None` while supplying its strong global bound. MG28 derives the missing true sinh-pole second derivative by analytically differentiating SM42's rational interval formula `T_s(w)=N(w)/(a²+w²)` twice with `w=2*pi*xi`, `a=1/2`, `N=2[a*cosh(B/2)*sin(Bw)-w*sinh(B/2)*cos(Bw)]`. Formula is nonsingular at zero and checked by the expected odd-frequency parity `T_s''(0)=0`. All trigonometric, hyperbolic and pi terms are original enclosing rational intervals; no sample or finite difference.

For each source, reuse MG27's independently exact decomposition of MG26's original `r_old = up(value_interval_radius + derivative_interval_radius*half + Kold_i*half²/2)`, and construct `r_new` by replacing only `Kold_i` with `Knew_i`, preserving all other original SI10 source data. Assert exact rational `r_new<=r_old` on every source/cell.

## New full-frequency calculation and strict scope

Rebuild three 24D source moment Loewner brackets on [0,4] (unweighted H_C, first G_C and second S_C) with *exactly the same MG26 per-cell Young tau*, eliminating trial-optimizer ambiguity. Use the physically reconstructed whole source H and exact original high SM41 tails in the same verified MG26 remaining-mass closure to bound the complete real-frequency G_o,S_o. Preserve rank-one sinh-pole response c and its mixed correction in Gstar/Sstar.

Report exact rational ratio to MG26 for all three prefix moment widths, and compare whole-original-frequency pole-corrected Gstar/Sstar bracket widths at k=12 and 16. A trace-width reduction does not automatically imply Loewner dominance, inverse existence, 24D strict residual, signed 470D cap or RH; certify such claims separately.

**Acceptance: PASSED original 24D interval and comparison checks.** No automatic claim that keeping cancellation yields a meaningful improvement. W-ODD-NEG; full original 470D strong residual and signed 51/56 negative cap; independent original Fourier/form-domain audit; complete odd/even/Weil/CC27/RH remain OPEN.
