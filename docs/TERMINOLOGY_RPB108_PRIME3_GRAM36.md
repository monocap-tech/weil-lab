# RPB108 prime-3 full residual Gram terminology

- Aperture a=11/20: physical support [-a,a], with active prime powers 2 and 3.
- E_36: span of the physical orthonormal Legendre vectors of degrees 0..35. P_36 is its orthogonal projection.
- q_i: actual interior native source for the i-th physical vector, on the supported logarithmic form domain.
- R_36: actual residual Gram, R_ij=< (1-P_36)q_i,(1-P_36)q_j > in physical L2.
- Rhat_36: the explicitly integrated Gram of the certified source surrogates; its operator error is bounded separately.
- Q_36: independently certified full native restriction, including actual prime shifts and both poles.
- K_36: the actual lawful form-complement lift correction. The complement coercivity 1/4 proves K_36<=4R_36.
- G_36=Q_36-4R_36: a sufficient lower estimator for the exact corrected form Q_36-K_36. Its negative directions would not be negative directions of the whole form.
- Endpoint logarithm L(t)=-(log(t)+log(1-t))/2: kept exact on t in (0,1), with all products and projection terms retained.
- Source-map error eta: physical L2 operator error bounded by the square root of the sum of squared row errors.
- Gram error delta=eta(2M+eta): operator enclosure when M bounds the surrogate residual map norm.
- Fixed-aperture unit domination: same-domain consequence of a certified strictly positive whole form at this aperture. It does not close global endpoint exclusion or retained source/null transport.

All arithmetic certificates here use rational outward intervals. They are not Lean proofs; F4 and FULL TRANSPORT CLOSED retain their separate open obligations.
