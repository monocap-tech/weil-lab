# Original signed 2D interval-rounding repair

The accepted source at 6aecb3c rounds each cell baseline downward to
denominator 10^9, then constructs a symmetric interval using an independently
upward-rounded analytic error. The lower endpoint is safe. The upper endpoint
needs an additional rounding payment: upward-rounding the error does not
necessarily absorb the baseline's downward rounding loss.

For N=7168 cells, the total baseline loss is strictly less than N/10^9.
Keep the original lower endpoints and add N/10^9 to each upper endpoint
before physical-pole and high-negative accounting. This does not change the
source family, quadrature mesh, analytic error estimates, or operator.

The dedicated workflow checks this payment and includes a concrete exact
rational regression where the old interval upper misses the true value.

## Scope of the cross bound

The matrix used to prove positivity retains the signed [0,12] form and
physical pole, and subtracts the potentially negative high-frequency form.
The positive high-frequency form is discarded as a whole PSD quadratic form.
Thus the offdiagonal absolute bound concerns this retained form, not the
complete original form's offdiagonal: positive high-frequency mixed entries
have not been bounded in absolute value.

The old JSON key full_signed_cross_abs_upper is retained as a compatibility
alias, with explicit cross_bound_scope and retained_signed_cross_abs_upper.
The positivity conclusion still concerns the complete original signed form,
since adding the discarded PSD form preserves positivity.

## Exact preflight from GitHub evidence

Source artifact: 12622301137, accepted run 40254734157, source 6aecb3c.
Archive SHA-256:
17524731b1d231eeb4567b3a5ecb6b7167832aef2ec473345044dcf6d9f559cc
JSON SHA-256:
72f17f3b2614e399c5387061514aac0def3912e1ebe5e921844d33cc045beb0e

Exact local recomposition from those bytes gives decimal displays:
- Rounding upper payment: 0.000007168.
- Retained cross absolute upper: 0.002148137538520956.
- Determinant lower: 0.000018254646391302014.
- Coordinate minimum-eigenvalue lower: 0.00014269702991883318 > 1/7100.

The previous 1/7000 coordinate bound must not be carried forward.
The two original diagonal lowers remain unchanged, so the strict signed 2D
positivity survives this repair. Under the separate inherited physical Gram
bounds and change-of-basis estimates, the weaker 1/7100 coordinate bound
still gives physical L2 coercivity >1/45000: 7100*5*(121/100)=42955<45000.
The earlier intermediate coefficient bound 1/35000 is not established by
this repaired comparison; use 1/35500 instead.

A dedicated full GitHub replay must accept the modified source before the
repair is called CI-accepted. Neither this repair nor the 2D result controls
the other original J470 directions or their coupling/infinite complement.
All inherited analytic/domain assumptions remain. W-ODD-NEG, even/CC27,
Weil and RH remain OPEN.
