# RC75: weighted prime transfer and the physical tail boundary

Date: 2026-10-11. Route: RPB108 consolidation. Status: PASS.

RC75 certifies a sharper full physical paired-prime operator bound and propagates it through the existing actual rank-38 projection for the existing 22 source inputs. It also certifies noncompactness of the physical prime operator. The latter is not a lower bound for the canonical source residual.

## Exact results

| Quantity | Certified value |
| --- | --- |
| Full paired-prime physical operator norm upper | 5973/2048 = 2.91650390625 |
| Selected positive weight | h(t) = 1 + (3/8)t^2, t = x/(11/10) |
| Rank-38 residual upper relative to actual original 22-input canonical Gram | 6919/4096 = 1.689208984375 |
| Even residual factor; Young parameter | 6919/4096; 3/4 |
| Odd residual factor; Young parameter | 6539/4096; 3/4 |
| RC74 residual factor | 4379/2048 = 2.13818359375 |
| Fractional decrease of the residual upper bound | 1839/8758, approximately 20.99794% |
| Physical finite-rank prime tail norm squared lower | greater than 1.2850856544599 |

The previous complete prime norm upper was approximately 4.103148316338222. The new bound concerns the same full physical operator; it does not assert projection-specific prime norm decay. The source covariance still has 22 inputs, while the actual canonical target projection has rank 38.

## Weighted energy certificate

Let B = 11/10 and let all inputs be zero-extended from [-B,B]. The complete operator is

K_pr u(x) = - sum_n c_n (u(x + log n) + u(x - log n)),

with n in {2,3,4,5,7,8,9} and c_n = log(p)/sqrt(n), where n is a power of p. Write A = -K_pr. The nonnegative symmetric translation kernel permits a weighted energy estimate. For positive h, the pointwise inequality

2 |u(x)u(y)| <= |u(x)|^2 h(y)/h(x) + |u(y)|^2 h(x)/h(y)

and symmetry give |<u,A u>| <= kappa ||u||_2^2 whenever (A h)(x) <= kappa h(x). Since A is bounded and self-adjoint, this proves ||K_pr|| <= kappa in the original physical L2 norm. Introducing h does not replace that norm by a weighted norm.

In scaled coordinates t = x/B, the 14 translations have offsets delta = +/- log(n)/B. Their true support cutoffs partition [-1,1] into 15 segments. On each segment the active translations are constant, and the required inequality is the quadratic polynomial

q(t) = kappa (1+a t^2) - sum_active c_n (1+a(t+delta)^2) >= 0.

The validator uses the certified rational coefficient and logarithm boxes from RC43. It proves strict ordering of all cutoff boxes and expands each segment to contain its true endpoints. For a quadratic C0+C1*t+C2*t^2 on [l,r], the Bernstein controls are

q(l), C0+C1*(l+r)/2+C2*l*r, q(r).

All three controls have nonnegative certified lower endpoints on every expanded segment. Nonnegative Bernstein controls imply nonnegativity throughout the interval. Values at support cutoffs do not affect the L2 operator. Eight rational weight profiles are tested, with exact rational bisection for kappa; the selected profile is a=3/8 and kappa=5973/2048. This is a certified upper bound, not a claim of an optimal norm or optimal weight.

Generation constructs the quadratic coefficients first. Independent replay constructs each shifted weight's Bernstein controls directly and verifies that every saved outward enclosure contains its independently computed interval.

## Transfer to the actual canonical residual

Keep rho=252/257, the actual projection Pi_38 from RC70, the sharp physical Riesz error Gram E_phys from RC67, the nominal trial physical Gram T, and the source approximation operator error delta from RC68. Keep the projected arch bound beta_arch from RC74 and the parity pole bounds beta_pole,p from RC73.

For each parity p, set k_p = beta_arch + 5973/2048 + beta_pole,p. The prime part uses the full physical norm and the canonical-adjoint contraction bound; the arch and pole parts retain their previously certified projection-sensitive estimates. The correlated projected transfer enclosure, divided by rho, is

E = (1+nu) D_k E_phys D_k + (1+1/nu) delta^2 T,

where nu=1/65536 and D_k is the diagonal matrix of parity constants. The validator rounds this matrix outward and proves E_RC74-E positive semidefinite using exact rational arithmetic. Parity orthogonality is retained.

Let W be RC71's nominal physical polynomial-subtraction residual Gram for degree less than 38. For parity-dependent Young parameters t_p, the actual canonical residual is bounded by the outward-rounded matrix

A_res = rho [(1+t_p) W + (1+1/t_p) E].

At RC74's unchanged Young parameters, the entire residual enclosure also improves in Loewner order. A finite exact search then selects t_even=t_odd=3/4. Exact positive-semidefinite comparisons against RC67's actual canonical input Gram lower establish

Gamma_38 <= (6919/4096) M_22.

Replay also verifies the relative comparisons after exact physical-coordinate congruence. The 20.99794% decrease compares certified scalar upper bounds; it is not a measurement of the actual residual's decrease.

## Physical noncompactness and its scope

Set epsilon=1/10000, J=[-epsilon,epsilon], and

u_j(x) = 1_J(x) exp(i*pi*j*x/epsilon) / sqrt(2*epsilon), j=1,2,... .

These inputs form an orthonormal sequence in physical L2 and converge weakly to zero. The certified logarithm boxes prove that only the n=2 and n=3 translations of J remain in [-B,B]. The four output intervals J +/- log(2), J +/- log(3) lie strictly inside the aperture and are pairwise disjoint; all n>=4 output intervals lie outside it. Consequently

||K_pr u_j||_2^2 = 2 c_2^2 + 2 c_3^2

for every j. The exact lower bound stored in the certificate is 2*(coefficient_lower(2)^2+coefficient_lower(3)^2), greater than 1.2850856544599.

For any finite-rank physical orthogonal projection Q, the bounded sequence K_pr u_j is weakly null, hence Q K_pr u_j converges strongly to zero. Thus

||(I-Q) K_pr||^2 >= 2 c_2^2 + 2 c_3^2.

In particular, increasing a finite physical polynomial head cannot make this full physical operator tail norm tend to zero. The certificate proves the interval separation and the numerical lower bound; the orthonormality, weak-convergence, and finite-rank argument are the analytic proof above.

This does not lower-bound (I-Pi_38) i* K_pr: the canonical adjoint i* may suppress high frequencies. It also does not lower-bound prime transfer on the specific Riesz-error inputs. No actual canonical leakage failure or aperture obstruction follows from this physical noncompactness result.

## Validation and provenance

Artifacts:

- scripts/validate_rpb108_rc75_weighted_prime_transfer.py
- certificates/rpb108_rc75_weighted_prime_transfer.json
- notes/RPB108_RC75_WEIGHTED_PRIME_TRANSFER_AND_PHYSICAL_TAIL_BOUNDARY_20261011.md

The input order is RC74, RC73, RC71, RC68, RC67, RC70, RC59, RC43. The JSON records SHA-256 hashes of all eight inputs and checks RC74's inherited seven-input provenance. It records every profile, every segment's outward Bernstein controls, physical tail interval boxes, the complete transfer and residual matrices, and the parity comparison factors.

Generate with the validator's default repository paths. Independently replay with:

`python scripts/validate_rpb108_rc75_weighted_prime_transfer.py --replay certificates/rpb108_rc75_weighted_prime_transfer.json`

Both generation and independent replay passed. Replay reconstructs shifted-weight controls, support geometry, physical tail interval conditions, trial Gram contraction, and exact canonical matrix comparisons. No floating-point diagnostic is an acceptance condition.

## Remaining frontier

The sufficient scalar source budget remains uncertified. RC75 neither proves actual rank-38 scalar-budget failure nor evaluates a 38-input source covariance. It does not establish a larger Weil head floor, whole-aperture positivity, RH, or F4, and it adds no Lean formalization. A further improvement must address the actual canonical projected prime transfer or the specific Riesz-error inputs; the physical noncompactness result alone does not settle either.
