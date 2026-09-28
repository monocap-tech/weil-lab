# Terminology registry — GERM-71 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Parent registry:** [Terminology](TERMINOLOGY.md)  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This supplement introduces the GERM-71 notation without modifying historical definitions.

## Second-section self-overlap parameter

Retain `kappa=k-5h`, `tau=h-5kappa`, and `theta=kappa-8tau`, with `3theta<tau<4theta`. Set

```math
\zeta=e-(3h-\tau),\qquad
\eta=e-2h=h-\tau+\zeta,\qquad
\nu=\eta-(h-\kappa)=\kappa-\tau+\zeta.
```

The physical second section `(h-tau,h)` has coordinate `0<y<tau`. Its internal part is exactly `(0,zeta)` in that coordinate. In this pass `0<zeta<=tau-theta` is the exclusion range; necessary retyped second-section formulas are checked on `0<zeta<tau`.

## Inside-to-inside first-section wrap

With `E_+=T_11^+` and `E_-=T_11^-`, write `J_1=E_+^5 E_-`. This is the six-original-step first-section wrap whose two section endpoints are both internal. It is the species isolated by GERM-70, not the coordinate-swap matrix also historically denoted J.

## Retyped second-section maps

The maps `A_2,P_2,E_2^+,D_2,Q_2,E_2^-` are respectively the six second-section types `00+`, `10+`, `11+`, `00-`, `01-`, `11-` over `S_2(y)=y+theta mod tau`. Bits record membership of the source and target in `(0,zeta)`; plus/minus records absence/presence of wrap. They are products of the licensed first-section species, not newly assumed local source maps. Their chronological words and precise domains are in the pass and verifier.

## Exterior replacement third section

The section `G_ext=(tau-theta,tau)` in y coordinates is physically `(h-theta,h)`. Unlike GERM-70's bottom section `(0,theta)`, this section remains exterior while `zeta<=tau-theta`. With `y=tau-theta+v` its first return is `v -> v-alpha mod theta`, where `alpha=tau-3theta`, and takes three or four S2 steps.

The seven complete exterior words are denoted `B_(s,ell)` for `ell in {3,4}` and `0<=s<ell`. Here s counts overlap positions after the initial wrap, and ell is the complete S2 return time. Their coordinate chart is `C_71=[[1,1],[0,3]]`. Cone factors are per complete return, not per original rotation step.

## Positive-determinant discriminant

For a real two-by-two matrix B with positive determinant, `disc(B)=tr(B)^2-4 det(B)`. A negative value is called projectively elliptic here: dividing by the positive scalar `sqrt(det B)` would give a determinant-one elliptic matrix. This terminology does not license deleting that scalar from a physical cocycle or its L2 norm estimates. In particular, `|tr B|>2` alone does not imply hyperbolicity when `det B != 1`.
