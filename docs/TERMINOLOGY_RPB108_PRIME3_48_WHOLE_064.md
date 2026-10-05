# RPB108 actual 48-coordinate sign at aperture 16/25

- Aperture a=16/25=0.64: support [-a,a], width d=32/25, active prime powers 2 and 3.
- L=64/25: native analytic expansion parameter; exponential remainder multiplier 13 and kernel multiplier 3.
- E_48 and P_48: physical Legendre span and orthogonal projection for degrees 0..47 at this aperture.
- Q_48: actual restriction including both poles and both prime translations.
- C_s: supported translation by s plus its adjoint. Its norm is one when a<s<2a; the disjoint two-strip swap proof applies to both actual primes here.
- A=log(2)/sqrt(2)+log(3)/sqrt(3): total compressed-prime physical loss bound.
- Physical complement coercivity 24/25: uniform 48-moment bound through this aperture, using physical cutoff 35/4. Its inverse factor is 25/24; logarithmic coercivity remains 9/100 at independent cutoff 7.
- R_48: actual residual Gram after P_48; Rhat_48 is its enclosure surrogate and delta its certified operator error.
- K_48: lawful lift-energy correction, bounded by (25/24)R_48.
- Corrected margin tau=1/20480000000: certified lower bound for Q_48-(25/24)R_48, hence for Q_48-K_48.
- Lift norm at most 4: physical operator norm bound from (625/576)(trace Rhat_48 upper+delta)<16.
- Whole-domain physical margin 1/696320000000: same-domain square-completion bound at a=16/25.

This excludes fixed-aperture weak null modes and gives corresponding full-source unit domination. Global endpoint exclusion, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These analytic/rational certificates are not Lean formalized.
