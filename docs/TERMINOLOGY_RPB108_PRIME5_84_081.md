# RPB108 prime-5 activation and 84-moment complement at aperture 81/100

- Aperture a=81/100=0.81: support [-a,a], width d=81/50. Active prime powers are 2, 3, 4 and 5. The prime-5 threshold is a=log(5)/2; a=4/5 lies below it.
- ell_n=log(n)/d: translation length in t=(x+a)/d. Prime 5 adds the first and last edge panels, yielding nine panels. Its source amplitude is A5=log(5)/sqrt(5); its native correlation coefficient is 2A5. Prime 4 retains Lambda(4)=log(2).
- s3=log(3), s5=log(5), epsilon=d-s5: physical prime-5 overlap length, with 0<epsilon<min(s5-s3,2s3-s5). The prime-3/5 fibres containing prime-5 edges have four vertices with offsets s3,0,s5,s5-s3, in chain order.
- J35=(A5+sqrt(A5^2+4A3^2))/2, A3=log(3)/sqrt(3): exact four-point chain norm, rounded upward to 1.089148588713 in the certificate. Other prime-3/5 fibres have only a prime-3 edge or no edge.
- J24=(A4+sqrt(A4^2+8A2^2))/2, A2=log(2)/sqrt(2), A4=log(2)/2: existing joint prime-2/4 three-point fibre norm. The total loss upper bound is J24+J35.
- E84 and P84: physical Legendre span of degrees 0..83 and its orthogonal projection at this aperture. The certified complement is the supported form-domain subspace orthogonal to E84. Its matching finite restriction and actual residual source Gram are not certified in this entry.
- rho84(T): exact 84-moment low-frequency mass upper bound; p84: absolute pole upper bound. Physical cutoff T=243/20 and logarithmic cutoff 19/2 give complement coercivity 51/100 and 9/100, uniformly for apertures in [1/2,81/100].
- beta84=100/51: inverse complement energy factor available for a future matching 84-coordinate Schur calculation.

This entry certifies activation geometry and complement coercivity. Whole-domain positivity remains certified through a=4/5. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean is unchanged; these certificates are not Lean formalized.
