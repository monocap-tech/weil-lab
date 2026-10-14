# RC226 - coherent signed tails and a fixed-payment obstruction

RC226 improves the certified actual eight-source inverse-response width
from RC225's 0.770397 to **0.766318**. The half-Gram gate remains open.
More decisively, an exact audit proves that the fixed trial's current
two-sided coupled payment model has width at least **0.578135**, for every
positive payment parameter. Further scalar parameter tuning cannot pass
this particular model's 0.5 gate.

This model obstruction is not a lower bound on the true operator error or
actual inverse width. It does not exclude other trial maps, stronger error
models, or mixed structural/inherited endpoints.

## Signed tails before envelopes

Write U for the RC225 trial, r for its nominal residual, and W_c=U+c*r.
The lower coupled endpoint uses c=1; the upper uses c=2/a, where
a=32125/230953. Previously their Grams used separate bounds on U, r,
and their infinite-tail pairing. RC226 reconstructs each W_c finite Gram
directly from the pinned source, mixed, and action Gram intervals, then
combines the signed leading coefficients of its common eta tail before
paying the nonleading remainders. A positive weighted triangle majorant
pays every remaining tail function without assuming orthogonality.

The nominal residual tail receives the same coherent leading/remainder
payment. The actual inverse identity is unchanged. Its variational tail
pairing is still paid, while its W_c term now uses the direct combined
Gram. The old cross-tail parameter remains in the inherited parameter
schema but does not affect this new W_c bound.

The response family remains eight sources and the trial span eleven
vectors. The RC225 trial coefficients, canonical operator, domain, source
normalization, action centers, action-error radii, and cutoffs are unchanged.
The complete shared regular high-input, delta regular low-input, matched
centered endpoint, and remaining individual error terms are retained.

## Exact fixed-model audit

Let E_C be the retained centered-endpoint Gram payment. Every allowed
four-component Young error matrix E satisfies E >= E_C. On a fixed
rational response probe, the paid coupled gap is bounded below by

    B + 2 sqrt(U_tail R_tail)
      + sqrt(W_lower E_C) + sqrt(W_upper E_C),

where all symbols here denote scalar probe energies, and

    B = base_gap + N_upper/a - N_lower/2 + (1/a-1/2) E_C.

The inequality follows from t*A+B/(4*t) >= sqrt(A*B) for positive t;
it applies independently of all error-combination and endpoint parameters.
The validator checks the required PSD matrices and evaluates the probe
using exact rational arithmetic. Integer square roots supply certified
lower bounds on the three geometric-mean terms. Dividing by the unchanged
source-reference probe energy proves the 0.578135 floor.

The probe was proposed from numerical generalized eigenvectors, but its
coefficients, scalar energies, square-root inequalities, and final floor
are checked exactly. Numerical optimization supplies candidates only.
The selected actual enclosure still has both endpoints coupled and all
actual action errors, finite rounding uncertainty, and infinite tails paid.

## Custody and next frontier

The validator pins the entire inherited chain and the RC225 certificate
and helper. Reverse replay uses the saved rational parameters and audit
probe and reproduces the parsed certificate exactly. Publication adds
three files with an expected-head non-force branch update and preserves
all prior files. The additions are scanned for conflict markers.

RC227 should change the fixed trial or the retained endpoint-error/residual
construction. Repeating positive scalar tuning on the audited fixed model
cannot close its gate. The accepted six-source inverse width 0.4361 and
RC216 eight-source native action-error gate 0.420465 remain unchanged.
The actual eight-source inverse gate, source-range and odd-sector coverage,
Stage I, F4, Lean, and RH remain open.
