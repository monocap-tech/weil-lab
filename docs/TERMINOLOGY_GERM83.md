# Terminology registry — GERM-83 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with [GERM-83](../notes/_recurrence83.md) and the GERM-72 correction issued in GERM-73. Historical names and assertions are not rewritten.

## Parameter and scopes

Retain the residual lengths psi7, chi7, sigma8, rho9, c10 and nu8. Write
```math
t=e-e_{80},\qquad a=t-\psi_7=e-e_{82},\qquad
\nu_8=\psi_7-\sigma_8,\qquad
 a_{\max}=\psi_7-2\sigma_8=\sigma_8+\rho_9.
```
The new eighth formulas hold on `0<a<=nu8`; the GERM-83 exclusion covers only `0<a<=amax`. These are not identical scopes.

## GERM-83-local eighth maps

The symbols U_i and V_i retain their GERM-81 definitions. The following A, D, E are local to GERM-83, not identifications with earlier namesakes:
```math
A=U_0V_1,\qquad D=U_0^2V_1,\qquad E=U_1U_0V_1.
```
Their chronological seventh words are `V1,U0`, `V1,U0,U0`, and `V1,U0,U1`. A acts on the two-step eighth branch. D and E are the exterior-last-source and interior-last-source alternatives on the three-step branch. E is exactly GERM-82's newly required eighth word.

## Ninth words and retained chart

The ninth section remains `(0,sigma8)`, with physical observation `W(t0+y)` and `t0=h-beta+gamma-xi+2eta7`. Define
```math
N_{s,n}=E^sD^{n-s-1}A,
\qquad(s,n)\in\{(0,3),(1,3),(0,4),(1,4),(2,4)\}.
```
The rightmost factor acts first. The existing GERM-82 chart is retained exactly:
```math
C_{83}=C_{82}=\begin{pmatrix}1&-1\\-12/5&21/10\end{pmatrix},\qquad
\widehat N_{s,n}=(-1)^s C_{82}^{-1}N_{s,n}C_{82}.
```
The factor 13 applies per complete ninth return, not per original rotation step. No tenth induction or new retained coordinate is introduced.

The next word is `A,E,E`, with matrix `E^2 A`, on the directly checked strip `a=amax+b`, `0<y<b<c10`. It is not included in the current cone certificate.
