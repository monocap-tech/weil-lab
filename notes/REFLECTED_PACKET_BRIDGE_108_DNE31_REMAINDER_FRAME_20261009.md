# RPB108 — DNE31: complete native border and frozen optimized remainder

Read [DNE31 terminology](../docs/TERMINOLOGY_RPB108_DNE31_REMAINDER_FRAME.md) before the definitions below.
Parent DNE30: 1daea791c7fe90a355183d19bcf78dd95edc1664.
Only research/rpb108-direct-null-exclusion is written. Phase, Coupled and Aperture are untouched.

## Result

DNE29's optimized four-column source credits could not yet be used on a concrete remaining frame: its complete native border and energy projection were uncomputed. DNE31 calculates every original native pairing between that frame and DNE24's 52-column remainder in each parity. It also reconstructs and tightens the full tested native matrix directly from the original sources, then freezes an exact rational approximate projection.

All 104 resulting remainder polynomials are exactly specified and can be expanded by the materializer. The complete native border of the frozen frame is bounded; it is not assumed to vanish. No remaining native energy, remaining complete source Gram, new positive retained direction or whole-aperture sign is certified.

| Certified quantity | Even | Odd |
| --- | ---: | ---: |
| Complete new T4/W52 native border entries | 208 | 208 |
| Fresh T4 native matrix entries | 16 | 16 |
| Primary / replay regular orders | 660 / 700 | 660 / 700 |
| Primary / replay directed Decimal digits | 780 / 800 | 780 / 800 |
| Frozen remainder polynomials | 52 | 52 |
| Scaled native border operator norm upper | <1.441e-16 | <8.023e-21 |
| Sufficient required native floor relative to raw W mass | <1.328e-28 | <7.266e-38 |
| Inherited optimized complete-source credit c | 0.11 | 0.14 |

The required floor is a sufficient input threshold, not an established lower bound on the remaining form. In particular DNE24's raw W floor cannot simply be transferred to the differently lifted hatY frame.

## Complete original native integration

Reconstruct T4 using the exact selected DNE29 polynomial coefficients, with normalized Legendre bases available through degree 180. The pinned DNE16 source helper supplies the original singular harmonic polynomial, regular archimedean convolution, endpoint logarithms, signed pole and all clipped translations for prime powers {2,3,4,5,7,8} in both orientations. No shift in the physical form is introduced.

The seven positive half-interval cells represent every original translation cell by reflection parity. For each of the four source polynomials, calculate all needed monomial moments once. Convert these to original normalized Legendre source coordinates and pair with the exact rational W columns. This reorganization computes the full four-by-52 border without repeating 52 full source reconstructions.

The endpoint primitive is the original exact polynomial-division log primitive, including its endpoint limit. The regular source error is bounded uniformly by

    eta_N = 2a*(550/19)*(106/125)^N + 3*10^-99,
    a=53/50.

Each border entry pays eta_N times the full physical norm of its T4 source polynomial and the outward physical norm of its W test. The error concerns the original source, not a sampled approximation. A directed rational storage grid of 10^-110 is applied outward. Truncated native intervals are rounded first, and their original-source errors are then paid explicitly in exact rational arithmetic.

The same source coordinates reconstruct all 16 native T4 matrix entries in each parity. Every fresh interval overlaps the inherited DNE29 matrix. Primary N=660 and replay N=700 enclosures are nested for all 416 border entries and all 32 tested matrix entries. The fresh matrix box intersects both transpose orientations, both source orders and the inherited box; the result is symmetric and contained in the already authenticated native box. Thus the existing A_s>q I theorem still applies.

Initial N=360/400 diagnostics already paid the complete border but exposed uncertainty from the older T4 native box as the main projection-error term. They are superseded for this certificate by the higher-order source runs; no mathematical failure of the actual remainder is inferred from those wider boxes.

## Exact frozen projection and residual

Let A4=Q(T4,T4), P=Q(T4,W52), A_s=S A4 S and P_s=S P. The scale S and q are inherited from DNE29: q=1/25 even and 7/50 odd. The matrix midpoints choose a rational J on a 10^-60 grid. This is only a candidate selection. Define

    K=S J,
    hatY=W52-T4 K,
    E_s=P_s-A_s J=S Q(T4,hatY).

Every entry of E_s is enclosed using the complete new border and tightened tested matrix. The certificate sums their squared absolute maxima to give f2. Therefore

    ||E_s||^2 <= ||E_s||_F^2 <= f2,
    ||A_s^-1 P_s-J||^2 <= f2/q^2.

This pays the finite coefficient projection error without treating the midpoint inverse as exact, computing an infinite inverse, or setting the mixed native border to zero.

The exact retained components of T4 have the same span as DNE24's four constraints. W52's free-coordinate block is the identity. Each frozen column satisfies the exact polynomial identity

    hatY_j + sum_i T4_i K_ij = W_j.

Consequently the quotient by the tested retained span is unchanged. T4 and hatY retain full rank 56 per parity; adding all F112 vectors still gives the whole original aperture domain. The hatY columns can include finite high coefficients through degree 180. They need not be physically or natively orthogonal. Their exact normalized Legendre coefficient masses and outward physical norms are retained and independently recomputed.

## Native-border interface for the remaining calculation

The raw W physical mass satisfies G_W>=I because its free-coordinate minor is the identity. Thus

    ||A_s^-1/2 E_s G_W^-1/2||^2 <= f2/q.

If the remaining original native matrix hatB=Q(hatY,hatY) is certified to satisfy hatB>=b G_W, then

    ||A4^-1/2 Q(T4,hatY) hatB^-1/2||^2 <= f2/(q b).

The equality of this norm with its scaled version follows by congruence of the native forms; no Euclidean identity is assigned to the nonorthogonal physical frame.

For

    b > 16*kappa^2*f2/(q*c^2),
    kappa=11/25,

the native mixed dual norm is below c/(4*kappa). Together with the still-required complete original projected source estimate

    Gamma_hatY <= (c/2) hatB,

DNE25's rational criterion applies: r+kappa*epsilon<c. The full native-plus-source block would then certify whole 1.06 positivity with all infinite high modes. This conclusion remains conditional. Neither hatB nor Gamma_hatY is computed here. A full signed matrix comparison may be preferable to this conservative scalar allocation.

## Validation and custody

The independent validator imports no producer code and passes 19,705 exact rational checks. It checks original and optimized retained constraints, the identity free minor, every source-error payment, all nested native intervals, symmetric tested-matrix intersection, all rational projection coefficients, every mixed residual endpoint and its Frobenius payment. It reconstructs all frozen polynomial identities and exact physical masses. The materializer independently expands both 52-column packets and verifies their masses against the certificate.

Full three-coordinate native/source controls cross positive, null and negative while their individual diagonal native energies and eliminated high block remain positive. Their Schur determinant is 16/25-e^2 for e=3/5,4/5,1. At e=4/5 the exact original null is (1,-4/5,-3/5). Three positive whole-physical-mass shifts preserve that vector at the corresponding positive eigenlevel. These are abstract controls, not original Weil countermodels.

DNE30 was recovered and reproduced in both modes: its consumer passes 61 assertions per run and its independent validator passes 2,760 checks. The new scripts pass syntax checks. Custody records every new artifact, decoded import and pinned inherited input hash. No prior file is overwritten.

## Remaining frontier and scope

The optimized native border and a concrete rational remainder frame are now available. The next original calculation is the complete 52-by-52 native energy and complete F112-projected source Gram for these frozen columns, with all mixed correlations and source approximation errors. Testing only diagonals or selected source shells would not discharge it.

DNE29's eight-direction positive restriction and common physical guard 2.4*10^-35 are unchanged. The uncovered retained dimension is still 104. Whole 1.06 positivity, unit-response exclusion on that remainder, all-aperture continuation, RH/F4/full transport and Lean remain open. This is an original finite native-source calculation and exact rational validation, not Lean closure.

## Reproduction

For each parity, run `certify_dne31_native_border.py` with DNE16_ORDER=660 and DNE16_PRECISION=780 for primary, and DNE16_ORDER=700 and DNE16_PRECISION=800 for replay. Each takes the parity and `--output` path. Encode the resulting JSON with deterministic gzip mtime=0 and base64, retaining its exact decoded bytes.

Run `certify_dne31_remainder_frame.py parity primary replay output` to freeze the map and pay the residual. Run `validate_dne31_remainder_frame.py` with even primary, even replay, even frame, odd primary, odd replay, odd frame, followed by `--output validation.json`.

To expand a frozen packet, run `materialize_dne31_remainder.py frame primary selected_T3 output`. The selected T3 is the inherited DNE29 selected-column file of the same parity. The materialized file has the same exact polynomial-column schema as that inherited input and includes all 52 remainder columns.
