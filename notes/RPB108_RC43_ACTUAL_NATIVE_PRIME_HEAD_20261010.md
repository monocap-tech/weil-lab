# RPB108 RC43 — all active paired prime translations in the native low head

2026-10-10. Parent RC42: `115fab778753d5220dace52f134d88fcf0585fbc`.
Only `research/rpb108-route-consolidation` is written.

## Result

All 36 upper-triangular entries of the complete active-prime contribution
to the first eight actual native Riesz features are rigorously enclosed.
The active set is exactly {2,3,4,5,7,8,9}. Both translation directions and
the actual coefficient Lambda(n)/sqrt(n) are retained for every term.

A finite-chain bound gives

    ||K_prime||_(physical L2) <4.103149,
    ||A_prime||_(canonical D) <4.023321,
    sigma_prime^*sigma_prime <=k_prime^2 M,
    k_prime^2 <16.187109.

The actual low-eight prime head is indefinite: its feature-0 diagonal is
strictly negative, while its feature-1 diagonal is strictly positive.
This is a component result, not a negative vector for the full original
Weil form. The archimedean remainder and complete mixed source covariance
remain open. There is no new aperture positivity.

## Original form, active set, and definitions

The unchanged cap is B=11/10, R=2B=11/5. Physical inclusion i from the
canonical logarithmic carrier satisfies ||i||^2<=rho=252/257. The original
form is pinned to CC27 blob `e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482`.

Let S_ell f(x)=f(x+ell), with zero extension outside (-B,B). Its physical
adjoint is S_-ell. Define the complete active **prime operator** by

    K_prime=-sum_n c_n(S_log(n)+S_-log(n)),
    c_n=Lambda(n)/sqrt(n).

Define its canonical lift A_prime=i^*K_prime i, actual native head
H_prime=R_native^* A_prime R_native, and actual source map
sigma_prime=A_prime R_native. M=R_native^*R_native is the actual native
canonical Gram. These are component definitions; they do not replace the
full A_Q or its full remainder source map.

Directed exponential bounds certify 9<exp(11/5)<10. Prime powers among
integers 2 through 9 give exactly the seven terms above. For n=p^a the
coefficient is log(p)/sqrt(n), including n=4,8,9. It is not log(n)/sqrt(n)
and is not twice log(p)/sqrt(n). The two translations already supply the
two orientations.

## Full physical operator bound through finite chains

For a fixed positive displacement ell, decompose (-B,B) into fibers modulo
ell. On each fiber S_ell+S_-ell is the adjacency matrix of a finite path.
If m ell<R<(m+1)ell, every such path has at most m+1 nodes. The maximal
path norm applies to the entire physical L2 operator through this direct
integral decomposition, not through a finite-dimensional approximation.

Fresh interval and exact matrix checks give

| Prime power n | Base prime | Maximum nodes | Paired-translation norm |
| --- | --- | ---: | --- |
| 2 | 2 | 4 | (1+sqrt(5))/2 |
| 3 | 3 | 3 | sqrt(2) |
| 4 | 2 | 2 | 1 |
| 5 | 5 | 2 | 1 |
| 7 | 7 | 2 | 1 |
| 8 | 2 | 2 | 1 |
| 9 | 3 | 2 | 1 |

For each term, an outward rational a_n is accepted by exact LDL on
a_n I minus the path adjacency matrix. Path bipartite symmetry gives the
matching negative-eigenvalue bound. Shorter paths are compressions, so
the same bound applies. Triangle inequality then gives

    k_phys=sum_n c_n_upper a_n_upper
           =4.10314831633822...,
    k_prime=rho k_phys=4.02332052808261... .

RC21 already introduced this support-chain mechanism, with the coarser
physical rational bound 11029/2640. RC43 reuses that mechanism and refreshes
its coefficients and path constants; its main new result is the actual
low-eight native head attachment. The new physical scalar bound is about
1.8 percent tighter than RC21's. The generic bound using norm 2 for every
paired translation is about 7.075006 physically; finite chains reduce that
generic budget by about 42 percent.
The exact outward fractions are stored in the JSON; decimal displays are
not the acceptance values.

## Polynomial trial head with both orientations

RC39's native trial map V has 32 Legendre rows and eight columns. Convert
each column exactly into a polynomial p_j(t), t=x/B. For ell=log(n),
the positive translated overlap is

    F_ij(ell)=B integral_(-1)^(1-ell/B) p_i(t)p_j(t+ell/B)dt.

The paired original contribution is precisely

    -c_n[F_ij(ell)+F_ji(ell)].

The second overlap is the adjoint orientation after a change of variable.
The generation pass uses directed 220-digit arithmetic to shift the power
basis, integrate its degree-62 product exactly in that coordinate, and
enclose all 20 same-parity trial entries for each prime power. The 16
opposite-parity entries are zero exactly by reflection. Enclosures are
rounded outward to denominator 10^20 before summing all seven terms.

The nearly maximal n=9 displacement is included even though its physical
overlap is narrow. No newly-admitted-shell shortcut, one-direction shift,
quadrature sampling, or diagonal-only source surrogate is used.

## Transfer to the actual native head

RC39 supplies the whole canonical trial error

    (R_native-V)^*(R_native-V)<=beta P_phys,
    beta=91276884027/64250000000000.

Physical error inclusion therefore gives

    ||i(r_j-v_j)||_2^2<=rho beta(P_phys)_jj.

Let T=V^* i^*i V, computed exactly by congruence from RC38's physical
trial Gram. Put e_j=sqrt(rho beta(P_phys)_jj) and v_j=sqrt(T_jj).
Expanding the difference between actual and trial prime pairings gives
the rigorous entry radius

    k_phys(e_i v_j+e_j v_i+e_i e_j).

This pays both linear errors and the quadratic error. Added to the entire
trial interval, it encloses the actual native entry. Representative outward
enclosures are

| Actual prime-head entry | Lower | Upper |
| --- | ---: | ---: |
| (0,0) | -4.581053311341 | -3.303113730745 |
| (1,1) | 0.625532750930 | 1.013755960101 |
| (3,3) | 0.447446450573 | 1.008600421537 |

The first two entries certify component indefiniteness. No full inertia
claim is made. All 36 actual head-entry enclosures are emitted.

A whole-matrix enclosure is also available. RC38 proves T<=t_V P_phys.
For the rational trial-head center Q_trial the exact certificate gives

    -epsilon P_phys <=H_prime-Q_trial<=epsilon P_phys,
    epsilon<0.295248.

The budget includes k_phys[2sqrt(rho beta t_V)+rho beta] and every interval
rounding error. A checked P_phys>=(1/8)I converts a center-entry halfwidth
h into an additional 64h P_phys bound. It is a physical-feature-metric
enclosure; it is not asserted to meet the original canonical head floor.

## Whole actual canonical source bound

Since A_prime is selfadjoint and ||A_prime||<=k_prime,

    -k_prime M<=H_prime<=k_prime M,
    sigma_prime^*sigma_prime<=k_prime^2 M.

These bounds concern the entire actual canonical source map, without
truncating or sampling its output. Its exact Gram is not evaluated. The
bound alone is far too coarse to certify RC22's combined cross-source
condition. Full archimedean/prime/pole cross correlations still matter.

## Independent replay and scope

Run:

    python scripts/validate_rpb108_rc43_native_prime_head.py
    python scripts/validate_rpb108_rc43_native_prime_head.py --replay certificates/rpb108_rc43_native_prime_head.json

The second pass takes rational centers of the 40-digit enclosed log and
coefficient values. It independently translates the two polynomials to
z=t+1 and integrates their product on [0,2-ell/B] using exact rational
moments. Displacement uncertainty is paid through the moving-endpoint
term and the Legendre derivative bound |P_n'|<=n(n+1)/2; coefficient
uncertainty is also paid. Every one of the 140 same-parity packet entries
is independently checked against its interval before the totals and actual
native entry budgets are replayed.

Additional controls verify opposite-parity cancellation with both
orientations, constant-function overlap length R-ell, the complete active
set, both source input hashes, chain inequalities, exact path LDL bounds,
both component signs, whole-source bounds, and the collective head-error
budget. Generation and replay pass. No floating eigensolver supplies an
accepted sign.

The direct-integral chain theorem, Riesz attachment, reflection, and
operator transfer are analytic arguments documented here, not Lean proofs.
Directed Decimal elementary-function assumptions are inherited from RC30.

RC42's actual signed-pole attachment remains unchanged. The original
archimedean remainder, complete arithmetic mixed covariance, full
8600-feature head/projection, original full-head floor, positivity at 1.10,
RH/F4, and Lean closure remain open. Other branches and historical files
are preserved.
