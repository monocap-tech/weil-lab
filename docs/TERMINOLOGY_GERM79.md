# Terminology registry — GERM-79 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with GERM-78 and the GERM-72 source-word correction. This registry does not alter historical records or ratify experimental dependencies.

## All-internal eighth-map library

Retain the seventh-coordinate lengths psi7 and chi7, the eighth return cut `sigma8=3psi7-chi7`, and `nu8=chi7-2psi7`. Set `a=delta-2psi7`, where `delta=e-e76`.

On `0<a<nu8`, the three eighth maps are
```math
A=U_1V_1,\qquad D=U_1U_0V_1,\qquad E=U_1^2V_1.
```
Their chronological seventh words are V1,U1; V1,U0,U1; and V1,U1,U1. E denotes the all-internal eighth return, not a new source coordinate or an unrelated extension operator. All three retain exact determinant one.

## Ninth-section remainder

Define
```math
\rho_9=\psi_7-3\sigma_8,\qquad
c_9=\sigma_8-\rho_9,\qquad
 a_{\max}=\psi_7-2\sigma_8=\sigma_8+\rho_9.
```
Here rho9 is a residual length, distinct from the earlier entry/exit determinant ratio rho. GERM-79 certifies `0<rho9<sigma8`.

The ninth section is `K9=(0,sigma8)` in the eighth coordinate, with physical field `W(t0+y)`, `t0=h-beta+gamma-xi+2eta7`. Its first return is
```math
y\mapsto y+\rho_9\pmod{\sigma_8},
```
with return time 3 for `y<c9` and 4 for `y>c9`.

## Complete ninth words and chart

With s counting the final consecutive E visits, the complete words are
```math
B_{s,n}=E^sD^{n-s-1}A,
\qquad(s,n)\in\{(0,3),(1,3),(0,4),(1,4),(2,4)\}.
```
Chronologically these start with A, followed by the compulsory D steps and then s E steps. The common chart is
```math
C_{79}=\begin{pmatrix}1&4\\-2&-23/2\end{pmatrix}.
```
Its signed-cone bounds apply per complete ninth return. The new exclusion scope is `0<a<=amax`, not the whole three-eighth-map formula scope. The next newly legal word is `E^2 A`.
