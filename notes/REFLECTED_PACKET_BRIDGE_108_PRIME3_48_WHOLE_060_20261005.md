# RPB108: actual whole-domain sign at aperture a=3/5

Base: e2f3a9199ceaa0175f9521b86c1f2de9dc092331.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_48_WHOLE_060.md.

## Result

On the actual canonical supported logarithmic form domain at a=3/5,

Q(h) >= (1/94720000000) ||h||_2^2.

The form includes actual prime powers 2 and 3 and both pole terms. This excludes fixed-aperture weak null modes and supplies the corresponding full-source WD-T10 unit domination. No global endpoint exclusion or retained witness/null transport is inferred.

## New aperture and analytic remainder bounds

The degree-47 native matrix and source constructors are explicitly enabled at a=3/5; smaller supported degrees are not enabled at this new aperture. Old supported apertures retain their existing arithmetic. No matrix or source enclosure from a=14/25 is substituted under dilation.

Here L=4a=12/5 exceeds the former convenient bound 9/4. Rational logarithms prove L<log(12) and L>log(5). Therefore exp(L)<12, providing the new exponential remainder multiplier. Also exp(-L)<1/5, so

L/(1-exp(-L)) < (12/5)/(4/5)=3.

The function z/(1-exp(-z)) is increasing for z>=0: its derivative has positive numerator exp(z)-1-z. Thus the bound 3 holds on the entire kernel expansion interval 0<=z<=L. This preserves the proved Bernoulli remainder formula and multiplier 3. The native finite computation uses exponential order 160, 120 Bernoulli pairs, gamma order 12 and outward grid 10^-200. Both actual primes satisfy log(3)<2a<log(4), so only prime powers 2 and 3 are active.

The source constructor re-evaluates the same kernel bound at 2d=12/5, with d=6/5. The source exponential remainder coefficient 3/2 is half the kernel bound; the negative exponential Taylor remainder retains its original power/factorial estimate. Its pole exponential bound remains valid since d/2=a<log(2). The source exponential order is 60, and the number of Bernoulli pairs is increased from 32 to 40 at this aperture only. Thus the kernel remainder uses 4(d/3)^82/[1-(d/3)^2], with d/3=2/5. Gamma order remains 20 and all coefficient-rounding errors are retained.

The exact integer correlation/product evaluation, beta-integral regular factors, cached-power composition and once-rounded interval dots from the previous dimension extension are reused. All 6768 regular factors for j=0..47 and k=0..140 agree exactly with the original binomial sums through the enlarged source expansion.

## Complete native matrix and sources

All 48 actual native and shifted pivots pass, with raw physical margin 1/1024000000. Every mixed entry is included, and odd mixed entries vanish exactly by reflection. The native negative diagonal control is rejected. The actual physical normalization is sqrt((2n+1)/(2a)). The full native matrix reproduces byte-for-byte.

All 48 interior sources retain the exact endpoint logarithm, both regular-difference terms, both pole moments and the actual prime translations on the five exact panels with cuts 0,1-log(3)/d,1-log(2)/d,log(2)/d,log(3)/d,1. Midpoint polynomial coefficients are rounded to denominator dividing 10^40, with total absolute changes added to each panel's error budget. The combined actual physical L2 source-map error is below 1.715e-29. The rounded source certificate reproduces exactly.

## Matching lawful complement

For k=48 at upper aperture 3/5, physical cutoff T=933/100 gives the existing integrated-mass majorant rho=4a T[2a(22/7)T]^96/[(97!!)^2(1-q)], with q=[2a(22/7)T]^2/(97*99)<1. This dominates the smaller-aperture mass bounds by monotonicity. The 48-moment pole loss is p=16a(a/2)^96/(48!)^2.

With S=sqrt(2)log(2), A=log(3)/sqrt(3), and c(T)=log(T)-1/(2T)-S, the actual physical lower bracket c(T)-(10+c(T))rho-p-A exceeds 0.5543164247. Hence physical coercivity 11/20 is certified uniformly through a=3/5. The compressed prime-3 adjacency norm remains at most one because a<log(3).

The independent logarithmic frequency split retains cutoff 7 and coercivity 9/100. This preserves the lawful complement lift on the same logarithmic form domain. The physical inverse factor is 20/11. The complete complement certificate reproduces exactly.

## Full Gram and corrected sign

The full residual Gram removes exactly the physical degrees 0..47. It retains all log/log, smooth/smooth, both log/smooth and projection products on every actual prime panel. All 2304 source/native pairings pass, with maximum interval difference below 4.163e-38. The maximum Gram entry width is below 8.726e-109, and the actual Gram operator error delta=eta(2M+eta) is below 1.002e-28. Native/source input hashes are recorded. The full Gram and whole-domain certificate reproduces byte-for-byte.

The lawful correction satisfies K_48<=(20/11)R_48. All 48 rational interval pivots of

Q_48-(20/11)Rhat_48-[(20/11)delta+1/1280000000]I

are positive. Thus the actual corrected form has physical lower margin tau=1/1280000000. Replacing the first corrected diagonal by -1 is rejected. No spectral operator-domain membership is assumed.

## Whole-domain assembly

The actual residual-map norm squared is bounded by trace(Rhat_48) upper+delta. Multiplying this by (20/11)^2 bounds the lawful physical lift squared norm by a value below 28.203<36. Use integer lift norm L_lift=6. For h=e+u with e in E_48 and u in the lawful complement,

Q(h)>=tau||e||_2^2+(11/20)||u+lift(e)||_2^2,

while ||h||_2^2<=2(1+L_lift^2)||e||_2^2+2||u+lift(e)||_2^2. Therefore

Q(h)>=min(tau/[2(1+L_lift^2)],11/40)||h||_2^2
     =(1/94720000000)||h||_2^2.

Strict positivity on this same actual supported logarithmic form domain excludes fixed-aperture weak null modes and establishes the corresponding full-source unit-domination consequence.

## Validation and scope

The full native matrix, rounded sources, complement and full Gram/whole-domain certificates reproduce exactly. All native and corrected pivots, exact matrix parity, all 2304 pairings, retained source errors, input hashes, the 6768 regular-factor checks and both negative diagonal controls pass. The new aperture branches preserve earlier supported arithmetic; the validation manifest records the artifacts and scope.

Next: larger apertures with their actual prime panels/complement, or global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged; these analytic/rational certificates are not Lean formalized.
