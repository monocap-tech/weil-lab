# RC299 — native P8 original-action column with exact P4/P6 regression

**Parent:** RC298 merged at \`acb7ce39ff7f354fcc4e155870eb0a4bc5ddaa94\`.
**Carrier:** original Connes–Weil aperture \`B=11/10\`.
**Reference for subsequent augmentation:** rank 317, even rank 122.
**Mathematical standing:** Stage I, F4, RH and Lean remain **OPEN**.

## Why this pass

RC295 and RC298 proved that the strict RC292 approximation thresholds
cannot be reached by any input seed supported on, respectively,
\`span{P0,P2,P4}\` and \`span{P0,P2,P4,P6}\`.
The latter no-go is not a claim that the true inverse fails; it says
that continued numerical optimization *inside that four-column space*
cannot clear the specific acceptance gate.

The immediate productive response is to enlarge the **actual native
input-action oracle**, not to rerun more four-column least squares.
RC299 generalizes RC296's formula for the next even input \`P8\`.

## Exact construction and formula controls

The new validator evaluates the original, **not yet augmented**, Weil
action on P8, retaining all even outputs through degree 64 and explicitly
paying the remaining output in its D-energy budget:

- The native Legendre input polynomial and signed analytic endpoint
  coefficients, including the source-degree-dependent diagonal;
- The regular archimedean polynomial and its inherited uniform error;
- The pole Taylor term with its remainder;
- All seven active prime powers, both signed translations for each,
  and the fifteen induced physical prime segments;
- Prime-parameter uncertainties, finite coefficient rounding, and
  regular/prime/endpoint omitted-mode bounds.

**Important regression:** before evaluating P8, the identical
degree-parameterized algorithm must reproduce *all 65* original
coefficients and **every** error component previously frozen for P4
(RC240) and P6 (RC296). Any coefficient, normalization, or error
budget discrepancy fails the validator.

The test uses exact Python \`Fraction\` arithmetic and immutable
Git-blob pins for all inherited data and helper source. Floating-point
search results do not establish any inequality in this checkpoint.

The uniform-in-degree use of the legacy endpoint and source formulas
at d=8 remains an **imported analytic obligation**, not a newly
independently proved general-domain theorem. Exact regression at
degrees 4 and 6 detects implementation drift; it does not establish
every imported estimate for degree 8 from first principles.

## What this proves — and does not

This checkpoint adds a fifth explicit original-action **input**
column P8 through output degree 64, with a global bound on all omitted
output, contingent on the inherited analytic estimates.

It is **not yet** an exact coefficient-by-coefficient original action
through degree 2048. Nor is it a rank-317 augmented action or
operator-wide recurrence evaluator. In particular, it cannot legitimately
claim that an arbitrary vector arising in the RC292 Chebyshev inverse
recurrence has been evaluated.

The RC298 exclusion remains valid for the *smaller* four-column trial
space. It does not automatically extend to a five-dimensional space
containing P8.

## Next: RC300

1. Resolve P8's original signed prime and analytic endpoint projection
   explicitly for modes 65–2048, with all higher D output controlled.
2. Add the rank-317 physical augmentation *only* at n=8:
   \`N_new P8 = N_original P8 + lambda/(H8+s) P8\`.
3. Compare a genuine five-input family against RC292's fixed signed
   residual thresholds, including finite-output dual obstructions.
4. Continue developing a repeatable degree-parameterized oracle.
   Repeated column construction is **not** yet a uniform arbitrary-input
   operator norm bound.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc299_native_p8_action.py --output certificates/rpb108_rc299_native_p8_action.json
python scripts/validate_rpb108_rc299_native_p8_action.py --output certificates/rpb108_rc299_native_p8_action.json --replay
\`\`\`

The second command recomputes the exact result and requires it to match
the committed certificate byte-for-byte. A failed replay never qualifies
as a new result. GitHub Actions checks reproducibility, not independent
peer review of the analytic inputs.
