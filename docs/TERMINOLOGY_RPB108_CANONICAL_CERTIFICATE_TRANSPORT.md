# Canonical certificate transport — first formalization pass

`WeilDefect.CanonicalCertificate` is the namespace for the algebraic consumer
of RC23/RC36 certificate bounds. Definitions precede their load-bearing use:

- **Quadratic evaluation:** a scalar obtained by evaluating a form on one
  arbitrary coefficient vector. A matrix entry is not a quadratic evaluation.
- **Whole quadratic error bound:** an absolute difference bound valid for
  every coefficient vector, scaled by its Euclidean squared norm `n`.
- **Source residual:** the complete residual of an attached trial source;
  its bound cannot be replaced by a finite-test or sampled bound.
- **Common Schur reserve:** a constant `δ` bounding the quadratic form below
  by `δ` times the sum of the squared norms of both sectors.
- **Checked diagonal-factor witness:** an exact equality `M = Lᴴ diag(d) L`
  together with nonnegative diagonal entries. The factor need not be
  triangular or invertible; zero diagonal entries are allowed.
- **Whole weak-residual representation:** an identity between the canonical
  Riesz-error pairing and a physical residual pairing for every vector of
  the complete supported carrier. Galerkin stationarity alone is insufficient.

The scalar algebraic consumer does not authenticate analytic attachment,
matrix enclosures, support, or the infinite complementary estimate. Those
are explicitly supplied hypotheses; no physical or canonical domain is
identified by this namespace.

## LF04 additive definitions

- **Log-metric spectral product:** the exact product of `log(exp 1 + |ξ|)`
  with the physical vector's Fourier transform. Its physical L2 membership
  is stronger than the existing one-logarithm form energy condition.
- **Spectral log-metric physical source:** inverse Fourier transform of that
  L2 product. It represents the metric pairing on the whole supported carrier.
  Equality with RC24's compressed jump-density formula is a separate obligation.

## LF05 additive definitions

- **Metric jump density:** RC24's exponentially damped Poisson-mixture
  density, intended for strictly positive jump distance.
- **Endpoint tail:** its integral beyond the positive distance to one endpoint.
- **Two-tail exterior source:** the sum of the left and right endpoint tails.
- **Endpoint source candidate:** the constant, internal-difference and two-tail
  terms in RC24's physical formula. It is a function definition, not yet a
  proved L2 representative or identified spectral source.
- **Whole weak limit attachment:** convergence of physical sources in L2
  together with convergence of their whole test pairings to the canonical
  metric. The limit then represents every test pairing.

## LF06 additive definition

- **Damped logarithm integrand:** `exp(-b*t) * (1-exp(-s*t))/t` for
  positive damping b and nonnegative frequency s. Its improper integral
  over positive t is intended to equal `log((b+s)/b)`. LF06 proves an
  exponential domination bound and submits the Frullani specialization.

## LF07 additive definitions

- **Damped inverse-transform integrand:** the complex exponential with real
  decay `-t*|ξ|` and phase `w*ξ`, where t>0 and w is angular frequency.
- **Normalized Poisson density:** `2*t/(t^2 + 4*pi^2*x^2)`, obtained when
  the angular frequency is `2*pi*x` in the project's inverse transform.

## LF08 additive definition

- **Poisson mass budget:** actual integrability, positivity and exact unit
  integral of the normalized physical Poisson density. Its absolute integral
  is also one. This concerns the full real line; finite-cap compression still
  loses exterior mass and retains both endpoint contributions.

## LF09 additive definitions

- **Off-diagonal jump convergence:** integrability of the actual defining
  time integral at every strictly positive jump distance. Cauchy domination
  supplies this convergence, independently of totalized integral conventions.
- **Conservative jump majorant:** `ell(r) <= 1/r` for r>0, using the full
  undamped Cauchy integral. This deliberately loses the half-line factor.
- **Pointwise Lipschitz cancellation:** the bound
  `norm((v(x)-v(y))*ell(abs(x-y))) <= L` under the explicit modulus
  `norm(v(x)-v(y)) <= L*abs(x-y)`, including the zero difference on the
  diagonal. Measurability and integral convergence in the spatial variable
  remain separate obligations.

## LF10 additive definition

- **Finite-cap internal jump budget:** for a measurable trial with modulus
  `norm(v(x)-v(y)) <= L*abs(x-y)` on y in [-B,B], the actual cancelled
  spatial integrand is integrable there. For B>=0 its integral has norm
  at most `2*B*L`. This budget controls the internal-difference term only;
  both exterior tails are retained in the endpoint candidate.

## LF12 additive definitions

- **Damped spatial far-tail budget:** `ell(r) <= C/r^2`, where
  `C = 1/(2*pi^2*exp(1))` and r>0. It comes from integrating the actual
  time damping against the spatial denominator lower bound.
- **Positive-distance endpoint budget:** genuine convergence of each
  tail beyond d>0, with `tail(d) <= C/d`. Both exterior contributions
  are therefore bounded at interior points. This coarse reciprocal-distance
  bound does not establish endpoint L2 integrability.

## LF13 additive definition

- **Logarithmic endpoint budget:** with `C=1/(2*pi^2*exp(1))`,
  `tail(d) <= C + abs(log(d))` for every d>0. Split at distance one,
  integrate the near-diagonal reciprocal majorant, and use the damped
  far-tail budget beyond one. Both endpoint contributions are bounded
  by the corresponding sum of absolute logarithms at interior points.
  Square integrability and spectral source identification are separate.

## LF19 additive definition

- **Endpoint candidate parameter measurability:** measurability of the moving
  positive-distance tail, both exterior contributions, the internal jump
  integral and the complete candidate for a measurable trial. This includes
  totalized integral values and does not establish convergence, square
  integrability, weak attachment or spectral source identity.

## LF21 additive definitions

- **Squared-log distance majorant:** `log(d)^2 <= 16*(d^(-1/2)+d^(1/2))`
  for d>0. Both powers are integrable on each finite distance interval.
- **Endpoint-tail distance L2 membership:** `MemLp tail 2` under volume
  restricted to (0,D], D>=0, obtained from actual tail measurability and
  the logarithmic bound. Transferring this to the two physical cap endpoints,
  constructing the complete candidate in L2 and identifying its source
  action are separate obligations.

## LF22 additive definition

- **Physical cap candidate L2 membership:** actual L2 membership on the
  interior (-B,B) of both endpoint tails, their bounded-trial product and
  the complete endpoint candidate, for B>=0 and a measurable trial with
  a pointwise bound and Lipschitz modulus on [-B,B]. This is a function
  membership result; weak attachment, spectral identity and domain
  identification remain separate. Closed-cap null-endpoint transport
  and full-line zero extension are not yet invoked.

## LF23 additive definitions

- **Endpoint candidate zero extension:** the indicator of [-B,B] times
  the actual endpoint candidate; zero outside the cap.
- **Endpoint candidate physical L2 representative:** the full-line L2
  equivalence class constructed from the proved zero-extension membership
  for bounded measurable Lipschitz trials. The class agrees almost
  everywhere with that formula. This is not yet the spectral source or
  a weak representative of the logarithmic metric. Endpoint null-set
  transport does not prove convergence of the endpoint improper integrals.

## LF24 additive definition

- **Exterior half-line tail identification:** the actual spatial kernel
  integral over y>B equals tail(B-x) when x<B; the integral over y<-B
  equals tail(B+x) when -B<x. Translation and reflection preserve volume.
  These are the two geometric exterior pieces of the jump operator; its
  complete zero-extension split and source attachment remain separate.


## LF29 additive terms — actual trial jump

- `neutralLogMetricTrialZeroExtension B v`: the trial `v` on the closed cap
  `[-B,B]` and zero elsewhere. This differs from LF23's zero extension of the
  endpoint source candidate.
- `neutralLogMetricTrialJump B v x y`: `(v(x)-v_zero(y))*ell(|x-y|)`;
  its full-line integral is genuinely convergent at interior `x` under the
  measurable cap Lipschitz hypotheses. The endpoint candidate is `v(x)` plus
  this integral. Spectral/Fourier source identity remains separate.
