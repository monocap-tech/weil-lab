# NF409 — Actual 16-cell screen conflict; exact original signed principal weights and continuous-z acceptance gate

**2026-10-31 PT. Active W-ODD-NEG OPEN; RH OPEN.** No source changes, no new signed kernel cells, no merge, no general domain transfer. All investigations concern the unchanged original fourth u4, full signed seven-prime arch multiplier, original J242 support [-11/10,11/10], NF404 dyadic pole centering, and NF407 original physical g=p+z with p=q+r known analytically.

## Previous / current / next

**Previous NF408:** Original 242+4 source coefficient radius accepted to full m(D) supported L2 error <1e-745, first true full signed physical action point sampled provisionally, and exact source-cancellation-first continuous original physical z formula. NF408 16-cell full norm pilot was still running.

**Current NF409:** The NF408 physical 16-cell pilot finished. TWO outer resolutions produce **contradictory outcomes** relative to original NF404 acceptance cap:

- C (original NF404 source-exact necessary sufficient gate): approximately 1.09505377311842130765508e-21.
- 2-node each positive original source cell: E2 approximately 1.00556144888668981182995e-21, BELOW C.
- 4-node each positive original source cell: E4 approximately 1.10888703738754228311475e-21, ABOVE C.
- Absolute discrepancy: 1.03325588500852471284802e-22, over two thousand times original available exterior power budget gamma² approximately 5.12968e-26.

The successful GitHub workflow #41218841422 completed a **NUMERICAL SCREEN**, not a norm certificate. No monotonic interpolation or conventional two-mesh difference constitutes a lower/upper interval. Thus the real original norm criterion is neither accepted nor refuted.

**Next NF410:** source-native, correlation-preserving interval/Taylor physical evaluator of the continuous original z, with nested arch integration, genuine source seam support checks and exact signed principal quadrature weights; prioritize the observed numerical hotspot cells 6,3,7. Do not spend another undirected pass increasing all Gauss nodes.

## A. Independently validate continuous original source action in two forms

NF409 evaluates the same exact source at x=B/2=0.55 and x=1.09 using (i) original complete compact arch+7 signed prime action and post-subtraction of q+r, and (ii) NF408 analytically stable, jump/log-free continuous z expression. The apparent uncalibrated differences are 3.09740938312426e-16 and 9.54167643560368e-25.

These are fully explained by one explicitly measured Gaussian quadrature residual: the original compact action approximates the integral of u4(x) K(t)/2 from t1 to t2, while the stable formula computes that term exactly as u4(x)[J(t1)-J(t2)]/2. Independent Gauss quadrature of known K on the SAME grid explains the complete discrepancy. After subtracting that known finite quadrature mismatch, the residuals are about 4.76e-56 and 1.81e-55 respectively, at display precision. This verifies the algebraic original two-form rewriting NUMERICALLY, not its common x/t integral error or exact source norm. CI #41220105704 SUCCESS; historical failed attempts #41219904869 and #41220093038 preserved. Durable original source data NF409_original_continuous_two_form_pilot.json.

## B. Source-EXACT analytic signed q+r integral on every physical cell

NF407 already certified all seven original prime seam jumps, the endpoint logarithm and complete principal power ||p||² approximately 2.126406994276591e-21. NF409 provides exact signed integral weights, so later z×p correlations never require numerical quadrature of either discontinuous r or logarithmic q.

For original B=11/10, original signed v=u4(B)<0, seven c_n=Lambda(n)/sqrt(n)>0, x_n=|B-log n|, define H(d)=d[1+log(B/d)], H(0)=0. Then for any positive support cell [a,b],

Integral_a^b q(x) dx = (v/2)[H(B-a)-H(B-b)].

Integral_a^b r(x) dx = v Sum_n c_n max(0,b-max(a,x_n)).

On x>0, p(x)=q(x)+r(x)<0. Source exact Fraction arithmetic using original NF406 rational seam enclosures, original NF407 signed v/c_n intervals and rigorous log series produces all EIGHT positive original cell integrals, all strictly negative, and independently reproduces the global source half-support integral

Integral_0^B p(x) dx = (v B/2)+v Sum_n c_n(B-x_n) approximately -2.9329044382676e-11.

This is a **true original source-exact integral** of the KNOWN p, NOT a measurement of z or of the full centered original scalar. CI #41220241790 SUCCESS, durable NF409_original_principal_cell_integrals_exact.json.

## C. Explicit future rigorous norm-acceptance contract

Because p is negative on each positive cell, if a future INDEPENDENT native interval encloser proves z(x)∈[lo_i,hi_i] for ALL x of each original cell (or subcell), then

hi_i Integral_i p ≤ Integral_i z p ≤ lo_i Integral_i p.

Also, cell width times min/max_{t in [lo_i,hi_i]} t² bounds Integral_i z².

The true source norm obeys the exact odd-reflection identity

||g||² = ||p||² +2 Sum_positive_cells Integral z² +4 Sum_positive_cells Integral z p.

All p integrals and ||p||² are already source EXACT with outward rational enclosures. The only remaining unmeasured quantities are **verified continuous-z interval ranges** and x/t integration errors. No z interval envelopes exist yet, so no original centered scalar certification can be claimed.

Alternatively certify ||z-z_pc||_{L2(I)}≤eps for a source-attested piecewise constant approximation z_pc. Its entire E_pc=||p+z_pc||² is algebraically computable from original signed exact p-cell integrals. If ||p+z_pc||≤R and E_pc+2R eps+eps²≤C, the original full centered bound follows. A fixed prospective exact entry budget R=3.32e-11 and eps=9e-17 costs

2R eps+eps² = 5.9760081e-27 < gamma²/8.

This is a **conditional acceptance policy**, not a certificate of any numerical pilot. The accepted original full multiplier source-radius error <1e-745 is negligible compared with this proposed physical quadrature budget, but the physical quadrature error is not bounded.

## D. Physically localize the preliminary numerical disagreement

Reconstruct each original positive physical cell's SIGNED contribution to the E4-E2 delta as

Delta E_i = 2*(z2_positive_4-z2_positive_2) +4*(zp_positive_4-zp_positive_2).

The three largest absolute provisional differences are:
- cell 6, from -B+log7 to -B+log8: +1.64712013735e-22;
- cell 3, from -B+log4 to B-log2: -1.53210887480e-22;
- cell 7, from -B+log8 to -B+log9: +9.66953173187e-23.

These account for more than 80% of sum of absolute signed cellwise variations. They partly cancel globally. The near-origin cell 1 adds only approximately 6.71e-28 to this intermesh difference, which is **not** an upper on its true error. This is a numerical refinement order, not an a posteriori verified error estimator. Source pilot was copied byte-identically from original NF408 branch and Git blob pinned 70ae4fac5061b6d4583c22097f9fe9fed687d482 before analysis, to preserve late-arriving parent evidence without overwriting old research. Source exact arithmetic on unverified numerical decimals is appropriately typed as a reproducibility diagnostic only; inspect its CI before acceptance.

## Disposition

ACCEPTED: source-exact signed known p cell integrals, independent global overlap, source-resolved original coefficients and source interval error.

NUMERICAL ONLY: two-form continuous action, 2/4-node contradictory original full physical pilot, prioritized cell variation.

OPEN: actual full original z L2 interval, signed z/p cross interval, whole centered physical positive scalar, fourth original physical lowband upper, general original domain, exterior inverse, W-ODD-NEG and RH.

**Next bold NF410:** rigorous original continuous physical z function enclosure/correlation first, not further unvalidated global Gauss mesh.
