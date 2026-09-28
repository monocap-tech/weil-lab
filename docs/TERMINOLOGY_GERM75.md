# Terminology registry — GERM-75 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read this supplement with GERM-73's source-word correction, GERM-74, and GERM-75. It neither rewrites historical definitions nor promotes experimental results.

## Fourth-section overlap parameter

Retain the residual lengths `alpha=beta+gamma`, `theta=2beta+gamma`, `xi=5gamma-beta`, and `omega=gamma-19xi`. Here beta and gamma are residual lengths, not the earlier prime coefficients. Define

```math
e=3h-\beta+\zeta,\qquad \varepsilon=\alpha+\zeta.
```

The theta-section overlap width is epsilon; the fourth-section overlap width is zeta. The new exclusion scope is `0<zeta<=14xi`. The newly audited third/fourth local formulas hold on `0<zeta<beta`; the fifth formula scope used here is `0<zeta<gamma`.

## Internal nonwrap and typed return libraries

`N3` denotes the new inside-to-inside third-section nonwrap, with chronological second-section word `11-,11+,11+`. It is distinct from `I3`, whose wrap word has three successive `11+` letters after its initial `11-`.

At the fourth and fifth levels, a label `ij+` or `ij-` records the source and target overlap bits i,j. A plus denotes a nonwrapping negative translation; a minus denotes its wrap. The six possible types are `00+`, `01+`, `11+`, `00-`, `10-`, `11-`. These labels require all intermediate source-domain checks; endpoint bits alone never establish a word.

Write the fourth maps as `A4,Q4,E4+,D4,P4,E4-`, in that order, and the fifth maps as `A5,Q5,E5+,D5,P5,E5-`. Their determinant factors are `1,rho^-1,1,1,rho,1`, respectively. Individual generators are not asserted to have an expanding cone.

## Exterior replacement sixth section

In the fifth coordinate choose

```math
\mathcal T_{\rm ext}=(\gamma-\xi,\gamma),\qquad
z=\gamma-\xi+y,\quad 0<y<\xi.
```

Its physical observation is `W(h-beta+gamma-xi+y)`. Its induced map is `y -> y+omega mod xi`, with return lengths 19 and 20. It is a different section from the bottom sixth section used in GERM-74; sharing the induced translation does not make their return words identical.

The complete return words are

```math
B_{0,N}=D_5A_5^{N-1},\qquad
B_{s,N}=P_5(E_5^+)^{s-1}Q_5A_5^{N-s-1},
\quad N\in\{19,20\},\quad 1\le s\le14.
```

Here s counts consecutive overlap source positions before the final wrap. The cone chart is

```math
C_{75}=\begin{pmatrix}-1&4\\1&-48/5\end{pmatrix}.
```

The factor 3 certified in GERM-75 is per complete sixth return, not per original rotation step. The fifteenth-visit word is outside that certificate.
