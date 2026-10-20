# MG14 — Original full-source affine first and second low-frequency moments

October 19, 2026. Follows verified MG13 PR #262, which certified 24-channel original Fourier first and second moment Loewner brackets on 24 selected frequency cells but had negative lower-reference traces for both moments. Complete original odd/even/Weil/CC27/RH and the independent Fourier/domain analytic audit remain OPEN.

## Mathematical change

The original 25 odd supported SI10 physical source functions are transformed by MG11's EXACT analytic double-boundary coefficients into 23 functions h_i that vanish with their derivatives on the common support boundary, plus the genuine original sinh pole s as channel 24. MG12's physical source Gram and all real pole crosses remain the geometric reference.

MG14 retains MG13's SAME 24 disjoint real source frequency cells in three selected regions. For every cell [m-h/2,m+h/2] and each original source, it calls SM44 true physical Fourier midpoint intervals, SM46 true ORIGINAL source derivative and local second derivative intervals, SM44 analytic source curvature, and SM46 rigorous third-derivative moment upper bounds. In transformed coordinates the true Fourier vector is

  T(xi) = v + d*(xi-m) + e(xi),

where v,d are rational vectors and |e_i(xi)| <= r_i follows from all original source-coefficient and Taylor intervals. No finite differences, FFT samples, or substituted cancellation coefficients enter.

For E²=sum r_i² and A=||v||+h||d||/2, rational square-root uppers give the COMPLETE covariance inequality

  -delta I24 <= TT^t - (v+d*t)(v+d*t)^t <= delta I24,
  delta = 2*A*sqrt(E²)+E².

The EXACT integrated affine reference is C=vv^t+(h²/12)dd^t. All 576 matrix source-cross entries remain, and its mixed linear cross integrates to zero on each centered symmetric cell. SM43's whole-real actual original digamma/seven-prime multiplier bound 0<l<=a_o(xi)<=u, including kink crossings, yields two independent complete-matrix Loewner sandwiches:

  2*h*l*(C-delta I) <= M1cell <= 2*h*u*(C+delta I),
  2*h*l²*(C-delta I) <= M2cell <= 2*h*u²*(C+delta I).

The factor two pays both real Fourier frequency signs. M1 is the original A_o moment, M2 the A_o-squared strong-action moment, NOT Astar-squared with its separate pole terms.

## Controlled MG13 comparison

On precisely the same real frequency panels, construct THREE individually rigorous complete 24×24 Loewner matrix pairs for BOTH first and second moments:

- midpoint: faithful MG13 original midpoint method and complete-source scalar covariance fee, with its verified exact trace replay;
- affine: the MG14 original true source derivative and exactly integrated dd^t Fourier covariance;
- adaptive: on each cell for each moment, select between full-matrix midpoint and affine references by maximizing the exact LOWER TRACE. Selection does not imply one matrix Loewner dominates the other. All chosen full-matrix lower and upper bounds remain valid.

Final full symmetric rational source-matrix export pays an exact row-sum Loewner fee. A negative reference trace is not a negative eigenvector of the true operator. No assumed numerical improvement is built into acceptance.

If the new affine method tightens the chosen-panel references, extend toward certified whole low-band integral plus MG11's tail, physical Gram and Astar pole cross responses. If the source derivative/curvature error remains too large, redesign toward SM46 weighted-source J0,J1,J2 moments and correlated matrix error before increasing trial dimension or panel count.

These 24 selected frequency cells do NOT cover the full [0,Lambda]. No actual Galerkin residual, full470 resolvent, odd/even, Weil/CC27 or RH claim follows.
