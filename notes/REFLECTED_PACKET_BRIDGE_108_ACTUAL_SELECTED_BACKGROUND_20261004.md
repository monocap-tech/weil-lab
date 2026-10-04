# RPB108 normalized actual selected/background split — 2026-10-04

## Definitions and exact construction

The finite selection is a set of actual divisor multiplicity coordinates, not an unspecified zero packet or an orbit quotient. The selected continuous ℓ² projection retains exactly those coordinates. The background projection is its complement. Their squared norms add to the original squared norm, and both projection norms are bounded by the input norm.

The positive and negative full-divisor analyses from the certified complete source graph are multiplied by 1/sqrt(2). This second factor is separate from the pair-source diagonalization factor already present in the sources. It removes the factor two certified in full-divisor source attachment. The normalized negative analysis splits into selected and background continuous maps, with exact additive vector and squared-energy identities.

The finite selected normalized energy equals one half the sum of raw selected negative-source sample squares on the same graph vector.

The signed source quadratic is normalized positive energy minus normalized full negative energy. The effective-background quadratic is normalized positive energy minus unselected normalized negative energy. On every graph vector, the latter equals the former plus selected normalized negative energy.

On every unchanged constructed Green lift, the signed source quadratic equals the zero-form real part. The effective-background quadratic therefore equals the native signed Weil multiplier/cross-pole quadratic plus half the raw finite selected negative-source energy.

## Certification

- Module: `WeilDefect/Arithmetic/ActualZetaSelectedBackground.lean`.
- Root imports the new module.
- Candidate: 4e5a43c0598221663e1b6b85e428c75f35f1ccdb.
- Passed [run 37183383661](https://github.com/monocap-tech/weil-lab/actions/runs/37183383661), job 111380272097.
- Lean 4.34.0; isolated 9154/full 9187 build jobs.
- All 12 public theorems audited: each depends exactly on [propext, Classical.choice, Quot.sound].
- The unfinished trusted-declaration gate passed.

## Residue and boundaries

This is a concrete normalized coefficient construction on the certified source graph. No abstract source-representation premise or retained operator-domain premise was added. Selection is arbitrary finite actual coordinates; any fixed-packet orbit/multiplicity matching must still be proved.

The effective-background expression is signed. Positivity and a WD-T10-compatible square-root factorization are not consequences of the split. The graph uses its complete product graph norm; any Hilbert realization or native-form extension beyond Green lifts remains to be proved before adjoint-based constructions. Retained P/C/k source/null identification and k membership are not supplied.

Next cursor: prove the actual effective-background positivity/factorization needed for WD-T10/WD-T38 on a lawful complete source/form domain, preserving the now-certified full-divisor normalization and selected/complement coefficient split. Align finite actual-coordinate selection with the retained fixed packet's orbit/multiplicity convention; no pair-closed or one-per-orbit selection is silently assumed. If a Hilbert graph realization, density or extension of the native Weil form is needed, prove it before using adjoints or transferring the Green-lift identities. Retained k membership and same-vector P/C/k source/null identification remain open. No concrete WD-T38 application was recovered in the pinned 152-file scan. Central cancellation, background completion, boundary removal and F-4 remain open; SOURCE is off the critical path.
