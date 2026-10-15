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
degree, selects the exact-rational largest normalized ratio, and
stores both annihilator vectors and every paid error contribution.
The final checked certificate requires strict ratios >100 for both
original sources; these are sufficient obstructions on the stated
three-column trial-input span.

## Certified universal obstruction — both original sources

RC295's rational candidate search has found explicit annihilators that
**exclude the RC292 residual acceptance threshold for all seeds** in
the existing three-column input span, not merely RC293/294's selected
least-squares seeds. This is a *mathematical obstruction to a restricted
inverse-approximation family*, not a zero or negative mode of the
original Weil operator.

| Original source | Four finite output rows | Exact lower for dual ratio versus accepted maximum | Universal three-column acceptance |
| --- | --- | ---: | --- |
| Hard `P0` | **0, 2, 4, 6** | **>199.63×** | **Impossible** under pinned estimates |
| Soft `P4-tP0` | **0, 2, 4, 14** | **>1899.85×** | **Impossible** under pinned estimates |

The ratio is the strict lower for
`(|q·b_mid|-E_source-E_all_columns)/(Q sqrt(T))`.
When it exceeds one, an assumed seed with actual D-residual norm
squared smaller than RC292's T contradicts the exact dual inequality.
The arbitrary signed `P2` seed coefficient is fully allowed;
indeed the proof covers **all real** coefficients on P0/P2/P4,
without needing RC292's additional projection restriction.

The certificate is particularly strong for the soft source:
the finite-output original action cannot meet RC292's residual
tolerance in this restricted three-column input space, even when
the old tested trial coefficients are replaced by the optimal
unknown real coefficients.

The dual support ends at degree 14, so the original model's
infinite output tail has exactly zero pairing with the witness.
All finite original-action uncertainty is nevertheless paid via
the RC279 global D-fault norms, and the accepted-seed coefficient
bound accounts for every possible signed combination. This
obstruction does not depend on an assumed diagonalization of
the full original Weil operator.

**Operational consequence:** Running a more sophisticated optimizer
on exactly the same three source-action columns cannot satisfy
the specific RC292 residual acceptance criterion. The next viable
route is a genuinely larger source-action span, with paid new
original operator columns, or an operator-wide response evaluator.
It does not follow that a three-column seed is useless for every
weaker method or that the *true* inverse cannot satisfy the signed
cross-payment objective.

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
