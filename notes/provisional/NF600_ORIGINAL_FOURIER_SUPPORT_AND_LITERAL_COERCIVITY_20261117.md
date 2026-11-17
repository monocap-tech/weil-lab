# NF600 — formalize literal two-collar Fourier, prime and pole budget

Stacked on NF599 #631. New NF600 proof scripts are compiler-pending.

## Verified NF599-head receipts

- NF598 run 44183095880 job 134392328066: full actual signed graph form/literal EF, exact smooth signed limit and relative margin transfer, and physical graph-lift uniqueness all LEAN PASS. Corrected-source wrapper remains blocked.
- NF598 job 134392327486 and NF596 run 44183099733 job 134392341017: full cached/reduced block checker soundness LEAN PASS, including analytic high-degree discharge 250..399 and the 250-order conditional collar budget. Checker truth is still NOT kernel-certified. Endpoint sign cast failed, and NF600 repairs the particular cast by binding its rational threshold to a local variable before casting. No acceptance claimed for repair.
- NF599 run 44183096877 job 134392338829: strengthened scalar two-collar margin budget LEAN PASS; actual digamma gamma-lower build failed by final inspection, logs not yet recovered. Support-transfer step not yet reported. The graph-correction core and terminal specialization remain under compilation; do not infer a pass.
- Prior exact 800-endpoint executable replay, qualitative original uncorrected graph and full source interval soundness remain verified. No fresh numerical replay in NF600.

## New mathematical simplification

Use the unitary Mathlib Fourier coordinate ξ, not an integral over a moving threshold 30/(2π). The original collars E have total measure 1/250. With physical energy m=||s||², Hölder on E gives ||s||_1<=sqrt(m/250); hence |Fourier(s)(ξ)|²<=m/250 at every ξ. On the larger FIXED low band (-5,5), the total energy is <=10*m/250=m/25. Outside, |−2πξ|>=30 since π>3. Plancherel gives total Fourier energy m. The actual complete gamma-weighted integral, with NF599's thresholds −28/5 and 11/10 and integrability, is therefore >=104m/125. This is not a truncation of the high-frequency integral. No separate small numerical U400 premise.

## Six new candidate modules

1. CollarPrimeGeometry: exact measure, actual difference support |t|<1/500 or 549/250<|t|<11/5. For every integer n>=2 other than 9, log n is outside this set (log2 lower, log8 upper, log10 lower). The log10 estimate uses exp(11)<10^5 from exp(1)<11/4. Log9 positive overlap must cross left to right.
2. CollarFourierMass: support L1 bound from the genuine restricted-measure Hölder theorem, exact Schwartz Plancherel, pointwise density and low-band bounds.
3. CollarPrimeBound: identify literal window correlation with the actual Schwartz autocorrelation using a.e. translation; reduce complete infinite prime sum to n=9, bound each signed translated overlap by m/2 using pointwise 2ab<=a²+b² on opposite collar masks, paid once using translation invariance. Exact von Mangoldt(9)=log3, log3<6/5, coefficient <=2/5. Thus |Re prime|<=2m/5.
4. CollarPoleBound: actual two exponential moments each <=2||s||_1 since exp(11/20)<=2. Preserve both Hermitian cross terms, bound |Re pole|<=8||s||_1²<=4m/125.
5. CollarArchLower: split full gamma-weighted Fourier integral on the fixed low band and its complement, with no omitted tails.
6. CollarCoercivity: weighted density integrability from Schwartz decay and existing actual gamma growth; actual literal EF correlation spectral identity at −2πξ, exact rescaling of the full integral, and split into actual gamma/prime/pole costs. Candidate universal 2/5 smooth support margin and graph transfer for all original coefficients using the already accepted uncorrected seed graph. No original moment correction is needed for local coercivity.

The final mathematical target is nonnegative relative margin (2/5)||physical K||²<=S(K), not strict at the zero vector. Nonzero original source (e.g. from a certified endpoint sign) would imply strict positivity. New Lean build has not been run locally; all new attachments are candidates, and upstream actual digamma proof still needs recovery. No source-specific sign certificate or global positivity claim. Full kernel-checker truth, exact solve custody, terminal canonical correction and global Weil coercivity remain open. No main merge, W_ODD_NEG or RH claim.
