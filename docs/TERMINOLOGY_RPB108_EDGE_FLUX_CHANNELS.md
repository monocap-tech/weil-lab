# RPB108 edge-flux channel terminology

Base: 1ef926fcd11525c80395beac0560ddfc8920b245. Registered with first use.

- Right-edge profile: f(v)=h(a-v) on (0,2a), zero elsewhere; it is an L2 profile, not an endpoint trace.
- Singular edge-flux channel: the real pairing of the half-Carleman exterior action with f(t-u), with coefficient 1/2 retained in the total flux.
- Remainder edge-flux channel: the same pairing with k(s)-1/(2s); Hilbert-Schmidt compactness does not assert critical integrability.
- Strict interior prime echo: a frozen term with log(n)<2a, reading f(log(n)-u) in a strict interior interval for small u.
- Opposite-edge threshold echo: a frozen term with log(n)=2a, reading f(2a-u)=h(-a+u). Threshold equality remains included.
- Real reflection parity sector: real h satisfying h(-x)=sigma h(x), sigma=+1 or -1. At least one such sector contains a nonzero null vector if the full real-kernel form has any nonzero complex null vector. This is a reduction, not a sign or existence theorem.
- Collective critical flux cancellation: integrability of the absolute signed sum Pole-Singular/2-Remainder-Prime against dt/t^2. Individual channel norm bounds do not establish it.

The channels use the actual frozen source at the unchanged aperture. No enlarged null equation, actual trace, nonzero null existence or closure flag is inferred.
