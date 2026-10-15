# RC302 — native polynomial action on V5, uniform D error, and exact noninvariance

**Parent:** merged RC301 `197e0ede552e633d7cb661158451164aca4a632f`.  
**Carrier:** physical original Weil aperture B=11/10, augmented rank-317 even reference.  
**Input domain:** `V5 = span{P0,P2,P4,P6,P8}`.  
**Standing:** original Weil positivity, true inverse response, Stage I, global F4, RH, and Lean **OPEN**.

## Research question

RC301 excluded the entire five-input family from meeting RC292's stringent sufficient inverse-residual tolerance. Merely adding more seed optimizers is now unproductive. RC302 asks what a **reusable native polynomial action interface** can actually certify from the existing input columns, and whether the available carrier is closed under the action needed by a Chebyshev inverse recurrence.

The answer splits into a positive and a negative theorem.

## 1. Positive theorem: all supported polynomials share an actual action contract

For every rational input `y = y0 P0 + y2 P2 + y4 P4 + y6 P6 + y8 P8`, the finite model action is obtained by the exact linear sum of the five independently evaluated native original-action profiles and five **single-coordinate** rank-317 physical augmentations:

`hatN(y)_n = sum_d y_d c_{n,d} + 1_{n in {0,2,4,6,8}} y_n lambda/(H_n+s_mid)`

for **all** n from 0 through 2048. The operator itself is not truncated: the native profiles retain their original global D-faults and infinite high-output D-energy tails.

Let `E_d` denote the full original source-action D error, including its independently charged tail D norm and physical augmentation interval error:

`E_d = original_global_D_fault_d + sqrt(original_tail_D_energy_d) + sqrt(m_d(H_d+s_upper)) * radius_d`.

For `w_d=m_d(H_d+s_lower)`, the exact finite-rank interface obeys

`||N_new y - hatN(y)||_D <= sum_d |y_d| E_d <= C5 ||y||_D`

where

`C5 = sqrt(sum_d E_d^2/w_d)`

is rigorously enclosed above using rational outward square-root rounding. This is a **basis-independent, coefficient-independent bound over the entire five-dimensional supported input space**, not a list of isolated examples. The action formula and its bound also extend to real coefficients by finite-dimensional linearity/continuity, under the inherited source assumptions.

The validator tests exact parity, 2049-coordinate linear superposition, two genuinely mixed signed polynomial inputs, and the global error-budget inequality. It stores a small sample of output centers rather than duplicating five already-pinned 2049-coordinate arrays in the certificate.

## 2. Negative theorem: the supported polynomial space is not invariant

The original-plus-augmentation action of P0 (and independently P8) has a **nonzero physical P10 output component**. Since P10 lies outside V5, the actual image cannot lie in V5.

This is not inferred from a nonzero rounded coefficient alone. The validator proves the exact strict rational inequality

`m_10 (H_10+s_lower) * c_{10,d}^2 > original_global_D_fault_d^2`

for d=0 and d=8. Because the physical augmentation on these sources affects only their **own** retained coordinates, it does not alter the output component at n=10. Consequently, even paying the full inherited original D-fault, that exterior component cannot disappear.

The certificate gives an outward-safe positive lower bound for the D-distance from the true output to V5.

Thus **N_new V5 is not contained in V5**. The existing five-column interface cannot simply be fed its own general output and used to perform a second operator multiplication on that output, much less the full RC292 Chebyshev recurrence. This is a precise missing API-domain obligation, not a statement that the full operator lacks a well-defined square.

## 3. What it does not show

The uniform constant C5 controls only V5; it is **not** a global operator norm or an arbitrary-degree analytic tail theorem. RC279/297/300 materialized the five inputs separately, and their analytic assumptions are inherited. The negative result is noninvariance of the *finite polynomial trial space*, not a negative source direction for the original Weil quadratic form or impossibility of the actual inverse.

No new 314-dimensional Schur positivity, Stage I, RH, or Lean certificate is asserted.

## RC303 next requirement

Extend the source-action evaluator to genuinely new arbitrary polynomial degrees, with a degree-uniform signed prime/archimedean/pole/endpoint formula and degree-indexed global error and tail control. An operator recursion must accept the supported input **and its high-output image**, without silently discarding modes beyond degree eight or assuming the output is invariant under the trial space.

## Reproduce

```bash
python scripts/validate_rpb108_rc302_polynomial_action_interface.py --output certificates/rpb108_rc302_polynomial_action_interface.json
python scripts/validate_rpb108_rc302_polynomial_action_interface.py --output certificates/rpb108_rc302_polynomial_action_interface.json --replay
```

The result is contingent on pinned native original source formula and tail contracts; the Actions replay establishes computational custody, not independent proof of the imported analytic assumptions.
