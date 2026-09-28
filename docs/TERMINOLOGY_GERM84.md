# Terminology registry — GERM-84 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with [GERM-83](../notes/_recurrence83.md) and [GERM-84](../notes/_recurrence84.md). Historical names and the GERM-72 correction are unchanged.

## Parameter and residual lengths

Retain `t=e-e80`, `sigma=sigma8`, `psi=psi7`, `rho=rho9=psi-3sigma`, and `c=c10=sigma-rho`. Define the GERM-84 excess parameter
```math
b=t-(2\psi_7-2\sigma_8)=e-e_{83}.
```
The ninth formulas apply on `0<b<=sigma`; the new exclusion is only `0<b<=rho`. The remaining formula width is c. Retain `omega10=sigma-10c`, with `0<omega10<c`.

## Local ninth matrices

A, D, E are exactly the GERM-83 eighth matrices. Define **GERM-84-local**
```math
P=EDA,\qquad Q=E^2A,\qquad R=E^2DA,\qquad S=E^3A.
```
P/Q are the ninth branch y<c; R/S are the branch y>c. Q/S have source y<b. Repeated P/Q/R/S notation does not identify these with earlier matrices.

## Tenth words and parameter charts

The tenth section is `(0,c10)` in the ninth coordinate; its physical field is `W(t0+y)`, where `t0=h-beta+gamma-xi+2eta7`.

For `0<b<=c`, use `R^(N-1)P` or `R^(N-1)Q`, N=10,11. For `c<=b<=rho`, use `S^s R^(N-s-1)Q` with N=10,11 and `0<=s<=N-2`. There are 21 distinct temporal words, tested in 23 parameter/chart cells because two products are shared.

The low and high charts are
```math
C_{\rm lo}=\begin{pmatrix}1&1\\-97/50&-19/10\end{pmatrix},\qquad
C_{\rm hi}=\begin{pmatrix}1&-1\\-97/50&199/100\end{pmatrix}.
```
The chart depends on the fixed parameter b, not the orbit point. The factor 5 is per complete tenth return. The first newly admitted all-internal tenth word above b=rho is `S^9 Q`; it is not part of this expanding library.
