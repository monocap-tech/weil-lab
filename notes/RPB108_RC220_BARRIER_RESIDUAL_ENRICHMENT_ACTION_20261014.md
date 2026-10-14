# RC220: residual enrichment with an independent canonical action

Starting head: `dc7b695ed4cabfdde7424cb94b371dd74a33ea68` (RC219).

RC220 constructs **q220**, an exact rational even Legendre polynomial of
degree 768 along RC219's saved nominal residual direction. Its complete
canonical action has relative D-norm error below **3.25e-9**. An exact
one-direction correction also proves a strict reduction of that nominal
residual energy. This is a usable new inverse trial vector; the independent
response-source family remains eight-dimensional.

## Capture and action are separate certificates

The RC219 source coefficients and trial coefficients define a nominal
residual `r_nom`. RC220 reconstructs its low coefficients from the pinned
finite native carriers and the exact same represented action formulas used
by RC218. The larger v10 endpoint carrier is retained, and the negative
`r D^-1 v10` term above degree 512 is restored explicitly. No old error
radius is attached to a different nominal action.

The complete nominal residual norm is controlled using RC219's interval
joint block through degree 65534 and RC218's signed analytic tail model.
Subtracting a rigorous captured-prefix energy lower bound, then adding
input coefficient rounding, gives the complete residual-to-polynomial
distance. All omitted finite and infinite input coefficients are paid.

| Polynomial degree | Nominal relative capture error upper |
| --- | ---: |
| 128 | 0.688099 |
| 256 | 0.602872 |
| 512 | 0.509097 |
| 768 | 0.471437 |

Degree 768 passes the nominal half-norm capture budget. The inherited
actual trial-action error radius is about 1.51338e-4, while the nominal
residual norm lower bound is about 5.39144e-5. Their difference does not
provide a positive actual residual norm lower bound. Therefore the
**actual-residual half-norm capture is not certified**. This failure of
the sufficient estimate is recorded without inferring actual residual
failure.

The canonical action of the exact finite polynomial q220 can nevertheless
be certified independently. It uses:

- the signed regular-kernel construction with kernel degree 192, output
  degree 2304, and private 900-digit directed interval arithmetic;
- finite endpoint output through degree 4094;
- 25 exact signed endpoint moments and a geometric remainder covering
  every higher even output coefficient;
- the negative `r D^-1 q220` term and every coefficient-rounding payment.

The complete action radius is the sum of the paid endpoint, negative-term,
and regular-action errors. Its relative error is computed against the
lower D-energy of the exact polynomial. The actual diagonal pairing is
also certified strictly between `a ||q220||_D^2` and `2 ||q220||_D^2`,
with `a=32125/230953`.

## A proved correction of the saved witness

Let `d` bound `||r_nom-q220||_D` and `m` bound `||M q220||_D`, obtained
from the represented finite action energy, its full analytic tail, and
the independently paid action radius. The actual canonical diagonal
pairing gives

`<r_nom, M q220>_D >= <q220, M q220>_D - d m = b > 0`.

For the saved positive rational `theta`, this yields

`||r_nom-theta M q220||_D^2 <= E_old_upper - 2 theta b + theta^2 m^2`.

Paying `theta` times the new action error returns this correction to the
stored nominal eleven-action span. The resulting nominal residual energy
upper bound is **strictly below the old nominal residual energy lower
bound**. The certificate saves this rational inequality, the reduction
fraction, and the corrected witness's nominal residual-chord width upper
bound. The saved correction proves at least **9.3967% nominal residual
energy reduction**. Its one-direction nominal residual-chord width upper
bound is **0.591837**, still above 0.5. This is a new bound for the saved
direction in the enlarged nominal span, not a replacement for RC218's
global eight-source inverse-width enclosure.

## Validation and continuation

```bash
python scripts/validate_rpb108_rc220_barrier_residual_action.py --output certificates/rpb108_rc220_barrier_residual_action.json
python scripts/validate_rpb108_rc220_barrier_residual_action.py --output certificates/rpb108_rc220_barrier_residual_action.json --replay
```

Replay rechecks all immutable Git blob pins, reverses finite reconstruction,
signed regular-kernel and endpoint summations, and compares the complete
certificate. The input metric and endpoint correction are retained; no
cutoff commutation or residual/action error independence is assumed.

RC221 should certify the new mixed/action rows for q220 and evaluate the
eleven-trial, eight-source inverse. The global RC218 inverse enclosure is
not improved by declaration here, and RC219's all-coefficient obstruction
has not been reevaluated uniformly in the enlarged span.

The RC210 six-source inverse width 0.4361 and RC216 eight-source action-error
gate 0.420465 are unchanged. Eight-source inverse acceptance, source-range
coverage, odd coverage, Stage I, RH, F4, and Lean closure remain open.
Publication is add-only; existing repository files are unchanged.
