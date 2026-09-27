# SZ-KERNEL-EDGE-GERM-29 — Two-prime prime-silent classification through the log4 threshold

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-28  
**Target tested:** MULTIPRIME PRIME-SILENT KERNEL  
**Public promotion:** forbidden

## 0. Objective

GERM-28 reduced the complete all-center prime-tent kernel to the finite
translation operator

\[
(\mathsf P_cf)(x)
=
\sum_{\lambda\in\mathscr H_c^\circ}
a_\lambda
\left[
f(x-\lambda)+f(x+\lambda)
\right]
\]

and classified its kernel in the one-prime-base regime

\[
\log2<L\le\log3,
\qquad
L=2c.
\]

The next unresolved regime begins when \(\log3\) becomes active.

This pass solves the entire first multiprime interval

\[
\boxed{
\log3<L\le\log4.
}
\]

Write

\[
a=\log2,
\qquad
b=\log3.
\]

Because

\[
b<L\le2a=\log4,
\]

the strict active prime-power delays are exactly

\[
\boxed{
a,\ b.
}
\]

The two-delay translation equation still has the same kernel as the
one-delay equation:

\[
\boxed{
\ker\mathsf P_c
=
L^2(L-a,a).
}
\]

Thus the \(\log3\) channel creates no new ambient prime-silent cancellation
modes before the \(\log4\) threshold.

At the endpoint

\[
L=\log4,
\]

the middle interval collapses and

\[
\boxed{
\ker\mathsf P_c=\{0\}.
}
\]

Combining with GERM-27 gives the stronger regular-kernel statement

\[
\boxed{
K_c^{\rm ps}
=
K_c\cap\ker\mathsf P_c
=
\{0\}
\qquad
(0<L\le\log4).
}
\]

So prime-silent triviality, and therefore fixed-scale prime coercivity on the
finite-dimensional regular kernel, persists through the entire first
multiprime regime.

The next genuine transition occurs only after the delay

\[
\log4=2\log2
\]

itself becomes active.

---

# I. Two-delay regime

## 1. Active set

Assume

\[
\boxed{
b<L\le2a,
}
\]

where

\[
a=\log2,
\qquad
b=\log3.
\]

Since

\[
2a=\log4,
\]

the delay \(2a\) is not strictly active.

There are no other prime-power logarithms between \(b\) and \(2a\).

Hence

\[
\boxed{
\mathscr H_c^\circ=\{a,b\}.
}
\]

Write

\[
A=a_a=\frac{\log2}{\sqrt2}>0,
\]

\[
B=a_b=\frac{\log3}{\sqrt3}>0.
\]

The prime translation equation is

\[
\boxed{
A[f(x-a)+f(x+a)]
+
B[f(x-b)+f(x+b)]
=
0
}
\]

for almost every

\[
0<x<L,
\]

with zero extension outside \((0,L)\).

---

# II. Boundary parameters

## 2. Define the two boundary widths

Set

\[
\boxed{
u=L-b,
\qquad
v=L-a.
}
\]

Because

\[
b>a,
\]

we have

\[
u<v.
\]

Because

\[
L\le2a,
\]

we have

\[
v\le a.
\]

Also

\[
u<L-a=v<a<b.
\]

The candidate invisible core is

\[
\boxed{
J=(v,a)=(L-a,a).
}
\]

It is nonempty for

\[
L<2a
\]

and empty at

\[
L=2a.
\]

---

# III. One-channel right boundary strip

## 3. Centers \(u<x<v\)

Take

\[
u<x<v.
\]

Then:

- \(x<a\), so
  \[
  x-a<0,
  \qquad
  x-b<0;
  \]
- \(x>u=L-b\), so
  \[
  x+b>L;
  \]
- \(x<v=L-a\), so
  \[
  x+a<L.
  \]

Thus the only surviving translation term is

\[
Af(x+a).
\]

Hence

\[
f(x+a)=0.
\]

As \(x\) ranges over \((u,v)\),

\[
x+a
\]

ranges over

\[
(a+u,L).
\]

Therefore

\[
\boxed{
f=0
\quad\text{on }(a+u,L).
}
\]

---

# IV. One-channel left boundary strip

## 4. Centers \(a<x<b\)

Take

\[
a<x<b.
\]

Because

\[
x>a\ge v,
\]

we have

\[
x+a>L.
\]

Also

\[
x+b>L
\]

and

\[
x-b<0.
\]

The only surviving term is

\[
Af(x-a).
\]

Therefore

\[
f(x-a)=0.
\]

As \(x\) ranges over \((a,b)\),

\[
x-a
\]

ranges over

\[
(0,b-a).
\]

Thus

\[
\boxed{
f=0
\quad\text{on }(0,b-a).
}
\]

---

# V. Arithmetic inequalities needed for propagation

## 5. Compare the boundary widths

We need two elementary inequalities.

First,

\[
u\le b-a.
\]

This is equivalent to

\[
L-b\le b-a,
\]

or

\[
L\le2b-a.
\]

Since

\[
L\le2a,
\]

it suffices that

\[
2a\le2b-a,
\]

that is,

\[
3a\le2b.
\]

Exponentiating,

\[
2^3\le3^2,
\]

which is

\[
8\le9.
\]

Therefore

\[
\boxed{
u\le b-a.
}
\]

Second,

\[
b\ge a+u.
\]

This is the same inequality:

\[
b\ge a+L-b
\iff
L\le2b-a.
\]

Hence

\[
\boxed{
b\ge a+u.
}
\]

---

# VI. Propagate the right-boundary zero

## 6. Centers \(0<x<u\)

Take

\[
0<x<u.
\]

Then:

\[
x<a<b,
\]

so the negative shifts are outside the support.

Both positive shifts are active:

\[
x+a<L,
\qquad
x+b<L.
\]

The equation is

\[
\boxed{
Af(x+a)+Bf(x+b)=0.
}
\]

But

\[
x+b>b\ge a+u,
\]

and

\[
x+b<L.
\]

Section III already gives

\[
f=0
\quad\text{on }(a+u,L).
\]

Therefore

\[
f(x+b)=0.
\]

Hence

\[
f(x+a)=0.
\]

As \(x\) ranges over \((0,u)\),

\[
x+a
\]

ranges over

\[
(a,a+u).
\]

Combining with Section III:

\[
\boxed{
f=0
\quad\text{on }(a,L).
}
\]

---

# VII. Propagate the left-boundary zero

## 7. Centers \(b<x<L\)

Take

\[
b<x<L.
\]

Both positive shifts lie outside the support.

Both negative shifts are active:

\[
x-a>0,
\qquad
x-b>0.
\]

The equation is

\[
\boxed{
Af(x-a)+Bf(x-b)=0.
}
\]

Now

\[
0<x-b<L-b=u\le b-a.
\]

Section IV gives

\[
f=0
\quad\text{on }(0,b-a).
\]

Therefore

\[
f(x-b)=0.
\]

Hence

\[
f(x-a)=0.
\]

As \(x\) ranges over \((b,L)\),

\[
x-a
\]

ranges over

\[
(b-a,v).
\]

Combining with Section IV:

\[
\boxed{
f=0
\quad\text{on }(0,v).
}
\]

---

# VIII. Exact ambient kernel

## 8. Only the middle interval survives

Sections VI--VII show that every solution of

\[
\mathsf P_cf=0
\]

satisfies

\[
f=0
\quad\text{on }(0,v)\cup(a,L).
\]

Therefore

\[
\operatorname{supp}f
\subseteq
(v,a)
=
(L-a,a).
\]

Conversely, GERM-27's geometric prime-invisible-core theorem applies whenever

\[
a<L<2a.
\]

It gives

\[
L^2(L-a,a)
\subseteq
\ker\mathsf P_c.
\]

Hence, for

\[
b<L<2a,
\]

\[
\boxed{
\ker\mathsf P_c
=
L^2(L-a,a).
}
\]

At

\[
L=2a,
\]

the interval is empty and Sections VI--VII give

\[
\boxed{
\ker\mathsf P_c=\{0\}.
}
\]

Thus the same formula holds with the convention

\[
L^2(\varnothing)=\{0\}.
\]

---

# IX. Combined classification through log4

## 9. Join with GERM-28

GERM-28 already proved

\[
\ker\mathsf P_c
=
L^2(L-a,a)
\]

for

\[
a<L\le b.
\]

The present pass proves the same formula for

\[
b<L\le2a.
\]

Therefore:

\[
\boxed{
\ker\mathsf P_c
=
L^2(L-\log2,\log2)
\qquad
(\log2<L\le\log4).
}
\]

This is the complete ambient prime-tent kernel classification through the
first two prime bases and up to the first repeated \(2\)-power threshold.

---

# X. Prime-silent regular kernel

## 10. Below log4

For

\[
a<L<2a,
\]

GERM-27 proved the pure-core exclusion

\[
\boxed{
K_c
\cap
L^2(L-a,a)
=
\{0\}.
}
\]

At

\[
L=2a,
\]

the ambient prime kernel itself is zero.

Therefore

\[
\boxed{
K_c^{\rm ps}
=
K_c\cap\ker\mathsf P_c
=
\{0\}
\qquad
(a<L\le2a).
}
\]

---

## 11. Include the small-window regime

For

\[
L\le a,
\]

GERM-8's Bombieri--Yoshida small-window input gives

\[
K_c=\{0\}.
\]

Hence

\[
K_c^{\rm ps}=\{0\}
\]

there as well.

Thus the full result is

\[
\boxed{
K_c^{\rm ps}=\{0\}
\qquad
(0<L\le\log4).
}
\]

No nonzero regular kernel vector is prime-silent anywhere below or at the
\(\log4\) support threshold.

---

# XI. Fixed-scale prime coercivity through log4

## 12. Finite-dimensional consequence

Let

\[
0<L\le\log4.
\]

If

\[
K_c\ne\{0\},
\]

then

\[
\mathsf P_c|_{K_c}
\]

is injective.

Because \(K_c\) is finite dimensional,

\[
\boxed{
\kappa_c
=
\inf_{\substack{f\in K_c\\
\|f\|_2=1}}
\|\mathsf P_cf\|_2
>0.
}
\]

Therefore

\[
\boxed{
\|\mathsf P_cf\|_2
\ge
\kappa_c\|f\|_2
\qquad
(f\in K_c).
}
\]

This extends the GERM-28 fixed-scale prime-channel coercivity theorem through
the entire first multiprime interval.

No uniformity in \(c\) is asserted.

No shrinking-collar rate is asserted.

---

# XII. What changes after log4

## 13. The repeated dyadic delay enters

If

\[
L>\log4=2a,
\]

the delay

\[
2a=\log4
\]

becomes active.

The translation operator now contains at least

\[
\boxed{
a_2(\tau_a+\tau_{-a})
+
a_3(\tau_b+\tau_{-b})
+
a_4(\tau_{2a}+\tau_{-2a}).
}
\]

The common central shadow

\[
(L-a,a)
\]

has already disappeared.

The boundary proof above no longer applies because:

1. the intervals \(v=L-a\) and \(a\) have reversed order;
2. centers near \(a\) see both \(+a\) and \(-a\);
3. the new \(2a\)-channel couples the two support ends;
4. cancellation can occur among three distinct shift lengths.

Thus

\[
\boxed{
L=\log4
}
\]

is the first genuine transition in the ambient prime-silent equation.

---

# XIII. Prime-affine / archimedean-affine form

## 14. General prime-silent regular vector

For any support scale, take

\[
f\in K_c^{\rm ps}.
\]

Prime silence gives

\[
\mathsf P_cf=0.
\]

Equivalently, the prime part of the screw potential has zero second
distributional derivative on the old interval.

Therefore the prime potential is affine there:

\[
\boxed{
F_{\rm prime}(x)=\alpha x+\beta.
}
\]

Because the full screw potential is constant for a regular kernel vector,

\[
F_{\rm total}(x)=C,
\]

the non-prime/archimedean potential satisfies

\[
\boxed{
F_\infty(x)
=
-\alpha x+(C-\beta).
}
\]

Thus every multi-prime prime-silent vector satisfies an exact
archimedean-affine equation on the entire support interval.

This is the correct global formulation beyond the explicit boundary regime.

GERM-20/26 show that local archimedean flatness alone is not enough to solve
this equation.

The missing input is the simultaneous global translation recurrence

\[
\mathsf P_cf=0.
\]

---

# XIV. Result of this NF pass

The multiprime prime-silent kernel is completely classified through the
\(\log4\) threshold.

For

\[
\boxed{
\log2<L\le\log4,
}
\]

including the first two-prime interval,

\[
\boxed{
\ker\mathsf P_c
=
L^2(L-\log2,\log2).
}
\]

Consequently,

\[
\boxed{
K_c^{\rm ps}
=
\{0\}
\qquad
(0<L\le\log4).
}
\]

So the fixed-scale prime channel is coercive on every nonzero finite
regular kernel in this range.

The second prime base \(\log3\) does **not** create new prime-silent regular
directions.

The first unresolved transition is exactly

\[
\boxed{
L>\log4,
}
\]

when the repeated dyadic delay \(\log4\) enters and the common geometric blind
core disappears.

---

# XV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-30 / POST-LOG4 PRIME-SILENT BOUNDARY FIBERS}.
}
\]

The next pass should analyze the translation equation just above

\[
L=\log4
\]

with active delays

\[
\log2,\ \log3,\ \log4.
\]

The immediate targets are:

1. derive a finite boundary-fiber parametrization of
   \[
   \ker\mathsf P_c;
   \]
2. determine whether the ambient kernel becomes nonzero immediately after
   \(\log4\);
3. intersect those fibers with the global archimedean-affine condition for
   \(K_c^{\rm ps}\);
4. test whether prime-silent triviality persists even if the ambient prime
   kernel acquires cancellation modes.

No post-\(\log4\) classification is proved in this pass.

---

# XVI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified multiprime prime-silent classification result.

No public promotion and no canonical cursor movement are asserted.
