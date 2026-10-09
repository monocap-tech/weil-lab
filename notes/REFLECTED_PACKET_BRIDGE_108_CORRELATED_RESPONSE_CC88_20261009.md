# CC88: recover the seventh even response without a new source

CC parent: 5c6f6540b5d1bbcea8cc30e577a105da9fe317a4 (CC87). Immutable read-only Native Source: 5f8a6c1e54a39236df253a5aae5f7be55fee74ed (NF45). Aperture is 53/50 and kappa=207/1000. Other branches are unchanged.

## Result

Computing the seventh response directly from the correlated Woodbury block certifies a positive even improvement at the exact NF44 selection witness. NF45's subtraction-based gain enclosure straddled zero. Both enclosures concern the same paid original packet; no new source or unrecorded arithmetic information is used.

| Parity | Direct response at NF44 witness | Interval width reduction | Tightened complete condensed margin |
|---|---:|---:|---:|
| Even | [1.76505e-25,2.06746e-25] | >324 times | [-8.67104e-23,-8.15441e-23] |
| Odd | [6.52733e-22,6.53118e-22] | >76 times | [4.44738e-22,4.60934e-22] |

Decimal intervals are outward summaries; JSON preserves exact rational bounds. The even packet remains indefinite. The positive gain is much smaller than the remaining deficit. The odd packet retains CC87's conditional positive sign.

## Correlated block identity

Let H7=(H6,y7) be the original high polynomials. Use the paid physical/native/source moments M=H7*H7, QH=H7*AH7 and GH=(AH7)*(AH7). With C=QH-kappa M and T=GH-2 kappa QH+kappa^2 M, the exact Woodbury denominator simplifies to

    N7=C+T/kappa=GH/kappa-QH.

The physical Gram cancels algebraically before interval evaluation. This does not remove any physical normalization, source error or domain obligation. Set W7=R*(A-kappa I)H7, obtained from the signed joined source and native crosses. Exact preservation of NF44 entries makes N6 and W6 the principal block and first six columns of these same objects.

Write N7=[[N6,n],[n*,n77]] and W7=(W6,w7). Put

    delta=n77-n*N6^-1n,
    z=w7-W6 N6^-1n.

Block inversion gives the exact identity

    R*(A3^-1-A4^-1)R = z z*/(kappa^2 delta).

Here A3 and A4 are NF44's six-source and NF45's seven-source minorants. The common G/kappa reaction cancels, and the remaining block-inverse difference factors into this outer product. The formula is compatible with NF45's scalar-defect identity but evaluates directly on original paid moment intervals. It avoids subtracting two separately enclosed full inverse reactions. For a frozen rational witness h, calculate z*h first and enclose its signed square divided by the positive denominator. Do not infer positivity from midpoint arithmetic.

## Verified rational inverse and interval custody

The validator authenticates NF45 certificates through CC87's fixed hashes and NF44 baseline certificates through CC85's fixed hashes. It forms N6 from the paid GH and QH intervals. Let J be the exact rational inverse of the symmetric midpoint matrix. Exact rational pivots prove the midpoint positive definite. The outward residual bound rho=||I-J N6||_infinity is strictly below one. Thus

    ||N6^-1-J||_infinity <= rho ||J||_infinity/(1-rho).

This bounds every inverse entry. For every compatible symmetric matrix, the same residual condition also holds along the segment from its midpoint, so no eigenvalue can cross zero; N6 remains positive definite. The directly enclosed delta has a positive lower bound, independently confirming the N7 block denominator sign. Compact outward rational rounding at intermediate matrix multiplications preserves inclusion; floating point is used only to choose the rounding grid, never to decide a sign.

Every direct response entry overlaps NF45's published response. Direct frozen-witness gains overlap its published gain intervals. The direct lower matrix K6+Delta is intersected entrywise with NF45's enclosure for the same K7. The consumer recomputes the tightened leading inverse and complete condensed margin. These checks confirm positive even witness response, negative even full condensed margin and positive odd full condensed margin. Exact block-inverse versus outer-product controls run at ordinary and small response scales, with signed-square controls spanning zero and negative intervals.

The source integrations are not rerun. The remaining-high floor A >= kappa I, surplus C positivity, original source-domain attachments and upstream physical/error payments are inherited. The new inverse enclosure and block response arithmetic are independently reconstructed here. Interval inclusion is the claim; no midpoint matrix is substituted for the original packet.

## Frontier

NF45's historical sign-straddling even response interval remains unchanged. CC88 adds a tighter positive enclosure. Selection still targets NF45's updated even witness against the seven-source minorant, using CC82/CC84/CC86 full-matrix acceptance and response conditioning. The new gain does not justify extrapolating how many columns will suffice.

The even joined sign, unconditional background floor and complete remaining-background transport remain open. The odd fixed joined packet passes conditionally, while the full simultaneous six-retained-direction sign, other 106 retained directions and collective coupling remain open. Whole-domain positivity stays certified at aperture 21/20. No whole 53/50, all-cap continuation, RH, F4, full transport or Lean closure is claimed.

## Reproduction

Run `python scripts/certify_cc88_correlated_seventh_response.py notes/cc87-source notes/cc85-source --output notes/data/RPB108_CC88_CORRELATED_SEVENTH_RESPONSE_20261009.json` from the repository root. The imported source files are immutable. The validator uses only Python's standard library and prior CC arithmetic helpers.
