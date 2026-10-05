# RPB108 actual 48-coordinate sign at aperture 69/100

- Aperture a=69/100=0.69: support [-a,a], width d=69/50, active prime powers 2 and 3.
- L=69/25: native analytic expansion parameter; exponential remainder multiplier 16 and kernel multiplier 3.
- E_48 and P_48: physical Legendre span and orthogonal projection for degrees 0..47 at this aperture.
- Q_48: actual restriction including both poles and both active prime translations.
- C_s: supported translation by s plus its adjoint; its norm is one for a<s<2a. This applies to both actual primes here.
- A=log(2)/sqrt(2)+log(3)/sqrt(3): total compressed-prime physical loss bound at this aperture.
- Physical complement coercivity 89/100: uniform 48-moment bound through this aperture, with physical cutoff 81/10. The inverse factor is 100/89; logarithmic coercivity is 9/100 at independent cutoff 7.
- R_48: actual residual Gram after P_48; Rhat_48 is its surrogate and delta its certified operator error.
- K_48: lawful lift-energy correction, bounded by (100/89)R_48.
- Corrected margin tau=1/1310720000000: certified lower bound for Q_48-(100/89)R_48 and hence Q_48-K_48.
- Lift norm at most 4: physical operator norm bound from (10000/7921)(trace Rhat_48 upper+delta)<16.
- Whole-domain physical margin 1/44564480000000: same-domain square-completion bound at a=69/100.
- Upcoming prime-4 threshold a=log(2)=log(4)/2: prime power 4 starts contributing beyond this aperture, with von Mangoldt coefficient Lambda(4)/sqrt(4)=log(2)/2.
- Three-point prime-2 fibre: the path adjacency [[0,1,0],[1,0,1],[0,1,0]], with eigenvalues -sqrt(2),0,sqrt(2). Its positive-measure appearance when 2log(2)<2a<3log(2) changes the compressed prime-2 norm to sqrt(2).

The present certificate stops at a=69/100 and includes no prime-4 term. It excludes fixed-aperture weak null modes and gives corresponding full-source unit domination. Global endpoint exclusion, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These analytic/rational certificates are not Lean formalized.
