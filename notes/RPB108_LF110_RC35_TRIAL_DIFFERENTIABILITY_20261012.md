# LF110 — RC35 trial differentiability

Adds differentiability over the reals for all eight exact normalized RC35 physical trial functions. Rational polynomial evaluation is transferred through the real coefficient map, normalized by x/B, summed with exact coefficients and composed with the real-to-complex embedding. Adds the explicit real derivative formula containing the normalization factor 1/B. These formulas also remain valid at B=0 under totalized division, although the actual certificate uses B=11/10.

This supplies differentiability, not yet the full complex derivative witness and its interval-integrability, quantitative trial/derivative bounds or physical carrier construction. Those are required before consuming the cap-domain and residual interfaces. No residual enclosure is inferred from polynomial regularity.

Local syntax and unfinished-declaration scans pass. Lean is unavailable locally. LF109 run 38298753815, job 114976192561, passed targeted checks and was running the root build when inspected. LF106 (945b189cb489a1c6afa20440f9f7a4425abf651a, run 38269079086) remains the latest confirmed full-root checkpoint. LF110 requires cumulative CI. No aperture positivity, F4 closure or RH is claimed.
