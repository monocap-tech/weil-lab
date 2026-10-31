# Weil-Lab NF427 — Original full cell-6 series cutoff (1500 coefficients) and scalable native block

**2026-10-31 PT. Canonical `W-ODD-NEG` OPEN; RH OPEN.** Stacked on verified original NF426 [PR #432](https://github.com/monocap-tech/weil-lab/pull/432). No source swaps, main merge, or promotion beyond actual math/numerical gates.

## Previous cursor / current circle / next bold

**Previous NF425/426.** NF425 proved one degree-2048 **Chebyshev interpolant** existence error <2e-45 using a source-derived complex Bernstein ellipse E2. NF426 independently calculated the first four n=0..3 **Chebyshev *series*** coefficients in 2048-bit Arb, preserving the full 246-generator NF407 source, original NF406 seams, the original NF404 dyadic pole and original endpoint log, and passed a complete physical x=9/10 comparison with the separate NF416 I0/I1 evaluator. The missing 2045 coefficients and cell-6 signed integral were OPEN. Those four numerical coefficients are series coefficients, *not* the distinct interpolant coefficients; no interchange is assumed.

**Current NF427.** Derive an exact source-replayed **series** cutoff of degree **1499** on the true original entire cell6; use it to reduce the numerical target from 2049 to **1500** coefficient intervals. At the same time submit a source-preserving native block computation for **n=0..63**, 64 coefficients, including the independent NF416 x=.9 cross-method check. Acceptance of the 64 numerical coefficients is conditional on focused native CI PASS with all coefficient outward widths <1e-25. Passing the exact-tail job alone is not acceptance of the native values.

**Next NF428.** Verify 64 native coefficient intervals; continue the same generator in 64/128-mode source-correlated blocks or a shared full 1500-mode call; archive completed interval data permanently, and implement original high-degree signed log/Chebyshev moments, then the genuine full cell6 `pz,z²` interval and the remaining seven cells.

## The key improvement: distinguish interpolant and series

The original fixed-branch physical source model from NF424 is a sum of correlated original exponential-polynomial modes, native endpoint-digamma terms and two endpoint image series. Define `z_F` as the **finite original 2048-image midpoint source model**, not an unrelated surrogate. Its fixed cell-6 analytic continuation is holomorphic on

`x=C+H*t,  C=91/100, H=7/100, t in E_2`,

where `Re x<=399/400<B=11/10` and `|Im x|<=21/400`. From original NF425's coefficient-exact raw triangle and native removable pole ledger,

`sup_(t in E2)|z_F(C+Ht)|<M=10^400.`

NF426 constructs **Chebyshev-series coefficients** `a_n` in

`z_F(C+Ht)=sum_(n>=0) a_n*T_n(t).`

For n>=1, the standard ellipse contour/Cauchy bound is

`|a_n| <= 2*M*2^(-n).`

For **N=1499**, the discarded high-mode *series* tail is bounded uniformly for all real `-1<=t<=1` by

`sup |sum_(n>=1500) a_n*T_n(t)| <= 2*M*sum_(n>=1500) 2^(-n) = 4*10^400/2^1500 < 10^-50.`

These are NOT NF425's original degree-2048 Chebyshev-*interpolation* coefficients. There is no interpolation aliasing error: the finite series expansion is used directly.

NF424 separately proves from actual original NF407 source coefficient radii and the original NF406 cell6 image separation that on the *whole original physical open cell* `J6=(log7-B,log8-B)`

`sup_(J6)|z_true-z_F| < 10^-45`.

Therefore the **mathematically defined but not yet completely numerically enclosed** degree-1499 series partial sum satisfies the original whole-cell strict residual

`sup_(J6)|z_true-sum_(n=0)^1499 a_n*T_n((x-C)/H)| < 2*10^-45`.

The exact-rational script `scripts/local_replay/nf427_original_cell6_chebyshev_series_tail_exact.py` replays the true source ball/hash, true prime-support knot/hash, original parent NF423, original NF425 preflight script SHA, ellipse/source envelope and exact strict integer bounds. **This is a new complete original cell6 mathematical cutoff certificate, not a certified list of all 1500 coefficients.**

The gap between the previous 2049 interpolant sample/coefficient requirement and the new 1500 directly evaluated Chebyshev-series coefficients is **549 fewer coefficient evaluations**, with an explicit <1e-50 omission charge. In particular, it is invalid to set the remaining a_n for n>=1500 to zero *without* paying that tail.

## Native 64-mode implementation and acceptance

`scripts/local_replay/nf427_original_cell6_chebyshev_64_mode_native.py` inherits the exact NF426 246-generator `arb/acb` evaluator but widens the certified requested range to n=0..63. It evaluates all original source-polynomial digamma derivatives, five true signed source translations (n2,3,4,5,7), the NF404 dyadic centering and source endpoint log, and all 2048 common left/right endpoint image amplitudes, then uses Bessel `I_n` directly. The original odd sinh `lambda=±1/2` m=0 pole is eliminated analytically, as in NF426, before Arb evaluation. The source coefficient radii and analytic finite-image tail are included as an extra `4e-45` charge **per coefficient**. The full native x=9/10 global source response is independently compared with the previously certified genuine NF416 physical integral; a failed overlap stops acceptance.

For each n=0..63, the acceptance condition is:

- Correct original NF407 SHA, NF406 SHA, NF423 SHA, NF416 SHA, exact 246 source and signed branch status.
- Outward Arb ball plus the explicit original source/image analytic charge for coefficient `a_n`, with `width<1e-25`.
- Complete original x=9/10 shared transfer pointwise interval overlaps independent NF416 certified separate I0/I1 integral (after source-tail charge).
- All 64 outward rational enclosures retained by a focused workflow artifact and original prefix is explicitly **not** represented as a full polynomial norm or signed scalar.

The 64-mode test is a **bounded scaling experiment** for the full 1500-coefficient target, not evidence that the remaining 1436 modes have already been evaluated. A successful job reduces the uncomputed count from 1496 (after NF426's four) to **1436**. Those 1436 numerical modes remain OPEN.

## Full scalar acceptance interface

Once all 1500 coefficient balls have been constructed, let `P_{1499}` denote their **interval** Chebyshev series. On the **true** irrational physical knot endpoints, original signed

`int_(J6) p(x)*P_{1499}(x) dx`, `int_(J6) P_{1499}(x)^2 dx`

must be evaluated with outward rational/Arb intervals, using the exact original logarithm and all five active original signed prime jumps; NF410's k=0..3 Taylor moments are not sufficient for this high-degree series. Polynomial products can be formed using `T_m*T_n=(T_(m+n)+T_|m-n|)/2`, but direct coefficient pairwise sums are expensive and require a carefully selected moment recurrence. The uniform original source/model error <2e-45 (plus certified numerical coefficient radii) must be propagated into the signed scalar and squared norm. **None of these integrals or scalar acceptance decisions is claimed in NF427's exact-tail certificate alone.**

## Custody and standing

- Exact original-source/rational cutoff: `scripts/local_replay/nf427_original_cell6_chebyshev_series_tail_exact.py`.
- Native scaled 64-mode coefficients: `scripts/local_replay/nf427_original_cell6_chebyshev_64_mode_native.py`.
- Focused workflow: `.github/workflows/nf427-cell6-cheb-series-cutoff-native64.yml`. Native numeric evidence must be read from exact job/artifact, not inferred from code.
- Expected standing split: **accepted original-source Chebyshev SERIES cutoff** if exact runner PASS; **native 64-mode prefix only accepted if native runner PASS**; original cell6 complete integral, all other cells, full NF410/NF404, original fourth exterior J242 upper, even/whole Weil, `W-ODD-NEG`, domain/infinite inverse and RH **OPEN**.

No automatic main merge.
