# RPB108: physical translation scale and two-vector compression

Additive definitions, 2026-10-07. For an actual contact vector h with c=kappa_R(h)!=0, put

    D_mass(t)=||h||_2^2-Re<h,tau_t h>_L2
             =||tau_t h-h||_2^2/2,
    V_mass(R)=integral_(|xi|>R)|hhat(xi)|^2 dxi,
    W_tail(R)=integral_(|xi|>R)w(xi)|hhat(xi)|^2 dxi.

Here hhat uses the canonical unitary 2pi-frequency convention and w(xi)=log(exp(1)+|xi|). These are PHYSICAL Fourier quantities, not original divisor-copy source tails. No source normalization is changed.

For a real terminal vector h of definite reflection parity, lambda_sum(t) and lambda_difference(t) are the physical mass-normalized eigenvalues of Q compressed to span{h,tau_t h}. They are not asserted to be eigenvalues of the full enlarged operator. The trials change the physical vector and can be simultaneously centered to fit aperture a+t/2.
