# RPB108: actual whole-domain sign at aperture a=69/100

Base: d1fd6004014278372db7554f68f32c92504b4aef.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_48_WHOLE_069.md.

## Result

On the entire actual supported logarithmic form domain at a=69/100,

Q(h)>=(1/44564480000000)||h||_2^2.

This excludes fixed-aperture weak null modes and establishes corresponding full-source WD-T10 unit domination. Global endpoint exclusion and F4 remain open.

## Actual aperture and analytic errors

The 48-coordinate native matrix, physical sources and full residual Gram are recomputed at a=69/100, d=69/50, L=69/25. The actual active prime powers remain 2 and 3 because log(3)<2a<log(4). The five source panels are cut at 0,1-log(3)/d,1-log(2)/d,log(2)/d,log(3)/d,1. Both poles and all mixed terms are retained.

Rational logarithm bounds prove L<log(16) and log(15)<L<14/5. Thus exp(L)<16 and L/(1-exp(-L))<(14/5)/(14/15)=3. Monotonicity of z/(1-exp(-z)) supplies the same bound on the entire kernel interval. Native exponential order 160, 120 Bernoulli pairs and gamma order 12 are retained. Sources use exponential order 60, 40 Bernoulli pairs and gamma order 20. The source remainder is 4(d/3)^82/[1-(d/3)^2]; its coefficient 3/2 remains half the kernel bound. The pole remainder remains valid since a<log(2). All outward arithmetic uses grid 10^-200, with source polynomial rounding at grid 10^-40 and its error retained. The new aperture is enabled only for degree 47; previous audited arithmetic is preserved.

## Matching compressed-prime complement

Use the compressed-prime complement method from the preceding checkpoint with its matching 48-source projection. For a translation length s with a<s<2a, write the supported operator C_s=T_s+T_s*. It swaps the disjoint intervals [-a,a-s] and [-a+s,a], and vanishes on the middle interval. Its two-point fibre matrix is [[0,1],[1,0]], so ||C_s||=1. The two edge intervals are disjoint because a<s. This applies to both s=log(2) and s=log(3) at a=69/100 and, whenever active, throughout [1/2,69/100]. Below activation C_s=0.

The actual prime term is -(log(n)/sqrt(n))<f,C_log(n)f>. Hence the total prime loss is at most A||f||_2^2, A=log(2)/sqrt(2)+log(3)/sqrt(3). Applying this supported estimate to prime 2 saves half its former global Fourier multiplier penalty. No smaller-overlap norm gain is asserted.

Let m_0(xi)=Re psi(1/4+i pi xi)-log(pi) be the archimedean symbol. The high-frequency estimate before prime subtraction is m_0(xi)>=log|xi|-1/(2|xi|). It follows directly from the Euler first-order integral remainder: for z=x+iy, x>0, y>0, the term after log(z)-1/(2z) has absolute value at most (1/2)integral_0^infinity dt/[(x+t)^2+y^2]<=pi/(4y). Thus Re psi(z)>=log|z|-(1/2+pi/4)/y. With y=pi|xi| and pi>2, (pi+2)/(4pi)<1/2, giving the stated estimate. For completeness the low floor is independently checked: the Euler series gives

Re psi(x+iy)-psi(x)=sum_{n>=0} y^2/[(n+x)((n+x)^2+y^2)] >= 0.

Using psi(1/4)=-gamma-3log(2)-pi/2 and gamma<H_100-log(100)<1 gives a certified global lower bound greater than -5.378, hence greater than -10. Thus no low-floor constant for a different prime symbol is silently reused.

For moment vanishing through degree 47, put T=81/10 and

rho=4a T[2a(22/7)T]^96/[(97!!)^2(1-q)], q=[2a(22/7)T]^2/(97*99)<1,
p=16a(a/2)^96/(48!)^2, c=log(T)-1/(2T).

Both rho and p increase with a on this range. The actual physical lower bracket is c-(10+c)rho-p-A>0.8958155620>89/100. The matching physical inverse factor is 100/89.

The independent logarithmic cutoff remains 7. For w(xi)=log(e+|xi|), w<=log|xi|+3/|xi| on |xi|>=7. The rational inequality (9/10)log(7)-(4/5)/7-A>0 proves m_0-A>=w/10 there. On the low band w<3, so the remaining bracket 1/10-(10+A+3/10)rho_log-p exceeds 0.09999999355>9/100. This provides lawful logarithmic coercivity and the complement lift on the same form domain.

At a=69/100 the current prime panels remain valid, but the next activation is a=log(2)=log(4)/2. The norm-one prime-2 swap argument also stops there: beyond that threshold its compressed adjacency has three-point fibres and norm sqrt(2) for support width between 2log(2) and 3log(2). On each three-point fibre the prime-2 adjacency matrix is [[0,1,0],[1,0,1],[0,1,0]], with eigenvalues -sqrt(2),0,sqrt(2); the longest fibres have positive measure immediately above the threshold. Further aperture work must include prime power 4 with coefficient Lambda(4)/sqrt(4)=log(2)/2, not log(4)/2, and the changed prime-2 chain bound. No sign beyond the threshold is claimed.

## Full native matrix, source map and corrected Gram

All 48 native and shifted pivots pass, with raw physical coercivity 1/1048576000000. Exact reflection parity and the native negative diagonal control pass. The combined actual source-map error is below 1.733e-24; polynomial coefficient-rounding errors are retained. Every actual source is paired with every native coordinate: all 2304 comparisons pass with maximum interval discrepancy below 3.534e-33. The matching residual Gram projects away exactly degrees 0..47 and retains all endpoint-log, smooth and mixed projection terms. Its maximum entry width is below 5.631e-111, and actual Gram operator error delta=eta(2M+eta) is below 1.120e-23. Native/source hashes are recorded.

All 48 interval pivots of

Q_48-(100/89)Rhat_48-[(100/89)delta+1/1310720000000]I

are strictly positive. Hence the actual lawful corrected form has physical margin tau=1/1310720000000. Its negative diagonal control is rejected. The lawful lift squared norm is below 13.188<16, so its physical operator norm is at most 4.

## Whole-domain assembly and validation

For h=e+u, with e in E_48 and u in the lawful complement,

Q(h)>=tau||e||_2^2+(89/100)||u+lift(e)||_2^2,
||h||_2^2<=2(1+4^2)||e||_2^2+2||u+lift(e)||_2^2.

Therefore

Q(h)>=min(tau/34,89/200)||h||_2^2
     =(1/44564480000000)||h||_2^2.

No physical spectral operator-domain membership is assumed. This same-domain sign excludes weak null modes and gives the corresponding full-source unit-domination consequence.

All four rational certificates reproduce byte-for-byte. The previous a=16/25 matrix and sources reproduce unchanged under the extended constructors. All 6768 regular-factor identities, native/corrected shifted pivots, 2304 pairings, input hashes, constructor guards and both negative diagonal controls pass. No floating quantity enters a sign decision.

Next: cross prime-4 activation with the correct prime-power coefficient and changed prime-2 chain, then recompute the matching matrix, sources, complement and Gram; or pursue independent global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI standing are unchanged. These analytic/rational certificates are not Lean formalized.
