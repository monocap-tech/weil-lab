# RPB108 uniform critical rank terminology

CC31, 2026-10-08. Complete original normalized Q=P*P-N*N.

- **Fixed-cap Garding constants:** alpha_B>0 and kappa_B>=0 such that
  Q(h)>=alpha_B||h||_D^2-kappa_B||h||_2^2 on the complete D_B.
  This uses the original native form, not an old positivity margin.
- **Positive analysis upper constant:** U_B with ||Ph||<=U_B||h||_D
  on D_B. The existing lower observability constant is c_B>0.
- **Low-frequency Gram:** Z_R=F_R*F_R on D_B, where F_R takes the
  physical Fourier transform restricted to [-R,R]. Fourier frequency
  uses exp(-2pi i xi x); tr Z_R<=4BR.
- **Cap protected space:** the finite spectral subspace of Z_R above
  alpha_B/(4 kappa_B), when kappa_B>0. Its orthogonal complement has
  original Q>=alpha_B||h||_D^2/2. It is not an actual source prefix.
- **Uniform critical rank:** d_B bounds rank E_s on EVERY old strictly
  positive s<=B for the cap-only band eta_B defined in the report.
- **Scalar critical residual bound:** for each unit critical eigenvector,
  ||M_t^(-1/2)J_i*||^2<=b_B lambda_i omega_B(delta_i), with the entire
  D_t and protected positive metric retained. This is not a bound for
  individual zero rows, or a finite physical trial norm.
- **Coherence factor:** positive Gram matrices with d rows satisfy the
  diagonal-to-operator estimate with loss at most d. The factor is sharp.

These definitions do not assert that the scalar arithmetic bound holds.
Uniform critical rank bounds multiplicity, not leakage or positivity.
