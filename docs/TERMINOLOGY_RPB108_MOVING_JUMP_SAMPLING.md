# RPB108: moving-jump whole-domain sampling

Additive definitions, 2026-10-07. Retain Q, D_a, K, Phi, u_t, d_t, c_t, H_Q and the physical gauge Pi from PICK_CYCLIC_COMPLETION.

For an interior point xi, k_w^xi is the same-window jump-minus-one test solving

    (D+iw)k_w^xi = exp(iw xi)h_*/Phi(w)-delta_xi.

Its Fourier profile is i[exp(iw xi)Phi(z)/Phi(w)-exp(iz xi)]/(z-w). These are supported physical tests. Moving xi is not translation of the window or a change of source arithmetic.

The whole-domain sampling measure is nu_Phi=sum_(Phi(t)=0)c_t delta_t, with c_t=d_t/|Phi'(t)|^2. Its nodes are the real zeros of the hypothetical contact GENERATOR. They are not identified with actual zeta zeros.

The sampling map T_Phi f=(sqrt(c_t)F_f(t))_t is an isometry from H_Q onto the sequence space at these nodes. It annihilates K. The complete actual zeta analysis Gamma remains a different map and observes K; its source lift retains Gamma(P_K f).

The theorem is conditional on nonnegative actual contact. For the actual lowest positive eigenspace its counterpart is sampling of Q_mu=Q-mu physical mass, and Q retains the additional mu mass term.
