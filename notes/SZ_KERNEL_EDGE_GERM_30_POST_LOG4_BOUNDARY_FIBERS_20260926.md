# SZ-KERNEL-EDGE-GERM-30 — Post-log4 boundary fibers and prime-translation injectivity through log5

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-29  
**Target tested:** POST-LOG4 PRIME-SILENT BOUNDARY FIBERS  
**Public promotion:** forbidden

## 0. Objective

GERM-29 classified the all-center prime translation kernel through

\[
L=\log4.
\]

At that threshold the former geometric blind interval collapses and the
ambient prime operator becomes injective.

This pass asks whether nontrivial cancellation modes appear immediately after
\(\log4\), when the repeated dyadic delay

\[
\log4
\]

becomes active.

They do not.

In the entire next support regime

\[
\boxed{
\log4<L\le\log5,
}
\]

the strict active prime-power delays are exactly

\[
\boxed{
\log2,\quad\log3,\quad\log4.
}
\]

A complete boundary-fiber elimination shows

\[
\boxed{
\ker\mathsf P_c=\{0\}.
}
\]

Thus the ambient finite prime-translation operator is itself injective through
the whole post-\(\log4\), pre-\(\log5\) regime.

Consequently

\[
\boxed{
K_c^{\rm ps}=\{0\}
\qquad
(0<L\le\log5),
}
\]

and the fixed-scale prime coercivity theorem on the regular kernel extends
through the \(\log5\) threshold.

The proof reduces every hypothetical solution to one short left boundary
fiber and then derives two incompatible gain recurrences from the left and
right boundary equations.

---

# I. Active delays and weights

## 1. Arithmetic constants

Set

\[
\boxed{
a=\log2,
\qquad
b=\log3,
\qquad
c=\log4=2a,
\qquad
d=\log5.
}
\]

Assume

\[
\boxed{
c<L\le d.
}
\]

Because the activation convention is strict,

\[
\lambda<L,
\]

the delay \(d=\log5\) is not active even at \(L=d\).

Hence

\[
\boxed{
\mathscr H_c^\circ=\{a,b,c\}.
}
\]

Write the positive weights

\[
\boxed{
A=\frac{\log2}{\sqrt2},
\qquad
B=\frac{\log3}{\sqrt3},
\qquad
C=\frac{\log2}{2}.
}
\]

The prime translation equation is

\[
\boxed{
A[f(x-a)+f(x+a)]
+
B[f(x-b)+f(x+b)]
+
C[f(x-c)+f(x+c)]
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

# II. Stable boundary ordering

## 2. Short post-log4 width

Set

\[
\boxed{
u=L-c,
\qquad
s=c-b,
\qquad
r=b-a.
}
\]

Then

\[
u>0.
\]

Also

\[
u\le d-c=\log(5/4).
\]

Since

\[
5/4<4/3,
\]

we obtain

\[
\boxed{
u<s.
}
\]

And because

\[
4/3<3/2,
\]

\[
\boxed{
s<r.
}
\]

Define

\[
\boxed{
v=L-b=s+u,
\qquad
w=L-a=a+u.
}
\]

Since

\[
u<s
\]

and

\[
u<r,
\]

the ordering is

\[
\boxed{
0<u<s<v<a<w<b<c<L.
}
\]

This ordering is stable throughout

\[
c<L\le d.
\]

---

# III. The seven boundary equations

## 3. Leftmost centers: \(0<x<u\)

Only positive shifts survive:

\[
\boxed{
Af(x+a)+Bf(x+b)+Cf(x+c)=0.
}
\tag{E0}
\]

---

## 4. Centers \(u<x<v\)

The \(+c\) shift has left the support, while \(+a,+b\) remain:

\[
\boxed{
Af(x+a)+Bf(x+b)=0.
}
\tag{E1}
\]

---

## 5. Centers \(v<x<a\)

Only the \(+a\) shift survives:

\[
\boxed{
Af(x+a)=0.
}
\]

Hence

\[
\boxed{
f=0
\quad\text{on}\quad
(v+a,c).
}
\tag{Z1}
\]

---

## 6. Centers \(a<x<w\)

Only the two \(a\)-shifts survive:

\[
\boxed{
f(x+a)=-f(x-a).
}
\]

Let

\[
H(t)=f(t),
\qquad
0<t<u.
\]

Since

\[
x-a\in(0,u),
\qquad
x+a\in(c,L),
\]

we obtain

\[
\boxed{
f(c+t)=-H(t),
\qquad
0<t<u.
}
\tag{T}
\]

Thus the far-right boundary fiber is the negative copy of the far-left
fiber.

---

## 7. Centers \(w<x<b\)

Only the \(-a\) shift survives:

\[
\boxed{
Af(x-a)=0.
}
\]

As

\[
x-a\in(u,r),
\]

we obtain

\[
\boxed{
f=0
\quad\text{on}\quad
(u,r).
}
\tag{Z2}
\]

---

## 8. Centers \(b<x<c\)

Only \(-a\) and \(-b\) survive.

Set

\[
y=x-b,
\qquad
0<y<s.
\]

Then

\[
x-a=r+y.
\]

The equation is

\[
\boxed{
Af(r+y)+Bf(y)=0.
}
\]

Define

\[
\boxed{
\beta=\frac BA.
}
\]

Because

\[
f(y)=0
\quad
(u<y<s)
\]

by (Z2), we obtain

\[
\boxed{
f(r+y)=-\beta H(y),
\qquad
0<y<u,
}
\tag{M1}
\]

and

\[
\boxed{
f=0
\quad\text{on}\quad
(r+u,a).
}
\tag{Z3}
\]

---

## 9. Centers \(c<x<L\)

Write

\[
x=c+y,
\qquad
0<y<u.
\]

All positive shifts are outside the support, while all three negative shifts
survive.

Since

\[
c-a=a,
\qquad
c-b=s,
\]

the equation is

\[
\boxed{
Af(a+y)+Bf(s+y)+CH(y)=0.
}
\tag{ER}
\]

This will be one of the two equations determining the remaining interior
fiber.

---

# IV. Resolve the \(E1\) strip

## 10. A useful fixed location

Define

\[
\boxed{
d_0=a+s=3a-b.
}
\]

The zero interval (Z1) starts at

\[
v+a
=
a+s+u
=
d_0+u.
\]

Now write

\[
x=u+y,
\qquad
0<y<s
\]

in (E1).

Then

\[
x+a=a+u+y,
\]

and

\[
x+b=b+u+y.
\]

For

\[
0<y<s-u,
\]

we have

\[
x+b<c,
\]

and in fact

\[
x+b\in(d_0+u,c),
\]

so (Z1) gives

\[
f(x+b)=0.
\]

Hence

\[
f(x+a)=0.
\]

Thus

\[
\boxed{
f=0
\quad\text{on}\quad
(a+u,d_0).
}
\tag{Z4}
\]

---

## 11. The last \(u\)-piece of \(E1\)

For

\[
s-u<y<s,
\]

set

\[
t=y-(s-u),
\qquad
0<t<u.
\]

Then

\[
x+b=c+t,
\]

so by (T),

\[
f(x+b)=-H(t).
\]

Also

\[
x+a=d_0+t.
\]

Equation (E1) gives

\[
\boxed{
f(d_0+t)=\beta H(t),
\qquad
0<t<u.
}
\tag{M2}
\]

So every source interval except

\[
(a,a+u)
\]

has now been expressed either as zero or as a fixed scalar copy of the head
fiber \(H\).

---

# V. The only remaining interior fiber

## 12. Define \(U\)

Set

\[
\boxed{
U(t)=f(a+t),
\qquad
0<t<u.
}
\]

The whole source is now determined by \(H\) and \(U\).

It remains to combine the two boundary equations (E0) and (ER).

---

# VI. The offset \(u_0=\log(9/8)\)

## 13. Geometry of the \(\log3\)-shift

Since

\[
b-d_0
=
b-(3a-b)
=
2b-3a,
\]

define

\[
\boxed{
u_0
=
2b-3a
=
\log(9/8)
>0.
}
\]

This is exactly the offset at which the \(b\)-shift begins to intersect the
copy interval (M2).

There are two cases.

---

# VII. Case I: \(u\le u_0\)

## 14. Left boundary equation

Take

\[
0<t<u.
\]

Then

\[
b+t\ge d_0+u,
\]

because

\[
u\le u_0=b-d_0.
\]

Also

\[
b+t<c.
\]

Hence (Z1) gives

\[
f(b+t)=0.
\]

From (E0), using

\[
f(c+t)=-H(t),
\]

we obtain

\[
AU(t)-CH(t)=0.
\]

Thus

\[
\boxed{
U(t)=\gamma H(t),
}
\tag{L}
\]

where

\[
\boxed{
\gamma=\frac CA.
}
\]

---

## 15. Right boundary equation

Because

\[
u\le u_0=r-s,
\]

we have

\[
s+t<r
\]

for

\[
0<t<u.
\]

Since

\[
s+t>u,
\]

the interval (Z2) gives

\[
f(s+t)=0.
\]

Equation (ER) gives

\[
AU(t)+CH(t)=0,
\]

hence

\[
\boxed{
U(t)=-\gamma H(t).
}
\tag{R}
\]

Combining (L) and (R),

\[
H(t)=0
\]

for almost every

\[
0<t<u.
\]

Thus

\[
\boxed{
f=0.
}
\]

So no ambient prime-silent fiber exists whenever

\[
u\le u_0.
\]

Equivalently,

\[
L\le
c+u_0
=
\log(9/2).
\]

---

# VIII. Case II: \(u>u_0\)

## 16. The residual length

Set

\[
\boxed{
q=u-u_0>0.
}
\]

We will also need

\[
\boxed{
q<u_0.
}
\]

Indeed,

\[
u\le\log(5/4),
\]

and

\[
\log(5/4)
<
2\log(9/8),
\]

because

\[
\frac54
<
\left(\frac98\right)^2
=
\frac{81}{64},
\]

equivalently

\[
80<81.
\]

Thus

\[
u<2u_0,
\]

and hence

\[
0<q<u_0<u.
\]

---

# IX. Left boundary recurrence in Case II

## 17. Equation from \(E0\)

For

\[
0<t<q,
\]

the point

\[
b+t
=
d_0+(u_0+t)
\]

lies in the copy interval (M2), so

\[
f(b+t)
=
\beta H(u_0+t).
\]

For

\[
q<t<u,
\]

the point \(b+t\) lies in the zero interval (Z1).

Therefore (E0) gives

\[
\boxed{
U(t)
=
\gamma H(t)
-
\beta^2H(t+u_0),
\qquad
0<t<q,
}
\tag{L1}
\]

and

\[
\boxed{
U(t)=\gamma H(t),
\qquad
q<t<u.
}
\tag{L2}
\]

---

# X. Right boundary recurrence in Case II

## 18. Equation from \(ER\)

For

\[
0<t<u_0,
\]

we have

\[
s+t<r,
\]

and (Z2) gives

\[
f(s+t)=0.
\]

Hence

\[
\boxed{
U(t)=-\gamma H(t),
\qquad
0<t<u_0.
}
\tag{R1}
\]

For

\[
u_0<t<u,
\]

write

\[
t=u_0+\tau,
\qquad
0<\tau<q.
\]

Then

\[
s+t=r+\tau.
\]

By (M1),

\[
f(s+t)
=
-\beta H(\tau)
=
-\beta H(t-u_0).
\]

Therefore (ER) gives

\[
\boxed{
U(t)
=
-\gamma H(t)
+
\beta^2H(t-u_0),
\qquad
u_0<t<u.
}
\tag{R2}
\]

---

# XI. The middle interval dies

## 19. Compare \(L2\) and \(R1\)

Because

\[
q<u_0,
\]

the interval

\[
(q,u_0)
\]

is nonempty.

There,

\[
U(t)=\gamma H(t)
\]

from (L2), while

\[
U(t)=-\gamma H(t)
\]

from (R1).

Hence

\[
\boxed{
H(t)=0
\quad
\text{for }q<t<u_0.
}
\tag{Z5}
\]

---

# XII. The two gain recurrences are incompatible

## 20. Lower-to-upper relation

For

\[
0<t<q,
\]

compare (L1) and (R1):

\[
\gamma H(t)
-
\beta^2H(t+u_0)
=
-\gamma H(t).
\]

Thus

\[
\boxed{
\beta^2H(t+u_0)
=
2\gamma H(t).
}
\tag{G1}
\]

---

## 21. Upper-to-lower relation

Now take

\[
t\in(u_0,u).
\]

Write

\[
t=u_0+\tau,
\qquad
0<\tau<q.
\]

Compare (L2) and (R2):

\[
\gamma H(t)
=
-\gamma H(t)
+
\beta^2H(\tau).
\]

Therefore

\[
\boxed{
2\gamma H(t)
=
\beta^2H(t-u_0).
}
\tag{G2}
\]

In particular, for

\[
0<\tau<q,
\]

\[
\boxed{
2\gamma H(\tau+u_0)
=
\beta^2H(\tau).
}
\tag{G2'}
\]

---

## 22. Consistency condition

Equations (G1) and (G2') give, for

\[
0<t<q,
\]

\[
H(t+u_0)
=
\frac{2\gamma}{\beta^2}H(t)
\]

and also

\[
H(t+u_0)
=
\frac{\beta^2}{2\gamma}H(t).
\]

Therefore any nonzero \(H(t)\) would require

\[
\boxed{
\beta^2=2\gamma.
}
\]

We now show this is impossible.

---

# XIII. Exact gain mismatch

## 23. Compute \(\gamma\)

Because

\[
C=\frac{\log2}{2},
\qquad
A=\frac{\log2}{\sqrt2},
\]

we have

\[
\boxed{
\gamma=\frac1{\sqrt2}.
}
\]

Hence

\[
\boxed{
2\gamma=\sqrt2.
}
\]

---

## 24. Lower bound for \(\beta^2\)

We have

\[
\boxed{
\beta^2
=
\frac{B^2}{A^2}
=
\frac23
\left(
\frac{\log3}{\log2}
\right)^2.
}
\]

Since

\[
9>8,
\]

we have

\[
3>2^{3/2},
\]

hence

\[
\frac{\log3}{\log2}
>
\frac32.
\]

Therefore

\[
\boxed{
\beta^2
>
\frac23\cdot\frac94
=
\frac32.
}
\]

But

\[
\boxed{
\sqrt2<\frac32.
}
\]

Thus

\[
\boxed{
\beta^2> \frac32>\sqrt2=2\gamma.
}
\]

In particular,

\[
\beta^2\ne2\gamma.
\]

So (G1)--(G2') force

\[
H=0
\quad
\text{on }(0,q)
\]

and hence on

\[
(u_0,u)
\]

as well.

Together with (Z5),

\[
\boxed{
H=0
\quad
\text{on }(0,u).
}
\]

Thus again

\[
\boxed{
f=0.
}
\]

---

# XIV. Ambient prime translation kernel through log5

## 25. Post-log4 result

Both cases give

\[
\boxed{
\ker\mathsf P_c
=
\{0\}
\qquad
(\log4<L\le\log5).
}
\]

At

\[
L=\log4,
\]

GERM-29 already proved the same statement.

Therefore

\[
\boxed{
\ker\mathsf P_c
=
\{0\}
\qquad
(\log4\le L\le\log5).
}
\]

---

# XV. Combined classification through log5

## 26. Join the previous regimes

For

\[
0<L\le\log2,
\]

the regular kernel itself is trivial by the small-window input.

For

\[
\log2<L<\log4,
\]

GERM-28--29 give the ambient prime kernel

\[
L^2(L-\log2,\log2)
\]

with zero intersection with \(K_c\).

For

\[
\log4\le L\le\log5,
\]

the ambient prime translation operator is injective.

Hence the prime-silent regular kernel satisfies

\[
\boxed{
K_c^{\rm ps}
=
\{0\}
\qquad
(0<L\le\log5).
}
\]

This extends prime-silent triviality through the entire next prime threshold.

---

# XVI. Fixed-scale prime coercivity through log5

## 27. Regular-kernel consequence

For every

\[
0<L\le\log5
\]

with

\[
K_c\ne0,
\]

the restriction

\[
\mathsf P_c|_{K_c}
\]

is injective.

Since \(K_c\) is finite dimensional,

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

Again, this is a fixed-scale theorem.

No uniformity in \(c\) and no shrinking-collar rate are asserted.

---

# XVII. What changes after log5

## 28. New prime base

For

\[
L>\log5,
\]

the new delay

\[
\log5
\]

enters.

The translation operator then contains at least

\[
\log2,\ \log3,\ \log4,\ \log5.
\]

The boundary-fiber pattern changes again.

In particular, the \(\log5\)-channel creates additional relations between the
head fiber and interior copies that are not present in the three-delay
calculation above.

No classification beyond \(\log5\) is asserted here.

---

# XVIII. Result of this NF pass

The feared post-\(\log4\) ambient cancellation modes do **not** appear before
the next prime threshold.

For

\[
\boxed{
\log4<L\le\log5,
}
\]

the active three-delay translation equation has only the zero solution:

\[
\boxed{
\ker\mathsf P_c=\{0\}.
}
\]

The proof is a complete boundary-fiber reduction to one head fiber \(H\),
followed by two incompatible gain recurrences.

Therefore:

\[
\boxed{
K_c^{\rm ps}=\{0\}
\qquad
(0<L\le\log5).
}
\]

Prime-channel fixed-scale coercivity on the regular kernel now persists
through the \(\log5\) threshold.

This is the strongest positive prime-custody result in the GERM chain so far.

---

# XIX. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-31 / POST-LOG5 PRIME-SILENT FIBERS}.
}
\]

The next pass should add the \(\log5\) delay and test whether the boundary
fiber method continues to force ambient injectivity.

The immediate questions are:

1. whether the new \(5\)-channel creates a genuine gain resonance;
2. whether the source can still be reduced to finitely many short boundary
   fibers;
3. whether ambient prime injectivity persists to the next threshold
   \[
   \log7;
   \]
4. whether a reusable induction principle over successive prime-power
   thresholds can be extracted.

No post-\(\log5\) result is asserted in this pass.

---

# XX. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified post-\(\log4\) prime-translation injectivity result.

No public promotion and no canonical cursor movement are asserted.
