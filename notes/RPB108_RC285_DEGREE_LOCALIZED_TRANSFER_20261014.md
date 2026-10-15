# RC285 — degree-localized source inverse response in reduced references

Parent: RC284 `17c5900dec38469eb18d4a54e564c7668ab371a2`. Aperture `B=11/10`.
The original Weil form remains unchanged. Candidate reference ranks: 301,
**317**, 334 (see RC283). Stage I and RH remain OPEN.

## Method

RC284 reused the old P0 and P1 rational trial polynomials (degree at most
64). Their original Weil action, new augmented action, source residual, and
variational center are identical under each reduced reference because the
new projection still contains the trial's support. Their *inverse response*
is not identical.

RC274 provides degree-by-degree rational bounds on the actual original
output residual numerator for modes 65 through 2048, including the two
parities' full infinite tails and global model faults. RC278 transfers
these outputs to its refined trial by a *known exact scale factor* t.
For each reduced reference the lower comparison form is exactly

    G_new >= W_new = D_(retained low projection)
                     + (D-lambda)_(orthogonal complement),

with the same original physical D=diag(H_n+s), and
lambda equal to RC278's certified negative allowance. The resulting
D-normalized weight is

    w_n = 1                  for n < first omitted degree,
    w_n = 1-lambda/(H_n+s)   for n >= first omitted degree.

The rational validator uses the lower endpoint of the certified s interval,
then rounds every denominator weight downward. It computes complete
nonnegative inverse-energy payments in three regions:

1. Modes 0--64, using RC278's retained residual-center coefficients.
2. Modes 65--(first omitted minus 1), from RC274's actual original-output
   intervals, with weight one.
3. Modes first-omitted--2048 from the *same* RC274 intervals, with
   positive lower weights; plus the separately certified infinite tail
   from RC274, with its own first-tail weight.

All RC274 original residuals are rescaled by RC278's exact trial factor.
RC278's complete source/center-rounding energy is preserved. Its global
D-fault norm is charged by delta^2/mu_new. The RC284 Young payment
(eta=1/100) is retained to make the comparison exact and monotone.

This avoids RC284's coarse assignment of the whole degree >64 residual
to the smallest reference weight. Every numerical gate estimate is an
**upper response / lower gate enclosure**. A negative lower gate remains
inconclusive and is never an original negative witness.

## Certified source-gate results

Degree localization is strong enough to certify **strictly positive
actual native P0 and P1 gate directions** in *each* reduced reference.
The following values are decimal views of exact rational **lower**
bounds stored in the certificate:

| New total reference rank | Even P0 lower | Odd P1 lower |
| --- | ---: | ---: |
| 301 | +0.0038741283 | +0.0058178857 |
| **317** | **+0.0064476498** | **+0.0067537262** |
| 334 | +0.0065401945 | +0.0068879479 |

Compared with RC284's inconclusive negative lower enclosures, the
localized actual-source payments now cross zero rigorously. The
relative ease of the 317 reference makes it a practical next choice.
Because opposite reflection parity pairs to zero, the two tested
P0/P1 directions form a strictly positive two-direction restriction
within each *single* reduced reference.

**This is not full positivity.** The other 315 coordinates for rank
317, including same-parity cross terms, are not resolved. Do not
transfer RC280's additional old-reference pivots to these new
references.

## Exact custody and validity checks

- Pin the RC129 D moment, RC274 65--2048 interval/tail certificate,
  RC278 rescaled source trials, RC283 reduced references, and RC284
  conservative response bounds.
- Verify the complete set of parity degrees 65--2048 with no omitted
  residual interval, no repeated term, and both infinite tails.
- Reconstruct RC278's *unrounded* source model energy as a subbound of
  its previously certified old model upper bound.
- Verify each localized model bound and native gate lower is at least as
  strong as RC284's corresponding conservative bound.
- Do not transfer old five-pivot certificates or assert full rank-317
  positivity. Conditional inverse polynomial actions remain unexecuted.

## Next gate

The new-source test has passed. The coupled same-parity P0/P2/P4
and P1/P3/P5 families must now be rebuilt against the new 317-reference operator
and their complete covariance treated together. Positivity of two
separate source directions cannot replace the coupled gate.

## Reproduction

```bash
python scripts/validate_rpb108_rc285_degree_localized_transfer.py --output certificates/rpb108_rc285_degree_localized_transfer.json
python scripts/validate_rpb108_rc285_degree_localized_transfer.py --output certificates/rpb108_rc285_degree_localized_transfer.json --replay
```

GitHub Actions performs the committed exact-rational replay. This
validates the arithmetic custody and implications of pinned historical
certificates, not an independent proof of every imported analytic fact.
