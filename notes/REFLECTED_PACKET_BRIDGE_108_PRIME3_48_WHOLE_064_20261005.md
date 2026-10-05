# RPB108: actual whole-domain sign at aperture a=16/25

Base: b0bdd60b239addd75c526654cd38251adf228b9b.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_48_WHOLE_064.md.

## Actual aperture and analytic errors

The 48-coordinate native matrix, physical sources and full residual Gram are recomputed at a=16/25, d=32/25, L=64/25. The actual active prime powers remain 2 and 3 because log(3)<2a<log(4). The five source panels are cut at 0,1-log(3)/d,1-log(2)/d,log(2)/d,log(3)/d,1. Both poles and all mixed terms are retained.

Rational logarithm bounds prove L<log(13) and log(8)<L<21/8. Thus exp(L)<13 and L/(1-exp(-L))<(21/8)/(7/8)=3. Monotonicity of z/(1-exp(-z)) supplies the same bound on the entire kernel interval. Native exponential order 160, 120 Bernoulli pairs and gamma order 12 are retained. Sources use exponential order 60, 40 Bernoulli pairs and gamma order 20. The source remainder is 4(d/3)^82/[1-(d/3)^2]; its coefficient 3/2 remains half the kernel bound. The pole remainder remains valid since a<log(2). All outward arithmetic uses grid 10^-200, with source polynomial rounding at grid 10^-40 and its error retained. The new aperture is enabled only for degree 47; previous audited arithmetic is preserved.

## Stronger compressed-prime complement

This checkpoint improves the complement proof rather than substituting a smaller projection's Gram. For a translation length s with a<s<2a, write the supported operator C_s=T_s+T_s*. It swaps the disjoint intervals [-a,a-s] and [-a+s,a], and vanishes on the middle interval. Its two-point fibre matrix is [[0,1],[1,0]], so ||C_s||=1. The two edge intervals are disjoint because a<s. This applies to both s=log(2) and s=log(3) at a=16/25 and, whenever active, throughout [1/2,16/25]. Below activation C_s=0.

The actual prime term is -(log(n)/sqrt(n))<f,C_log(n)f>. Hence the total prime loss is at most A||f||_2^2, A=log(2)/sqrt(2)+log(3)/sqrt(3). Applying this supported estimate to prime 2 saves half its former global Fourier multiplier penalty. No smaller-overlap norm gain is asserted.

Let m_0(xi)=Re psi(1/4+i pi xi)-log(pi) be the archimedean symbol. The high-frequency estimate before prime subtraction is m_0(xi)>=log|xi|-1/(2|xi|). It follows directly from the Euler first-order integral remainder: for z=x+iy, x>0, y>0, the term after log(z)-1/(2z) has absolute value at most (1/2)integral_0^infinity dt/[(x+t)^2+y^2]<=pi/(4y). Thus Re psi(z)>=log|z|-(1/2+pi/4)/y. With y=pi|xi| and pi>2, (pi+2)/(4pi)<1/2, giving the stated estimate. For completeness the low floor is independently checked: the Euler series gives

Re psi(x+iy)-psi(x)=sum_{n>=0} y^2/[(n+x)((n+x)^2+y^2)] >= 0.

Using psi(1/4)=-gamma-3log(2)-pi/2 and gamma<H_100-log(100)<1 gives a certified global lower bound greater than -5.378, hence greater than -10. Thus no low-floor constant for a different prime symbol is silently reused.

For moment vanishing through degree 47, put T=35/4 and

rho=4a T[2a(22/7)T]^96/[(97!!)^2(1-q)], q=[2a(22/7)T]^2/(97*99)<1,
p=16a(a/2)^96/(48!)^2, c=log(T)-1/(2T).

Both rho and p increase with a on this range. The actual physical lower bracket is c-(10+c)rho-p-A>0.9754205406>24/25. The matching physical inverse factor is 25/24.

The independent logarithmic cutoff remains 7. For w(xi)=log(e+|xi|), w<=log|xi|+3/|xi| on |xi|>=7. The rational inequality (9/10)log(7)-(4/5)/7-A>0 proves m_0-A>=w/10 there. On the low band w<3, so the remaining bracket 1/10-(10+A+3/10)rho_log-p exceeds 0.09999999999>9/100. This provides lawful logarithmic coercivity and the complement lift on the same form domain.

## Full matrix, sources and corrected sign

All 48 native pivots and shifted pivots pass, with raw physical coercivity 1/16384000000. Reflection parity is exact and the negative diagonal control is rejected. The combined actual source-map error eta is below 3.499e-27. All 2304 native/source pairings pass with maximum discrepancy below 7.948e-36. All log/log, log/smooth, smooth/smooth and projection terms are retained in the matching residual Gram. Its maximum entry width is below 7.401e-110; the actual Gram operator error delta=eta(2M+eta) is below 2.182e-26. Native and source file hashes are retained in the Gram certificate.

All 48 interval pivots of

Q_48-(25/24)Rhat_48-[(25/24)delta+1/20480000000]I

are strictly positive. Hence the actual lawful corrected form has lower margin tau=1/20480000000. The corrected negative diagonal control is rejected. The lift squared norm is below 10.547<16, so use physical lift norm at most 4.

## Whole-domain assembly and validation

For h=e+u, where e belongs to E_48 and u to the lawful complement, square completion gives

Q(h)>=tau||e||_2^2+(24/25)||u+lift(e)||_2^2,
||h||_2^2<=2(1+4^2)||e||_2^2+2||u+lift(e)||_2^2.

Consequently, on the entire actual supported logarithmic form domain at a=16/25,

Q(h)>=min(tau/34,12/25)||h||_2^2
     =(1/696320000000)||h||_2^2.

This excludes fixed-aperture weak null modes and establishes the corresponding full-source WD-T10 unit domination. No spectral operator-domain membership is assumed.

The matrix, rounded sources, complement and full Gram/whole-domain certificate reproduce byte-for-byte. The previous a=3/5 matrix and sources reproduce unchanged under the narrowly extended constructors. All 6768 regular-factor identities, 48 native and corrected pivots, 2304 pairings, input hashes and both negative diagonal controls pass.

## Scope

Next: larger apertures with actual prime panels and matching complement bounds, or global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These analytic/rational certificates are not Lean formalized. Lean source, axioms and prior CI standing are unchanged.
