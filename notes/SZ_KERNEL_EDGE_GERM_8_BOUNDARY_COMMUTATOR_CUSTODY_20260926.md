# SZ-KERNEL-EDGE-GERM-8 — Boundary-commutator custody and the no-raw-descent theorem

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-7  
**Target tested:** BOUNDARY-COMMUTATOR CUSTODY  
**Public promotion:** forbidden

## 0. Objective

GERM-7 identified the failure of whole-line arithmetic translation invariance
with support truncation and a boundary-strip commutator.

This pass determines what that commutator can and cannot do.

The main conclusion is stronger than expected:

\[
\boxed{
\text{for every }0<\ell\le\log2,\;
K_c\text{ has no nonzero subspace invariant under }
T_{\ell,c}=P_c\tau_\ell E_c.
}
\]

In particular, for the first prime delay

\[
\ell=\log2,
\]

neither the stabilized flat space \(F_\infty\) nor the persistence space
\(P_c^+\) can be invariant under the raw truncated translation unless that
space is zero.

Therefore the raw first-prime translation cannot descend to a nonzero edge
quotient by the usual invariant-subspace construction.

Any viable arithmetic action on

\[
\mathcal E_c=F_\infty/P_c^+
\]

must be **corrected** by a nontrivial boundary/persistence term.

This converts the boundary commutator from a nuisance term into a mandatory
load-bearing object.

The pass also sharpens GERM-7's global formula: the commutator is the sole
defect only on the interior core where the shifted evaluation remains inside
the old support.  On the opposite entry strip there is an additional shifted
old-exterior residual.

---

# I. Source pin: the \(\log2\) positivity window

## 1. Bombieri--Yoshida small-support positivity

Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
numbers, I* (2000), reports that Yoshida reduced fixed-window positivity to a
finite calculation and verified positivity at

\[
\boxed{
t=\frac{\log2}{2}.
}
\]

Bombieri's Theorem 12 also proves positivity for functions supported in an
interval of length

\[
|I|<\log2.
\]

Thus the classical localized Weil form is positive definite throughout the
strict no-prime interval and at the Yoshida boundary needed here.

Via the already-established Suzuki bridge, the corresponding regular screw
zero kernel is trivial:

\[
\boxed{
K_a=\ker G_a=\{0\}
\qquad
\left(
0<a\le\frac{\log2}{2}
\right).
}
\]

**Ratification guard:** this classical source statement is externally pinned
here but has not yet been added as a dedicated canonical source note on the
current branch.  Any later ratification of the present pass should source-pin
this dependency explicitly.

---

# II. Truncated translations are nilpotent

## 2. Definition

Let

\[
H_c=L^2(-c,c),
\]

with zero extension

\[
E_c:H_c\to L^2(\mathbb R)
\]

and restriction

\[
P_c:L^2(\mathbb R)\to H_c.
\]

For

\[
\ell>0,
\]

define

\[
\boxed{
T_{\ell,c}=P_c\tau_\ell E_c,
}
\]

where

\[
(\tau_\ell f)(y)=f(y-\ell).
\]

Thus

\[
(T_{\ell,c}u)(y)
=
u(y-\ell)
\]

when the shifted point remains in the old interval, and is zero otherwise.

---

## 3. Nilpotence

Repeated application shifts the source to the right:

\[
T_{\ell,c}^k
=
P_c\tau_{k\ell}E_c
\]

on the surviving support.

Hence

\[
\boxed{
T_{\ell,c}^N=0
\qquad
\text{whenever }
N\ell\ge2c.
}
\]

So every fixed positive truncated translation is nilpotent.

---

# III. Kernel of one truncated shift

## 4. Exact support description

If

\[
T_{\ell,c}u=0,
\]

then

\[
u(z)=0
\]

for almost every

\[
z\in(-c,c-\ell).
\]

Therefore

\[
\boxed{
\ker T_{\ell,c}
=
L^2(c-\ell,c)
}
\]

as a subspace of \(H_c\), up to null endpoints.

Thus any vector killed by the translation is supported in the discarded
right boundary strip of width \(\ell\).

---

# IV. Recentring a strip-supported kernel vector

## 5. Boundary strip

Assume

\[
0<\ell\le\log2
\]

and suppose

\[
0\ne u\in K_c
\]

also satisfies

\[
T_{\ell,c}u=0.
\]

Then

\[
\operatorname{supp}u
\subseteq
(c-\ell,c).
\]

Set

\[
a=\frac{\ell}{2},
\qquad
y_0=c-a,
\]

and define the recentered source

\[
w(r)
=
u(y_0+r),
\qquad
-a<r<a.
\]

---

## 6. Potential identity

Let

\[
F_w(\xi)
=
\int_{-a}^{a}
g(\xi-r)w(r)\,dr.
\]

Changing variables gives

\[
F_w(\xi)
=
F_u(y_0+\xi),
\]

because \(u\) has no source outside the boundary strip.

For

\[
|\xi|<a,
\]

we have

\[
y_0+\xi
\in
(c-\ell,c)
\subset
(-c,c).
\]

Since

\[
u\in K_c,
\]

its screw potential is constant on the whole old interval:

\[
F_u(x)=C_u
\qquad
(|x|<c).
\]

Therefore

\[
\boxed{
F_w(\xi)=C_u
\qquad
(|\xi|<a).
}
\]

Hence

\[
\boxed{
w\in K_a.
}
\]

---

## 7. Small-window positivity kills the strip source

Because

\[
a=\frac{\ell}{2}
\le
\frac{\log2}{2},
\]

the Bombieri--Yoshida positive window gives

\[
K_a=\{0\}.
\]

Thus

\[
w=0,
\]

hence

\[
u=0,
\]

contradiction.

Therefore

\[
\boxed{
K_c\cap\ker T_{\ell,c}
=
\{0\}
\qquad
(0<\ell\le\log2).
}
\]

---

# V. No invariant kernel subspace

## 8. Theorem

Let

\[
V\subseteq K_c
\]

be a subspace satisfying

\[
T_{\ell,c}V\subseteq V
\]

for some

\[
0<\ell\le\log2.
\]

If \(V\ne0\), then the nilpotent operator

\[
T_{\ell,c}|_V
\]

has nontrivial kernel.

Thus there exists

\[
0\ne u\in V
\]

with

\[
T_{\ell,c}u=0.
\]

But Section IV gives

\[
K_c\cap\ker T_{\ell,c}=\{0\}.
\]

Contradiction.

Hence

\[
\boxed{
T_{\ell,c}V\subseteq V
\Longrightarrow
V=\{0\}
\qquad
(0<\ell\le\log2).
}
\]

This applies to arbitrary subspaces of the finite-dimensional regular kernel.

---

# VI. Consequences for the stabilized spaces

## 9. Flat space

Since

\[
F_\infty\subseteq K_c,
\]

if

\[
T_{\ell,c}F_\infty
\subseteq
F_\infty
\]

for any

\[
0<\ell\le\log2,
\]

then

\[
\boxed{
F_\infty=\{0\}.
}
\]

Therefore a nonzero superflat family cannot be invariant under any such raw
truncated translation.

---

## 10. Persistence space

Likewise,

\[
P_c^+\subseteq K_c.
\]

Thus

\[
T_{\ell,c}P_c^+
\subseteq
P_c^+
\]

implies

\[
\boxed{
P_c^+=\{0\}.
}
\]

So the persistence space itself is not naturally stable under the raw
truncated shift unless it is trivial.

---

# VII. No raw quotient descent

## 11. Ordinary quotient criterion

For a linear operator \(T\) to descend in the standard way to

\[
F_\infty/P_c^+,
\]

one requires at least

\[
T(F_\infty)\subseteq F_\infty
\]

and

\[
T(P_c^+)\subseteq P_c^+.
\]

For

\[
T=T_{\ell,c},
\qquad
0<\ell\le\log2,
\]

the first condition alone forces

\[
F_\infty=0.
\]

Therefore:

\[
\boxed{
\text{the raw truncated translation cannot descend to a nonzero }
\mathcal E_c.
}
\]

In particular this applies at the first prime delay

\[
\boxed{
\ell=\log2.
}
\]

Thus GERM-7's desired arithmetic quotient action cannot be obtained by simply
showing that the first-prime boundary commutator vanishes.

If it vanished strongly enough to restore raw invariance, there would be no
edge obstruction left.

---

# VIII. Precision correction to GERM-7

## 12. Exact global identity

GERM-7 derived

\[
F_{T_{\ell,c}u}(x)
=
F_u(x-\ell)
-
B_{\ell,+}u(x),
\]

with

\[
B_{\ell,+}u(x)
=
\int_{c-\ell}^{c}
g(x-\ell-z)u(z)\,dz.
\]

This identity is global.

However, for a kernel vector \(u\), the simplification

\[
F_u(x-\ell)=C_u
\]

holds only when

\[
x-\ell\in(-c,c),
\]

that is,

\[
x\in(-c+\ell,c+\ell).
\]

Inside the target interval \((-c,c)\), this gives the **core zone**

\[
\boxed{
-c+\ell<x<c.
}
\]

There,

\[
\boxed{
F_{T_{\ell,c}u}(x)
=
C_u-B_{\ell,+}u(x).
}
\]

---

## 13. Entry zone

On the left entry strip

\[
-c<x<-c+\ell,
\]

the shifted point

\[
x-\ell
\]

lies outside the old support interval.

Write

\[
x=-c+s,
\qquad
0<s<\ell.
\]

Then

\[
x-\ell
=
-c-(\ell-s).
\]

Therefore

\[
F_u(x-\ell)
=
C_u+r_-(\ell-s),
\]

where

\[
r_-(\delta)
=
F_u(-c-\delta)-C_u
\]

is the old left exterior residual.

Hence

\[
\boxed{
F_{T_{\ell,c}u}(-c+s)
=
C_u
+
r_-(\ell-s)
-
B_{\ell,+}u(-c+s).
}
\]

So the global failure of \(T_{\ell,c}u\) to remain a kernel vector has two
pieces:

1. on the core zone: the boundary-strip commutator;
2. on the entry zone: the boundary-strip commutator **plus the shifted old
   exterior residual**.

Thus the broad phrase

\[
\text{arithmetic invariance defect}
=
\text{boundary-strip commutator}
\]

from GERM-7 is exact only on the core zone.

The global custody statement must include the entry residual.

This is a scope correction, not a change to GERM-7's local commutator formula.

---

# IX. The commutator is itself a smaller-support screw potential

## 14. Recenter the discarded strip

Again set

\[
a=\frac{\ell}{2},
\qquad
y_0=c-a,
\]

and define

\[
w(r)
=
u(y_0+r),
\qquad
-a<r<a.
\]

Then

\[
B_{\ell,+}u(x)
=
\int_{-a}^{a}
g\bigl((x-c-a)-r\bigr)w(r)\,dr.
\]

Therefore

\[
\boxed{
B_{\ell,+}u(x)
=
F_w(x-c-a).
}
\]

So the boundary commutator is exactly the ordinary screw potential of the
discarded boundary-strip source, viewed in shifted coordinates.

---

## 15. Edge interpretation

At the original right endpoint

\[
x=c,
\]

the smaller coordinate is

\[
x-c-a=-a,
\]

the **left endpoint** of the recentered strip.

Thus variations of

\[
B_{\ell,+}u
\]

near the original endpoint are precisely edge variations of the
smaller-support strip potential near its left endpoint.

This identifies the previous blind-germ analysis with the commutator:

\[
\boxed{
\text{blind prime germ}
=
\text{edge germ of the discarded-strip potential}.
}
\]

The commutator is therefore a compressed copy of the original edge problem,
but its strip source need not itself lie in the smaller kernel unless the
strong condition \(T_{\ell,c}u=0\) holds.

---

# X. What the first-prime commutator must do

## 16. Minimal prime translation

Take

\[
\ell=\log2.
\]

If

\[
F_\infty\ne0,
\]

then by Section VI

\[
\boxed{
T_{\log2,c}F_\infty
\not\subseteq
F_\infty.
}
\]

Therefore there exists a superflat kernel vector whose first-prime truncated
translate leaves the stabilized flat space.

Hence the first-prime boundary/entry defect is necessarily load-bearing on
any nonzero obstruction.

It cannot be discarded as:

- zero;
- automatically persistent;
- or a harmless invariant correction.

---

# XI. Corrected rather than raw translation

## 17. The only remaining descent mechanism

Since raw translation invariance is impossible, a quotient action—if one
exists—must have the form

\[
\boxed{
\widehat T_{\ell,c}
=
T_{\ell,c}
-
C_{\ell,c},
}
\]

where

\[
C_{\ell,c}
\]

is a nontrivial correction built from boundary and/or persistence data.

To act on

\[
\mathcal E_c,
\]

one would need

\[
\widehat T_{\ell,c}(F_\infty)
\subseteq
F_\infty
\]

and

\[
\widehat T_{\ell,c}(P_c^+)
\subseteq
P_c^+.
\]

The correction cannot vanish identically on a nonzero flat space.

Thus the remaining problem is naturally a finite-dimensional lifting or
cohomology problem:

\[
\boxed{
\text{can the boundary defect be absorbed by a canonical persistent
correction without destroying the arithmetic moment spectrum?}
}
\]

---

# XII. Result of this NF pass

The boundary-commutator route is now sharply constrained.

For every

\[
0<\ell\le\log2,
\]

\[
\boxed{
K_c
\text{ has no nonzero }T_{\ell,c}\text{-invariant subspace}.
}
\]

Therefore:

\[
\boxed{
\text{raw truncated translation cannot act on a nonzero edge quotient}.
}
\]

At the first prime delay,

\[
\ell=\log2,
\]

this uses exactly the Yoshida/Bombieri small-support positivity boundary.

The commutator is not lower-order residue that one hopes to eliminate.
It is mathematically forced whenever a nonzero obstruction exists.

Moreover:

\[
\boxed{
B_{\ell,+}u
=
\text{smaller-support screw potential of the discarded strip},
}
\]

so the blind-germ chain is precisely the local edge manifestation of support
translation failure.

The correct next problem is not raw invariance but **corrected invariance
modulo persistence**.

---

# XIII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-9 / PERSISTENT-CORRECTION LIFT}.
}
\]

The next pass should test whether there is a canonical finite-dimensional
correction

\[
C_{\ell,c}
\]

constructed from:

- the persistence projection;
- the one-sided Schur reconstruction;
- or the boundary-strip screw potential,

such that

\[
\widehat T_{\ell,c}
=
T_{\ell,c}-C_{\ell,c}
\]

preserves \(F_\infty\) and \(P_c^+\).

The decisive requirement is that the correction preserve enough of the simple
arithmetic moment spectrum from GERM-7 to retain the finite-dimensional
rigidity theorem.

A positive result could close

\[
\mathcal E_c=0.
\]

A negative result would show that support custody, rather than
quasi-analyticity, is the terminal obstruction of this route.

No corrected lift is constructed in this pass.

---

# XIV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified structural/custody result.

No public promotion and no canonical cursor movement are asserted.
