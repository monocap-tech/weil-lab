# NF578 — genuine 242-column kernel accepted; recover finite Gram and physical graph builds

Stacked on NF577 PR #608. No new accepted Lean results from NF578 yet.

## Verified NF575 compiler receipts

Actions run 44016585418, job 133815866848, on NF575 head 3ff64b64350b47b8b32a5911c4ef1c00ae5f15c3:
- ActualZetaOriginalJ242SquareKernelTransport built successfully.
- ActualZetaOriginalJ242Actual67BlockCoverage, Original68RootBudget, QuadraticRootMultiplicity, Actual67BlockHermiteCompleteness, and ActualOddJetKernelClosure all built successfully. The entire actual 242-column real left-kernel theorem neutralNF568OriginalActual242OddJetMatrix_leftKernel_zero is accepted, including all 241 original oscillators and genuine sinh pole. No numerical rank or Gram assumption occurs.
- The two accepted modules supply the mathematically unconditional right-kernel result via the existing NF569 composition; global combination differentiation and the terminal canonical Gram module are still not accepted.
- NF575 physical strip-log build failed on one diagnostic at line 32; the log dyadic envelope failed at line 103. Downstream modules could not be established from that job.

## Repairs

Three existing files repaired in response to actual CI:
1. Global combination jets: use simp for finite-order vs infinity regularity rather than le_top, and expose the last Fin row's Nat value and isLt.
2. Strip log carrier: unfold the continuum weight before the integrability theorem rather than simp at the mismatched target function.
3. Log dyadic envelope: explicitly prove 1 <= 2+abs(t) for log_nonneg.

All changes are proof-script candidates, not altered definitions or new assumptions.

## New independent Lean module

ActualZetaOriginalEndpointSeedGeometry defines actual affine compression at c=1099/1000 and real convolution with displacement radius (1-s)/2000, for the original half-collar (549/500,11/10). It proves candidate pointwise strict support of the integrand/convolution and exact oddness of the reflected seed. This is a pointwise integral definition, not an abstract seed hypothesis. It does not prove existence of a smooth unit-mass mollifier, its transform identity, smoothness or ordinary L2 convergence.

The module also implements exact high- and low-frequency rational scalar comparisons for the NF577 strip constant 1/40000 after the analytical split/log estimates. The underlying endpoint integration by parts remains to be formalized.

## Local arithmetic

Re-read actual NF494-native.zip and recomputed SHA, full 400 outward U intervals, Cauchy tail and derivative-tail in Python Fraction in this pass. Exact gates M0<2e-7, M1<7e-4, U(B)<-1e-11 and both strip scalar constants pass. Approximate values: M0=1.9659655557684862e-7, M1=6.957098822919963e-4, U(B) upper=-1.16798644909683e-11; tails 4.076412541946651e-121 and 8.153897824035919e-116. The two sufficient rational tests have left sides 1.26268032e-5 and 1.6032e-6, each less than 1/40000. Inherited holomorphic-source certificate and actual binding in Lean remain distinct obligations.

A focused GitHub workflow checks Gram and the independent new geometry, then the carrier/graph chain in separate steps even after a failure. No new axiom, sorry, or admit intentionally introduced. No local Lean compiler installed. No main merge.

Next: verify full Gram and correction, formalize the convolution transform and physical L2 limit, then the original endpoint integration estimates and frozen coefficient/source binding. Full signed Weil coercivity, W_ODD_NEG, RH OPEN.
