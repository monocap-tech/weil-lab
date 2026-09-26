# SZ-KERNEL-EDGE-DET-1 — Sharp no-go for abstract Gram-determinant rigidity

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-QA-3-CANONICAL-GRAMIAN  
**Target tested:** CANONICAL GRAM DETERMINANT RIGIDITY  
**Public promotion:** forbidden

## 0. Objective

SZ-KERNEL-EDGE-QA-3 canonically packages the possible endpoint obstruction

\[
\mathcal E_c=F_\infty/P_c^+
\]

into the positive edge Gramian

\[
A_c(\varepsilon)
=
\mathcal O_\varepsilon^*\mathcal O_\varepsilon
\]

and its determinant

\[
D_c(\varepsilon)=\det A_c(\varepsilon).
\]

If \(\mathcal E_c\ne0\), then throughout the stabilized collar

\[
A_c(\varepsilon)>0,
\qquad
D_c(\varepsilon)>0,
\]

while both are flat to every algebraic order as \(\varepsilon\downarrow0\).

The present pass asks whether the following structural package is already
strong enough to force a contradiction:

1. finite-dimensional quotient;
2. injective collar observation;
3. positive Gramian;
4. rank-\(\le2\) Gramian growth;
5. positive determinant;
6. infinite flatness;
7. local second-order Volterra structure.

The answer is **no**.

There is an explicit finite-dimensional model satisfying all of those
properties, including rank-one growth and exact Volterra realization.

Therefore any future determinant-rigidity proof must use additional
Weil-specific coupling from the global first-kind equation.

---

# I. Abstract flat observation model

## 1. Model space

Fix any integer

\[
d\ge1
\]

and let

\[
E=\mathbb C^d
\]

with its standard Hilbert structure.

For

\[
v=(v_0,\ldots,v_{d-1})\in E,
\]

define the polynomial

\[
p_v(\delta)
=
\sum_{j=0}^{d-1}
v_j\delta^j.
\]

Let

\[
\chi(\delta)
=
\begin{cases}
e^{-1/\delta^2}, & \delta>0,\\
0, & \delta=0.
\end{cases}
\]

Then \(\chi\in C^\infty([0,\infty))\) and

\[
\chi^{(N)}(0)=0
\qquad
\forall N\ge0.
\]

Define the two-edge observation

\[
\boxed{
\Gamma_\delta(v)
=
\bigl(
\chi(\delta)p_v(\delta),
0
\bigr)
\in\mathbb C^2.
}
\]

Every observation germ is \(C^\infty\)-flat at the edge.

---

## 2. Integrated observation is injective

For \(0<\varepsilon\), define

\[
\mathcal O_\varepsilon:
E\to L^2((0,\varepsilon);\mathbb C^2)
\]

by

\[
(\mathcal O_\varepsilon v)(\delta)
=
\Gamma_\delta(v).
\]

If

\[
\mathcal O_\varepsilon v=0,
\]

then

\[
\chi(\delta)p_v(\delta)=0
\]

for almost every \(0<\delta<\varepsilon\).

Since

\[
\chi(\delta)>0
\qquad
(\delta>0),
\]

we obtain

\[
p_v(\delta)=0
\]

on a set of positive measure.  A polynomial with that property is identically
zero, hence

\[
v=0.
\]

Therefore

\[
\boxed{
\mathcal O_\varepsilon
\text{ is injective for every }\varepsilon>0.
}
\]

So infinite edge flatness does not conflict with exact finite-dimensional
detectability.

---

# II. Gramian properties

## 3. Positive Gramian

Define

\[
A(\varepsilon)
=
\mathcal O_\varepsilon^*
\mathcal O_\varepsilon.
\]

In the standard basis,

\[
\boxed{
A(\varepsilon)_{ij}
=
\int_0^\varepsilon
e^{-2/\delta^2}
\delta^{i+j}
\,d\delta,
\qquad
0\le i,j\le d-1.
}
\]

For \(0\ne v\in E\),

\[
\langle A(\varepsilon)v,v\rangle
=
\int_0^\varepsilon
e^{-2/\delta^2}
|p_v(\delta)|^2
\,d\delta
>0.
\]

Hence

\[
\boxed{
A(\varepsilon)>0
\qquad
(\varepsilon>0).
}
\]

Thus

\[
\boxed{
D(\varepsilon)
:=
\det A(\varepsilon)
>0
\qquad
(\varepsilon>0).
}
\]

---

## 4. Rank-one growth

Differentiating the Gramian entrywise gives

\[
A'(\varepsilon)
=
\Gamma_\varepsilon^*
\Gamma_\varepsilon.
\]

Because only one output component is used,

\[
\boxed{
\operatorname{rank}A'(\varepsilon)=1
}
\]

for every \(\varepsilon>0\).

Thus even the stronger condition

\[
\operatorname{rank}A'(\varepsilon)\le1
\]

does not forbid a positive infinitely-flat determinant.

The rank-\(\le2\) growth law of the actual two-edge Weil Gramian is therefore
not, by itself, a rigidity mechanism.

---

## 5. Infinite flatness of the whole matrix

For every \(M\ge0\) and every pair \(i,j\),

\[
e^{-2/\delta^2}\delta^{i+j}
=
o(\delta^M)
\qquad
(\delta\downarrow0).
\]

Hence

\[
A(\varepsilon)_{ij}
=
o(\varepsilon^M)
\qquad
\forall M.
\]

Since \(E\) is finite dimensional,

\[
\boxed{
\|A(\varepsilon)\|
=
o(\varepsilon^M)
\qquad
\forall M.
}
\]

Consequently

\[
\boxed{
D(\varepsilon)
=
o(\varepsilon^M)
\qquad
\forall M.
}
\]

So the model has exactly the apparently paradoxical pair

\[
\boxed{
D(\varepsilon)>0
\quad(\varepsilon>0),
}
\]

and

\[
\boxed{
D
\text{ is flat to every algebraic order at }0.
}
\]

There is no contradiction in \(C^\infty\).

Only a quasi-analyticity or equivalent rigidity input could turn this into a
contradiction.

---

# III. Continuous Cauchy-Binet is also satisfied

## 6. Sample minors

For \(x=(\delta,+)\), the scalar observation row is

\[
\bigl(
\chi(\delta),
\chi(\delta)\delta,
\ldots,
\chi(\delta)\delta^{d-1}
\bigr).
\]

Given distinct sample points

\[
0<\delta_1<\cdots<\delta_d<\varepsilon,
\]

the sampled determinant is

\[
\det
\bigl(
\chi(\delta_i)\delta_i^{j-1}
\bigr)_{i,j=1}^d.
\]

Factoring the common row weights gives

\[
\boxed{
\det
=
\left(\prod_{i=1}^d\chi(\delta_i)\right)
\prod_{1\le i<j\le d}
(\delta_j-\delta_i).
}
\]

This is nonzero for distinct positive samples.

Thus the finite sampled matrices separate \(E\), exactly as in the ratified
QA-2 existence theorem, while every matrix entry remains arbitrarily flat as
the samples approach the edge.

The continuous Cauchy-Binet identity then gives the positive canonical
determinant as the integral of these squared Vandermonde minors.

Therefore continuous Cauchy-Binet does not itself generate a finite-order
edge coefficient.

---

# IV. The no-go survives the prime-hinge Volterra structure

## 7. Flat observations are exact second-order Volterra germs

The ratified prime-hinge local term has the form

\[
H_f(\delta)
=
\int_0^\delta
(\delta-t)f(t)\,dt.
\]

The abstract model above can be placed inside exactly this class.

For \(j=0,\ldots,d-1\), define

\[
h_j(\delta)
=
\chi(\delta)\delta^j.
\]

Because \(h_j\) is \(C^\infty\)-flat,

\[
h_j(0)=h_j'(0)=0.
\]

Set

\[
f_j(t)
=
h_j''(t)
\qquad
(t>0).
\]

Since every derivative of \(e^{-1/t^2}\) is a polynomial in \(t^{-1}\) times
\(e^{-1/t^2}\),

\[
f_j\in L^2(0,\varepsilon)
\]

for every \(\varepsilon>0\).

Twice integrating gives

\[
\boxed{
h_j(\delta)
=
\int_0^\delta
(\delta-t)f_j(t)\,dt.
}
\]

Therefore, for

\[
f_v
=
\sum_{j=0}^{d-1}v_j f_j,
\]

we have

\[
\boxed{
\chi(\delta)p_v(\delta)
=
\int_0^\delta
(\delta-t)f_v(t)\,dt.
}
\]

Thus the entire countermodel can be realized by a finite-dimensional family
of the **same local Volterra transforms** that arise from a prime hinge.

---

## 8. Consequence for QA-1

The following implication is false at the level of local \(L^2\) germs:

\[
\text{finite-dimensional Volterra family}
+
\text{injective edge observation}
+
\text{superflatness}
\Longrightarrow
\text{finite-order edge jet}.
\]

Even a one-site finite-dimensional Volterra family may be:

- injectively detectable on every collar;
- pointwise \(C^\infty\)-flat;
- positive at the Gram-determinant level;
- infinitely flat at every finite jet.

Therefore singular-site localization alone is not enough.

The missing information cannot be supplied by the local Volterra kernel
\((\delta-t)\) in isolation.

---

# V. Exact boundary of the determinant strategy

## 9. What QA-3 achieved

QA-3 successfully removed the arbitrary choices from the finite edge-matrix
certificate.

The canonical objects

\[
A_c(\varepsilon)
\]

and

\[
D_c(\varepsilon)
\]

remain useful because they reduce the obstruction to intrinsic finite
dimensions and expose any future rigidity as a scalar/operator statement.

That canonicalization is genuine.

---

## 10. What DET-1 rules out

The following data, even taken together, are insufficient to prove

\[
\mathcal E_c=0:
\]

\[
\boxed{
\begin{array}{c}
A_c(\varepsilon)>0,\\[2mm]
A_c'(\varepsilon)\succeq0,\\[2mm]
\operatorname{rank}A_c'(\varepsilon)\le2,\\[2mm]
D_c(\varepsilon)>0,\\[2mm]
A_c,D_c\text{ superflat at }0,\\[2mm]
\text{finite singular-site localization},\\[2mm]
\text{local second-order Volterra structure}.
\end{array}
}
\]

An abstract model can satisfy all of these without being zero.

Therefore no proof may legitimately close the edge obstruction from these
properties alone.

---

# VI. What must enter next

## 11. The first-kind global coupling becomes load-bearing

The countermodel assigns its local \(L^2\) germs freely.

The actual Weil problem does not.

A genuine kernel vector satisfies the global interior equation

\[
\boxed{
G_cu=0.
}
\]

Equivalently, after distributional differentiation, its endpoint and interior
germs participate in the singular integral/delay system containing:

- the Stieltjes/Cauchy edge term;
- finitely many arithmetic translations;
- the archimedean remainder;
- and, at a prime-power threshold, one direct opposite-edge coupling.

Therefore the only remaining route capable of excluding the countermodel is
to prove that the global first-kind equation prevents the local singular germs
from carrying a common nontrivial flat divisor.

---

## 12. Common-flat-factor formulation

The abstract countermodel has the factorization

\[
\Gamma_\delta
=
\chi(\delta)P(\delta),
\]

where

\[
\chi(\delta)=e^{-1/\delta^2}
\]

is a nonzero infinitely-flat scalar factor and \(P(\delta)\) is an analytic
finite-dimensional polynomial observation.

This exposes a sharper target.

A flat-but-leaking Weil obstruction would require the exterior observation
family, or its nonzero Plücker coordinates, to possess an analogous
nontrivial flat factor generated by the local singular germs.

Thus the missing theorem may be formulated as:

\[
\boxed{
\text{WEIL FIRST-KIND FLAT-DIVISOR EXCLUSION}
}
\]

> On the finite-dimensional kernel quotient
> \(\mathcal E_c\), the coupled screw-kernel singular integral/delay equation
> admits no nonzero observation family whose full-rank Plücker coordinates
> share an infinitely-flat edge divisor.

Any theorem of this form would exclude the explicit countermodel mechanism
and force a finite-order determinant contribution.

---

# VII. Result of this NF pass

The canonical determinant is **not** rigid merely because it is:

- positive;
- superflat;
- generated by a rank-\(\le2\) positive derivative;
- the continuous Cauchy-Binet average of finite edge minors;
- assembled from finitely many second-order local Volterra germs.

There is an explicit \(d\)-dimensional countermodel satisfying all of those
properties.

Therefore

\[
\boxed{
\text{CANONICALIZATION}
\ne
\text{RIGIDITY}.
}
\]

The determinant route remains useful only after the actual first-kind Weil
equation is inserted as a constraint on the local germ family.

---

# VIII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-1 / FIRST-KIND FLAT-DIVISOR EXCLUSION}.
}
\]

The next pass should work with the actual coupled equations

\[
F_u''(c+\delta)
=
\frac12\mathcal C_{+,c}u(\delta)
+
\mathcal D_{+,c}u(\delta)
+
\mathcal R_{+,u}(\delta)
\]

and its left-edge analogue, together with

\[
G_cu=0
\quad\text{on }(-c,c),
\]

to determine whether a finite-dimensional nonzero kernel family can support a
common infinitely-flat divisor across all full-rank edge observations.

The first useful subtargets are:

1. identify which pieces of the exterior equation are analytic in
   \(\delta\) on the kernel family;
2. isolate the local \(L^2\) germ terms that could carry a flat divisor;
3. transport those germ terms through the interior first-kind equation;
4. test whether the resulting finite germ-coupling system has an injective
   analytic coefficient matrix or a finite-order determinant.

No such Weil-specific exclusion is proved in this pass.

---

# IX. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified sharpness/no-go residue.

No public promotion and no canonical cursor movement are asserted.
