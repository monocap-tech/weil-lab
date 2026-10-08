# RPB108 critical flux limit terminology

CC29, 2026-10-08. Original normalized Q=P*P-N*N only.

- **Common source operator:** on a fixed cap B, extend T_B=N_B P_B^-1
  by zero off V_B. If Pi_a projects onto V_a, then
  A_a=T_B Pi_a T_B*. All A_a act on the same complete negative ambient.
- **Fixed critical band:** E_s=1_[1-eta,1)(A_s), with a cap-only
  eta in (0,1), on every old strictly positive window. A band shrinking
  arbitrarily with the old gap is not substituted for this projection.
- **Critical defect:** G_s=E_s(I-A_s)E_s, restricted to ran E_s.
- **Critical covariance:** L_st L_st*=E_s(A_t-A_s)E_s. It includes the
  entire positive-source shell, not a spatial strip or height prefix.
- **Vanishing modulus target:** L_st L_st*<=C_B omega_B(G_s), where
  omega_B is bounded and nonnegative on [0,eta], with omega_B(x)->0
  as x->0. Constants, band and positive admissible step are cap-only.
- **Power target:** omega_B(x)=x^alpha, any fixed alpha>0. For alpha<1
  it is weaker than bounded defect-relative reaction, though it still
  suffices for the first-contact exclusion argument in CC29.
- **Contact flux:** gamma_t=<y,(A_t-A_a)y>, for an actual unit contact
  output y with A_a y=y. It is positive for every t>a, conditionally on
  such contact existing. It is not a numerically evaluated zeta constant.
- **Expected old defect:** d_s=<y,(I-A_s)y>. This belongs to the same
  hypothetical contact vector y; it is not a physical coercivity margin.

The new argument is an endpoint sufficiency audit, not an actual estimate
of arithmetic critical covariance. Strict whole budgets and low output
remain necessary inputs for the earlier finite-step product proof.
