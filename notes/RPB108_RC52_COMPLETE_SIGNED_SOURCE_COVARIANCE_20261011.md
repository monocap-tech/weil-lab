# RPB108 RC52 — complete signed bounded-remainder source covariance

2026-10-11 UTC (2026-10-10 in Los Angeles).
Parent RC51: `499c52fbad54cb1b0da1b003a7c19502f98e2f93`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

The remaining archimedean–prime physical trial source covariance is
now enclosed. Combining it with RC48–RC51 completes all self and
mixed trial covariances of the archimedean, prime and signed pole
bounded-remainder actions on native features 0 through 7. Paid
approximation and actual Riesz-map transfer certify

    sigma_total^*sigma_total <=3.773930291713645... M_8
                            <(1887/500) M_8.

The previous split triangle bound, combining RC51's archimedean–pole
bound with RC48's prime bound, was 38.57251300352868... M_8. The
complete signed bound is more than 10.22 times smaller. This is an
eight-feature canonical source-Gram upper envelope, not an evaluated
actual canonical source Gram or a projected residual bound.

Six individual actual native directions now have strictly positive
original-Weil diagonal enclosures: **1, 2, 3, 4, 6 and 7**. Exact parity
also strengthens the certified two-feature subspace floor to

    Q(h)>=(1/21)||h||_D^2
    for h in span{actual native representatives r_6,r_7}.

This improves RC50–RC51's 1/25 floor. Positivity on the combined span
of all six directions and the full eight-feature head are not certified.
The full 1250-feature projection and whole-aperture positivity remain
open. Generation and independent reflected logarithmic-moment replay
pass. No RH/F4 or Lean closure follows.

## Definitions and the complete source being bounded

Let R_native be the actual canonical native Riesz map, V the rounded
32-mode trial map, i the physical inclusion, M_8=R_native^*R_native,
and P the physical native feature Gram. Keep B=11/10, R_width=11/5
and y=(x+B)/R_width. Define

    K_total=K_arch+K_prime+K_pole,
    sigma_total=i^* K_total iR_native.

K_arch=L_arch-L_w is RC50's bounded archimedean remainder, with norm
less than 8. K_prime is the negative sum of the fourteen truncated
oriented translations at prime powers 2,3,4,5,7,8,9. K_pole retains
both signs: 2|cosh(x/2)><cosh(x/2)| minus
2|sinh(x/2)><sinh(x/2)|. These actions preserve parity.

The original canonical Weil head is M_8 plus the K_total head. The
canonical identity contribution M_8 is added exactly once in head
assembly; it is not part of the bounded source sigma_total above.
This distinction is also relevant to future projected-source work.

RC50 supplies a nominal logarithmic-polynomial archimedean action

    F_arch,nom,j=A_j(y)+B_j(y)log y+C_j(y)log(1-y),
    ||(K_arch iV-F_arch,nom)a||_2<=delta ||iV a||_2,
    delta<49/200000.

The same paid delta is inherited from RC50 and checked against RC51.
It covers constant uncertainty and both entire metric-kernel and
regular archimedean-kernel truncation. The prime and pole actions are
integrated with directed interval coefficients and support endpoints.

## Archimedean–prime mixed integration

Use t=x/B=2y-1. For each active prime power n=p^k, define
ell_n=log(n)/B and c_n=log(p)/sqrt(n). The physical prime source is

    F_prime,j(t)=-sum_n c_n[
       V_j(t+ell_n) 1_[-1,1-ell_n](t)
       +V_j(t-ell_n) 1_[-1+ell_n,1](t)].

The fourteen interior support knots together with -1 and 1 give the
same fifteen disjoint integration segments as RC48. Their interval
enclosures are strictly ordered, and each segment's active set is
checked. On each segment, F_prime,j is a degree-31 polynomial in y.
Native rounded coefficients are used without substitution by the
feature polynomials or exact Riesz representatives.

Compute every ordered same-parity pairing

    Z_ij=<F_arch,nom,i,F_prime,j>_physical,
    X_arch,prime,ij=Z_ij+Z_ji.

There are 32 ordered same-parity pairings, producing 20 symmetric
same-parity entries. All opposite-parity entries vanish exactly.
Each pairing integrates the archimedean polynomial and both logarithmic
parts against the summed active prime polynomial over all fifteen
segments. No prime term or moving support endpoint is omitted.

For a=k+1, exact primitive families are

    integral y^k dy=y^a/a,
    integral y^k log y dy=y^a(log y/a-1/a^2),
    integral y^k log(1-y)dy
       =[(y^a-1)log(1-y)-sum_(r=1)^a y^r/r]/a.

Their limits at y=0 are zero. At y=1 they are 1/a, -1/a^2 and
-H_a/a respectively. These endpoint limits are supplied exactly;
the validator never evaluates log(0). Interior logarithms, translation
lengths and coefficients use directed 220-digit intervals. Products
have degree at most 255. Mixed endpoints are rounded outward to
rationals at denominator 10^25.

Independent replay uses the global reflection identity

    C_i(y)=(-1)^i B_i(1-y),
    F_prime,j(1-y)=(-1)^j F_prime,j(y).

For equal parity, the full-interval log(1-y) contribution equals the
log y contribution. Replay therefore integrates A_i+2B_i log y
against the same piecewise prime source. This uses two moment families
instead of the generator's three, and every replayed symmetric mixed
entry lies inside its saved rational interval. The source builder and
validated prime-support geometry are inherited explicitly; the new
logarithmic integration identity is independently replayed.

## All six covariance families assembled before transport

The nominal complete source is F_nom=F_arch,nom+F_prime+F_pole. Its
physical Gram is assembled as

    U_nom=U_arch,pole,nom + U_prime
          +X_prime,pole + X_arch,prime.

RC51's U_arch,pole,nom already contains archimedean and pole self
terms plus their mixed term. RC48 supplies prime self-covariance, and
RC49 supplies signed prime–pole covariance. Thus each of the three
self families and three symmetrized mixed families appears once.
This preserves correlations before squaring, rather than summing
component norm allowances. The new mixed diagonals have both signs;
no uniform cancellation or semidefinite mixed-matrix claim is made.

For the head, add RC48's trial prime head to RC51's nominal trial
archimedean–pole remainder head. This is the complete nominal bounded
remainder head, without an additional M_8 term.

## Paid actual transfer and canonical source envelope

Let T be the physical trial Gram, B_err RC47's physical Riesz-error
Gram upper bound, e_j its physical error column allowances, and
rho=252/257. On each parity block, the complete physical operator norm
is bounded by

    k_even=8+k_prime+2||cosh(x/2)||_2^2,
    k_odd=8+k_prime+2||sinh(x/2)||_2^2,

where k_prime is RC43's full paired-prime physical operator bound.
With n_j=sqrt(U_nom,jj_upper) and v_j=sqrt(T_jj), both rounded upward,
the true trial action norm is at most s_j=n_j+delta v_j. The complete
head entry's paid trial-to-actual radius is

    delta sqrt(T_ii T_jj)+e_i s_j+e_j s_i
       +k_(i mod 2)e_i e_j.

Add the actual canonical M_8 enclosure once, then intersect with
RC51's complete original head. This gives the new actual original
head intervals. The actual physical source differs from F_nom by at
most d_j=delta v_j+k_(j mod 2)e_j. Source-Gram entry errors are bounded
by d_i n_j+d_j n_i+d_i d_j. Those saved physical enclosures are distinct
from canonical source entries.

For a whole-map envelope, check P>=I/8. If h is the maximum nominal
Gram entry halfwidth, set

    U_up=center(U_nom)+64h P,
    S=diag(k_(j mod 2)),
    D_err=(33/32) S B_err S+33 delta^2 T.

The fixed Young inequality pays both correlated Riesz-map error and
archimedean source approximation. Exact parity supports the blockwise
operator bound S. For each tested rational t>0,

    sigma_total^*sigma_total
       <=A_t=rho[(1+t)U_up+(1+1/t)D_err].

Exact rational PSD bisection verifies A_t<=lambda_t P. The best of
the six tested t values is 1/2. RC39's M_8>=alpha P, with
alpha=8947777583/17179869184, yields the asserted lambda_t/alpha
allowance. No floating eigenvalue is used in the certificate.

## Original head progress and the evidence boundary

Display endpoints are rounded further outward from the saved rationals.

| Native feature | Actual original Weil diagonal |
|---:|---:|
| 0 | [-0.005228, 0.080970] |
| 1 | [0.017438, 0.061161] |
| 2 | [0.000961, 0.050018] |
| 3 | [0.006304, 0.048622] |
| 4 | [0.006993, 0.047645] |
| 5 | [-0.001108, 0.034632] |
| 6 | [0.040074, 0.075135] |
| 7 | [0.041615, 0.073539] |

Every same-parity complete head interval is more than 1.18 times
narrower than RC51's; the minimum improvement is 1.1832810864....
The validator checks Q_ii_lower>M_ii_upper/21 for i=6,7 exactly.
Both Q_67 and M_67 vanish by parity. Consequently the 1/21 floor holds
for all complex linear combinations of r_6 and r_7. The actual Gram
lower bound ensures these representatives are independent.

The six positive diagonals certify six individual directions. They
do not establish a six-dimensional floor: same-parity couplings and
their uncertainty must also be controlled. Directions 0 and 5 remain
unresolved, and the full head floor is still open.

The complete nominal low-eight bounded source covariance is now
assembled with actual transfer paid. The next obligations concern
projection of this combined source, the resulting canonical residual,
and refinement or expansion of the actual head. The unprojected
3.774 M_8 envelope does not satisfy the much smaller projected-residual
gate by itself. It also supplies no full 1250-feature projection or
whole-aperture positivity certificate. RC44's complement floor and
RC45's conditioning statement are preserved.

## Reproduction

The default input order is RC39, RC43, RC42, RC47, RC46, RC48, RC49,
RC50 and RC51. All input hashes and their shared native, operator and
transport dependencies are checked.

    python scripts/validate_rpb108_rc52_complete_source_covariance.py
    python scripts/validate_rpb108_rc52_complete_source_covariance.py --replay certificates/rpb108_rc52_complete_source_covariance.json

Replay checks the reflected mixed integrals, all six source covariance
families, paid approximation, actual source/head transfer, historical
intersections, the stronger two-feature floor and exact rational PSD
bounds. This numerical certificate is separate from Lean formalization.
