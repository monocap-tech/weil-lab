# RC295 — finite-output dual obstruction test for all three-column inverse seeds

Parent RC294 at `85e01a8cdd663fdb817ca0dcc47bca0c0c3cff6b`.
**Reference:** reduced rank-317 actual positive reference.
**Allowed trial input span:** `V=span{P0,P2,P4}`.
**Goal:** determine whether any real/rational seed in this *entire*
three-dimensional space can satisfy RC292's strict residual tolerance.
This is stronger than checking RC294's two explicit rational seeds.

## Exact dual-method construction

RC279 certifies the original D-normalized Weil action on P0, P2, P4,
including its finite original action coefficients (0–2048), complete
global D faults and infinite output tails. On these three inputs the
new reference adds the exactly known physical projection augmentation

    N_new Pj = N_original Pj + lambda/(H_j+s) Pj.

Fix midpoint `s_mid` of the RC129 exact `s` interval and a set of
four even output degrees `J={0,2,4,n}` with n≥6. Let `A_J` be the
four-by-three matrix of *nominal* original Weil actions, including the
new reference's source-mode augmentation. Define a nonzero rational
left annihilator `q` by its signed 3×3 minors:

    q^T A_J = 0.

The checker computes this identity **exactly**, not by a floating
nullspace. The vector `q` is a finite-output dual witness, not an
inverse operator, not a source eigenvector and not a new original
arithmetic action.

For any response seed `y` in V and either unchanged original input
source `b=D^{-1}P0` or `b=D^{-1}(P4-tP0)`, write

    r = b - N_new y,
    Q^2 = sum_(n in J) q_n^2/[m_n (H_n+s_lower)].

Then physical Cauchy gives

    |q^T r| ≤ Q ||r||_D.

Because `q^T A_J=0`, its nominal source signal `q^T b_mid`
cannot be eliminated by *any* seed coefficient. All differences
between actual and nominal actions are rigorously paid using:
the complete RC279 global original-action D-error norms; the
RC129 source and augmented-projector rational `s` interval;
and a norm bound on any seed that *hypothetically* meets RC292's
strict residual tolerance.

Specifically, if `||r||_D²<T` then `N_new≥mu I` implies

    ||y||_D ≤ (||b||_D+sqrt(T))/mu.

This bounds each candidate coefficient using its exact physical
Legendre D mass. As a result, the dual test yields a
**seed-independent conditional lower**:

    |q^T r|
        ≥ |q^T b_mid| - E_source - E_all_three_columns.

If this last lower strictly exceeds `Q sqrt(T)`, there cannot be
*any* three-column seed with residual square below `T`. That is
a sound no-go statement about this **input action subspace**; it
does not prove the full infinite-dimensional inverse cannot attain
RC292's test.

The search considers 14 explicit choices of the fourth even output
degree and keeps the exact-rational strongest normalized ratio. The
result will be materialized from GitHub Actions generation; the
provisional certificate does not authorize claims of exclusion.

## Important limitations

- The projected original-output infinite tail is outside the finite
  support of `q`, hence contributes **exactly zero** to the dual
  functional. That is an orthogonality statement, not a decision to
  delete an uncertainty from a global norm test.
- The full original-action D faults are still paid by Cauchy. If the
  inherited fault definition does not cover the finite output
  coefficient discrepancy in the exact RC279 normalization, this
  contract must be revisited rather than accepted by replay alone.
- Failure of the dual sufficient test is inconclusive. A positive
  result rules out just the stated RC292 tolerance among the
  three available input columns, not positivity of the original
  Weil form or the possibility of successful higher-dimensional trials.
- No new prime action, arbitrary-input operator, Chebyshev recurrence,
  six-mode positivity, 314-dimensional Schur positivity, Stage I,
  global F4, RH, or Lean result is asserted.

## Next frontier

If the universal three-column residual obstruction passes, RC296
must enlarge the actual original-action oracle beyond P0/P2/P4,
or certify a reusable operator kernel for arbitrary recurrence
vectors. Existing RC279 action columns are insufficient for the
full RC292 Chebyshev inverse program.

## Exact replay

```bash
python scripts/validate_rpb108_rc295_three_column_dual_obstruction.py --output certificates/rpb108_rc295_three_column_dual_obstruction.json
python scripts/validate_rpb108_rc295_three_column_dual_obstruction.py --output certificates/rpb108_rc295_three_column_dual_obstruction.json --replay
```

The validator imports pinned prior certificates. Actions generation
and replay establish exact arithmetic custody, not independent
confirmation of the imported original Weil source theorems.
