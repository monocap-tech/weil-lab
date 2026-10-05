# RPB108: full 36-source Gram at 14/25 and a certified scalar-bound obstruction

Base: a01bb2b46197b67443cd7f6ff3f90008bea48d3c.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_056_GRAM.md.

## Actual Gram and source custody

The complete actual 36-source residual Gram at a=14/25 is now certified using the previously reproduced source enclosures and independently certified native matrix. It removes exactly the physical degrees 0..35, retains the exact endpoint logarithm, every smooth/smooth and both log/smooth term, every projection product and all five actual prime-2/prime-3 panels. All 1296 source/native pairings pass, with maximum interval difference below 3.148e-33.

The largest surrogate Gram entry width is below 3.042e-114. The surrogate residual-map norm is below 2.377, and the actual Gram operator error delta=eta(2M+eta) is below 1.019e-24. Native and source input hashes are recorded in the certificate. All mixed terms are retained; no approximate parity is imposed on rounded source polynomials.

Polynomial products use the same exact integer denominator-clearing identity as the preceding Gram. The integration dot product is now accumulated exactly as integers before a single outward rounding: moment interval endpoints lie on grid 10^-200, so with common coefficient denominator D each lower/upper sum is an integer divided by D*10^200. Negative coefficients swap the endpoint choices. This encloses the exact rational linear combination and avoids repeated interval rounding and Fraction normalization. Independent comparisons for 12 low/mixed/top-degree source-polynomial smooth/log products are contained in the original interval dot enclosures. The complete new certificate reproduces byte-for-byte.

## The corrected scalar estimate fails

The current complement factor 100/31 yields a certified negative direction of Q_36-(100/31)R_36. Including the Gram error, its quadratic upper bound is below -1.1326e-5 and its Rayleigh upper bound below -7.9302e-6. The same vector has strictly positive raw native energy.

Using the existing unrounded complement lower value above 0.3180393848 gives inverse factor approximately 3.144264665. This estimator also has a certified rational negative direction, with Rayleigh upper bound below -0.0003738. The vector is recorded separately and its raw native energy is again strictly positive. Its certified ratio Q(v)/R(v) is below 2.825486, so any scalar factor that makes the whole estimator positive must be smaller than that value. Equivalently, the scalar physical coercivity would need to exceed 0.35392148. These are necessary conditions on this estimator, not negative full-form witnesses or sufficient conditions for positivity.

The actual corrected form is Q_36-K_36 and satisfies Q_36-K_36>=Q_36-beta R_36 under a lawful inverse bound. The negative lower estimates therefore do not determine its sign. Corrected sign and whole-domain positivity at 14/25 remain open.

## Cutoff-only repair of this family is excluded

This obstruction is not resolved by further tuning the frequency cutoff in the same 36-moment scalar proof. Define its continuous ideal lower-bracket family

F(T)=c(T)-(10+c(T))rho(T)-p-A,
c(T)=log(T)-1/(2T)-S, S=sqrt(2)log(2), A=log(3)/sqrt(3).

On the positive-bound branch rho<1, the rational outward lower evaluations are at most this ideal bracket. If rho>=1, the lawful bracket is nonpositive: for c<0 discard the nonnegative losses, and for c>=0 use c(1-rho)-10rho-p-A<=0. Thus that branch cannot contribute a positive certificate. The pole bound p is independent of T and nonnegative. On the lawful range 10+c(T)>=0 and geometric ratio<1, take T0=763/100.

For T<=T0, monotonicity of c and nonnegativity of the discarded losses give F(T)<=c(T0)-A. Rational intervals enclose this upper symbol below 0.352014802<353/1000.

For T>=T0, write q(T)=[2a(22/7)T]^2/(73*75). The mass majorant obeys rho'(T)/rho(T)=73/T+q'(T)/(1-q(T))>=73/T. Also c'(T)=1/T+1/(2T^2). At T0, c(T0)>0 and the exact rational gap

730 rho(T0)-(1+1/(2T0))

is strictly positive. Both rho and c increase with T. When rho<=1,

F'(T)=c'(T)(1-rho)-(10+c)rho'
     <=[1+1/(2T)-730 rho]/T<0.

When rho>=1, both terms make F'(T)<0 directly. Thus F decreases beyond T0 throughout the admissible geometric range. It follows that every member of this scalar cutoff family is below 353/1000. Cutoffs with c(T)<-10 do not support the low-mass substitution used by this family and cannot supply a positive bound by that substitution.

The family ceiling 0.353 is strictly below the obstruction vector's required scalar coercivity above 0.35392148. Therefore no cutoff adjustment in this family can certify positivity of Q_36-beta R_36 at this aperture. This limits the proof family; it does not bound the true complement coercivity, exclude a stronger prime estimate or preclude a direction-sensitive lawful lift calculation.

## Concrete next projection

The same general moment theorem already certifies an actual 48-moment complement at this aperture. With physical cutoff 10, its unrounded lower bracket exceeds 0.6268, hence physical coercivity 3/5. The independent logarithmic cutoff 7 retains coercivity 9/100. The lawful complement inverse factor is 5/3. This certificate reproduces byte-for-byte.

This complement removes physical degrees 0..47. It cannot be paired with the existing 36-vector matrix or residual Gram. Next: construct the full actual 48-vector native restriction and all 48 actual source enclosures at a=14/25, then integrate their matching residual Gram and decide the corrected form. No independent observation is inferred from multiplicity copies.

## Validation and scope

The full Gram, unrounded-factor obstruction, scalar-family ceiling and 48-moment complement certificates reproduce exactly. All 1296 pairings and actual Gram error bounds pass. Both negative-estimator vectors have positive raw native energy, providing the coupling-omission control. The existing native negative diagonal control remains attached to the unchanged input matrix.

Artifacts: scripts/certify_native_prime3_gram36_056.py, scripts/certify_native_prime3_gram36_056_obstruction.py, scripts/certify_native_prime3_cutoff_family_056.py, scripts/certify_native_prime3_complement48_056.py and the matching notes/data certificates.

Whole-domain sign remains certified at 11/20 with physical margin 1/4000000000. Actual corrected sign at 14/25, global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source and axioms are unchanged; these analytic/rational certificates are not Lean formalized.
