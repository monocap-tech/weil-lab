# Terminology registry — GERM-82 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This supplement is read with [GERM-82](../notes/_recurrence82.md). Earlier
matrix names and historical records are not changed.

## Parameter and inherited names

Retain `t=e-e80`, `sigma=sigma8`, `psi=psi7`, `rho=rho9=psi-3sigma`,
and `c=c10=sigma-rho`. The new exclusion range is `sigma<t<=psi`.
The existing residual `nu8=psi7-sigma8=chi7-2psi7` is the endpoint increment;
it is not a new length or a new return section.

The symbols A0, A1, B0, B1, U0, U1, V0, and V1 below mean the
**GERM-81-local** matrices. They are not earlier matrices with the same labels.

## Terminal internal-visit count and complete ninth words

For a first return from `(0,sigma)` to itself under the eighth rotation,
let n be its return time (3 or 4), and s the number of final consecutive
intermediate eighth sources below t. The initial source always uses A1.
The full chronological word is A1, followed by n-s-1 B0 maps, then s B1 maps.

Define the **GERM-82 ninth word** by
```math
N_{s,n}=B_1^s B_0^{n-s-1}A_1,
\qquad n\in\{3,4\},\quad 0\le s<n.
```
There are seven such words. This definition includes all intermediate
source bits, not merely the first and last bits.

## Direct ninth-return cone chart

The **GERM-82 chart** is
```math
C_{82}=\begin{pmatrix}1&-1\\-12/5&21/10\end{pmatrix},
\qquad \det C_{82}=-3/10.
```
The positive representative of N_(s,n) is its conjugate multiplied by +1
when s=n-1 and by -1 otherwise. The actual signs stay in the source equation.
The certified factor 7/2 is per complete ninth return, not per original
rotation step, not a global kernel gap, and not a tenth-return certificate.

## Next eighth species

For `t>psi7`, the new chronological seventh word V1,U0,U1 has matrix
`J8=U1 U0 V1`. This is a new GERM-81-local eighth branch; using the same
letters does not identify it with the similarly written GERM-77 guard.
Its activation is recorded, but GERM-82 proves no exclusion above t=psi7.
