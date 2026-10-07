# RPB108: critical eigenmode control and signed order-one target

- Actual shifted eigenspace K_a^mu={h in D_a:q_h=mu h on I_a}; mu is a real physical eigenvalue. K_a^0 is the full native kernel. A positive-eigenvalue vector is not a zero-null vector.
- Shifted residual q_h^mu=q_h-mu h. On the exterior it equals q_h, since the unchanged physical vector is zero there.
- Critical positive moment M_(+,1)(h)=sum_actual_copies |theta_q| |p_q(h)|^2. It is the source height order one, corresponding to Xcrit; notation differs from M_(+,s) with exponent 2s in the historical fractional registry.
- Critical signed cutoff J_(epsilon,1)(theta)=integral_epsilon^t0 (1-cos(theta t))dt/t^2; I_(epsilon,1)(h)=sum J_(epsilon,1)(theta)(|p|^2-|n|^2), taking two finite sums before the cutoff limit.
- W_(epsilon,1)=integral_epsilon^t0 D_w(t)dt/t^2, nonnegative and monotone as epsilon decreases.
- B_(epsilon,1)^mu=integral_epsilon^t0 F_h^mu(t)dt/t^2 is the genuine exterior flux of an actual shifted eigenmode. The full trace uses a physical L2 orthonormal basis of the stated entire eigenspace.
- Subcritical half-height moments for the remainder: s=1/4 means M_(+,s)=sum |theta|^(1/2)|p|^2 and likewise for n. These are already derived for actual shifted eigenmodes.
- Shifted critical promotion: K_a^mu intersect Xcrit=K_a^mu intersect H1, with the same global derivative in K_a^mu. It is analytic and inherits the pinned boundary input, not a Lean theorem.
- Critical signed contact target: finite liminf I_(epsilon,1)^K for the whole hypothetical nonnegative zero-contact kernel. It is equivalent to its critical positive trace finiteness and suffices for K=0; its actual bound remains unproved.
