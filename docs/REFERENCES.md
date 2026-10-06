# References

This is the working bibliography for the public Weil-defect project.

A reference being listed here does not imply that every nearby theorem is imported from it. Exact load-bearing locations are recorded separately in [Imported Source Pins](IMPORTED_SOURCE_PINS.md).

## Foundational / finite-truncation background

### Enrico Bombieri

*Remarks on Weil's quadratic functional in the theory of prime numbers, I.*

Rendiconti Lincei, Serie 9, **11** (2000), 183–233.

https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0

Load-bearing pins currently used:

- Lemma 10, p. 210 — multiplicity-null directions;
- Theorem 8, p. 213 — finite negative-index count;
- equation (7.7), p. 204 — matrix/kernel decay context; after H1-P4.2 this is no longer load-bearing for WD-T28.

## Operator factorization

### R. G. Douglas

*On majorization, factorization, and range inclusion of operators on Hilbert space.*

Proceedings of the American Mathematical Society **17** (2), 413–415 (1966).

DOI: 10.1090/S0002-9939-1966-0203464-1

https://doi.org/10.1090/S0002-9939-1966-0203464-1

Load-bearing pin:

- Theorem 1 — range inclusion / majorization / factorization equivalence and reduced solution.

## Zeta zero counting

### E. C. Titchmarsh; revised by D. R. Heath-Brown

*The Theory of the Riemann Zeta-function*, 2nd ed.

Oxford University Press, 1986.

Public scan used for source pinning:

https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf

Load-bearing pin:

- Chapter IX, Theorem 9.2, equation (9.2.1), p. 211:
  ```math
  N(T+1)-N(T)=O(\log T).
  ```

## Compact-window explicit formula

### Xuefeng Zhu

*Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law.*

arXiv:2608.24827v2 (2026).

https://arxiv.org/abs/2608.24827

Load-bearing pins:

- equations (2)–(3), p. 2;
- support convention $\log n<2L$.

## Special-function asymptotics

### NIST Digital Library of Mathematical Functions

§5.11(i), equation 5.11.2.

https://dlmf.nist.gov/5.11.E2

Load-bearing pin:

```math
\psi(z)\sim\log z-\frac1{2z}-\cdots.
```

## Operator-theoretic context

### Masatoshi Suzuki

*Weil's quadratic form via the screw function.*

arXiv:2606.09096 (2026).

https://arxiv.org/abs/2606.09096

Currently contextual/non-load-bearing for the stable theorem statements.

## Shorted operators / Schur complements

### W. N. Anderson, Jr. and G. E. Trapp

*Shorted Operators. II.*

SIAM Journal on Applied Mathematics **28** (1975).

https://doi.org/10.1137/0128007

Currently contextual for the general shorted-operator extension. The stable WD-T13 statement is restricted to the strictly positive/invertible-block Schur-complement setting and does not require the general theorem.


## Dagger geometry / formal adjoints

### Jón Hákon Garðarsson and Paolo Perrone

*Dagger Categories in Riemannian Geometry.*

arXiv:2610.02257v1 (2026).

https://arxiv.org/abs/2610.02257

Relevant results:

- Theorem 5.8 — classification of daggers on finite-dimensional vector spaces by scalar involution and unimodular Hermitian forms;
- Proposition 6.16 — for an isometry, the orthogonal complement is the isometric kernel of its dagger;
- Theorem 7.8 — extension to finitely generated projective modules;
- Theorem 13.3 — classification of daggers on differential operators by metric-divergence structures, acting as formal adjoints;
- Propositions 13.7 and 11.12 — metric and divergence are independent data.

**Status:** contextual/non-load-bearing for the current RPB theorem DAG. In particular, the paper explicitly allows indefinite forms and does not supply the positive-energy/coercivity step required by WD-T10/F-4. See the [RPB-108 dagger-geometry interface audit](../notes/REFLECTED_PACKET_BRIDGE_108_DAGGER_GEOMETRY_INTERFACE_AUDIT_20261005.md).

## Citation policy

The public project distinguishes:

- imported source theorem;
- exact specialization;
- internal proof;
- derived reduction;
- conditional morphology theorem;
- computational evidence;
- open interface.

Exact source pinning and internal proof verification are separate audit steps.
