# RC300 — complete native P8 high-output action and rank-317 physical augmentation

**Parent:** merged RC299 (`83b6bab10b6a342102c33b461cabda3c10288c9c`).  
**Carrier:** original Weil physical aperture `B=11/10`.  
**Reference:** rank 317 (122 even, 195 odd; first omitted even degree 244).  
**Standing:** Stage I, F4, RH, and Lean remain **OPEN**.

## Result

RC299 constructed a genuinely new original even-input action for `P8`,
through output degree 64, including all original regular, pole, prime,
endpoint and omitted-output allowances. RC300 uses the pinned RC279
prime/endpoint projection engine to **materialize the same original P8
input's 2049 coefficients through degree 2048**, retaining RC299's first
65 coefficients *exactly*. No omitted high mode is assigned zero:
the remaining infinite original output is controlled by the analytic
prime and endpoint tail certificate.

The new materialized certificate is
`certificates/rpb108_rc300_native_p8_high_projection.json`.

The original even native input-action interface now covers exactly
`span{P0,P2,P4,P6,P8}` as a linear input family. These are **five
source/input columns**, not five output modes, not a uniform operator
kernel, and not permission to evaluate arbitrary Chebyshev recurrence
vectors outside this span.

## The physical rank-317 patch

The retained even projection contains `P8`, so the augmentation of
the original action is concentrated in a single physical coordinate:

`N_new P8 = N_original P8 + [lambda/(H8+s)] P8`.

The source moment `s` is the pinned RC129 interval. RC300 attaches
an exact outward rational center/radius enclosing the added coefficient,
and pays its error in the physical `D` norm using

`sqrt(m8*(H8+s_upper)) * radius`.

This term increases the total **global** original-action D-fault bound.
Since the augmentation has finite support at output degree 8, it does
**not** alter the original infinite-output tail. The same reference
parameter `lambda` and reduced rank-317 parity selection as RC297
are preserved.

## Verification

The validator requires:
- Immutable hash pins for RC129, RC283, RC296, RC297, RC299 and the
  inherited original prime data and projector implementation.
- Equality of all 65 low original P8 output centers with RC299.
- 2049 ordered output-degree entries and exact zero odd-parity centers.
- Actual nonzero new even source output above degree 64.
- Complete preserved original high-output tail and positive paid global fault.
- Correct even reference rank and augmentation at *only* n=8.
- An exact rational full-certificate regeneration and replay.

All checks in the certificate generator and reverse-order exact replay
passed on GitHub Actions. The one-time generator workflow was removed
from the feature branch after producing the committed artifact; the
ordinary RPB108 certificate custody/replay workflow remains in place
for PR validation.

## Precise limitations

**This does not establish a five-column inverse approximation.**
No five-column signed Galerkin residual, dual obstruction, Schur gate,
global F4, RH or Stage I closure has been certified here.

The high-degree prime/endpoint projection and global tail formulas
are reused from prior validated *computational certificates*.
Their applicability to degree-eight inputs remains contingent on the
imported analytic formulas and cannot be elevated to an independent
proof of the entire original Weil operator merely by replaying the
arithmetic.

## RC301

Compute actual signed inverse seeds in the five-column span and/or use
an exact six-output dual functional to test *all* five-column seeds
against RC292's unchanged strict residual tolerance. Charge all five
original global D-faults, `s`-interval source/augmentation variations,
and every rational dual nonannihilation defect. If the restricted space
is excluded, the next mathematical priority is a reusable native
arbitrary-input action interface, not another optimizer over the same
five inputs.

## Reproduction

```bash
python scripts/validate_rpb108_rc300_native_p8_high_projection.py --output certificates/rpb108_rc300_native_p8_high_projection.json
python scripts/validate_rpb108_rc300_native_p8_high_projection.py --output certificates/rpb108_rc300_native_p8_high_projection.json --replay
```

As always, a successful exact replay checks the pinned calculation and
its internal arithmetic custody; it is not independent peer review of
the imported analytic bounds.
