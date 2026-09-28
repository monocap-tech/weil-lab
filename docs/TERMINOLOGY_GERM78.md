# Terminology registry — GERM-78 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with GERM-77 and the GERM-72 correction issued by GERM-73. Historical terms and records are unchanged.

## Retained parameter and section

Use `delta=e-e76`, not `e-e77`. Retain `psi7`, `chi7`, `nu8=chi7-2psi7`, and `sigma8=3psi7-chi7`. The seventh-map formula scope remains `0<delta<chi7`. GERM-78 proves exclusion on `psi7<delta<=2psi7`.

The eighth section remains the interval `(0,psi7)` in the seventh coordinate; its physical observation is `W(t0+z)`, with `t0=h-beta+gamma-xi+2eta7`. No new section or independent source coordinate is introduced.

## Internal-visit eighth words

The label records the return time followed by the interior bits of its intermediate sources. The initial source is always interior in this pass. Products act rightmost first.

| Label | Chronological seventh word | Matrix |
| --- | --- | --- |
| B(2;0) | V1,U0 | U0 V1 |
| B(2;1) | V1,U1 | U1 V1 |
| B(3;00) | V1,U0,U0 | U0^2 V1 |
| B(3;01) | V1,U0,U1 | U1 U0 V1 |

The verifier keys are `2/0`, `2/1`, `3/00`, and `3/01`. These labels do not replace the historical U/V map names.

## Cone chart and next word

The chart is
```math
C_{78}=\begin{pmatrix}1&5\\0&-40/3\end{pmatrix}.
```
The positive representatives are `-C78^-1 B C78`. Their common forward/backward factor is 3/2 per complete eighth return, not per original rotation step.

The next all-internal word B(3;11) is `V1,U1,U1`, with matrix `U1^2 V1`. It is a scope guard only; its admission above `delta=2psi7` is not covered by the present cone certificate.
