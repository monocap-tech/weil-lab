# RPB108 Gaussian edge split terminology

First load-bearing use: GAUSSIAN_EDGE_SPLIT_20261006. Historical definitions are unchanged.

- **Hard endpoint test split**: g_R^in=1_[-a,a](K_R*h), with the exterior part defined by subtraction. The interior part is a canonical logarithmic-domain test; it need not be H1.
- **Actual exterior action**: integral_{|x|>a} q_h(x) conjugate(K_R*h)(x) dx, with q_h=m_a(D)h+p_h and the unchanged full actual cutoff and signed pole.
- **Adjacent-step control**: h=1_[a-1,a], q=-1_[a,a+1], a>=1/2. Here q is an independently assigned residual control, not the actual native residual of h.
- **Touching-support Gaussian pairing**: the pairing across an endpoint with no fixed positive gap. It is not the separated far-field action.
- **Edge cancellation target**: the actual exterior action's weighted signed partial sums with weight n^(3/2)/log(e+n) have finite liminf basiswise on the full kernel. This remains an unproved endpoint-exclusion theorem.
