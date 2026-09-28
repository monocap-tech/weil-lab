# Terminology registry — GERM-66 additive research supplement

**Date:** 2026-09-27 (America/Los_Angeles)  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Parent:** [GERM-65 terminology](TERMINOLOGY_GERM65.md), [main registry](TERMINOLOGY.md)  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This supplement defines new notation without rewriting historical uses. It is not a ratification.

## Two-layer bridge-feedback chamber

The parameter range `h < e <= 2h`, written `e=h+eta`, `0<eta<=h`. The scalar source equations and coefficients `mu,d,b,a,g,Delta` are those in GERM-65. The retained state remains `W(t)=(x(t),epsilon x(u-t))^T`, with `u=k+e`.

For `0<t<eta`, the two lower seed layers are t and h+t, together with their reflections e-t and eta-t. The top k-bridge for the first layer depends on the second layer. A four-coordinate representation of these values does not, by itself, prove that four independent state coordinates must be retained.

## Two-port overlap reduction

The exact elimination of the paired source rows at t and eta-t, together with their bridge equations, expressing `W(t+h)=N0 W(t)` for `0<t<eta`. The matrix defining this solve is `C_*`; its determinant is `-a(2a+d^2-1)/(g mu)`. Its right-hand coefficient matrix is `D_*`. These names denote coefficient matrices, not form domains or prime channels.

`N0` is the first overlap h-step. `N1` is the second overlap h-step, with source `h<t<e`. `F=N1 N0` is the two-step gate from t to t+2h. These symbols are specific to GERM-66; N0 is not the old nilpotent relay insertion, and F is not an earlier scalar forcing coefficient.

`K0` is the corrected k-bridge on `0<t<eta`; `K1=J K0^{-1} J` is its reflected bridge on `h<t<e`. The old K applies only on `eta<t<h` in this chamber. Upper gates are `H0=J N0^{-1} J`, `H=J N^{-1} J`, and `H1=J N1^{-1} J`.

## Six-type directed return library

On the h-circle let `R(t)=t+kappa mod h`, and put `i=1` if `t<eta`, otherwise i=0; `j=1` if `R(t)<eta`, otherwise j=0. These i,j are binary labels, not the logarithmic delay j.

`T_ij^+` denotes a nonwrapping return with displacement +kappa. `T_ij^-` denotes a wrapping return with displacement -lambda_ret. The only types are `00+`, `10+`, `11+`, `00-`, `01-`, and `11-`. Their actual state maps and domains are proved in the pass note, not inferred from their names.

This is a necessary return section for source solutions in `h<e<=2h`, not a complete global replacement of the higher-rank delay algebra. All six matrices are positive. Their determinants are respectively 1, 2, 1, 1, 1/2, and 1; determinant-one normalization is not assumed.

The signed-quadrant argument retains the GERM-65 cones, with a certified common forward/backward expansion factor 5/4 for this six-map library. No claim is registered above e=2h.
