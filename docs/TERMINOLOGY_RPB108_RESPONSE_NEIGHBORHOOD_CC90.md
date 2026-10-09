# CC90 response-neighborhood terminology

Definitions are additive; historical statements remain unchanged.

* **Current matrix K7:** the tightened NF45 seven-source even joined lower matrix reconstructed in CC88. All geometry in CC90 is calculated after this update.
* **Reference response z:** the signed seventh-column response border reconstructed in CC88, viewed as a direction in the current retained coordinates.
* **Leading response norm:** ||u||_E=sqrt(u*E^-1u), where E is the positive leading block of K7. This is a response metric, not physical L2 distance between polynomials.
* **Effective border tau(v):** v_last-v_pair*E^-1r for the current K7 border r.
* **Normalized slope:** |tau(v)|/sqrt((-s)||v_pair||_E^2), where s is the current negative condensed margin. Slope greater than one is necessary for a rank-one response ray to pass at some strength.
* **Two-component rejection neighborhood:** simultaneous bounds on the leading response's movement in ||.||_E and the effective border's movement, each with its specified reference normalization. Both bounds are required.

The neighborhood tests proposed inverse-response directions, not physical polynomial proximity. It does not certify or reject any uncomputed native source. The standing floor A >= (207/1000) I remains a hypothesis.
