# Terminology registry — GERM-103 additive research supplement

**Date:** 2026-09-29  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical cursor:** SZ-CROSS-COLLAR-3, unchanged

Historical definitions and the GERM-72 / GERM-87 corrections remain unchanged.

## Post-s15 excess

Retain \(z=e-e_{101}\) and define

\[
\varepsilon=z-s_{15}=e-e_{102}.
\]

GERM-103 treats \(0<\varepsilon\le t_{15}\).

## Seventeenth residuals

Retain the GERM-102 sixteenth circle length \(t_{15}\) and its residual \(\rho_{16}\). Define

\[
c_{16}=t_{15}-\rho_{16},
\qquad
\rho_{17}=t_{15}-5c_{16},
\qquad
c_{17}=c_{16}-\rho_{17}.
\]

The seventeenth section is \(K_{17}=(0,c_{16})\), with map

\[
y\mapsto y+\rho_{17}\pmod{c_{16}},
\]

and return times five or six.

## GERM-103-local sixteenth maps

All \(H_1,J_1,J_2\) inputs retain their GERM-102 fifteenth definitions:

\[
A_0=H_1^3J_1,\qquad
A_1=H_1^3J_2,\qquad
B_0=H_1^4J_1,\qquad
B_1=H_1^4J_2.
\]

## Complete seventeenth words

For \(0<\varepsilon\le c_{16}\):

\[
B_0^{N-1}A_i,\qquad i\in\{0,1\},\quad N\in\{5,6\}.
\]

For \(c_{16}\le\varepsilon\le t_{15}\):

\[
B_1^sB_0^{N-s-1}A_1,
\qquad N\in\{5,6\},\quad0\le s<N.
\]

Products act rightmost first.

The cone charts are

\[
C_{\rm low}=
\begin{pmatrix}
1&1\\
-2827/2000&-27/20
\end{pmatrix},
\qquad
C_{\rm high}=
\begin{pmatrix}
1&1\\
-279/200&-283/200
\end{pmatrix}.
\]
