# RC294 — three-column native original-action oracle and paid inverse seed search

Parent: RC293 `b0857a567f8ef9c6e0a39b867b3feea5fd90c589`.
Aperture B=11/10, new reference rank 317 (even 122; first omitted
even degree 244). Original Weil form unchanged.

## Strict scope

RC293 had certified full-domain native residuals only for two rational
inverse-response seeds supported on P0 and P4. Its D-residual upper
bounds were much larger than the RC292 conditional acceptance budgets.
RC294 extends the **source input subspace** to the entire even
`span{P0,P2,P4}` by reusing RC279's three existing original-source
action columns. This is a genuine certified finite-*input*-dimensional
action interface, **not** a projected finite-domain inverse.

For every rational input `Yhat=y0 P0+y2 P2+y4 P4`, the complete
D-normalized reduced-reference action is

    N_new Yhat = sum(yj N_original Pj) +
                 sum(yj lambda/(H_j+s) Pj).

RC279's stored exact-rational original action centers cover modes
0--2048 and certify full infinite output tails and global arithmetic
D-faults for all three columns. RC129 pays the s interval at the source
and augmentation modes. Minkowski sums of the *signed* rational
finite output centers and the absolute tail/global uncertainty
amplitudes yield a rigorous full-domain D-residual upper bound.

The candidate seed-selection step solves the 3x3 least-squares
normal equations of the **finite, nominal** action profiles using
ordinary floating-point arithmetic. Its result is rounded to
ten decimal places and used **only as a rational proposal**.
No floating-point least-squares value is used as a rigorous
operator bound. The proof is the separate exact Fraction audit of
that proposed seed against complete original arithmetic errors
and omitted infinite modes.

## Audit gates

- Immutable RC129, RC279, RC283, RC290, RC292, RC293 blobs are pinned.
- For P0 and v_soft=P4-tP0, replay the RC293 two-column seeds with
  y2=0 and verify their rational residual enclosures agree.
- For each source, certify a three-column least-squares proposal
  using the same true original-source right-hand-side, new augmented
  reference, and full source tail/error charges.
- Select the smaller of the strictly paid 2- and 3-column estimates.
- Compare the selected **upper** D-residual squared to RC292's strict
  signed-inverse acceptance threshold. A failed bound does not prove
  every 3-column approximation fails, nor prove an actual negative
  source direction. If the new y2 coordinate is nonzero, its
  approximate retained-rest signed projection is also paid rather
  than asserted zero.

The new interface only supports the existing three action columns.
It cannot apply the original Weil operator to an **arbitrary**
Legendre vector produced in a 177-/215-step Chebyshev recurrence.
Claiming full native inverse execution would therefore be invalid.

## Next requirement

Recover the next batch of actual original-action columns with
complete prime, archimedean, endpoint and infinite-tail bounds; or
derive a rigorously reusable operator-kernel/tail rule that certifies
all recurrence vectors. The present conditional signed acceptance
and the 314-dimensional principal Schur gate remain open.

Reproduce:

```bash
python scripts/validate_rpb108_rc294_three_column_seed_action.py --output certificates/rpb108_rc294_three_column_seed_action.json
python scripts/validate_rpb108_rc294_three_column_seed_action.py --output certificates/rpb108_rc294_three_column_seed_action.json --replay
```

This certificate tests arithmetic consistency against inherited
analytic inputs; it does not independently establish their truth.
Stage I, RH, F4, Lean: **OPEN**.
