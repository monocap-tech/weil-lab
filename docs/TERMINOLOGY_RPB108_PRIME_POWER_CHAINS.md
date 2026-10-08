# RPB108 prime-power chain dictionary

Introduced with NF62, 2026-10-08.

- **Prime-power chain**: the physical points r+j log(p) inside an interval of length 2a, with r chosen modulo log(p). Its maximum almost-everywhere number of points is m_p=ceil(2a/log(p)). Endpoint-only points do not add a node.
- **Prime chain matrix**: the m_p by m_p real symmetric matrix with diagonal zero and entry log(p) p^(-|i-j|/2) off the diagonal. It represents ALL active powers of that prime, both orientations, on the longest chains.
- **Chain prime budget**: the sum over primes p<exp(2a) of the largest eigenvalue of their prime chain matrices. It bounds the complete original prime operator by summing across different primes. It is not the existing, stronger joint weighted-Schur bound.
- **Negative pole allowance**: 2(sinh(a)-a), the exact magnitude of the negative eigenvalue of the original rank-two physical pole operator. The positive eigenvalue is retained, rather than called negative loss.

These are physical operator/form bounds. In the NF61 derivative carrier they become bounds relative to the primitive mass operator M_a; they do not become strict source-gain bounds.
