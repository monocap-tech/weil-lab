# Terminology registry — GERM-68 additive research supplement

**Date:** 2026-09-27 (America/Los_Angeles)  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Parent:** [Terminology](TERMINOLOGY.md), retaining [GERM-67](TERMINOLOGY_GERM67.md)  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This supplement registers the constructions used in GERM-68; it does not change historical definitions or ratify imported dependencies.

## Fixed exterior section

Write `e=2h+eta`, `kappa=k-5h`, `lambda=h-kappa`, and `tau=h-5kappa`. The new proof range is `kappa<eta<=lambda`. For the retained rotation `R(t)=t+kappa mod h`, the **fixed exterior section** is `E=(lambda,h)`. It is disjoint from the overlap `I_eta=(0,eta)` in this range. Use `t=lambda+z`, `0<z<kappa`, as its coordinate.

The first return to E takes N=6 steps for `z<tau` and N=5 for `z>tau`. In z-coordinates it is `z -> z-tau mod kappa`. This is an induced map of the already-derived recurrence, not a replacement for the entire prime-log translation algebra.

## Full-return overlap count and block

The integer s is the number of visits to `(0,eta)` between two successive E visits. It is characterized off seams by `z+(s-1)kappa<eta<z+s kappa`.

Let `A=T_00^+`, `P=T_10^+`, `Q=T_01^-`, and `E_+=T_11^+` refer to the GERM-67 matrices. The full-return block is

```math
B_{s,N}=A^{N-s-1}P E_+^{s-1}Q,
\qquad (N,s)\in\{(5,1),\ldots,(5,4),(6,1),\ldots,(6,5)\}.
```

Products act rightmost first. The section E and the matrix E_+ are different objects. A and P here are matrix aliases, not the old coefficient a or ambient prime-channel operator. The full-return block contains the compulsory ordinary steps; it is not the shorter overlap-excursion block.

## Signed cone chart

The common rational chart is

```math
C=\begin{pmatrix}1&1\\1/2&2\end{pmatrix},\qquad U=C^{-1}W.
```

The **signed cone chart** means that `sigma_s C^{-1} B_(s,N) C` is strictly positive, where `sigma_s=+1` for s=1,2 and `sigma_s=-1` for s=3,4,5. The sign remains in the actual recurrence. It is harmless only because the norm and double cones are invariant under simultaneous negation of both coordinates.

The tested norm is `||U||_1`. Its same-sign double cone expands forward; its opposite-sign double cone expands backward. The corresponding cones in W-coordinates are their images under C. No invariant positive cone is asserted for each individual GERM-67 generator.

## Overlapping-section boundary

At `eta>lambda`, the fixed section E intersects the overlap. The first wrap from that part of E is `11-` instead of `01-`. This is the **overlapping-section boundary** of the GERM-68 proof. It is not a breakdown of the three-layer source formulas and does not assert the existence of a kernel.
