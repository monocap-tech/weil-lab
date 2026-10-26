# Actual aligned SI29: quantitative cubic Fourier tail

The active W-ODD-NEG remains open. Parent is draft PR #332, commit 06b833b276a8c717eb46efe55d6d8b339f2e87e2, passing run 40402266617. The new workflow pins successful original normalization run 40385192745, source, artifact and hashes, then reconstructs the same exact-real endpoint system from its retained full J470 projection and C. It does not replace exact real alignment by midpoint coefficients.

For the actual normalized W=(I-P_J470)FC and its aligned representative Wtilde, compute all original 484 physical third-derivative inner products, propagate the full projection and exact-real anchor-alignment enclosures, and obtain the entire 14x14 D3=Wtilde'''*Wtilde''' plus second endpoint vector e2=Wtilde''(B). Regularized sine/cosine primitives extend recursively through powers -10. The entire actual 14-feature third-derivative Gram is independently checked with degree-255 Taylor series and explicit third-derivative tail payments; these check the new negative-power formulas. Polynomial source and pole terms use the already established positive-power physical integration recurrences.

The exact zero endpoint value and first derivative justify three integrations by parts on the physical interval. For each coefficient vector y,

    |hat(Wtilde y)(xi)|^2 <= P ||y||^2/(6^6 |xi|^6),
    P = 8 ||Wtilde''(B)||^2 + 4B tr(D3),

where oddness gives equal absolute second endpoint values and Cauchy-Schwarz bounds the third-derivative L1 norm. The dyadic enclosures yield a rational outward P upper using exact Fractions. The defining endpoint system establishes exact zeros; containment of zero in the reevaluated endpoint balls is only a numerical consistency check.

For R=2^k>=1, t=(7/10)k>log R, the inherited original Ao high-frequency majorant gives the complete two-sided matrix tail bounds

    energy tail <= (2P/6^6) [(17+t)/5+1/25]/R^5,
    Ao strong squared Fourier tail <= (2P/6^6)
        [(17+t)^2/5+2(17+t)/25+2/125]/R^5.

The log bound follows from the positive exponential Taylor inequality exp(7/10)>2. The output retains full D3 and endpoint enclosures, P, and all exact dyadic-cutoff payments. The strong bound concerns the Ao multiplier, not an asserted Astar pole-action tail. The energy tail bounds the aligned representative's Fourier contribution and does not alone certify errors for all full-J energy-projection entries or mixed source terms.

This supplies the previously missing numerical cubic constant. It is a conservative tail-feasibility check; a listed cutoff is not a resource commitment to integrate every frequency cell up to it. It neither computes actual Astar projection/entries nor matched forcing or inverse response. The full-J quotient and energy Schur are unchanged by alignment; prior Schur bounds remain inherited, not rederived from the new representative's unprojected energy. W-ODD-NEG, independent original analytic/domain review, even/CC27/Weil/RH remain OPEN. Draft and unmerged; local arithmetic and GitHub acceptance are separate.

Local feasibility result: P<2^95. The first tested dyadic cutoffs meeting energy-tail tolerances 1e-6, 1e-9 and 1e-12 are respectively 2^21, 2^23 and 2^25. At cutoff 4096 this particular upper bound exceeds 4.6 million. These are limitations of the retained uniform third-derivative certificate, NOT lower bounds on the true tail and NOT a theorem that all cubic-tail methods fail. They do not authorize a brute-force integration to those large endpoints. Further work should seek frequency-local packet bounds or sharper coupled derivative data before choosing an integration grid.
