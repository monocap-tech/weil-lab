# SM59 — Original 25-source rank-aware inertia and leafwise coupled negative bounds

October 19, 2026. Canonical W-ODD-NEG remains OPEN. Stacked on SM58 PR #241.

## Verified source results

SM57 corrected focused Actions 39275848672 SUCCESS: full original 25 physically supported odd sources, 973 original SI10 signed-negative whole-real leaves, 25×25 genuine signed LOWER, source-reference lower inertia (0 positive,25 negative,0 zero).

SM58 corrected focused Actions 39281588617 SUCCESS: full 25 original sine/xcos/sinh Fourier covariance and derivatives, exact all-source mixed negative UPPER. Its trace 12.99524585115 is much smaller than SM57 diagonal majorant trace 86.419118373857. The five certified global negative-upper convex mixes t=0,1/4,1/2,3/4,1 yield exact original 25-source signed LOWER negative inertia 24,25,25,25,25 respectively. The coupled-only t=0 lower has one positive direction, 24 negative reference directions, none zero. All negative inertia belongs only to the LOWER reference, not necessarily the actual signed operator. The actual original 25-source restriction's negative index has not been exactly classified.

Full passing SM58 Actions artifact 12201213066 carries its 25×25 matrix, source artifact SHA-256 568d088af18a705748c4ed5d04a9baf2f2d7a0dc2f8994f1914bb3bc8eabb9d7; SM57 source artifact 12197969921. A pinned compact summary is committed under certificates/rpb108_sm58_full25_signed_summary.json.

## SM59A — Actual finite 25-source negative-index ceiling 23

The independently certified SM52 signed original physical 2×2 coupled sine2/xcos17 LOWER is

    [1.070559452403   0.003816       ]
    [0.003816         1.437706842403]

which is strictly positive definite by exact Sylvester minors (Actions 39205091881 SUCCESS). SM52C verified original physical L² coercivity W_odd(h)>=69/200 ||h||² on this genuine two-source plane. SM59A uses original full 25×25 physical Gram interval and exact SM42 rational-preconditioned Gershgorin to certify the 25 physical sources are independent, and that sources 2,17 lie within them with their true common center 1845/128.

For the actual original signed form on V25=span(g0,...,g24), any actual negative-definite subspace N is disjoint from the strictly positive plane P2=span(g2,g17). Thus dim(N)+2<=25, and

    ACTUAL n_minus(Wodd restricted to V25) <= 23.

This is strictly better than the ceiling 24 obtained from the globally conservative SM58 LOWER by inertia monotonicity. It is a valid dimension theorem, not a claim that the SM58 reference lower is PSD.

Do NOT splice the positive SM52 2×2 block into the SM58 25×25 LOWER: the missing cross terms of that replacement have no proved Loewner error and can invalidate the bound.

The exact finite-source next obligation is the true 23-dimensional signed Schur block: in a basis P2 ⊕ P2-perp-H, the actual 25-source signed form Q has blocks [A B; B^T C], A>0, and inertia negative(Q) = negative(C-B^T A^-1 B). Neither the actual signed B,C nor the entire physical orthogonal remainder is currently certified.

## SM59B — Local 25-source negative upper selection

The entire SI10 973-leaf true signed-negative Fourier operator admits BOTH SM57's source-cap diagonal UPPER and SM58's full-source affine covariance UPPER. On each individual original signed real leaf one may select either fully valid Loewner UPPER. Choosing smaller exact-rational TRACE on each leaf yields an independent 25-source upper with raw trace no larger than either original entire trace. That alone is NOT Loewner dominance or inertia positivity. Additional independently valid source2, source17 and pole24 diagonal-targeted leaf selections are allowed, with full exact 25×25 signed LOWER and true rational inertia acceptance. No actual negative witness may be inferred from negative lower eigenvalues.

The complete 470-source Astar inverse, infinite original odd orthogonal remainder, O1/O2, even E1-E4, full Weil form, CC27 and RH remain OPEN. Independent original Fourier/form-domain and SI10 negative-support mathematical audit is separate from Actions.
