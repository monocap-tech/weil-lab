# Terminology registry — GERM-85 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with GERM-84 and [GERM-85](../notes/_recurrence85.md). Historical definitions and the GERM-72 correction remain unchanged.

## Excess parameter and eleventh residuals

Retain `b=e-e83`, `rho9=psi7-3sigma8`, `c10=sigma8-rho9`, and `omega10=sigma8-10c10`. Define
```math
\varepsilon=b-\rho_9=e-e_{84},\qquad
c_{11}=c_{10}-\omega_{10},\qquad
\omega_{11}=c_{10}-4c_{11}.
```
GERM-85 certifies `4c11<c10<5c11`, hence `0<omega11<c11`. Its new exclusion domain is `0<epsilon<=c10`. This closes the current eighth formula window, not the larger original three-layer interval.

## GERM-85-local tenth maps

P/Q/R/S in these definitions are **GERM-84-local**. The following U/V labels are **GERM-85-local tenth maps**, not the older seventh matrices:
```math
V_0=S^8RQ,\quad V_1=S^9Q,\qquad
U_0=S^9RQ,\quad U_1=S^{10}Q.
```
V denotes the tenth wrap from `0<y<c11`; U the nonwrap from `c11<y<c10`. The subscript is the source bit relative to `(0,epsilon)`.

The next-branch guard in GERM-85 separately uses **GERM-81-local seventh** U1 and V1. That guard is not a product of the new tenth maps.

## Eleventh section and signed cone chart

The eleventh section is `K11=(0,c11)` in the tenth coordinate, with physical observation `W(t0+y)` and `t0=h-beta+gamma-xi+2eta7`. Its first-return map is
```math
y\longmapsto y+\omega_{11}\pmod{c_{11}}.
```
Returns take four or five tenth steps. Eleven distinct words arise across four low-parameter and nine high-parameter cells, with two shared words. The common chart is
```math
C_{85}=\begin{pmatrix}1&1\\-53/25&-199/100\end{pmatrix}.
```
Its estimates apply per complete eleventh return, not per original rotation step or to either elliptic tenth map individually.
