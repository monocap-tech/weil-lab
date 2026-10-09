# CC72 — signed source mixtures improve directional certificates

Definitions: docs/TERMINOLOGY_RPB108_SIGNED_MIXTURE_CC72.md. Integration parent CC71: ae03e419ef9b975ee219806873c755b4d3149982. Read-only producer NF28: 1b227864aa6398e59922fde470f371fb9b72dc11.

## Complete original mixed source information

NF28 constructs the complete signed physical high-source Gram of the NF26 corrected trial v and the NF27 exact retained response w. Both complete sources include the original archimedean endpoint logarithms, all thirteen prime translation cells, the pole source and every mixed source-sector cross. The source replacement and projection errors are paid before any matrix sign comparison. Rational grid 10^-500, regular kernel N320 and pole degree40 are inherited unchanged.

The fresh unmodified producer replay and independent unsquared native-projection replay are recorded in the custody certificate. The latter uses authenticated original N720/K620 pairings against e118 even and e117 odd, independently of the squared source Gram. The two-direction native energy form is positive. The coarse joint matrix Q2-Gamma/kappa is rigorously indefinite: its v diagonal is positive, w diagonal negative and determinant negative.

In particular, the original source-square/energy ratio for w lies in (0.69827,0.69829) even and (0.80553,0.80554) odd, above the floor budget0.207. This confirms the unchanged unlifted-background estimator failure from CC70 using a complete actual source witness. It rejects the estimator, not the original form, and does not undo CC71's finite116 positivity.

## A positive trial survives finite retained elimination

The new consumer evaluates the complete original native energy and source Gram on u_alpha=v-alpha w. At alpha=1, the retained direction is x-w, not x. The directional score has rigorous lower bounds

    even > 8.4700e-37,
    odd  > 6.9480e-32.

Thus subtracting this frozen finite retained response does not destroy the positive original directional infinite-high Schur certificate. This conclusion uses the complete source of the actual mixture; it is not the invalid subtraction of NF27's finite reaction from NF26's separate score. The signed covariance is load-bearing.

## Signed-source selection improves the bound

Since U_ww<0, the coarse score f(alpha)=U_vv-2alpha U_vw+alpha^2 U_ww is concave. The midpoint optimum selects a weight only; then all proof comparisons use exact rational interval arithmetic. Frozen weights are

    even alpha=-608041/1000000,
    odd  alpha=106817/1000000.

Their rigorously paid directional score lower bounds exceed

    even 3.7358e-36,
    odd  7.5729e-32.

In each parity the selected score lower bound exceeds the original v score U_vv upper bound from the same complete NF28 Gram. This is a certified improvement of that sufficient directional bound, not an improvement claim about the unknown exact Schur value. The even selected mixture adds w rather than subtracting it; finite energy minimization and source-aware score selection need not choose the same sign.

The retained physical mass is computed exactly as ||x-alpha w||^2=||x||^2+alpha^2||w||^2. Dividing the score by this mass supplies a physical retained Schur lower bound. Exact reflection parity gives zero cross term, so the two selected opposite-parity directions span a positive two-dimensional original Schur restriction. The alpha=1 pair separately gives another such restriction. None of these modified directions is asserted to be an actual critical eigenvector.

## Why this still does not assemble the matrix

The same U is indefinite. Any invertible change of trial coordinates within span(v,w) preserves that fact by congruence. Choosing a better direction cannot make the entire fixed two-direction coarse restriction positive. The original true Schur matrix may still be positive; its inverse metric remains uncomputed.

Let T=R* C^-1 R and Delta=Gamma/kappa-T>=0. Repairing the w diagonal necessarily requires

    Delta_ww > Gamma_ww/kappa-Q_ww.

The exact consumer publishes a lower bound on this necessary credit and on its fraction of the floor-based w response. The fraction exceeds70% even and74% odd. These are necessary reduction targets for the current unlifted w, not established credits or sufficient collective conditions. In addition, the signed inverse mixed term must meet the determinant budget. Knowing the sign of the physical source covariance does not determine the sign of its inverse-weighted counterpart.

CC71's high lifts genuinely change the trial space and therefore can evade this fixed-span obstruction. The next collective task is still to certify the complete residual Gram of a jointly lifted retained family, or obtain the signed true-response matrix. These scalar mixtures are probes and restricted sign certificates, not a replacement for that matrix calculation.

## Controls and reproduction

Three exact controls have matrices [[1,1/2],[1/2,1/4+s]] with s=-1/100,0,1/100. Their determinants are s, while the tested first direction stays positive on both sides and at the genuine null crossing. Three physical near-critical congruences scale the first direction by1e-18: its score is1e-36 and the determinant is1e-36*s. Three whole-mass shifts of the positive-semidefinite null matrix by1/1000,1/10,2 have those exact positive ground levels. These distinguish directional success, a genuine collective crossing and positive ground levels. They concern the explicitly identified matrix test, not complete Weil countermodels.

```sh
python3 scripts/certify_native_mixed_high_sources_nf28_106.py notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF26_FIXED_TRIAL_CC69_20261009.json notes/data/RPB108_NF26_SOURCE_INPUT_CC69_20261009.json notes/data/RPB108_NF27_SOURCE_INPUT_CC70_20261009.json INPUT_DIR/native112_N720_K620.json.gz --output /tmp/nf28_replay.json
python3 scripts/certify_signed_mixture_cc72.py /tmp/nf28_replay.json notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF27_SOURCE_INPUT_CC70_20261009.json --output /tmp/cc72_mixture.json
python3 scripts/check_native_mixed_projection_nf28_106.py notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF27_SOURCE_INPUT_CC70_20261009.json INPUT_DIR/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64 --output /tmp/nf28_native_checks.json
```

The independent checker uses the unchanged NF24 native residual projection archive (SHA-256 after decompression4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346). Its original unsquared source intervals and fresh replay are retained in custody.

Highest whole-domain anchor remains21/20 with margin1/(3*10^63). CC71 finite116 positivity and prior infinite-high restricted null exclusions remain. Whole53/50, collective infinite-high Schur positivity, all-cap old-gap-independent leakage, uniform defect-relative frame for actual critical eigenvectors, global actual null exclusion, RH/F4, transport and Lean remain open. No full-Weil nonimplication or actual negative vector is claimed. Historical wording and paused fronts are unchanged.
