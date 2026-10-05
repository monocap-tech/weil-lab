# RPB108 actual 48-coordinate sign at aperture 3/4

- Aperture a=3/4=0.75: support [-a,a], width d=3/2, active prime powers 2, 3, 4, with Lambda(4)=log(2).
- L=4a=3: native expansion parameter; exponential multiplier 21 and kernel multiplier 4. Source exponential remainder coefficient 2 is half the kernel bound; source Bernoulli pairs are 48.
- ell_n=log(n)/d: source translation length in t=(x+a)/d; all seven actual panels and central prime-2 overlap are retained.
- E_48, P_48, Q_48 and R_48: physical Legendre span, projection, actual native restriction and complete actual residual source Gram at this aperture. Rhat_48 is its surrogate and delta its actual operator error.
- J24=(A4+sqrt(A4^2+8A2^2))/2, A2=log(2)/sqrt(2), A4=log(2)/2: joint prime-2/prime-4 three-point fibre norm. Total prime loss bound is A=J24+log(3)/sqrt(3).
- m_0(t)=Re psi(1/4+i pi t)-log(pi): pure archimedean multiplier in the fixed Fourier normalization.
- periodic_B2(u)=r^2-r+1/6, r the fractional part of u: second periodic Bernoulli polynomial, with absolute bound 1/6, used in the convergent Euler--Maclaurin remainder.
- Sharp high estimate: m_0(t)>=log|t|-7/(216t^2) for |t|>=1; the actual low floor is m_0>-27/5.
- Floor-10 sharp family: F(T)=c(T)-(10+c(T))rho(T)-p-A, c(T)=log(T)-7/(216T^2). Its certified ceiling 4763/10000 is a limit of this sufficient cutoff family, not an upper bound on actual coercivity.
- Negative estimator vectors: certified negative directions of Q_48-beta R_48, with positive native Q_48 control. They do not witness negative actual Q or negative lawful corrected form.
- Refined-floor complement: c(T)-(27/5+c(T))rho(T)-p-A at T=15/2, certifying physical coercivity 12/25 and inverse factor 25/12. Independent logarithmic cutoff 7 retains 9/100.
- K_48: lawful lift-energy correction bounded by (25/12)R_48 under the refined-floor complement.
- Corrected margin tau=1/20000000000000000: certified lower bound for Q_48-(25/12)R_48 and therefore Q_48-K_48.
- Lift norm at most 8: physical norm bound from (625/144)(trace Rhat_48 upper+delta)<64.
- Whole-domain physical margin 1/2600000000000000000: same-domain square-completion bound at a=3/4.

The successful refined-floor theorem changes the earlier floor-10 family; its positivity is consistent with the preserved negative estimator and family-ceiling certificates. It excludes fixed-aperture weak null modes and gives corresponding full-source unit domination. Global endpoint exclusion, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These analytic/rational certificates are not Lean formalized.
