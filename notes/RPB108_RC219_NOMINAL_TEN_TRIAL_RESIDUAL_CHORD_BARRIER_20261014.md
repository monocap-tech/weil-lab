# RC219: fixed nominal ten-trial residual-chord obstruction

Starting head: `0dd0af802ac0f7a0c60d102f61d5f3243e32dac7` (RC218).

RC219 certifies a **0.65 lower bound** for the ideal two-sided spectral
residual-chord width in the fixed RC218 nominal ten-action span. The required
width is at most 0.5. The statement holds for **every real or complex trial
coefficient**, rather than only the two trial maps evaluated in RC218.

This resolves a specific next-frontier choice: reducing action-error payments
while retaining these nominal carriers cannot make this two-sided chord pass.
Residual enrichment, recomputed carrier centers, or a different inverse
enclosure mechanism remains necessary for this approach. Mixed structural
endpoints and other inverse methods are not excluded by this certificate.

## Exact certificate

Let `w` be the saved rational eight-source direction, `f_w` its source
combination, and `x` arbitrary coefficients in the ten nominal action
carriers. The interval matrices from RC218 cover the D-energy prefix through
degree 65534. They produce an 11 by 11 joint block `K` for

`[1,x]^* K [1,x] = ||f_w - sum(x_k nominal_action_k)||_prefix^2`.

The sign-aware interval evaluation and weighted Loewner rounding give a
rational lower block `K_lower`. Set

- `a = 32125/230953`;
- `c = 1/a - 1/2`, the residual-chord coefficient;
- `q = w^* G_source_upper w`, an upper bound for the full source energy;
- `kappa = (13/20) q / c`.

The validator checks **`K_lower - kappa e_0 e_0^*` is positive semidefinite**
using exact rational arithmetic. Consequently every `x` has prefix residual
energy at least `kappa`. The full nominal residual energy is at least its
prefix energy, so its ideal residual-chord gap is at least `(13/20) q`, and
therefore at least `(13/20) ||f_w||_D^2`. Infinite residual tails can only
increase this norm; discarding them here is valid for a lower bound.

The spectral residual identity motivating this diagnostic is that, for an
exact trial action and residual `r=f-Mu`, inverse-response bounds using
`(1/2) ||r||_D^2 <= <r,M^-1 r>_D <= (1/a) ||r||_D^2`
have gap `c ||r||_D^2`. RC219 establishes a geometry obstruction for the
stored nominal carriers in this formula. It does **not** assert those
carriers are exact actions of the actual operator.

The floating generalized eigenvector only proposes `w`. The resulting
rational witness, all input and helper blob pins, interval block, rounding
diagonal, and exact PSD witness are saved. No numerical eigenvalue is used
as a certificate. The reported 0.65 is a deliberately conservative proved
floor, not a claimed optimum.

## Next usable interface

The certificate also saves a rounded rational least-residual trial for this
direction, its signed source coefficients, its finite nominal residual
energy interval, and its complete trial-action error radius by the triangle
inequality. These define an enrichment proposal. No additional source,
canonical action, or enriched inverse gate is claimed to be certified.

RC220 should construct and certify a useful residual enrichment along this
direction, or justify a different inverse enclosure. A larger inverse trial
space need not enlarge the independent response-source family.

## Validation and retained scope

Run:

```bash
python scripts/validate_rpb108_rc219_nominal_trial_span_barrier.py --output certificates/rpb108_rc219_nominal_trial_span_barrier.json
python scripts/validate_rpb108_rc219_nominal_trial_span_barrier.py --output certificates/rpb108_rc219_nominal_trial_span_barrier.json --replay
```

Replay reverses pin traversal, rechecks every immutable dependency and exact
PSD assertion, and compares the complete output with the saved certificate.
Publication adds this validator, certificate, and note to RC218; no prior
repository files are edited.

The accepted RC210 six-source inverse width remains 0.4361. The RC216
eight-source action-error gate remains 0.420465. The eight-source inverse
gate remains open. This checkpoint proves neither a true inverse failure
nor Stage I, RH, F4, or Lean closure.
