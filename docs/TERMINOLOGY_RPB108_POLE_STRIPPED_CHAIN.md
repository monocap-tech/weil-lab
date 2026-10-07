# RPB108 terminology: pole-stripped actual derivative chain

Introduced 2026-10-07 UTC, global/F4 lane. Historical notation is unchanged.

- A_a: physical self-adjoint operator of the complete actual native form on I_a.
- H_a: its pole-free operator E0-T_a; not the bounded correction B_a from ACTUAL_LOG_OPERATOR_ATTACHMENT. H_a is called B_a in CRITICAL_RECIPROCAL_PROMOTION.
- c_a(x)=cosh(x/2), s_a(x)=sinh(x/2), restricted to I_a.
- C(u)=integral c_a(x)u(x)dx, S(u)=integral s_a(x)u(x)dx: complex-linear actual pole moments. P_a u=2c_a C(u)-2s_a S(u).
- K=ker A_a, r=dim K; F_j=K intersect global H^j, the already proved exact Sobolev flag.
- Z=K intersect ker C intersect ker S=K intersect ker H_a: the actual pole-annihilated null subspace.
- L_p=D^2-1/4: the pole-annihilating differential map, used only on F_2 so its output is supported physical L2 and in K. It is not a bounded operator on K, a change of window, or same-vector transport.
- Active pole moments: (C,S)|_K is nonzero. Inactive pole moments: both vanish identically on K. This is a proved dichotomy, not an assumed nonvanishing condition.
- q=eta^2: squared angular Fourier frequency. psi_0(q)=m0(eta/(2pi))-m0(0), the archimedean complete Bernstein function. Phi_a(eta)=psi_0(eta^2)+2sum w_n[1-cos(eta log n)] is the full pole-free jump exponent. Its constant mass shift is omitted only for this exponent test.
