# SZ-KERNEL-EDGE-GERM-4 — Movable-center reachability and the diagonal obstruction

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-3  
**Target tested:** SCHUR RECONSTRUCTION REGULARITY  
**Public promotion:** forbidden

## 0. Objective

GERM-3 proved that one-sided visible half-collars determine the entire regular
kernel

\[
K_c=\ker G_c
\]

and that the blind halves are finite-dimensional Schur reconstructions of the
visible data.

The natural next attempt is to exploit the fact that

\[
F_u(x)=C_u
\qquad
(|x|<c)
\]

at **every** interior center, not merely near the two endpoints.

One might hope to move the center into the interval until an outward-blind
edge germ becomes visible through another prime delay, thereby producing a
triangular reconstruction of the blind halves.

This pass shows exactly how far that idea works.

The result has two parts:

1. arithmetic prime-delay reachability is indeed triangular when the active
   delays are ordered by length;
2. every movable-center equation simultaneously introduces the
   archimedean diagonal singularity at the new center.

Thus prime recentering does not close a finite Schur system by itself.

The smallest active prime hinge has no arithmetic predecessor at all, so the
irreducible core is necessarily archimedean/diagonal.

---

# I. Centered identity at an arbitrary interior point

## 1. Movable center

Let

\[
u\in K_c
\]

and let

\[
x\in(-c,c).
\]

Set

\[
d(x)=c-|x|.
\]

For every

\[
0<\delta<d(x),
\]

both

\[
x-\delta,\qquad x+\delta
\]

remain in the old interval.

Since

\[
F_u\equiv C_u
\]

there,

\[
F_u(x+\delta)+F_u(x-\delta)-2F_u(x)=0.
\]

Therefore

\[
\boxed{
0
=
\int_{-c}^{c}
\Delta_\delta^2 g(x-y)\,u(y)\,dy,
}
\]

where

\[
\Delta_\delta^2g(t)
=
g(t+\delta)+g(t-\delta)-2g(t).
\]

This is the movable-center version of the centered identity from GERM-1.

No differentiation of \(u\) or of a flat collar residual is used.

---

# II. Prime part at a movable center

## 2. Even prime hinge

For a prime power \(n\), write

\[
\ell=\log n,
\qquad
a_\ell=\frac{\Lambda(n)}{\sqrt n}.
\]

The corresponding even prime hinge is

\[
h_\ell(t)
=
a_\ell(|t|-\ell)_+.
\]

For

\[
0<\delta<\ell,
\]

the two singular points \(t=\pm\ell\) are separated.

A direct calculation gives

\[
\boxed{
\Delta_\delta^2 h_\ell(t)
=
a_\ell
\left[
(\delta-|t-\ell|)_+
+
(\delta-|t+\ell|)_+
\right].
}
\]

Hence at interior center \(x\), the prime contribution is

\[
\boxed{
a_\ell
\int_{-c}^{c}
\left[
(\delta-|y-(x-\ell)|)_+
+
(\delta-|y-(x+\ell)|)_+
\right]
u(y)\,dy.
}
\]

Thus one prime delay probes two compact tent moments centered at

\[
x-\ell
\qquad\text{and}\qquad
x+\ell.
\]

Whenever one center lies outside \((-c,c)\), that tent contributes nothing
after zero extension.

---

# III. Boundary-linked blind site and geometric shielding

## 3. Right-edge prime site

Fix an active interior prime delay

\[
0<\ell<2c
\]

and its right-edge physical singular site

\[
\boxed{
y_\ell=c-\ell.
}
\]

GERM-1 identified the interval immediately to the right of \(y_\ell\) as the
outward-blind half for the right-edge inward motion.

Move the center to

\[
x=c-h,
\qquad
h>0.
\]

The same prime branch has its left tent center at

\[
x-\ell
=
y_\ell-h.
\]

The admissibility condition for the centered identity is

\[
0<\delta<h.
\]

Therefore the support of that tent lies in

\[
(y_\ell-h-\delta,\;y_\ell-h+\delta).
\]

Since

\[
\delta<h,
\]

we have

\[
y_\ell-h+\delta<y_\ell.
\]

Thus

\[
\boxed{
\text{the same prime branch never crosses }y_\ell
\text{ while the center remains interior}.
}
\]

No amount of recentering through \(x\uparrow c\) lets the \(\ell\)-branch
directly sample the outward-blind half

\[
(y_\ell,y_\ell+\rho).
\]

This is a geometric shielding lemma.

The blind half is not an artifact of choosing the endpoint as the original
center.

---

# IV. Reachability by a different prime delay

## 4. Smaller delays can reach a larger-hinge blind point

Take a point

\[
y=y_\ell+t
=
c-\ell+t
\]

with

\[
t>0
\]

small.

Let

\[
\lambda
\]

be another active prime delay.

To make \(y\) appear as the left-shift sample

\[
x-\lambda=y,
\]

choose

\[
x=y+\lambda
=
c-\ell+t+\lambda.
\]

This center lies inside the old interval on the right precisely when

\[
x<c,
\]

that is,

\[
\boxed{
\lambda<\ell-t.
}
\]

Hence, for sufficiently small \(t\),

\[
\boxed{
\lambda<\ell
\Longrightarrow
\text{the }\lambda\text{-delay can reach the blind side of the }\ell\text{-site}.
}
\]

Conversely,

\[
\lambda\ge\ell
\]

cannot reach points immediately to the right of \(y_\ell\) through a
right-interior center of this form.

Thus arithmetic reachability of boundary blind sites is ordered by prime-delay
length.

---

## 5. Directed delay graph

Order the active prime delays

\[
0<\ell_1<\ell_2<\cdots<\ell_N<2c.
\]

Define a directed reachability relation

\[
\ell_j\longrightarrow\ell_k
\]

when the \(\ell_j\)-delay can sample the outward-blind side of the
\(\ell_k\)-edge site by an interior recentering.

For sufficiently small local collars,

\[
\boxed{
\ell_j\longrightarrow\ell_k
\quad\Longleftrightarrow\quad
\ell_j<\ell_k.
}
\]

Therefore the prime-delay reachability graph is acyclic and strictly
triangular in the ordered delays.

This is the triangular structure sought in GERM-3.

---

# V. The minimal-hinge core

## 6. Smallest active arithmetic delay

If

\[
2c>\log2,
\]

the smallest possible active prime-power delay is

\[
\boxed{
\ell_{\min}=\log2.
}
\]

Its right-edge physical site is

\[
y_{\min}=c-\log2.
\]

There is no positive prime-power delay

\[
\lambda<\log2.
\]

Therefore the outward-blind half of the \(\log2\) site has no arithmetic
predecessor in the movable-center reachability graph.

Thus

\[
\boxed{
\text{the minimal prime blind germ cannot be recovered by prime recentering}.
}
\]

If

\[
2c\le\log2,
\]

there are no active interior prime hinges at all.

In that regime the edge problem is already purely archimedean at the level of
nonanalytic local carriers.

---

# VI. Why triangular reachability still does not close

## 7. The new center carries the archimedean diagonal singularity

Suppose a smaller delay

\[
\lambda<\ell
\]

is used to reach a blind point

\[
y=c-\ell+t
\]

through the interior center

\[
x=y+\lambda.
\]

The same movable-center identity contains the archimedean contribution

\[
\int_{-c}^{c}
\Delta_\delta^2 a_\infty(x-z)u(z)\,dz.
\]

Suzuki's local expansion gives, near the origin,

\[
a_\infty(\tau)
=
\frac12|\tau|\log|\tau|
+
\text{lower singular/regular terms}.
\]

Therefore the centered archimedean kernel is nonanalytic at

\[
z=x.
\]

So the recentered equation introduces a new local singular germ of \(u\) near

\[
\boxed{
z=x=y+\lambda.
}
\]

This point generally is not one of the finite edge singular sites
\(\Sigma_c\).

Hence the operation

\[
\text{use smaller prime delay to expose an edge blind germ}
\]

simultaneously performs

\[
\text{introduce a new logarithmic diagonal germ at the movable center}.
\]

The finite edge-germ system is not closed under recentering.

---

## 8. Continuum of possible diagonal centers

As

\[
y
\]

varies through a blind interval and

\[
\lambda
\]

is fixed, the center

\[
x=y+\lambda
\]

varies through an interval.

Therefore the newly introduced archimedean diagonal germ is not confined to a
new finite set of sites.

It sweeps a continuum of interior centers.

Thus a naive elimination scheme based only on the ordered prime delays would
replace the finite blind-germ problem by a continuum local-principal problem.

That is not a valid finite Schur closure.

---

# VII. Relation to existing form-domain control

## 9. What is currently ratified

The canonical bridge provides a logarithmic form-domain estimate of the form

\[
\int_{\mathbb R}
\log(e+|t|)
|\widehat f(t)|^2\,dt<\infty
\]

for the relevant closed form carrier.

This gives logarithmic form control.

It explicitly does **not** provide a positive-Sobolev bootstrap.

Therefore current canonical regularity is insufficient to replace the new
diagonal germ by a pointwise trace, finite Taylor jet, or analytic local
coefficient.

No triangular prime-delay argument may silently assume such regularity.

---

# VIII. Sharp status of the Schur-reconstruction attempt

## 10. What succeeds

The movable-center analysis proves:

\[
\boxed{
\text{prime-delay reachability is strictly lower-triangular in }\ell.
}
\]

Consequently every nonminimal prime blind side is arithmetically reachable
through at least one smaller active delay.

This is genuine structure in the Schur reconstruction.

---

## 11. What fails

The same recentering necessarily creates an uncontrolled archimedean
diagonal channel.

Therefore

\[
\boxed{
\text{triangular prime reachability}
\not\Rightarrow
\text{triangular Schur reconstruction}.
}
\]

The obstruction is not another arithmetic cycle.

It is the logarithmic diagonal principal species.

---

# IX. Refined obstruction hierarchy

## 12. Three layers

The remaining endpoint problem now has a natural hierarchy.

### Layer 1 — prime edge geometry

Finite, ordered, and triangular:

\[
\ell_1<\cdots<\ell_N.
\]

### Layer 2 — blind-half reconstruction

Nonminimal blind halves are reachable by smaller prime delays.

The minimal prime blind half is not.

### Layer 3 — archimedean diagonal

Every movable-center reconstruction couples to the local logarithmic principal
germ at the center.

This layer is continuous in the center variable and is not removed by the
current logarithmic form-domain estimate.

Thus the deepest surviving obstruction is

\[
\boxed{
\text{MINIMAL-HINGE / LOG-DIAGONAL CORE}.
}
\]

---

# X. Consequence for the edge quotient

## 13. What a nonzero superflat obstruction must do

If

\[
\mathcal E_c\ne0,
\]

then after GERM-3 and the present pass:

1. its kernel representatives are determined by one-sided visible data;
2. every nonminimal prime blind component is connected to a smaller-delay
   interior equation;
3. any attempt to eliminate those components generates logarithmic diagonal
   germs;
4. the minimal prime blind component, when present, has no arithmetic
   predecessor;
5. when no prime hinge is active, only the archimedean diagonal/endpoint
   mechanism remains.

Therefore a flat-but-leaking class cannot be sustained by a closed finite
prime-delay subsystem alone.

It must use the logarithmic principal species essentially.

---

# XI. Result of this NF pass

The Schur-reconstruction regularity problem does not close by movable-center
prime elimination.

The exact new statements are:

\[
\boxed{
\ell_j\to\ell_k
\iff
\ell_j<\ell_k
}
\]

for local arithmetic reachability of right-edge blind germs;

\[
\boxed{
\text{the minimal active prime hinge has no arithmetic predecessor};
}
\]

and

\[
\boxed{
\text{every movable-center elimination imports a new archimedean diagonal
germ}.
}
\]

Hence the prime part is triangular, but the full Weil system is not reduced to
a finite triangular matrix by this maneuver.

The remaining load-bearing object is the local logarithmic diagonal operator.

---

# XII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-5 / LOG-DIAGONAL BOOTSTRAP}.
}
\]

The next pass should test the strongest regularity that follows from the
interior logarithmic principal equation without assuming positive Sobolev
control.

Natural subtargets are:

1. derive local iterated logarithmic regularity from the principal
   logarithmic operator;
2. determine whether all-logarithmic-order regularity is enough to control the
   Schur reconstruction;
3. construct a countermodel if intersection of all logarithmic domains still
   admits infinitely-flat local germs;
4. isolate any additional arithmetic/zero-side input needed beyond the
   logarithmic principal species.

No such bootstrap is proved in this pass.

---

# XIII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified NF structural/no-go result.

No public promotion and no canonical cursor movement are asserted.
