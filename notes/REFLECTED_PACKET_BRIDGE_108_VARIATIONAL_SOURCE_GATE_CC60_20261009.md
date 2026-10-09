# CC60: rational variational source certificate and native penalty bounds

Read [definitions](../docs/TERMINOLOGY_RPB108_VARIATIONAL_SOURCE_GATE_CC60.md) first. This additive integration makes CC59's conditional correlated estimate usable without an enclosed optimal inverse. It includes new exact bounds from authenticated ORIGINAL NF17/NF19 high-block entries; it computes no missing archimedean source and does not duplicate the independent NF22 producer.

## Inverse-free sufficient gate

Keep CC59's original carrier, high floor kappa=207/1000, measured high source map K, compensated source sigma, and corrected retained form S2. For ANY fixed exact rational two-by56 matrix Y, set

    rho_Y=sigma-KY,
    W0=C2(C2-kappa I),
    J(Y)=rho_Y*rho_Y+Y*W0Y.

Then the complete unmeasured response obeys T_rest<=J(Y)/kappa. Thus the matrix inequality J(Y)<kappa S2 suffices for original whole-domain positivity. Y can be selected from approximate data and frozen rationally BEFORE rigorous source integration. It need not equal the exact optimizer.

Indeed, with P=sigma*sigma, H=K*K, Z=K*sigma and V=W0+H,

    Y_star=V^{-1}Z,
    J(Y)=P-Z*V^{-1}Z+(Y-Y_star)*V(Y-Y_star).

This exact square completion proves both the gate and its relation to CC59. The displayed variational gap pays an approximate optimizer exactly; there is no need to enclose Y_star if J(Y) itself is directly certified. At Y=0 one recovers the coarse P/kappa estimate. Optimization gives CC59's majorant, not necessarily the actual complete response.

## Physical source projection must still be complete

For a low x, the rational trial modifies the finite polynomial to p_Y=(T-H2Y)x. Its source has low projection (S2-BY)x and measured high projection -C2Yx. Hence the direct source to integrate is

    rho_Y(x)=L p_Y-E(S2-BY)x+H2 C2Yx=P_U L p_Y.

The last HIGH projection term is essential: the trial-corrected polynomial does not retain the measured source annihilation of T alone. Removing only E would falsely include the measured high source as part of the unmeasured residual. The exact validator checks BOTH projections and the remaining source coefficients. All functions required remain finite linear combinations of NF21's original58 polynomial sources.

## Authenticated native penalty bounds

The source archives are the immutable first columns112/113 and second columns114/115 used in NF17/NF19, raw SHA256 respectively

    da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee
    0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad.

Their six complete original high entries retain all signed archimedean, prime and pole contributions. All24 component intervals and their full-interval compatibility are checked. The lower bounds use positive shifted diagonals and a strictly positive worst-case two-by-two determinant. The upper bounds use an interval Gershgorin row bound, not floating-point eigenvalues.

| Parity | Certified spectrum of C2 | Certified spectrum of W0 |
|---|---|---|
| Even | 2.8 < lambda < 4.19 | 7.2604 < lambda < 16.68877 |
| Odd | 2.89 < lambda < 4.02 | 7.75387 < lambda < 15.32826 |

Because f(lambda)=lambda(lambda-kappa) is increasing above kappa, these C2 bounds give the W0 bounds exactly. The [validation](data/RPB108_VARIATIONAL_SOURCE_GATE_CC60_VALIDATION_20261009.json) includes the original FULL intervals rounded outward to10^-45 and exact rational penalty bounds. It is the original native Q high block, not a source-square matrix.

In particular one may replace the actual matrix penalty by w Y*Y, taking w=1668877/100000 even or766413/50000 odd. This conservative native envelope avoids a matrix inverse and uncertain products inside the penalty. It loses some correlation sharpness, so failure is still inconclusive.

## Source-error certificate with a rational trial

Suppose rhohat_Y directly approximates the COMPLETE trial-corrected projected source and ||rho_Y-rhohat_Y||<=eta in physical operator norm. For any t>0,

    J(Y) <= (1+t)rhohat_Y*rhohat_Y
            +(1+1/t)eta² I+w Y*Y.

Comparing this explicit upper matrix with kappa times a certified LOWER enclosure of S2 gives a sufficient sign test. The radius must pay every source sector, all projection coefficients including the C2Y high term, and all interval and truncation errors. Exact rational Y adds no coefficient enclosure error of its own. A finite list of approximate source coefficients does not certify eta or the omitted high tail. No native eta is provided here.

An exact scalar control uses the CC59 aligned high model c=3,k=3,S2=4, a rational Y=17/100, and source radius eta=1/1000. With t=1/10 and the conservative ORIGINAL EVEN native penalty envelope w=16.68877, the certified upper J is746426453/10^9=0.746426453<kappa S2=0.828. The coarse P/kappa gate fails because P=1. Thus a rational approximate correction and paid source error can certify the refined estimate without computing its exact optimizer. The control's source radius is abstract; only the penalty envelope is taken from genuine original arithmetic.

## Rank limitation and near-critical consequences

Since Z has two rows, ker(Z) has dimension at least54 in each56-dimensional retained parity. For x in ker(Z), the optimized J equals P exactly; no choice of Y improves this direction. This kernel is not the measured source kernel ker(B*), and it is not a kernel of the complete source. In particular, every three-dimensional retained subspace has a nonzero vector in ker(Z). This applies to the actual NF19 three-dimensional low-energy Ritz planes without identifying them as full-operator critical eigenspaces. Whether the coarse estimate succeeds on such blind vectors remains unevaluated.

If a variational gate passes on a vector, the positive penalty implies

    ||Yx||² < [kappa/w_lower] S2(x,x).

For either parity kappa/w_lower<3/100. Thus on the certified NF19 low three-planes, where A(x,x)<10^-20||x||² even or10^-17||x||² odd and S2<=A, any passing correction must obey ||Yx||²<3*10^-22||x||² even or3*10^-19||x||² odd. This is a necessary bound for this estimator, not a bound on the actual unknown optimum or proof that the gate fails. It identifies the scale on which native correlations must be measured. A rank-two gain can address aligned directions but cannot establish a lower frame over all retained directions by itself.

## Exact checks and standing

[Validator](../scripts/validate_variational_source_gate_cc60.py), [validation](data/RPB108_VARIATIONAL_SOURCE_GATE_CC60_VALIDATION_20261009.json), [custody](data/RPB108_VARIATIONAL_SOURCE_GATE_CC60_CUSTODY_20261009.json): both authenticated native source hashes,24 source-component interval checks, two high spectral enclosures, five rational variational gap identities, both physical projection identities, a paid-error passing gate and a blind three-plane control pass. The validator also replays CC59's three genuine crossings and three positive ground eigenlevels with whole-mass shifted nulls; these remain abstract controls, not native crossings.

NF22 arrived during publication recovery: independent source head1261995ecc9ce80351ab3cfbaf802929444fe92e and additive integration handoff b67b87731ca7bb1fd7daa318642217c35adb0527 are preserved. NF22 certifies original arch-source squared norms on e0/e1 in (7.082144075590,7.082144075591) even and (1.083143528165,1.083143528166) odd, keeping endpoint logarithms exact and bounding a degree320 regular expansion. Its combined complete-source values are explicitly numerical diagnostics, not certificates: the arch-prime/pole cross terms remain the next arithmetic task. It supplies no full compensated native residual, H,Z or CC59/CC60 gate.

After the missing signed cross integrals, the next native witness test can fix a rational Y, integrate rho_Y and pay its physical error radius, then compare the positive source norm plus native penalty to kappa S2. A directional result will not certify the collective56-dimensional gate. Failure of any sufficient estimator is not native negativity. The minimal exact condition remains T_rest<S2, and the requested cap-uniform old-gap-independent leakage and defect-relative lower frame require further original arithmetic estimates. No logical nonimplication from complete Weil identities is claimed. Whole positivity21/20 remains; target53/50, actual contact exclusion, RH/F4, full transport and Lean remain open. Historical wording and paused fronts remain intact.
