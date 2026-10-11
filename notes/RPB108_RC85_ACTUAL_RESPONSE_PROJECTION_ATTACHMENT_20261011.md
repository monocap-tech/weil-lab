# RPB108 RC85 — actual rank-38 response and original-source attachment

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `227e8c94a22a51995d9fd54ae1faa2e8b740ab33` (RC84).

## Result

RC85 attaches RC83's fixed canonical response and RC84's direct error
certificate to the actual rank-38 Riesz projection. It pays the original
source uncertainty using the unchanged projected transfer certificate
from RC82. It also constructs a sharper actual head Gram upper enclosure.

The new response attachment is certified, but RC82 remains the stronger retained source bound: `2061/4096 = 0.503173828125`. No source-bound improvement is asserted.

The rank is still 38, the source still has 22 inputs, and the canonical
trial dimension is still 64. The original Riesz trials and RC83 response
coefficients are unchanged. No enlarged source covariance or new Weil or
complement floor is evaluated. The scalar source budget remains open.
Generation and independent replay: **PASS**.

## Why this is an actual projection attachment

Let `S = i* F_nom`, `Z` be the RC83 polynomial response, `e = S-Z`, and
`Pi` be the actual rank-38 projection from RC70. The head Riesz vectors
`R_j = i* P_j` use physical Legendre targets `P_j`, `0 <= j < 38`.
This is the same head as RC70's native basis, by the exact invertible
Chebyshev–Legendre conversion.

The response is a vector in the canonical physical-polynomial trial space.
It does not automatically lie in the Riesz head. Its exact head pairings
are nevertheless available from the Riesz identity:

`Y_jk = <R_j,Z_k>_can = <P_j,Z_k>_phys = mass_j Z_jk`.

If `M` is the actual head Gram, then

`Gram_can((I-Pi)Z) = Gram_can(Z) - Y' M^-1 Y`.

RC85 bounds this expression using the actual metric enclosure and an
actual head Gram upper matrix, rather than a nominal projection.

## Sharpening the actual head Gram upper

Convert RC70's fixed 64-mode head trials to Legendre targets, giving `V`.
Their first 22 columns equal the corresponding RC67 trials exactly.
RC81 supplies their complete canonical Riesz-error upper matrix `E_low`.
For the additional targets 22–37, RC85 evaluates 16 physical squared-norm
enclosures for `P_j - L_nom V_j`, using the recentered order-192 canonical
operator formula. It pays the same actual strong-operator correction
`delta_L = 2 radius(c56) + (4/3)(192+64)42^193/193!`, with Young parameter
`1/65536`, and transports through `i*`. The resulting individual canonical
error bounds are rounded upward at `10^-30`.

There are eight additional errors in each parity block. Cauchy–Schwarz
bounds their joint Gram by eight times the diagonal of individual squared
norm bounds. No uncomputed high-target cross covariances are treated as
zero. With a positive block Young parameter `nu`, the full head error Gram
is bounded by

`E_head = diag_blocks((1+nu) E_low, (1+1/nu) 8 diag(E_high))`,

separately in the even and odd sectors. The cross blocks vanish in this
upper matrix because their contribution has been paid by Young's inequality.
The true cross errors are not asserted to vanish.

For the canonical trial metric center `G` and lower enclosure `G_lo`, let
`J = X' V`, where `X` is the diagonal physical target mass embedded in 64
rows. The exact Riesz-error identity gives

`M = J + J' - V' G_actual V + Gram_can(R-V)`.

Thus `M_up = J + J' - V' G_lo V + E_head`, after upward Loewner rounding
at `10^-24`, is an upper bound for the actual head Gram. Exact rational
checks certify positivity and consistency with the RC70 Ritz lower matrix
`M_lo`. Whole Loewner improvement over RC70's generic `rho D38` upper
matrix is certified.

Let `G_up` be the actual trial-metric upper enclosure. Then

`Q = Z' G_up Z - Y' M_up^-1 Y`,

with upward Loewner rounding, bounds `Gram_can((I-Pi)Z)`.

## Response error and original source uncertainty

RC84 certifies the physical covariance upper matrix `B84` for
`F_nom - L_actual Z`. Consequently

`(I-Pi)e = (I-Pi)i*(F_nom - L_actual Z)`

has Gram bounded by `E_tail = tau38^2 B84`, using RC82's adjoint tail norm.
The global canonical error upper is `E_global = rho B84`, also supplied
by RC84. No second tail or embedding factor is applied to either matrix.

The unchanged RC82 matrix `E_transfer` bounds the projected difference
between the actual original source `i*(q+K_actual iR22)` and `S`.
It includes the original Riesz error and the nominal Weil-operator
approximation error. This differs from the canonical strong-operator
correction already paid in RC84. Both are accounted for here.

A triangle/Young attachment of `Q`, `E_tail` and `E_transfer` is valid but
remains weaker than RC82. The certificate records that calculation as a
comparison. The tighter attachment retains the response's near-orthogonality
to the entire 64-mode canonical physical-polynomial trial space.

## Certified trial-space orthogonality defect

Let `H` and `R_H` be the center and radius of RC83's 64-by-22 physical
source-pairing table, and `D` the 64-mode physical mass matrix. The actual
response-error pairings with the trial basis are

`d_actual = H_actual - G_actual Z`.

Writing `d = H - GZ`, the finite metric uncertainty has mass bound
`delta_G`, so

`d_actual' D^-1 d_actual`
`<= 3[d' D^-1 d + box(R_H' D^-1 R_H) + delta_G^2 Z'DZ] = Omega`.

Here `box(K)` is the diagonal matrix of row sums of the nonnegative-entry
matrix `K`. It pays every independent pairing interval perturbation.
The three-term inequality is Cauchy–Schwarz, and `G_actual >= D` implies
that `Omega` also bounds the canonical covariance of the projection of
`e` onto the 64-mode trial space. `Omega` is rounded upward at `10^-60`.
It is a certified defect enclosure, not an assertion of exact Galerkin
orthogonality in the actual metric.

## Actual projection coefficients and the retained cross term

The true head coefficient matrix is `A_true = M^-1 Y`, while the computable
one is `A0 = M_up^-1 Y`. Exact relative comparisons certify, in each parity,

`M_lo >= (1-eta) M_up`, and `E_head <= kappa M_up`, with `eta < 1`.

In the `M_up` norm, the inverse perturbation satisfies

`(A_true-A0)' M_up (A_true-A0)`
`<= [eta/(1-eta)]^2 Y' M_up^-1 Y`.

A paid Young inequality therefore bounds the covariance of
`(R-V) A_true` by the recorded matrix `F`:

`F = (1+v) A0' E_head A0`
`  + (1+1/v) kappa[eta/(1-eta)]^2 Y'M_up^-1Y`.

The true coefficients are not evaluated exactly. The certificate uses
these inverse enclosures to pay their uncertainty.

Since `R A_true = Pi Z`, write

`(I-Pi)Z = (Z - V A_true) - (R-V) A_true`.

The first parenthesis lies in the 64-mode trial space and has canonical
Gram at most `6 Z'G_up Z + 4F`; this follows from two applications of
Cauchy–Schwarz and `||Pi Z|| <= ||Z||`. Its cross pairing with `e` is paid
using `Omega`. The second parenthesis is controlled by `F`, and its cross
pairing with `e` is paid using `E_global`. With `sigma = 10^-20` and positive
`w`, the nominal projected source upper is

`N = Q + E_tail + sigma(6 Z'G_up Z + 4F) + Omega/sigma`
`  + w F + E_global/w`.

This bounds `Gram_can((I-Pi)S)` while retaining the small trial-space defect.
Finally, for positive `u`,

`Gram_can((I-Pi)S_actual) <= (1+u) N + (1+1/u) E_transfer`.

All displayed matrices, rounding allowances implicit in the recorded
Loewner matrices, and relative comparisons use exact rational arithmetic.
The parameter searches are finite certificate searches, not claims of
continuous or global optimality.

## Verified bounds and retention

Each displayed factor is checked against the RC67 original 22-input
canonical Gram lower matrix. The old or new upper is retained independently
in each parity sector, which is valid because the actual source covariance
and projection preserve parity.

| Parity | Uncorrelated response attachment | Correlated response attachment | RC82 | Retained |
|---|---:|---:|---:|---:|
| even | 413/512 = 0.8066406250 | 2499/4096 = 0.6101074219 | 2061/4096 | 2061/4096 |
| odd | 3067/4096 = 0.7487792969 | 1175/2048 = 0.5737304688 | 471/1024 | 471/1024 |

Whole Loewner improvement of the new source matrix over the RC82 source
matrix is not certified; the retained factor comparison is made separately in each parity block. The retained scalar factor is a certified upper bound,
not a measured leakage value or an actual error-reduction claim.

## Independent replay

The additional 16 operator residual diagonals are regenerated with
reflection-reduced logarithmic moments and checked inside the saved
rational enclosures. Replay verifies projection capture by solving
`M_up A0 = Y` and computing `A0' M_up A0`, rather than only multiplying
by the inverse on both sides. It independently reconstructs the final
source attachment sum, repeats the exact positive-semidefinite and
relative-Gram checks, and requires equality with the saved JSON certificate.
All nine direct input SHA-256 hashes and their cross-provenance links are
checked. Generation and independent replay both pass.

Repository replay command:

```bash
python scripts/validate_rpb108_rc85_actual_response_projection_attachment.py --replay certificates/rpb108_rc85_actual_response_projection_attachment.json
```

## Remaining scope

The scalar source budget remains uncertified. No actual rank-38 failure,
38-input original source covariance, enlarged Weil or complement floor,
whole-aperture positivity, RH, F4 or Lean result is asserted.
The source and head correlations can still be tightened; the limited
high-target diagonal calculation deliberately pays uncomputed correlations
with Cauchy–Schwarz rather than evaluating their full Gram.
