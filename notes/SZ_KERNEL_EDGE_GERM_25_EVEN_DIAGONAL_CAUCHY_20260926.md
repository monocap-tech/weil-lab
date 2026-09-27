# SZ-KERNEL-EDGE-GERM-25 — Even-diagonal Cauchy normal form and principal-log no-go

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-24  
**Target tested:** EVEN-DIAGONAL CAUCHY NORMAL FORM  
**Public promotion:** forbidden

## 0. Objective

GERM-24 reduced the multi-prime hard branch to a finite-dimensional family in
which:

- finitely many reachable movable centers separate the source after local
  symmetrization;
- exact local oddness has been eliminated as a simultaneous hiding mechanism;
- every surviving nonzero direction has a nonzero **even** local source germ
  at some selected center;
- nevertheless the corresponding logarithmic diagonal field is superflat.

The question for this pass is whether the two-sided centered logarithmic
singularity is intrinsically more rigid than the one-sided Stieltjes
transforms defeated in GERM-20.

At the level of the principal logarithmic species, the answer is no.

For the principal kernel

\[
q(t)=\frac12|t|\log|t|,
\]

the centered even-source channel has an exact Cauchy/logarithmic normal form.
Its boundary expansion is controlled by inverse odd moments of the even local
source.

Using the Mellin momentless construction already introduced in GERM-20, one
can construct a nonzero source germ that:

1. is superflat at the center;
2. is even-visible, not parity-blind;
3. has every inverse odd moment equal to zero;
4. produces a centered principal-log field that is superflat to every
   algebraic order.

Therefore:

\[
\boxed{
\text{two-sided centering}
+
\text{even source visibility}
+
\text{principal logarithmic singularity}
\not\Rightarrow
\text{quasi-analytic rigidity}.
}
\]

This is a local principal-species no-go.

It does **not** yet prove the same statement for the complete Suzuki
archimedean kernel.  The lower-order analytic/cusp remainder is now the only
local ingredient not included in the countermodel.

---

# I. Principal local kernel

## 1. Logarithmic singular part

Suzuki's archimedean screw kernel has local principal behavior

\[
a_\infty(t)
=
\frac12|t|\log|t|
+
\text{lower singular / regular terms}.
\]

Set

\[
\boxed{
q(t)
=
\frac12|t|\log|t|.
}
\]

Take an even local source about a selected movable center, represented on the
positive half by

\[
\sigma\in L^2(0,\rho).
\]

The principal centered channel is

\[
\boxed{
D_\sigma(\delta)
=
\int_0^\rho
\left[
q(t+\delta)
+
q(|t-\delta|)
-
2q(t)
\right]
\sigma(t)\,dt,
}
\]

for

\[
0<\delta<\rho.
\]

This is exactly the principal contribution to the symmetrized local diagonal
field from GERM-24.

---

# II. Exact derivative normal form

## 2. Region \(t>\delta\)

For

\[
t>\delta>0,
\]

we have

\[
q(t+\delta)
=
\frac12(t+\delta)\log(t+\delta),
\]

and

\[
q(t-\delta)
=
\frac12(t-\delta)\log(t-\delta).
\]

Differentiating with respect to \(\delta\),

\[
\boxed{
\frac{\partial}{\partial\delta}
\left[
q(t+\delta)+q(t-\delta)-2q(t)
\right]
=
\frac12
\log\frac{t+\delta}{t-\delta}.
}
\]

---

## 3. Crossing region \(0<t<\delta\)

For

\[
0<t<\delta,
\]

\[
|t-\delta|=\delta-t.
\]

Hence

\[
\boxed{
\frac{\partial}{\partial\delta}
\left[
q(t+\delta)+q(\delta-t)-2q(t)
\right]
=
1+\frac12\log(\delta^2-t^2).
}
\]

Therefore the exact derivative of the principal centered field is

\[
\boxed{
D_\sigma'(\delta)
=
\frac12
\int_\delta^\rho
\log\frac{t+\delta}{t-\delta}\,
\sigma(t)\,dt
+
\int_0^\delta
\left[
1+\frac12\log(\delta^2-t^2)
\right]
\sigma(t)\,dt.
}
\]

This is the two-sided centered Cauchy/logarithmic normal form.

---

# III. Outer Cauchy series

## 4. Expansion away from the crossing point

For

\[
t>\delta,
\]

\[
\frac12
\log\frac{t+\delta}{t-\delta}
=
\operatorname{arctanh}\left(\frac{\delta}{t}\right).
\]

Thus for

\[
t>2\delta,
\]

\[
\boxed{
\frac12
\log\frac{t+\delta}{t-\delta}
=
\sum_{k=0}^{K-1}
\frac{\delta^{2k+1}}
{(2k+1)t^{2k+1}}
+
\mathcal R_K(t,\delta),
}
\]

with

\[
\boxed{
|\mathcal R_K(t,\delta)|
\lesssim_K
\frac{\delta^{2K+1}}{t^{2K+1}}.
}
\]

Hence the outer centered channel is governed by the inverse odd moments

\[
\boxed{
I_k(\sigma)
=
\int_0^\rho
t^{-(2k+1)}
\sigma(t)\,dt.
}
\]

---

# IV. Crossing region under source superflatness

## 5. Superflat source mass

Assume

\[
\boxed{
\|\sigma\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Then for every fixed inverse power \(M\),

\[
t^{-M}\sigma(t)\in L^1(0,\rho)
\]

and the contribution from

\[
0<t<2\delta
\]

is superflat in \(\delta\), even after multiplication by finite powers of

\[
|\log\delta|.
\]

In particular,

\[
\boxed{
\int_0^\delta
\left[
1+\frac12\log(\delta^2-t^2)
\right]
\sigma(t)\,dt
=
o(\delta^N)
\qquad
\forall N.
}
\]

The near-crossing portion

\[
\delta<t<2\delta
\]

of the first integral is likewise superflat.

Thus only the inverse-moment Cauchy series on

\[
t>2\delta
\]

can contribute finite algebraic orders.

---

# V. Construction of a nonzero inverse-momentless source

## 6. Mellin momentless functions

GERM-20 introduced smooth functions

\[
\mu_0,\mu_1
\]

on

\[
(0,\infty)
\]

with the following properties:

- they are flat at \(0\);
- they decrease faster than every power at \(+\infty\);
- every nonnegative polynomial moment vanishes:
  \[
  \int_0^\infty
  y^m\mu_j(y)\,dy=0,
  \qquad
  m=0,1,2,\ldots;
  \]
- \(\mu_0,\mu_1\) are linearly independent.

They arise as inverse Mellin transforms of

\[
M_j(s)
=
s^j\sin(\pi s)e^{s^2}.
\]

---

## 7. Invert the local radius

Fix

\[
\rho>0
\]

and set

\[
a=\rho^{-1}.
\]

For

\[
0<t<\rho,
\]

define

\[
y=\frac1t-a.
\]

Then

\[
y\in(0,\infty),
\qquad
t=\frac1{y+a}.
\]

Given a rapidly decreasing \(\mu\), define

\[
\boxed{
\sigma(t)
=
\mu\left(\frac1t-a\right).
}
\]

Because \(\mu\) is rapidly decreasing at infinity,

\[
\sigma
\]

is superflat as

\[
t\downarrow0.
\]

Because \(\mu\) is flat at \(0\),

\[
\sigma
\]

also dies smoothly at

\[
t=\rho.
\]

Thus

\[
\sigma\in C_c^\infty(0,\rho)
\]

in the open-interval sense with flat endpoint extensions, and in particular

\[
\sigma\in L^2(0,\rho).
\]

---

# VI. Inverse odd moments

## 8. Change of variables

For

\[
k\ge0,
\]

\[
\begin{aligned}
I_k(\sigma)
&=
\int_0^\rho
t^{-(2k+1)}
\sigma(t)\,dt\\
&=
\int_0^\infty
(y+a)^{2k-1}
\mu(y)\,dy.
\end{aligned}
\]

For

\[
k\ge1,
\]

the weight

\[
(y+a)^{2k-1}
\]

is a polynomial in \(y\).

Therefore every polynomial-momentless \(\mu\) gives

\[
\boxed{
I_k(\sigma)=0,
\qquad
k\ge1.
}
\]

For

\[
k=0,
\]

the remaining condition is

\[
\boxed{
I_0(\sigma)
=
\int_0^\infty
\frac{\mu(y)}{y+a}\,dy.
}
\]

---

## 9. Kill the last inverse moment

Let

\[
M
=
\operatorname{span}\{\mu_0,\mu_1\}.
\]

The map

\[
\mu
\longmapsto
\int_0^\infty
\frac{\mu(y)}{y+a}\,dy
\]

is one linear functional on the two-dimensional space \(M\).

Therefore its kernel contains a nonzero vector.

Choose

\[
\boxed{
0\ne\mu\in M
}
\]

such that

\[
\boxed{
\int_0^\infty
\frac{\mu(y)}{y+a}\,dy=0.
}
\]

The associated

\[
\sigma(t)
=
\mu(1/t-a)
\]

is nonzero and satisfies

\[
\boxed{
I_k(\sigma)=0
\qquad
\forall k\ge0.
}
\]

---

# VII. Superflatness of the principal centered field

## 10. Outer region

Fix an arbitrary integer \(K\ge1\).

On

\[
t>2\delta,
\]

insert the finite Cauchy expansion:

\[
\frac12
\log\frac{t+\delta}{t-\delta}
=
\sum_{k=0}^{K-1}
\frac{\delta^{2k+1}}
{(2k+1)t^{2k+1}}
+
\mathcal R_K.
\]

Because

\[
I_k(\sigma)=0,
\]

the integral of each displayed coefficient over the full interval
\((0,\rho)\) vanishes.

Replacing the full moment by the truncated region \(t>2\delta\) introduces
only the missing interval

\[
0<t<2\delta,
\]

which is superflat by source superflatness.

The remainder satisfies

\[
\left|
\int_{2\delta}^\rho
\mathcal R_K(t,\delta)\sigma(t)\,dt
\right|
\lesssim_K
\delta^{2K+1}
\int_0^\rho
t^{-(2K+1)}
|\sigma(t)|\,dt.
\]

The weighted integral is finite.

Hence

\[
\boxed{
D_\sigma'(\delta)
=
O_K(\delta^{2K+1})
+
\text{superflat}.
}
\]

Because \(K\) is arbitrary,

\[
\boxed{
D_\sigma'(\delta)
=
o(\delta^N)
\qquad
\forall N.
}
\]

---

## 11. Integrate once

Since

\[
D_\sigma(0)=0,
\]

we obtain

\[
D_\sigma(\delta)
=
\int_0^\delta
D_\sigma'(s)\,ds.
\]

Therefore

\[
\boxed{
D_\sigma(\delta)
=
o(\delta^N)
\qquad
\forall N.
}
\]

The same conclusion holds in local \(L^2(0,\varepsilon)\) form.

Thus the centered principal logarithmic field is nonzero-source but
infinitely flat.

---

# VIII. This is not parity blindness

## 12. The even carrier is genuinely nonzero

The full local source about the movable center is obtained by even reflection
of \(\sigma\):

\[
f_{\rm loc}(h+t)
=
f_{\rm loc}(h-t)
=
\frac12\sigma(t).
\]

Therefore

\[
\boxed{
\Sigma_{h,\rho}f_{\rm loc}
=
\sigma
\ne0.
}
\]

So the countermodel lies entirely in the diagonal-even source sector exposed
by GERM-24.

It is not in the local odd kernel.

---

# IX. Comparison with the one-sided Stieltjes no-go

## 13. Same non-quasi-analytic mechanism in different coordinates

GERM-20 used a Möbius/Stieltjes coordinate to construct a nonzero one-sided
source with:

- superflat source mass;
- superflat one-sided archimedean transform.

The present pass uses reciprocal local radius

\[
y=\frac1t-\frac1\rho
\]

to construct a nonzero **even** source with:

- superflat mass at the diagonal;
- vanishing inverse odd moments;
- superflat centered principal-log field.

Thus the one-sided and two-sided local failures are two manifestations of the
same momentless Mellin mechanism.

---

# X. Scope guard: full Suzuki kernel

## 14. What has and has not been disproved

The complete local archimedean kernel is

\[
a_\infty(t)
=
q(t)+r_\infty(t),
\]

where

\[
q(t)=\frac12|t|\log|t|
\]

is the principal logarithmic species and \(r_\infty\) contains the remaining
lower-singular / regular terms.

This pass proves a no-go for the map

\[
\sigma
\longmapsto
\int_0^\rho
\Delta_\delta^2q(t)\sigma(t)\,dt.
\]

It does **not** prove that the same constructed \(\sigma\) makes

\[
\int_0^\rho
\Delta_\delta^2a_\infty(t)\sigma(t)\,dt
\]

superflat.

The remainder may contribute additional finite-order moment constraints.

Therefore the correct conclusion is:

\[
\boxed{
\text{the principal logarithmic singularity alone has no
quasi-analytic rigidity}.
}
\]

Any stronger local rigidity must use the exact lower-order Suzuki
archimedean structure, prime coupling, or both.

---

# XI. Consequence for GERM-24

## 15. Even-source detection is insufficient

GERM-24 established that a nonzero hard-branch vector has some selected center
with

\[
\Sigma_{h,\rho}f\ne0
\]

while its full diagonal observation is superflat.

The present countermodel shows that the implication

\[
\boxed{
\Sigma_{h,\rho}f\ne0
\Longrightarrow
\text{principal log field has finite order}
}
\]

is false.

Thus parity reduction, while necessary, is not enough.

The surviving local question concerns the **exact** Suzuki remainder beyond
the principal \(|t|\log|t|\) term.

---

# XII. Result of this NF pass

The two-sided centered logarithmic principal species has an exact Cauchy
normal form:

\[
\boxed{
D_\sigma'(\delta)
=
\frac12
\int_\delta^\rho
\log\frac{t+\delta}{t-\delta}\sigma(t)\,dt
+
\int_0^\delta
\left[
1+\frac12\log(\delta^2-t^2)
\right]\sigma(t)\,dt.
}
\]

There exist

\[
\boxed{
0\ne\sigma\in L^2(0,\rho)
}
\]

with source mass superflat at \(0\) and

\[
\boxed{
\int_0^\rho
t^{-(2k+1)}\sigma(t)\,dt=0
\qquad
\forall k\ge0,
}
\]

for which

\[
\boxed{
D_\sigma(\delta)
=
o(\delta^N)
\qquad
\forall N.
}
\]

The source is genuinely even-visible and not parity-blind.

Therefore:

\[
\boxed{
\text{principal two-sided log diagonal}
\not\Rightarrow
\text{finite-order rigidity}.
}
\]

The local load-bearing remainder has now been narrowed to the exact
nonprincipal Suzuki archimedean terms.

---

# XIII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-26 / FULL ARCHIMEDEAN REMAINDER TEST}.
}
\]

The next pass should insert the exact positive-axis formula

\[
a_\infty''(t)
=
-e^{t/2}
+
\frac{e^{-5t/2}}{1-e^{-2t}}
\]

into the centered even-source channel and determine whether its nonprincipal
part adds a complete moment family that kills the GERM-25 counterspace.

Two outcomes are possible:

1. **rigidity:** the exact remainder supplies enough independent moments to
   force the even source to vanish;
2. **no-go:** the Mellin momentless construction can be extended to satisfy
   the exact remainder constraints as well.

No full-archimedean conclusion is asserted in this pass.

---

# XIV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified even-diagonal principal-log no-go result.

No public promotion and no canonical cursor movement are asserted.
