# RC307 — direct high signed-prime action and a bounded nominal prime component

**Parent:** RC306 merge `42313bd4739e918e9085ff94a290a0bb5462e4fa`.  
**Original physical aperture:** `B=11/10`.  
**Status:** distinct signed-prime source action advances; original Weil operator, inverse, Stage I, F4, RH and Lean **OPEN**.

## Objectives

RC303 evaluated the seven-prime translated source for the signed mixed
polynomial `q=P4-P6/2+P8/3-P10/5` through output degree 64.
RC304 reached degree 2048 by **superposing four independently evaluated
Legendre columns** but did not perform a separate high-output
projection of the polynomial's own signed prime source.
RC306 supplied much sharper finite-degree arithmetic uncertainty
by physical sup norm and Markov inequalities.

RC307 performs the still-missing **independent high signed-prime projection**
on that actual mixed polynomial, then proves a new and separate
global bound on the nominal prime operator itself.

## 1. Direct mixed source, projected to 2048

The input is the exact rational polynomial

`q = P4 - (1/2)P6 + (1/3)P8 - (1/5)P10`.

The original signed prime model is the sum, over the seven active
prime powers, of two *truncated translated copies of q* with the
respective negative source coefficients. This construction contains
all pairwise source-prime cross terms naturally.

RC307 reconstructs the 14 signed translated contributions and 15
piecewise polynomial segments. It then uses the independent
RC273/RC253 high-boundary projector on that single mixed source.
All even high Legendre output intervals from degree 66 to 2048
are materialized as exact rational intervals. The intervals are
outward-rounded to a fixed rational grid. The boundary formula
is checked against direct polynomial integration at n=66.

The full exact source energy and captured Legendre output energy
yield the model output energy beyond degree 2048 by Parseval
subtraction, without declaring the original infinite source tail
zero. The D-inverse energy tail is paid by the harmonic weight
`1/(H_2050+s_lower)`.

An independent 65-coefficient reconstruction at the **high
projector's chosen admissible rational parameter values** must match
RC273's low digest. RC303 used midpoint parameters instead, so the
models need not agree coefficient by coefficient. RC307 pays the
exact low-mode physical L2 discrepancy using twice RC306's certified
signed-prime parameter uncertainty. This prevents falsely claiming
that the mixed high model is a replay of the old column centers.

## 2. Dimension-free nominal prime action bound

There is a useful operator-theoretic simplification that does **not**
depend on polynomial degree, source derivatives, or prime
arithmetic precision.

Let `T_u` denote translation by `u` on the real line.
Extend `q in L²([-B,B])` by zero outside the aperture.
Each signed paired-prime action has the form

`P_j q = -c_j [1_I T_{u_j}q + 1_I T_{-u_j}q]`.

Translation is an L² isometry on the full line and multiplication
by an interval indicator is an L² contraction. Thus,

`||P_j q||_2 <= 2 c_j ||q||_2`.

Using the exact upper interval coefficient `c_j_high` for all
seven active prime powers:

`||P q||_2 <= C_nom ||q||_2`,
`C_nom=2 sum_{seven} c_j_high`.

No signed-source positivity or finite polynomial degree cap appears
in this estimate. The nominal signed-prime operator extends uniquely
by density to a bounded operator on all physical L².

For the actual positive metric offset `s>=s_lower`, the weighted
D action similarly satisfies

`||D^-1 P q||_D <= C_nom/sqrt(s_lower) ||q||_2`,

and since `||q||_2 <= ||q||_D/sqrt(s_lower)`,

`||D^-1 P q||_D <= C_nom/s_lower ||q||_D`.

This is a bounded **component of the original Weil action**,
not an assertion that the whole original operator (including the
analytic endpoint, regular archimedean, and pole terms) is bounded
on this same space. It is also **distinct from** RC306's error from
uncertainty in prime positions and coefficients, whose finite-degree
bounds grow with degree.

## 3. Exactly what is certified and what is imported

The computer certifies the rational native interval data,
prime-segment construction, high output enclosures, Parseval
energy capture, and the functional consequences of an exact
nominal-prime operator bound. The elementary L² isometry of
translations, interval restriction contraction and
density-extension theorem are imported analytic facts.

The high projector itself is inherited from RC273/RC253 and its
Legendre boundary/analytic interval implementation. The
certificate therefore establishes exact arithmetic custody
*conditional on* these analytic source identities; it is not
independent peer review.

## 4. Remaining full-action obligations

- Complete degree-adaptive direct prime projection for arbitrary
  signed finite input polynomials (only this mixed q is explicitly
  materialized through output 2048 here).
- Account for regular archimedean, pole, endpoint and source
  intervals on a common completion, not merely in per-column
  experimental profiles.
- Establish boundedness or compatible closed-domain mapping of
  the *complete* original action so that successive Chebyshev
  applications are mathematically defined and error-controlled.
- Discharge the original signed inverse/Schur positivity thresholds,
  Stage I, F4 and RH only after the corresponding inequalities exist.

## RC308

Use the dimension-free nominal prime bound plus RC306's
degree-adaptive error estimates as inputs to a complete
original-action common-carrier audit. Seek a direct
degree-adaptive prime output projector, rather than accumulating
more isolated basis columns or declaring the full inverse proven.

## Reproduce

```bash
python scripts/validate_rpb108_rc307_direct_prime_completion.py --output certificates/rpb108_rc307_direct_prime_completion.json
python scripts/validate_rpb108_rc307_direct_prime_completion.py --output certificates/rpb108_rc307_direct_prime_completion.json --replay
```
