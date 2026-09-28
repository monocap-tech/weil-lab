# Terminology registry — GERM-65 additive research supplement

**Date:** 2026-09-27 (America/Los_Angeles)  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Parent registry:** [Terminology](TERMINOLOGY.md)  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

This page adds notation for the GERM-65 pass. It does not redefine historical terminology or promote the pass into the canonical theorem inventory.

## Scalar two-coordinate state

For the scalar parity profile x, external parity epsilon in {+1,-1}, and u=k+e, define

```math
W(t)=\begin{pmatrix}x(t)\\\varepsilon x(u-t)\end{pmatrix},\qquad 0<t<u.
```

This is a bounded observation of an L2 profile, not a classical endpoint jet. It satisfies the inherited reflection constraint `W(u-t)=epsilon J W(t)`, where J swaps coordinates. It is not identified without proof with the historical P/J state `(X,S)`.

The coefficient notation in this pass is

```math
\mu=\beta\gamma,\quad d=\delta\gamma,\quad b=\beta\mu,
\quad a=b^2,\quad g=1-a,\quad \Delta=1-\mu^2.
```

These a, b, d are pass-local coefficient symbols; they are not the logarithmic delay symbols with the same letters in GERM-60.

## Directed lower-defect return section

For `lambda_ret < e <= h`, with `kappa=k-5h` and `lambda_ret=h-kappa`, use the h-circle rotation

```math
R(t)=t+\kappa\pmod h
```

restricted to lower-defect points in `(0,e)`. A directed edge is retained exactly when its source and target lie in `(0,e)`. Its two allowed coordinate displacements are `+kappa` and `-lambda_ret`, not `+kappa` and `+lambda_ret`.

This is a derived section of the scalar recurrence in this parameter range. It does not replace the full rank-three delay algebra or assert a complete two-matrix model above e=h.

## Local and return matrix names

M is the derived gate-free h-step in W-coordinates. N is the lower-gate h-step; H=`J N^{-1} J` is the upper-gate h-step. K is the k-bridge between W(t) and W(t+k), for `0<t<e` and `e<=h`.

The directed internal return matrices are

```math
T_\kappa=N^{-1}M^{-3}H^{-1}K,
\qquad
T_{-\lambda}=N^{-1}M^{-4}H^{-1}K.
```

M and K have determinant one. N and H do not individually have determinant one; their determinants cancel in either return matrix. The exact formulas and domains are derived in the pass note, not assumed by these names.

## Signed-quadrant exclusion

On real two-coordinate states, use the double cones

```math
C_+=\{(x,y):xy\ge0\},\qquad C_-=\{(x,y):xy\le0\}.
```

GERM-65 tests forward expansion on C+ for the two directed return matrices, and backward expansion on C- for their inverses. It does not require one expanding cone for arbitrary forward and inverse words. Complex-valued profiles are handled by real and imaginary parts.

The finite-path entry and exit covectors are called `ell_in` and `ell_out`. They are evaluations of ordinary L2-profile relations on parameter intervals, not pointwise boundary traces of the original neutral mode.
