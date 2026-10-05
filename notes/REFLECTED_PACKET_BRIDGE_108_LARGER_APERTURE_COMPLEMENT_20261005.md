# RPB108: uniform complement extension to aperture 51/100

Base: 901aa2943328efd9f789101afcb78f7c4ad852f6.

## Definitions and scope

For a in [1/2,51/100], let H_a be the established supported logarithmic form domain, Q_a the actual native Weil form, and F_20(a) the subspace physically orthogonal to the normalized Legendre vectors sqrt((2n+1)/(2a)) P_n(x/a), 0 <= n < 20. The uniform complement estimate means a bound for every f in F_20(a) at every aperture in this interval. It does not identify analyses under dilation or supply a retained witness.

The actual complement satisfies

Q_a(f) >= (2/5)||f||_2^2,
Q_a(f) >= (9/100)||f||_(H_a)^2.

This preserves the inverse factor 5/2 throughout the interval. The new certificate concerns the complement only. Whole-domain positivity at a larger aperture has not been established.

## Prime activation and scaled observations

The established native prime support condition is log(n)<2a for prime powers n. Rational logarithm enclosures show log(2)<1 and 102/100<log(3). Thus only prime 2 contributes on the entire interval; its amplitude S=sqrt(2)log(2)<1 is unchanged.

Physical dilation of the existing plane-wave Legendre identity gives

|fhat(t)|^2 <= 2a ||f||_2^2 sum_(n>=20)(2n+1)|j_n(2pi a t)|^2.

With pi<22/7, y=2a(22/7)T and q=y^2/(41*43)<1, integration before summation gives

integral_[-T,T] |fhat(t)|^2 dt <= rho(a,T)||f||_2^2,
rho(a,T)=4aT y^40/[(41!!)²(1-q)].

The exact successive-term ratio is y^2/(2n+3)^2, bounded by q. All terms are nonnegative, so integration and summation are lawful. The majorant increases with a where q<1, making its value at 51/100 a uniform upper bound.

Moment vanishing removes the degree-19 Taylor polynomials of exp(plus or minus x/2). Since exp(a/2)<2, each pole moment has norm at most sqrt(2a)*2*(a/2)^20/20!. Consequently the absolute pole form is bounded by p(a)||f||_2^2, where p(a)=16a*(a/2)^40/(20!)². This too increases with a.

## Rational coercivity checks

The existing actual symbol bounds m(t)>=log|t|-1/(2|t|)-S for t!=0 and m(t)>-10 hold unchanged because the active prime set is unchanged. At T=91/20 let c=log(T)-1/(2T)-S. Then

Q_a(f) >= [c-(10+c)rho(51/100,T)-p(51/100)]||f||_2^2.

The rational lower bound is approximately 0.4018792287885, strictly greater than 2/5. This is a uniform bound, not a sample of apertures.

For the logarithmic norm w(t)=log(e+|t|), retain the established high-band inequality m(t)>=w(t)/10 for |t|>=4, using S<1, log(2)>2/3 and e<3. On the low band w<2. Since ||f||_2<=||f||_(H_a),

Q_a(f) >= [1/10-(51/5)rho(51/100,4)-p(51/100)]||f||_(H_a)^2.

The rational lower bound is approximately 0.0998886236007, strictly greater than 9/100. This supplies the same lawful form-domain lift construction at each aperture. No physical spectral operator-domain membership is assumed.

## Remaining finite task

For each aperture the exact corrected form is S_20(a)=Q_20(a)-K_20(a), with K_20(a)<= (5/2)R_20(a). The physical basis, pole moments, prime translation locations, native matrix and full residual Gram all depend on a. The certificate at a=1/2 cannot be reused as their enclosure at 51/100.

Next: construct Q_20(a) and R_20(a) with the normalized same-vector basis at a specified larger aperture, retain all mixed terms and operator errors, and certify the corrected form before claiming whole-domain positivity there. Alternatively an independent global endpoint argument remains admissible. This turn supplies no quantitative extension of the full-domain positive aperture.

## Validation and status

scripts/certify_native_larger_aperture_complement.py uses exact Fraction arithmetic and the existing outward rational transcendental enclosures. Its JSON reproduces exactly. It verifies prime activation, pi and exponential bounds, both coercivity margins, and rejection of an invalid geometric-ratio control. The control is an arithmetic-domain check, not a negative matrix sign test. The analytic scaling and monotonicity arguments are given above.

The half-aperture whole-domain result at 901aa29 remains the promoted checkpoint. Larger-aperture full Schur sign, global endpoint exclusion, all-window unit domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged; this extension is not Lean formalized.
