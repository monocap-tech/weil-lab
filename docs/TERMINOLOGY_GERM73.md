# Terminology registry — GERM-73 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This supplement is read with [the GERM-72 correction](../notes/_recurrence72_correction.md) and [GERM-73](../notes/_recurrence73.md). Historical records are not rewritten.

## Residual lengths and scope

Retain the residual lengths
```math
\alpha=\tau-3\theta,\qquad
\beta=\theta-\alpha,\qquad
\gamma=\alpha-\beta.
```
Here beta and gamma are residual lengths, not the prime-weight coefficients carrying the same letters in earlier notes. Write
```math
e=3h-\theta+\varepsilon,\qquad 0<\varepsilon\le\beta.
```
The exact new arithmetic bound is
```math
49\gamma<10\beta<50\gamma.
```

## Corrected third-section library

On the theta-circle, the map is `v -> v-alpha mod theta`. The chronological second-section words are:
```text
A3: 01-, 11+, 10+
Q3: 01-, 11+, 11+
P3: 11-, 11+, 11+, 10+
D3: 01-, 11+, 11+, 10+
```
The A3 and D3 definitions in GERM-72 are superseded, not silently reused. Products act rightmost first.

## Fourth-section words

The fourth section is `alpha<v<theta`; its coordinate is `w=v-alpha`, of length beta. Its physical location in the original W-coordinate is `(h-beta,h)`.
```math
\mathcal A=D_3A_3,\quad
\mathcal O=D_3^2A_3,\quad
\mathcal J=D_3P_3Q_3,\quad
\mathcal E=P_3Q_3.
```
These are complete fourth-section return matrices. Their exact domains are part of the proof. The elliptic matrix E is not required to expand individually.

## Fifth return section

For `gamma<epsilon<=beta`, use `0<w<gamma`. Physically this is `(h-beta,h-beta+gamma)`. Put
```math
\xi=5\gamma-\beta,\qquad 0<\xi<\gamma.
```
A return takes N=4 steps for `0<z<xi` and N=5 for `xi<z<gamma`. The induced map is
```math
z\mapsto z+(\beta-4\gamma)\pmod\gamma.
```
The nine complete words are
```math
\mathcal B_{s,N}=\mathcal E^s\mathcal A^{N-s-1}\mathcal J,
\quad N\in\{4,5\},\quad 0\le s<N.
```
The cone chart is `[[1,-1],[6,-10]]`. Its factor 2 is per complete fifth return, not per original rotation step.

## Next internal-wrap species

Immediately above epsilon=beta, a third-section wrap may remain inside the overlap:
```math
I_3=(E_2^+)^3E_2^-.
```
This is a scoped next-interface observation, not a new closure theorem.
