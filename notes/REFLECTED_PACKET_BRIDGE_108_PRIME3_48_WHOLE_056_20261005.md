# RPB108: actual whole-domain sign at a=14/25 with 48 coordinates

Base: 082b252db548fce6976c962545a9a37c1c29f503.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_48_WHOLE_056.md.

## Result

On the actual canonical supported logarithmic form domain at aperture a=14/25,

Q(h) >= (1/2080000000) ||h||_2^2.

The form includes actual prime powers 2 and 3 and both poles. This excludes weak null modes at this aperture and gives corresponding full-source WD-T10 unit domination. It does not identify a retained source witness or establish global endpoint exclusion.

The preceding 36-moment scalar-family ceiling and negative lower-estimator directions remain valid historical certificates. The new result uses an actual larger projection with its matching matrix, sources and residual Gram. No multiplicity-copy count is substituted for independent coordinates.

## Full actual 48-vector restriction

The native matrix constructor admits degree 47 only at a=14/25 and only in matrix-return mode. Its previous supported constructors retain their arithmetic. The larger dimension uses exponential order 160 and 120 Bernoulli pairs, retaining the proved remainder formulas and the same audited constants: L=56/25<9/4, L<log(10), L>log(4), and log(3)<2a<log(4). Gamma order remains 12; intermediate arithmetic and square roots use outward grid 10^-200.

All 48 native and shifted pivots pass with raw physical margin 1/64000000. The matrix entry width is below 1.097e-47. Odd mixed entries vanish exactly by reflection; every other mixed entry is included. Replacing the first diagonal by -1 is rejected. All 1296 first-36 block intervals lie inside the earlier 36-vector matrix enclosures at the same aperture. The full new matrix reproduces exactly.

The native correlation integral is unchanged. Clear input coefficient denominators D_p,D_q and all antiderivative denominators D. Accumulate integer coefficients of the x-antiderivative of p(x)q(x-y). Its upper endpoint x=1 is a row sum, while x=y-1 is evaluated by polynomial Horner. Subtract and divide by D_p D_q D once per output coefficient. The total-degree bound prevents truncation during Horner; this is explicitly checked. Exact comparisons against the previous integer correlation pass for low, mixed and top pairs through degree 47, and low cases also agree with the original Fraction implementation. The top-degree product agrees with the original rational convolution.

## All 48 sources and exact evaluation improvements

The actual five-panel source formula is enabled for degree 47 at this aperture only; its default 36-source behavior is retained. It includes the exact endpoint logarithm, both regular difference integrals, all actual prime translations, both actual pole moments and physical normalization sqrt((2n+1)/(2a)). Exponential order 60, 32 Bernoulli pairs, gamma order 20, outward grid 10^-200 and coefficient rounding grid 10^-40 are retained, with every error budget recomputed through degree 47.

The regular-difference factor sum_{r=1}^j binom(j,r)(-1)^r/(k+r) is evaluated exactly as -H_j when k=0, and as j!(k-1)!/(k+j)!-1/k when k>0. These follow by integrating ((1-t)^j-1)t^(k-1); the k=0 case uses the harmonic-number identity. All 6000 factors for j=0..47 and k=0..124 agree exactly with the original binomial sums.

Polynomial composition caches each shift power using precisely the original multiplication order. This reproduces the same interval endpoints while avoiding repeated power evaluation. Top-degree interval prime translation and high-degree rational reflection agree exactly with the original composition. The saved 36-source certificate at a=11/20 reproduces byte-for-byte after this helper change, and all first-36 rounded source rows at a=14/25 agree byte-for-byte with their existing certificate.

The full 48-source physical map error is below 5.08e-25, including coefficient rounding. Every source enclosure has five actual panels; the endpoint logarithm remains exact. The full new source certificate reproduces exactly.

## Same-projection full residual Gram

Exact endpoint-log moments and projection products are extended to the explicit dimension pair (47,48), while old supported pairs remain available. The full actual residual Gram removes physical degrees 0..47. Every log/log, smooth/smooth, both log/smooth and every projection term is retained on all five actual prime panels. Polynomial products and moment dots use exact integer accumulation with one final outward rounding. No approximate source parity is imposed.

All 2304 source/native pairings pass, with maximum interval difference below 3.148e-33. The maximum Gram entry width is below 1.963e-107. The surrogate residual-map norm M is below 2.633; with source-map error eta, the actual Gram operator error delta=eta(2M+eta) is below 2.675e-24. Source and native input hashes are recorded. The complete Gram certificate reproduces byte-for-byte.

## Corrected sign and lawful whole-domain assembly

The matching 48-moment complement already gives physical coercivity 3/5 and logarithmic coercivity 9/100 at this aperture, so its lawful correction satisfies K_48<=(5/3)R_48. All 48 rational interval pivots of

Q_48-(5/3)Rhat_48-[(5/3)delta+1/40000000]I

are strictly positive. Thus Q_48-K_48>=(1/40000000)I. The negative diagonal control is rejected for this corrected test as well.

The actual residual-map squared norm is at most trace(Rhat_48) upper+delta. Therefore the lawful physical lift squared norm is at most (25/9) times that quantity, below 19.251<25. Use lift norm L=5. For h=e+u with e in E_48 and u in its lawful complement, square completion yields

Q(h)>=tau||e||_2^2+(3/5)||u+lift(e)||_2^2,

while ||h||_2^2<=2(1+L^2)||e||_2^2+2||u+lift(e)||_2^2. Consequently

Q(h)>=min(tau/[2(1+L^2)],3/10)||h||_2^2
     =(1/2080000000)||h||_2^2.

This uses the same supported logarithmic form domain and a lawful form lift; no spectral operator-domain membership is assumed. Strict positivity excludes fixed-aperture weak null modes and yields the same fixed-aperture full-source unit-domination consequence as the earlier sign apertures.

## Validation and scope

The native matrix, rounded sources and full Gram/whole-domain certificate reproduce exactly. Shared-block matrix containment, first-36 source row identity, the previous 36-source regression, exact correlation/product/factor/composition comparisons, all 2304 pairings and both native/corrected negative diagonal controls pass. The validation manifest binds the artifacts by hashes.

Next: a larger aperture with its actual prime panels and lawful complement, or global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and earlier CI claims are unchanged; these analytic/rational certificates are not Lean formalized.
