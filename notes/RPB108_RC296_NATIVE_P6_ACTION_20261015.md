# RC296 — a new native original P6 input-action column

**Parent:** RC295 `4a7c3afd67f46c28efbbf94a83539ead4766a04a`.
**Reference:** physical aperture B=11/10, proposed rank-317 reduced
augmented reference. **Stage I/RH/F4/Lean remain OPEN.**

## Why P6

RC295 used exact four-output dual annihilators to prove that **no**
response seed supported entirely on P0,P2,P4 meets the strict RC292
residual tolerance for either hard P0 or soft P4-tP0 source. That
mathematical exclusion applies to the 3-column *input subspace*, not
the exact inverse operator or all larger trials.

RC296 introduces a genuinely new original Weil input **P6**,
rather than interpolating the previous three actions. It takes the
symbolic Legendre original-action formulas from RC237/RC240, whose
regular, prime, pole and logarithmic endpoint pieces depend on the
input degree, and evaluates those formulas at d=6.

## Exact input and full-tail calculation

For each even output degree n<=64, RC296 computes the D-normalized
original Weil action coefficient as an interval. Its rational midpoint
and radius are outward rounded; all odd coefficients vanish by parity.
The calculation retains the seven active prime powers and their
complete signed physical prime segments, the regular-kernel
polynomial and its uniform error, the pole Taylor remainder, and
the analytic endpoint coefficient.

All output degrees >64 are paid as D-energy upper terms:

- endpoint omitted-output estimate at the first even omitted degree 66;
- finite polynomial regular omitted output;
- prime omitted output plus prime-parameter arithmetic fault;
- uniform regular-kernel uncertainty and pole-Taylor remainder;
- finite coefficient center/interval rounding.

These are combined in the same full-domain Minkowski D-error contract
as RC240. **No high modes are treated as exactly zero.**

The validator first recomputes the already committed P4 original action
from this generic formula and requires an **exact complete match** for
all 65 coefficients and every original-action error component. This
guards the implementation against a changed normalization, though it
does not by itself independently establish that every analytic tail
formula used for P4 is valid for d=6. That uniform-in-d application is
an explicit imported analytic requirement for interpreting RC296 as
a theorem about the original operator.

## Important mathematical boundary

RC296 produces the fourth native input **original** action column,
not the completed rank-317 augmented action, since the latter still
needs the new physical projection coefficient attached and certified
under its own source pin. The result is a degree-64 original-action
oracle with a paid entire high-output tail, not an explicit
coefficient-by-coefficient action through degree 2048.

This cannot yet run the RC292 full Chebyshev recurrence on arbitrary
vectors, certify the signed projected true inverse response, or close
the 314-dimensional remaining principal Schur gate. It does not
invalidate RC295's no-go result for the smaller P0/P2/P4 subspace.

**Next RC297:** apply the rank-317 physical projection augmentation to
P6 and resolve original prime+endpoint output at degrees 65..2048,
with explicit inherited and fresh global uncertainties; then test
actual four-input-column inverse seeds and possible dual obstructions.

## Reproduce

```bash
python scripts/validate_rpb108_rc296_native_p6_action.py --output certificates/rpb108_rc296_native_p6_action.json
python scripts/validate_rpb108_rc296_native_p6_action.py --output certificates/rpb108_rc296_native_p6_action.json --replay
```

The Actions replay checks exact pinned RC43/46/129/240 inputs and the
RC237/RC240 method sources. It tests arithmetic custody, not an
independent peer-reviewed proof of the inherited analytic formulas.
