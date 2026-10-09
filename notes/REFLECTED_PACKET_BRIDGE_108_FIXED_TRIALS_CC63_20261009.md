# CC63: exact rational compensated trial inputs for the native near-critical source test

Read [definitions](../docs/TERMINOLOGY_RPB108_FIXED_TRIALS_CC63.md) first. This constructs and certifies the original finite trial inputs for the next source computation; it does not duplicate the independent native source producer or claim that the full residual source has been evaluated.

## Original arithmetic result

The authenticated NF18 retained seeds are extended by rational coefficients on e112/e114 even and e113/e115 odd. Every resulting vector is EXACTLY fixed in the original physical normalized Legendre basis, with common coefficient denominator10^75. Its58 coefficients and all56 retained source projection intervals are published in the [certificate](data/RPB108_FIXED_TRIALS_CC63_CERTIFICATE_20261009.json).

| Quantity | Even | Odd |
|---|---:|---:|
| Original NF18 seed energy, approximate | 9.306557318e-35 | 3.391977951e-31 |
| Fixed trial energy, approximate | 9.255635704e-35 | 3.307019995e-31 |
| Certified trial energy bounds | 8e-35 < Q(p) < 1e-34 | 3e-31 < Q(p) < 4e-31 |
| Physical squared mass | >4/5 | >4/5 |
| Each measured high-source coefficient | absolute value <1e-60 | absolute value <1e-60 |
| Sum of two measured residual squares | <2e-120 | <2e-120 |

These are actual original signed energies and source pairings, not approximate eigenvalues or shifted quadratic forms. The original full energy strictly decreases from each seed to its fixed trial, with every native interval error paid. The fixed-trial Rayleigh quotients are below1.25e-34 even and5e-31 odd. They remain positive near-critical finite vectors, not actual full-operator critical eigenvectors.

The two additional high coefficients are approximately(3.62106e-19,-2.07233e-19) even and(-4.43660e-17,2.98030e-17) odd; these displays are not proof values. The exact integers in the certificate define the vectors.

## Authenticated source use and error payments

The original E112, first-high and second-high archives are checked against their immutable raw SHA256 identities. Their union contains3422 complete signed source records. All13688 arch/prime/pole/full component interval checks and the full interval compatibility checks pass. The NF18 seed file identifies the same original source and its own SHA256 is recorded.

For each parity, compute the native midpoint high matrix and mixed seed pairings, solve its exact rational two-by-two midpoint system, then round each correction downward onto denominator10^75. The rounded correction is the DEFINITION of the trial, not an enclosure of a silently exact compensation. Subsequent energy, measured residual and retained projection calculations use the complete original SOURCE INTERVALS rather than the midpoint matrix.

The retained coefficients Q(e_i,p) are all enclosed outward on the10^-60 grid. Their widths are at most2e-60. Choosing the56 interval midpoints therefore gives physical projection error at most sqrt(56)*1e-60<8e-60. This error is negligible relative to the required native source scale, but pays only the retained projection. Every archimedean, prime, pole and source-construction error remains a separate obligation.

Measured source coordinates are smaller than1e-60 but are NOT assumed zero. One can keep them in the full residual or explicitly pay their norm, which is below sqrt(2)*1e-60. Dropping them without payment would incorrectly identify this rational trial with the exact Galerkin lift. The full source remains the genuine action of the supported polynomial.

## The measured columns do not settle the source gate

Before compensation the original NF18 seeds have measured two-coordinate source-square LOWER estimates of approximately .0780449*kappa Q(x) even and .3605474*kappa Q(x) odd. These lower bounds do not refute a coarse upper source gate, but they also cannot certify one. They account for only two of infinitely many high coordinates. After the rational correction those two measured coordinates are tiny; the unseen source may still determine the whole response.

This is why a tiny measured residual, a positive finite trial energy or the existing finite collective response bounds cannot replace the complete arch-prime-pole source norm. CC61's same-source controls delimit what the finite data alone can conclude. No uniform defect-relative lower frame is inferred from the new trials.

## Exact next directional gate

For either published trial p, define the physical high residual

    r=Lp-sum_(i in E112, same parity) Q(e_i,p)e_i.

Keep all original source sectors and correlations BEFORE squaring. This removes the entire retained source projection and keeps every high coordinate, including the two small measured residuals. The finite polynomial source representation makes r physical L2.

Let x be the retained NF18 seed and z0=-H2 y its trial high component. Minimizing Q(x+z) over the entire canonical F112 is equivalent to minimizing Q(p+w) over w in F112. With C_full>=kappa I, this gives the exact identity and upper bound

    complete corrected seed energy = Q(p)-<r,C_full^{-1}r>,
    <r,C_full^{-1}r> <= ||r||²/kappa.

Consequently ||r||²<kappa Q(p) suffices for positivity on span{x}+F112. Exact measured annihilation is not required. Comparing a paid source-norm upper bound to a certified LOWER energy enclosure gives a valid directional sign certificate.

For example, the published coarse lower energy thresholds make the source-square targets κ*8e-35 even and κ*3e-31 odd sufficient. These are targets, not achieved source bounds. Failure of this sufficient physical gate remains inconclusive about actual negativity; a true C-form-dual estimate and CC59/CC60 correlated estimates remain alternatives. Passing separately in both parities would establish two directional infinite restrictions, not a full56-dimensional collective gate.

## Validation and current standing

[Exact producer/consumer](../scripts/certify_native_fixed_trials_cc63.py), [certificate](data/RPB108_FIXED_TRIALS_CC63_CERTIFICATE_20261009.json), [custody](data/RPB108_FIXED_TRIALS_CC63_CUSTODY_20261009.json). Both rational vectors, their masses, positive signed energy ranges, strict energy reductions, measured residual bounds and all112 retained source projection intervals pass. Source hashes and all13688 signed component checks are explicit. No actual null or native crossing is claimed, and no positive eigenlevel is relabeled as a null; the published seeds are finite retained witnesses only.

CC62's original E2+F112 gap1/100 at53/50 remains. The new trials address the actual much smaller retained energies beyond that restriction. The whole-domain anchor remains21/20. Complete target53/50 positivity, near-critical collective source norm and inverse response, cap-uniform old-gap-independent leakage, defect-relative critical frame, actual contact exclusion, RH/F4, full transport and Lean remain open. Historical wording, paused fronts and the independent source producer are preserved.
