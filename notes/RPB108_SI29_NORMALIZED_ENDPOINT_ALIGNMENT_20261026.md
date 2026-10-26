# Double endpoint cancellation on the actual normalized SI29 quotient

Parent custody: PR #331, fe581f3a0d48e06c197260b0e88cb6f0a3cf0f88, successful run 40398781425. The new workflow verifies the pinned original normalization run 40385192745/source/artifact/archive/JSON, retaining the actual full J470 physical projection X and dyadic transform C. W=(F-JX)C has the accepted normalized quotient and the same actual energy Schur bounded between 3328479/10^11 I and 64 I under inherited hypotheses. W-ODD-NEG remains open.

Use u=sin(2*pi*(37/64)x) and s=sinh(x/2), original J indices 0 and 469. Form A with rows [u(B),s(B)] and [u'(B),s'(B)]. Its determinant is strictly between .944 and .945. Evaluate the actual normalized 14-column endpoint jet V=[W(B);W'(B)] using the retained full projection coefficient balls. Define the EXACT REAL coefficient matrix L=-A^-1 V and the analytic representative Wtilde=W+[u,s]L. The checker encloses all 28 actual coefficients and verifies the directly reevaluated aligned jet enclosure contains zero.

The zero endpoint jets follow exactly from the defining linear system, not from a claim that a ball containing zero equals zero. Rounded midpoint coefficients do not give exact cancellation; if used, their endpoint leakage must be retained separately. The retained coefficient balls enclose the exact real construction and are not a dyadic replacement for L.

Oddness gives Wtilde(-B)=Wtilde(B)=0 and evenness of the first derivative gives Wtilde'(-B)=Wtilde'(B)=0. Three integrations by parts on the physical interval give, for every scalar combination w,

    |hat w(xi)| <= [2|w''(B)|+integral_-B^B |w'''(x)|dx]/(2*pi*|xi|)^3.

All source formulas are entire on the physical interval. This proves cubic decay for the aligned actual directions. A numerical uniform cubic-tail constant is NOT computed here; it still requires the second endpoint jet and third-derivative bounds. The script does not infer a numerical high-tail payment from the decay order alone.

The correction takes values entirely in the original J470 span. Thus the full physical quotient Gram, actual Astar energy Schur and matched forcing for J*R0=0 are unchanged. The actual energy Schur retains the prior bounds; this does not assert that the unprojected energy of Wtilde equals that of W. The calculation neither expands the source family nor replaces the full energy projection by a physical one.

Local native-ball endpoint construction passed; GitHub replay must be accepted separately. This supplies coordinates for the next full original coupling integration. Actual Astar projection, quantitative cubic-tail constant, matched forcing and inverse response remain uncomputed. Independent original Fourier/domain review, W-ODD-NEG, even/CC27/Weil/RH remain open. Draft and unmerged.
