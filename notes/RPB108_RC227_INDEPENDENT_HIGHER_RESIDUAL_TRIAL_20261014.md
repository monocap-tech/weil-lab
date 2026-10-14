# RC227 - independent higher-degree residual trial

RC227 constructs q227, an exact rational even polynomial of degree 1536,
from RC226's fixed-payment audit direction and the RC225 nominal residual.
Its complete canonical-action relative D-error is below **0.009922**.
An exact source-Gram Schur certificate proves that at least **43.3085%**
of its D-energy lies outside the span of the previous eleven trial vectors.
It is therefore a new, independently certified trial direction.

The response family is still eight sources. Adding q227 makes twelve
inverse trial vectors, once its mixed/action rows are assembled. The
enlarged inverse has not been evaluated in this checkpoint. The accepted
actual eight-source inverse width remains **0.766318**, and its 0.5 gate
remains open.

## Residual capture and exact polynomial definition

The rational target probe is pinned from RC226's payment-model audit. Its
nominal residual is reconstructed using the compatible RC223 endpoint
centers, RC225 trial map, and all eleven existing nominal action columns.
The finite-source/tail boundary at degree 988/990 and the q220 action are
included explicitly in the higher-degree reconstruction.

| Candidate degree | Nominal relative D-distance upper bound, approximately |
| --- | ---: |
| 768 | 0.941287 |
| 1536 | 0.582796 |
| 3072 | 0.580564 |
| 4094 | 0.574310 |

Degree 1536 captures roughly 66% of the nominal residual energy, a marked
improvement over the degree-768 candidate's roughly 11%. Increasing the
degree beyond 1536 gives smaller gains in this capture test. Neither the
selected nominal half-norm capture nor actual half-norm capture passes.
The actual residual nevertheless has a certified positive D-norm lower
bound on this probe. Capture success is separate from certifying the
canonical action of the exact polynomial and from the eventual uniform
eight-source inverse gate.

The stored rational coefficient centers define q227 exactly. Their radius
fields pay its comparison with the nominal target; they do not make the
new polynomial an uncertain input or remove any inherited actual-action
error.

## Complete canonical action

For M=D^-1 L at aperture 11/10, the endpoint action of the complete
degree-1536 polynomial is reconstructed through degree 4094. Twenty-five
exact signed moments define its analytic output beyond that prefix, with
the geometric remainder and finite rounding paid. The negative multiplier
action is retained on the entire input polynomial with its rounding error.

The regular action is split at input degree 768. The low input receives
the exact analytic-kernel/Legendre projection through output degree 2304,
using private 900-digit directed arithmetic and all parameter, series,
rounding, and infinite-output errors. The finite high input at degrees
770 through 1536 receives the inherited high-input smoothing bound:

    ||D^-1 R q_high||_D^2 <= (Phi_768 / s_lower) ||q_high||_L2^2.

Its physical input energy is computed exactly. The same formula is checked
against RC216's pinned Phi_512 value. The high regular-action center is
zero, with its nonzero error fully paid on all output degrees. No output
orthogonality or cutoff commutation is assumed. This error dominates the
new polynomial's complete relative action error of about 0.00992106912.

Exact integer recurrences generate the regular input's monomial
coefficients. Direct coefficient checks and the full Horner parity
identity verify the calculation. This changes the computation cost while
preserving the analytic helper's error estimates.

The complete error ledger also certifies the actual canonical pairing
between a||q227||_D^2 and 2||q227||_D^2, with a=32125/230953.

## Independence, custody, and next frontier

The finite-prefix source Gram is extended to twelve vectors using the
new source pairings and D-energy intervals. Its exact Loewner lower bound
has a positive Schur complement for q227. Since the full source norm
dominates the prefix norm, the resulting distance-from-span lower bound
also holds for the full D-space. This proves independence without claiming
additional independent response sources or source-range closure.

Reverse replay recomputes the capture candidates, complete action, and
source-Gram independence certificate and reproduces the parsed certificate
exactly. Publication adds the validator, certificate, and this note with an
expected-head non-force branch update and preserves the previous files.

RC228 must assemble q227's compatible mixed/action rows and test the
twelve-trial eight-source inverse with all errors and coherent tails paid.
RC226's fixed eleven-trial payment-model floor does not apply unchanged
to a new trial map. The six-source inverse width 0.4361 and RC216 native
action-error gate 0.420465 remain accepted. The actual eight-source inverse
gate, source-range and odd-sector coverage, Stage I, F4, Lean, and RH remain
open.
