# NF392 — Original j387 polynomial-geometry norm certificate and native selected-moment recovery

**Date:** 2026-10-29 PT. **Canonical:** `W-ODD-NEG` remains **OPEN**. Additive draft stacked on NF391 PR #376 (no main merge; no old source overwrite). The immediate task is to resolve, not evade, the missing native pole-restored selected moment of the exact frozen NF387 source trial. No alternative source, odd operator, test cutoff or selected rank is introduced.

## Recovery of NF390/NF391 and explicit execution repairs

At entry, the accessible GitHub workflow list had NF391 source-only run [40966444584](https://github.com/monocap-tech/weil-lab/actions/runs/40966444584) **queued**. NF390 native pole-restored selected moment had **no accepted native output** in the accessible verified outputs, and the 50-entry run-list truncation means absence from that page is NOT proof the workflow never ran.

Source-level preflight found two genuine program defects independent of the mathematical derivation:

1. In original NF390 `scripts/verify_nf390_original_j387_selected_moment.py`, the source `C` is already an `arb_mat` from `makeF`. Its `C[t,col]` entries must be multiplied as Arb. Replacing `v*phys.a(F(C[t,col]))` with `v*C[t,col]` preserves exactly the original source coefficients at the inherited 4096-bit precision and avoids invalid/inexact `Fraction(arb)` conversion. This repair has been committed to both historical parent branch NF390 PR #375 and the inherited NF391 PR #376.
2. NF391 `scripts/local_replay/nf391_original_orthogonal_lowband_moment_gate.py` tried `j['scale_alpha']`, which does not exist in actual frozen NF387 source JSON. The exact field is `j['scalar_alpha']`. Correcting the read on NF391 PR #376 makes the original source-only replay executable without changing any formula, source hash or acceptance budget.

These are **verification blockers**; they are not numerical evidence that the candidate passed or failed. The NF392 branch descends from NF391's repaired head. The new NF392 focused workflow includes the exact source-only check and native original selected-moment production against the *same* frozen accepted original signed archive.

## New original-source polynomial norm certificate (not another witness family)

The frozen original (h=j_{387}) is the actual two-source dyadic combination

`h(x)=alpha*(121-100*x²)*sin(2*pi*(37/64)*x)`, `alpha=-88873/2^48`, supported on `I=[-B,B]` with `B=11/10`.

Its original NF387 raw J242 coefficient vector is unchanged (nonzero only at 0 and 2). Its exact boundary vanishing uses `100 B²=121`. NF391's previous physical norm cap used `|h|<=121|alpha|` and `2B<9/4`, giving `||h||<(363/2)|alpha|≈5.7306868584e-8`.

Pay the actual polynomial *shape*, not its worst value. Since `|sin|<=1`, exact source-only integration gives

`||h||² <= alpha² * int_-B^B (121-100x²)² dx`

`= alpha² * 2*(121² B-2*121*100*B³/3+10000*B⁵/5)`

`= alpha²*(1288408/75).`

And **the exact rational comparison** `(1311/10)² - 1288408/75=2531/300>0` shows

`||h|| < (1311/10)|alpha| =116512503/2814749767106560 ≈4.139355631593844e-8`.

This is a *strictly smaller* physical norm upper on the identical original (j_{387}), with no Fourier transform, sign assumptions, trigonometric evaluation, new kernel cells or selected-source optimization. It only uses `sin²<=1`, so is deliberately conservative; it does not claim to measure the actual native `||j||²`.

## More decisive necessary original candidate-specific discrepancy criterion

The previous NF391 same-residual orthogonal Bessel gate is retained exactly: original NF380 n512 physical exterior gives `e0=8.34e-14` strict lowband component, and `e0²+(2673/10^16)² > tau4²` with `tau4=2.8e-13`. Original NF375 complete multiplier highband upper at `Lambda=2^24` is `H`.

The native-selected moment `A=<m(D)u4,h>` must **restore the original odd pole**:

`A=Wodd(u4,h)+2<u4,s><h,s>`, `s=sinh(x/2)∈J242`.

If `|A-||h||²|>(H+2673/10^16)||h||`, this exact fixed h fails the original NF375 fourth physical lowband target, using the Bessel sum. From the new exact polynomial norm bound, source-only Fraction comparison yields

`(H+2673/10^16)||h|| < (H+2673/10^16)*(1311/10)*(88873/2^48)`

`≈1.3072582380793738e-20 <131/10^22 =1.31e-20.`

Therefore a genuine native selected-moment discrepancy **certified strictly greater than `1.31e-20`** is now sufficient to **STOP only the fixed j387 trial**. The prior sufficient source-only discrepancy ceiling was `1.81e-20`. This is a 27.6% tightening **of the coarse sufficient diagnostic ceiling**, not a new scalar operator bound or proof that the actual discrepancy exceeds either threshold. For a genuine native moment and native actual physical norm, always use its exact rational squared comparison in NF391, which is stronger than the conservative source-only ceiling.

## Reproducibility and stopping point

`scripts/local_replay/nf392_original_j387_polynomial_norm_gate.py` SHA-pins genuine original NF380 n512 source SHA256 `9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b`, NF375 Git blob `03c709571046d3f09307614aaded9749f5a15ba1`, and actual NF387 j Git blob `d705ae312be5324bff64f3a9540e30e8b8bd34dc`. It imports the **repaired** NF391 source-only Bessel gate and checks all inequalities using exact Python `Fraction`.

The dedicated NF392 workflow independently replays the exact source-only norm and tries the actual NF390 Arb selected moment with historical authentic signed archive ZIP SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`, unchanged all 30,371 signed WJJ/WJF archive cells, 16 physical overlap checks, true pole correction and zero new signed kernel cells. It outputs the native selected moment and optional exact combined NF391/NF392 verdict only when that native run has succeeded; no fallback or invented certificate.

**Stop rule:** if actual native output proves its certified discrepancy exceeds the candidate-specific necessary test, retire frozen j387 **only**. If it remains inconclusive, stop repeated source-only diagnostic tightening and proceed to original source-adapted physical J242 approximation or rigorous lowband integral, rather than attempting another arbitrary exterior harmonic. No *full original lowband upper*, full complement inverse, operator-domain audit, `W-ODD-NEG`, even, whole Weil or RH is discharged.
