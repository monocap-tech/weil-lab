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

## Contemporary Suzuki/event-cell and Weil-sign research — contextual leads (2026-10-28 review)

### Rainer Andreas Mittermeier

*Compact Weil Event Cells from Suzuki's Screw Function: Parity Polarization, Exact Enclosures, and Uniform Gram Certificates.*

- Version 1, **2026-09-10**: https://doi.org/10.5281/zenodo.22687244
- Version 2, **2026-10-25**: https://doi.org/10.5281/zenodo.23603376
- Both deposits list separate PDF and reproducibility ZIP files.

Public abstract claims: scalar Suzuki screw-function polarization into even/odd finite Gram kernels, prime-power event-cell enclosures and fixed-window realization, continuous-family finite matrix certificates and positive-core Schur diagnostics. Version 2 reports a 16-node even family at half-support L=0.8 with normalized row margins above 0.2109; it explicitly **does not** certify global Weil positivity or RH. No page-specific theorem, computation or program has been independently replayed in Weil-Lab.

**Status: CONTEXTUAL / EXTERNAL LEAD, NOT LOAD-BEARING.** No imported theorem ID; no claim of mathematical equivalence to the original signed Fourier J242/NF376 exterior response. September v1 precedes our October operator investigations. The separate comparison/verification docket is [External Mittermeier Source Audit](EXTERNAL_MITTERMEIER_SOURCE_AUDIT_20261028.md).

Related preprints by the same listed author, also **CONTEXTUAL / NOT LOAD-BEARING**:

- *A Conductor-23 Operator Architecture for the Riemann-Weil Problem: Positive Hilbert Host, Arithmetic Observability, Common Form Domain, and Limits of Sign Transfer*, version 3 (2026-10-25): https://doi.org/10.5281/zenodo.23137105. Public abstract explicitly reports no sign-preserving Weil comparison.
- *Recovery-Selected Weil Rectangles: Exact Prime-Power Dynamics and the Global Positivity Problem*, version 2 (2026-10-25): https://doi.org/10.5281/zenodo.23635192. Public abstract reports global viability criteria and unresolved sign transfer; neither is an infinite-tail positivity certificate.

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
