# Terminology registry — GERM-67 additive research supplement

**Date:** 2026-09-27 (America/Los_Angeles)  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Parents:** [main registry](TERMINOLOGY.md), [GERM-66 supplement](TERMINOLOGY_GERM66.md)  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This supplement defines the GERM-67 notation. It does not alter historical definitions or ratify the new pass.

## Three-layer feedback representation

Write `e=2h+eta`, `0<eta<=h`. A fundamental seed t in `(0,eta)` has three seed sites `t,t+h,t+2h`; a seed in `(eta,h)` has two. The reflected scalar values are included as in GERM-66. Six physical seed values are not assumed to be six independent retained coordinates.

For a seed chain of length m (m=2 or 3), put `A_i=x(t+ih)` and `B_i=epsilon x(e-t-ih)`, with `C_i=mu A_i+B_i` and `D_i=A_i+mu B_i`. Here `C_i,D_i` are scalar seed combinations, not operators or form domains. The conventions `D_-1=0`, `C_m=0` encode the inactive end feedback. Coefficients `a,d,mu,g,Delta`, and `W(t)=(x(t),epsilon x(u-t))^T` retain their GERM-65/66 meanings.

## Layer-prefix maps

`L_(m,i)` is the exact map from `W(t)` to `W(t+ih)` obtained by solving the paired source rows for that chain, with `L_(m,0)=I`. The final map `F_m=L_(m,m)` includes the last seed-to-bulk step. The local step is `N_(m,i)=L_(m,i+1)L_(m,i)^(-1)`. The bridge `K_(m,i)` maps `W(t+ih)` to `W(k+t+ih)`. Its upper-step counterpart is `H_(m,i)=J N_(m,i)^(-1) J`.

These definitions are licensed only after the paired pivots and prefix determinants have been shown nonzero. GERM-67 supplies that check for m=2 and 3. No arbitrary-layer theorem is asserted.

`Pi_3` is the four-by-four coefficient matrix of the paired rows in the unknowns `(A_1,B_1,A_2,B_2)` after fixing W(t). Set `chi=2a+d^2-1`, `Xi=chi^2+g^2 mu^2-a^2 d^2`, and `Psi=3chi^2+g^2 mu^2-2a^2 d^2`. These are pass-local coefficient expressions, not spectral parameters.

## Induced isolated-overlap return

On the h-circle use `R(t)=t+kappa mod h`, and let the overlap interval be `I_eta=(0,eta)`. For `0<eta<=kappa`, no two consecutive R-iterates lie in I_eta. The first-return map `S_eta` to `D_eta=(eta,h)` skips each isolated visit to I_eta. Its return times are one or two, and its images partition D_eta up to endpoints.

The labels `T_ij^+` and `T_ij^-` retain their source/target overlap-bit and wrap meanings, but denote the newly derived GERM-67 matrices. They are not the matrices bearing those labels in GERM-66. The two ordinary GERM-67 maps are the GERM-66 `11+` and `11-` maps.

The isolated-overlap excursion matrix is `B_exc=T_10^+ T_01^-`, with the rightmost map applied first. The two-visit diagnostic is `B_two=T_10^+ T_11^+ T_01^-`. A statement about either matrix is not a statement about arbitrary return words.

## Weighted signed-quadrant certificate

The norm is `||(X,Y)||_*=|X|+|Y|/5`. The cones remain `C_+={XY>=0}` and `C_-={XY<=0}` for real states. GERM-67 certifies forward C+ expansion and backward C- expansion by at least 7/5 for the three induced blocks, not for every individual three-layer generator.

The three-layer formulas are proved for `2h<e<=3h`. The new source-kernel exclusion is proved only for `2h<e<=2h+kappa`. The interval above that exclusion endpoint remains open even though its local layer formulas are available.
