# RC229 - Stage I operator and coverage audit

RC228's exact eight-source canonical inverse gate remains passed at
**0.485647 < 0.5**, with margin **0.014353**. RC229 rechecks that gate and
transfers it by exact congruence to the earlier seven-source frame.
The twelve trials are sufficient for the specified finite inverse test.
Increasing that trial count is not the remaining Stage I stopping rule.

The important remaining distinction is the operator being solved. The
tested inverse is M^-1, where M=D^-1 L and L is the supported canonical
Fourier metric action. RC121 explicitly separates L from the original
Weil operator A_Q and from its positive augmentation H. RC228 does not
claim an inverse response for H or the full original source range.

## Exact transfer to the native seven-frame

RC228's response order is (P0,P2,f0,psi0,w14,v10,delta,t10), with
delta=z_b6-v10. Let T map native coordinates in the order
(P0,psi0,f0,w14,v10,z_b6,t10) to that eight-frame:

| Native source | Eight-frame coordinates |
| --- | --- |
| P0 | P0 |
| psi0 | psi0 |
| f0 | f0 |
| w14 | w14 |
| v10 | v10 |
| z_b6 | v10 + delta |
| t10 | t10 |

Congruencing the source Gram and both inverse endpoints by T yields
positive seven-frame Gram and enclosure matrices and the same certified
relative-width upper bound 0.485647. The validator checks these matrices
by exact rational elimination. This is a transfer of the new fully paid
canonical inverse enclosure; it does not attach old independent z action
centers or radii to the rebuilt correlated source.

Thus the previous native seven-frame is included in the passing eight-frame.
It is not a statement that either finite frame exhausts the original
augmentation source range or that a reference/augmented inverse has been
identified with M^-1.

## What odd coverage is already known, and what is missing

All eight response sources and all twelve trial vectors have only even
Legendre degrees. Their infinite tails also have even support. The actual
canonical metric and endpoint/regular actions preserve reflection parity.
The nonzero odd polynomial P1 is D-orthogonal to every tested source, with

    ||P1||_D^2 >= (2B/3)(1+s_lower) > 0,  B=11/10.

The validator computes this positive exact lower bound using RC129's
actual constant enclosure. Consequently the tested source span contains
no nonzero odd vector. Enlarging its even trial span cannot by itself
produce an odd response certificate.

This does not erase earlier odd results. RC112 already proves a global
original complement floor 5001251/500000000 > 0.01 outside an explicit
639-dimensional exceptional head: 248 even and 391 odd dimensions.
It also provides the inherited 611-dimensional effective strong
compression. RC115 constructs both parity adjoint source tests, and
RC116-RC118 provide source-realization information. What is missing here
is a complete odd response construction for the chosen original
augmentation, not the entire odd parity theory or its complement bound.

The number 639 is an exceptional-head dimension and an auxiliary rank
upper bound, not a complement dimension or a requirement to evaluate
639 dense responses. A structured or matrix-free proof can discharge the
full-range obligation, provided every omitted range is controlled.

## Original augmentation acceptance contract

RC114's projection-free route uses

    H = A_Q + Q*Q,   B_aux = Q H^-1 Q*.

Original positivity requires a complete bound B_aux <= (1-zeta) I_aux
with zeta>0. With a trial Y and r=Q*-HY,

    B_aux = QY + Y*Q* - Y*HY + r*H^-1 r.

The residual correction is added. It must not be imported with the
subtracted sign used in a different effective-head identity. The
auxiliary frequency metric, canonical metric, and D-energy metric are
distinct and require explicit transfer.

RC115 also gives a rational-model Hhat. It is a different augmentation
with its own response operator. Matching positive lower floors is not
permission to reuse upper spectral endpoints, action budgets, inverse
responses, or a correction from another augmentation.

RC229 supplies an exact abstract nonimplication control: a positive
canonical metric M=I has inverse width zero; an eight-dimensional
auxiliary restriction is 1/4 I and passes; an unseen odd auxiliary
direction has value 9/4, leaving the original form value -5/4. The
example preserves parity and the augmentation algebra. It is a logical
control, not an actual negative Weil direction or an arithmetic
counterexample. It confirms why neither metric-inverse acceptance nor a
passing auxiliary restriction establishes the missing full-range bound.

## Remaining obligations

| Obligation | Required evidence |
| --- | --- |
| Original action interface | Actual A_Q or chosen H/Hhat actions, with prime, signed pole, augmentation, and approximation errors paid |
| Full source range | Exact factorization/exhaustiveness or a uniform bound on the discarded augmentation range |
| Odd responses | Canonical odd source realization and actual original/augmented action and inverse-response contracts |
| Auxiliary metric | Frequency Gram or an equivalent full-range operator estimate, with all factor and truncation errors |
| Original positivity response | Complete response norm below one, or an equivalent complete signed original Schur certificate |
| Stage I assembly | Composition in the same operator, source definitions, domains, parity decomposition, and metrics |

No minimum additional source count or number of optimization passes is
proved. Finite trial sufficiency is already established for RC228's gate;
coverage and the original operator interface are the next questions.

## Verification and custody

The audit pins RC228 and the earlier operator, coverage, augmentation,
source-range, and native-frame evidence. It recomputes the accepted
matrix inequalities, native-frame congruences, parity witness, and
abstract signed control in exact rational arithmetic. Reverse-order
replay reproduces the entire certificate. Publication adds the audit
validator, certificate, and this note through an expected-head non-force
update, preserving the preceding files and passed gates.

RC230 should establish the chosen original augmentation source-range and
operator interface, then develop its odd responses and auxiliary metric.
Stage I, original augmented response acceptance, F4, Lean, and RH remain
open. The canonical metric inverse pass is retained without being
relabelled as original Weil positivity.
