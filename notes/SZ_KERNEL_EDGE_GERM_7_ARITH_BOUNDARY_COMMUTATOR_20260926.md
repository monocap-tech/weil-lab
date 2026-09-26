# SZ-KERNEL-EDGE-GERM-7 — Arithmetic moment spectrum and boundary-commutator closure

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-6  
**Target tested:** MOMENT-DILATION CLOSURE  
**Public promotion:** forbidden

## 0. Objective

GERM-6 showed that a constant-coefficient recurrence in the archimedean moment
index would force the local \(L^2\) source to vanish.

It then asked whether the arithmetic dilation algebra could somehow be
converted into moment-index shift closure.

That conversion is not needed.

The actual von-Mangoldt weighted translation operator already has a simple
diagonal spectrum on the archimedean moment lattice.  Its eigenvalues are
strictly separated.  Consequently:

\[
\boxed{
\text{finite-dimensional invariance under the arithmetic translation operator}
\Longrightarrow
\text{zero source family}.
}
\]

Thus arithmetic invariance itself would kill the edge obstruction.

The reason this does not immediately close the Weil problem is now exact:
the regular screw kernel is defined on a **truncated support interval**.

Full-line translations commute with convolution, but support
restriction/zero-extension do not commute with translation.

The resulting commutator is an explicit boundary-strip operator.

Therefore the remaining problem is no longer
"dilation versus moment shift."

It is:

\[
\boxed{
\text{BOUNDARY-COMMUTATOR CUSTODY}.
}
\]

---

# I. Archimedean moments

## 1. Moment lattice

Let

\[
I\Subset(0,\infty)
\]

and let

\[
f\in L^2(I),
\]

extended by zero to the whole line.

For

\[
m\ge1,
\]

set

\[
\lambda_m
=
2m+\frac12
\]

and

\[
\boxed{
M_m(f)
=
\int_{\mathbb R}
e^{-\lambda_m s}f(s)\,ds.
}
\]

GERM-2 proved that the tail family

\[
\{M_m:m\ge1\}
\]

separates compactly supported \(L^2\) sources away from the origin.

---

# II. Weighted arithmetic translations

## 2. One translation

For

\[
\ell>0,
\]

define the whole-line translation

\[
(\tau_\ell f)(s)
=
f(s-\ell).
\]

Then

\[
\boxed{
M_m(\tau_\ell f)
=
e^{-\lambda_m\ell}M_m(f).
}
\]

For

\[
\ell=\log n,
\]

this becomes

\[
M_m(\tau_{\log n}f)
=
n^{-(2m+1/2)}M_m(f).
\]

---

## 3. Weil-weighted arithmetic operator

Let

\[
H
\]

be a nonempty finite set of prime powers and define

\[
\boxed{
\mathfrak D_H
=
\sum_{n\in H}
\frac{\Lambda(n)}{\sqrt n}
\tau_{\log n}.
}
\]

Then

\[
\boxed{
M_m(\mathfrak D_Hf)
=
\alpha_m(H)M_m(f),
}
\]

where

\[
\boxed{
\alpha_m(H)
=
\sum_{n\in H}
\frac{\Lambda(n)}{n^{2m+1}}.
}
\]

Every summand is positive.

Hence

\[
\alpha_m(H)>0
\]

and

\[
\boxed{
\alpha_{m+1}(H)<\alpha_m(H)
}
\]

for every \(m\ge1\).

Thus the moment eigenvalues are pairwise distinct.

---

## 4. Full arithmetic spectrum

Formally, with all prime powers included,

\[
\alpha_m
=
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{2m+1}}.
\]

For \(m\ge1\), the series is absolutely convergent and the classical
Dirichlet-series identity gives

\[
\boxed{
\alpha_m
=
-\frac{\zeta'}{\zeta}(2m+1).
}
\]

Since

\[
2m+1>1,
\]

we also have directly from the positive Dirichlet series

\[
\boxed{
-\frac{\zeta'}{\zeta}(2m+1)>0.
}
\]

The sequence is strictly decreasing in \(m\).

The finite-\(H\) version is sufficient for the rigidity theorem below and
avoids any global support issue.

---

# III. Finite-dimensional arithmetic-invariance rigidity

## 5. Moment image

Let

\[
V
\]

be a finite-dimensional subspace of compactly supported \(L^2\) sources on
which the moment map is injective.

Set

\[
W
=
\mathcal M(V)
=
\{
(M_1(f),M_2(f),\ldots):
f\in V
\}.
\]

Suppose

\[
\boxed{
\mathfrak D_HV\subseteq V.
}
\]

Then \(W\) is invariant under the diagonal sequence operator

\[
A_H
=
\operatorname{diag}
(\alpha_1(H),\alpha_2(H),\ldots).
\]

---

## 6. Minimal-polynomial argument

Because \(W\) is finite dimensional,

\[
A_H|_W
\]

has a nonzero minimal polynomial

\[
P.
\]

Thus

\[
P(A_H)w=0
\qquad
(w\in W).
\]

Coordinatewise,

\[
\boxed{
P(\alpha_m(H))\,w_m=0
\qquad
\forall m\ge1.
}
\]

The values

\[
\alpha_m(H)
\]

are pairwise distinct.

A nonzero polynomial has only finitely many roots.

Therefore every

\[
w\in W
\]

has only finitely many possibly nonzero coordinates.

Hence, for the corresponding source \(f\),

\[
M_m(f)=0
\]

for all sufficiently large \(m\).

By the same polynomial-density argument used in GERM-2 and GERM-6, vanishing
of the moment tail forces

\[
f=0.
\]

Thus

\[
W=\{0\}
\]

and

\[
\boxed{
V=\{0\}.
}
\]

We have proved:

\[
\boxed{
\mathfrak D_HV\subseteq V
\quad\Longrightarrow\quad
V=\{0\}.
}
\]

---

# IV. Consequence for the edge program

## 7. Stronger than moment-shift closure

GERM-6 showed that shift invariance

\[
S\mathcal M(V)\subseteq\mathcal M(V)
\]

would force \(V=0\).

The present theorem is stronger in project relevance:

\[
\boxed{
\text{invariance under the actual weighted prime-translation operator}
\Longrightarrow
V=0.
}
\]

No conversion to the moment shift is required.

Thus the true closure target is simply to show that the finite edge-defect
source family is invariant under a suitable nonzero arithmetic translation
operator.

---

# V. Why full-line invariance would be natural

## 8. Translation-invariant convolution

Let

\[
C_g
\]

denote whole-line convolution by the screw kernel or by its differentiated
distributional kernel, in whichever normalized form is being used.

Whole-line convolution commutes with translations:

\[
\boxed{
C_g\tau_\ell
=
\tau_\ell C_g.
}
\]

Hence any full-line nullspace of a translation-invariant convolution operator
is automatically invariant under every translation and therefore under every
finite arithmetic combination

\[
\mathfrak D_H.
\]

Combined with Section III, a finite-dimensional compact-source full-line
nullspace of this kind would have to vanish.

The actual Weil kernel escapes this immediate argument only because it is a
**truncated-support kernel**.

---

# VI. Truncated translations

## 9. Support operators

Let

\[
H_c=L^2(-c,c).
\]

Write

\[
E_c:
H_c\to L^2(\mathbb R)
\]

for zero extension and

\[
P_c:
L^2(\mathbb R)\to H_c
\]

for restriction.

For

\[
0<\ell<2c,
\]

define the truncated positive translation

\[
\boxed{
T_{\ell,c}
=
P_c\tau_\ell E_c.
}
\]

Explicitly,

\[
(T_{\ell,c}u)(y)
=
u(y-\ell)
\]

when

\[
y-\ell\in(-c,c)
\]

and is zero otherwise.

---

# VII. Exact boundary commutator

## 10. Potential of a truncated translate

Let

\[
u\in K_c=\ker G_c
\]

and define

\[
F_u(x)
=
\int_{-c}^{c}
g(x-y)u(y)\,dy.
\]

For

\[
T_{\ell,c}u,
\]

we have

\[
F_{T_{\ell,c}u}(x)
=
\int_{-c}^{c}
g(x-y)
u(y-\ell)\,dy.
\]

Set

\[
z=y-\ell.
\]

The condition

\[
y\in(-c,c)
\]

becomes

\[
z\in(-c-\ell,c-\ell),
\]

while \(u(z)\) is supported only on

\[
(-c,c).
\]

Therefore

\[
\boxed{
F_{T_{\ell,c}u}(x)
=
\int_{-c}^{c-\ell}
g(x-\ell-z)u(z)\,dz.
}
\]

Add and subtract the missing right boundary strip:

\[
F_{T_{\ell,c}u}(x)
=
F_u(x-\ell)
-
\int_{c-\ell}^{c}
g(x-\ell-z)u(z)\,dz.
\]

Hence

\[
\boxed{
F_{T_{\ell,c}u}(x)
=
F_u(x-\ell)
-
B_{\ell,+}u(x),
}
\]

where

\[
\boxed{
B_{\ell,+}u(x)
=
\int_{c-\ell}^{c}
g(x-\ell-z)u(z)\,dz.
}
\]

This is the exact right-boundary commutator term.

---

## 11. Kernel-vector specialization

If

\[
x-\ell\in(-c,c),
\]

then

\[
F_u(x-\ell)=C_u.
\]

Therefore

\[
\boxed{
F_{T_{\ell,c}u}(x)
=
C_u
-
B_{\ell,+}u(x).
}
\]

Thus \(T_{\ell,c}u\) is again a kernel vector on the relevant interior region
if and only if the boundary-strip potential

\[
B_{\ell,+}u(x)
\]

is constant there.

The failure of arithmetic invariance is **exactly** the boundary strip

\[
(c-\ell,c).
\]

---

# VIII. Mirror boundary commutator

## 12. Negative translation

For

\[
T_{-\ell,c}
=
P_c\tau_{-\ell}E_c,
\]

the analogous calculation discards the left boundary strip

\[
(-c,-c+\ell).
\]

One obtains

\[
\boxed{
F_{T_{-\ell,c}u}(x)
=
F_u(x+\ell)
-
B_{\ell,-}u(x),
}
\]

with

\[
\boxed{
B_{\ell,-}u(x)
=
\int_{-c}^{-c+\ell}
g(x+\ell-z)u(z)\,dz.
}
\]

Hence the two support commutators are carried entirely by the two boundary
strips.

---

# IX. Weighted arithmetic commutator

## 13. Finite prime family

For a nonempty finite prime-power set \(H\), define the truncated arithmetic
operator

\[
\boxed{
\mathfrak D_{H,c}
=
\sum_{n\in H}
\frac{\Lambda(n)}{\sqrt n}
T_{\log n,c}.
}
\]

Then, on an interior region where every translated center remains in
\((-c,c)\),

\[
\boxed{
F_{\mathfrak D_{H,c}u}(x)
=
\left(
\sum_{n\in H}
\frac{\Lambda(n)}{\sqrt n}
\right)C_u
-
\mathfrak B_{H,+}u(x),
}
\]

where

\[
\boxed{
\mathfrak B_{H,+}
=
\sum_{n\in H}
\frac{\Lambda(n)}{\sqrt n}
B_{\log n,+}.
}
\]

Thus the entire failure of the arithmetic operator to preserve \(K_c\) is
encoded by a finite weighted boundary-strip potential.

---

# X. Conditional quotient closure

## 14. Exact sufficient condition

Let

\[
E_c\simeq\mathcal E_c
\]

be a finite-dimensional representative of the edge obstruction.

Suppose there exists a nonempty finite prime-power set \(H\) such that:

1. the truncated arithmetic operator maps the stabilized flat family into
   itself modulo persistence;
2. equivalently, on the quotient,
   \[
   [\mathfrak D_{H,c}]:
   \mathcal E_c\to\mathcal E_c
   \]
   is well defined;
3. the induced quotient action has the same arithmetic moment multiplier
   \[
   \alpha_m(H)
   \]
   on a separating compact-source moment chart.

Then Section III forces

\[
\boxed{
\mathcal E_c=0.
}
\]

Therefore arithmetic quotient invariance is a complete sufficient edge
rigidity criterion.

---

# XI. Why current superflatness does not supply it

## 15. Boundary strips are exactly the dangerous region

The right boundary commutator depends on

\[
u|_{(c-\ell,c)}.
\]

The left boundary commutator depends on

\[
u|_{(-c,-c+\ell)}.
\]

These are not harmless bulk regions.

They contain:

- the physical endpoints;
- edge singular sites;
- and, depending on \(\ell\), several prime-hinge neighborhoods.

The ratified edge package explicitly allows a nonzero superflat obstruction to
remain locally nontrivial at such sites.

Therefore superflat collar leakage does **not** imply

\[
B_{\ell,\pm}u=0
\]

or even that the boundary commutator is persistent.

So quotient invariance is not yet proved.

---

# XII. Reinterpretation of the preceding edge work

## 16. What the blind-germ chain was measuring

GERM-1 through GERM-4 can now be read as increasingly precise analyses of the
support-translation commutator:

- blind hinge germs are local pieces of the boundary loss;
- one-sided observability reconstructs the lost strip from visible data;
- movable-center reachability tracks how boundary-strip information can be
  re-entered through smaller delays;
- the logarithmic diagonal appears when trying to reconstruct the commutator
  locally.

Thus the boundary commutator is not a new obstruction unrelated to the
previous chain.

It is the operator-theoretic compression of that chain.

---

# XIII. Result of this NF pass

The moment-dilation problem has a stronger solution than the moment-shift
route suggested in GERM-6.

For every nonempty finite arithmetic family \(H\),

\[
\boxed{
M_m(\mathfrak D_Hf)
=
\alpha_m(H)M_m(f),
\qquad
\alpha_{m+1}(H)<\alpha_m(H).
}
\]

Hence

\[
\boxed{
\text{finite-dimensional arithmetic invariance}
\Longrightarrow
\text{zero source family}.
}
\]

For the full prime family,

\[
\boxed{
\alpha_m
=
-\frac{\zeta'}{\zeta}(2m+1).
}
\]

The Weil kernel fails to inherit this full-line rigidity only because support
truncation breaks translation invariance.

That failure is exact:

\[
\boxed{
\text{arithmetic invariance defect}
=
\text{boundary-strip commutator}.
}
\]

Therefore the remaining edge obstruction is now concentrated in one operator
interface rather than a diffuse quasi-analyticity problem.

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-8 / BOUNDARY-COMMUTATOR CUSTODY}.
}
\]

The next pass should determine whether, on the stabilized flat quotient,

\[
\mathfrak B_{H,\pm}
\]

is:

1. persistent;
2. lower rank than the full edge obstruction;
3. triangular under the prime-delay ordering;
4. expressible through the one-sided Schur reconstruction of GERM-3;
5. or capable of descending to zero after quotienting by \(P_c^+\).

Any nonzero arithmetic operator whose boundary commutator vanishes on
\(\mathcal E_c\) would force

\[
\mathcal E_c=0
\]

by the arithmetic-invariance theorem of this pass.

No such quotient commutator vanishing is proved here.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified structural/closure-criterion residue.

No public promotion and no canonical cursor movement are asserted.
