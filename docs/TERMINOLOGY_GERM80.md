# Terminology registry — GERM-80 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with GERM-79 and GERM-80. The GERM-72 correction remains in force.

## Residual parameter and endpoint

Retain delta=e-e76, sigma8=3psi7-chi7, rho9=psi7-3sigma8.
Define
```math
\delta_{79}=\chi_7-\sigma_8,\qquad b=\delta-\delta_{79}.
```
The new exclusion range is `0<b<=sigma8`. Its right endpoint is the previously open seventh-map formula endpoint `delta=chi7`; GERM-80 derives its inclusion from lower source contracts rather than assuming continuity.

## Retyped ninth matrices

The matrix labels P, Q, R, S in this pass mean
```math
P=EDA,\quad Q=E^2A,\quad R=E^2DA,\quad S=E^3A,
```
where A, D, E are the GERM-79 eighth matrices. These local matrix labels are not the ambient operator P_c or a section rotation S_j.

P/Q apply below the ninth cut and R/S above it. Q/S mean that the ninth source lies in `(0,b)`. The internal eighth visits are retained in every definition.

## Tenth section

Define
```math
c_{10}:=\sigma_8-\rho_9=c_9,\qquad
\omega_{10}:=\sigma_8-10c_{10}.
```
The label c10 is an explicit alias for GERM-79's cut c9, now used as a section length; it is not a different arithmetic residual. The certificate establishes `10c10<sigma8<11c10`.

The tenth section is `K10=(0,c10)` inside the ninth circle. Its first return is `y -> y+omega10 mod c10`, with return times ten or eleven. Its physical field is `W(t0+y)`, using the unchanged GERM-77 physical origin t0.

## Parameter-dependent charts

Two fixed rational charts are used, selected by the parameter b, not by the orbit point:
```math
C_{\rm low}=\begin{pmatrix}1&1\\-293/100&-14/5\end{pmatrix},\qquad
C_{\rm high}=\begin{pmatrix}1&-1\\-113/40&277/100\end{pmatrix}.
```
The low chart applies for `0<b<=c10`; the high chart for `c10<=b<=sigma8`. There is no chart change along an orbit at fixed b. Four low-strip and 21 high-strip tests certify 23 distinct complete words; two words are shared. The common cone factor is 400 per complete tenth return, not per original step.
