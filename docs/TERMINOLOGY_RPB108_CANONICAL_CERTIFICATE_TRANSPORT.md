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
