# RPB108 quadratic gain spectral split terminology

Registered 2026-10-06 before the companion theorem.

- `E=ker D(c)`, `r=dim E>0`: finite coefficient space of an actual nonnegative contact, isomorphic to its full native kernel by `B_c=-G_c^-1 R_c*`.
- `Ereg=B_c^-1(K_c intersect global H1)`, `d=dim Ereg`: regular coefficient subspace; `d<=r-1`.
- `Gamma_s=Pi_E[Lambda(c+s)-Lambda(c)]Pi_E/s^2`, regarded as an operator on E: positive normalized gain increment. The ambient selected carrier may be larger than E.
- `lambda_1(s)<=...<=lambda_r(s)`: eigenvalues of Gamma_s, counted with multiplicity. These are finite response eigenvalues, not physical native eigenvalues.
- `W=Ereg^perp intersect E`: fixed rough complement, not all of E minus Ereg.
- `D_w(s;h)`: nonnegative weighted Fourier translation defect from QUADRATIC_GAIN_REGULARITY; distinct from the finite source defect D(c).
- `M_s(h)`: full exterior residual collar mass from COLLAR_GAIN; both collars and all native terms retained.
- Sequencewise bounded gain: finite liminf of e_s(h)/s^2. This allows a vector-dependent sequence and does not assume an O(s^2) bound for all sufficiently small s.
- Total normalized gain trace: trace_E Gamma_s, a sum over the full finite null coefficient space, not a single inverse-boundary observable.
