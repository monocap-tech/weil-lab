# Terminology registry — GERM-69 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Parent:** [Terminology](TERMINOLOGY.md), retaining [GERM-68](TERMINOLOGY_GERM68.md)  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Historical definitions and claims are not rewritten or promoted by this supplement.

## Section-overlap width and second remainder

In the existing three-layer range, write `e=2h+eta`, `lambda=h-kappa`, and `tau=h-5kappa`. The **section-overlap width** is `nu=eta-lambda`: for nu>0, the old section `(lambda,h)` intersects the source overlap `(0,eta)`. In its coordinate `t=lambda+z`, the overlap is `(0,nu)`.

The **second remainder** is `theta=kappa-8tau`. The GERM-69 verifier certifies `0<theta<tau`, equivalently `8tau<kappa<9tau`. These are lengths, not the physical coefficient symbols of GERM-65/67.

## Second exterior section

For `0<nu<=5tau`, the **second exterior section** is `F=(kappa-tau,kappa)` in the old z coordinate. In the original h-circle it is `(h-tau,h)`. It is outside the section overlap because `5tau<kappa-tau`.

Parameterize it by `z=kappa-tau+y`, `0<y<tau`. The first return of the old section rotation `S(z)=z-tau mod kappa` takes eight or nine S-steps and acts as `y -> y+theta mod tau`. This is a derived iterated section of the necessary scalar recurrence, not a new model for the entire rank-three delay algebra.

## First-section matrix names

With the inherited six-map notation, set `P=T_10^+`, `Q=T_01^-`, `E_+=T_11^+`, and `E_-=T_11^-`. Define

```math
A_1=P E_+^3Q,\quad D_1=P E_+^4Q,\quad
Q_1=E_+^4Q,\quad P_1=P E_+^4E_-,\quad E_1=E_+^4E_-.
```

These names are local to GERM-69. In particular, D1 is not an earlier constraint atom with a similar name. A1 and D1 are outside-to-outside returns; Q1 enters the section overlap; P1 exits it; E1 remains inside it. Their source domains are stated and checked in the pass note and verifier.

## Nested full-return word

For a return to F taking N old-section steps, let s count positions in `(0,nu)` before the final wrap. A **nested full-return word** is the actual chronological product

```math
D_{0,N}=D_1A_1^{N-1},\qquad
D_{s,N}=P_1E_1^{s-1}Q_1A_1^{N-s-1}\quad(s\ge1).
```

In the proved range, `N in {8,9}` and `s in {0,...,5}`. Products act rightmost first. They contain 41 or 46 original h-circle return steps, respectively. This is a finite library of complete legal words, not a flat orbit-constraint determinant construction.

## Second-section cone chart

The fixed chart is `C2=[[1,1],[1,20]]`. The positive representatives are `(-1)^N C2^{-1}D_(s,N)C2`. The actual signs remain in the cocycle. Same-sign and opposite-sign double cones are invariant under simultaneous negation, so their expansion estimates apply without changing the equation.
