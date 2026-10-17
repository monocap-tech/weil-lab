# LF107 — exact RC35 trial data import

LF106 commit 945b189cb489a1c6afa20440f9f7a4425abf651a passed run 38269079086, job 114878548455: cumulative targets, complete root library and unfinished-declaration rejection all succeeded. This validates LF103–LF105 with the LF106 transfer repair and supersedes LF102 as the latest full-root checkpoint.

Imports all 128 rational entries of the committed RC35 16-by-8 trial coefficient map into a local matrix literal in `rc35_trial_coefficients_parity`, in a root-imported module. Rows index Legendre modes 0 through 15; columns index physical moment targets 0 through 7. Lean checks that every opposite-parity coefficient is exactly zero. No rounded float is used; no new global data definition is introduced.

The input is certificates/rpb108_rc35_enriched_metric.json at the LF106 SHA. The literal import supplies concrete data, but the parity theorem does not certify the nominal metric solve, polynomial assembly, carrier identity, physical residual norm, or matrix Loewner bounds. Those remain separate obligations.

Local checks: exact rational parse, 16-by-8 dimensions, all 64 opposite-parity entries zero, balanced syntax and no unfinished declarations. No local Lean executable is available; LF107 must pass remote cumulative CI. Next: assemble the actual trial polynomials with x/B normalization, then their physical carrier representatives and moment pairings. No aperture positivity, F4 closure or RH is claimed.
