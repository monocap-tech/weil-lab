# RPB108: full actual residual Gram and sharp inverse obstruction

## Definitions and carrier custody

Work at a=1/2 on the actual supported logarithmic form domain H. Let phi_i(x)=sqrt(2i+1)P_i(2x), E_20=span(phi_0,...,phi_19), Pi_20 the physical L2 projection onto E_20, and F_20 its complement inside H. The actual native form is Q. The already certified complement satisfies Q(f)>(1/5)||f||_2^2 and Q(f)>(9/100)||f||_H^2 on nonzero F_20.

The actual interior source q_e represents Q(e,f)=<q_e,f>_2 for e in E_20 and f in H. Define r_e=(I-Pi_20)q_e and its twenty-coordinate Gram R_20. No operator-domain assumption, retained-vector membership, full graph density, zero simplicity or background positivity is used. All source, prime, pole and energy slots retain the same e.

The exact complement lift z_e is the form-domain solution Q(z_e,f)=Q(e,f) on F_20, constructed by its coercive H-Riesz inverse. Set K(e,e')=Q(z_e,z_e') and S_20=Q_20-K. This inverse is not assumed to have a spectral operator-domain attachment.

## Full residual Gram theorem

All twenty source vectors now have a certified projected residual Gram. The surrogate retains the exact endpoint logarithm L(t)=-(log t+log(1-t))/2 and the previously certified rational smooth polynomials on the three exact prime panels. The matrix reconstruction includes the full log Gram, smooth Gram, both log/smooth mixed Grams, and every degree-0..19 projection subtraction.

The maximum surrogate entry width is below 1.58e-52. The actual Gram operator error from the twenty-source approximation is below 7.07e-29, using the enclosed surrogate trace to bound its source-map norm. Source approximation and integration errors are both accounted for. The twenty-by-twenty physical source-pairing discrepancy against the independently enclosed native matrix is below 1.93e-36 and within every individual certified source error.

`scripts/certify_native_twenty_residual_gram.py` and `notes/data/RPB108_TWENTY_RESIDUAL_GRAM_CERTIFICATE_20261005.json` provide the actual construction. Input source/native certificate SHA256 hashes are pinned in the output. The exact log helper now permits the twenty-source, twenty-projection instantiation while preserving its prior default output.

## Exact logarithmic integration

For n=k+1 the primitives are

integral t^k log t dt = t^n(log t/n-1/n^2),
integral t^k log(1-t) dt = [(t^n-1)log(1-t)-sum_(j=1)^n t^j/j]/n.

At t=0 both integrals have primitive limit zero; at t=1 the second primitive has limit -H_n/n. These limits are evaluated directly, avoiding singular logs. Powers, harmonic sums and log bounds give cached interval moments of t^k and t^k L on each panel. Polynomial products are rational before interval dot products against these moments. Intermediate rounding uses a 10^-120 grid; logarithms use 220 atanh-series terms and a rational uniform tail bound after range reduction.

For all sources 0..19, exact endpoint-log moments and projection products are computed by the earlier harmonic-number identities. Physical normalization is explicit. Opposite parity is not discarded from the computed total Gram merely on floating evidence; every mixed term is evaluated and enclosed.

## Certified obstruction to the no-lift estimator

The actual complement coercivity implies K<=5R_20. Consequently the conservative lower estimator is G=Q_20-5R_20, with S_20>=G. The new calculation exhibits an explicit rational physical coefficient vector a, supported on the even degrees, with

G(a,a)/||a||_2^2 < -9.53e-6.

The exact rational vector, quadratic upper bound and Rayleigh upper bound are in the JSON. A rational midpoint LDL calculation only proposes the vector; interval evaluation of its quadratic form plus 5delta||a||^2 proves the strict negative sign for the actual estimator. Floating eigensolvers are not used in this certificate. The same-vector raw Q_20 energy is certified positive.

This is not an actual negative witness of Q or S_20. G is a lower estimator. Its negative direction shows that the factor-5 no-lift estimate is too coarse to establish positivity on all twenty coordinates. Its margin is far larger than the enclosed errors, so refining quadrature or source precision cannot remove this obstruction to that specific estimator.

## Minimal exact inverse-slack theorem

Define D=5R_20-K. Then D>=0 and exactly

S_20=G+D.

For the certified coefficient vector a, let gamma be minus the recorded strictly negative actual-estimator quadratic upper bound. If S_20(a,a)>=0, necessarily

D(a,a)>=gamma>0,
equivalently K(a,a)<=5R_20(a,a)-gamma.

The constant gamma is an explicit positive rational in the output (`required_inverse_slack_lower_bound`). The current uniform coercivity estimate gives only D>=0; it does not provide this positive directional gap. Thus the independent missing information is sharper control of the actual complement inverse on the observed source range. Raw twenty-vector positivity and exact observation/synthesis construction are insufficient by themselves.

The required directional gap exceeds 1.47008e-5 in the recorded normalization. The same-vector raw Q energy is above 0.0002898697. These compare actual energies of the unchanged rational trial vector, not a surrogate negative witness of Q.

The complete remaining sign is still the twelve-coordinate Schur form after eliminating the already positive E_8 block of S_20, six coordinates per parity. No entries of the true complement correction K are replaced by an assumed positivity statement. The negative estimator certificate neither produces a nonzero weak-null witness nor settles the twelve-coordinate sign.

## Concrete next construction

For an explicit linear approximate lift Z:E_20->F_20, retain e as the original coordinate and define g_e=e-Ze. Use this same g_e in Q, poles, primes and its actual source. Let S_Z(e,e')=Q(g_e,g_e') and R_Z be the Gram of (I-Pi_20)q_(g_e). The established coercive residual theorem gives

S_Z-5R_Z <= S_20 <= S_Z.

This provides a route to the missing inverse information without another carrier representation: construct actual finite polynomial lifts in F_20, evaluate their actual mixed matrix, and certify their residual sources. The estimator certificate gives a definite direction where the lift must recover nonzero slack. All original-coordinate custody remains explicit; g_e is not silently relabeled as a retained source witness.

A sharper independently proved physical complement coercivity constant can also improve the factor before constructing larger lifts. The current 1/5 bound is conservative; any better inverse factor must follow from the actual native symbol and source range, not be assumed because a finite matrix would pass with it.

Global endpoint input, F4 and FULL TRANSPORT CLOSED remain open. This is a precise obstruction to the current factor-5 closure method, not a proof of actual negative energy or failure of the canonical carrier.

## Validation and formalization scope

The previous default endpoint-log certificate reproduces unchanged after parameterization. All first-eight new Gram intervals overlap the independently calculated previous degree-20-complement intervals. Interval elimination confirms the full surrogate Gram is positive. All 400 source pairings satisfy their independent native/source enclosures. Numerical certificate data reproduce exactly when inverse-slack metadata are added. Input hashes are verified. Lean source, axioms and previously reported CI claims are unchanged; the new certificate is rational arithmetic and analytic work, not new Lean formalization.
