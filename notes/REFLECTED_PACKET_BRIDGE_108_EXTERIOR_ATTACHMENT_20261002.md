# RPB-108 — actual exterior multiplier attachment

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `fe9566792500d73678639ff1afbf82ac0b01cdee`.

## Actual exterior pairing identities

For 0≤c<a and a Schwartz test u vanishing on (-a,a), the actual carrier
pairing is zero. The certified scalar-centering action law therefore
identifies centered and uncentered shifted digamma actions on u.
Actual centered action zero convergence now proves the shifted tail
converges to zero on these separated tests.

The existing certified defect identity then gives

    archimedeanMultiplierCore(h)(u) = ∫ u(x) gap(h,a-c,x) dx.

The already-certified exact finite prime split supplies

    rightLimitWeilMultiplierCore(a,h)(u)
      = ∫ u(x) [gap(h,a-c,x)-finitePrimePhysical(h,a,x)] dx.

Both component pairings are genuinely integrable, so subtraction inside
the integral is justified. These are actual exterior representations of
the existing multiplier action. They retain its full-symbol temperate-
growth premise; no physical archimedean representation premise is added.

## Remaining whole-source obligations

Add the named physical pole on compact tests, then identify the central
region and reconstruct across the boundaries. The exterior identity
does not supply central cancellation or whole compact weak realization.
The multiplier core itself excludes the pole.

Whole source attachment, central/boundary reconstruction and actual source-
domain/quadratic/polarization/normalized estimate witnesses remain open.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.
Threshold bookkeeping is closed; logarithmic coercivity has not started.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,980 build jobs passed. All four endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `850bfece8cc0dbc7667a39450e9c0607122b8fbb`, run `37069105759`, job `111044051054`, source blob `10b8eee12415382b27e69bd25e210973e20f8120`.

Validation-only workflow/cache changes are excluded from research promotion;
historical notes are immutable.
