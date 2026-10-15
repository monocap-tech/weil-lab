# RC303 — Direct signed prime source on an even polynomial; new native P10 low action

**Parent:** RC302 merged at `be83e44cdccc7cb2435a3630bf782c19ee34e83e`.  
**Carrier:** original Connes–Weil physical aperture `B=11/10`.  
**Cutoff:** original output Legendre degrees 0–64, with omitted D-energy paid.  
**Standing:** full original operator action, Stage I, global F4, RH, Lean all **OPEN**.

## Motivation

RC302 certified the entire known input space `V5=span(P0,P2,P4,P6,P8)`
by linear extension of five previously calculated native columns and
proved it is **not invariant**: even `N_new(P0)` and `N_new(P8)`
have nonvanishing exterior `P10` components. It cannot execute a
Chebyshev recurrence from this input space. The next aim is therefore
an evaluator operating **on the source polynomial itself** rather than
a closed list of stored native response columns.

## A new source-polynomial primitive

RC303 implements `native_prime_on_polynomial(q, prime)` on a
general rational even monomial polynomial `q` with degree <=10.
For each of seven active prime powers, the evaluator takes the
genuine **signed translated input polynomial**

`q(x + ell/B)` and `q(x - ell/B)`,

with the original prime coefficient and physical support restrictions.
It constructs all 14 signed translation terms and 15 exact piecewise
source polynomials. It directly integrates and projects that
piecewise translated polynomial onto Legendre output degrees 0–64.

The omitted prime output is **not** guessed from samples or set to zero.
Its exact model squared L2 energy is determined by Parseval subtraction:

`||Q_prime||_L2^2 - sum_{n<=64} mass_n |(Q_prime)_n|^2 >= 0`.

Source-parameter uncertainty is controlled by the input polynomial's
full physical mass, coefficient absolute sum, and derivative bound,
rather than borrowing a single Legendre-column error.

This prime primitive is defined for all rational even `q` within the
specified finite degree cap, but the certificate exercises an exact
mixed polynomial and the new P10 basis input. It is **not** a uniform
operator-wide analytic result for arbitrary degrees.

## Exact degree-10 and signed-mixed input tests

The degree-indexed original source evaluator now includes P10,
retaining the same original regular archimedean, logarithmic endpoint,
pole Taylor, and seven-prime construction used for P4, P6 and P8.
It reproduces **all 65 low original coefficients and every stored
error component** for the three inherited input degrees before
accepting a new P10 source.

The deliberately signed mixed input is

`q = P4 - (1/2) P6 + (1/3) P8 - (1/5) P10`.

For all 65 output coordinates, RC303 computes its prime action
*directly from this source polynomial* and verifies exact equality
against the linear superposition of four independently computed
single-degree original prime actions. Thus the new source-polynomial
API has a genuine independent implementation check.

The full mixed original low output also combines exact regular and
pole source responses, degree-wise analytic endpoint numerators,
the log(2) source interval, the physical D parameter interval, and
all signed finite-mode coefficient roundoff. It pays the direct
prime omitted energy, regular omitted energy, analytic endpoint
Minkowski bound, regular-kernel and pole uncertainties, and original
prime-parameter faults. Each resulting interval is compared with
the inherited basis-column enclosures.

**Important distinction:** a direct prime action on `q` is now
implemented. The endpoint and regular/pole parts still reuse
degree-wise analytic formulas and error bounds. This does not certify
a globally source-degree-uniform analytic estimate, nor does it
grant the power to apply the full operator repeatedly to an infinite
output vector.

## Outstanding analytic issues

1. The inherited endpoint tail bound contains a factor
   `(64-d)^-2`; it is only used where `d<64` and is not
   a degree-independent estimate beyond the fixed output cutoff.
2. The original prime-parameter fault uses a source-dependent
   monomial coefficient/derivative bound; more general polynomial
   degrees may make this large.
3. The direct source primitive provides a finite-output prime model
   and an all-output prime L2 remainder. It does **not** supply the
   weighted full `D` action on arbitrary infinite inputs or show
   stability of the Chebyshev recurrence.
4. The use of imported analytic formulas at d=10 remains a stated
   proof assumption; exact regressions for P4/P6/P8 do not prove
   that theorem for all input degrees.

## RC304

Extend the signed translated prime source projector and analytic
endpoint coefficients through output degree 2048 for P10 and the
mixed polynomial, attach the rank-317 physical augmentation at
degree 10, and audit whether its degree-dependent tail/error
budget can be made uniform over a useful increasing-degree family.
Avoid claiming arbitrary-input operator control from a single
new finite-degree test.

## Reproduction

```bash
python scripts/validate_rpb108_rc303_direct_polynomial_prime.py --output certificates/rpb108_rc303_direct_polynomial_prime.json
python scripts/validate_rpb108_rc303_direct_polynomial_prime.py --output certificates/rpb108_rc303_direct_polynomial_prime.json --replay
```

All new certificates rely on inherited original Weil source and tail
estimates; exact Actions replay verifies pinned arithmetic custody,
not independent peer review or Stage I closure.
