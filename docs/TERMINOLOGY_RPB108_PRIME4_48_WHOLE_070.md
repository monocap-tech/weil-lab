# RPB108 actual 48-coordinate sign after prime-4 activation

- Aperture a=7/10=0.70: actual support [-a,a], width d=7/5, active prime powers 2, 3 and 4.
- Lambda(n): the von Mangoldt coefficient. Lambda(2)=Lambda(4)=log(2), while Lambda(3)=log(3). The source translation coefficient for 4 is Lambda(4)/sqrt(4)=log(2)/2.
- L=4a=14/5: native expansion parameter; exponential remainder multiplier 17 and kernel multiplier 3.
- ell_n=log(n)/d: actual translation length in the source coordinate t=(x+a)/d.
- C_s: supported translation by s plus its adjoint. At this aperture C_log(2) has norm sqrt(2), while C_log(3) and C_log(4) have norm one.
- A2=log(2)/sqrt(2), A4=log(2)/2: weights in the joint prime-2/prime-4 operator A2 C_log(2)+A4 C_log(4).
- J24=(A4+sqrt(A4^2+8A2^2))/2: largest eigenvalue and norm of the weighted three-point fibre matrix [[0,A2,A4],[A2,0,A2],[A4,A2,0]]. It bounds the joint prime-2/prime-4 form loss, with smaller fibres bounded by the same number.
- E_48 and P_48: physical Legendre span and orthogonal projection for degrees 0..47 at this aperture.
- Q_48: actual restriction including both poles and prime powers 2, 3, 4.
- Seven-panel sources: exact source approximations with the central simultaneous positive and negative prime-2 translations retained; exponential order 60 and 44 Bernoulli pairs.
- Physical complement coercivity 12/25: uniform 48-moment bound through this aperture at cutoff 8. Its inverse factor is 25/12; logarithmic coercivity remains 9/100 at independent cutoff 7.
- R_48: actual residual Gram after P_48; Rhat_48 is its surrogate, delta its certified operator error, and K_48 the lawful lift-energy correction bounded by (25/12)R_48.
- Corrected margin tau=1/5242880000000: certified lower bound for Q_48-(25/12)R_48 and hence Q_48-K_48.
- Lift norm at most 7: physical norm bound from (625/144)(trace Rhat_48 upper+delta)<49.
- Whole-domain physical margin 1/524288000000000: same-domain square-completion bound at a=7/10.

This excludes fixed-aperture weak null modes and gives corresponding full-source unit domination. Global endpoint exclusion, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These analytic/rational certificates are not Lean formalized.
