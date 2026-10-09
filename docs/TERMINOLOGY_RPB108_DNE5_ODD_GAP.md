# RPB108 DNE5 — Native heat smoothing and reflected-cut diagnostics

**DNE5** is the quantitative odd spectral-gap investigation following DNE4's complete weighted ground-state domain identity. DNE5 does not claim global odd positivity or exclusion of an original contact.

For a finite aperture a, use the exact positive Dirichlet jump operator J_a of DNE3 on physical L2(-a,a), including the continuous native jump kernel j(d)=exp(-|d|/2)/(1-exp(-2|d|)) and all currently active prime powers, each with c_n=Lambda(n)/sqrt(n)>0 and displacement ell_n=log n. This is the POLE-FREE positive operator; H_a=J_a-kappa_a I.

Let phi_a>=0 denote its normalized even positive ground eigenfunction, with J_a phi_a=mu_a phi_a, mu_a=kappa_a+lambda_0(H_a)>=0; DNE2 proves phi>0 almost everywhere. Put M_a=||phi_a||_infinity and S_a^phi=int_I phi_a (NOT the sum of prime coefficients).

**Full-line heat bound:** If Psi_a(xi) is the characteristic exponent of the unrestricted translation-invariant positive jump form with precisely the same active finite prime powers, then Psi_a(xi)>=log(e+|xi|)-8-a_arch(0), where a_arch(0)=psi(1/4)-log pi. For time t=1 its whole-line convolution density p_1 has ||p_1||_2<=exp(8+a_arch(0))*sqrt(2/e)<exp(3)*sqrt(2/e). The killed supported semigroup is dominated pointwise by the free semigroup. Hence M_a<=exp(mu_a+3)*sqrt(2/e). There is no claim of a positive uniform boundary infimum.

**Odd transformed spectral gap:** For the closed weighted DNE4 form, on the odd parity space, gamma_odd(a)=inf W_phi(u)/||u||²_(phi² dx) is bounded below by
`gamma_odd(a)>=j(2a)*S_a^phi/M_a>=j(2a)/M_a²>0`.
The last inequality uses the L2 normalization 1<=M_a S_a^phi. It is a genuine form-domain inequality.

**At a=53/50:** NF12's authenticated full signed low4 intervals and CC40's pinned copy show H_a on normalized degree0 has value < -4, so lambda_0(H_a)<-4. CC37 bounds the active coefficient sum <4; elementary special-function constants yield kappa_a<15. Therefore mu_a<11. Since j(2a)>1/9 and M_a<e^14 sqrt(2/e), one obtains the conservative explicit rational spectral statement
`gamma_odd(53/50)>3^(-30)`.
This is not a strict gap above -lambda_0 (which exceeds 4).

**Diameter-floor no-go:** The same *specific* coarse certificate `Gamma_diam=j(2a) S_a^phi/M_a` always obeys `Gamma_diam<=2a*j(2a)<9/10` at a=53/50. Hence it cannot by itself establish `gamma_odd>-lambda_0>4`. This is a limitation of a sufficient lower bound, not an upper bound on the ACTUAL gamma_odd and not a negative Weil vector.

**Reflected sign-cut test:** The odd weighted function u(x)=sgn(x) lies in DNE4's COMPLETE weighted domain once phi is bounded. Its normalized Rayleigh value is exactly
```
C_cut(phi) =
 4 int_0^a int_0^a j(x+y)phi(x)phi(y)dxdy
 +4 sum_(ell_n<=2a)c_n
     int_(max(0,ell_n-a))^(min(a,ell_n))
                phi(z)phi(ell_n-z) dz.
```
Thus `gamma_odd<=C_cut(phi)`. This is a new **upper** diagnostic including all original prime bridges across the symmetry point; it is NOT a lower certificate, and no actual phi integral is yet evaluated.

**Next requirement:** Find an eigenfunction-adapted, prime-sensitive lower bound exceeding the ground depth -lambda_0, or an independent arithmetic obstruction. Heat smoothing, diameter conductance and the sign-cut upper diagnostic alone do not exclude moment-zero nulls.
