# RPB108: actual 52-coordinate whole-domain sign at aperture 4/5

Base: 2d5151ad84cff9ede821e86c106a22a9cdc07ceb.
Definitions: docs/TERMINOLOGY_RPB108_PRIME4_52_080.md.

## Actual matrix and sources

Here a=4/5, d=2a=8/5, L=4a=16/5. Rational logarithmic enclosures certify log(4)<d<log(5). Prime powers 2, 3 and 4 remain the entire active set; Lambda(4)=log(2). Prime 5 first activates at a=log(5)/2, strictly above this aperture. This calculation recomputes the native matrix, actual sources and complete residual Gram with the matching 52-dimensional physical Legendre projection. No 48-dimensional residual Gram is reused.

The physical basis is sqrt((2n+1)/(2a))P_n(x/a), n=0..51. Rational bounds L<log(25) and L>log(5) give exp(L)<25 and L/(1-exp(-L))<4. Native exponential order is 180, Bernoulli pairs 140, gamma order 12 and outward interval grid 10^-200. All 52 native and shifted pivots pass; the raw physical margin is 1/68719476736000000. Exact reflection parity holds; the negative diagonal control is rejected.

The actual sources retain the endpoint logarithm, both regular-difference terms, both pole moments and all seven prime-translation panels. Their endpoints and translations are:

| t interval | Active translations |
| --- | --- |
| (0,1-ell_4) | +2,+3,+4 |
| (1-ell_4,1-ell_3) | +2,+3 |
| (1-ell_3,ell_2) | +2 |
| (ell_2,1-ell_2) | +2,-2 |
| (1-ell_2,ell_3) | -2 |
| (ell_3,ell_4) | -2,-3 |
| (ell_4,1) | -2,-3,-4 |

Here t=(x+a)/d and ell_n=log(n)/d. The source coefficient for each prime-4 translation is -log(2)/2. Omitting that translation or replacing its coefficient by -log(4)/2 fails the constant-coordinate pairing control. Panel-order and translation activation controls also pass.

Source exponential order is 60, Bernoulli pairs 52 and gamma order 20. The kernel remainder is 4(d/3)^106/[1-(d/3)^2]; the exponential coefficient 2 is half the kernel bound. The pole argument has absolute value at most d/4=2/5<log(2), proving its Taylor remainder multiplier 2. All polynomial rounding at grid 10^-40 is included in the source error. Aggregate actual source-map error is below 9.784e-26. All 8580 regular-factor identities for j=0..51 and k=0..164 agree with the original binomial sums. Exact high-degree correlations agree independently for (0,51), (48,51) and (51,51). Unsupported dimension/aperture combinations are rejected. Both previous a=3/4 matrix and source certificates reproduce byte for byte.

## Uniform actual 52-moment complement

The complete complement estimate uses the actual quarter-line multiplier m_0(t)=Re psi(1/4+i pi t)-log(pi). The earlier convergent Euler--Maclaurin identity proves m_0(t)>=log|t|-7/(216t^2) for |t|>=1. Its low-frequency bound follows from Re psi(1/4+iy)>=psi(1/4)=-gamma-3log(2)-pi/2 and the rational gamma/log/pi enclosures: m_0>-27/5.

For supported functions orthogonal to degrees 0..51, use the exact 52-moment low-frequency mass estimate rho and pole estimate p. The joint prime-2/prime-4 loss is J24=(A4+sqrt(A4^2+8A2^2))/2, with A2=log(2)/sqrt(2), A4=log(2)/2. Since 2log(2)<2a<3log(2), this is the three-point weighted translation-fibre norm. The prime-3 loss is log(3)/sqrt(3), since a<log(3)<2a. These losses bound all smaller apertures in [1/2,4/5] as well, including before individual terms activate.

At physical cutoff T=38/5, c=log(T)-7/(216T^2), the rigorous quantity c-(27/5+c)rho-p-J24-log(3)/sqrt(3) exceeds 0.497130457049555 and hence 49/100. Independent logarithmic cutoff 7 gives a lower bound exceeding 0.099998579175869 and hence 9/100. The inverse energy factor is 100/49. These complement bounds alone do not decide the whole form sign.

## Complete residual Gram and sign

On the entire actual canonical supported logarithmic form domain at a=4/5,

Q(h)>=(1/357341279027200000000)||h||_2^2.

All 52 corrected shifted pivots certify tau=1/2748779069440000000 after the complete residual Gram and actual operator error are subtracted with inverse factor 100/49. The maximum residual-Gram entry width is below 1.919e-102; maximum native/source pairing discrepancy is below 3.484e-35; delta is below 7.114e-25. All 2704 pairings lie within their independently certified source errors.

The lift norm squared is below 55.054<64, so the physical lift norm is at most 8. Same-domain square completion gives the lower bound min(tau/[2(1+8^2)],(49/100)/2)=tau/130=1/357341279027200000000. This is a whole-domain bound, not merely finite-restriction positivity. It excludes fixed-aperture weak null modes and establishes the corresponding full-source WD-T10 unit domination. The corrected negative diagonal control is rejected.

The Gram retains the endpoint-log/log, endpoint-log/smooth and smooth/smooth terms, and subtracts the entire matching 52-coordinate source projection. All mixed terms remain present. Actual source errors yield the operator correction delta=eta(2M+eta), where M bounds the surrogate residual-source map. Every native/source pairing is independently compared with the freshly certified native matrix. The corrected matrix is Q_52-(100/49)Rhat_52-(100/49)delta I, with a further certified positive margin where applicable.

## Validation and standing

The matrix, sources, complement, complete Gram and activation controls are reproduced byte for byte. Independent exact arithmetic and unsupported-constructor controls pass. The previous a=3/4 matrix and source certificates also reproduce after the shared helper extensions. Only degree 51 at aperture 4/5 is newly enabled; all older constructor arithmetic is preserved.

These are analytic/rational arithmetic certificates. Lean, axioms and CI are unchanged. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open.
