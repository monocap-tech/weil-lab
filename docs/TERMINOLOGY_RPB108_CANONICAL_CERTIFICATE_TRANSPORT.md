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
