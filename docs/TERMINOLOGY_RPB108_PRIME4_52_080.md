# RPB108 actual 52-coordinate whole-domain sign at aperture 4/5

- Aperture a=4/5=0.80: support [-a,a], width d=8/5, active prime powers 2, 3, 4, with Lambda(4)=log(2). Prime 5 activates only above this aperture, at log(5)/2.
- L=4a=16/5: native expansion parameter; exponential multiplier 25, kernel multiplier 4. Native exponential order 180, Bernoulli pairs 140. Source exponential order 60, Bernoulli pairs 52 and exponential remainder coefficient 2.
- ell_n=log(n)/d: translation length in t=(x+a)/d. All seven actual source panels, including central prime-2 overlap, are retained.
- E_52, P_52, Q_52, R_52: matching physical Legendre span of degrees 0..51, orthogonal projection, actual native restriction and complete actual residual source Gram. Rhat_52 is the Gram surrogate, eta the source-map error, M its surrogate residual-map norm bound and delta=eta(2M+eta) its actual operator-error bound.
- J24=(A4+sqrt(A4^2+8A2^2))/2, A2=log(2)/sqrt(2), A4=log(2)/2: joint prime-2/prime-4 three-point translation-fibre norm.
- m_0(t)=Re psi(1/4+i pi t)-log(pi): actual quarter-line archimedean multiplier, with high lower estimate log|t|-7/(216t^2), |t|>=1, and global floor -27/5.
- rho(T): exact 52-moment low-frequency mass upper bound; p: absolute pole upper bound. At T=38/5 the physical complement lower bound is 49/100; the independent logarithmic cutoff 7 gives 9/100. These bounds hold uniformly on [1/2,4/5].
- beta=100/49: inverse complement energy factor; K_52: lawful lift-energy correction bounded by beta R_52.
- tau=1/2748779069440000000: certified corrected margin for Q_52-beta R_52, hence Q_52-K_52.
- Lift norm at most 8: follows from beta^2(trace Rhat_52 upper+delta)<64.
- Whole-domain margin 1/357341279027200000000: same-domain square-completion lower bound tau/[2(1+8^2)] at aperture 4/5.

This excludes fixed-aperture weak null modes and establishes corresponding full-source WD-T10 unit domination. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These analytic/rational certificates are not Lean formalized.
