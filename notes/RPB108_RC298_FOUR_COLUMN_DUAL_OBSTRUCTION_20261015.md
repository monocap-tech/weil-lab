# RC298 — four-column native inverse: finite-output dual obstruction

**Parent:** RC297, `57c81e17b994c5f349c64836d862fe79f1a96013`.
**Original action input span:** `V_4=span{P0,P2,P4,P6}`.
**Positive reference:** reduced rank 317 (122 even, 195 odd), aperture `B=11/10`.
**Status:** Stage I, original Weil positivity, global F4, RH and Lean remain **OPEN**.

## Purpose

RC297 supplied the fourth genuinely evaluated original Weil action column,
`P6`, through output degree 2048, with separately paid global arithmetic
error and remaining high-output D energy. RC295 had already excluded all
three-column seeds. RC298 tests whether the additional native P6 input can
make either RC292's **strict sufficient residual tolerance** attainable.

Instead of merely fitting two further four-column least-squares seeds,
RC298 takes the stronger route: a **seed-independent dual exclusion** for
the entire four-dimensional input span, including *all real* coefficients,
with no signed-projection restriction. If the stronger test succeeds, no
optimizer restricted to these four columns can pass the RC292 residual gate.

## Rigorous paid five-output test

For an original source `v`, let `b=D^{-1}v` and
`r=b-N_new y`, with `y in V_4`. For each source a rational
five-output functional `q` is supported on either

- hard `P0`: output degrees **0, 2, 4, 6, 8**;
- soft `P4-tP0`: output degrees **0, 2, 4, 6, 14**.

Its five coefficients are stored as exact rationals in the certificate.
They were proposed numerically, but the checker does **not** treat them as
exact annihilators: it computes each nonzero nominal discrepancy
`eta_d = sum_n q_n (N_new P_d)_n` using `Fraction` and pays it.
This avoids silently converting approximate linear algebra into a theorem.

The exact inherited original action centers come from RC279 for P0/P2/P4
and RC297 for P6. The reference augmentation
`lambda/(H_d+s)` is added *only* at the matching physical degree
`d=0,2,4,6`, with the RC129 `s` interval paid.

For the finite-support dual functional, write

`Q^2 = sum_{n in support(q)} q_n^2/[m_n (H_n+s_lower)]`.

If `||r||_D^2 < T`, coercivity `N_new >= mu I` requires
`||y||_D <= (||b||_D+sqrt(T))/mu`. Every seed coefficient is
therefore bounded from above, and the entire error budget contains:

1. each exact nonzero nominal finite-output dual action `eta_d`;
2. the **full-domain original action D-fault** for each of four inputs;
3. the rank-317 finite projection augmentation's `s`-variation;
4. the source right-hand side's `s`-variation.

The output degrees beyond the witness support, including degree >2048,
have **exactly zero pairing** with `q`. This is finite-support
orthogonality, *not* an assertion that the original infinite D-tail
vanishes or a blanket omission of its cost in an ordinary full-domain
residual estimate.

The checker verifies the exact rational contradiction

`|q*b_mid| - source_error - sum_d coefficient_bound_d * column_error_d > C * Q_upper * sqrt(T)_upper`

for the source-specific constant `C`. Since both C are >1, the
hypothesis `||r||_D^2 < T` cannot hold for **any** `y in V_4`.

## Conditional certified bounds

| Original source | Witness output rows | Guaranteed strict ratio against RC292 tolerance | Result |
| --- | --- | ---: | --- |
| Hard `P0` | 0,2,4,6,8 | **>100** | Every four-column seed excluded |
| Soft `P4-tP0` | 0,2,4,6,14 | **>1000** | Every four-column seed excluded |

These are conservative rational **witness margins**, not assertions of
exact minimizers or measurements of a true inverse solution. The checker
uses rigorous rational upper square roots; the ratios follow from exact
inequalities, contingent upon the same pinned source analytic and
arithmetic contracts used by RC279 and RC297.

### The scope of the obstruction

The new column **does not** solve RC292's strict signed inverse-response
test. More importantly, within the inherited native action estimates,
*none* of the possible `P0/P2/P4/P6` input seeds can solve it.
This excludes one finite **input trial family**, not the true inverse
`N_new^{-1}b`. It is not a negative direction for the Weil quadratic
form, not a refutation of positivity, and not an RH implication.

The approximate signed-rest projection budgets need not even be checked:
the residual tolerance is impossible on the whole four-column family,
so adding a projection constraint cannot rescue it.

**RC299 frontier:** obtain genuinely new certified native input action
columns beyond `P6`, or develop an operator-wide evaluable
prime/archimedean/endpoint action to run the RC292 Chebyshev recurrence.
A fifth input should be judged by whether it defeats a similarly paid
dual test, rather than merely by an improved least-squares fit.

## Reproduction

```bash
python scripts/validate_rpb108_rc298_four_column_dual_obstruction.py --output certificates/rpb108_rc298_four_column_dual_obstruction.json
python scripts/validate_rpb108_rc298_four_column_dual_obstruction.py --output certificates/rpb108_rc298_four_column_dual_obstruction.json --replay
```

GitHub Actions exact replay checks pinned source blobs, the complete
rational inequalities, and the committed witness artifact. It does not
independently peer review imported analytic tail formulas or certify
Stage I closure.
