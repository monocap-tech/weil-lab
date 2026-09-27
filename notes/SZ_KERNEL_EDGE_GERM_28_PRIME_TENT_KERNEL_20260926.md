# SZ-KERNEL-EDGE-GERM-28 — All-center prime-tent kernel reduction and one-delay classification

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-27  
**Target tested:** PRIME-TENT KERNEL CLASSIFICATION  
**Public promotion:** forbidden

## 0. Objective

GERM-27 identified an exact prime-invisible core in the range

\[
\log2<L<\log4,
\qquad
L=2c,
\]

but did not classify the kernel of the complete all-center prime-tent
observation.

This pass performs that reduction.

The full continuum family of movable-center prime tents is equivalent to one
finite translation operator on the zero-extended source:

\[
\boxed{
(\mathsf P_cf)(x)
=
\sum_{\lambda\in\mathscr H_c^\circ}
a_\lambda
\left[
f(x-\lambda)+f(x+\lambda)
\right].
}
\]

Precisely,

\[
\boxed{
\mathscr P_h(\delta)f=0
\text{ for every admissible }(h,\delta)
\iff
\mathsf P_cf=0
\text{ a.e. on }(0,L).
}
\]

This converts the prime-tent kernel problem into a finite translation
equation.

In the entire one-prime-base regime

\[
\boxed{
\log2<L\le\log3,
}
\]

the translation equation can be solved exactly:

\[
\boxed{
\ker\mathsf P_c
=
L^2(L-\log2,\log2).
}
\]

Thus the GERM-27 prime-invisible core is not merely contained in the
all-center prime kernel there; it is the whole ambient prime kernel.

Combining this with GERM-27's kernel exclusion gives

\[
\boxed{
K_c^{\rm ps}
=
K_c\cap\ker\mathsf P_c
=
\{0\}
}
\]

throughout the one-prime-base regime.

Consequently the prime translation channel has a positive fixed-scale
singular-value floor on the finite-dimensional regular kernel.

The multi-prime kernel remains open.

---

# I. The finite prime translation operator

## 1. Active delays

Let

\[
\mathscr H_c^\circ
=
\left\{
\lambda=\log n:
\Lambda(n)\ne0,\;
0<\lambda<L
\right\},
\]

and

\[
a_\lambda
=
\frac{\Lambda(n)}{\sqrt n}.
\]

Extend

\[
f\in L^2(0,L)
\]

by zero to all of \(\mathbb R\).

Define

\[
\boxed{
(\mathsf P_cf)(x)
=
\sum_{\lambda\in\mathscr H_c^\circ}
a_\lambda
\left[
f(x-\lambda)+f(x+\lambda)
\right],
\qquad
0<x<L.
}
\]

Because the active delay set is finite,

\[
\mathsf P_c:
L^2(0,L)\to L^2(0,L)
\]

is bounded.

---

# II. Relation to movable-center tents

## 2. Prime adjacency germ

GERM-27 defined

\[
(\mathcal C_hf)(t)
=
\sum_{\lambda}
a_\lambda
\left[
\Sigma_{h-\lambda}f(t)
+
\Sigma_{h+\lambda}f(t)
\right].
\]

Expanding the symmetrizations gives

\[
\begin{aligned}
(\mathcal C_hf)(t)
&=
\sum_\lambda a_\lambda
\bigl[
f(h-\lambda+t)
+
f(h-\lambda-t)\\
&\qquad\qquad
+
f(h+\lambda+t)
+
f(h+\lambda-t)
\bigr].
\end{aligned}
\]

Group the terms at the two points

\[
h+t,
\qquad
h-t.
\]

Then

\[
\boxed{
(\mathcal C_hf)(t)
=
(\mathsf P_cf)(h+t)
+
(\mathsf P_cf)(h-t).
}
\]

---

## 3. Tent field

GERM-27 also gives

\[
\mathscr P_h(\delta)f
=
\int_0^\delta
(\delta-t)
(\mathcal C_hf)(t)\,dt.
\]

Therefore, distributionally,

\[
\boxed{
\frac{d^2}{d\delta^2}
\mathscr P_h(\delta)f
=
(\mathsf P_cf)(h+\delta)
+
(\mathsf P_cf)(h-\delta).
}
\]

This is the exact bridge between the continuum tent family and the single
translation operator.

---

# III. All-center equivalence

## 4. Translation kernel implies tent kernel

Assume

\[
\mathsf P_cf=0
\quad
\text{a.e. on }(0,L).
\]

Then

\[
\mathcal C_hf(t)=0
\]

for every admissible center/scale almost everywhere.

Since every prime tent satisfies

\[
\mathscr P_h(0)=0,
\qquad
\partial_\delta\mathscr P_h(0)=0,
\]

we obtain

\[
\boxed{
\mathscr P_h(\delta)f=0
}
\]

for every admissible \((h,\delta)\).

---

## 5. Tent kernel implies translation kernel

Conversely assume

\[
\mathscr P_h(\delta)f=0
\]

for every

\[
h\in(0,L),
\qquad
0<\delta<\min(h,L-h).
\]

Set

\[
g=\mathsf P_cf.
\]

Then

\[
\boxed{
g(h+t)+g(h-t)=0
}
\]

for almost every admissible \((h,t)\).

The map

\[
(x,y)
\longleftrightarrow
\left(
h=\frac{x+y}{2},
\;
t=\frac{|x-y|}{2}
\right)
\]

shows that

\[
\boxed{
g(x)+g(y)=0
}
\]

for almost every pair

\[
(x,y)\in(0,L)^2.
\]

By Fubini, for almost every \(x_1,x_2\), choose a common generic \(y\).
Then

\[
g(x_1)=-g(y)=g(x_2).
\]

Thus \(g\) is almost everywhere constant.

Substituting back into

\[
g(x)+g(y)=0
\]

gives

\[
2g=0.
\]

Hence

\[
\boxed{
g=0.
}
\]

Therefore

\[
\boxed{
\bigcap_{h,\delta}
\ker\mathscr P_h(\delta)
=
\ker\mathsf P_c.
}
\]

This is the complete all-center reduction.

---

# IV. No-active-prime regime

## 6. Smallest support

If

\[
L\le\log2,
\]

there is no strict interior active prime delay.

Therefore

\[
\boxed{
\mathsf P_c=0
}
\]

on all of

\[
L^2(0,L).
\]

So the ambient prime-tent kernel is the whole source space.

However GERM-8's small-window positivity input gives

\[
\boxed{
K_c=\{0\}
}
\]

in this regime.

Thus the absence of prime observation carries no actual regular kernel
obstruction.

---

# V. One-prime-base regime

## 7. Only \(\log2\) is active

Assume

\[
\boxed{
a:=\log2<L\le\log3.
}
\]

Because

\[
\log3<2\log2,
\]

we also have

\[
L<2a.
\]

The strict active delay set is exactly

\[
\mathscr H_c^\circ=\{a\}.
\]

Hence

\[
\boxed{
(\mathsf P_cf)(x)
=
a_2
\left[
f(x-a)+f(x+a)
\right],
}
\]

where

\[
a_2=\frac{\log2}{\sqrt2}>0.
\]

The scalar coefficient is irrelevant to the kernel.

---

# VI. Exact one-delay kernel

## 8. Left boundary equation

Take

\[
0<x<L-a.
\]

Since

\[
L-a<a,
\]

we have

\[
x<a.
\]

Therefore

\[
x-a<0,
\]

so the zero extension gives

\[
f(x-a)=0.
\]

The equation

\[
\mathsf P_cf(x)=0
\]

then gives

\[
f(x+a)=0.
\]

As \(x\) ranges over

\[
(0,L-a),
\]

the point

\[
x+a
\]

ranges over

\[
(a,L).
\]

Therefore

\[
\boxed{
f=0
\quad\text{a.e. on }(a,L).
}
\]

---

## 9. Right boundary equation

Take

\[
a<x<L.
\]

Because

\[
L<2a,
\]

we have

\[
x+a>L.
\]

Hence

\[
f(x+a)=0.
\]

The translation equation gives

\[
f(x-a)=0.
\]

As \(x\) ranges over

\[
(a,L),
\]

the point

\[
x-a
\]

ranges over

\[
(0,L-a).
\]

Thus

\[
\boxed{
f=0
\quad\text{a.e. on }(0,L-a).
}
\]

---

## 10. The middle interval is free

The only source interval not killed by Sections 8--9 is

\[
\boxed{
J_c=(L-a,a).
}
\]

Conversely, if

\[
\operatorname{supp}f\subseteq J_c,
\]

then for every

\[
x\in(0,L),
\]

both

\[
x-a
\quad\text{and}\quad
x+a
\]

miss \(J_c\) whenever they lie inside the support interval.

Equivalently,

\[
\mathsf P_cf=0.
\]

Therefore

\[
\boxed{
\ker\mathsf P_c
=
L^2(J_c),
\qquad
a<L\le\log3.
}
\]

This is the exact one-delay classification.

---

# VII. Relation to GERM-27

## 11. Prime-invisible core is the whole ambient kernel

GERM-27 proved

\[
L^2(J_c)
\subseteq
\ker(\text{all movable-center prime observations})
\]

through the larger range

\[
a<L<2a.
\]

The all-center equivalence now shows that in the one-prime-base subrange

\[
a<L\le\log3,
\]

there are no additional cancellation modes:

\[
\boxed{
\ker(\text{all prime tents})
=
L^2(J_c).
}
\]

So geometric invisibility completely explains the prime kernel there.

---

# VIII. Intersection with the regular Weil kernel

## 12. Pure-core exclusion

GERM-27 proved

\[
\boxed{
K_c\cap L^2(J_c)=\{0\}
}
\]

by reducing a core-supported regular kernel vector to the injective
archimedean endpoint transform of GERM-2.

Combining this with the exact ambient classification gives

\[
\boxed{
K_c\cap\ker\mathsf P_c
=
\{0\},
\qquad
\log2<L\le\log3.
}
\]

Using the terminology registry,

\[
\boxed{
K_c^{\rm ps}=\{0\}.
}
\]

Thus no nonzero regular kernel vector is silent to the complete prime
translation channel in the entire one-prime-base regime.

---

# IX. Fixed-scale prime coercivity on \(K_c\)

## 13. Positive singular-value floor

Since

\[
K_c
\]

is finite dimensional and

\[
\mathsf P_c|_{K_c}
\]

is injective, compactness of the unit sphere gives

\[
\boxed{
\kappa_c
:=
\inf_{\substack{f\in K_c\\
\|f\|_2=1}}
\|\mathsf P_cf\|_2
>0.
}
\]

Therefore

\[
\boxed{
\|\mathsf P_cf\|_{L^2(0,L)}
\ge
\kappa_c
\|f\|_{L^2(0,L)}
\qquad
(f\in K_c).
}
\]

This is a genuine fixed-scale prime-channel coercivity theorem.

It is not a shrinking-collar estimate.

---

# X. Finite all-center observation extraction

## 14. From \(\mathsf P_c\) back to tents

The continuum tent family is jointly injective on

\[
K_c
\]

in the one-prime-base regime.

Because \(K_c\) is finite dimensional, finitely many bounded scalar
functionals extracted from finitely many tent observations already separate
\(K_c\).

Thus there exist finitely many admissible centers/scales and local test
functionals yielding an injective finite observation map on \(K_c\).

This is an existential finite reduction.

No canonical choice or shrinking-scale rate is asserted.

---

# XI. Multi-prime regime

## 15. Second prime base enters

If

\[
L>\log3,
\]

the delay

\[
\log3
\]

is active in addition to

\[
\log2.
\]

The translation operator becomes

\[
\mathsf P_cf
=
a_2(\tau_a+\tau_{-a})f
+
a_3(\tau_b+\tau_{-b})f
+\cdots,
\]

with

\[
a=\log2,
\qquad
b=\log3.
\]

Because

\[
a/b\notin\mathbb Q,
\]

the associated translation geometry is no longer reducible to one finite
path-fiber decomposition.

---

## 16. What remains known below \(\log4\)

For

\[
\log3<L<\log4,
\]

GERM-27 still gives

\[
\boxed{
L^2(J_c)\subseteq\ker\mathsf P_c,
\qquad
J_c=(L-\log2,\log2).
}
\]

Thus the multi-prime ambient kernel remains infinite dimensional in this
range.

But this pass does not prove that

\[
\ker\mathsf P_c=L^2(J_c).
\]

Additional cancellation modes between the \(\log2\) and \(\log3\) shifts may
exist.

---

## 17. Above the geometric transition

For

\[
L\ge\log4,
\]

the common prime-invisible interval disappears.

The operator kernel could nevertheless remain nontrivial because distinct
shift channels can cancel.

No general injectivity theorem for

\[
\mathsf P_c
\]

is proved here.

Likewise, no general classification of

\[
K_c^{\rm ps}
=
K_c\cap\ker\mathsf P_c
\]

is proved in the multi-prime regime.

---

# XII. Prime-silent vectors inside \(K_c\)

## 18. Structural meaning

Take

\[
f\in K_c^{\rm ps}.
\]

Then:

1. the complete prime centered second-difference field vanishes at every
   movable center;
2. the prime contribution to the screw potential is affine on the old
   interval;
3. because the total screw potential is constant on the old interval, the
   archimedean contribution is affine with the opposite slope.

Thus the multi-prime prime-silent problem is a coupled
prime-affine / archimedean-affine classification problem.

This is a much smaller target than the original edge obstruction.

---

# XIII. Result of this NF pass

The all-center prime-tent kernel has been reduced exactly to one finite
translation operator:

\[
\boxed{
\ker(\text{all movable-center prime tents})
=
\ker\mathsf P_c.
}
\]

In the one-prime-base regime

\[
\log2<L\le\log3,
\]

the kernel is explicit:

\[
\boxed{
\ker\mathsf P_c
=
L^2(L-\log2,\log2).
}
\]

But the actual regular Weil kernel has zero intersection with that ambient
blind sector:

\[
\boxed{
K_c^{\rm ps}
=
\{0\}.
}
\]

Hence the prime channel has a fixed-scale norm gap on \(K_c\):

\[
\boxed{
\|\mathsf P_cf\|_2
\ge
\kappa_c\|f\|_2.
}
\]

This is a genuine positive result.

The unresolved prime-tent kernel problem begins exactly when the second prime
base enters:

\[
\boxed{
L>\log3.
}
\]

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-29 / MULTIPRIME PRIME-SILENT KERNEL}.
}
\]

The next pass should analyze

\[
K_c^{\rm ps}
=
K_c\cap\ker\mathsf P_c
\]

once \(\log3\) is active.

The most useful routes are:

1. exploit the incommensurate \(\log2/\log3\) translation geometry;
2. derive the exact affine prime-potential condition on \(K_c^{\rm ps}\);
3. combine it with the complete archimedean moment system;
4. determine whether
   \[
   K_c^{\rm ps}=0
   \]
   persists beyond the one-prime-base regime.

A proof of prime-silent triviality would give fixed-scale prime coercivity on
the entire regular kernel and sharply constrain the remaining superflat edge
obstruction.

No multi-prime prime-silent classification is proved in this pass.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified all-center prime-kernel classification result.

No public promotion and no canonical cursor movement are asserted.
