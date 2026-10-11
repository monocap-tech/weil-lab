# RC76: quartic weighted prime transfer

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC76 replaces RC75's quadratic positive weight with a quartic weight in the same physical weighted Schur estimate. It certifies a smaller complete paired-prime operator norm bound and propagates it through the unchanged actual rank-38 canonical projection for the existing 22 source inputs.

| Quantity | Certified value |
| --- | --- |
| Selected weight, with t=x/(11/10) | h(t)=1+t^2/8+t^4/4 |
| Full paired-prime physical operator norm upper | 11669/4096 = 2.848876953125 |
| RC75 full prime norm upper | 5973/2048 = 2.91650390625 |
| Actual rank-38 residual upper relative to original actual 22-input canonical Gram | 853/512 = 1.666015625 |
| Even factor; Young parameter | 853/512; 3/4 |
| Odd factor; Young parameter | 6441/4096; 3/4 |
| RC75 residual factor | 6919/4096 = 1.689208984375 |
| Fractional decrease of residual upper bound | 95/6919, approximately 1.37303% |

The decrease concerns certified upper bounds. It does not measure a decrease of the actual residual or certify the required scalar source budget.

## Positive weight and exact support geometry

On [-B,B], B=11/10, let

K_pr u(x) = -sum_n c_n [u(x+log n)+u(x-log n)],

with zero extension outside the interval, n in {2,3,4,5,7,8,9}, and c_n=log(p)/sqrt(n) for n a power of p. The positive self-adjoint translation adjacency A=-K_pr obeys the physical L2 weighted energy estimate from RC75: A h <= kappa h implies ||K_pr|| <= kappa. This is a bound in the original physical norm.

For h(t)=1+a*t^2+b*t^4, all tested a,b are nonnegative, so h>=1 globally. The fourteen translation support cutoffs have certified ordered rational boxes and partition [-1,1] into fifteen segments. Each segment is enlarged to include its true endpoints, then split into four exact rational subintervals. All sixty subintervals use the active translation set of their parent segment. The inequality remains polynomial even on the small enlargement outside the true segment; proving it there is stronger than needed.

On a subinterval [l,r], certify

q(t)=kappa h(t)-sum_active c_n h(t+delta_n) >= 0,

where delta_n=+/-log(n)/B. This is a degree-four polynomial. Generation builds its power coefficients C_m and converts them to degree-four Bernstein controls:

B_i = sum_{m=0}^4 C_m sum_j [binom(i,j) binom(4-i,m-j) / binom(4,m)] l^(m-j) r^j.

The inner sum ranges over max(0,m-(4-i)) <= j <= min(i,m). Each control has a certified nonnegative lower endpoint. Since Bernstein basis functions are nonnegative and sum to one, this proves q>=0 throughout the subinterval. Support-cutoff point values are immaterial to the L2 operator.

The coefficient and offset boxes are inherited from RC43; the validator checks that they enclose the independently constructed interval translation geometry. Eight rational profiles are tested, including RC75's quadratic weight. Exact fourteen-step rational bisection in [2,4] yields the stored feasible bounds. No optimality of the profile or of the operator norm is claimed.

## Independent replay

Replay constructs controls directly from shifted endpoint products. Put L=l+delta and R=r+delta. The i-th degree-four control of h(t+delta) is

1 + (a/6) [binom(4-i,2) L^2 + (4-i)i L R + binom(i,2) R^2] + b L^(4-i) R^i.

Replay subtracts the active translated controls from kappa times the unshifted controls. This avoids generation's power-coefficient construction. Every saved outward rational enclosure must contain the independent interval result and have a nonnegative lower endpoint. Generation and replay use directed interval arithmetic; floating-point exploration is not an acceptance condition.

## Actual canonical transfer

Keep rho=252/257, RC74's projected arch bound, RC73's projected parity pole bounds, RC67's sharp physical Riesz-error Gram E_phys and actual canonical input Gram lower, RC68's source approximation error delta, RC71's nominal degree-less-than-38 subtraction residual Gram W, and RC70's actual rank-38 head.

For parity p, let k_p=beta_arch+11669/4096+beta_pole,p. With nu=1/65536, the projected transfer enclosure divided by rho is the outward-rounded matrix

E=(1+nu) D_k E_phys D_k+(1+1/nu) delta^2 T,

where T is the nominal trial physical Gram. Exact rational PSD checks certify E_RC75-E>=0. At RC75's unchanged Young parameters, the entire residual upper also improves in Loewner order. A finite exact parity search again selects t_even=t_odd=3/4, giving

A_res=rho [(1+t_p)W+(1+1/t_p)E].

Exact PSD comparisons against the actual canonical input Gram lower establish Gamma_38 <= (853/512) M_22. Replay independently contracts the trial Gram and verifies the relative comparisons after exact physical-coordinate congruence.

## Provenance, artifacts, and scope

Inputs, in order: RC75, RC74, RC73, RC71, RC68, RC67, RC70, RC59, RC43. SHA-256 hashes bind all nine inputs; RC75's eight-input provenance is checked against the remaining eight hashes.

- scripts/validate_rpb108_rc76_quartic_prime_transfer.py
- certificates/rpb108_rc76_quartic_prime_transfer.json
- notes/RPB108_RC76_QUARTIC_WEIGHTED_PRIME_TRANSFER_20261011.md

The certificate stores all eight profile proofs, sixty subintervals per profile, five control enclosures per subinterval, complete transfer and residual matrices, and parity factors. Default repository input paths support generation. Independent replay uses:

`python scripts/validate_rpb108_rc76_quartic_prime_transfer.py --replay certificates/rpb108_rc76_quartic_prime_transfer.json`

Generation and independent replay passed. RC75's physical noncompactness witness is rechecked and retained, without changing its scope: it does not prove a canonical source obstruction. The prime improvement is a full physical operator bound, not a projection-specific decay estimate.

The existing 22-input covariance is bounded after projection onto the actual 38-feature head. A 38-input source covariance and a larger Weil floor remain unevaluated. No actual rank-38 scalar-budget failure, whole-aperture positivity extension, RH, F4, or Lean formalization is claimed. The modest gain here leaves the main frontier at a sharper actual canonical projected prime transfer or tighter control of the specific Riesz-error inputs.
