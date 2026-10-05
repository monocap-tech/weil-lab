# RPB108 aperture 14/25 full Gram and cutoff-family terminology

- R_36: actual residual Gram of all 36 native sources at a=14/25 after removing exactly the physical Legendre coordinates 0..35. Rhat_36 denotes the integrated certified source surrogate.
- delta: the actual Gram operator error bound eta(2M+eta), where eta is the certified source-map physical L2 error and M^2 is bounded by the surrogate Gram trace.
- Scalar inverse estimator G_beta=Q_36-beta R_36: a sufficient lower estimator for the exact corrected form when K_36<=beta R_36. A negative direction of G_beta is not a negative direction of the actual corrected form or full native form.
- Cutoff majorant family: F(T)=c(T)-(10+c(T))rho(T)-p-A, with c(T)=log(T)-1/(2T)-sqrt(2)log(2), A=log(3)/sqrt(3), p the proved 36-moment pole bound and rho(T) the existing integrated-mass majorant at a=14/25. Its lawful positive-bound use requires T>0, geometric ratio below one, and 10+c(T)>=0.
- Family ceiling 353/1000: an upper bound on every lower constant produced by this specific scalar majorant family as T varies. This is not an upper bound on the true complement coercivity.
- Required scalar coercivity: the reciprocal of the obstruction vector's certified upper bound on Q(v)/R(v). Every scalar inverse bound that makes G_beta positive must have coercivity larger than this necessary value. It is not sufficient by itself.
- 48-moment complement: the actual lawful native complement after physical degrees 0..47 are removed at a=14/25; its certified physical lower bound is 3/5 and logarithmic lower bound 9/100.
- Factor 5/3: sufficient inverse bound for the 48-moment complement. It cannot be applied to the 36-source Gram or the 36-vector projection.
- Once-rounded interval dot: exact integer accumulation of a rational polynomial's linear combination of fixed-grid moment intervals, followed by one outward rounding.

Full-source pairing custody at dimension 36 is closed; the 48-vector matrix, all 48 sources, matching residual Gram and corrected sign are not yet certified. Whole-domain positivity remains certified at a=11/20. Global endpoint exclusion, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean is unchanged.
