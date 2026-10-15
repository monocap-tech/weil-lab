# RPB108 — RC273: resolving the projection response's original-action tail

Parent RC272: `9a51c7978992b91dca65c24f3eba62c060fe1550`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC273 keeps RC272's exact four-trial responses and degree-128 low residual centers,
but replaces their dominant undifferentiated original-action tail allowance by a
resolved prime/endpoint output through degree 2048. The original P2/P4 or P3/P5
column faults remain fully paid. All new same-parity prime and endpoint cross
terms are kept before squaring. The reference remains RC271's rank-608 physical
projection augmentation; the legacy rank-639 route remains intact.

| Paid quantity, approximately | Even P0 | Odd P1 |
|---|---:|---:|
| Previous added inverse correction | 0.00254074861591 | 0.00281490107852 |
| New added inverse correction | 0.000391192576444 | 0.000226846570231 |
| Correction reduction factor | 6.49 | 12.41 |
| Actual inverse response upper | 0.106367141541 | 0.0338730804557 |
| Native gate lower | -0.00418246829348 | -0.000838377413777 |
| Native gate upper, preserved | 0.00392398083404 | 0.00407833914453 |

Both gate intervals still contain zero. No positive new gate or actual negative
direction is certified. Exact fractions, rather than displayed decimals, determine
these conclusions. The residual correction is now about 2.07 times the fixed-trial
closing allowance even and 1.21 times it odd, compared with RC272's factors 13.42
and 14.96. These ratios describe these trial/error budgets only.

## Exact input combination and preserved low output

For source P_b and RC272's exact trial coefficients y, write

\[
 Z=y_0P_b+y_1P_{b+2}+y_2P_{b+4}+y_3R_b,
 \qquad A=y_0P_b+y_3R_b.
\]

A is an exact rational polynomial of degree at most 64. RC272's largest error
contributions came from these first and residual-shaped columns. The two small
intermediate-trial columns are left as their complete actual-action error bounds;
their errors are not dropped or assumed independent.

The residual for the unchanged trial and reference is still

\[
 e=D^{-1}P_b-N_PZ,
 \qquad N_P=N_0+\lambda D^{-1}P.
\]

All its low center coefficients through degree 128 and the source-diagonal s
uncertainty are preserved exactly from RC272. The augmentation output is confined
to degree 64. Above degree 128 the explicit new model therefore needs only the
original endpoint and prime terms for A. The polynomial pole model ends at degree
40; the regular polynomial tail and all actual regular/pole approximation faults
are paid separately in the remaining global error budget.

## Complete prime output and a positive captured-energy bound

Use the same seven active prime pairs as the inherited arithmetic certificates.
RC242's exact generic prime routine is applied to A with output cutoff 64. It
defines the 16-digit rational translation/coefficient model, pays its difference
from the actual parameters, and constructs the entire physical output on fifteen
support segments. Its exact piecewise polynomial norm retains every cross-prime
and input term. Direct projection computes the low coefficients through 64 and
an outward upper bound on the omitted physical energy.

For each of the seven positive interior boundaries b, expand the jump polynomial
in Legendre coordinates. Green's identity for the Legendre operator gives the
high-degree coefficient, for n>64 of the matching parity,

\[
 c_n=(2n+1)\sum_{b>0}(1-b^2)
 \left[\left(\sum_d\frac{j_dP_d'(b)}{n(n+1)-d(d+1)}\right)P_n(b)
       -\left(\sum_d\frac{j_dP_d(b)}{n(n+1)-d(d+1)}\right)P_n'(b)\right].
\]

Here j_d are the jump's exact Legendre coefficients. Reflected boundaries give
the matching equal contribution; the sign and normalization are checked by direct
polynomial integration at the first new degree, 66 even or 65 odd. All jump
polynomials are reconstructed exactly. RC253 supplies the analytic Green identity;
RC262's interval recurrence supplies high Legendre boundary values through 2048.

Every high prime coefficient is enclosed on a 10^-60 grid. Lower bounds on
mass(n)*|c_n|^2 are subtracted from the certified physical tail after degree 64.
This gives a positive outward upper bound on the prime model energy after 2048.
The subtraction uses lower captured energy, never upper energy. No sampled
oscillation, prime independence, or disappearance of cross terms is assumed.

The whole fresh prime parameter fault is retained separately. Although low output
uses earlier column centers and high output uses this common model, both are
related to the same actual original operator with their own paid errors.

## Endpoint contribution and the omitted model tail

For n above the input degree, the endpoint numerator is exactly

\[
 h_n=(2n+1)\sum_d\frac{A_d}{n(n+1)-d(d+1)}.
\]

There is no log2 coefficient uncertainty on this tail. For degrees 129 through
2048, h_n is combined with the prime coefficient interval before forming its
squared contribution. The signed cancellation between the two terms is retained.

Above 2048, RC252's signed moment expansion and parity telescoping inequality
give an endpoint D-energy upper E_end. If E_prime is the remaining prime physical
energy and n0 is the first omitted matching degree, a valid D-energy model tail is

\[
 E_{tail}\le
 \left(\sqrt{E_{end}}+
       \sqrt{E_{prime}/(H_{n0}+s_{lo})}\right)^2.
\]

The endpoint bound keeps the first four signed input moments and bounds only the
remaining geometric series absolutely. Its positive bracket and the monotone
harmonic denominator are checked exactly. This is a bound for the endpoint/prime
model tail, not a deletion of the other original components.

## Remaining actual-action faults

The new residual model is the direct sum of the preserved low center, the
resolved high endpoint/prime output, and its infinite model tail. The difference
from the actual residual is paid by a single global D-norm allowance epsilon:

- The complete RC272 original-action faults of the two intermediate native trials.
- The low finite coefficient errors of P_b and R_b.
- Twice their old regular-kernel, prime-parameter and pole-Taylor fault norms,
  conservatively covering the different low and high model blocks.
- Their regular polynomial omitted-output norms after degree 128.
- The fresh common prime model's entire physical parameter fault, converted to
  D energy using the positive lower bound for D.

These allowances are added by the norm triangle with the exact trial coefficient
magnitudes. They need not be independent or orthogonal. The deliberately redundant
global arithmetic payments avoid identifying the old hybrid prime model with the
new common model. Low and high output blocks are orthogonal only for the diagonal
inverse majorant used next.

## Projection-aware inverse payment

For the unchanged reference, reuse RC272's family of valid lower forms

\[
 N_P\succeq d I_D+\kappa D^{-1}P,
 \quad d=a[\gamma-p(1+\theta^{-1})\delta^2],
 \quad\kappa=\lambda-p(1+\theta),\quad a=32125/230953.
\]

The same finite theta grid k/100, k=1,...,99, is evaluated with fresh outward
rounding. The inverse majorant is diagonal. In the resolved output its safe
coefficient weight is

\[
 w_n=\left[d+\frac{\kappa}{H_n+s_{hi}}\mathbf1_{n\in I}\right]^{-1}.
\]

The new physical numerator interval v_n contributes at most
mass(n)*max|v_n|^2*w_n/(H_n+s_lo). Output inside the retained projection receives
its stronger weight; output outside it receives the global weight. The infinite
model tail is entirely outside the projection and contributes E_tail/d.

Let V_low, V_inside, V_outside and V_tail be these four model energy bounds, and
let R_s be the preserved source-diagonal uncertainty bound. Then

\[
 C\ge\langle e,N_P^{-1}e\rangle_D,
 \qquad
 C=\left[\sqrt{V_{low}+V_{inside}+V_{outside}+V_{tail}}
          +\sqrt{R_s}+\sqrt{\epsilon^2/d}\right]^2.
\]

This adds orthogonal degree blocks inside the diagonal majorant, not inside the
actual inverse operator. No commutation of N_P with the projection is assumed.
Every retained numerator interval, infinite tail and global error is paid.

The selected even model energy bound is approximately 0.0003253984, of which
0.0002512515 is resolved output outside the retained projection and 0.0000631731
is the infinite model tail. The selected odd model bound is approximately
0.0001577921, with corresponding contributions 0.0000875062 and 0.0000603686.
The remaining global fault energy allowances are approximately 0.0000030269 even
and 0.0000062495 odd; their square-root cross payments remain in the correction.
Thus further progress can come from the unresolved secondary-native trial tails
or from a stronger inverse estimate outside the retained projection. Increasing
the prime cutoff alone is not asserted to close either gate.

The inverse response center remains RC272's exact interval trial form. Its upper
bound is intersected with the new center-plus-C bound; the new native gate lower
bound is mass(b)-lambda*T_upper. The correction is added to the inverse response,
so reducing it raises the gate lower bound. An individual gate entry, even if
positive, is not the complete same-parity matrix inequality.

## Reproduction and status

```bash
python scripts/validate_rpb108_rc273_projection_original_tail.py \
  --output certificates/rpb108_rc273_projection_original_tail.json
python scripts/validate_rpb108_rc273_projection_original_tail.py \
  --output certificates/rpb108_rc273_projection_original_tail.json --replay
```

All 254 inherited blob pins are verified. Generation uses 1500-digit recurrence
grids and 120-digit static boundary intervals; replay uses 1540 and 140 digits,
reverses dependency and summation traversal, and compares the complete certificate
exactly. Direct high-degree integration and full segment-norm/digest checks are
independent controls on the new prime output. All acceptance uses exact rational
arithmetic. The analytic proof is not formalized in Lean.

The original below-0.01 count ceiling 608, nonpositive ceiling 582, the legacy two
positive signed pivots and the separate eight-source inverse width 485647/1000000
are preserved. Only the two projection auxiliary sources P0/P1 are tested here;
the full 608-source matrix gate remains open. Stage I, global/F4 and RH are not
claimed. Next: use the paid tail split to improve the response trials or extend
the coupled source range, retaining every inverse covariance payment.
