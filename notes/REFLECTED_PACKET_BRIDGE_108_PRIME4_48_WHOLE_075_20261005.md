# RPB108: actual 48-coordinate whole-domain sign at aperture 3/4

Base: 8529fd2a94b4a7eb815e468d4fe9f20aeb402401.
Definitions: docs/TERMINOLOGY_RPB108_PRIME4_48_WHOLE_075.md.

## Result

On the entire actual canonical supported logarithmic form domain at a=3/4,

Q(h)>=(1/2600000000000000000)||h||_2^2.

The full 48-coordinate restriction and source Gram suffice after a sharper archimedean estimate and retention of the certified low-frequency floor. Failed sufficient estimates are retained as scoped diagnostic certificates. This excludes fixed-aperture weak null modes and establishes corresponding full-source WD-T10 unit domination. Global endpoint exclusion and F4 remain open.

## Actual prime threshold and native matrix

Rational intervals certify log(4)<2a=3/2<log(5). Thus prime powers 2, 3 and 4 are active. The actual coefficient is Lambda(4)=log(2), not log(4). The native prime contribution for 4 is -2Lambda(4)/sqrt(4) times its physical correlation. The full matrix is freshly evaluated at this aperture with both pole terms and physical normalization sqrt((2n+1)/(2a)).

Here L=4a=3. Rational bounds log(4)<L<log(21) prove exp(L)<21 and exp(-L)<1/4. Hence L/(1-exp(-L))<3/(3/4)=4. Monotonicity of z/(1-exp(-z)) supplies kernel multiplier 4 throughout [0,L]. Native exponential order 160, 120 Bernoulli pairs, gamma order 12 and outward grid 10^-200 are retained. The new aperture is enabled only for degree 47. All 48 native and shifted pivots pass with raw physical margin 1/268435456000000. Exact reflection parity and the native negative diagonal control pass.

## Seven actual source panels

The normalized source constructor keeps the exact endpoint logarithm, both regular-difference terms, both pole moments and all actual prime translations. Its exact panels are:

| t interval | Active source translations |
| --- | --- |
| (0,1-ell_4) | +2,+3,+4 |
| (1-ell_4,1-ell_3) | +2,+3 |
| (1-ell_3,ell_2) | +2 |
| (ell_2,1-ell_2) | +2,-2 |
| (1-ell_2,ell_3) | -2 |
| (ell_3,ell_4) | -2,-3 |
| (ell_4,1) | -2,-3,-4 |

The central overlap is required because ell_2<1/2 after this threshold. Panel endpoints are exact logarithmic expressions; endpoint values do not affect the L2 source map. The source coefficient for either prime-4 translation is -log(2)/2. Panel-order and activation controls pass.

Source exponential order remains 60; Bernoulli pairs increase to 48 at this new aperture. The kernel remainder is 4(d/3)^98/[1-(d/3)^2]. The source exponential remainder coefficient 2 is half the new kernel bound. The pole exponent is (d/2)(t-1/2), whose absolute argument is at most d/4=3/8<log(2); this proves the existing Taylor remainder multiplier 2 directly even though d/2 now exceeds log(2). Older aperture guards and arithmetic are retained. Gamma order is 20; all midpoint polynomial rounding at grid 10^-40 is included in the source error. The actual source-map error is below 2.172e-26. All 7536 regular-factor identities for j=0..47 and k=0..156 agree with the original binomial sums.

On the normalized constant coordinate, omitting prime 4 changes the native/source pairing by log(2)(1-log(4)/d)>0.0525. Using log(4)/2 instead of log(2)/2 produces the same excess magnitude. Both exceed twice the certified constant-row source error and are rejected by the independent coefficient controls.

## Joint prime-2/prime-4 complement bound

Let s=log(2), A2=log(2)/sqrt(2), A4=log(2)/2. Since 2s<2a<3s, the longest supported translation fibres have three points. On each such fibre A2 C_s+A4 C_2s is the weighted matrix

[[0,A2,A4],[A2,0,A2],[A4,A2,0]].

Its antisymmetric eigenvalue is -A4; its symmetric eigenvalues solve lambda^2-A4 lambda-2A2^2=0. The largest eigenvalue and operator norm are J24=(A4+sqrt(A4^2+8A2^2))/2, below 0.887767. On two-point fibres the norm is A2<J24; one-point fibres contribute zero. Below prime-4 activation, C_2s vanishes and the same J24 remains a conservative bound. Thus this is uniform for a in [1/2,3/4]. Prime 3 separately has compressed norm at most one because a<log(3), giving total prime loss A=J24+log(3)/sqrt(3). Bounding the two related prime powers jointly avoids the larger separate-norm penalty; neither term is omitted.

For k=48 and physical cutoff T=373/50, the existing integrated-Bessel mass bound is

rho=4a T[2a(22/7)T]^96/[(97!!)^2(1-q)], q=[2a(22/7)T]^2/(97*99)<1.

The pole loss is p=16a(a/2)^96/(48!)^2. Both majorants increase with a on this range. Using the pure archimedean floor -10 and high-frequency bound c=log(T)-1/(2T), independently proved in notes/REFLECTED_PACKET_BRIDGE_108_PRIME3_48_WHOLE_064_20261005.md, the actual physical bracket c-(10+c)rho-p-A exceeds 0.4095636415>2/5.

At independent logarithmic cutoff 7, the rational inequality (9/10)log(7)-(4/5)/7-A>0 supplies the high-band lower bound w/10, with w=log(e+|xi|). On the low band w<3, so the logarithmic bracket 1/10-(10+A+3/10)rho_log-p exceeds 0.09997787231>9/100. These initial estimates supply inverse factor 5/2 and lawful logarithmic complement coercivity. Their corrected sign fails below; the successful complement is stronger.

## Full Gram and the failed scalar estimates

All 2304 native/source pairings pass, with maximum discrepancy below 1.667e-35. The matching residual Gram projects away exactly degrees 0..47 and retains all log/log, smooth/smooth, log/smooth and mixed projection terms on every actual panel. Its maximum entry width is below 4.060e-109; actual Gram operator error delta=eta(2M+eta) is below 1.484e-25. Native/source hashes and all source errors are retained.

The initial Q_48-(5/2)R_48 estimator has a certified negative vector with Rayleigh upper bound below -3.222e-18. The same vector has strictly positive native Q_48 energy. Tightening the scalar roundoff to physical coercivity 409/1000 and inverse factor 1000/409 still yields a certified negative estimator direction, below -1.652e-16. These are negative lower-estimator directions, not negative actual native or corrected-form witnesses.

## Sharper quarter-line estimate

Write m_0(t)=Re psi(1/4+i pi t)-log(pi). For x>0 and y>0, Euler--Maclaurin through the B2 term gives

psi(z)=log(z)-1/(2z)-1/(12z^2)+integral_0^infinity periodic_B2(u)/(z+u)^3 du,
z=x+iy, periodic_B2(u)=r^2-r+1/6 with r the fractional part of u.

The remainder identity follows from the convergent Euler digamma sum by applying the finite Euler--Maclaurin formula and taking its limit; its integral is absolutely convergent. Since |periodic_B2|<=1/6, its absolute value is at most (1/6)integral_0^infinity [(x+u)^2+y^2]^(-3/2)du<=1/(6y^2). At x=1/4 and y>=x, -Re(1/(12z^2))>=0, Re(1/(2z))<=1/(8y^2), and log|z|>=log(y). Thus

Re psi(1/4+iy)>=log(y)-7/(24y^2).

Using pi>3 gives the rigorous actual high-band bound

m_0(t)>=log|t|-7/(216t^2), |t|>=1.

The independent low floor follows from the positive Euler series difference

Re psi(x+iy)-psi(x)=sum_{n>=0} y^2/[(n+x)((n+x)^2+y^2)]>=0,

and psi(1/4)=-gamma-3log(2)-pi/2. The exact upper gamma<H_100-log(100), Machin pi enclosure and rational logarithms give m_0(t)>-5.378>-27/5 everywhere.

## Ceiling of the earlier floor-10 family

With the new high estimate but retained low floor -10, cutoff 373/50 gives physical lower bound above 0.4759447 and certifies 47/100. Its inverse factor 100/47 still yields a negative estimator direction, below -2.408e-16. The same vector has positive native energy and requires scalar coercivity above 0.4766494345 to eliminate this sufficient-estimator obstruction.

This is not repaired by adjusting only the cutoff in that same proof family. Let F(T)=c(T)-(10+c(T))rho(T)-p-A, c(T)=log(T)-7/(216T^2). Positive lawful bounds require c>0 and rho<1: outside this region, with c>=-10 required by the low/high split, F cannot be positive. The mass bound has a positive power-series expansion rho=constant*T^97/(1-bT^2), so rho'>0 and rho''>0. On the positive region,

F''=c''(1-rho)-2c' rho'-(10+c)rho''<0.

Certified derivative signs F'(186/25)>0 and F'(187/25)<0 trap its maximum between these two cutoffs. The tangent at 373/50 bounds the whole interval by a value below 0.476127, hence below 4763/10000=0.4763. This is smaller than the countervector requirement above 0.4766. Therefore no positive outward lower bound from this floor-10 sharp cutoff family removes that vector's obstruction. This is a ceiling of the specified proof family, not an upper bound on actual complement coercivity.

## Retaining the actual low floor resolves the sign

Use the proved low floor -27/5 instead of -10, the same sharp quarter-line high estimate, and physical cutoff T=15/2. The new bracket

c(T)-(27/5+c(T))rho(T)-p-A

exceeds 0.4808725435>12/25. At independent logarithmic cutoff 7 the high-band check is (9/10)log(7)-(3/10)/7-7/(216*49)-A>0. On the low band w<3, the bracket 1/10-(27/5+A+3/10)rho_log-p exceeds 0.09998648227>9/100. This certifies the actual 48-moment physical complement coercivity 12/25 and inverse factor 25/12 uniformly through a=3/4. It changes the floor-10 family and so bypasses, rather than contradicts, its proved ceiling.

The actual residual Gram and its error are independent of the chosen scalar inverse factor. The successful corrected certificate reuses the complete certified enclosure with native/source/Gram hashes verified, delta=eta(2M+eta) checked, and the same physical projection retained. All 48 rational interval pivots of

Q_48-(25/12)Rhat_48-[(25/12)delta+1/20000000000000000]I

are strictly positive. The negative diagonal control is rejected. Hence corrected margin tau=1/20000000000000000 is lawful. The lift squared norm is below 50.634<64, so use physical lift norm at most 8.

For h=e+u, e in E_48 and u in the lawful complement,

Q(h)>=tau||e||_2^2+(12/25)||u+lift(e)||_2^2,
||h||_2^2<=2(1+8^2)||e||_2^2+2||u+lift(e)||_2^2.

Consequently Q(h)>=min(tau/130,6/25)||h||_2^2=(1/2600000000000000000)||h||_2^2. No physical spectral operator-domain membership is assumed.

## Validation and scope

All native, source, complement, full Gram, activation, tighter/sharper obstruction, cutoff-family ceiling and successful refined-floor correction certificates reproduce byte-for-byte. The previous a=7/10 matrix and sources reproduce unchanged. All 7536 regular-factor identities, seven panels, 2304 pairings, constructor guards, input hashes, native/refined-correction negative diagonal controls, positive-native controls for all negative estimators and prime-4 omission/doubled-coefficient controls pass. No floating quantity enters a sign decision.

Next: larger apertures with actual prime terms, source panels and matching complement bounds, or independent global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI standing are unchanged. These analytic/rational certificates are not Lean formalized.
