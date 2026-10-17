# LF111 — complex polynomial derivative interface

Adds a classical complex-valued derivative witness for a rational polynomial evaluated at x/B, using LF110's exact real derivative and the continuous linear real-to-complex embedding. Adds interval-integrability of that explicit derivative on any finite interval, derived from its continuity. Normalization 1/B is retained and endpoint vanishing is not assumed.

These interfaces apply to every rational polynomial mode in the concrete RC35 assembly. Finite trial sums still need their explicit combined derivative witness, cap bounds and physical carrier identification before the residual consumer is instantiated. No numerical residual estimate is supplied here.

Local structural and unfinished-declaration scans pass. Lean is unavailable locally. LF110 run 38300895232 was pending; LF109 run 38298753815, job 114976192561, had passed targeted checks and was running the root build. LF106 (945b189cb489a1c6afa20440f9f7a4425abf651a, run 38269079086) remains the latest confirmed full-root checkpoint. LF111 requires cumulative CI. No aperture positivity, F4 closure or RH is claimed.
