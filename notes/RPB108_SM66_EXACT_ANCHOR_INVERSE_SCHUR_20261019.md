# SM66 — Actual 21D signed Schur using the exact SM64 four-source inverse

October 19, 2026. Canonical W-ODD-NEG remains OPEN. Stacked on SM65 draft PR #252.

## The new verified prerequisite

SM64 focused Actions 39323057878 PASSED. The original signed physical odd form is strictly positive on the original source plane P=(g1,g2,g17,g22), with four exact positive Sylvester minors approximately 0.510771828331, 0.549326416966, 0.793717093530, 0.015689275128. Along with independently certified full original 25-source physical Gram SPD, this establishes the ACTUAL finite source25 negative index at most 21, conditional on original Fourier/form-domain identities. It does not classify the infinite odd operator.

The exact SM64 whole-signed 4x4 physical anchor lower is pinned from passing Actions artifact 12222433495 via canonical SHA256 a597efeaddbf690c82a8a1274fc4ba3e15d6a31eb3594db502e7f8c15544ce42. The validator checks all four exact positive LDL pivots and every entry of the exact rational inverse identity A64*A64_inverse=I4. No source3/4 block splicing is allowed.

## Complete source25 enclosure and all 84 true crosses

SM66 first REPLAYS the entire true source25 SM65 analytic computation, including both SM58 full 625-entry source hashes, the independently verified SM62 625-entry original signed full25 lower (including 338 disjoint extra signed-positive windows with kappa-excess accounting), the physical exceptional sinh pole, and the independent SM41/SM42 whole-frequency original analytic upper with the genuine infinite tail. Thus it re-establishes the true Loewner inequalities L62 <= Qactual <= U.

With E=U-L62 and F=Q-L62, 0<=F<=E. Therefore every one of the 4*21 original physically supported positive-anchor-to-complement cross entries satisfies

    |B_ij| <= b_ij = |L62_ij| + sqrt_up(E_ii E_jj).

The cross indices are original P=(1,2,17,22) and R=all other 21 SI10 original physical sources. No orthogonality of the original coordinate source vectors is assumed; Schur congruence is algebraic in this independent original physical source basis.

## Full exact positive 4x4 inverse and 21D Schur domination

Since the ACTUAL positive signed anchor A=Q_PP satisfies A>=A64>0, inverse Loewner order gives A_inverse<=A64_inverse. SM66 computes the FULL exact rational inverse including all 16 entries, not a scalar Gershgorin replacement.

For all real complement z, use absolute mixed-source bounds and exact symmetric nonnegative row-weighted Cauchy:

    z' B' A_inverse B z
      <= sum_(i,l) |(A64_inverse)_il|
                    (sum_j b_ij |z_j|)(sum_k b_lk |z_k|)
      <= sum_j d_j z_j^2,

    d_j = ceil_1e-12( sum_(i,l) b_ij |(A64_inverse)_il| sum_k b_lk ).

The second inequality follows from 2|z_j z_k|<=z_j^2+z_k^2 and symmetry of the nonnegative source-weight coupling matrix.

Consequently the ACTUAL source-restricted signed 21D Schur satisfies

    Sactual_21 = Q_RR - B' A_inverse B
               >= L62[R,R] - diag(d_1,...,d_21).

Every diagonal penalty is rounded UP before entering the entire 21x21 rational matrix. The compact exported matrix additionally subtracts its full max-absolute-row-sum rounding fee.

An independently valid SAME-four-anchor scalar comparator uses ell=min_i(A64_ii-sum_jneqi|A64_ij|)>0. It gives

    d_ell_j=ceil_1e-12( sum_i b_ij sum_k b_ik /ell).

These two upper diagonals are compared entry by entry. A smaller total trace is NOT proof of diagonal Loewner dominance; exact coordinatewise inequality is explicitly tested. Both 21D signed Schur LOWER references and the bare signed 21-coordinate compression receive exact rational inertia diagnostics.

## Strict scope

SM66 can improve the quantitative actual signed Schur bound, but negative eigenvalues of any Schur LOWER reference do NOT establish negative actual operator directions or exact actual negative index. The verified actual finite 25-source negative-index ceiling is 21 from SM64; actual 21D Schur PSD/inertia are separately OPEN.

The complete original 470-source Astar inverse and strong infinite orthogonal remainder, W-ODD-NEG O1/O2, even positivity, signed Weil positivity, CC27, RH and independent Fourier/form-domain analytic audit remain OPEN. SM66 focused Actions must pass all complete source and inverse/cross/21D gates before accepting a numerical certificate.
