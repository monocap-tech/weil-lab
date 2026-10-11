# RPB108 RC86 — complete correlated head error covariance

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `edf97c7802cbb26f6a6153395c42a7916d00a648` (RC85).

## Result

RC86 evaluates the complete physical strong-operator residual Gram for the
38 actual Riesz head targets, replacing RC85's low/high block Young and
additional-target diagonal Cauchy–Schwarz envelope. It attaches the full
correlated error matrix to the actual head Gram, response projection, and
original source. The retained source factor is
`2061/4096 = 0.503173828125`.
The new candidate improves on RC85’s response candidate in both parity
sectors, but neither beats the previously retained RC82 source bound.
The certified reduction in the retained upper factor is `0`.

The head rank remains 38, original source input count 22, and polynomial
trial dimension 64. RC70/RC67 Riesz trials and RC83 response coefficients
are unchanged. The scalar source budget remains open.
Generation and independent replay: **PASS**.

## Complete covariance and actual operator transport

Write `R_j = i* P_j`, where the targets `P_j` are physical Legendre modes,
and convert RC70's fixed trial matrix to these targets: `V = V_native C38^-1`.
The first 22 columns equal `V67_native C22^-1` exactly. The residuals are
`r_j = P_j - L_nom V_j`, for `0 <= j < 38`.

All 741 upper-triangular entries are accounted for. Opposite-parity entries
are exactly zero (361). Same-parity entries number 380: RC81's 132 low-target
entries and RC85's 16 additional-target diagonals are preserved exactly;
232 previously missing off-diagonal entries are calculated. No uncomputed
same-parity correlation is discarded.

The recentered canonical operator uses its order-192 regular/logarithmic
kernel expansion. Signed interval moment evaluation gives the complete
nominal physical Gram enclosure. If its midpoint is `Q_center` and `a_i`
is the sum of interval radii in row `i`, then

`Q_up = Q_center + diag(a)`

is a Loewner upper by the symmetric row-sum bound. Entries are rounded
outward on the `10^-20` rational grid. Every resulting PSD claim is checked
with exact fractions.

The strong-operator correction is

`delta_L = 2 radius(c56) + (4/3)(192+64)42^193/193!`.

For the physical trial Gram `T = V'DV` and `t = 1/65536`,

`B_head = (1+t)Q_up + (1+1/t)delta_L^2 T`,

rounded upward in Loewner order on the `10^-30` grid, bounds the actual
physical residual covariance. With `rho = 252/257`,

`E_head = rho B_head`

bounds the complete actual canonical Riesz-error Gram `Gram_can(R-V)`.
The diagonal upper-bound improvement factors over RC85 range from
`1.250000000` to `40.000000000`. Diagonal comparisons
and whole-matrix comparisons are reported separately.

## Actual head and response projection

Let `G_lo, G_up` be RC67's actual 64-mode metric enclosures, `X` the physical
Legendre mass matrix embedded in 64 rows, `J = X'V`, and `M` the actual
38-target Riesz Gram. The exact identity

`M = J + J' - V'G_actual V + Gram_can(R-V)`

provides `M_up = J + J' - V'G_lo V + E_head`, rounded upward at `10^-24`.
The validator checks `M_up >= M_lo`, using RC70's converted actual Ritz
lower matrix. This bound is on the actual Riesz head.

For the fixed RC83 response `Z`, exact Riesz pairings give `Y = X'Z`.
Consequently

`Gram_can((I-Pi38)Z) <= Q = Z'G_up Z - Y'M_up^-1Y`,

again with upward Loewner rounding. Replay solves `M_up A0 = Y` and checks
`A0'M_up A0 = Y'A0`, independently of the generation contraction.

## Complete original-source attachment

Use the unchanged RC84 response-error bounds `E_global = rho B84` and
`E_tail = tau38^2 B84`, and unchanged RC82 projected actual-source transfer
upper `E_transfer`. The certified trial-space response error projection
upper `Omega` is reconstructed from the RC83 pairing intervals and RC67
metric enclosure. It is checked exactly equal to RC85's `Omega`, as are
`E_tail` and `E_transfer`.

The true projection coefficients are `A_true = M^-1Y`; they are enclosed,
not substituted with their computable approximation `A0 = M_up^-1Y`.
Exact relative comparisons certify `M_lo >= (1-eta)M_up` and
`E_head <= kappa M_up`, with `eta < 1`. Their inverse perturbation and a
paid Young inequality bound `Gram_can((R-V)A_true)` by

`F = (1+v)A0'E_head A0 + (1+1/v)kappa[eta/(1-eta)]^2 Y'M_up^-1Y`.

RC86 uses 32 rational bisection steps for the internal relative uncertainty
and balancing estimates, avoiding coarse quantization of small coefficient
errors. Final reported source factors use the existing 12-step exact PSD
bisection. All searches give certified upper bounds; global optimization
is not claimed.

For `sigma = 10^-20` and positive `w`, the trial-space orthogonality defect
and full correlated head error give the nominal source upper

`N = Q + E_tail + sigma(6 Z'G_up Z + 4F) + Omega/sigma + wF + E_global/w`.

This follows from `(I-Pi38)Z = (Z-V A_true)-(R-V)A_true`: the first term
lies in the 64-mode trial space, and the second is bounded by `F`.
The response-error cross term is paid by `Omega` for the first term and
`E_global` for the second. A final Young inequality attaches the actual
original source uncertainty:

`A_source = (1+u)N + (1+1/u)E_transfer`.

Each parity searches 15 rational `(w,u)` pairs around certified balancing
weights. The resulting covariance upper and relative input comparisons
are checked exactly. The smaller RC85 retained or RC86 candidate factor
is selected separately per parity, justified by exact parity preservation.

## Verified comparisons

| Exact whole Loewner comparison | Certified |
|---|---|
| head_Riesz_error_whole_Loewner_improves_RC85 | False |
| head_Gram_upper_whole_Loewner_improves_RC85 | False |
| projected_response_upper_whole_Loewner_improves_RC85 | False |
| coefficient_error_upper_whole_Loewner_improves_RC85 | True |
| new_response_attachment_whole_Loewner_improves_prior_retained | False |

A false comparison means that this particular whole-matrix improvement is
not certified; it does not invalidate either upper bound.

All source factors compare to the unchanged RC67 original 22-input
canonical Gram lower matrix.

| Parity | RC85 candidate | RC86 candidate | Prior retained | RC86 retained |
|---|---:|---:|---:|---:|
| even | 2499/4096 = 0.6101074219 | 591/1024 = 0.5771484375 | 2061/4096 | 2061/4096 |
| odd | 1175/2048 = 0.5737304688 | 565/1024 = 0.5517578125 | 471/1024 | 471/1024 |

These are certified upper factors, not measured leakage values. The
certificate records every parameter candidate, interval, rounding row
allowance, diagonal comparison and final retained matrix.

## Independent replay and provenance

Replay regenerates all 380 same-parity entries using reflection-reduced
six-term logarithmic moments, rather than the generation nine-term form,
and checks containment in the saved rational enclosures. This includes
all reused entries. It independently contracts the physical trial Gram,
reconstructs projection capture by an exact solve, and rebuilds the final
source sum through a separate expression. All exact PSD and relative-Gram
checks are repeated, and the complete result must equal the saved JSON.
All ten input SHA-256 hashes and cross-provenance links are checked.

Repository replay command:

```bash
python scripts/validate_rpb108_rc86_complete_head_error_covariance.py --replay certificates/rpb108_rc86_complete_head_error_covariance.json
```

## Remaining scope

No scalar source budget, actual rank-38 scalar-budget failure, 38-input
original source covariance, enlarged Weil or complement floor,
whole-aperture positivity, RH, F4 or Lean result is asserted.
