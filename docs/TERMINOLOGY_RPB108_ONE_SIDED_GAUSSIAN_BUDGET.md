# RPB108: one-sided Gaussian logarithmic mass budget

Registered: 2026-10-06, before the associated theorem's first load-bearing use.
Source base: 4d65dd0898806f31f0389fd6542cbbc525d01334.

For a supported physical L2 vector h, use the mathlib Fourier convention
F(xi)=integral h(x) exp(-2 pi i x xi) dx.
For integers n>=1 define
  M_n(h)=integral exp(-(2 pi xi-n)^2/n)|F(xi)|^2 dxi.
These are the existing project moving-Gaussian masses sampled at R=n, not new observations or changed Fourier normalization.

For nonzero h put H=||h||_2 and define its one-sided Gaussian logarithmic mass budget by
  sum_(n>=1) log(H^2/M_n(h))/(1+n^2).
Each summand is nonnegative because 0<M_n<=H^2. The associated note proves finiteness for every nonzero compactly supported L2 h, without any null equation.

A divergent decay profile is a sequence omega(n)>=0 for which
  sum omega(n)/(1+n^2)=infinity.
An eventual upper bound M_n<=C H^2 exp(-omega(n)) with such a profile contradicts the finite budget. This does not give a pointwise lower bound on M_n or an injective single scalar boundary moment.

The profile used for the actual endpoint criterion is omega(n)=n/log(e+n).
No renamed kernel, historic packet or same-vector transport is defined by this criterion.
