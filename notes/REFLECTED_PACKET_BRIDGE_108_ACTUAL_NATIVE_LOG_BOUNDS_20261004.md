# RPB108 actual native logarithmic envelope — 2026-10-04

## Definition and proof

The symbol is the unchanged right-limit compact Weil symbol in mathlib Fourier coordinates: the actual quarter-line digamma bracket at 2πξ minus the actual finite prime trigonometric sum. The weight is the existing canonical logarithmic Fourier weight log(exp(1) + |ξ|).

The certified vertical Stirling theorem gives |Re ψ(z) − log ‖z‖| ≤ 4 for positive real part and |Im z| ≥ 1. On the actual quarter-line z = 1/4 + iπξ and |ξ| ≥ 1, elementary norm comparisons bound the difference between log ‖z‖ and the canonical logarithmic weight. The established continuity of the gamma bracket supplies a bound on the remaining compact frequency interval.

Thus the actual archimedean symbol differs from the canonical weight by a uniformly bounded real function. The finite prime symbol is bounded by the sum of absolute actual prime coefficients over the unchanged right-limit prime-power set; equality-threshold primes remain included.

Combining these proves, for every window a, the existence of C ≥ 0 such that |m_a(ξ) − weight(ξ)| ≤ C for every real ξ. In particular:

- weight(ξ) ≤ m_a(ξ) + C;
- m_a(ξ) + C ≤ (1 + 2C) weight(ξ).

The lower logarithmic coefficient is exactly 1. These statements contain no symbol-envelope hypothesis, source representation premise, background domination assumption, or all-derivative temperate-growth premise.

## Certification

- Module: `WeilDefect/Arithmetic/ActualZetaNativeLogBounds.lean`.
- Candidate: f3014cb90a6b79a87db66ef7f766f186a1c328ef.
- Passed [run 37203034063](https://github.com/monocap-tech/weil-lab/actions/runs/37203034063), job 111438434921.
- Lean 4.34.0; isolated 9151/full 9189 build jobs.
- Six theorem axiom audits, each exactly [propext, Classical.choice, Quot.sound].
- Unfinished trusted-declaration gate passed.
- Saved validation cache: rpb108-actual-native-log-bounds-verified-v1.

## Scope and independent obstruction

WD-T10 requires a contractive background factorization S_B = −S_+ X_B. The complete Hilbert source graph supplies lawful adjoints and bounded signed covariance operators, but those constructions do not produce that factorization. The newly proved shifted symbol inequality is not unshifted effective-background positivity.

This chunk establishes actual zeroth-order logarithmic control. It does not prove smoothness and polynomial control of all symbol derivatives, identify source forms on the entire logarithmic carrier, establish Green/source density, or attach retained k to the graph. The same-vector P/C/k source/null obligation remains unchanged. No actual WD-T38 constructor application was recovered in the prior pinned 152-file scan; this chunk does not extend that scan.

Next cursor: Integrate the certified actual native logarithmic envelope on the canonical logarithmic form domain and combine it with the actual pole bound to obtain unconditional native Gårding/form continuity, without assuming the all-derivative temperate-growth premise or retained spectral operator-domain membership. Then address actual source-form extension/density and the independent unshifted effective-background positivity/factorization obligation. The now-complete Hilbert source graph has lawful adjoints, but signed covariance and shifted coercivity do not establish WD-T10's contractive background factorization. Align fixed-packet orbit/multiplicity custody and retain the same P/C/k vector for source/null attachment. No concrete WD-T38 constructor application was recovered in the prior pinned 152-file scan. Central cancellation, background completion, boundary removal and F-4 remain open; SOURCE is off the critical path.
