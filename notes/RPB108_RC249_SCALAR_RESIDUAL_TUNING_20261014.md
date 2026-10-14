# RPB108 RC249: scalar residual tuning and its certificate obstruction

Starting head: `ca8ab074bde5ec4216c75226a812d7c772763cd6` (RC248).

For the RC248 selected trial polynomial Z, let f=N0 Pbase and e=f-N Z.
RC249 uses the exact identity
`e(t)=f-N(t Z)=t e+(1-t) f` for every real scalar t. The RC248 residual
center and complete error bound, together with RC245's degree-128 original
source center and complete error bound, enclose this scaled residual.
All omitted outputs and model faults are inherited. Same-parity errors
are combined by the norm triangle inequality, with no independence or
orthogonality assumption.

The retained center squared D-energy is an exact quadratic polynomial in
t, with the canonical metric parameter interval paid. The full error
norm bound is `delta(t)=|t| sqrt_up(Ee)+|1-t| sqrt_up(Es)`, rounded upward.
Actual residual energy and the positive augmented inverse bounds give
new inverse-response and signed-gap enclosures. These are intersected
with RC248's intervals. Original N0, augmented N, and the canonical
inverse remain distinct; no operator commutation is assumed.

An exact finite search evaluates 1,001 rational scales from 0.9 to 1.1,
in steps of 1/5000. It does not claim optimality over a continuous domain.

| Source | Selected upper scale | RC248 inverse upper | RC249 inverse upper | RC249 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 1 | 4.493986789 | 4.493986789 | [-4.405427593, 0.077120767] |
| N0 P1 | 997/1000 | 6.339861093 | 6.339354546 | [-6.242271730, 0.083675302] |

Decimal entries are approximate; the certificate stores rational
endpoints. The prior inverse lower endpoints, approximately 0.011438429
and 0.013407514, are preserved.

RC249 also certifies a limitation of this particular inherited scalar
error envelope over **all real t**. Write Cnom(t) for the midpoint
variational center and nl(t) for the retained center squared energy
using the lower metric endpoint. The computed inverse UPPER formula is
at least

`q(t)=Cnom(t)+(nl(t)+t^2 Ee)/mu`.

This follows because its upper variational center exceeds the midpoint,
its retained center norm exceeds the lower-metric norm, and its chosen
error norm squared exceeds t^2 Ee. The omitted nonnegative norm cross
term is dropped. The exact quadratic has a positive leading coefficient,
so completing the square gives a uniform floor.

| Source | Uniform floor of inverse UPPER formula | Uniform ceiling of direct signed-gap LOWER formula |
| --- | ---: | ---: |
| N0 P0 | 2.271508269 | -2.182949073 |
| N0 P1 | 3.156820519 | -3.059737704 |

The direct signed-gap LOWER formula is at most midpoint F00 minus q(t),
by the exact scalar variational identity. The inverse-upper floors also
exceed the respective original source form upper bounds. Thus neither
lower-gap route in this scalar envelope can certify positivity at any
real scale. This does **not** bound the true inverse response from below,
prove a negative Weil direction, exclude other four-trial coefficients,
or exclude freshly recomputing coupled actions for each scaled input.
It identifies a limitation of the specified reused certificates.

Validation: 182 inherited Git blob pins; exact all-real completion of the
square; every grid candidate checked against the uniform envelope; exact
nonidentity metric and noncommuting operator controls for the scaled
residual identity and variational inverse enclosures. Replay reverses
the pin, energy-summation, and candidate orders and requires equality of
the complete JSON, with deterministic tie selection.

Run:
`python scripts/validate_rpb108_rc249_scalar_residual_tuning.py --output certificates/rpb108_rc249_scalar_residual_tuning.json`

Replay:
`python scripts/validate_rpb108_rc249_scalar_residual_tuning.py --output certificates/rpb108_rc249_scalar_residual_tuning.json --replay`

The sources and four-trial spaces are unchanged. The rank-639 signed
criterion (248 even and 391 odd) remains unevaluated, and the original
full auxiliary norm gate remains open. The separate canonical eight-source
inverse width stays `485647/1000000`. Stage I, RH, F4, and Lean remain open.

Next cursor RC250: improve complete direct residual output tails or
inverse coercivity; scalar rescaling with this inherited norm envelope
cannot close the signed source tests.
