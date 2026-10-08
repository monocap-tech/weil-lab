# RPB108 pre-contact shadow terminology

This registry is additive; historical definitions and wording are unchanged.

- **Shadow front:** `research/rpb108-precontact-shadow`, independent of the aperture and Global/F4 fronts. Its first publication is PS1, not NF56.
- **Fixed carrier:** H=D_1 with squared norm E_log(f)=integral log(e+|xi|)|fhat(xi)|^2 dxi. U_a f(x)=a^(-1/2)f(x/a) is physical mass-unitary dilation.
- **Form operator:** A(a), the bounded H-Riesz operator of Q_a(U_a f,U_a g). A(a)=I+compact. It is not the physical operator.
- **Physical operator:** L(a), the self-adjoint operator associated to that form in physical L2. Its resolvent is J(A(a)+beta J*J)^(-1)J*. M=J*J is the physical mass form on H.
- **Canonical margin:** delta_a=inf Q_a(U_a f)/||f||_H^2. At a=1 the published conservative certificate gives delta_1=2e-34 as a lower bound, not the exact infimum.
- **Physical bottom:** mu_a=inf Q_a(h)/||h||_2^2. This is not delta_a.
- **Complete channels:** P_a,N_a use the existing normalized full actual divisor dictionary, all multiplicity copies and both signed channels, with Q=||P||^2-||N||^2. The earlier unnormalized partner-copy difference is 2Q; it must be divided by two before this dictionary is used.
- **Shadow cluster:** the r physical modes approaching the zero kernel of a provisional first contact, with spectral projection Pi_a. Aligned frames need not be individual eigenvectors.
- **Complete source Gram:** S_a=P_a(V_a)*P_a(V_a) in a physical orthonormal cluster frame V_a; E_a=V_a*L(a)V_a. The exact negative Gram is S_a-E_a.
- **Effective form budget:** omega(a,b), an explicitly evaluable upper bound for ||A(b)-A(a)||. Failure of its sufficient inequality is not a lower bound on the actual perturbation.

All new infinite-dimensional deductions in PS1 are written analytic proofs. Its checker audits finite rational algebra and conservative scalar budgets only. No new Lean certificate, actual zero computation, global positivity or RH theorem is claimed.
