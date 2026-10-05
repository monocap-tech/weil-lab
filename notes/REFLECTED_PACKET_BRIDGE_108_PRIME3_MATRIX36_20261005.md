# RPB108: full 36-vector matrix and source enclosures at the prime-3 aperture

Base: 02101958a186c64661283e5cabe3699d21b9d058.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_MATRIX36.md.

## Concrete extension

At a=11/20, with actual prime powers 2 and 3, the complete native matrix on e_n(x)=sqrt((2n+1)/(2a))P_n(x/a), 0<=n<36, is certified. It includes the previously missing degrees 20..35 and every mixed matrix entry. Its raw physical restriction satisfies

Q(e,e) > (1/32000000)||e||_2^2 for every nonzero e in E_36.

There are also certified five-panel polynomial enclosures of all 36 actual interior sources, with the exact endpoint logarithm retained. Their combined physical L2 source-map error is less than 6.49e-26, including coefficient rounding. These are the inputs for the full 36-source residual Gram; that Gram and the lift-corrected sign are not certified by this turn.

## Exact correlation arithmetic

The native physical correlation identity is unchanged. Let D_p and D_q clear the denominators of p and q, and let D clear every integration denominator 1..deg(p)+deg(q)+1. The summand formerly written as a Fraction c_i c_j binom(j,k)(-1)^k/(i+j-k+1) is evaluated as the integer

(D_p c_i)(D_q c_j) binom(j,k)(-1)^k D/(i+j-k+1).

Both endpoint contributions are accumulated as integers, then divided by D_p D_q D once per output coefficient. This avoids repeated Fraction normalization in the inner correlation loops. It is algebraically the same formula; zero coefficients are skipped without changing it. Independent comparisons with the older Fraction implementation pass for low, mixed, and top degrees through 35.

For even total degree, reflection identifies the two directed physical correlations, as in the earlier twenty-vector proof. For odd total degree, the mixed entries are exactly zero. Every prime correlation uses its actual shift log(n)/(2a), and the physical normalization includes the denominator 2a. No half-aperture matrix is substituted.

## Matrix enclosure and finite sign

The degree-35 constructor is enabled only for a=11/20 and matrix-return mode. The existing smaller-degree constructors retain their parameters. The larger degree uses exponential order 120, 100 Bernoulli pairs, gamma order 12 at n=100, and outward arithmetic grid 10^-200. Square roots are enclosed on that same precision grid in this constructor; the older square-root constructor is restored afterward.

The original analytic remainder proof is evaluated with these higher orders. At L=4a=11/5, the exponential remainder multiplier is 10 and the kernel multiplier is 3, with the same rational bounds already checked for prime-3 activation. The Bernoulli remainder factor L/6 is below one. Correlation coefficient sums, both exponential errors, kernel errors and all constants are retained entrywise.

All 36 raw and shifted rational interval elimination pivots are strictly positive after subtracting (1/32000000)I. The maximum native entry enclosure width is below 1.097e-47. Replacing the first diagonal by -1 is rejected. Every odd mixed entry is exactly zero. All 400 matrix intervals in the first-twenty shared block lie inside the previously certified twenty-vector intervals. These finite pivots are not eigenvalues or lift-corrected pivots.

## Full source construction and rounding custody

The scaled actual-source construction is extended to p_n(t)=P_n(2t-1) for every n<=35, using d=2a=11/10 and t=(x+a)/d. It retains A_d(s)=(1/2)B(2ds)exp(-ds/2), both regular difference integrals, endpoint H terms, the constant -gamma-log(2pi)-log(d), both actual pole moments with their physical measure factor, and all active prime-2 and prime-3 translates on the five exact panels. The physical source normalization remains sqrt((2n+1)/d).

The analytic bounds use |P_n|<=1 and the physical-coordinate polynomial derivative bound n(n+1) in the unit coordinate, exactly as in the previous source theorem. Exponential order 60 and 32 Bernoulli pairs retain the proved kernel remainder formula. Gamma order is raised to 20, and intermediate arithmetic and square roots use grid 10^-200, to control high-degree coefficient cancellation. The higher-order gamma enclosure uses the same Euler--Maclaurin formula and next-term remainder at n=100. The exact endpoint logarithm is not approximated.

Each midpoint coefficient is rounded downward to a rational with denominator dividing 10^40. The sum of absolute changes is added to that panel's coefficient radius. Since |t^k|<=1 on [0,1], this encloses the entire added polynomial error uniformly, even when coefficients are large. Each row's maximum coefficient radius is updated before its physical normalization, and the source-map error is recomputed from all 36 row errors. The rounded certificate is the one reproduced and saved.

For the first twenty sources, the sum of coefficient differences on every panel is within the sum of the old and new coefficient-radius budgets. This is an error-budget agreement check, not byte identity: the gamma precision and rounding scheme have changed. The entire new 36-source certificate reproduces byte-for-byte.

## Remaining same-vector Gram obligation

The actual 36-moment complement theorem already gives physical coercivity 1/4 and logarithmic coercivity 9/100. Thus the exact lift-corrected form is S_36=Q_36-K_36, with K_36<=4R_36. The new native matrix and source enclosures now cover all 36 directions needed by this theorem.

Next: extend exact endpoint-log moments and projection products through degree 35; integrate every log/log, smooth/smooth and both log/smooth term on the five actual prime panels; check all 1296 source/native pairings; enclose the induced Gram operator error; and decide Q_36-4R_36 or sharpen the actual lift bound if that estimator is inconclusive. The previously certified 400 pairings do not certify the additional rows or the larger projection. No extra observation is obtained merely by increasing a bookkeeping multiplicity count.

Raw matrix positivity and a coercive complement do not decide the full form without the coupling correction. No actual negative vector, weak-null vector, retained witness transport or whole-domain positivity at 11/20 is asserted here. The certified full-domain result through 27/50 remains intact.

## Validation and status

The full native matrix and rounded 36-source certificate reproduce exactly. Integer/Fraction correlation comparisons pass through degree 35; the first-twenty matrix enclosures are nested; source panel differences remain within their coefficient-error budgets; parity and matrix negative control checks pass.

Artifacts: scripts/certify_native_prime3_matrix36.py, scripts/certify_native_prime3_source36.py, the narrowly extended scripts/certify_native_legendre_small_window.py, and notes/data/RPB108_PRIME3_{MATRIX36,SOURCE36}_CERTIFICATE_20261005.json.

The full residual Gram, corrected sign at 11/20, global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged; these new analytic/rational certificates are not Lean formalized.
