# RPB-108 actual-divisor summability terminology

- Actual divisor: `NeutralActualZetaDivisorCoordinate`, whose coordinates
  include every actual open-strip zeta zero with its analytic multiplicity copies.
- Unit band: `neutralActualZetaDivisorUnitBand n`, the half-open
  absolute-height band with `floor(abs(Im rho))=n`. Bands uniquely partition
  the actual divisor and each is finite.
- Quartic height weight: `neutralActualZetaDivisorQuarticWeight q`,
  `1/(1+abs(Im rho(q)))^4`. This auxiliary scalar weight is not the
  logarithmic form-domain weight or a spectral operator-domain assertion.
- Coarse band count: one fixed `A>0` gives `card(band n)<=A(n+1)^2`.
  It follows from cumulative growth and does not assert local O(log n) density.
- Quartically bounded samples: a complex family `f(q)` with the explicit
  bound `norm(f(q))<=M*w(q)`. Actual summability of w is unconditional;
  deriving the analytic decay of a particular sample family is separate.

Definitions appear in the source before their first theorem use.
Certification and next cursor are recorded in
[the proof note](../notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_DIVISOR_SUMMABILITY_20261004.md).
