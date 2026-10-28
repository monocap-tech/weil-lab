# Weil-Lab — NF364: split original critical positive forcing, certify sine tail and locate projected-head gate

**Date:** 2026-10-28. **Status:** read-only local analytic/exact-rational preflight. **Original operator:** unchanged seven-prime supported odd Weil construction, `B=11/10`, accepted physical `J242`, `Q=I-P_J`. **No:** repository write, new selected direction, strong positive exterior inverse, positive head projection certificate, signed Schur positivity, native/Lean promotion, or RH claim.

## A. Source custody

The exact 32-sine plus true supported pole coefficients are from PR #348's original critical four-plane. Pinned artifact `/mnt/data/nf361-pr348-fourmode.zip` SHA256 `735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968`, embedded `original_four_mode_critical_block.json` SHA256 `a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922`. Source frequencies `c_n=5n/11`, and the same exact rational `a_{in}`, `b_i` are retained. Both primary and independent scripts verify the hashes and all four source coefficients from this archive.

Let `s(x)=sinh(x/2)` on `[-B,B]`, zero elsewhere, `f_i=g_i+b_i s` with `g_i=sum a_{in} sin(2π c_n x)`. Let `a_o(xi)=max(1/1000,m(xi))` be the complete original positive multiplier, `A_o=P_I F^{-1} a_o F` its supported selfadjoint realization, and `A_*=A_o-2|s><s|`. Since the retained exact selected span contains `s`, `Qs=0`, and

`Q A_* f_i = Q A_o g_i + b_i p`,  where  `p=Q A_o s`.

**This is an exact physical-output identity**, not Fourier projection commutation. `p` is a single *shared* physical response for all four source functions; it has not been computed, and its coarse bound below is not a matched response certificate.

## B. Rigorous pole-output bound (new independent scalar payment)

The positive multiplier satisfies accepted SM41 `a_o(xi) <= 17+log|xi|` for `|xi|>=1`. For `|xi|<=1`, use the exact positive digamma Euler series, its negative constant `ψ(1/4)-logπ<0`, `π²<10`, the `k=0` term `<=4`, and the decreasing `k>=1` bound:

`sum_{k>=1} (πxi)^2/(k+1/4)^3 <= 10*(64/125+8/25) = 8.32`.

The original complete seven-prime amplitude is `<70751/10000`, so `a_o(xi)<20` throughout `|xi|<=1`.

The exact physical squared mass is `||s||²=sinh(B)-B<1/4`. To check the strict upper rationally, bound `sinh(B)-B` by `(B³/6)/(1-B²/20)` because the consecutive positive-series term ratio from degree three onward is at most `B²/20`.

For the high-frequency sine transform of `s`, write `k=2πxi`, `I(k)=int_0^B sinh(x/2) sin(kx) dx`, and integrate by parts twice, retaining the original ODE `s''=s/4`:

`(1+1/(4k²)) I(k) = -s(B)cos(kB)/k + s'(B)sin(kB)/k²`.

Therefore `|hat s(xi)|=2|I(k)| <= s(B)/(π|xi|) + s'(B)/(2π² xi²)`. The exact positive-series bounds at `B/2=11/20` give `s(B)<3/5`, `s'(B)=cosh(B/2)/2<3/5`, and `π>3` gives

`|hat s(xi)| < (7/30)/|xi|` for `|xi|>=1`.

The full supported action is a contraction of the whole-line multiplier output. With the exact SM41 integral `2∫_1^∞(17+log t)²/t²dt=650`,

`||Q A_o s||² <= ||a_o hat s||² <400/4 +650*(7/30)² = 2437/18 <136`.

The original rational source coefficients satisfy

`sum_i b_i²=5029689/500000000000000000000000 = 1.0059378e-17`.

Thus the **complete shared pole forcing**, as a map from four real coefficients to physical `L²`, satisfies

`||p b^T||_op² <=136 sum_i b_i² <1.368076e-15`.

This is a **coarse scalar upper**, not a certified sufficiently small near-critical error. In particular `136 sum b_i² / .00998` is about `1.37e-13`, much larger than the accepted four-plane signed-form norm bound `~9.84e-17`. The shared pole response should be retained and calculated or canceled jointly if the final sign budget requires it.

## C. Exact sine-only high tail

For `|xi|>=32`, the original sine-transform rational identity from NF363 gives, with exact alternating moments `S1`, `S3` and positive fifth-moment remainder,

`|hat g_i(xi)| <= |S1_i|/(3|xi|²) + |S3_i|/(3|xi|⁴) + (4/9)sum_n |a_in|c_n^5 / |xi|⁶`.

Integrate the square of these positive majorants with `a_o(xi)²<=(17+log|xi|)²`; all mixed coefficient directions are paid by coefficient Cauchy, using the strict rational `log2<347/500`. The primary program evaluates ordered term pairs as exact `Fraction`; the *independent* program expands the squared inverse-power polynomial before integration and agrees on every exact rational.

| Cutoff | Four-direction squared sine-only tail `T_s(L)` (rigorous upper; displayed decimal) |
|---:|---:|
| 128 | `1.311935e-15` |
| 256 | `1.151393e-16` |
| 512 | `1.461291e-17` |
| 1024 | `1.922169e-18` |
| 4096 | `3.350421e-20` |
| 8192 | `4.417187e-21` |
| 16384 | `5.815925e-22` |

No frequency or source dimensions were added. At 1024, this is about a factor five smaller than the NF363 complete sine-plus-pole cutoff upper; at 4096, it is about a factor 38 smaller. The pole has **not disappeared** from the full action: it is retained as `p` rather than paid with a cutoff. Its physical response is still unknown.

## D. Exact projected-head identity and first-response gate

For any cutoff `L>=32`, define the four physical head columns

`w_{L,i}=P_I F^{-1}[1_{|xi|<=L} a_o(xi) hat g_i(xi)]`

and let `R_{L,i}=P_I F^{-1}[1_{|xi|>L} a_o(xi) hat g_i(xi)]`. The physical `Q` is applied **after** whole-line inverse Fourier transform and physical compression; do not commute it with the frequency band projection. For any coefficient vector `z in R^4`,

`Q A_* f_z= Q w_L(z)+ (b·z)p +Q R_L(z)`, with `||Q R_L(z)||² <=T_s(L)||z||²`.

For any four *trial* physical selected vectors `j_i in J242`, the exact finite-dimensional best approximation identity is

`||Q w_L(z)|| = inf_{j in J242} ||w_L(z)-j|| <= ||w_L(z)-sum_i z_i j_i||`.

Therefore one explicitly checked correlated **4-column supported physical head residual** with norm ceiling `delta_head` would give a rigorous upper on the full first forcing:

`||Q A_* f_z|| <= (delta_head +sqrt(T_s(L)) + sqrt(136 sum b_i²)) ||z||`.

If the pole action is evaluated together with the four head columns in a *joint* selected approximation, the last scalar pole term can be replaced by its actual correlated residual. This is the preferred near-critical variant. It does not require inverting the 242-dimensional selected Gram to certify an upper bound: **any specified trial selected combination provides a valid upper**. A lower bound would need a separate variational test.

With positive exterior operator `H=A_*|_{J242^perp}` and `H>=mu_H I`, the first energy-dual solve `H v_z=Q A_*f_z` has `||v_z||_{a_F}²<=||Q A_* f_z||²/mu_H`. This does not compute `v_z` and does not certify the subsequent directional Neumann moments.

## E. Certified obstruction to the naive raw low-band bound

The PR348 four-plane has physical Gram `>=99/100 I`, and `A_o>=κ I` with `κ=1/1000`. The old NF363 complete all-source tail at 32 has *exact-rational* squared upper `<10^-12`, so its physical compression has norm `<10^-6` per unit source coefficient vector. Let

`v_32(z)=P_I F^{-1}[1_{|xi|<=32} a_o(xi) hat f_z(xi)]`, **including the pole part in `f_z`**.

The reverse triangle inequality yields

`||v_32(z)||>=||A_o f_z|| -10^-6||z|| >= (κ sqrt(.99)-10^-6)||z|| >989/10^6 ||z||`.

Thus the *unprojected* low-band squared action is **rigorously** `> 978121/10^12 ||z||²`, around `9.78e-7`, for all nonzero coefficients. Merely using `||Qv_32||<=||v_32||` can never certify a `~10^-14`-scale projected forcing squared norm: it fails as a method before integration. This does not lower-bound `||Qv_32||` and is not a negative original-Weil witness. The decisive missing quantity is **correlated physical selected-space subtraction**.

A SciPy/digamma pilot (not interval certified) found unprojected low `[0,32]` squared strong-action diagonal values approximately `1.9`, `0.63`, `0.40`, `0.42`; their nonconvergence at coarse sampling is another reason not to treat them as a sign certificate.

## F. Decision and next cursor

- Exact-rational local proof and independent replay: full 4-column sine-only tail and common pole upper **PASS**.
- A raw-contraction-only approach to low-band projected forcing **STOP** by exact lower bound.
- The pole is one shared complete forcing, **not four high-frequency cutoff tasks**.
- The **actual** four-column projected low-band residual `delta_head`, an acceptable candidate `j_i`, and the first matched exterior-positive solve are **UNCOMPUTED**.
- Next bounded gate: construct or recover a *single* correlated selected-frame candidate for the physical low-band action on these same four critical directions; certify its **supported physical residual** (preferably including the one common pole response). Do not start more Fourier cutoff/precision work without that candidate and a declared sign budget.

**Standing:** W-ODD-NEG, complete four-direction Schur, canonical original operator/domain audit, even/whole form, RH all **OPEN**. No GitHub writes or promotion.

**Local artifacts:** `nf364_split_tail_exact.py`, `nf364_split_tail_exact_report.json`, `nf364_independent_replay.py`, `nf364_lowband_pilot.py`. Source archives and earlier signed certificates unchanged.
