# Weil-Lab — NF363: exact endpoint-moment cancellation on the original critical four-plane

**Date:** 2026-10-28. **Custody:** read-only local analytic/exact-rational continuation of NF362; no GitHub modification, source expansion, 242-column inverse, full `W-ODD-NEG` acceptance, or native-Arb CI claim. Original Fourier/operator-domain identification and locally sharpened exterior-floor promotion remain separately OPEN.

## 1. Decision and correction to the prior proposal

NF362's "two positive solves" count starts **after** the forcing `g=QK_-e` is available. Given an accepted original critical function `f` in the actual physical four-plane, one must first construct its `A_*`-energy-dual projection into `E=A_*^-1 J242`:

- `F=J242^perp`, `Q=P_F`; `H` is the operator associated with the positive form `a_*=A_*` restricted to `F`.
- `v_f=H^-1(QA_*f) in F`, `e_f=f-v_f in E`; hence `a_*(e_f,z)=0` for every `z in F`.
- `g_f=QK_-e_f=QK_-f-(QK_-Q)v_f`.
- Only **after** this preliminary positive exterior solve can one compute `u_0=H^-1g_f`, then `u_1=H^-1(QK_-Q)u_0` for the four-term NF362 Neumann correction. Starting from the fixed physical critical functions therefore entails **up to three** positive exterior solves per direction, not two; the first is a different forcing.

The accepted 242-dimensional physical projection and the exceedingly small `||Qf||` do not identify `e_f` or control `QA_*f`. In particular, small physical distance to `J242` does not bound the unbounded positive operator's mixed action.

There is, however, an exact original-geometry cancellation that dramatically reduces the high-frequency portion of this **first** forcing.

## 2. Exact transform and signed endpoint moments

The actual PR348 accepted four-plane has four fixed rational functions on `[-B,B]`, `B=11/10`:

`f_i(x) = sum_{n=1}^{32} a_{i,n} sin(2 pi c_n x) + b_i sinh(x/2)`, `c_n=5n/11`.

Their zero extensions are used in the *original physical Fourier form*, not a substitute spectral model. Because `2B c_n=n`, all sine generators vanish at both physical endpoints. With the Fourier convention `hat f(xi)=integral f(x) exp(-2 pi i xi x) dx`, direct integration yields

`hat{sin(2 pi c_n x) 1_{[-B,B]}}(xi) = -i (-1)^n c_n sin(2 pi B xi) / [pi(xi^2-c_n^2)]`.

At `xi=+/-c_n` the displayed rational form has a removable singularity; the sinc representation must be used for interval evaluation there. Our high tail only uses `|xi|>=32>2 max c_n`, where denominators are uniformly separated from zero.

Define exact rational alternating moments

`S_{i,2j+1}=sum_{n=1}^{32} (-1)^n a_{i,n} c_n^(2j+1)`.

The first two moment values are:

| Critical index | `|S_{i,1}|` (approx.) | `|S_{i,3}|` (approx.) | `|b_i|` |
|---:|---:|---:|---:|
| 0 | 2.18148045e-6 | 3.65743158e-3 | 989e-12 |
| 1 | 2.11777273e-8 | 2.22713953e-4 | 143e-12 |
| 2 | 1.50219409e-6 | 2.18201352e-3 | 882e-12 |
| 3 | 6.33813455e-6 | 1.05511153e-2 | 2878e-12 |

Each value is computed **exactly** as a rational from the PR348 pinned candidate, not approximated by a floating Fourier integral. These small moments are *not declared zero*.

Geometric-series identity, for `|xi|>=32`, gives

`sum_n (-1)^n a_n c_n/(xi^2-c_n^2) = S1/xi^2 + S3/xi^4 + sum_n (-1)^n a_n c_n^5/[xi^4(xi^2-c_n^2)]`.

Since `|xi^2-c_n^2| >= (3/4)xi^2` and `pi>3`, the sine high tail is bounded by

`|hat f_sine(xi)| <= (|S1|/3)|xi|^-2 + (|S3|/3)|xi|^-4 + (4/9 sum_n |a_n| c_n^5)|xi|^-6`.

The supported true-pole Fourier transform has the separately proved integration-by-parts envelope

`|hat{sinh(x/2)1_{[-B,B]}}(xi)| <= (440/837)/|xi|`,

so its contribution has coefficient `C1_i=(440/837)|b_i|` of order `1e-10`–`1e-9`. The pole is **not** set to zero in the source; `Qs=0` removes only the rank-one *output* after projecting onto the complement.

## 3. Full high-frequency squared strong-action upper (rigorous rational coefficient)

SM41's original positive multiplier satisfies `0<a_o(xi)=max(1/1000,m(xi))<=17+log|xi|` on `|xi|>=1`. For each `f_i`, put the positive envelope

`p_i(t)=C1_i/t + (|S1_i|/3)t^-2 + (|S3_i|/3)t^-4 + (4/9 sum_n |a_{i,n}|c_n^5)t^-6`.

For every *real coefficient vector* `z in R^4`, the pointwise coefficient Cauchy inequality yields

`|hat(sum z_i f_i)(xi)|^2 <= ||z||_2^2 sum_i p_i(|xi|)^2` for `|xi|>=32`.

Consequently the **entire high-frequency original positive strong-multiplier action**, including all four mixed directions, obeys the scalar Loewner upper

`||1_{|xi|>=Lambda} a_o(xi) hat(sum_i z_i f_i)(xi)||_L2^2 <= T_Lambda ||z||_2^2`,

where `T_Lambda=2 sum_i integral_{Lambda}^infinity (17+log t)^2 p_i(t)^2 dt`.

This is integrated in **exact rational arithmetic** using `Lambda=2^k` and SM41's accepted rational bound `log Lambda < (347/500)k`. For `q>1`, the integral formula is

`integral_Lambda^infinity (17+log t)^2 t^-q dt = Lambda^(1-q)/(q-1) * [(17+log Lambda)^2 + 2(17+log Lambda)/(q-1)+2/(q-1)^2]`.

Replacing `log Lambda` by its rational upper gives a strict rational outward ceiling. No sampled quadrature or rounded eigenvalue is used.

| Frequency cutoff `Lambda` | Unsigned first-denominator bound | **Two-moment exact-rational upper** `T_Lambda` |
|---:|---:|---:|
| 256 | 2.28381e-4 | **1.90319e-16** |
| 512 | 3.03050e-5 | **3.74532e-17** |
| 1,024 | 4.01435e-6 | **9.64748e-18** |
| 2,048 | 5.30892e-7 | **3.18788e-18** |
| 4,096 | 7.01015e-8 | **1.27862e-18** |
| 16,384 | 1.21704e-9 | **2.82612e-19** |

All certified values are exact fractions in the JSON; decimals are display-only. In particular,

`T_1024 < 1/10^17`, `T_4096 < 13/10^19`.

At cutoff 1,024 the two-moment rational bound is **over 4.16e11 times smaller** than the corresponding unsigned-envelope bound, without changing the original vectors or the multiplier.

## 4. What this pays for the first energy-dual projection

For each original critical combination `f=sum z_i f_i` in the strong Fourier domain, define the **complete** positive exterior forcing `b=QA_*f`. Since `s in J242`, the pole output vanishes exactly:

`QA_* f = Q P_I F^-1(a_o hat f)`.

Let `b_Lambda = Q P_I F^-1(1_{|xi|<=Lambda} a_o hat f)`. The physical support compression and Q are contractions; hence the complete, *infinite* tail satisfies

`||b-b_Lambda||_2^2 <= T_Lambda ||z||_2^2`.

If `H>=mu I` (the positive restricted operator is at least the signed exterior floor), then the projection-solve truncation error obeys

`||H^-1 b-H^-1 b_Lambda||_{a_F}^2 <= (T_Lambda/mu)||z||_2^2`.

This does **not** bound the truncated forcing `b_Lambda`, obtain the positive inverse `H^-1b_Lambda`, estimate its residual, or establish any Schur sign. It pays **only** the previously unbounded-looking *high-frequency strong-action truncation error* for the first projection. Using the locally replayed floor `mu>0.00998`, e.g. at `Lambda=4096`, the error squared is `<1.282e-16 ||z||^2`, which is comparable to (not far below) the four-plane's `~1e-16` signed-form scale. At `Lambda=16384` this specific tail error is `<2.833e-17 ||z||^2`. Native CI acceptance of the stronger floor remains open. With only the accepted older floor `~.00098323`, the same truncation pays more and may need a higher cutoff or sharper directional energy estimate.

**Important cost correction:** NF362's "two positive solves" excludes the preliminary `e=A_*`-energy projection solve. Starting from actual PR348 functions: `v=H^-1 QA_* f`; `e=f-v`; `g=QK_-e`; `u0=H^-1g`; `u1=H^-1L u0`. There are generally **three** positive solves in total per critical direction for the four-term correction, unless a separate lawful shortcut is proved.

A rational 3x3 structural control confirms that `Qf=0`, near-zero `w(f,f)`, exterior signed coercivity and zero probed coupling do **not** bound `QA_*f` on an unprobed direction. Thus the original accepted physical quotient near-zero alone cannot instantiate this projection.

## 5. Reproducibility and standing

Primary archive: PR348 successful artifact `12738593751`, local ZIP SHA256 `735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968`; `original_four_mode_critical_block.json` SHA256 `a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922`. PR348 accepted conditional Fourier/form realization and original four-dimensional critical plane remain unchanged.

- Primary exact Fraction producer: `nf363_critical_sine_tail_higher.py`.
- Primary rational report: `nf363_critical_sine_tail_higher_report.json`.
- Separate rational squared-polynomial coefficient replay: `nf363_independent_tail_replay.py` (matching exact rationals at cutoffs 512, 1024, 2048, 4096, 16384).
- Additional exact rational geometric/resonance/first-projection obstruction checker: `nf363_projection_feasibility_check.py`.

**Closure in this bounded NF:** full four-direction original **positive strong-multiplier Fourier tail** certified analytically/exact-rationally from existing physical source coefficients; first projection's low-frequency image, its physical projection against J242, any matched positive solve, and actual directional Neumann moments all OPEN. This is a local analytic proof with exact rational verification, not a GitHub native/Lean acceptance event. No code or obligation status was changed in GitHub.

**Next cursor:** implement one **correlated low-band** enclosure for `Q P_I F^-1(1_{|xi|<=Lambda} a_o hat f)` with explicit removable-resonance handling, then test one matched exterior-positive inverse residual. Stop before an extra solve or a complete 242-column computation unless that first residual passes an actual near-critical sign budget.
