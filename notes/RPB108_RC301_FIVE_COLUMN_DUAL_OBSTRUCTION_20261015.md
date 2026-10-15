# RC301 — all five-column native signed inverse seeds excluded by a six-output dual

**Parent:** RC300 merged to Route Consolidation as `a129ecab91665fb87aabc93a51348016bf0eb051`.
**Original even input span:** `V_5=span{P0,P2,P4,P6,P8}`.
**Preferred positive reference:** rank 317, even rank 122, aperture `B=11/10`.
**Standing:** Stage I, full original Weil positivity, F4, RH and Lean **OPEN**.

## Why the new fifth column matters

RC295 established a three-input-column obstruction against RC292's
strict sufficient inverse-response residual thresholds. RC298 repeated
the obstruction for all four inputs P0/P2/P4/P6. RC300 provided a fifth
genuinely evaluated original input-action column P8, projected through
output degree 2048 with complete original high-output error and its
single-coordinate rank-317 augmentation.

RC301 tests whether the additional source coordinate resolves the
inverse-approximation obstruction. The method does **not** simply
optimize two more five-coordinate seed vectors. It instead gives a
finite-output dual contradiction for **every real seed in V_5**,
without requiring its signed-rest projection to satisfy RC292's
additional projection cap. This is stronger on the restricted trial
family than failure of a particular least-squares proposal.

## Exact six-output dual witnesses

For `b=D^-1 v`, `N_new=D^-1 G_new`, and `y in V_5`,
the native residual is `r=b-N_new y` and RC292 requires
`||r||_D^2 < T` as one sufficient condition for paying the
cross Schur terms. Use exact rational dual coefficients `q_n`
on the following six-output index sets:

| Original source | Dual output degrees | Exact lower margin | Outcome |
| --- | --- | --- | --- |
| Hard P0 | 0,2,4,6,8,16 | **>100×** | Every five-input seed ruled out for RC292 tolerance |
| Soft P4−tP0 | 0,2,4,6,8,14 | **>1000×** | Every five-input seed ruled out for RC292 tolerance |

The decimal-looking dual coefficients in the stored certificate are
**exact rational witnesses**, suggested by finite numerical exploration.
Crucially, the five rational nominal annihilation discrepancies
`eta_d=sum_n q_n (N_new P_d)_n` are evaluated using `Fraction`
and paid **without assuming they vanish**.

The rest of the proof is a paid dual Cauchy argument:

- `Q^2=sum_n q_n^2/[m_n(H_n+s_lower)]` bounds `q*r`
  by `Q ||r||_D`;
- `N_new>=mu I_D` gives
  `||y||_D<=(||b||_D+sqrt(T))/mu` for any hypothetically
  accepted seed, controlling each coefficient;
- the full original-action D-fault for each of P0, P2, P4, P6,
  P8 is charged, alongside each `eta_d`, the source interval
  error and every single-coordinate projection-augmentation
  interval error;
- all original output degrees outside the finite witness support,
  including >2048, have *zero pairing with the dual functional*.
  This is exact finite-support orthogonality, not a zero-tail claim
  about the original operator or a global full-residual certificate.

The checker proves exact rational strict inequalities with
`gap > 100 Q sqrt(T)` (hard) and `gap > 1000 Q sqrt(T)`
(soft), after all these charges. There is therefore no real
`y in V_5` meeting the **unchanged** RC292 residual acceptance
threshold for either source, given the imported original action
and positivity estimates.

## Mathematical interpretation

Five native action input columns suffice to **exclude this finite
Galerkin trial class**, not to decide the original Weil form.
An actual inverse solution may use arbitrarily many input degrees;
no finite-column dual test forbids that. The true signed inverse
projection, global 314-dimensional remaining principal Schur gate,
Stage I, F4, RH, and Lean remain unproved.

The new observation is methodological: even as the constructed
native input family grows from three to four to five, residual
acceptance continues to fail by orders of magnitude. Continuing
to optimize exactly these five inputs is mathematically futile
for RC292's specified strict sufficient residual route.

The evidence favors developing a **reusable original Weil
operator action on arbitrary polynomial input vectors**, with
uniform certified prime, archimedean, pole and endpoint output
bounds, so that the full RC292 Chebyshev inverse-response
recurrence can be executed rather than repeatedly hand-coding
single Legendre inputs.

## Next frontier — RC302

Specify and audit the arbitrary-degree source-action interface.
Separate linear finite-combination support (already mathematically
available for the five known columns) from an evaluator applicable to
the recursively produced vectors over *all* required degrees.
State which analytic estimates are truly uniform in input
degree and which remain imported per-column assumptions.
Until an operator-wide action is certified, further columns
remain a fallback, not the preferred new mathematical strategy.

## Reproduce

```bash
python scripts/validate_rpb108_rc301_five_column_dual_obstruction.py --output certificates/rpb108_rc301_five_column_dual_obstruction.json
python scripts/validate_rpb108_rc301_five_column_dual_obstruction.py --output certificates/rpb108_rc301_five_column_dual_obstruction.json --replay
```

Actions replay validates exact rational arithmetic and the pinned
source-code/artifact inputs; it is not independent peer review of
the inherited analytic formulae or the Weil positivity theorem.
