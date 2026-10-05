# RPB108: full prime-3 residual Gram and corrected sign at a=11/20

Base: ca71f742199e53c9dbecbb5f9f568df816edd148.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_GRAM36.md.

## Actual source and projection custody

This calculation consumes the independently reproduced 36-vector native matrix and the certified, rounded five-panel source enclosures at a=11/20. Both include actual prime powers 2 and 3, both pole terms, and the physical normalization. The residual projection removes exactly physical degrees 0..35. Input file hashes are recorded in the certificate.

Writing t=(x+a)/(2a), p_i(t)=P_i(2t-1), and L(t)=-(log(t)+log(1-t))/2, the surrogate source is sqrt((2i+1)/(2a))[p_i L+s_i]. The five cuts are 0,1-log(3)/(2a),1-log(2)/(2a),log(2)/(2a),log(3)/(2a),1. Each smooth polynomial is used on its own actual panel.

The exact endpoint-log moments are extended through degree 70 and projection dimension 36. The old supported cases remain available, and the new dimension pair (35,36) is admitted explicitly. Endpoint log/log products use the existing harmonic-number and zeta(2) identity, with zeta(2) enclosed by the Machin pi series. The pure endpoint residual Gram includes the complete 36-vector projection subtraction.

On all five panels, rational power primitives integrate every smooth/smooth term, and exact logarithmic primitives integrate both log/smooth terms. All mixed degrees are retained; only the analytically exact odd pure-log products vanish by reflection. The rounded smooth sources need not have exact parity, so their odd terms are not discarded.

If C_ni=integral p_n s_i and D_ni=integral p_n p_i L, the smooth correction is

Rhat_ij=Rlog_ij+sqrt((2i+1)(2j+1))[integral s_i s_j+integral p_i L s_j+integral p_j L s_i-sum_n(2n+1)(C_ni C_nj+D_ni C_nj+D_nj C_ni)].

Every one of the 1296 source/native pairings sqrt((2i+1)(2j+1))(D_ji+C_ji) is compared against the independent native Q_ij interval. The permitted difference is the certified physical L2 row error, because every physical test vector has norm one. This checks source normalization, poles, prime panels and the larger projection against the same native matrix.

## Exact arithmetic and source errors

The polynomial product identity is evaluated by clearing each input polynomial's coefficient denominators, accumulating the integer convolution, and dividing once per output coefficient. It is the same rational convolution as the original helper; independent checks include mixed rational denominators and long polynomial products. Integration and elimination use outward rational grid 10^-200. No floating value enters a sign decision.

Let eta be the source-map L2 error, including all coefficient rounding. Orthogonal projection is contractive, so the same eta bounds the residual-map error. With M=sqrt(trace Rhat upper), delta=eta(2M+eta) bounds the actual Gram operator error. In particular, ||R||<=trace Rhat upper+delta; this uses the operator norm estimate, not a claim that the trace error is delta.

The uniform 36-moment complement certificate gives physical coercivity 1/4 and logarithmic coercivity 9/100 through this aperture. Its lawful form-domain lift correction therefore satisfies K_36<=4R_36. To certify a corrected margin tau, rational interval elimination is applied to Q_36-4Rhat_36-(4delta+tau)I.

## Whole-domain assembly

If the corrected margin is positive and the actual lift norm is at most L, write f=e+u with e in E_36. Completing the square in the lawful complement form gives Q(f)>=tau||e||^2+(1/4)||u+lift(e)||^2. Also ||f||^2<=2(1+L^2)||e||^2+2||u+lift(e)||^2. Hence the physical whole-domain margin is min(tau/[2(1+L^2)],1/8). The bound L^2<=16(trace Rhat upper+delta) is recorded separately.

This assembly uses the same supported logarithmic form domain and a lawful form lift; no spectral operator-domain premise or retained witness identification is introduced. Strict positivity excludes fixed-aperture weak null modes and supplies the same fixed-aperture unit-domination consequence as the prior aperture results. It does not itself attach the retained WD-T38 source/null data.

## Certified result and obstruction

The full actual 36-source residual Gram is enclosed by the integrated surrogate and the source-error budget. All 1296 native pairings pass, with maximum interval difference below 9.716e-34. The largest Gram entry width is below 3.042e-114; M<2.188 and the actual Gram operator error is below 2.84e-25.

The sufficient estimator Q_36-4R_36 has a certified rational negative direction v recorded in the JSON. Including the Gram error, its quadratic upper bound is below -2.5826e-5 and its Rayleigh upper bound is below -1.5114e-5. The same vector has raw native energy above 2.15299e-4. Dropping the coupling correction therefore rejects this negative-direction check; the raw restriction remains positive.

This is a negative direction of a lower estimator, not a negative direction of Q_36-K_36 or of the full native form. Corrected sign and whole-domain positivity at 11/20 remain open.

Using the existing unrounded physical complement lower bound instead of 1/4 gives inverse factor approximately 3.847444. The same vector still has estimator quadratic upper bound below -1.6630e-5. Rounding the complement constant was therefore not the obstruction. For this vector, a uniform inverse factor must be smaller than the certified ratio Q(v)/R(v), which is less than 3.571570, to make this estimator positive. This necessary condition does not prove that such a uniform factor suffices. A direction-sensitive lawful lift estimate, a stronger complement theorem, or a larger projection is needed.

The complete Gram certificate reproduces byte-for-byte. The source/native pairing checks and the positive raw-energy control use rigorous intervals throughout. Artifacts: scripts/certify_native_prime3_gram36.py, scripts/certify_native_prime3_gram36_obstruction.py, the narrowly extended scripts/certify_native_endpoint_log_gram.py, and notes/data/RPB108_PRIME3_{GRAM36,GRAM36_OBSTRUCTION}_CERTIFICATE_20261005.json.

Next: sharpen the actual lift correction on the near-null finite directions or increase the complement projection; the first open sign aperture remains 11/20, while whole-domain sign stays certified through 27/50.

## Scope

Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged. The new analytic/rational certificate is not Lean formalized.
