# RPB108 terminology: signed cutoff source moment

Date: 2026-10-07 UTC. Additive endpoint-exclusion definitions.

- r is a source height order, 0<r<2, not kernel dimension.
- J_(epsilon,r)(theta)=integral_epsilon^t0 (1-cos(theta t)) t^(-1-r) dt is a bounded nonnegative ordinate multiplier at each epsilon>0.
- I_(epsilon,r)(h)=sum_q J_(epsilon,r)(theta_q)(|p_q(h)|^2-|n_q(h)|^2) is the signed cutoff source moment. Its two sums are finite at fixed epsilon. Taking this difference before sending epsilon to zero is mandatory.
- I_(epsilon,r)^K is the sum over a physical L2 orthonormal basis of the whole actual kernel. It is basis independent, and retains all actual divisor copies.
- E_h, R_h, B_QRH=3/8, K_a and the existing positive/negative fractional source moments retain their meanings from the preceding registries.
- Signed cutoff here integrates over translation scale; it is not a sharp height cutoff, a prescribed retained selection or an effective-background coordinate.
