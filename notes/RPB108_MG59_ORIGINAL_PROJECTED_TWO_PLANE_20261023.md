# MG59 — Original physical two-plane action projection BEFORE source/multiplier/pole error bounding

**Status: exact original 41-cell 2D source producer and a separately implemented independent verifier submitted; GitHub Actions acceptance pending.** Parent MG58 #307 is independently rebuilding genuinely fresh 47- and 55-cell original source moments. MG59 is complementary: it uses the already independently verified MG57 *41 genuine original source cells* and changes the mathematical order of projection and uncertainty enclosure, not the original operator or source data.

## Why MG58's full24 source lower is not the only path to a 2D source certificate

MG57's original full24 corrected-action lower L57 has exact rational signed inertia (1 positive,23 negative). Sylvester's law says that **no two-dimensional subspace can have a strictly positive definite restriction of that SAME particular conservative lower L57**. This does NOT rule out strict positive original true strong-action energy on a second direction: L57 is an underestimate with a large independently paid whole24 diagonal Young error. A source-plane-specific bound may retain physical covariances suppressed by the whole24 estimate and be stronger than `V^T L57 V`.

## Physically true projected source action and a NEW common-scalar correlation

Retain the original SI10 25 physical source functions, MG11 original 23 boundary-adapted plus genuine sinh-pole 24D frame, signed seven-prime/digamma multiplier `a_o(xi)`, and true physical action
```
u_j(xi)=a_o(xi) t_j(xi)-2 t_p(xi) b_j,
b=F^*s  (true original sinh-pole column).
```

For ANY original real integer source coefficient vector z, the ACTUAL physical Fourier source for the transformed strong action on z is a scalar
```
y_z(xi)=a_o(xi) sum_j z_j t_j(xi)
        -2 t_p(xi) sum_j z_j b_j.
```

On each accepted original MG57 positive-frequency physical cell, the source Taylor form is `t=v+x*d+e`, `|e_j|<=r_j`, `x in [-half,half]`, scalar multiplier `a=ac+delta_a` with `|delta_a|<=da`, pole column `b=bmid+delta_b` with component radii `brad_j`. Define `B_z=sum_j z_j bmid_j`, `V_z=sum_j z_j v_j`, `D_z=sum_j z_j d_j`. The exact projected strong-action affine midpoint and derivative are

```
Y0=ac*V_z-2*v_p*B_z,
Y1=ac*D_z-2*d_p*B_z.
```

And the **rigorous shared physical-error** component radius is

```
rho_z =
  sum_j |ac*z_j - 2*B_z*1_{j=p}| * r_j
  + da*(|V_z|+half*|D_z|+sum_j |z_j|r_j)
  + 2*(sum_j |z_j|brad_j)*
      (|v_p|+half*|d_p|+r_p).
```

This is a rigorous original full-real-frequency strong-action source enclosure: same pole Taylor e_p and multiplier delta_a are each one physical scalar and **must not** be adversarially signed independently for all 24 channels. Crucially, project to a chosen 2D physical source plane *before* charging Young errors; do not take the already lossy full24 MG57 moment `L57` and project it afterward.

## Whole two-plane lower

Choose original known MG57 positive mixed integer vector
```
v=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
```
and test ten independent second vectors: nine chosen original coordinate axes and MG57's second independent short-integer positive ray. For each real original-source two-plane basis `W=[v,w]`, project every true original cell onto the two physical Fourier action scalar sources `(y_v,y_w)`, integrate its exact affine rank-one covariance, and charge its **2D** error radius via independently accepted directional Young inequality. This gives exact rational 2x2 matrices
```
W^T S_* W >= W^T S_original,[0,4] W >= L_projected_2x2,
```
including the mirrored negative physical frequency band. The unmeasured original frequency action energy remains PSD; no signed or original source part is omitted.

An accepted genuinely positive 2D original source plane requires
```
L00>0, L11>0, L00*L11-L01^2>0
```
checked in **exact rational arithmetic**. Then an explicit conservative original SOURCE COEFFICIENT Euclidean coercivity lower on span(v,w) is
```
det(L2)/(trace(L2)*(||v||²+||w||²)) >0.
```
This is a proof for the **restricted original source plane only**; it cannot be promoted to `S_*>=cWW^T` as a GLOBAL Loewner bound without complement cross-term control. Negative conservative 2D lowers do not prove physical negative original action directions.

## Why this remains valuable regardless of MG58's outcome

MG58 changes physical Fourier resolution in two original frequency bands, aiming to produce a second positive direction in the **global** 24D original conservative lower. MG59 keeps independently accepted MG57 physical cells and tests an analytically stronger **projection-before-bounding** inequality. These are different verification axes: MG58's subdivision does not address correlated source/pole/multiplier uncertainty inside each physical cell, and MG59's projected two-plane does not produce a new original globally positive full24 lower.

The separate independent verifier does not import MG59's producer. It reconstructs accepted original 41 physical cells from MG32 plus MG57 pinned archive, the physical original pole column from MG24, and the same common-scalar error coefficients by a distinct algebraic order. It checks every 2x2 rational lower and upper, original full24 MG57 restriction for comparison, all ten source planes' exact Gram determinant signs, and the physical one-plane/two-plane restricted operator scope.

No original full24 residual source contraction, original full470D inverse, signed odd 51/56 spectral cap, independent Fourier/form/domain proof, or complete even/Weil/CC27/RH proof. All OPEN.
