# NF607 — residual custody accepted; gamma and prime costs certified

Stacked on NF606 #638. All new NF607 changes await compilation.

## New verified results

- NF606 run 44213681897 job 134498063691 accepted the generic real residual bound, row-specific selected coefficient box and literal unweighted physical H,V,w attachment. No hypotheses about interval enclosure, actual frame or solution were silently discharged.
- NF606 job 134498064136 independently passed the stricter fixed-frame 8192-bit residual route: all 242 row payments and four critical coordinates PASS in 76.18 s. The output was uploaded as artifact 14386734683, size 1148613 bytes, zip SHA256 c496a7954300cb6bdb4556c1b85ffffcf01037a11e8d593fabbe075a0f0f16ab. This is rigorous Arb verification of the real residual hypotheses, not yet a Lean proof of these inequalities. Verified from CI logs; artifact not downloaded in this turn.
- NF605 run 44211798238 job 134491740435 and NF600 run 44211798260 jobs 134491739674,134491739855: gamma lower thresholds, complete gamma integral lower theorem (conditional on integrability), actual log9 prime bound, Fourier mass and graph lower-bound transport all LEAN PASS. Thus the archimedean lower bound 104/125 (once the literal integral integrability and normalization are attached) and prime cost 2/5 have certified mathematical proofs. The pole module failed at parsing of adjacent |* and ≤m tokens, not a reported counterexample; downstream coercivity was blocked. Independent remote dominance compiled as dependency of the analytic nonzero module, which failed on two fun_prop goals for critical analytic terms. NF607 repairs those by introducing the point as in accepted NF551. No complete local positivity theorem yet.
- NF605 permanent endpoint assembly still running at final inspection. All 275 individual kernel checks, literal receipt sign and aggregate already accepted as documented earlier.

## Literal analytic entry attachment

NF606 moment recurrence had four diagnostics: real-to-complex cast of 1, two missing pow derivative elaborations, and unreduced lambda in product rewrite. NF607 imports Deriv.Pow, differentiates real powers before complex embedding, fixes simplification, and reduces the pointwise product goal.

Each original selected mode has two exact complex exponential-polynomial terms: sin uses ±1/(2i), cos uses +1/2 for both signs, true sinh pole uses ±1/2 at exponents ±1/2. The original four critical probes retain all 32 weighted sines and a weighted sinh pole each (33 two-term blocks). For terms t=(c,m,z), u=(d,n,w), their integrated product is cd J_(m+n)(z+w). New candidates bind all 242² original unweighted Gram entries to four exact moments per entry, and all 968 mixed entries to 33 such blocks. The same literal selected/critical complexification lemmas previously certified by NF588 are reused. No weighted collar Gram substitution, no quadrature or new source data.

## Next

Verify the repaired pole module and literal archimedean normalization, complete local coercivity; compile the exact moment dictionary and then bind the outward arithmetic for H,V, historical frame and actual transformed solution. The residual theorem and independent numerical validation are now both accepted in their respective systems, but the formal real inequality attachment is open. No new NF607 numerical run or local Lean build, no main merge. Global Weil positivity, full U400 kernel truth, W_ODD_NEG and RH remain open.
