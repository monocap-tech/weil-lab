# RPB-108 — compact exterior source realization

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `b5e35610cc3c790d4deb7e03e022f97196ad0750`.

## Actual pole addition

The corrected frozen source action is the right-limit fixed-cutoff multiplier
core plus the actual physical pole pairing. The preceding exterior core
attachment and compact-test pole integrability justify adding these two
genuine integrals. The result is the pairing with the existing full exterior
ingredients: gap function minus finite prime part plus physical pole.
These ingredients are locally integrable, so their pairing with every
compact Schwartz test genuinely converges.

## Existing candidate attachment

For a test vanishing on (-a,a), zero continuation changes none of its
pairings. Pointwise, the test is zero centrally and the candidate equals
the exterior ingredients elsewhere. Consequently, for 0≤c<a,

    ∫ u(x) neutralExteriorResidualCandidate(h,a,x) dx
      = frozenWeilCompactAction(h,a,u)

on every compact exterior Schwartz test. This is actual realization by
the previously constructed candidate, retaining full-symbol growth.
No whole source representation premise is introduced.

## Remaining central and boundary obligations

The candidate vanishes centrally by definition, but that does not imply
the actual corrected source action vanishes on central tests. Equality
on exterior tests also does not exclude a boundary-supported distribution
defect. Central cancellation and boundary reconstruction are therefore
needed before extending the identity to arbitrary compact tests.

Whole compact weak source realization and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open. Canonical Weil,
main and WD-T40 mathematical standing are unchanged. Threshold bookkeeping
is closed; logarithmic coercivity has not started.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,981 build jobs passed. All four endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `cbbee3e50dd3e4d68451b12ad874fe31887cee47`, run `37069776850`, job `111046209012`, source blob `49daf738913f8f6e4587adfe8a509dcfb90895b3`.

Validation-only workflow/cache changes are excluded from research promotion;
historical notes are immutable.
