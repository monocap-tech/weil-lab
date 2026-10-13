# RC179: finite focus residual direction and complete canonical action

Parent: RC178, `251f9280cecb8f77da488062fd841ce768fedee1`.

RC178 identified a substantial residual on the source mixture f0-P2/6-P0/1200 under its selected least-residual inverse trial. RC179 constructs a paid finite approximation to that residual and evaluates its actual canonical action. The chosen exact degree-256 polynomial now supplies a concrete additional inverse trial direction. The enlarged inverse response and half-Gram gate are not evaluated in this checkpoint.

## 1. Exact finite direction with full residual approximation error

Use S=(P0,P2,f0), M=D^-1 L, L=D+h+R-rI, the selected RC178 coefficient matrix Y, and x=(-1/1200,-1/6,1). Let

\[
 \rho=(S-MS Y)x,\qquad\widehat\rho=(S-VY)x.
\]

The exact finite polynomial q has rational coefficients obtained by outward enclosure and midpoint selection for every even coefficient of rho_hat through degree M_input=256. Each retained coefficient enclosure pays the actual s uncertainty. Once selected, q has fixed rational coefficients; its own canonical action has no uncertain-input error.

The nominal-to-q D error is bounded by the square root of three energies: retained coefficient rounding, omitted finite output coefficients through degree 4094, and RC178's complete analytic residual-tail Gram evaluated on x. These three supports are disjoint. RC178's correlated nominal-to-actual residual error is then added by the triangle inequality. It is not declared orthogonal to any coefficient error.

| Quantity | Certified bound |
|---|---:|
| Nominal residual to q, D norm | <0.003360265705 |
| Actual residual to q, D norm | <0.003858981125 |
| Actual residual to q, relative D norm | <0.1 |
| Exact q D-energy | approximately 0.00174630242190 |

The relative approximation bound divides the paid error by RC178's certified actual residual norm lower, greater than 0.0414247834. The certificate retains all individual omitted energies; the cut at 256 is an approximation choice, not a coverage claim.

## 2. Actual regular action on the signed finite polynomial

RC176's analytic spatial kernel/Beta-convolution/log-moment construction is applied to the exact signed even polynomial q. Its degree is 256, the regular kernel series is cut at 192, the analytic polynomial-plus-log source has maximum power 449, and the regular output polynomial is projected through degree 768.

The kernel constants are fixed rational centers; their replacement errors are paid globally before the cancelling monomial arithmetic. Directed 360-digit operations handle the finite polynomial convolution and closed Legendre moments. The coefficient-center digest of the complete analytic source is recorded; the generator reconstructs it exactly on replay. The actionable D^-1 regular polynomial and every endpoint-log tail contribution are stored.

There is no regular input truncation in this step: the input is the exact q. The separate rho-to-q approximation enters only when transferring this action to the actual focus residual.

The physical source error is the kernel-parameter error plus the all-range kernel series remainder and coefficient rounding. It transfers to D^-1 norm by division by sqrt(s_lower). Above degree 768, the polynomial part of the represented source vanishes, and all remaining log moments are bounded by RC176's full infinite-series formula. Large-coefficient tail square roots use a 10^-300 grid. Low coefficient rounding and represented output tail energies add on disjoint supports; the whole-function kernel error is then added by the triangle inequality.

\[
 \|D^{-1}Rq-\widehat p_R\|_D<5.512\times10^{-9}.
\]

The stored certificate supplies all rational constants and output coefficients behind this bound.

## 3. Full signed endpoint action and negative-r correction

For the same-parity Legendre multiplication matrix of h,

\[
 h_{nm}=\frac{2n+1}{|n-m|(n+m+1)}\quad(n\ne m),
\]

\[
 h_{nn}=2H_{2n}-2H_n+\frac1{2n+1}-\log2.
\]

Every coefficient of D^-1 hq is evaluated by directed signed sums through degree O=4094. Negative input coefficients are retained; no positivity of q is assumed. For n>O, with z_n=n(n+1) and A=sum_m |q_m|,

\[
 |(D^{-1}hq)_n|\le
 \frac{\eta_n A}{1-M_{input}(M_{input}+1)/z_{first}},
 \quad\eta_n=\frac{2n+1}{z_n(H_n+s)},
 \quad z_{first}=(O+2)(O+3).
\]

RC177's full eta D-energy tail T therefore gives the endpoint tail norm at most sqrt(T) A/(1-rho_input). The finite coefficient errors and infinite endpoint tail have disjoint support and their energies add.

The finite -r D^-1 q correction is evaluated with the actual s enclosure through degree 256. Its coefficient error is paid separately.

## 4. Complete actual canonical action and residual transfer

The actionable finite canonical trial is

\[
 \widehat v_q=q+\widehat p_{D^{-1}hq}
                +\widehat p_{-rD^{-1}q}
                +\widehat p_{D^{-1}Rq}.
\]

It has maximum degree 4094 and is specified by the exact q and the three stored polynomial components. Every omitted action tail is paid. Errors in the endpoint, negative-r, and regular components may overlap, so their norm bounds are added by the triangle inequality.

| Quantity | Certified upper bound |
|---|---:|
| Endpoint action error on q, full D norm | 0.000043646288 |
| Regular action error on q, full D norm | 0.000000005512 |
| Complete actual canonical action error on q | 0.000043651799 |
| Transferred canonical action error on actual rho | 0.007761614048 |

The last bound uses the actual global canonical norm ||M||_D<=2:

\[
 \|M\rho-\widehat v_q\|_D
 \le2\|\rho-q\|_D+\|Mq-\widehat v_q\|_D.
\]

The complete action error on the chosen exact q is much smaller than this transferred bound. Enriching the inverse trial space uses q itself and the smaller q-action error; it does not need to identify q with rho.

As an independent structural control, the actual canonical pairing satisfies

\[
 0.0007613999678 < (q,Lq) < 0.0007650482790,
\]

and the adverse interval endpoints verify a||q||_D^2 <= (q,Lq) <=2||q||_D^2, with a=32125/230953. This check includes the full q-action error and actual D constant.

## 5. Replay and next cursor

All eleven input certificates are hashed and cross-linked. Native w14 is reconstructed with its historical coefficient digest. Generation/replay reverse carrier reconstruction, focus-prefix accumulation, regular kernel convolution, and signed endpoint summation. The entire new certificate must match exactly, including the analytic regular-source digest.

```bash
python scripts/validate_rpb108_rc179_focus_residual_canonical_action.py \
  --replay --output certificates/rpb108_rc179_focus_residual_canonical_action.json \
  certificates/rpb108_rc178_three_source_canonical_inverse.json \
  certificates/rpb108_rc177_three_source_canonical_action_gram.json \
  certificates/rpb108_rc176_f0_regular_output_carrier.json \
  certificates/rpb108_rc172_quadratic_regular_action.json \
  certificates/rpb108_rc171_regular_legendre_projection.json \
  certificates/rpb108_rc129_four_vector_joint_moment.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc127_enriched_even_endpoint_action.json \
  certificates/rpb108_rc121_diagonal_metric_equivalence.json \
  certificates/rpb108_rc175_f0_regular_physical_source.json \
  certificates/rpb108_rc170_poisson_regular_action.json
```

Next: add q to the inverse trial space, certify the correlated mixed source/action Gram rows, and recompute the actual three-source inverse residual enclosure. RC179 does not claim that the enlarged space passes the half-Gram gate. RC178's failed enclosure and RC173's earlier two-source pass remain unchanged.

The native seven-source frame is unchanged. Stage I, the full seven-source canonical inverse, the original augmented Weil floor and auxiliary response bound, whole-aperture original positivity, RH, F4, and Lean remain open/unclaimed.
