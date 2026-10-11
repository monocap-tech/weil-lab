# RPB108 RC83 — source-specific canonical trial response

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `5f83f7b33a81773c8929f98cc0ec5f825b6149a1` (RC82).

## Result

RC83 certifies 704 same-parity physical Legendre pairings of the complete
nominal source against modes 0–63, preserves all first-38 pairing enclosures
from RC71 exactly, and constructs a rational 64-mode canonical trial response.
It certifies this response using the actual canonical metric enclosure.
The response-error upper matrix is smaller in Loewner order than the
zero-response upper matrix. The 22 diagonal upper bounds fall by
44.5055%–61.2996% relative to that zero-response comparison.

This is a response construction for the complete **nominal** source. It does
not improve the RC82 actual rank-38 projected-source bound, which remains
`2061/4096 = 0.503173828125` relative to the original canonical input Gram.
The scalar source budget remains open.

## Dimensions and source

| Object | Dimension or rank | Meaning |
|---|---:|---|
| Source inputs | 22 | Existing native features 0–21 |
| Original Riesz trials | 64 × 22 | Unchanged RC67 coefficients used in the source |
| New canonical trial response | 64 × 22 | Physical Legendre trial vectors in canonical space |
| Actual Riesz projection head | 38 | Unchanged RC70 projection target rank |

The nominal source is `F_nom = q + K_nom V64`, with the original RC67 Riesz
trials. It includes the RC68 archimedean source forms, all fourteen signed
prime translations on fifteen support segments, and the signed pole term.
The pairing table contains 704 nontrivial same-parity enclosures and 704
exact zero mixed-parity entries. These are interval enclosures, not asserted
exact nominal pairings. The new response is a trial approximation to
`i* F_nom`; its coefficients are not substituted into the original source.

The canonical trial space here is the canonical span of physical Legendre
polynomials. It is distinct from the actual rank-38 Riesz head, which spans
adjoint images of physical Legendre polynomials. Consequently this trial
response does not automatically vanish under the rank-38 complementary
projection.

## Certified response and bounds

Write `H` for the midpoint of the physical pairing enclosure table and `R_H`
for its entrywise radius, `G` for the RC67 canonical metric center, and
`D = diag(11/[5(2n+1)])` for the physical mass matrix. RC67 supplies
`G - delta D <= G_actual <= G + delta D`, with `delta = 1849/10^30`.

The exact rational center solve is `Z_exact = G^-1 H`. Each entry is rounded
to the nearest multiple of `10^-40` to produce `Z`. Mixed parity stays zero.
Let `T = Z' D Z`, `Q = |Z|' R_H`, and let `A_H` be the diagonal matrix with
row sums of `Q + Q'`. For every pairing table admitted by the intervals,
`Z' DeltaH + DeltaH' Z` lies between `-A_H` and `A_H` in Loewner order.
Thus the total uncertainty allowance is `A = A_H + delta T`.

Define

`L_raw = H'Z + Z'H - Z'GZ - A`.

The variational identity implies `L_raw <= Gram_can(i* F_nom)`.
It also lower-bounds the canonical Ritz capture in the 64-mode trial space:
for any input vector the true Galerkin response maximizes
`2 <Z, i* F_nom> - ||Z||_can^2` over that space.
The published `L` is a downward Loewner rounding of `L_raw` at `10^-24`,
with the diagonal row-sum rounding allowance recorded explicitly.
Exact rational LDL checks certify `L >= 0`.

Let `U` be the complete nominal physical source Gram upper matrix from RC68
and `rho = 252/257`. The canonical embedding gives
`Gram_can(i* F_nom) <= rho U`. Therefore

`Gram_can(i* F_nom - Z) <= rho U - L_raw`.

The published error upper matrix is an upward Loewner rounding of the
right-hand side at `10^-24`. It is positive semidefinite, and
`rho U - error_upper` is positive semidefinite. The same error upper also
bounds the true 64-mode Galerkin projection error, since the Galerkin
response minimizes the canonical approximation error. Separate lower and
upper matrices for `Z'G_actual Z` are also certified and recorded.

These bounds are for the actual canonical metric applied to the nominal
source. No RC68 source-approximation uncertainty or RC81 original-Riesz
error has yet been attached to this new response certificate.

## Conservative whole-input error comparison

Both columns below compare the indicated covariance upper matrix to the
RC67 original 22-input canonical Gram lower matrix. The comparisons are
certified separately in the two parity blocks.

| Parity | Zero-response upper factor | New trial-response error upper factor |
|---|---:|---:|
| even | 2207/512 = 4.3105468750 | 2383/1024 = 2.3271484375 |
| odd | 4293/1024 = 4.1923828125 | 5495/2048 = 2.6831054688 |

These factors concern the unprojected nominal-source trial response error.
They are not replacements for the smaller RC82 rank-38 projected-source
factor, and are not measured errors. The diagonal fractional reductions are
comparisons of certified upper matrices, not claims about the actual error
reduction.

The variational bound still uses the generic `rho U` upper matrix for the
source norm. The next usable interface is the explicit rational response
`Z`: a direct covariance of `F_nom - L_nom Z`, followed by actual operator
and source uncertainty transport, can target the response residual without
this generic source-norm subtraction. That work is not part of RC83.

## Validation and independent replay

Generation uses ordinary polynomial prime-segment moments, separate left
and right archimedean logarithmic moments, and exponential moment series.
Independent replay uses affine segment coordinates and binomial moment
reconstruction, reflected archimedean logarithmic moments, and the closed
exponential-moment formula. Every regenerated pairing is checked inside the
saved enclosure. The first 38 enclosures are checked against RC71 as well.

Replay independently checks the response square-completion identity

`H'Z + Z'H - Z'GZ = H'G^-1 H - (Z-Z_exact)' G (Z-Z_exact)`

and every center normal equation. It checks all recorded exact-rational
positive-semidefinite and relative-Gram comparisons, then requires exact
JSON equality with the saved certificate. All dependency SHA-256 hashes
are recorded, with the RC70, RC68, RC71 and RC82 provenance links checked.
Generation and independent replay: **PASS**.

Repository replay command:

```bash
python scripts/validate_rpb108_rc83_nominal_source_canonical_response.py --replay certificates/rpb108_rc83_nominal_source_canonical_response.json
```

## Scope retained

No actual original-source attachment to the new response, projected
rank-38 response evaluation, enlarged source-input covariance, scalar
source-budget closure or actual rank-38 failure is certified. No new Weil
floor, complement floor, whole-aperture positivity, RH, F4 or Lean claim
is made. RC82 remains the retained actual projected-source certificate.
