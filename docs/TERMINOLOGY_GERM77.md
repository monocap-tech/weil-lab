# Terminology registry — GERM-77 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with GERM-76 and the GERM-72 correction issued by GERM-73. Symbols below are local to the induced source recurrence and do not rename older prime coefficients.

## Seventh-section active width

Retain eta7=xi-omega, chi7=2omega-xi, psi7=eta7-chi7, and d=zeta-14xi. Define
```math
\delta=d-\eta_7.
```
The new seventh-section formula domain is `0<delta<chi7`. The newly proved exclusion is only `0<delta<=psi7`. The interval `(0,delta)` marks the seventh source positions whose first sixth-return atom changes from A20 to E20; this is a map-selection interval, not a new independent scalar-source coordinate.

## Four source-bit seventh maps

U0 and U1 are the nonwrapping seventh maps, on `psi7<z<chi7`. V0 and V1 are its wrapping maps, on `0<z<psi7`. The subscript is `i=1` when `z<delta`, and `i=0` when `z>delta`.

Their exact chronological sixth-atom words are:
```text
U0: A20,E20,A19
U1: E20,E20,A19
V0: A20,E20,A19,E20,A19
V1: E20,E20,A19,E20,A19
```
A19, A20, E20 retain the GERM-76 meanings. These formulas are not derived merely from endpoint bits; the note and verifier check the intermediate sources.

## Eighth bottom section

Exact arithmetic establishes `2psi7<chi7<3psi7`. Set
```math
\nu_8=\chi_7-2\psi_7,\qquad
\sigma_8=3\psi_7-\chi_7,\qquad
\nu_8+\sigma_8=\psi_7.
```
The eighth section is `(0,psi7)` in the seventh coordinate. Its first-return map is `z -> z+nu8 mod psi7`, with return time 2 below sigma8 and 3 above sigma8.

For `0<delta<=psi7`, its four complete matrices are `B_(i,n)=U0^(n-1) V_i`, with i=0,1 and n=2,3. Products act rightmost first. At delta=psi7 only i=1 remains generically.

The chart is `C77=[[1,4],[-9/4,-11]]`. The certified factor 17 is per complete eighth return, not per original rotation step. The original physical section begins at `h-beta+gamma-xi+2eta7`; its translation must not be suppressed when observing W.
