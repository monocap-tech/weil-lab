# RPB108 actual 48-coordinate sign at aperture 3/5

- Aperture a=3/5=0.60: actual support [-a,a], width d=2a=6/5, with active prime powers 2 and 3.
- L=4a=12/5: the native analytic expansion parameter. Exponential remainder multiplier 12 and kernel multiplier 3 are certified at this value.
- E_48 and P_48: physical Legendre span and orthogonal projection for degrees 0..47 at this aperture.
- Q_48: actual native restriction on E_48, including both poles and actual prime shifts at a=3/5.
- Source expansion: exponential order 60 and 40 Bernoulli pairs at this aperture, with exact endpoint logarithm and five actual prime panels. Older apertures retain 32 pairs.
- Physical complement coercivity 11/20: the actual 48-moment complement lower bound at this aperture. Here 11/20 is a coercivity constant, not the aperture.
- Complement inverse factor 20/11: sufficient lawful inverse bound from the physical coercivity 11/20; logarithmic coercivity remains 9/100.
- R_48: actual residual Gram of all 48 sources after the matching P_48 projection. Rhat_48 is its surrogate and delta its certified operator error.
- K_48: actual lawful form-complement lift correction, satisfying K_48<=(20/11)R_48.
- Corrected margin tau=1/1280000000: lower bound certified for Q_48-(20/11)R_48 and therefore Q_48-K_48.
- Lift norm at most 6: physical operator norm bound from (400/121)(trace Rhat_48 upper+delta)<36.
- Whole-domain physical margin 1/94720000000: same-domain square-completion bound at a=3/5.

This fixed-aperture sign excludes weak null modes and gives corresponding full-source unit domination. It does not prove global endpoint exclusion, retained witness/null transport, F4 or FULL TRANSPORT CLOSED. The new rational/analytic certificates are not Lean formalized.
