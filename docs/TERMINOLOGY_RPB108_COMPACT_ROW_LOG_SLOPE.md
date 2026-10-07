# RPB108: compact rows at the logarithmic height scale

Date: 2026-10-07 UTC. Additive definitions.

- Actual K, kappa_R, A_tau and S_K retain the full-native definitions. L_tau=log(1/tau).
- q=2^16, H_j=q^j, c_j=H_j^(-1/2), j>=1, are CONTROL heights and amplitudes, not actual zero locations.
- f(x)=max(1-16|x-1/8|,0) is the supported triangle. h=f sum_j c_j exp(-iH_j x) is one unchanged physical control vector.
- B=3/8. The artificial rows have locations (theta,beta)=(+/-H_j,+/-B), with all four sign partners counted as norm weights, not independent observations.
- P=integral f cosh(Bx), N=integral f sinh(Bx), Delta=P^2-N^2>0.
- Artificial A_tau^art and S^art use those rows only. They are NOT the actual Q/source dictionary. A positive native Q(h) is compatible with these artificial observations.
- A fixed finite packet contribution means a finite sum of actual source energies weighted by alpha_tau(|theta|). Alpha_tau(u)<=u bounds it independently of tau. No finite complete physical realization is inferred.

The control distinguishes nonzero logarithmic growth from the older control's mere critical divergence.
