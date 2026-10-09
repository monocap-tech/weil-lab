# CC90: quantitative rejection neighborhood for the next even response

CC parent: d1838e8bca1dc4a0003af312414c5855dfb17d38 (CC89). Read-only source: NF45 5f8a6c1e54a39236df253a5aae5f7be55fee74ed, unchanged. Other branches are unchanged. Aperture is 53/50; the original remaining-high floor A >= (207/1000)I remains an explicit hypothesis.

## Result

CC89 excluded arbitrary amplification of one even response ray relative to the six-source base. CC90 now works at the current seven-source matrix, which already includes that credit, and certifies a neighborhood of response directions that also cannot repair the even certificate at any strength.

The seventh response's normalized slope in this current geometry is strictly below 61/100. If a proposed next response remains within both 19-percent drift bounds defined below, its normalized slope is at most 80/81, below the required value one. Its full-matrix orientation therefore fails independently of its positive denominator or hypothetical strength.

No next original source has been evaluated. This is an acceptance screen for its paid inverse-response data, not a test of distance between physical polynomials. It does not convert small physical overlap, physical orthogonality or similar-looking coefficients into a sign conclusion.

## Current-matrix proof

Write K7=[[E,r],[r*,c]], E>0, s=c-r*E^-1r<0, and d=-s>0. Define ||u||_E^2=u*E^-1u and tau(v)=v_last-v_pair*E^-1r. Let z be the independently rebuilt seventh response border, a=||z_pair||_E^2>0. The rational interval calculation proves

    tau(z)^2/(d a) < (61/100)^2.

The enclosed squared ratio is [0.25731,0.36955], using the current tightened seven-source matrix. It is not the six-source ratio used in CC89.

For a proposed next response v, suppose BOTH conditions hold for the same exact paid matrix and response:

    ||v_pair-z_pair||_E <= (19/100) sqrt(a),
    |tau(v)-tau(z)| <= (19/100) sqrt(d a).

The norm triangle inequality gives ||v_pair||_E >= (81/100)sqrt(a). The effective-border triangle inequality gives |tau(v)| <= (80/100)sqrt(d a). Thus

    |tau(v)| / sqrt(d ||v_pair||_E^2) <= 80/81 < 1,
    d ||v_pair||_E^2 - tau(v)^2 >= (161/10000) d a > 0.

For any b>0 and lambda>=0, the complete condensed margin after adding lambda v v*/b is

    s + lambda tau(v)^2/(b+lambda ||v_pair||_E^2).

Its credit ceiling is below d, so it remains negative for every lambda. This conclusion uses the already updated K7; it does not neglect the seventh credit when assessing a proposed eighth response.

Response normalization is free for this orientation screen: scaling v and b by alpha and alpha^2 leaves its matrix credit invariant. If a nonzero rescaling puts a candidate in the stated neighborhood, the ray fails. Physical source normalization does not amplify inverse credit. A candidate outside the neighborhood is unresolved; it need not pass.

## Validation and application

The companion validator independently reruns CC88's authenticated moment/inverse calculation, obtains the tightened seven-source matrix, recomputes its condensed geometry and certifies the rational slope bound. Exact controls attain the worst-case neighborhood slope 80/81, preserve negative/null/positive cone crossings, show that either drift bound alone is insufficient, and distinguish good orientation from sufficient paid finite strength.

To use the screen, reconstruct a candidate's response v=(A-A4)y acted against A4^-1R, with its proper positive Woodbury denominator and all original signed/source payments. Enclose the two drift inequalities in the current matrix metric. Only proving both justifies rejection by this neighborhood. Failing to prove them yields no conclusion. Passing a witness response alone remains insufficient; CC82's complete cone decides the actual finite-strength sign.

This is a one-new-response screen. A correlated multi-column packet must use CC84/CC86's full span metric. No assertion that separately rejected response rays imply rejection of their joint packet is made. The same distinction matters for physical source combinations.

Native integration is not rerun, no new source polynomial is certified, and the background floor is not proved. Odd's fixed joined packet retains its conditional pass. Even sign, complete remaining-background transport, the simultaneous six-retained-direction result, other 106 retained directions and collective coupling remain open. Whole-domain certified aperture remains 21/20. Whole 53/50, old-gap-independent all-cap continuation, RH/F4, full transport and Lean closure are not claimed.

## Reproduction

Run `python scripts/certify_cc90_even_response_neighborhood.py notes/cc87-source notes/cc85-source --output notes/data/RPB108_CC90_EVEN_RESPONSE_NEIGHBORHOOD_20261009.json`. The immutable NF45 and NF44 files and prior CC rational helpers suffice.
