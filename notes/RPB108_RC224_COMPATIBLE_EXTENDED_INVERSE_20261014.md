# RC224 — compatible extended endpoint inverse

RC224 rebuilds the eight-source inverse calculation using RC223's extended
delta/t10 endpoint centers together with their certified error radii. The
actual inverse-response width improves from RC222's 4.590826 to **0.778220**,
on the same source Gram normalization. The half-Gram gate remains open:
0.778220 is greater than 0.5. This is a certified enclosure improvement,
not an actual inverse-width lower bound or a Stage I closure.

## Compatible reconstruction

The response family is still P0, P2, f0, psi0, w14, v10, delta=z_b6-v10,
and t10. The eleven inverse trial vectors retain q185, q202, and q220.
The source definitions, operator, domain, and normalization do not change.

The finite prefix through degree 65534 reconstructs both changed mixed
columns and every nominal action-Gram entry involving delta or t10. Every
source-Gram entry and each unaffected mixed/action entry is checked against
RC221 exactly. All 33 actual self-adjoint pairing intersections involving
delta, t10, or q220 are nonempty, with both orientations' tails and action
errors paid. The new endpoint moment centers also determine the analytic
output-tail bounds; their rounding errors remain in the complete action
error ledger.

Both the rebuilt least-residual eleven-vector trial and RC221's fixed trial
are evaluated against the new action centers. RC222's earlier actual
enclosure remains available as an independently valid fallback. Its old
approximant centers never receive RC223's smaller radii.

## Paid enclosure

The selected rebuilt trial has nominal residual Gram upper bound 0.057170
and complete shared trial-action error Gram upper bound 0.005812, relative
to the unchanged source Gram. These are intermediate payment bounds;
neither is the inverse width. The final two-sided coupled enclosure is
0.778220.

The shared regular high-input smoothing, delta regular low-input band,
matched centered endpoint error, and remaining individual error terms are
all retained. Endpoint omissions for the five infinite-source endpoint
actions now begin at degree 32768. Positive weighted triangle payments
combine the error components without assuming output orthogonality.
Source tails, analytic action tails, finite rounding, and input/output
projection errors are paid. No actual action error is artificially zeroed.
Numerical optimization only proposes rational parameters; exact rational
PSD tests certify the resulting enclosure and gate status.

The validator supports a reverse-order replay using the saved rational
proposals, with byte-equivalent parsed main and prefix certificates.
Publication adds four new files without replacing earlier artifacts and
uses an expected-head, non-force branch update.

## Remaining frontier

RC225 should inspect the rebuilt residual-tail and shared-error payments
and refine the dominant contribution. RC219's nominal ten-trial chord
obstruction does not rule out this eleven-trial calculation, and RC222's
fixed old endpoint-payment audit does not apply unchanged to the matched
RC223 endpoint model.

The accepted six-source inverse width 0.4361 and RC216 eight-source native
action-error gate 0.420465 are retained. The actual eight-source inverse
gate, source-range and odd-sector coverage, Stage I, F4, Lean, and RH
remain open.
