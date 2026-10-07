# RPB108: transverse second count and weighted negative sampling

Date: 2026-10-07 UTC. Additive definitions.

- Z2(T)=sum_(actual copies,|theta_rho|<=T) beta_rho^2 counts transverse displacement with multiplicity. It is a divisor-location sum, not a positive/negative source energy of a physical vector.
- N(sigma,T) in the external density paper counts zeta zeros with Re rho>=sigma and 0<Im rho<=T. The paper's beta is Re rho; OUR beta_rho is the displacement Re rho-1/2 up to sign. These are different variables.
- eta>0 is a logarithmic saving parameter, unrelated to the aperture lane's source-error eta.
- Weighted negative analysis Nminus_eta h has coordinate n_rho(h)/sqrt((1+|theta_rho|)log(e+|theta_rho|)^eta). Its domain here is supported physical L2(-a,a). It is not the complete unweighted analysis N0, a height-positive critical moment, or an effective covariance.
- Negative sampling profile n_rho(h)=integral_(-a)^a h(x) exp(i theta_rho x) sinh(beta_rho x)dx uses the existing half-sum/half-difference raw normalization and multiplicity copies. Changing the negative sign convention does not change its norm.
- Hilbert-Schmidt custody refers to square summability of these WEIGHTED physical L2 observation norms. Removing the weights is not justified.
